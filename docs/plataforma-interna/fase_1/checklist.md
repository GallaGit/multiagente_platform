# Checklist — módulo delivery

**Problema activo:** pérdida de leads por mala orquestación (asignación, SLA, seguimiento).  
**Entrega activa:** Sprint de Orquestación de Leads.  
**Prioridad:** producto externo antes de ampliar plataforma. Norte: [`.agents/rules/PROBLEMA.md`](../../../.agents/rules/PROBLEMA.md).

Orden recomendado para Orchestrator + Frontend + Backend **como subflujo de delivery**.  
Mapa empresa: [arquitectura-flujo.md](../arquitectura-flujo.md). Ver [decisiones.md](decisiones.md).

## 1. Estructura de agentes

- [x] `agents/orchestrator/`, `agents/frontend/`, `agents/backend/`
- [x] `system.md` de oficio (plantillas en [agentes.md](agentes.md); el nicho entra por pack)
- [x] Legacy `developer` / `business` deshabilitados en registry (archivos permanecen)

## 2. Carga de prompts

- [x] Leer `agents/<nombre>/system.md`
- [x] Fallar claro si no existe

## 3. Cliente LLM

- [x] `LLM_API_KEY`, `LLM_PROVIDER` (opcional `LLM_MODEL`)
- [x] `(system, user) -> str`
- [x] Groq SDK ([decisiones.md](decisiones.md))

## 4. Orchestrator → brief + route → FE|BE

- [x] Llamar Orchestrator con el encargo
- [x] Parsear `{ "agent", "reason", "brief" }`
- [x] Validar `agent` ∈ `{frontend, backend}` (fallback → `backend`)
- [x] Llamar agente con mensaje + `brief`
- [x] Devolver `routed_to` + `documentation` + `reply` + `reason`

## 5. FastAPI `/chat`

- [x] App con `POST /chat`
- [x] Contrato [api.md](api.md) (`documentation`, rutas FE/BE)
- [x] Body `message` no vacío
- [x] Research separado: `POST /research` (no routable en `/chat`)

## 6. Aceptación (delivery)

- [x] Mock: panel/UI → `frontend`
- [x] Mock: API/conector → `backend`
- [x] Prueba real con Groq (`LLM_API_KEY`; local Windows: `LLM_VERIFY_SSL=false` si falla SSL)

**HubSpot laboratorio:** propiedades custom de Contacts verificadas (`python -m api.hubspot_setup`). Flujo: [arquitectura-flujo.md](../arquitectura-flujo.md).
