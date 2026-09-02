"""Tests for lead orchestration with mocked HubSpot client."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
from fastapi.testclient import TestClient

from api.leads.hubspot import HubSpotError, compute_dedupe_key, normalize_email, normalize_phone
from api.leads.models import LeadEstado, LeadIngestRequest, LeadUpdateRequest
from api.leads.orchestrator import (
    enrich_lead_operational,
    ingest_lead,
    list_exceptions,
    reset_round_robin,
    update_lead,
)


class FakeHubSpotClient:
    def __init__(self) -> None:
        self.contacts: dict[str, dict[str, Any]] = {}
        self.tasks: list[dict[str, Any]] = []
        self._seq = 0
        self.owners = [
            {"id": "owner-1", "email": "a@demo.com", "firstName": "Ana", "lastName": "Demo"},
            {"id": "owner-2", "email": "b@demo.com", "firstName": "Bruno", "lastName": "Demo"},
        ]

    def _next_id(self) -> str:
        self._seq += 1
        return str(self._seq)

    def list_owners(self):
        from api.leads.models import OwnerResponse

        return [
            OwnerResponse(
                id=o["id"],
                email=o["email"],
                first_name=o["firstName"],
                last_name=o["lastName"],
            )
            for o in self.owners
        ]

    def find_existing_contact(
        self,
        email: str | None,
        telefono: str | None,
        origen: str | None = None,
        origen_ref: str | None = None,
    ):
        for contact in self.contacts.values():
            props = contact["properties"]
            if email and props.get("email") == normalize_email(email):
                return contact
            if telefono and props.get("phone") == normalize_phone(telefono):
                return contact
        if origen and origen_ref:
            for contact in self.contacts.values():
                props = contact["properties"]
                if (
                    props.get("lead_origen") == origen
                    and props.get("lead_origen_ref") == origen_ref
                ):
                    return contact
        return None

    def create_contact(self, properties):
        contact_id = self._next_id()
        props = properties.model_dump(exclude_none=True)
        now = datetime.now(timezone.utc).isoformat()
        contact = {
            "id": contact_id,
            "properties": {
                **props,
                "createdate": now,
                "lastmodifieddate": now,
            },
        }
        self.contacts[contact_id] = contact
        return contact

    def update_contact(self, contact_id: str, properties):
        contact = self.contacts[contact_id]
        contact["properties"].update(properties.model_dump(exclude_none=True))
        contact["properties"]["lastmodifieddate"] = datetime.now(timezone.utc).isoformat()
        return contact

    def create_task(self, **kwargs):
        self.tasks.append(kwargs)
        return {"id": self._next_id()}

    def list_contacts(self, **kwargs):
        estado = kwargs.get("estado")
        results = []
        for contact in self.contacts.values():
            props = contact["properties"]
            if kwargs.get("mvp_only", True) and not props.get("lead_origen"):
                continue
            if estado and props.get("lead_estado") != estado:
                continue
            if kwargs.get("exception_code") and props.get("exception_code") != kwargs["exception_code"]:
                continue
            results.append(contact)
        return results

    def list_contacts_with_exception_code(self, mvp_only=True, **kwargs):
        results = []
        for contact in self.contacts.values():
            props = contact["properties"]
            if not props.get("exception_code"):
                continue
            if mvp_only and not props.get("lead_origen"):
                continue
            results.append(contact)
        return results

    def contact_to_lead(self, contact, owners_map=None, is_duplicate=False):
        from api.leads.hubspot import HubSpotClient

        real = HubSpotClient.__new__(HubSpotClient)
        return HubSpotClient.contact_to_lead(real, contact, owners_map=owners_map, is_duplicate=is_duplicate)

    def build_metrics(self, leads):
        from api.leads.hubspot import HubSpotClient

        real = HubSpotClient.__new__(HubSpotClient)
        return HubSpotClient.build_metrics(real, leads)


@pytest.fixture(autouse=True)
def reset_rr():
    reset_round_robin(["owner-1", "owner-2"])
    yield
    reset_round_robin([])


def test_normalize_contact_fields():
    assert normalize_email("  Ana@Example.COM ") == "ana@example.com"
    assert normalize_phone("612345678") == "+34612345678"
    assert compute_dedupe_key("a@b.com", None) == "email:a@b.com"


def test_ingest_new_lead_assigns_owner_and_task():
    client = FakeHubSpotClient()
    payload = LeadIngestRequest(
        nombre="Ana Ejemplo",
        email="ana@example.com",
        telefono="612345678",
        origen="portal",
        origen_ref="IDEALISTA-001",
        inmueble_ref="REF-001",
        mensaje="Interesada en visitar",
    )
    result = ingest_lead(payload, client)  # type: ignore[arg-type]

    assert result.action == "created"
    assert result.lead.estado == LeadEstado.ASIGNADO
    assert result.lead.responsable_id == "owner-1"
    assert result.lead.siguiente_accion
    assert len(client.tasks) == 1
    assert client.tasks[0]["owner_id"] == "owner-1"


def test_ingest_duplicate_keeps_same_owner():
    client = FakeHubSpotClient()
    first = LeadIngestRequest(
        nombre="Ana Ejemplo",
        email="ana@example.com",
        telefono="612345678",
        mensaje="Primera consulta",
    )
    ingest_lead(first, client)  # type: ignore[arg-type]

    second = LeadIngestRequest(
        nombre="Ana Ejemplo",
        email="ana@example.com",
        telefono="612345678",
        mensaje="Segunda consulta",
    )
    result = ingest_lead(second, client)  # type: ignore[arg-type]

    assert result.action == "duplicate"
    assert result.lead.is_duplicate is True
    assert result.lead.responsable_id == "owner-1"
    assert len(client.contacts) == 1
    assert len(client.tasks) == 2


def test_ingest_insufficient_data_exception():
    client = FakeHubSpotClient()
    payload = LeadIngestRequest(nombre="Sin datos", origen="web")
    result = ingest_lead(payload, client)  # type: ignore[arg-type]

    assert result.action == "exception"
    assert result.lead.estado == LeadEstado.EXCEPCION
    assert result.lead.exception_code == "DATOS_INSUFICIENTES"
    assert result.lead.responsable_id is None
    assert len(client.tasks) == 0


def test_leads_api_503_without_hubspot_token(monkeypatch):
    monkeypatch.setenv("HUBSPOT_ACCESS_TOKEN", "")
    from api.config import get_settings

    get_settings.cache_clear()

    from api.main import app

    with TestClient(app) as test_client:
        response = test_client.get("/leads")
        assert response.status_code == 503

    get_settings.cache_clear()


def test_ingest_duplicate_by_origen_ref():
    client = FakeHubSpotClient()
    first = LeadIngestRequest(
        nombre="Evento A",
        email="evento.a@example.com",
        origen="portal",
        origen_ref="EVT-100",
    )
    ingest_lead(first, client)  # type: ignore[arg-type]

    second = LeadIngestRequest(
        nombre="Evento A repetido",
        email="otro@example.com",
        origen="portal",
        origen_ref="EVT-100",
    )
    result = ingest_lead(second, client)  # type: ignore[arg-type]

    assert result.action == "duplicate"
    assert len(client.contacts) == 1


def test_ingest_phone_dedupe():
    client = FakeHubSpotClient()
    ingest_lead(
        LeadIngestRequest(
            nombre="Ana",
            email="ana.phone@example.com",
            telefono="612345678",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    result = ingest_lead(
        LeadIngestRequest(
            nombre="Ana",
            email="ana.phone@example.com",
            telefono="612345678",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    assert result.action == "duplicate"
    assert len(client.contacts) == 1


def test_round_robin_alternates_owners():
    client = FakeHubSpotClient()
    first = ingest_lead(
        LeadIngestRequest(
            nombre="Lead 1",
            email="lead1@example.com",
            telefono="611111111",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    second = ingest_lead(
        LeadIngestRequest(
            nombre="Lead 2",
            email="lead2@example.com",
            telefono="622222222",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    assert first.lead.responsable_id == "owner-1"
    assert second.lead.responsable_id == "owner-2"


def test_ingest_sin_dueno_when_no_owners():
    client = FakeHubSpotClient()
    client.owners = []
    reset_round_robin([])
    result = ingest_lead(
        LeadIngestRequest(
            nombre="Sin owner",
            email="sin.owner@example.com",
            telefono="633333333",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    assert result.action == "exception"
    assert result.lead.exception_code == "SIN_DUENO"


def test_update_lead_sets_primera_respuesta():
    client = FakeHubSpotClient()
    created = ingest_lead(
        LeadIngestRequest(
            nombre="Ana",
            email="patch@example.com",
            telefono="644444444",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    updated = update_lead(
        created.lead.lead_id,
        LeadUpdateRequest(primera_respuesta_at=datetime.now(timezone.utc)),
        client,  # type: ignore[arg-type]
    )
    assert updated.primera_respuesta_at is not None
    assert updated.estado == LeadEstado.EN_SEGUIMIENTO


def test_enrich_lead_operational_marks_sla_roto():
    from api.leads.models import LeadResponse

    past = datetime.now(timezone.utc) - timedelta(hours=2)
    lead = LeadResponse(
        lead_id="1",
        estado=LeadEstado.ASIGNADO,
        sla_primera_respuesta_at=past,
        primera_respuesta_at=None,
        exception_code=None,
    )
    enriched = enrich_lead_operational(lead)
    assert enriched.exception_code == "SLA_ROTO"


def test_list_exceptions_includes_sla_roto_enriched():
    client = FakeHubSpotClient()
    past_ms = int((datetime.now(timezone.utc) - timedelta(hours=2)).timestamp() * 1000)
    contact_id = client._next_id()
    client.contacts[contact_id] = {
        "id": contact_id,
        "properties": {
            "firstname": "SLA vencido",
            "email": "sla@example.com",
            "lead_origen": "portal",
            "lead_estado": LeadEstado.ASIGNADO.value,
            "hubspot_owner_id": "owner-1",
            "sla_primera_respuesta_at": str(past_ms),
            "createdate": datetime.now(timezone.utc).isoformat(),
            "lastmodifieddate": datetime.now(timezone.utc).isoformat(),
        },
    }
    exceptions = list_exceptions(client)  # type: ignore[arg-type]
    assert any(item.exception_code == "SLA_ROTO" for item in exceptions)


def test_task_soft_fail_403_still_creates_lead():
    client = FakeHubSpotClient()

    def fail_task(**kwargs):
        raise HubSpotError("forbidden", status_code=403)

    client.create_task = fail_task  # type: ignore[method-assign]
    result = ingest_lead(
        LeadIngestRequest(
            nombre="Ana",
            email="task403@example.com",
            telefono="655555555",
            origen="portal",
        ),
        client,  # type: ignore[arg-type]
    )
    assert result.action == "created"
    assert "Tarea HubSpot no creada" in result.message


def test_build_metrics_counts_sla_rotos():
    from api.leads.models import LeadResponse

    client = FakeHubSpotClient()
    past = datetime.now(timezone.utc) - timedelta(hours=1)
    leads = [
        LeadResponse(
            lead_id="1",
            estado=LeadEstado.ASIGNADO,
            responsable_id="owner-1",
            siguiente_accion="Llamar",
            sla_primera_respuesta_at=past,
            primera_respuesta_at=None,
        )
    ]
    metrics = client.build_metrics(leads)
    assert metrics.sla_rotos == 1
