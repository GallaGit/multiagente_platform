"""Tests for lead orchestration with mocked HubSpot client."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pytest
from fastapi.testclient import TestClient

from api.leads.hubspot import compute_dedupe_key, normalize_email, normalize_phone
from api.leads.models import LeadEstado, LeadIngestRequest
from api.leads.orchestrator import ingest_lead, reset_round_robin


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

    def find_existing_contact(self, email: str | None, telefono: str | None):
        for contact in self.contacts.values():
            props = contact["properties"]
            if email and props.get("email") == normalize_email(email):
                return contact
            if telefono and props.get("phone") == normalize_phone(telefono):
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
        return list(self.contacts.values())

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
