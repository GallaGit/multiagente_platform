import { FormEvent, useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { api } from "../../lib/api";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  meta?: { routed_to?: string; reason?: string; documentation?: string };
}

export function ChatPanel() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  const chat = useMutation({
    mutationFn: api.chat,
    onSuccess: (data, variables) => {
      setMessages((prev) => [
        ...prev,
        { role: "user", content: variables },
        {
          role: "assistant",
          content: data.reply,
          meta: {
            routed_to: data.routed_to,
            reason: data.reason,
            documentation: data.documentation,
          },
        },
      ]);
      setInput("");
    },
  });

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    const trimmed = input.trim();
    if (!trimmed || chat.isPending) return;
    chat.mutate(trimmed);
  }

  return (
    <div className="glass flex h-full min-h-[520px] flex-col p-5">
      <h2 className="mb-4 text-lg font-semibold text-white">
        Chat delivery
      </h2>

      <div className="flex-1 space-y-3 overflow-y-auto pr-1">
        {messages.length === 0 && (
          <p className="text-sm text-slate-400">
            Encargos técnicos del sprint: paneles/UI → frontend; API,
            webhooks o conectores CRM → backend. El orchestrator documenta
            un brief y delega. Research ICP usa el panel de Research.
          </p>
        )}
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`rounded-2xl px-4 py-3 text-sm ${
              msg.role === "user"
                ? "ml-8 bg-violet-500/20 text-violet-50"
                : "mr-8 bg-white/10 text-slate-100"
            }`}
          >
            <p className="whitespace-pre-wrap">{msg.content}</p>
            {msg.meta?.routed_to && (
              <div className="mt-2 space-y-1 text-xs text-cyan-300/80">
                <p>
                  → {msg.meta.routed_to} · {msg.meta.reason}
                </p>
                {msg.meta.documentation && (
                  <p className="text-slate-400">
                    Brief: {msg.meta.documentation}
                  </p>
                )}
              </div>
            )}
          </div>
        ))}
      </div>

      <form className="mt-4 flex gap-2" onSubmit={handleSubmit}>
        <input
          className="glass-input flex-1"
          placeholder="Escribe un encargo de delivery…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit" className="glass-btn" disabled={chat.isPending}>
          Enviar
        </button>
      </form>
      {chat.isError && (
        <p className="mt-2 text-sm text-rose-300">
          {(chat.error as Error).message}
        </p>
      )}
    </div>
  );
}
