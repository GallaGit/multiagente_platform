import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { api } from "../lib/api";
import { ExceptionQueue } from "../components/leads/ExceptionQueue";
import { IngestForm } from "../components/leads/IngestForm";
import { KpiGrid } from "../components/leads/KpiGrid";
import { LeadTable } from "../components/leads/LeadTable";

export function LeadsPage() {
  const [mvpOnly, setMvpOnly] = useState(true);
  const queryClient = useQueryClient();

  const metricsQuery = useQuery({
    queryKey: ["metrics", mvpOnly],
    queryFn: () => api.getMetrics(mvpOnly),
    refetchInterval: 15000,
  });
  const leadsQuery = useQuery({
    queryKey: ["leads", mvpOnly],
    queryFn: () => api.getLeads(mvpOnly),
    refetchInterval: 15000,
  });
  const exceptionsQuery = useQuery({
    queryKey: ["exceptions", mvpOnly],
    queryFn: () => api.getExceptions(mvpOnly),
    refetchInterval: 15000,
  });

  const captureBaseline = useMutation({
    mutationFn: () => api.captureBaseline(undefined, mvpOnly),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
    },
  });

  const error =
    metricsQuery.error ?? leadsQuery.error ?? exceptionsQuery.error;

  const baselineCapturedAt = metricsQuery.data?.baseline?.captured_at;

  return (
    <>
      <header className="glass p-5">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div>
            <h1 className="text-2xl font-semibold text-white">
              Sprint de Orquestacion de Leads
            </h1>
            <p className="mt-2 max-w-3xl text-sm text-slate-400">
              Panel operativo conectado a HubSpot. Cada lead debe quedar con origen,
              responsable, SLA y siguiente accion trazables.
            </p>
          </div>
          <div className="flex flex-wrap items-center gap-3">
            <label className="flex items-center gap-2 text-sm text-slate-300">
              <input
                type="checkbox"
                checked={!mvpOnly}
                onChange={(event) => setMvpOnly(!event.target.checked)}
                className="rounded border-slate-600 bg-slate-900"
              />
              Incluir todos los contactos HubSpot
            </label>
            <button
              type="button"
              onClick={() => captureBaseline.mutate()}
              disabled={captureBaseline.isPending || !!error}
              className="rounded-lg bg-cyan-500/20 px-3 py-2 text-sm text-cyan-100 hover:bg-cyan-500/30 disabled:opacity-50"
            >
              {captureBaseline.isPending ? "Capturando…" : "Capturar baseline"}
            </button>
          </div>
        </div>
        <p className="mt-3 text-xs text-slate-500">
          {mvpOnly
            ? "Metricas filtradas: solo contactos con lead_origen (leads del orquestador MVP)."
            : "Modo debug: incluye contactos HubSpot sin campos custom del sprint."}
          {baselineCapturedAt && (
            <>
              {" "}
              · Baseline:{" "}
              {new Date(baselineCapturedAt).toLocaleString("es-ES", {
                dateStyle: "medium",
                timeStyle: "short",
              })}
              {metricsQuery.data?.baseline?.note
                ? ` — ${metricsQuery.data.baseline.note}`
                : ""}
            </>
          )}
        </p>
      </header>

      {error && (
        <div className="glass border-rose-400/30 p-4 text-sm text-rose-200">
          {(error as Error).message}. Revisa HUBSPOT_ACCESS_TOKEN en .env y
          ejecuta <code className="text-rose-100">python -m api.hubspot_setup</code>.
        </div>
      )}

      {captureBaseline.error && (
        <div className="glass border-amber-400/30 p-4 text-sm text-amber-100">
          {(captureBaseline.error as Error).message}
        </div>
      )}

      <KpiGrid
        dashboard={metricsQuery.data}
        loading={metricsQuery.isLoading}
      />

      <div className="grid gap-6 xl:grid-cols-3">
        <div className="xl:col-span-2">
          <LeadTable
            leads={leadsQuery.data?.items ?? []}
            loading={leadsQuery.isLoading}
          />
        </div>
        <div className="space-y-6">
          <IngestForm />
          <ExceptionQueue
            exceptions={exceptionsQuery.data?.items ?? []}
            loading={exceptionsQuery.isLoading}
          />
        </div>
      </div>
    </>
  );
}
