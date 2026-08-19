import { useQuery } from "@tanstack/react-query";
import { api } from "../lib/api";
import { ExceptionQueue } from "../components/leads/ExceptionQueue";
import { IngestForm } from "../components/leads/IngestForm";
import { KpiGrid } from "../components/leads/KpiGrid";
import { LeadTable } from "../components/leads/LeadTable";

export function LeadsPage() {
  const metricsQuery = useQuery({
    queryKey: ["metrics"],
    queryFn: api.getMetrics,
    refetchInterval: 15000,
  });
  const leadsQuery = useQuery({
    queryKey: ["leads"],
    queryFn: api.getLeads,
    refetchInterval: 15000,
  });
  const exceptionsQuery = useQuery({
    queryKey: ["exceptions"],
    queryFn: api.getExceptions,
    refetchInterval: 15000,
  });

  const error =
    metricsQuery.error ?? leadsQuery.error ?? exceptionsQuery.error;

  return (
    <>
      <header className="glass p-5">
        <h1 className="text-2xl font-semibold text-white">
          Sprint de Orquestacion de Leads
        </h1>
        <p className="mt-2 max-w-3xl text-sm text-slate-400">
          Panel operativo conectado a HubSpot. Cada lead debe quedar con origen,
          responsable, SLA y siguiente accion trazables.
        </p>
      </header>

      {error && (
        <div className="glass border-rose-400/30 p-4 text-sm text-rose-200">
          {(error as Error).message}. Revisa HUBSPOT_ACCESS_TOKEN en .env y
          ejecuta <code className="text-rose-100">python -m api.hubspot_setup</code>.
        </div>
      )}

      <KpiGrid metrics={metricsQuery.data} loading={metricsQuery.isLoading} />

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
