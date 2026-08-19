# Multiagent Business

MVP unificado: **dashboard glassmorphism** + **orquestación de leads (HubSpot)** + **agentes internos** (research, business, developer).

El nicho activo (inmobiliaria) vive en [`docs/nichos/inmobiliaria/`](docs/nichos/inmobiliaria/). El brief del producto vendible está en [`docs/nichos/inmobiliaria/mvp/`](docs/nichos/inmobiliaria/mvp/).

## Qué incluye

| Área | Descripción |
|------|-------------|
| **Panel Leads** | KPIs, tabla, cola de excepciones, ingesta simulada de portal → HubSpot |
| **Panel Agentes** | Chat orquestador + research ICP vía Groq |
| **API** | FastAPI: `/leads/*`, `/webhooks/lead`, `/chat`, `/research` |

HubSpot actúa como CRM de laboratorio (sustituto operativo de Witei para validar el flujo sin cuenta inmobiliaria).

## Arquitectura

```text
Frontend (React + Vite, :5173)
        |  proxy /api → :8000
        v
   FastAPI API
   /    |     \
  v     v      v
Leads  Chat  Research
  |       \    /
  v        Groq
HubSpot CRM
```

## Requisitos

- Python 3.11+
- Node.js 18+ y npm
- [Groq API key](https://console.groq.com/keys) (agentes)
- [HubSpot Private App](https://developers.hubspot.com/docs/api/private-apps) (panel de leads)

## Instalación backend

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
cp .env.example .env
```

Completa `.env`:

```env
LLM_API_KEY=tu_clave_groq
HUBSPOT_ACCESS_TOKEN=tu_token_private_app
SLA_MINUTES=60
```

### Configurar HubSpot

1. Crea una **Private App** en HubSpot con scopes:
   - `crm.objects.contacts.read` / `write`
   - `crm.objects.tasks.write`
   - `crm.objects.owners.read`
   - `crm.schemas.contacts.read` / `write`
2. Copia el access token a `HUBSPOT_ACCESS_TOKEN`.
3. Crea las propiedades custom en contactos:

```bash
python -m api.hubspot_setup
```

4. Asegúrate de tener al menos un **owner** (usuario) en la cuenta HubSpot para el round-robin.

## Instalación frontend

```bash
cd frontend
npm install
```

## Ejecución (desarrollo)

Terminal 1 — API:

```bash
uvicorn api.main:app --reload
```

Terminal 2 — UI:

```bash
cd frontend
npm run dev
```

Abre <http://localhost:5173>

- **/** — Panel de leads (HubSpot)
- **/agentes** — Chat y research

API docs: <http://127.0.0.1:8000/docs>

## Checklist demo (3 casos)

1. **Lead nuevo:** formulario con email + teléfono → contacto en HubSpot con responsable y tarea.
2. **Duplicado:** reenviar mismo email → actualiza contacto, no segundo owner.
3. **Datos insuficientes:** solo nombre → excepción `DATOS_INSUFICIENTES` en cola.

## API de leads (resumen)

```bash
# Ingestar lead simulado
curl -X POST http://127.0.0.1:8000/leads/ingest \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","email":"ana@demo.com","telefono":"612345678","origen":"portal","inmueble_ref":"REF-001"}'

# Listar leads y métricas
curl http://127.0.0.1:8000/leads
curl http://127.0.0.1:8000/leads/metrics
curl http://127.0.0.1:8000/leads/exceptions
```

## Tests

```bash
python -m pytest
```

Los tests de leads usan un cliente HubSpot simulado; no requieren token real.

## Estructura del proyecto

```text
.
├── agents/           # Prompts de orchestrator, research, business, developer
├── api/
│   ├── leads/        # Orquestación + HubSpot + rutas /leads
│   ├── hubspot_setup.py
│   └── main.py
├── frontend/         # React + Vite + Tailwind (glassmorphism)
├── docs/
└── tests/
```

## Limitaciones actuales

- Sin autenticación en API ni UI (solo desarrollo local).
- HubSpot es el CRM de laboratorio; Witei/Inmovilla quedan para piloto en cuenta del cliente.
- Chat/research sin memoria entre sesiones.
- Research no contacta prospectos; cumplimiento RGPD/LSSI manual.

## Cumplimiento

La investigación usa evidencia pública. Este proyecto no automatiza outreach comercial sin aprobación humana.
