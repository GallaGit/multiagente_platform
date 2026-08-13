# Registro de agentes

Contrato de **activación**. Los agentes son roles (oficio), no verticales. El nicho vive en `docs/nichos/<id>/`.

Fuente de verdad: [`agents/registry.json`](../../../agents/registry.json). Código: [`api/registry.py`](../../../api/registry.py), [`api/niche.py`](../../../api/niche.py).

## Regla

Un agente está **activo** solo si:

1. `enabled` es `true` en el registro, **y**
2. `requires_niche` es `false`, **o** el nicho activo tiene `manifest.json` y al menos un archivo de `context_files`.

Hoy `ACTIVE_NICHE=inmobiliaria` y existe [`docs/nichos/inmobiliaria/`](../../nichos/inmobiliaria/), así que `research` está encendido.

| Agente | `enabled` | `requires_niche` | Hoy |
|---|---|---|---|
| orchestrator | sí | no | activo (no se enruta) |
| developer | sí | no | activo |
| business | sí | no | activo |
| research | sí | sí | activo porque hay manifiesto válido |

El orquestador **solo lista** agentes routables (activos excepto él). Si el LLM pide uno apagado → fallback a `business`. `POST /research` y `python -m api.research` responden 503 / exit 1; no ejecutan el pipeline.

## Qué no es

- No es un selector de UI.
- No documenta otros sectores aquí.
- Apagar no borra el agente: sigue en disco y en el registro.

Para desactivar a mano: `"enabled": false` en `registry.json`. Para apagar research: quitar o invalidar el `manifest.json` del nicho activo.
