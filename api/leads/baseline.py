"""Local baseline snapshot for lab metrics comparison."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from api.config import ROOT_DIR
from api.leads.models import (
    BaselineSnapshot,
    LeadMetricsResponse,
    MetricsDashboardResponse,
    MetricsDelta,
)

DEFAULT_BASELINE_PATH = ROOT_DIR / "data" / "baseline.json"


def get_baseline_path() -> Path:
    return DEFAULT_BASELINE_PATH


def load_baseline(path: Path | None = None) -> BaselineSnapshot | None:
    target = path or get_baseline_path()
    if not target.exists():
        return None
    data = json.loads(target.read_text(encoding="utf-8"))
    return BaselineSnapshot.model_validate(data)


def save_baseline(snapshot: BaselineSnapshot, path: Path | None = None) -> BaselineSnapshot:
    target = path or get_baseline_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        snapshot.model_dump_json(indent=2),
        encoding="utf-8",
    )
    return snapshot


def capture_baseline(
    metrics: LeadMetricsResponse,
    *,
    note: str | None = None,
    mvp_only: bool = True,
    path: Path | None = None,
) -> BaselineSnapshot:
    snapshot = BaselineSnapshot(
        captured_at=datetime.now(timezone.utc),
        note=note,
        metrics=metrics,
        mvp_only=mvp_only,
    )
    save_baseline(snapshot, path=path)
    return snapshot


def compute_delta(
    current: LeadMetricsResponse,
    baseline: LeadMetricsResponse,
) -> MetricsDelta:
    mediana_delta: float | None = None
    if (
        current.mediana_tiempo_respuesta_min is not None
        and baseline.mediana_tiempo_respuesta_min is not None
    ):
        mediana_delta = round(
            current.mediana_tiempo_respuesta_min - baseline.mediana_tiempo_respuesta_min,
            1,
        )

    return MetricsDelta(
        total_leads=current.total_leads - baseline.total_leads,
        pct_con_responsable=round(
            current.pct_con_responsable - baseline.pct_con_responsable,
            1,
        ),
        pct_con_siguiente_accion=round(
            current.pct_con_siguiente_accion - baseline.pct_con_siguiente_accion,
            1,
        ),
        excepciones_abiertas=current.excepciones_abiertas - baseline.excepciones_abiertas,
        sla_rotos=current.sla_rotos - baseline.sla_rotos,
        mediana_tiempo_respuesta_min=mediana_delta,
    )


def build_dashboard(
    current: LeadMetricsResponse,
    baseline_snapshot: BaselineSnapshot | None = None,
) -> MetricsDashboardResponse:
    delta = None
    if baseline_snapshot:
        delta = compute_delta(current, baseline_snapshot.metrics)
    return MetricsDashboardResponse(
        current=current,
        baseline=baseline_snapshot,
        delta=delta,
    )
