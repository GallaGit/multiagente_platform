import { FormEvent, useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { api, type LeadIngestPayload } from "../../lib/api";

const initial: LeadIngestPayload = {
  nombre: "",
  email: "",
  telefono: "",
  origen: "portal",
  origen_ref: "",
  inmueble_ref: "",
  mensaje: "",
};

const actionLabels: Record<string, string> = {
  created: "Lead nuevo",
  duplicate: "Duplicado",
  exception: "Excepción",
};

type Feedback =
  | { kind: "success"; action: string; message: string }
  | { kind: "error"; message: string };

export function IngestForm() {
  const [form, setForm] = useState(initial);
  const [feedback, setFeedback] = useState<Feedback | null>(null);
  const queryClient = useQueryClient();

  const ingest = useMutation({
    mutationFn: api.ingestLead,
    onSuccess: (result) => {
      setFeedback({
        kind: "success",
        action: result.action,
        message: result.message,
      });
      setForm(initial);
      queryClient.invalidateQueries({ queryKey: ["leads"] });
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
      queryClient.invalidateQueries({ queryKey: ["exceptions"] });
    },
    onError: (error: Error) =>
      setFeedback({ kind: "error", message: error.message }),
  });

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setFeedback(null);

    const email = form.email?.trim() ?? "";
    const telefono = form.telefono?.trim() ?? "";
    if (!email && !telefono) {
      setFeedback({
        kind: "error",
        message: "Indica email o teléfono para ingestar el lead.",
      });
      return;
    }

    ingest.mutate({
      ...form,
      nombre: form.nombre || undefined,
      email: email || undefined,
      telefono: telefono || undefined,
      origen_ref: form.origen_ref || undefined,
      inmueble_ref: form.inmueble_ref || undefined,
      mensaje: form.mensaje || undefined,
    });
  }

  function setField<K extends keyof LeadIngestPayload>(
    key: K,
    value: LeadIngestPayload[K],
  ) {
    setForm((prev) => ({ ...prev, [key]: value }));
  }

  return (
    <div className="glass p-5">
      <h2 className="mb-4 text-lg font-semibold text-white">
        Simular lead de portal
      </h2>
      <form className="grid gap-3 md:grid-cols-2" onSubmit={handleSubmit}>
        <input
          className="glass-input"
          placeholder="Nombre"
          value={form.nombre ?? ""}
          onChange={(e) => setField("nombre", e.target.value)}
        />
        <input
          className="glass-input"
          placeholder="Email"
          type="email"
          value={form.email ?? ""}
          onChange={(e) => setField("email", e.target.value)}
        />
        <input
          className="glass-input"
          placeholder="Telefono"
          value={form.telefono ?? ""}
          onChange={(e) => setField("telefono", e.target.value)}
        />
        <input
          className="glass-input"
          placeholder="Origen (portal, web…)"
          value={form.origen ?? "portal"}
          onChange={(e) => setField("origen", e.target.value)}
        />
        <input
          className="glass-input"
          placeholder="Referencia origen"
          value={form.origen_ref ?? ""}
          onChange={(e) => setField("origen_ref", e.target.value)}
        />
        <input
          className="glass-input"
          placeholder="Referencia inmueble"
          value={form.inmueble_ref ?? ""}
          onChange={(e) => setField("inmueble_ref", e.target.value)}
        />
        <textarea
          className="glass-input md:col-span-2"
          placeholder="Mensaje del interesado"
          rows={3}
          value={form.mensaje ?? ""}
          onChange={(e) => setField("mensaje", e.target.value)}
        />
        <div className="flex flex-wrap items-center gap-3 md:col-span-2">
          <button type="submit" className="glass-btn" disabled={ingest.isPending}>
            {ingest.isPending ? "Ingestando…" : "Ingestar lead"}
          </button>
          <button
            type="button"
            className="glass-btn-ghost"
            onClick={() => {
              setFeedback(null);
              setForm({
                ...initial,
                nombre: "Ana Ejemplo",
                email: "ana.demo@example.com",
                telefono: "612345678",
                inmueble_ref: "REF-001",
                mensaje: "Interesada en visitar esta semana",
              });
            }}
          >
            Rellenar demo
          </button>
        </div>
      </form>
      {feedback && (
        <div
          className={`mt-3 rounded-lg border p-3 text-sm ${
            feedback.kind === "success"
              ? "border-emerald-400/30 bg-emerald-500/10 text-emerald-100"
              : "border-rose-400/30 bg-rose-500/10 text-rose-100"
          }`}
        >
          {feedback.kind === "success" && (
            <p className="mb-1 text-xs font-medium uppercase tracking-wide text-emerald-300">
              {actionLabels[feedback.action] ?? feedback.action}
            </p>
          )}
          <p>{feedback.message}</p>
        </div>
      )}
    </div>
  );
}
