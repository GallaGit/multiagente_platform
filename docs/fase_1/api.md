# API — Fase 1

Un solo endpoint. Sin autenticación en el MVP.

Proveedor por defecto: **Groq**. Ver [decisiones.md](decisiones.md).

## Endpoint

### `POST /chat`

Clasifica el mensaje y responde con el agente elegido.

**Request**

```json
{
  "message": "Necesito estimar una API REST en FastAPI para un CRM"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `message` | string | sí | Texto libre del usuario (no vacío) |

**Response 200**

```json
{
  "routed_to": "developer",
  "reply": "Para una API REST de CRM en FastAPI...",
  "reason": "Petición técnica de API y estimación"
}
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `routed_to` | string | `developer` o `business` |
| `reply` | string | Respuesta del agente elegido |
| `reason` | string | Motivo del Orchestrator (depuración) |

**Errores mínimos**

| Código | Cuándo |
|--------|--------|
| 400 | `message` ausente o vacío |
| 502 | Fallo del proveedor LLM |

## Variables de entorno

| Variable | Ejemplo | Descripción |
|----------|---------|-------------|
| `LLM_API_KEY` | `gsk_...` | Clave de Groq |
| `LLM_PROVIDER` | `groq` | Proveedor (MVP: solo `groq`) |
| `LLM_MODEL` | `llama-3.3-70b-versatile` | Modelo chat de Groq |

Plantilla: `.env.example`. No commitear `.env`.

## Comportamiento esperado

1. Validar `message`.
2. Llamar Orchestrator → obtener `agent` (+ `reason`).
3. Llamar al agente → obtener `reply`.
4. Devolver `{ "routed_to", "reply", "reason" }`.

## Ejemplo de prueba manual

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Prepara una propuesta para una clínica que quiere una web\"}"
```

Esperado: `routed_to` ≈ `business`.
