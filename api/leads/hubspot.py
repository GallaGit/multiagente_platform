"""HubSpot CRM client for lead orchestration."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

import httpx

from api.config import get_settings
from api.leads.models import (
    HubSpotContactProperties,
    LeadEstado,
    LeadMetricsResponse,
    LeadResponse,
    OwnerResponse,
)

HUBSPOT_BASE = "https://api.hubapi.com"

CUSTOM_PROPERTIES = [
    {
        "name": "lead_origen",
        "label": "Lead origen",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
    {
        "name": "lead_origen_ref",
        "label": "Lead origen ref",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
    {
        "name": "inmueble_ref",
        "label": "Inmueble ref",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
    {
        "name": "lead_estado",
        "label": "Lead estado",
        "type": "enumeration",
        "fieldType": "select",
        "groupName": "contactinformation",
        "options": [
            {"label": "Nuevo", "value": "nuevo"},
            {"label": "Asignado", "value": "asignado"},
            {"label": "En seguimiento", "value": "en_seguimiento"},
            {"label": "Excepcion", "value": "excepcion"},
            {"label": "Cerrado corto", "value": "cerrado_corto"},
        ],
    },
    {
        "name": "siguiente_accion",
        "label": "Siguiente accion",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
    {
        "name": "sla_primera_respuesta_at",
        "label": "SLA primera respuesta",
        "type": "datetime",
        "fieldType": "date",
        "groupName": "contactinformation",
    },
    {
        "name": "primera_respuesta_at",
        "label": "Primera respuesta",
        "type": "datetime",
        "fieldType": "date",
        "groupName": "contactinformation",
    },
    {
        "name": "exception_code",
        "label": "Codigo excepcion",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
    {
        "name": "dedupe_key",
        "label": "Dedupe key",
        "type": "string",
        "fieldType": "text",
        "groupName": "contactinformation",
    },
]

LEAD_PROPERTY_NAMES = [
    "email",
    "phone",
    "firstname",
    "hubspot_owner_id",
    "createdate",
    "lastmodifieddate",
    "lead_origen",
    "lead_origen_ref",
    "inmueble_ref",
    "lead_estado",
    "siguiente_accion",
    "sla_primera_respuesta_at",
    "primera_respuesta_at",
    "exception_code",
    "dedupe_key",
]


class HubSpotError(Exception):
    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


def normalize_email(email: str | None) -> str | None:
    if not email:
        return None
    cleaned = email.strip().lower()
    return cleaned or None


def normalize_phone(phone: str | None) -> str | None:
    if not phone:
        return None
    digits = re.sub(r"\D", "", phone)
    if not digits:
        return None
    if len(digits) == 9 and not digits.startswith("34"):
        digits = f"34{digits}"
    return f"+{digits}"


def compute_dedupe_key(email: str | None, telefono: str | None) -> str | None:
    normalized_email = normalize_email(email)
    if normalized_email:
        return f"email:{normalized_email}"
    normalized_phone = normalize_phone(telefono)
    if normalized_phone:
        return f"phone:{normalized_phone}"
    return None


def _parse_hubspot_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if value.isdigit():
            ms = int(value)
            return datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def _to_hubspot_datetime(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    ms = int(dt.timestamp() * 1000)
    return str(ms)


class HubSpotClient:
    def __init__(self, access_token: str | None = None) -> None:
        settings = get_settings()
        self.access_token = access_token or settings.hubspot_access_token
        self.verify_ssl = settings.hubspot_verify_ssl
        if not self.access_token:
            raise HubSpotError("HUBSPOT_ACCESS_TOKEN no configurado")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        url = f"{HUBSPOT_BASE}{path}"
        with httpx.Client(timeout=30.0, verify=self.verify_ssl) as client:
            response = client.request(
                method,
                url,
                headers=self._headers(),
                json=json,
                params=params,
            )
        if response.status_code >= 400:
            detail = response.text[:500]
            raise HubSpotError(
                f"HubSpot API error {response.status_code}: {detail}",
                status_code=response.status_code,
            )
        if response.status_code == 204 or not response.content:
            return {}
        return response.json()

    def ensure_custom_properties(self) -> list[str]:
        created: list[str] = []
        for prop in CUSTOM_PROPERTIES:
            name = prop["name"]
            try:
                self._request("GET", f"/crm/v3/properties/contacts/{name}")
            except HubSpotError as exc:
                if exc.status_code != 404:
                    raise
                self._request(
                    "POST",
                    "/crm/v3/properties/contacts",
                    json=prop,
                )
                created.append(name)
        return created

    def list_owners(self) -> list[OwnerResponse]:
        data = self._request("GET", "/crm/v3/owners", params={"limit": 100})
        owners: list[OwnerResponse] = []
        for item in data.get("results", []):
            owners.append(
                OwnerResponse(
                    id=str(item.get("id", "")),
                    email=item.get("email"),
                    first_name=item.get("firstName"),
                    last_name=item.get("lastName"),
                )
            )
        return owners

    def search_contact_by_email(self, email: str) -> dict[str, Any] | None:
        normalized = normalize_email(email)
        if not normalized:
            return None
        payload = {
            "filterGroups": [
                {
                    "filters": [
                        {
                            "propertyName": "email",
                            "operator": "EQ",
                            "value": normalized,
                        }
                    ]
                }
            ],
            "properties": LEAD_PROPERTY_NAMES,
            "limit": 1,
        }
        data = self._request("POST", "/crm/v3/objects/contacts/search", json=payload)
        results = data.get("results", [])
        return results[0] if results else None

    def search_contact_by_phone(self, phone: str) -> dict[str, Any] | None:
        normalized = normalize_phone(phone)
        if not normalized:
            return None
        payload = {
            "filterGroups": [
                {
                    "filters": [
                        {
                            "propertyName": "phone",
                            "operator": "CONTAINS_TOKEN",
                            "value": normalized.replace("+", ""),
                        }
                    ]
                }
            ],
            "properties": LEAD_PROPERTY_NAMES,
            "limit": 1,
        }
        data = self._request("POST", "/crm/v3/objects/contacts/search", json=payload)
        results = data.get("results", [])
        return results[0] if results else None

    def find_existing_contact(
        self, email: str | None, telefono: str | None
    ) -> dict[str, Any] | None:
        if email:
            found = self.search_contact_by_email(email)
            if found:
                return found
        if telefono:
            return self.search_contact_by_phone(telefono)
        return None

    def create_contact(self, properties: HubSpotContactProperties) -> dict[str, Any]:
        payload = {"properties": properties.model_dump(exclude_none=True)}
        return self._request("POST", "/crm/v3/objects/contacts", json=payload)

    def update_contact(
        self, contact_id: str, properties: HubSpotContactProperties
    ) -> dict[str, Any]:
        payload = {"properties": properties.model_dump(exclude_none=True)}
        return self._request(
            "PATCH",
            f"/crm/v3/objects/contacts/{contact_id}",
            json=payload,
        )

    def get_contact(self, contact_id: str) -> dict[str, Any]:
        params = {"properties": ",".join(LEAD_PROPERTY_NAMES)}
        return self._request("GET", f"/crm/v3/objects/contacts/{contact_id}", params=params)

    def create_task(
        self,
        *,
        contact_id: str,
        subject: str,
        body: str,
        due_at: datetime,
        owner_id: str | None = None,
    ) -> dict[str, Any]:
        properties: dict[str, Any] = {
            "hs_task_subject": subject,
            "hs_task_body": body,
            "hs_task_status": "NOT_STARTED",
            "hs_timestamp": _to_hubspot_datetime(due_at),
        }
        if owner_id:
            properties["hubspot_owner_id"] = owner_id
        payload = {
            "properties": properties,
            "associations": [
                {
                    "to": {"id": contact_id},
                    "types": [
                        {
                            "associationCategory": "HUBSPOT_DEFINED",
                            "associationTypeId": 204,
                        }
                    ],
                }
            ],
        }
        return self._request("POST", "/crm/v3/objects/tasks", json=payload)

    def list_contacts(
        self,
        *,
        estado: str | None = None,
        exception_code: str | None = None,
        limit: int = 100,
        mvp_only: bool = True,
    ) -> list[dict[str, Any]]:
        filters: list[dict[str, Any]] = []
        if mvp_only:
            filters.append(
                {
                    "propertyName": "lead_origen",
                    "operator": "HAS_PROPERTY",
                }
            )
        if estado:
            filters.append(
                {
                    "propertyName": "lead_estado",
                    "operator": "EQ",
                    "value": estado,
                }
            )
        if exception_code:
            filters.append(
                {
                    "propertyName": "exception_code",
                    "operator": "EQ",
                    "value": exception_code,
                }
            )

        if filters:
            payload = {
                "filterGroups": [{"filters": filters}],
                "properties": LEAD_PROPERTY_NAMES,
                "sorts": [{"propertyName": "createdate", "direction": "DESCENDING"}],
                "limit": min(limit, 100),
            }
            data = self._request("POST", "/crm/v3/objects/contacts/search", json=payload)
            return data.get("results", [])

        params = {
            "limit": min(limit, 100),
            "properties": ",".join(LEAD_PROPERTY_NAMES),
        }
        data = self._request("GET", "/crm/v3/objects/contacts", params=params)
        return data.get("results", [])

    def contact_to_lead(
        self,
        contact: dict[str, Any],
        *,
        owners_map: dict[str, OwnerResponse] | None = None,
        is_duplicate: bool = False,
    ) -> LeadResponse:
        props = contact.get("properties", {})
        owner_id = props.get("hubspot_owner_id")
        owner_name = None
        if owner_id and owners_map and owner_id in owners_map:
            owner = owners_map[owner_id]
            parts = [owner.first_name or "", owner.last_name or ""]
            owner_name = " ".join(p for p in parts if p).strip() or owner.email

        estado_raw = props.get("lead_estado") or LeadEstado.NUEVO.value
        try:
            estado = LeadEstado(estado_raw)
        except ValueError:
            estado = LeadEstado.NUEVO

        return LeadResponse(
            lead_id=str(contact.get("id", "")),
            nombre=props.get("firstname"),
            email=props.get("email"),
            telefono=props.get("phone"),
            origen=props.get("lead_origen"),
            origen_ref=props.get("lead_origen_ref"),
            inmueble_ref=props.get("inmueble_ref"),
            responsable_id=owner_id,
            responsable_nombre=owner_name,
            estado=estado,
            siguiente_accion=props.get("siguiente_accion"),
            sla_primera_respuesta_at=_parse_hubspot_datetime(
                props.get("sla_primera_respuesta_at")
            ),
            primera_respuesta_at=_parse_hubspot_datetime(
                props.get("primera_respuesta_at")
            ),
            exception_code=props.get("exception_code") or None,
            dedupe_key=props.get("dedupe_key"),
            created_at=_parse_hubspot_datetime(props.get("createdate")),
            updated_at=_parse_hubspot_datetime(props.get("lastmodifieddate")),
            is_duplicate=is_duplicate,
        )

    @staticmethod
    def _median_response_minutes(leads: list[LeadResponse]) -> float | None:
        deltas: list[float] = []
        for lead in leads:
            if lead.created_at and lead.primera_respuesta_at:
                minutes = (
                    lead.primera_respuesta_at - lead.created_at
                ).total_seconds() / 60
                if minutes >= 0:
                    deltas.append(minutes)
        if len(deltas) < 2:
            return None
        deltas.sort()
        mid = len(deltas) // 2
        if len(deltas) % 2 == 1:
            return round(deltas[mid], 1)
        return round((deltas[mid - 1] + deltas[mid]) / 2, 1)

    def build_metrics(self, leads: list[LeadResponse]) -> LeadMetricsResponse:
        total = len(leads)
        if total == 0:
            return LeadMetricsResponse(
                total_leads=0,
                pct_con_responsable=0.0,
                pct_con_siguiente_accion=0.0,
                excepciones_abiertas=0,
                sla_rotos=0,
                mediana_tiempo_respuesta_min=None,
            )

        with_owner = sum(1 for lead in leads if lead.responsable_id)
        with_action = sum(1 for lead in leads if lead.siguiente_accion)
        exceptions = sum(
            1 for lead in leads if lead.estado == LeadEstado.EXCEPCION and lead.exception_code
        )
        now = datetime.now(timezone.utc)
        sla_broken = sum(
            1
            for lead in leads
            if lead.sla_primera_respuesta_at
            and lead.sla_primera_respuesta_at < now
            and not lead.primera_respuesta_at
            and lead.estado != LeadEstado.CERRADO_CORTO
        )

        return LeadMetricsResponse(
            total_leads=total,
            pct_con_responsable=round(with_owner / total * 100, 1),
            pct_con_siguiente_accion=round(with_action / total * 100, 1),
            excepciones_abiertas=exceptions,
            sla_rotos=sla_broken,
            mediana_tiempo_respuesta_min=self._median_response_minutes(leads),
        )
