# Checklist — módulo delivery

Orden recomendado para Orchestrator + Frontend + Backend **como subflujo de delivery**.  
Mapa empresa: [arquitectura-flujo.md](../arquitectura-flujo.md). Ver [decisiones.md](decisiones.md).

## 1. Estructura de agentes

- [ ] `agents/orchestrator/`, `agents/frontend/`, `agents/backend/`
- [ ] `system.md` de oficio (plantillas en [agentes.md](agentes.md); el nicho entra por pack)
- [x] ~~Legacy~~ `developer` / `business` (puede permanecer hasta realinear)

## 2. Carga de prompts

- [x] Leer `agents/<nombre>/system.md`
- [x] Fallar claro si no existe

## 3. Cliente LLM

- [x] `LLM_API_KEY`, `LLM_PROVIDER` (opcional `LLM_MODEL`)
- [x] `(system, user) -> str`
- [x] Groq SDK ([decisiones.md](decisiones.md))

## 4. Orchestrator → brief + route → FE|BE

- [ ] Llamar Orchestrator con el encargo
- [ ] Parsear `{ "agent", "reason", "brief" }`
- [ ] Validar `agent` ∈ `{frontend, backend}` (fallback → `backend`)
- [ ] Llamar agente con mensaje + `brief`
- [ ] Devolver `routed_to` + `documentation` + `reply` + `reason`
- [x] ~~Legacy~~ route a `developer`/`business` sin `brief`

## 5. FastAPI `/chat`

- [x] App con `POST /chat`
- [ ] Contrato [api.md](api.md) (`documentation`, rutas FE/BE)
- [x] Body `message` no vacío
- [ ] Prueba manual local

## 6. Aceptación (delivery)

- [ ] Mock: panel/UI → `frontend`
- [ ] Mock: API/conector → `backend`
- [ ] Prueba real con Groq si hay `LLM_API_KEY`

**Prioridad:** producto externo (Sprint de Leads) antes de realinear este módulo. Flujo: [arquitectura-flujo.md](../arquitectura-flujo.md).
