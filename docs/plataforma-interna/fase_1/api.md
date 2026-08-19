# API — módulo delivery

Un solo endpoint para encargos de **delivery técnico** (no orquestación de toda la empresa).

Proveedor por defecto: **Groq**. Ver [decisiones.md](decisiones.md). Flujo: [arquitectura-flujo.md](../arquitectura-flujo.md).

## Endpoint

### `POST /chat`

El Orchestrator documenta el encargo y delega a `frontend` o `backend`.

**Request**

```json
{
  "message": "Necesito un webhook que registre leads de portal en el CRM con dueño y SLA"
}
```

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `message` | string | sí | Encargo de delivery (no vacío) |

**Response 200**

```json
{
  "routed_to": "backend",
  "documentation": "Objetivo: webhook portal→CRM. Alcance: alta de lead con dueño y SLA. Entregables: endpoint y reglas mínimas.",
  "reply": "Propongo FastAPI con endpoint de ingestión, deduplicación por email/teléfono...",
  "reason": "Encargo centrado en API, datos e integración"
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
| `LLM_MODEL` | `openai/gpt-oss-120b` | Modelo chat de Groq |

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
