"""Lead orchestration: validation, dedupe, assignment, SLA, tasks."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from api.config import get_settings
from api.leads.hubspot import (
    HubSpotClient,
    HubSpotError,
    _to_hubspot_datetime,
    compute_dedupe_key,
    normalize_email,
    normalize_phone,
)
from api.leads.models import (
    ExceptionCode,
    HubSpotContactProperties,
    IngestResult,
    LeadEstado,
    LeadIngestRequest,
    LeadResponse,
    LeadUpdateRequest,
    OwnerResponse,
)


@dataclass
class RoundRobinState:
    owner_ids: list[str]
    index: int = 0

    def next_owner(self) -> str | None:
        if not self.owner_ids:
            return None
        owner_id = self.owner_ids[self.index % len(self.owner_ids)]
        self.index += 1
        return owner_id


_round_robin = RoundRobinState(owner_ids=[])


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _sla_deadline(minutes: int | None = None) -> datetime:
    settings = get_settings()
    delta = minutes if minutes is not None else settings.sla_minutes
    return _utcnow() + timedelta(minutes=delta)


def _default_siguiente_accion(mensaje: str | None) -> str:
    if mensaje:
        return f"Llamar — {mensaje[:120]}"
    return "Llamar para cualificar interes"


def _resolve_owner_ids(client: HubSpotClient) -> list[str]:
    settings = get_settings()
    if settings.round_robin_owner_ids:
        return settings.round_robin_owner_ids

    global _round_robin
    if not _round_robin.owner_ids:
        owners = client.list_owners()
        _round_robin.owner_ids = [owner.id for owner in owners if owner.id]
    return _round_robin.owner_ids


def pick_next_owner(client: HubSpotClient) -> str | None:
    owner_ids = _resolve_owner_ids(client)
    if not owner_ids:
        return None
    global _round_robin
    _round_robin.owner_ids = owner_ids
    return _round_robin.next_owner()


def reset_round_robin(owner_ids: list[str] | None = None) -> None:
    global _round_robin
    if owner_ids is not None:
        _round_robin = RoundRobinState(owner_ids=owner_ids)
    else:
        _round_robin = RoundRobinState(owner_ids=[])


def ingest_lead(
    payload: LeadIngestRequest,
    client: HubSpotClient | None = None,
) -> IngestResult:
    hubspot = client or HubSpotClient()
    settings = get_settings()

    email = normalize_email(payload.email)
    phone = normalize_phone(payload.telefono)
    dedupe_key = compute_dedupe_key(email, phone)
    nombre = (payload.nombre or "").strip() or "Desconocido"

    if not email and not phone:
        props = HubSpotContactProperties(
            firstname=nombre,
            lead_origen=payload.origen,
            lead_origen_ref=payload.origen_ref,
            inmueble_ref=payload.inmueble_ref,
            lead_estado=LeadEstado.EXCEPCION.value,
            exception_code=ExceptionCode.DATOS_INSUFICIENTES.value,
            dedupe_key=dedupe_key,
        )
        try:
            contact = hubspot.create_contact(props)
        except HubSpotError as exc:
            raise HubSpotError(
                f"{ExceptionCode.SYNC_FALLIDO.value}: {exc}",
                status_code=exc.status_code,
            ) from exc
        lead = hubspot.contact_to_lead(contact)
        return IngestResult(
            lead=lead,
            action="exception",
            message="Lead sin email ni telefono — cola de excepcion",
        )

    existing = hubspot.find_existing_contact(email, phone)
    sla_at = _sla_deadline(settings.sla_minutes)
    siguiente = _default_siguiente_accion(payload.mensaje)

    if existing:
        contact_id = str(existing["id"])
        existing_owner = existing.get("properties", {}).get("hubspot_owner_id")
        props = HubSpotContactProperties(
            email=email,
            phone=phone,
            firstname=nombre,
            lead_origen=payload.origen,
            lead_origen_ref=payload.origen_ref,
            inmueble_ref=payload.inmueble_ref,
            lead_estado=LeadEstado.EN_SEGUIMIENTO.value,
            siguiente_accion=siguiente,
            sla_primera_respuesta_at=_to_hubspot_datetime(sla_at),
            exception_code="",
            dedupe_key=dedupe_key,
            hubspot_owner_id=existing_owner,
        )
        try:
            contact = hubspot.update_contact(contact_id, props)
            hubspot.create_task(
                contact_id=contact_id,
                subject="Solicitud de contacto (duplicado)",
                body=payload.mensaje or "Lead recurrente desde canal",
                due_at=sla_at,
                owner_id=existing_owner,
            )
        except HubSpotError as exc:
            raise HubSpotError(
                f"{ExceptionCode.SYNC_FALLIDO.value}: {exc}",
                status_code=exc.status_code,
            ) from exc

        lead = hubspot.contact_to_lead(contact, is_duplicate=True)
        return IngestResult(
            lead=lead,
            action="duplicate",
            message="Contacto existente actualizado; no se creo segundo responsable",
        )

    owner_id = pick_next_owner(hubspot)
    if not owner_id:
        props = HubSpotContactProperties(
            email=email,
            phone=phone,
            firstname=nombre,
            lead_origen=payload.origen,
            lead_origen_ref=payload.origen_ref,
            inmueble_ref=payload.inmueble_ref,
            lead_estado=LeadEstado.EXCEPCION.value,
            exception_code=ExceptionCode.SIN_DUENO.value,
            dedupe_key=dedupe_key,
        )
        try:
            contact = hubspot.create_contact(props)
        except HubSpotError as exc:
            raise HubSpotError(
                f"{ExceptionCode.SYNC_FALLIDO.value}: {exc}",
                status_code=exc.status_code,
            ) from exc
        lead = hubspot.contact_to_lead(contact)
        return IngestResult(
            lead=lead,
            action="exception",
            message="Sin owners disponibles en HubSpot",
        )

    props = HubSpotContactProperties(
        email=email,
        phone=phone,
        firstname=nombre,
        hubspot_owner_id=owner_id,
        lead_origen=payload.origen,
        lead_origen_ref=payload.origen_ref,
        inmueble_ref=payload.inmueble_ref,
        lead_estado=LeadEstado.ASIGNADO.value,
        siguiente_accion=siguiente,
        sla_primera_respuesta_at=_to_hubspot_datetime(sla_at),
        exception_code="",
        dedupe_key=dedupe_key,
    )
    try:
        contact = hubspot.create_contact(props)
        contact_id = str(contact["id"])
        hubspot.create_task(
            contact_id=contact_id,
            subject="Primera respuesta lead",
            body=payload.mensaje or "Nuevo lead desde canal",
            due_at=sla_at,
            owner_id=owner_id,
        )
    except HubSpotError as exc:
        raise HubSpotError(
            f"{ExceptionCode.SYNC_FALLIDO.value}: {exc}",
            status_code=exc.status_code,
        ) from exc

    owners_map = _owners_map(hubspot)
    lead = hubspot.contact_to_lead(contact, owners_map=owners_map)
    return IngestResult(
        lead=lead,
        action="created",
        message="Lead creado con responsable y tarea",
    )


def _owners_map(client: HubSpotClient) -> dict[str, OwnerResponse]:
    return {owner.id: owner for owner in client.list_owners()}


def list_leads(
    client: HubSpotClient | None = None,
    *,
    estado: str | None = None,
    exception_code: str | None = None,
    limit: int = 100,
) -> list[LeadResponse]:
    hubspot = client or HubSpotClient()
    contacts = hubspot.list_contacts(
        estado=estado,
        exception_code=exception_code,
        limit=limit,
    )
    owners = _owners_map(hubspot)
    leads = [
        hubspot.contact_to_lead(contact, owners_map=owners)
        for contact in contacts
    ]
    leads.sort(
        key=lambda item: item.created_at or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return leads


def list_exceptions(client: HubSpotClient | None = None) -> list[LeadResponse]:
    leads = list_leads(client, estado=LeadEstado.EXCEPCION.value)
    return [lead for lead in leads if lead.exception_code]


def compute_metrics(client: HubSpotClient | None = None):
    hubspot = client or HubSpotClient()
    leads = list_leads(hubspot)
    return hubspot.build_metrics(leads)


def update_lead(
    lead_id: str,
    payload: LeadUpdateRequest,
    client: HubSpotClient | None = None,
) -> LeadResponse:
    hubspot = client or HubSpotClient()
    props = HubSpotContactProperties()
    if payload.estado:
        props.lead_estado = payload.estado.value
    if payload.exception_code is not None:
        props.exception_code = payload.exception_code
    if payload.siguiente_accion:
        props.siguiente_accion = payload.siguiente_accion
    if payload.responsable_id:
        props.hubspot_owner_id = payload.responsable_id
    if payload.primera_respuesta_at:
        props.primera_respuesta_at = _to_hubspot_datetime(payload.primera_respuesta_at)
        if payload.estado is None:
            props.lead_estado = LeadEstado.EN_SEGUIMIENTO.value

    contact = hubspot.update_contact(lead_id, props)
    owners = _owners_map(hubspot)
    return hubspot.contact_to_lead(contact, owners_map=owners)
