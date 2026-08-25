# 04 — Integraciones

Stack del **laboratorio dev**: **HubSpot** + **canal simulado** (API).  
Prueba activa: [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md).

Referencia mercado España (entrega cliente): [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md).

## Arquitectura del lab (este repo)

```text
Canal simulado (POST /leads/ingest | POST /webhooks/lead)
        ↓
FastAPI — api/leads/orchestrator.py
        ↓
HubSpot CRM API (Contacts + propiedades custom)
        ↓
Dashboard React (/) — KPIs, tabla, cola excepciones
```

## CRM — HubSpot (lab activo)

| Tema | Estado |
|---|---|
| Rol | Sistema de registro del lead (Contacts) |
| Auth | Private App token (`HUBSPOT_ACCESS_TOKEN`) |
| Alta contacto | `POST /crm/v3/objects/contacts` |
| Update / dedupe | Search by email/phone + `PATCH` |
| Owner | `hubspot_owner_id` + round-robin en orchestrator |
| SLA / estado | Propiedades custom (`lead_estado`, `sla_primera_respuesta_at`, etc.) |
| Tareas | Opcional (`crm.objects.tasks.write`); si no hay scope, contacto se crea igual |
| Setup props | `python -m api.hubspot_setup` |

### Checklist de prueba técnica (HubSpot lab)

- [x] Auth Private App — token en `.env`
- [x] Crear contacto — vía `/leads/ingest`
- [x] Asignar responsable — round-robin owners HubSpot
- [x] Siguiente acción + SLA — props custom
- [x] Leer/listar leads — `GET /leads`, `/leads/exceptions`
- [x] Webhook equivalente — `POST /webhooks/lead`
- [x] Campos mínimos — email o teléfono; excepción si faltan ambos
- [x] Propiedades custom — `hubspot_setup` ejecutado
- [x] 3 casos operativos documentados — [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md) PASS 2026-08-26

Detalle y go/no-go: [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md).

## Canal — simulado (lab)

| Endpoint | Uso |
|---|---|
| `POST /leads/ingest` | Ingesta manual / demo portal |
| `POST /webhooks/lead` | Alias webhook para integraciones futuras |

Payload: ver [`api/leads/models.py`](../../../api/leads/models.py) (`LeadIngestRequest`).

WhatsApp personal / WA Business API: **fuera** del primer brief.

### Checklist canal simulado

- [x] Payload JSON con nombre, email, teléfono, origen, inmueble_ref
- [x] Campos nombre, contacto, ref
- [x] Duplicados — mismo email → update, mismo owner
- [x] Datos insuficientes — solo nombre → `DATOS_INSUFICIENTES`
- [ ] Latencia medida en corrida real — pendiente registro en 08

## Entrega cliente (referencia, no lab)

En agencias españolas el canal suele ser email de portal → Smart Inbox (Witei) o conector Inmovilla. Ver [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md). **Diferida** hasta piloto con cuenta del cliente.

## Decisión de go/no-go técnico (lab)

| Resultado | Decisión |
|---|---|
| HubSpot ingest + owner + SLA + excepciones OK | **GO** — lab validado |
| Falta token o props custom | Configurar `.env` + `hubspot_setup` |
| Cliente exige Witei sin API | Reformular a Smart Inbox en su cuenta (piloto) |
