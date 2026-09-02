import type { LeadMetrics, MetricsDashboard } from "../../lib/api";

interface KpiGridProps {
  dashboard: MetricsDashboard | undefined;
  loading: boolean;
  onCaptureBaseline?: () => void;
  capturePending?: boolean;
}

type CardKey =
  | "total"
  | "owner"
  | "action"
  | "response"
  | "exceptions"
  | "sla";

const cards: { key: CardKey; label: string; accent: string }[] = [
  { key: "total", label: "Leads entrados", accent: "text-white" },
  { key: "owner", label: "% con responsable", accent: "text-cyan-300" },
  { key: "action", label: "% con siguiente accion", accent: "text-violet-300" },
  {
    key: "response",
    label: "Mediana 1a respuesta (min)",
    accent: "text-emerald-300",
  },
  { key: "exceptions", label: "Excepciones abiertas", accent: "text-amber-300" },
  { key: "sla", label: "SLA rotos", accent: "text-rose-300" },
];

function valueFor(key: CardKey, metrics?: LeadMetrics) {
  if (!metrics) return "—";
  switch (key) {
    case "total":
      return String(metrics.total_leads);
    case "owner":
      return `${metrics.pct_con_responsable}%`;
    case "action":
      return `${metrics.pct_con_siguiente_accion}%`;
    case "response":
      return metrics.mediana_tiempo_respuesta_min == null
        ? "n/a"
        : `${metrics.mediana_tiempo_respuesta_min} min`;
    case "exceptions":
      return String(metrics.excepciones_abiertas);
    case "sla":
      return String(metrics.sla_rotos);
  }
}

function formatDelta(key: CardKey, delta?: MetricsDashboard["delta"]) {
  if (!delta) return null;

  let raw: number | null | undefined;
  switch (key) {
    case "total":
      raw = delta.total_leads;
      break;
    case "owner":
      raw = delta.pct_con_responsable;
      break;
    case "action":
      raw = delta.pct_con_siguiente_accion;
      break;
    case "response":
      raw = delta.mediana_tiempo_respuesta_min;
      break;
    case "exceptions":
      raw = delta.excepciones_abiertas;
      break;
    case "sla":
      raw = delta.sla_rotos;
      break;
  }

  if (raw == null || raw === 0) return null;

  const prefix = raw > 0 ? "+" : "";
  const suffix =
    key === "owner" || key === "action" ? " pp" : key === "response" ? " min" : "";
  return `${prefix}${raw}${suffix}`;
}

function deltaTone(key: CardKey, delta?: MetricsDashboard["delta"]) {
  if (!delta) return "text-slate-400";
  let raw: number | null | undefined;
  switch (key) {
    case "total":
      raw = delta.total_leads;
      break;
    case "owner":
      raw = delta.pct_con_responsable;
      break;
    case "action":
      raw = delta.pct_con_siguiente_accion;
      break;
    case "response":
      raw = delta.mediana_tiempo_respuesta_min;
      break;
    case "exceptions":
      raw = delta.excepciones_abiertas;
      break;
    case "sla":
      raw = delta.sla_rotos;
      break;
  }
  if (raw == null || raw === 0) return "text-slate-400";

  const higherIsBetter = key === "total" || key === "owner" || key === "action";
  const lowerIsBetter =
    key === "exceptions" || key === "sla" || key === "response";
  const positive = higherIsBetter ? raw > 0 : lowerIsBetter ? raw < 0 : false;
  const negative = higherIsBetter ? raw < 0 : lowerIsBetter ? raw > 0 : false;

  if (positive) return "text-emerald-300";
  if (negative) return "text-rose-300";
  return "text-slate-400";
}

export function KpiGrid({
  dashboard,
  loading,
  onCaptureBaseline,
  capturePending = false,
}: KpiGridProps) {
  const metrics = dashboard?.current;
  const showBaselineHint = !loading && dashboard && !dashboard.baseline;

  return (
    <div className="space-y-3">
      {showBaselineHint && onCaptureBaseline && (
        <div className="glass flex flex-wrap items-center justify-between gap-3 border-cyan-400/20 p-4 text-sm text-slate-300">
          <p>
            Sin baseline capturado. Usa el botón para guardar el día 0 y ver
            deltas en los KPIs.
          </p>
          <button
            type="button"
            className="glass-btn-ghost text-xs"
            disabled={capturePending}
            onClick={onCaptureBaseline}
          >
            {capturePending ? "Capturando…" : "Capturar baseline"}
          </button>
        </div>
      )}
      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-6">
      {cards.map((card) => {
        const deltaLabel = formatDelta(card.key, dashboard?.delta);
        return (
          <div key={card.key} className="glass p-4">
            <p className="text-xs uppercase tracking-wide text-slate-400">
              {card.label}
            </p>
            <p className={`mt-2 text-3xl font-semibold ${card.accent}`}>
              {loading ? "…" : valueFor(card.key, metrics)}
            </p>
            {deltaLabel && (
              <p className={`mt-1 text-xs ${deltaTone(card.key, dashboard?.delta)}`}>
                vs baseline {deltaLabel}
              </p>
            )}
          </div>
        );
      })}
      </div>
    </div>
  );
}
