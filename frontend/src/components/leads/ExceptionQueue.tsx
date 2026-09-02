import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import type { Lead } from "../../lib/api";
import { api } from "../../lib/api";

interface ExceptionQueueProps {
  exceptions: Lead[];
  loading: boolean;
}

export function ExceptionQueue({ exceptions, loading }: ExceptionQueueProps) {
  const [resolvingId, setResolvingId] = useState<string | null>(null);
  const [resolveError, setResolveError] = useState<string | null>(null);
  const queryClient = useQueryClient();

  const resolve = useMutation({
    mutationFn: (leadId: string) => api.resolveException(leadId),
    onMutate: (leadId) => {
      setResolvingId(leadId);
      setResolveError(null);
    },
    onSuccess: () => {
      setResolvingId(null);
      queryClient.invalidateQueries({ queryKey: ["leads"] });
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
      queryClient.invalidateQueries({ queryKey: ["exceptions"] });
    },
    onError: (error: Error) => {
      setResolvingId(null);
      setResolveError(error.message);
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

      {resolveError && (
        <p className="mb-3 rounded-lg border border-rose-400/30 bg-rose-500/10 p-3 text-sm text-rose-100">
          {resolveError}
        </p>
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
                disabled={resolvingId === lead.lead_id}
                onClick={() => resolve.mutate(lead.lead_id)}
              >
                {resolvingId === lead.lead_id ? "Resolviendo…" : "Resolver"}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
