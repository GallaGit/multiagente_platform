from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, model_validator


class LeadEstado(StrEnum):
    NUEVO = "nuevo"
    ASIGNADO = "asignado"
    EN_SEGUIMIENTO = "en_seguimiento"
    EXCEPCION = "excepcion"
    CERRADO_CORTO = "cerrado_corto"


class ExceptionCode(StrEnum):
    SIN_DUENO = "SIN_DUENO"
    SLA_ROTO = "SLA_ROTO"
    DATOS_INSUFICIENTES = "DATOS_INSUFICIENTES"
    DUPLICADO_CONFLICTO = "DUPLICADO_CONFLICTO"
    SYNC_FALLIDO = "SYNC_FALLIDO"


class LeadIngestRequest(BaseModel):
    nombre: str | None = None
    email: str | None = None
    telefono: str | None = None
    origen: str = Field(default="portal", min_length=1)
    origen_ref: str | None = None
    inmueble_ref: str | None = None
    mensaje: str | None = None


class LeadUpdateRequest(BaseModel):
    estado: LeadEstado | None = None
    exception_code: str | None = None
    primera_respuesta_at: datetime | None = None
    siguiente_accion: str | None = None
    responsable_id: str | None = None


class LeadResponse(BaseModel):
    lead_id: str
    nombre: str | None = None
    email: str | None = None
    telefono: str | None = None
    origen: str | None = None
    origen_ref: str | None = None
    inmueble_ref: str | None = None
    responsable_id: str | None = None
    responsable_nombre: str | None = None
    estado: LeadEstado
    siguiente_accion: str | None = None
    sla_primera_respuesta_at: datetime | None = None
    primera_respuesta_at: datetime | None = None
    exception_code: str | None = None
    dedupe_key: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    is_duplicate: bool = False


class LeadListResponse(BaseModel):
    items: list[LeadResponse]
    total: int


class LeadMetricsResponse(BaseModel):
    total_leads: int
    pct_con_responsable: float
    pct_con_siguiente_accion: float
    excepciones_abiertas: int
    sla_rotos: int


class OwnerResponse(BaseModel):
    id: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class IngestResult(BaseModel):
    lead: LeadResponse
    action: str
    message: str


class HubSpotContactProperties(BaseModel):
    email: str | None = None
    phone: str | None = None
    firstname: str | None = None
    hubspot_owner_id: str | None = None
    lead_origen: str | None = None
    lead_origen_ref: str | None = None
    inmueble_ref: str | None = None
    lead_estado: str | None = None
    siguiente_accion: str | None = None
    sla_primera_respuesta_at: str | None = None
    primera_respuesta_at: str | None = None
    exception_code: str | None = None
    dedupe_key: str | None = None

    @model_validator(mode="before")
    @classmethod
    def strip_empty(cls, data: object) -> object:
        if not isinstance(data, dict):
            return data
        return {key: value for key, value in data.items() if value not in (None, "")}
