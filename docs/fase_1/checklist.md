# Checklist de implementación — Fase 1

Orden recomendado. Marca cada paso al completarlo.

## 1. Estructura de agentes

- [x] En la raíz del repo: crear `agents/orchestrator/`, `agents/developer/`, `agents/business/`
- [x] Añadir `system.md` en cada una (plantillas en [agentes.md](agentes.md))

## 2. Carga de prompts

- [x] Función que lea `agents/<nombre>/system.md` y devuelva el texto
- [x] Fallar claro si el archivo no existe

## 3. Cliente LLM

- [x] Configurar `LLM_API_KEY`, `LLM_PROVIDER` (y opcional `LLM_MODEL`)
- [x] Función mínima: `(system: str, user: str) -> str`
- [x] Groq vía SDK oficial `groq` ([decisiones.md](decisiones.md))

## 4. Orchestrator → route → agente

- [x] Llamar Orchestrator con el mensaje del usuario
- [x] Parsear JSON `{ "agent", "reason" }`
- [x] Validar `agent` ∈ `{developer, business}` (con fallback si falla)
- [x] Llamar al agente elegido con el mismo mensaje
- [x] Devolver `routed_to` + `reply` (+ `reason`)

## 5. FastAPI `/chat`

- [x] App FastAPI con `POST /chat` según [api.md](api.md)
- [x] Validar body (`message` no vacío)
- [ ] Arrancar servidor local y comprobar health/respuesta (manual)

## 6. Prueba de aceptación

- [x] Test con mock: mensaje técnico → `developer`
- [x] Test con mock: mensaje comercial → `business`
- [ ] Prueba real con Groq (curl o `/docs`) cuando haya `LLM_API_KEY`

Cuando los bloques de código estén hechos, Fase 1 está implementada. Siguiente: separar knowledge (Fase 2 del [roadmap](../roadmap/fase_1.md)).
