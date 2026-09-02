import { NavLink, Outlet } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { api } from "../../lib/api";

const navClass = ({ isActive }: { isActive: boolean }) =>
  [
    "flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm font-medium transition",
    isActive
      ? "bg-white/15 text-white shadow-inner"
      : "text-slate-300 hover:bg-white/10 hover:text-white",
  ].join(" ");

export function GlassShell() {
  const health = useQuery({
    queryKey: ["health"],
    queryFn: api.health,
    refetchInterval: 30000,
  });

  return (
    <div className="min-h-screen">
      <div className="pointer-events-none fixed inset-0 overflow-hidden">
        <div className="absolute -left-24 top-10 h-72 w-72 rounded-full bg-violet-500/20 blur-3xl" />
        <div className="absolute bottom-0 right-0 h-96 w-96 rounded-full bg-cyan-500/15 blur-3xl" />
      </div>

      <div className="relative mx-auto flex min-h-screen max-w-[1600px] gap-6 p-4 md:p-6">
        <aside className="glass flex w-full shrink-0 flex-col gap-6 p-5 md:w-64">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-cyan-300/80">
              Multiagent
            </p>
            <h1 className="mt-1 text-xl font-semibold text-white">
              Business MVP
            </h1>
            <p className="mt-2 text-xs leading-relaxed text-slate-400">
              Orquestacion de leads + agentes internos
            </p>
          </div>

          <nav className="flex flex-col gap-2">
            <NavLink to="/" end className={navClass}>
              Panel Leads
            </NavLink>
            <NavLink to="/agentes" className={navClass}>
              Agentes
            </NavLink>
          </nav>

          <div className="mt-auto space-y-2 text-xs text-slate-400">
            <div className="flex items-center gap-2">
              <span
                className={`h-2 w-2 rounded-full ${
                  health.isSuccess
                    ? "bg-emerald-400"
                    : health.isError
                      ? "bg-rose-400"
                      : "bg-amber-400"
                }`}
              />
              API{" "}
              {health.isSuccess
                ? "conectada"
                : health.isError
                  ? "error"
                  : "conectando…"}
            </div>
            {health.isError && (
              <p className="text-rose-300">
                {(health.error as Error).message}
              </p>
            )}
            <p>HubSpot como CRM de laboratorio</p>
          </div>
        </aside>

        <main className="flex min-w-0 flex-1 flex-col gap-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
