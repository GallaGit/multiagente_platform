# Fase 1 — Guía de implementación (MVP)

Visión y contexto: [roadmap/fase_1.md](../roadmap/fase_1.md).

Las rutas de esta guía son relativas a la **raíz del repositorio** (`agents/`, `api/`, `docs/`, …). No hay carpeta envoltorio `business-ai/`.

## Objetivo

Clasificar una petición del usuario y responder con el agente correcto (`developer` o `business`).

## Agentes del MVP

| Agente | Rol |
|--------|-----|
| **Orchestrator** | Recibe la petición y decide a quién enrutar |
| **Developer** | Requisitos, arquitectura y código |
| **Business** | Clientes, propuestas y organización |

`Business` unifica sales/marketing/org en esta fase. No se implementan finance, legal ni support todavía.

## Stack

- Python
- FastAPI
- Groq (ver [decisiones.md](decisiones.md))
- Solo prompts (sin LangGraph, CrewAI ni AutoGen)

Sin frontend. Sin SQLite todavía.

## Qué entra

- Tres agentes como prompts en archivos `system.md`
- Un endpoint `POST /chat`
- Enrutado Orchestrator → Developer | Business
- Respuesta del agente elegido

## Qué no entra (fases posteriores)

- Knowledge separado por nicho
- Herramientas (GitHub, Gmail, CRM, etc.)
- Memoria persistente
- Orquestación multi-paso con estados
- Automatizaciones (n8n)

## Criterios de hecho

1. `POST /chat` acepta `{ "message": "..." }`.
2. El Orchestrator elige `developer` o `business`.
3. Ese agente genera la respuesta.
4. La API devuelve `{ "routed_to": "...", "reply": "...", "reason": "..." }`.
5. `pytest` (LLM mockeado) y/o prueba manual con curl/Swagger pasan con:
   - un mensaje técnico → `developer`
   - un mensaje comercial → `business`

## Documentos de esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [decisiones.md](decisiones.md) | Decisiones cerradas y cómo arrancar |
| [arquitectura.md](arquitectura.md) | Flujo y mapa de carpetas |
| [agentes.md](agentes.md) | Contratos y plantillas de prompts |
| [api.md](api.md) | Contrato del endpoint |
| [checklist.md](checklist.md) | Orden de implementación |
