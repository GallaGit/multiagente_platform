import { FormEvent, useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { api } from "../../lib/api";

export function ResearchPanel() {
  const [cities, setCities] = useState("Valencia, Alicante");
  const [limit, setLimit] = useState(10);
  const [result, setResult] = useState<{
    reply: string;
    queries: string[];
    hits: number;
    note: string;
  } | null>(null);

  const research = useMutation({
    mutationFn: () =>
      api.research(
        cities.split(",").map((c) => c.trim()).filter(Boolean),
        limit,
      ),
    onSuccess: setResult,
  });

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    research.mutate();
  }

  return (
    <div className="glass p-5">
      <h2 className="mb-4 text-lg font-semibold text-white">
        Research ICP
      </h2>
      <form className="space-y-3" onSubmit={handleSubmit}>
        <input
          className="glass-input"
          placeholder="Ciudades separadas por coma"
          value={cities}
          onChange={(e) => setCities(e.target.value)}
        />
        <input
          className="glass-input"
          type="number"
          min={1}
          max={20}
          value={limit}
          onChange={(e) => setLimit(Number(e.target.value))}
        />
        <button type="submit" className="glass-btn" disabled={research.isPending}>
          {research.isPending ? "Investigando…" : "Ejecutar research"}
        </button>
      </form>

      {research.isError && (
        <p className="mt-3 text-sm text-rose-300">
          {(research.error as Error).message}
        </p>
      )}

      {result && (
        <div className="mt-4 space-y-3 rounded-xl border border-white/10 bg-white/5 p-4 text-sm">
          <div className="flex flex-wrap gap-2 text-xs text-slate-400">
            <span className="badge bg-cyan-500/20 text-cyan-200">
              {result.hits} resultados
            </span>
            {result.queries.map((q) => (
              <span key={q} className="badge bg-white/10 text-slate-300">
                {q}
              </span>
            ))}
          </div>
          <p className="whitespace-pre-wrap text-slate-200">{result.reply}</p>
          <p className="text-xs text-slate-500">{result.note}</p>
        </div>
      )}
    </div>
  );
}
