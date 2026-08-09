# API — Fase 1

Un solo endpoint. Sin autenticación en el MVP.

Proveedor por defecto: **Groq**. Ver [decisiones.md](decisiones.md).

## Endpoint

### `POST /chat`

El Orchestrator documenta la petición y delega la implementación a `frontend` o `backend`.

**Request**

```json
{
  "message": "Necesito una API REST en FastAPI para un CRM"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `message` | string | sí | Texto libre del usuario (no vacío) |

**Response 200**

```json
{
  "routed_to": "backend",
  "documentation": "Objetivo: API REST CRM. Alcance: CRUD clientes. Entregables: endpoints y modelos.",
  "reply": "Propongo FastAPI con routers de clientes, Pydantic models...",
  "reason": "Petición centrada en API y servidor"
}
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `routed_to` | string | `frontend` o `backend` |
| `documentation` | string | Brief del Orchestrator |
| `reply` | string | Respuesta de implementación del agente elegido |
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
2. Llamar Orchestrator → obtener `agent`, `reason`, `brief`.
3. Llamar al agente elegido con mensaje + `brief` → obtener `reply`.
4. Devolver `{ "routed_to", "documentation", "reply", "reason" }` (`documentation` = `brief`).

## Ejemplo de prueba manual

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Diseña una pantalla de login con React\"}"
```

Esperado: `routed_to` ≈ `frontend`, con `documentation` no vacía.
