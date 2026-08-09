# Fase 1 — Guía de implementación (MVP)

Visión y contexto: [roadmap/fase_1.md](../roadmap/fase_1.md).

Las rutas de esta guía son relativas a la **raíz del repositorio** (`agents/`, `api/`, `docs/`, …). No hay carpeta envoltorio `business-ai/`.

## Objetivo

Documentar la petición (brief) y delegar la implementación al agente correcto (`frontend` o `backend`).

## Agentes del MVP

| Agente | Rol |
|--------|-----|
| **Orchestrator** | Recibe la petición, redacta documentación breve y elige quién implementa |
| **Frontend** | Implementación UI (HTML/CSS/JS, React, UX de pantallas) |
| **Backend** | Implementación API, datos, auth, lógica de servidor |

El Orchestrator no implementa código: documenta y delega. Ante una petición full-stack, elige el foco principal (`frontend` o `backend`); llamar a ambos queda para más adelante.

## Stack

- Python
- FastAPI
- Groq (ver [decisiones.md](decisiones.md))
- Solo prompts (sin LangGraph, CrewAI ni AutoGen)

Sin frontend de producto en este MVP. Sin SQLite todavía.

## Qué entra

- Tres agentes como prompts en archivos `system.md`
- Un endpoint `POST /chat`
- Orchestrator → `brief` + ruta → Frontend | Backend
- Respuesta con documentación + implementación del agente elegido

## Qué no entra (fases posteriores)

- Knowledge separado por nicho
- Herramientas (GitHub, Gmail, CRM, etc.)
- Memoria persistente
- Orquestación multi-paso / FE+BE en el mismo request
- Automatizaciones (n8n)

## Criterios de hecho

1. `POST /chat` acepta `{ "message": "..." }`.
2. El Orchestrator produce `brief` (documentación) y elige `frontend` o `backend`.
3. Ese agente genera la respuesta de implementación (usando el mensaje y el `brief`).
4. La API devuelve `{ "routed_to", "documentation", "reply", "reason" }`.
5. Pruebas (mock y/o manual) pasan con:
   - mensaje de UI → `frontend`
   - mensaje de API/servidor → `backend`

## Documentos de esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [decisiones.md](decisiones.md) | Decisiones cerradas y cómo arrancar |
| [arquitectura.md](arquitectura.md) | Flujo y mapa de carpetas |
| [agentes.md](agentes.md) | Contratos y plantillas de prompts |
| [api.md](api.md) | Contrato del endpoint |
| [checklist.md](checklist.md) | Orden de implementación |
