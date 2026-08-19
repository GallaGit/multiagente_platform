import { useMutation, useQueryClient } from "@tanstack/react-query";
import type { Lead } from "../../lib/api";
import { api } from "../../lib/api";

interface ExceptionQueueProps {
  exceptions: Lead[];
  loading: boolean;
}

export function ExceptionQueue({ exceptions, loading }: ExceptionQueueProps) {
  const queryClient = useQueryClient();
  const resolve = useMutation({
    mutationFn: (leadId: string) => api.resolveException(leadId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["leads"] });
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
      queryClient.invalidateQueries({ queryKey: ["exceptions"] });
    },
  });

  return (
    <div className="glass p-5">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold text-white">Cola excepciones</h2>
        <span className="badge bg-amber-500/20 text-amber-200">
          {exceptions.length}
        </span>
      </div>

      {loading && (
        <p className="text-sm text-slate-400">Cargando excepciones…</p>
      )}

      {!loading && exceptions.length === 0 && (
        <p className="text-sm text-slate-400">Sin excepciones abiertas.</p>
      )}

      <div className="space-y-3">
        {exceptions.map((lead) => (
          <div
            key={lead.lead_id}
            className="rounded-xl border border-white/10 bg-white/5 p-4"
          >
            <div className="flex flex-wrap items-start justify-between gap-3">
              <div>
                <p className="font-medium text-white">
                  {lead.nombre ?? "Sin nombre"}
                </p>
                <p className="mt-1 text-xs text-amber-200">
                  {lead.exception_code}
                </p>
                <p className="mt-1 text-xs text-slate-400">
                  {lead.email ?? lead.telefono ?? "Sin datos de contacto"}
                </p>
              </div>
              <button
                type="button"
                className="glass-btn-ghost"
                disabled={resolve.isPending}
                onClick={() => resolve.mutate(lead.lead_id)}
              >
                Resolver
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
