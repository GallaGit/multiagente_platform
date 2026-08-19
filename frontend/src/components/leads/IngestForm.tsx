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

export function IngestForm() {
  const [form, setForm] = useState(initial);
  const [feedback, setFeedback] = useState<string | null>(null);
  const queryClient = useQueryClient();

  const ingest = useMutation({
    mutationFn: api.ingestLead,
    onSuccess: (result) => {
      setFeedback(result.message);
      queryClient.invalidateQueries({ queryKey: ["leads"] });
      queryClient.invalidateQueries({ queryKey: ["metrics"] });
      queryClient.invalidateQueries({ queryKey: ["exceptions"] });
    },
    onError: (error: Error) => setFeedback(error.message),
  });

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setFeedback(null);
    ingest.mutate({
      ...form,
      nombre: form.nombre || undefined,
      email: form.email || undefined,
      telefono: form.telefono || undefined,
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
        <p className="mt-3 text-sm text-cyan-200">{feedback}</p>
      )}
    </div>
  );
}
