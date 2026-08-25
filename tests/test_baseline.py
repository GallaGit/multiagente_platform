"""Tests for MVP filter, baseline snapshot and metrics dashboard."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fastapi.testclient import TestClient

from api.leads.baseline import capture_baseline, load_baseline
from api.leads.models import LeadEstado, LeadMetricsResponse, LeadResponse
from api.leads.orchestrator import compute_metrics, list_leads


def _lead(
    lead_id: str,
    *,
    origen: str | None = "portal",
    owner: str | None = "owner-1",
    action: str | None = "Llamar",
    estado: LeadEstado = LeadEstado.ASIGNADO,
    exception_code: str | None = None,
    created_at: datetime | None = None,
    primera_respuesta_at: datetime | None = None,
) -> LeadResponse:
    now = datetime.now(timezone.utc)
    return LeadResponse(
        lead_id=lead_id,
        origen=origen,
        responsable_id=owner,
        siguiente_accion=action,
        estado=estado,
        exception_code=exception_code,
        created_at=created_at or now,
        primera_respuesta_at=primera_respuesta_at,
    )


class MvpFilterHubSpotClient:
    def __init__(self) -> None:
        self.contacts = {
            "1": {
                "id": "1",
                "properties": {
                    "lead_origen": "portal",
                    "lead_estado": "asignado",
                    "hubspot_owner_id": "owner-1",
                    "siguiente_accion": "Llamar",
                    "createdate": datetime.now(timezone.utc).isoformat(),
                },
            },
            "2": {
                "id": "2",
                "properties": {
                    "firstname": "Legacy",
                    "createdate": datetime.now(timezone.utc).isoformat(),
                },
            },
        }
        self.last_mvp_only: bool | None = None

    def list_owners(self):
        from api.leads.models import OwnerResponse

        return [OwnerResponse(id="owner-1", email="a@demo.com")]

    def list_contacts(self, **kwargs):
        self.last_mvp_only = kwargs.get("mvp_only", True)
        contacts = list(self.contacts.values())
        if self.last_mvp_only:
            contacts = [
                contact
                for contact in contacts
                if contact["properties"].get("lead_origen")
            ]
        estado = kwargs.get("estado")
        if estado:
            contacts = [
                contact
                for contact in contacts
                if contact["properties"].get("lead_estado") == estado
            ]
        return contacts

    def contact_to_lead(self, contact, owners_map=None, is_duplicate=False):
        from api.leads.hubspot import HubSpotClient

        real = HubSpotClient.__new__(HubSpotClient)
        return HubSpotClient.contact_to_lead(
            real,
            contact,
            owners_map=owners_map,
            is_duplicate=is_duplicate,
        )

    def build_metrics(self, leads):
        from api.leads.hubspot import HubSpotClient

        real = HubSpotClient.__new__(HubSpotClient)
        return HubSpotClient.build_metrics(real, leads)


def test_mvp_only_filters_non_orchestrator_contacts():
    client = MvpFilterHubSpotClient()
    all_leads = list_leads(client, mvp_only=False)  # type: ignore[arg-type]
    mvp_leads = list_leads(client, mvp_only=True)  # type: ignore[arg-type]

    assert len(all_leads) == 2
    assert len(mvp_leads) == 1
    assert mvp_leads[0].lead_id == "1"


def test_compute_metrics_mvp_only():
    client = MvpFilterHubSpotClient()
    all_metrics = compute_metrics(client, mvp_only=False)  # type: ignore[arg-type]
    mvp_metrics = compute_metrics(client, mvp_only=True)  # type: ignore[arg-type]

    assert all_metrics.total_leads == 2
    assert mvp_metrics.total_leads == 1
    assert mvp_metrics.pct_con_responsable == 100.0


def test_median_response_minutes_requires_two_samples():
    from api.leads.hubspot import HubSpotClient

    base = datetime(2026, 1, 1, tzinfo=timezone.utc)
    one_sample = [
        _lead("1", created_at=base, primera_respuesta_at=base + timedelta(minutes=30)),
    ]
    two_samples = [
        _lead("1", created_at=base, primera_respuesta_at=base + timedelta(minutes=20)),
        _lead("2", created_at=base, primera_respuesta_at=base + timedelta(minutes=40)),
    ]

    real = HubSpotClient.__new__(HubSpotClient)
    assert HubSpotClient.build_metrics(real, one_sample).mediana_tiempo_respuesta_min is None
    assert HubSpotClient.build_metrics(real, two_samples).mediana_tiempo_respuesta_min == 30.0


def test_baseline_post_and_get(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("HUBSPOT_ACCESS_TOKEN", "pat-test")
    from api.config import get_settings

    get_settings.cache_clear()

    baseline_path = tmp_path / "baseline.json"
    monkeypatch.setattr("api.leads.baseline.DEFAULT_BASELINE_PATH", baseline_path)
    monkeypatch.setattr("api.leads.baseline.get_baseline_path", lambda: baseline_path)

    fake = MvpFilterHubSpotClient()
    monkeypatch.setattr("api.leads.routes._hubspot_client", lambda: fake)

    from api.main import app

    with TestClient(app) as test_client:
        missing = test_client.get("/leads/baseline")
        assert missing.status_code == 404

        captured = test_client.post(
            "/leads/baseline",
            json={"note": "Lab day 0", "mvp_only": True},
        )
        assert captured.status_code == 200
        body = captured.json()
        assert body["note"] == "Lab day 0"
        assert body["metrics"]["total_leads"] == 1

        loaded = test_client.get("/leads/baseline")
        assert loaded.status_code == 200
        assert loaded.json()["metrics"]["total_leads"] == 1

        dashboard = test_client.get("/leads/metrics?mvp_only=true")
        assert dashboard.status_code == 200
        dash = dashboard.json()
        assert dash["current"]["total_leads"] == 1
        assert dash["baseline"]["note"] == "Lab day 0"
        assert dash["delta"]["total_leads"] == 0

    get_settings.cache_clear()


def test_capture_baseline_writes_file(tmp_path: Path, monkeypatch):
    baseline_path = tmp_path / "baseline.json"
    monkeypatch.setattr("api.leads.baseline.DEFAULT_BASELINE_PATH", baseline_path)

    metrics = LeadMetricsResponse(
        total_leads=3,
        pct_con_responsable=66.7,
        pct_con_siguiente_accion=100.0,
        excepciones_abiertas=1,
        sla_rotos=0,
        mediana_tiempo_respuesta_min=25.0,
    )
    snapshot = capture_baseline(metrics, note="demo", mvp_only=True, path=baseline_path)

    assert snapshot.note == "demo"
    assert baseline_path.exists()
    stored = json.loads(baseline_path.read_text(encoding="utf-8"))
    assert stored["metrics"]["total_leads"] == 3
    assert load_baseline(baseline_path) is not None
