import { ChatPanel } from "../components/agents/ChatPanel";
import { ResearchPanel } from "../components/agents/ResearchPanel";

export function AgentsPage() {
  return (
    <>
      <header className="glass p-5">
        <h1 className="text-2xl font-semibold text-white">Agentes internos</h1>
        <p className="mt-2 max-w-3xl text-sm text-slate-400">
          Orquestador multiagente para research, business y developer. Usa la
          misma API FastAPI que el CLI y Swagger.
        </p>
      </header>

      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <ChatPanel />
        </div>
        <ResearchPanel />
      </div>
    </>
  );
}
