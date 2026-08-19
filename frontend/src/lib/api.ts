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

export interface ChatResponse {
  routed_to: string;
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
  getLeads: () => request<LeadListResponse>("/leads"),
  getMetrics: () => request<LeadMetrics>("/leads/metrics"),
  getExceptions: () => request<LeadListResponse>("/leads/exceptions"),
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
