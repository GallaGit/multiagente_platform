import { useMutation, useQueryClient } from "@tanstack/react-query";
import type { Lead } from "../../lib/api";
import { api } from "../../lib/api";

function estadoBadge(estado: Lead["estado"]) {
  const map: Record<Lead["estado"], string> = {
    nuevo: "bg-slate-500/20 text-slate-200",
    asignado: "bg-cyan-500/20 text-cyan-200",
    en_seguimiento: "bg-violet-500/20 text-violet-200",
    excepcion: "bg-amber-500/20 text-amber-200",
    cerrado_corto: "bg-emerald-500/20 text-emerald-200",
  };
  return map[estado] ?? map.nuevo;
}

function formatSla(deadline: string | null, responded: string | null) {
  if (responded) return { label: "Respondido", overdue: false };
  if (!deadline) return { label: "—", overdue: false };
  const ms = new Date(deadline).getTime() - Date.now();
  if (ms <= 0) return { label: "Vencido", overdue: true };
  const mins = Math.floor(ms / 60000);
  if (mins < 60) return { label: `${mins} min`, overdue: false };
  return { label: `${Math.floor(mins / 60)}h ${mins % 60}m`, overdue: false };
}

interface LeadTableProps {
  leads: Lead[];
  loading: boolean;
}

export function LeadTable({ leads, loading }: LeadTableProps) {
  const queryClient = useQueryClient();
  const markResponse = useMutation({
    mutationFn: (leadId: string) => api.markFirstResponse(leadId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
      queryClient.invalidateQueries({ queryKey: ["exceptions"] });
    },
  });

  if (loading) {
    return (
      <div className="glass p-8 text-center text-slate-400">
        Cargando leads…
      </div>
    );
  }

  if (leads.length === 0) {
    return (
      <div className="glass p-8 text-center text-slate-400">
        No hay leads todavia. Usa el formulario de ingesta para simular un
        lead de portal.
      </div>
    );
  }

  return (
    <div className="glass overflow-hidden">
      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm">
          <thead className="border-b border-white/10 bg-white/5 text-xs uppercase tracking-wide text-slate-400">
            <tr>
              <th className="px-4 py-3">Contacto</th>
              <th className="px-4 py-3">Origen</th>
              <th className="px-4 py-3">Responsable</th>
              <th className="px-4 py-3">Estado</th>
              <th className="px-4 py-3">SLA</th>
              <th className="px-4 py-3">Siguiente accion</th>
              <th className="px-4 py-3">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {leads.map((lead) => {
              const sla = formatSla(
                lead.sla_primera_respuesta_at,
                lead.primera_respuesta_at,
              );
              const markingThis =
                markResponse.isPending &&
                markResponse.variables === lead.lead_id;

              return (
                <tr
                  key={lead.lead_id}
                  className="border-b border-white/5 transition hover:bg-white/5"
                >
                  <td className="px-4 py-3">
                    <div className="font-medium text-white">
                      {lead.nombre ?? "Desconocido"}
                    </div>
                    <div className="text-xs text-slate-400">
                      {lead.email ?? lead.telefono ?? "Sin contacto"}
                    </div>
                    {lead.is_duplicate && (
                      <span className="badge mt-1 bg-violet-500/20 text-violet-200">
                        Duplicado
                      </span>
                    )}
                  </td>
                  <td className="px-4 py-3 text-slate-300">
                    <div>{lead.origen ?? "—"}</div>
                    <div className="text-xs text-slate-500">
                      {lead.inmueble_ref ?? lead.origen_ref ?? ""}
                    </div>
                  </td>
                  <td className="px-4 py-3 text-slate-300">
                    {lead.responsable_nombre ?? lead.responsable_id ?? "—"}
                  </td>
                  <td className="px-4 py-3">
                    <span className={`badge ${estadoBadge(lead.estado)}`}>
                      {lead.estado}
                    </span>
                  </td>
                  <td
                    className={`px-4 py-3 ${
                      sla.overdue ? "font-medium text-rose-300" : "text-slate-300"
                    }`}
                  >
                    {sla.label}
                  </td>
                  <td className="px-4 py-3 text-slate-300">
                    {lead.siguiente_accion ?? "—"}
                  </td>
                  <td className="px-4 py-3">
                    {!lead.primera_respuesta_at &&
                      lead.sla_primera_respuesta_at && (
                        <button
                          type="button"
                          className="glass-btn-ghost text-xs"
                          disabled={markResponse.isPending}
                          onClick={() => markResponse.mutate(lead.lead_id)}
                        >
                          {markingThis ? "Guardando…" : "Marcar 1ª respuesta"}
                        </button>
                      )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      {markResponse.isError && (
        <p className="border-t border-rose-400/20 px-4 py-3 text-sm text-rose-200">
          {(markResponse.error as Error).message}
        </p>
      )}
    </div>
  );
}
