# Checklist de implementación — Fase 1

Orden recomendado. Modelo objetivo: Orchestrator (documenta) + Frontend + Backend.
Ver [decisiones.md](decisiones.md) (incluye deuda de código).

## 1. Estructura de agentes

- [ ] En la raíz: `agents/orchestrator/`, `agents/frontend/`, `agents/backend/`
- [ ] `system.md` en cada una (plantillas en [agentes.md](agentes.md))
- [x] ~~Versión antigua~~ `developer` / `business` (código legacy; realinear o retirar)

## 2. Carga de prompts

- [x] Función que lea `agents/<nombre>/system.md` y devuelva el texto
- [x] Fallar claro si el archivo no existe

## 3. Cliente LLM

- [x] Configurar `LLM_API_KEY`, `LLM_PROVIDER` (y opcional `LLM_MODEL`)
- [x] Función mínima: `(system: str, user: str) -> str`
- [x] Groq vía SDK oficial `groq` ([decisiones.md](decisiones.md))

## 4. Orchestrator → documentar + route → agente

- [ ] Llamar Orchestrator con el mensaje del usuario
- [ ] Parsear JSON `{ "agent", "reason", "brief" }`
- [ ] Validar `agent` ∈ `{frontend, backend}` (fallback → `backend`)
- [ ] Llamar al agente elegido con mensaje + `brief`
- [ ] Devolver `routed_to` + `documentation` + `reply` + `reason`
- [x] ~~Versión antigua~~ route a `developer`/`business` sin `brief` (pendiente reemplazar)

## 5. FastAPI `/chat`

- [x] App FastAPI con `POST /chat` (base existente)
- [ ] Alinear contrato a [api.md](api.md) (`documentation`, rutas FE/BE)
- [x] Validar body (`message` no vacío)
- [ ] Arrancar servidor local y comprobar respuesta (manual)

## 6. Prueba de aceptación

- [ ] Test con mock: mensaje UI → `frontend` (+ `documentation`)
- [ ] Test con mock: mensaje API → `backend` (+ `documentation`)
- [ ] Prueba real con Groq (curl o `/docs`) cuando haya `LLM_API_KEY`
- [x] ~~Tests antiguos~~ `developer` / `business` (actualizar al realinear código)

Cuando el código esté realineado con esta guía, Fase 1 queda cerrada en el nuevo modelo. Siguiente: knowledge (Fase 2 del [roadmap](../roadmap/fase_1.md)).
