# Módulo delivery — Orchestrator / Frontend / Backend

> **Alcance:** capa de **delivery técnico** dentro de la plataforma interna.  
> No es el flujo completo de la empresa.  
> Mapa: [arquitectura-flujo.md](../arquitectura-flujo.md) · Norte: [docs/README.md](../../README.md) · [plataforma](../README.md)

Evolución de capacidades: [roadmap-fase_1.md](../roadmap-fase_1.md).

Rutas de código relativas a la **raíz del repositorio** (`agents/`, `api/`, `docs/`, …).

## Objetivo

Dado un **encargo de delivery** (p. ej. panel de excepciones, conector CRM–canal, webhook de leads), documentar el brief y delegar a Frontend o Backend.

El Orchestrator **no** dirige comercial, ops ni QA de toda la empresa; solo este subflujo.

## Agentes de este módulo

| Agente | Rol en el nicho |
|--------|-----------------|
| **Orchestrator** | Brief del encargo + ruta FE o BE |
| **Frontend** | UI: paneles, demos, UX del control operativo del sprint |
| **Backend** | API, datos, auth, webhooks, conectores CRM/canal |

Ante un encargo full-stack, elegir el foco principal; llamar a ambos queda para orquestación multi-paso.

## Stack

- Python, FastAPI, Groq (ver [decisiones.md](decisiones.md))
- Solo prompts al inicio (sin LangGraph / CrewAI / AutoGen)

Sin producto SaaS de cliente en este módulo. Sin SQLite obligatorio aún.

## Qué entra

- Tres agentes como `system.md` (modelo objetivo: orchestrator, frontend, backend)
- `POST /chat` orientado a encargos de delivery
- Orchestrator → `brief` + ruta → Frontend \| Backend
- Respuesta con documentación + implementación del agente elegido

## Qué no entra aquí

- Roles de empresa (sales, ops, QA, support) — ver [arquitectura-flujo.md](../arquitectura-flujo.md)
- Knowledge del nicho cableado (fase posterior del roadmap)
- Herramientas CRM/Gmail/GitHub, memoria, multi-paso FE+BE, n8n

## Criterios de hecho (módulo delivery)

1. `POST /chat` acepta `{ "message": "..." }`.
2. Orchestrator produce `brief` y elige `frontend` o `backend`.
3. Ese agente responde con el mensaje + `brief`.
4. API: `{ "routed_to", "documentation", "reply", "reason" }`.
5. Pruebas: UI/panel → `frontend`; API/conector → `backend`.

Código actual puede seguir en `developer` / `business` hasta realinear; no bloquea el producto externo (Sprint de Leads).

## Documentos

| Archivo | Contenido |
|---------|-----------|
| [decisiones.md](decisiones.md) | Decisiones y arranque |
| [arquitectura.md](arquitectura.md) | Flujo técnico del módulo |
| [agentes.md](agentes.md) | Contratos y plantillas |
| [api.md](api.md) | Contrato del endpoint |
| [checklist.md](checklist.md) | Orden de implementación |
