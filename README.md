# Multiagent Business

MVP unificado: **dashboard glassmorphism** + **orquestación de leads (HubSpot)** + **agentes internos** (research, business, developer).

El nicho activo (inmobiliaria) vive en [`docs/nichos/inmobiliaria/`](docs/nichos/inmobiliaria/). El brief del producto vendible está en [`docs/nichos/inmobiliaria/mvp/`](docs/nichos/inmobiliaria/mvp/).

## Qué incluye

| Área | Descripción |
|------|-------------|
| **Panel Leads** (`/`) | KPIs, tabla, cola de excepciones, ingesta simulada portal → HubSpot |
| **Panel Agentes** (`/agentes`) | Chat orquestador + research ICP vía Groq |
| **API** | FastAPI: `/leads/*`, `/webhooks/lead`, `/chat`, `/research` |

HubSpot es el **CRM de laboratorio** (sustituto operativo de Witei mientras no haya cuenta inmobiliaria real).

> **Nota dashboard:** sin filtro, los KPIs cuentan **contactos del portal HubSpot** (hasta 100), no solo leads creados por el MVP. Los ingestados por el orquestador llevan campos custom (`lead_origen`, `lead_estado`, `siguiente_accion`, etc.).

## Arquitectura

```text
Frontend (React + Vite, :5173)
        |  proxy /api → :8000
        v
   FastAPI (local, uvicorn — sin Docker en este repo)
   /    |     \
  v     v      v
Leads  Chat  Research
  |       \    /
  v        Groq (openai/gpt-oss-120b)
HubSpot CRM (Private App token)
```

## Requisitos

- Python 3.11+
- Node.js 18+ y npm
- [Groq API key](https://console.groq.com/keys)
- [HubSpot Private App](https://developers.hubspot.com/docs/api/private-apps) con Access Token `pat-...`

## Instalación backend

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
cp .env.example .env
```

Completa `.env` (nunca commitear `.env`):

```env
LLM_API_KEY=tu_clave_groq
LLM_PROVIDER=groq
LLM_MODEL=openai/gpt-oss-120b
HUBSPOT_ACCESS_TOKEN=pat-eu1-...
HUBSPOT_PORTAL_ID=              # opcional
HUBSPOT_VERIFY_SSL=true         # false en Windows si falla SSL local
SLA_MINUTES=60
```

### Configurar HubSpot

1. Crea una **Private App** (privada / una cuenta). Scopes mínimos:
   - `crm.objects.contacts.read` / `write`
   - `crm.objects.owners.read`
   - `crm.schemas.contacts.read` / `write`
   - `crm.objects.tasks.write` — **opcional**; en muchas cuentas free/legacy no aparece. Sin él, el contacto se crea igual y la tarea se omite con aviso.
2. Copia el **Access token** completo (`pat-eu1-...`) a `HUBSPOT_ACCESS_TOKEN`.
3. Crea propiedades custom:

```bash
python -m api.hubspot_setup
```

4. Debe existir al menos un **owner** en HubSpot (round-robin).

### Composio (opcional, agentes Cursor)

Conectar HubSpot vía Composio MCP da acceso a los agentes del **chat de Cursor**. **No sustituye** el Private App token del backend FastAPI.

## Instalación frontend

```bash
cd frontend
npm install
```

Versiones pinneadas (cutoff supply-chain): ver [`frontend/SECURITY.md`](frontend/SECURITY.md).

Si `npm install` falla por SSL en Windows (`UNABLE_TO_VERIFY_LEAF_SIGNATURE`), usa `npm install --strict-ssl=false` solo en local.

## Ejecución (desarrollo local)

No hay Docker para esta API. Dos terminales:

```bash
# Terminal 1 — API
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2 — UI
cd frontend && npm run dev
```

- UI: <http://127.0.0.1:5173>
- API / Swagger: <http://127.0.0.1:8000/docs>
- Health: <http://127.0.0.1:8000/health>

Evita dejar varias instancias de uvicorn en el puerto 8000 (pueden servir código/env antiguos).

## Checklist demo (3 casos)

1. **Lead nuevo** — email + teléfono → contacto asignado (+ tarea si hay scope).
2. **Duplicado** — mismo email → update, mismo owner.
3. **Datos insuficientes** — solo nombre → excepción `DATOS_INSUFICIENTES`.

## API de leads (resumen)

```bash
curl -X POST http://127.0.0.1:8000/leads/ingest \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","email":"ana@demo.com","telefono":"612345678","origen":"portal","inmueble_ref":"REF-001"}'

curl http://127.0.0.1:8000/leads
curl http://127.0.0.1:8000/leads/metrics
curl http://127.0.0.1:8000/leads/exceptions
```

## Tests

```bash
python -m pytest
```

Leads usan HubSpot mockeado; no requieren token real.

## Estructura

```text
.
├── agents/
├── api/
│   ├── leads/           # HubSpot client + orquestación + rutas
│   ├── hubspot_setup.py
│   └── main.py
├── frontend/            # React + Vite + Tailwind
│   └── SECURITY.md      # Regla de versiones npm (cutoff 2026-08-01)
├── docs/
└── tests/
```

## Limitaciones

- Sin auth en API/UI (solo local).
- Sin Docker en este repo.
- Panel Leads lista contactos HubSpot (no solo leads MVP) hasta filtrar por campos custom.
- Tasks nativas opcionales si el portal no expone el scope.
- Witei/Inmovilla = piloto en cuenta del cliente, no este laboratorio.
- Research no hace outreach; cumplimiento RGPD/LSSI manual.

## Cumplimiento

La investigación usa evidencia pública. No se automatiza outreach comercial sin aprobación humana.
