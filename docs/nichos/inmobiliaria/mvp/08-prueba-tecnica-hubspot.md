# 08 — Prueba técnica HubSpot (lab activo)

**Tipo:** validación en laboratorio dev con cuenta HubSpot (Private App).  
**Objetivo:** cerrar el checklist de [04-integraciones.md](04-integraciones.md) y los 3 casos demo del [README del repo](../../../../README.md).

## Resumen ejecutivo

| Capacidad MVP | Resultado | Implicación |
|---|---|---|
| API REST Contacts | **GO** | Private App + token |
| Propiedades custom | **GO** | `python -m api.hubspot_setup` |
| Alta + owner + SLA | **GO** | `api/leads/orchestrator.py` |
| Dedupe email | **GO** | Search + update |
| Excepción datos insuficientes | **GO** | `DATOS_INSUFICIENTES` |
| Panel operativo | **GO** | Dashboard `/` |
| Tareas nativas | **Opcional** | Scope `crm.objects.tasks.write` |

**Decisión:** **GO** — el lab HubSpot valida la orquestación del sprint sin cuenta Witei.

## Prerrequisitos

1. `HUBSPOT_ACCESS_TOKEN` en `.env` (Private App).
2. Scopes mínimos: contacts read/write, owners read, schemas contacts read/write; tasks write opcional.
3. `python -m api.hubspot_setup` — propiedades custom creadas.
4. Al menos un **owner** en el portal HubSpot (round-robin).
5. API en marcha: `python -m uvicorn api.main:app --host 127.0.0.1 --port 8000`.
6. Windows SSL: `HUBSPOT_VERIFY_SSL=false` y `LLM_VERIFY_SSL=false` si aplica.

## Casos operativos

Usar emails únicos por corrida (sustituir `@demo.com` si repites pruebas).

### Caso 1 — Lead nuevo

```bash
curl -X POST http://127.0.0.1:8000/leads/ingest \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","email":"ana.demo@example.com","telefono":"612345678","origen":"portal","inmueble_ref":"REF-001"}'
```

**Esperado:**
- Contacto creado en HubSpot.
- `hubspot_owner_id` asignado.
- `lead_estado=asignado`, `siguiente_accion` y `sla_primera_respuesta_at` poblados.
- Visible en panel `/` y `GET /leads`.

### Caso 2 — Duplicado (mismo email)

Repetir el mismo payload del Caso 1 (mismo email).

**Esperado:**
- `is_duplicate: true` en respuesta ingest.
- Mismo contacto actualizado, **mismo owner**.
- No segundo responsable.

### Caso 3 — Datos insuficientes

```bash
curl -X POST http://127.0.0.1:8000/leads/ingest \
  -H "Content-Type: application/json" \
  -d '{"nombre":"SoloNombre","origen":"portal"}'
```

**Esperado:**
- Contacto con `lead_estado=excepcion`.
- `exception_code=DATOS_INSUFICIENTES`.
- Visible en `GET /leads/exceptions` y cola del panel.

## Verificación

| Check | Dónde |
|---|---|
| KPIs / métricas | `GET /leads/metrics?mvp_only=true` o panel `/` |
| Baseline snapshot | `POST /leads/baseline` · `GET /leads/baseline` · botón panel |
| Lista leads | `GET /leads?mvp_only=true` |
| Cola excepciones | `GET /leads/exceptions?mvp_only=true` |
| UI HubSpot | Contacts → propiedades custom |

## Resultados de corrida

**Fecha:** 2026-08-26 · API local · HubSpot Private App

| Caso | Resultado | Notas |
|---|---|---|
| 1 — Lead nuevo | **PASS** | `action=created`, `estado=asignado`, owner `97473872`, SLA y siguiente acción |
| 2 — Duplicado | **PASS** | `action=duplicate`, `is_duplicate=true`, mismo owner, sin segundo responsable |
| 3 — Datos insuficientes | **PASS** | `action=exception`, `exception_code=DATOS_INSUFICIENTES`, sin owner |

Ejemplo Caso 1 (email único): `ana.new.3d74424b@example.com` → contacto `848594430142` (IDs de ejemplo; varían por corrida).

## Baseline demo (lab)

**Fecha:** 2026-08-26 · Tras casos 1–3 · `mvp_only=true`

| Paso | Comando / acción | Resultado |
|---|---|---|
| Métricas pre-baseline | `GET /leads/metrics?mvp_only=true` | 4 leads MVP, 50% responsable, 75% siguiente acción, 1 excepción |
| Captura | `POST /leads/baseline` con `{"note":"Lab dia 0 post-3-casos demo","mvp_only":true}` | **PASS** — snapshot en `data/baseline.json` |
| Dashboard con delta | `GET /leads/metrics?mvp_only=true` | `baseline` presente; `delta` en cero (misma corrida) |

**Notas:**
- `mediana_tiempo_respuesta_min` = `null` (menos de 2 leads con `primera_respuesta_at` registrado).
- El panel muestra delta vs baseline en cada KPI tras capturar.
- Procedimiento operativo: [06-metricas.md](06-metricas.md).

## Limitaciones vs producción inmobiliaria

- HubSpot **no** es el CRM vertical típico del ICP español (Witei/Inmovilla).
- El canal es **simulado** (JSON), no email de portal real.
- El lab valida **lógica de orquestación** (registro → owner → SLA → excepción → métrica), no el parseo Smart Inbox.
- En piloto pagado el conector apunta al CRM del cliente — ver [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md).

## Siguiente

1. ~~Documentar baseline en [06-metricas.md](06-metricas.md).~~
2. Discovery comercial — [CHECKLIST-discovery-90d.md](../operacion/CHECKLIST-discovery-90d.md).
3. Piloto en CRM del cliente cuando haya compromiso económico — [CHECKLIST-piloto-pagado.md](../operacion/CHECKLIST-piloto-pagado.md).
4. Readiness: [docs/READINESS.md](../../../READINESS.md).
