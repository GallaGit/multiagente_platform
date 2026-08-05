# Decisiones — Fase 1 (MVP)

Registro para no repetir debates. Actualizar solo si cambia una decisión.

| Decisión | Valor | Fecha |
|----------|--------|-------|
| Alcance | Fase 1 completa: Orchestrator enruta + Developer/Business responde | 2026-08-05 |
| LLM | Groq (`LLM_PROVIDER=groq`) | 2026-08-05 |
| Cliente | SDK oficial `groq` (`from groq import Groq`) | 2026-08-05 |
| Modelo por defecto | `llama-3.3-70b-versatile` | 2026-08-05 |
| Agentes | `orchestrator`, `developer`, `business` | 2026-08-05 |
| Respuesta API | `{ routed_to, reply, reason }` (`reason` para depurar) | 2026-08-05 |
| Fallback de ruta | Si el JSON del Orchestrator falla → `business` | 2026-08-05 |
| Pruebas | `pytest` en `tests/` con LLM mockeado; Swagger/curl para prueba real | 2026-08-05 |
| Secrets | `.env` local (gitignored); plantilla en `.env.example` | 2026-08-05 |

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
- Contrato: [api.md](api.md)
