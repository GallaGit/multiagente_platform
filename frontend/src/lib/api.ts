export type LeadEstado =
  | "nuevo"
  | "asignado"
  | "en_seguimiento"
  | "excepcion"
  | "cerrado_corto";

export interface Lead {
  lead_id: string;
  nombre: string | null;
  email: string | null;
  telefono: string | null;
  origen: string | null;
  origen_ref: string | null;
  inmueble_ref: string | null;
  responsable_id: string | null;
  responsable_nombre: string | null;
  estado: LeadEstado;
  siguiente_accion: string | null;
  sla_primera_respuesta_at: string | null;
  primera_respuesta_at: string | null;
  exception_code: string | null;
  dedupe_key: string | null;
  created_at: string | null;
  updated_at: string | null;
  is_duplicate: boolean;
}

export interface LeadListResponse {
  items: Lead[];
  total: number;
}

export interface LeadMetrics {
  total_leads: number;
  pct_con_responsable: number;
  pct_con_siguiente_accion: number;
  excepciones_abiertas: number;
  sla_rotos: number;
  mediana_tiempo_respuesta_min: number | null;
}

export interface MetricsDelta {
  total_leads: number;
  pct_con_responsable: number;
  pct_con_siguiente_accion: number;
  excepciones_abiertas: number;
  sla_rotos: number;
  mediana_tiempo_respuesta_min: number | null;
}

export interface BaselineSnapshot {
  captured_at: string;
  note: string | null;
  metrics: LeadMetrics;
  mvp_only: boolean;
}

export interface MetricsDashboard {
  current: LeadMetrics;
  baseline: BaselineSnapshot | null;
  delta: MetricsDelta | null;
}

export interface IngestResult {
  lead: Lead;
  action: string;
  message: string;
}

export interface LeadIngestPayload {
  nombre?: string;
  email?: string;
  telefono?: string;
  origen?: string;
  origen_ref?: string;
  inmueble_ref?: string;
  mensaje?: string;
}

export interface LeadUpdatePayload {
  estado?: LeadEstado;
  exception_code?: string;
  primera_respuesta_at?: string;
  siguiente_accion?: string;
  responsable_id?: string;
}

export interface ChatResponse {
  routed_to: string;
  documentation: string;
  reply: string;
  reason: string;
}

export interface ResearchResponse {
  reply: string;
  queries: string[];
  hits: number;
  note: string;
}

const API_BASE = "/api";

function leadsQuery(mvpOnly: boolean) {
  return mvpOnly ? "" : "?mvp_only=false";
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(init?.headers ?? {}) },
    ...init,
  });
  if (!response.ok) {
    let detail = response.statusText;
    try {
      const body = await response.json();
      detail = body.detail ?? detail;
    } catch {
      /* ignore */
    }
    throw new Error(typeof detail === "string" ? detail : JSON.stringify(detail));
  }
  return response.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>("/health"),
  getLeads: (mvpOnly = true) =>
    request<LeadListResponse>(`/leads${leadsQuery(mvpOnly)}`),
  getMetrics: (mvpOnly = true) =>
    request<MetricsDashboard>(`/leads/metrics${leadsQuery(mvpOnly)}`),
  getExceptions: (mvpOnly = true) =>
    request<LeadListResponse>(`/leads/exceptions${leadsQuery(mvpOnly)}`),
  captureBaseline: (note?: string, mvpOnly = true) =>
    request<BaselineSnapshot>("/leads/baseline", {
      method: "POST",
      body: JSON.stringify({ note: note ?? null, mvp_only: mvpOnly }),
    }),
  getBaseline: () => request<BaselineSnapshot>("/leads/baseline"),
  ingestLead: (payload: LeadIngestPayload) =>
    request<IngestResult>("/leads/ingest", {
      method: "POST",
      body: JSON.stringify(payload),
    }),
  resolveException: (leadId: string) =>
    request<Lead>("/leads/" + leadId, {
      method: "PATCH",
      body: JSON.stringify({
        estado: "asignado",
        exception_code: "",
        siguiente_accion: "Revisar y contactar manualmente",
      }),
    }),
  updateLead: (leadId: string, payload: LeadUpdatePayload) =>
    request<Lead>(`/leads/${leadId}`, {
      method: "PATCH",
      body: JSON.stringify(payload),
    }),
  markFirstResponse: (leadId: string) =>
    request<Lead>(`/leads/${leadId}`, {
      method: "PATCH",
      body: JSON.stringify({
        primera_respuesta_at: new Date().toISOString(),
      }),
    }),
  chat: (message: string) =>
    request<ChatResponse>("/chat", {
      method: "POST",
      body: JSON.stringify({ message }),
    }),
  research: (cities: string[], limit: number) =>
    request<ResearchResponse>("/research", {
      method: "POST",
      body: JSON.stringify({ cities, limit }),
    }),
};
