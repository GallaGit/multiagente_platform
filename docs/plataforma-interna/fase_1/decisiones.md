# Decisiones — módulo delivery

Registro para no repetir debates. Actualizar solo si cambia una decisión.

| Decisión | Valor | Fecha |
|----------|--------|-------|
| Ubicación | Orchestrator / FE / BE = **capa delivery** dentro del flujo empresa, no el SO completo | 2026-08-12 |
| Alcance del módulo | Orchestrator documenta (brief) + delega a Frontend o Backend | 2026-08-09 |
| LLM | Groq (`LLM_PROVIDER=groq`) | 2026-08-05 |
| Cliente | SDK oficial `groq` (`from groq import Groq`) | 2026-08-05 |
| Modelo por defecto | `llama-3.3-70b-versatile` | 2026-08-05 |
| Agentes del módulo | `orchestrator`, `frontend`, `backend` | 2026-08-09 |
| Respuesta API | `{ routed_to, documentation, reply, reason }` | 2026-08-09 |
| Fallback de ruta | Si el JSON del Orchestrator falla → `backend` | 2026-08-09 |
| Full-stack | Elegir foco principal; no llamar FE+BE en el mismo request (aún) | 2026-08-09 |
| Pruebas | `pytest` en `tests/` con LLM mockeado; Swagger/curl para prueba real | 2026-08-05 |
| Secrets | `.env` local (gitignored); plantilla en `.env.example` | 2026-08-05 |
| Norte comercial | Sprint de Orquestación de Leads; producto externo primero | 2026-08-12 |
| Deuda FE/BE | Migración `developer`/`business` → FE/BE no es prioridad frente al sprint vendible | 2026-08-12 |
| Dominio | Knowledge y prompts orientados a agencias / leads, no software genérico | 2026-08-12 |
| Registro de agentes | `agents/registry.json`: `enabled` + `requires_niche`; research se apaga sin manifiesto de nicho | 2026-08-13 |
| Nicho activo | `ACTIVE_NICHE` + `docs/nichos/<id>/manifest.json` | 2026-08-13 |

## Código vs documentación

Modelo objetivo del módulo: `orchestrator` + `frontend` + `backend`.

El código puede seguir en `developer` / `business`. Realinearlo es trabajo de plataforma interna, no del MVP comercial. Norte: [docs/README.md](../../README.md) · Flujo: [arquitectura-flujo.md](../arquitectura-flujo.md).

## Cómo arrancar

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
# Copiar variables de .env.example a .env y poner LLM_API_KEY de Groq
uvicorn api.main:app --reload
pytest
```

- API docs: http://127.0.0.1:8000/docs
- Contrato objetivo: [api.md](api.md)
