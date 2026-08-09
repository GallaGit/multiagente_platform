# Decisiones — Fase 1 (MVP)

Registro para no repetir debates. Actualizar solo si cambia una decisión.

| Decisión | Valor | Fecha |
|----------|--------|-------|
| Alcance | Orchestrator documenta (brief) + delega a Frontend o Backend | 2026-08-09 |
| LLM | Groq (`LLM_PROVIDER=groq`) | 2026-08-05 |
| Cliente | SDK oficial `groq` (`from groq import Groq`) | 2026-08-05 |
| Modelo por defecto | `llama-3.3-70b-versatile` | 2026-08-05 |
| Agentes | `orchestrator`, `frontend`, `backend` | 2026-08-09 |
| Respuesta API | `{ routed_to, documentation, reply, reason }` | 2026-08-09 |
| Fallback de ruta | Si el JSON del Orchestrator falla → `backend` | 2026-08-09 |
| Full-stack | Elegir foco principal; no llamar FE+BE en el mismo request (aún) | 2026-08-09 |
| Pruebas | `pytest` en `tests/` con LLM mockeado; Swagger/curl para prueba real | 2026-08-05 |
| Secrets | `.env` local (gitignored); plantilla en `.env.example` | 2026-08-05 |

## Deuda: código vs documentación

La documentación ya describe `orchestrator` + `frontend` + `backend`.

El código actual del MVP **aún** usa `developer` / `business` (prompts y rutas antiguas). Pendiente realinear `agents/`, `api/orchestrate.py`, `api/main.py` y `tests/` con este modelo.

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
