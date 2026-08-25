from fastapi import APIRouter, HTTPException, Query

from api.config import get_settings
from api.leads.baseline import build_dashboard, capture_baseline, load_baseline
from api.leads.hubspot import HubSpotClient, HubSpotError
from api.leads.models import (
    BaselineCaptureRequest,
    BaselineSnapshot,
    IngestResult,
    LeadIngestRequest,
    LeadListResponse,
    LeadResponse,
    LeadUpdateRequest,
    MetricsDashboardResponse,
    OwnerResponse,
)
from api.leads.orchestrator import (
    compute_metrics,
    ingest_lead,
    list_exceptions,
    list_leads,
    update_lead,
)

router = APIRouter(prefix="/leads", tags=["leads"])


def _hubspot_client() -> HubSpotClient:
    settings = get_settings()
    if not settings.hubspot_access_token:
        raise HTTPException(
            status_code=503,
            detail="HUBSPOT_ACCESS_TOKEN no configurado",
        )
    return HubSpotClient()


def _handle_hubspot_error(exc: HubSpotError) -> HTTPException:
    status = exc.status_code or 502
    if status >= 500 or status == 429:
        status = 502
    return HTTPException(status_code=status, detail=str(exc))


@router.post("/ingest", response_model=IngestResult)
def ingest(body: LeadIngestRequest) -> IngestResult:
    try:
        return ingest_lead(body, _hubspot_client())
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc


@router.get("", response_model=LeadListResponse)
def get_leads(
    estado: str | None = Query(default=None),
    exception_code: str | None = Query(default=None),
    limit: int = Query(default=100, ge=1, le=100),
    mvp_only: bool = Query(default=True),
) -> LeadListResponse:
    try:
        items = list_leads(
            _hubspot_client(),
            estado=estado,
            exception_code=exception_code,
            limit=limit,
            mvp_only=mvp_only,
        )
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc
    return LeadListResponse(items=items, total=len(items))


@router.get("/metrics", response_model=MetricsDashboardResponse)
def get_metrics(
    mvp_only: bool = Query(default=True),
) -> MetricsDashboardResponse:
    try:
        current = compute_metrics(_hubspot_client(), mvp_only=mvp_only)
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc
    baseline = load_baseline()
    return build_dashboard(current, baseline)


@router.get("/baseline", response_model=BaselineSnapshot)
def get_baseline() -> BaselineSnapshot:
    snapshot = load_baseline()
    if snapshot is None:
        raise HTTPException(status_code=404, detail="Baseline no capturado")
    return snapshot


@router.post("/baseline", response_model=BaselineSnapshot)
def post_baseline(body: BaselineCaptureRequest) -> BaselineSnapshot:
    try:
        metrics = compute_metrics(_hubspot_client(), mvp_only=body.mvp_only)
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc
    return capture_baseline(
        metrics,
        note=body.note,
        mvp_only=body.mvp_only,
    )


@router.get("/exceptions", response_model=LeadListResponse)
def get_exceptions(
    mvp_only: bool = Query(default=True),
) -> LeadListResponse:
    try:
        items = list_exceptions(_hubspot_client(), mvp_only=mvp_only)
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc
    return LeadListResponse(items=items, total=len(items))


@router.get("/owners", response_model=list[OwnerResponse])
def get_owners() -> list[OwnerResponse]:
    try:
        return _hubspot_client().list_owners()
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc


@router.patch("/{lead_id}", response_model=LeadResponse)
def patch_lead(lead_id: str, body: LeadUpdateRequest) -> LeadResponse:
    try:
        return update_lead(lead_id, body, _hubspot_client())
    except HubSpotError as exc:
        raise _handle_hubspot_error(exc) from exc
