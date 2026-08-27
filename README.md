# Multiagent Business

**Problema que resolvemos:** en agencias inmobiliarias (ICP-01), los leads entran por portal/web/email y a menudo quedan sin dueño, SLA ni siguiente acción trazable en el CRM — respuesta tardía, duplicados y seguimiento abandonado.

**Producto activo:** [Sprint de Orquestación de Leads](docs/nichos/inmobiliaria/Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) — cada lead del alcance con origen, responsable, SLA, siguiente acción y resultado medible.

Norte corto para agentes y decisiones: [`.agents/rules/PROBLEMA.md`](.agents/rules/PROBLEMA.md) · protocolo: [`.agents/rules/ALINEACION.md`](.agents/rules/ALINEACION.md).

Nicho e investigación: [`docs/nichos/inmobiliaria/`](docs/nichos/inmobiliaria/). Brief técnico: [`docs/nichos/inmobiliaria/mvp/`](docs/nichos/inmobiliaria/mvp/).

## Laboratorio en este repo

Dashboard + API + agentes internos validan la orquestación en local con **HubSpot** (Private App + Contacts + propiedades custom). Canal simulado vía `/leads/ingest` y `/webhooks/lead`. No redefinen el problema ni son el CRM que se vende a agencias españolas (Witei/Inmovilla en entrega cliente).

## Qué incluye

| Área | Descripción |
|------|-------------|
| **Panel Leads** (`/`) | KPIs, tabla, cola de excepciones, ingesta simulada portal → HubSpot |
| **Panel Agentes** (`/agentes`) | Chat orquestador + research ICP vía Groq |
| **API** | FastAPI: `/leads/*`, `/webhooks/lead`, `/chat`, `/research` |

> **Nota dashboard:** por defecto los KPIs cuentan **solo leads MVP** (contactos con `lead_origen`). Activa “Incluir todos los contactos HubSpot” para debug. Baseline: botón en panel o `POST /leads/baseline`. Ver [06-metricas](docs/nichos/inmobiliaria/mvp/06-metricas.md).

## Arquitectura

```text
Frontend (React + Vite, :5173)
        |  proxy /api → :8000
        v
   FastAPI (uvicorn :8000 — Docker Compose o venv)
   /    |     \
  v     v      v
Leads  Chat  Research
  |       \    /
  v        Groq (openai/gpt-oss-120b)
HubSpot CRM (Private App token)
```

Datos en **HubSpot**; no hay base de datos en este repo. Compose no incluye Postgres.

## Requisitos

- Python 3.11+ (ruta venv) o [Docker Engine + Compose](https://docs.docker.com/compose/) (ruta recomendada)
- Node.js 18+ y npm (solo si arrancas el frontend fuera de Docker)
- [Groq API key](https://console.groq.com/keys)
- [HubSpot Private App](https://developers.hubspot.com/docs/api/private-apps) con Access Token `pat-...`

## Instalación backend

Con Docker solo hace falta `.env` (siguiente bloque). La ruta venv:

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
LLM_VERIFY_SSL=true             # false en Windows si falla SSL local
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
# o: docker compose run --rm api python -m api.hubspot_setup
```

4. Debe existir al menos un **owner** en HubSpot (round-robin).

### Composio (opcional, agentes Cursor)

Conectar HubSpot vía Composio MCP da acceso a los agentes del **chat de Cursor**. **No sustituye** el Private App token del backend FastAPI.

## Instalación frontend

Solo si no usas Compose:

```bash
cd frontend
npm install
```

Versiones pinneadas (cutoff supply-chain): ver [`frontend/SECURITY.md`](frontend/SECURITY.md).

Si `npm install` falla por SSL en Windows (`UNABLE_TO_VERIFY_LEAF_SIGNATURE`), usa `npm install --strict-ssl=false` solo en local.

## Ejecución con Docker (recomendado)

Misma UI (:5173) y API (:8000) que la ruta venv/npm. Copia `.env.example` → `.env` y rellena claves (nunca commitear `.env`):

```bash
cp .env.example .env
docker compose up --build
```

- UI: <http://127.0.0.1:5173> (Vite hace proxy de `/api` al servicio `api`)
- API / Swagger: <http://127.0.0.1:8000/docs>
- Health: <http://127.0.0.1:8000/health>

El contenedor API escucha en `0.0.0.0:8000`. Compose monta `./data` para persistir el baseline local. Parar: `docker compose down`.

Si ya tienes uvicorn o Vite en esos puertos, detenlos antes.

## Ejecución sin Docker (venv + npm)

Sigue siendo válida para desarrollo con recarga. Dos terminales, con `.env` y dependencias instaladas (secciones anteriores):

```bash
# Terminal 1 — API
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000

# Terminal 2 — UI
cd frontend && npm run dev
```

Mismos URLs que con Compose. Evita dejar varias instancias de uvicorn en el puerto 8000 (pueden servir código/env antiguos).

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
curl -X POST http://127.0.0.1:8000/leads/baseline \
  -H "Content-Type: application/json" \
  -d '{"note":"Lab día 0","mvp_only":true}'
curl http://127.0.0.1:8000/leads/baseline
```

## Tests

```bash
python -m pytest
```

Leads usan HubSpot mockeado; no requieren token real.

## Estructura

```text
.
├── Dockerfile           # API (python:3.12-slim, uvicorn 0.0.0.0:8000)
├── docker-compose.yml   # api + frontend; sin base de datos
├── agents/
├── api/
│   ├── leads/           # HubSpot client + orquestación + rutas
│   ├── hubspot_setup.py
│   └── main.py
├── frontend/            # React + Vite + Tailwind
│   ├── Dockerfile       # UI (Vite :5173, proxy /api → api:8000)
│   └── SECURITY.md      # Regla de versiones npm (cutoff 2026-08-01)
├── docs/
└── tests/
```

## Limitaciones

- Sin auth en API/UI (solo local).
- Docker Compose es laboratorio local, no un despliegue a producción.
- **No listo para producción SaaS** — ver [docs/READINESS.md](docs/READINESS.md).
- Métricas MVP filtradas por `lead_origen` (default); baseline local en `data/baseline.json`.
- Tasks nativas opcionales si el portal no expone el scope.
- Witei/Inmovilla = piloto en cuenta del cliente, no este laboratorio.
- Research no hace outreach; cumplimiento RGPD/LSSI manual.

## Cumplimiento

La investigación usa evidencia pública. No se automatiza outreach comercial sin aprobación humana.
