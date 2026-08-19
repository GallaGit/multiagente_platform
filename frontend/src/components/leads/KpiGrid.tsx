import type { LeadMetrics } from "../../lib/api";

interface KpiGridProps {
  metrics: LeadMetrics | undefined;
  loading: boolean;
}

const cards = [
  { key: "total", label: "Leads entrados", accent: "text-white" },
  { key: "owner", label: "% con responsable", accent: "text-cyan-300" },
  { key: "action", label: "% con siguiente accion", accent: "text-violet-300" },
  { key: "exceptions", label: "Excepciones abiertas", accent: "text-amber-300" },
  { key: "sla", label: "SLA rotos", accent: "text-rose-300" },
] as const;

function valueFor(key: (typeof cards)[number]["key"], metrics?: LeadMetrics) {
  if (!metrics) return "—";
  switch (key) {
    case "total":
      return String(metrics.total_leads);
    case "owner":
      return `${metrics.pct_con_responsable}%`;
    case "action":
      return `${metrics.pct_con_siguiente_accion}%`;
    case "exceptions":
      return String(metrics.excepciones_abiertas);
    case "sla":
      return String(metrics.sla_rotos);
  }
}

export function KpiGrid({ metrics, loading }: KpiGridProps) {
  return (
    <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-5">
      {cards.map((card) => (
        <div key={card.key} className="glass p-4">
          <p className="text-xs uppercase tracking-wide text-slate-400">
            {card.label}
          </p>
          <p className={`mt-2 text-3xl font-semibold ${card.accent}`}>
            {loading ? "…" : valueFor(card.key, metrics)}
          </p>
        </div>
      ))}
    </div>
  );
}
