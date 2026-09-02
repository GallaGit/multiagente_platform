# 05 — Reglas operativas

Valores por defecto del brief; se ajustan con el cliente en el diagnóstico. Toda regla tiene **owner humano**.

En el **lab HubSpot** estas reglas están implementadas en [`api/leads/orchestrator.py`](../../../api/leads/orchestrator.py).  
En **entrega cliente** (Witei/Inmovilla) equivalentes vía reglas nativas del CRM — ver [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md).

## 1. Entrada

- Solo el canal acordado en el alcance (lab: `/leads/ingest`).
- Origen obligatorio (`origen` + `origen_ref` si existe).
- Si faltan email **y** teléfono → `DATOS_INSUFICIENTES` (no asignar owner).

## 2. Deduplicación

| Prioridad de clave | Uso |
|---|---|
| 1. Email normalizado | Match fuerte → update contacto existente |
| 2. Teléfono E.164 | Match fuerte |
| 3. `origen` + `origen_ref` | Match de evento |

- Si match: actualizar registro existente; conservar `hubspot_owner_id` existente; no crear segundo responsable.
- Implementación: `HubSpotClient.find_existing_contact` (email → teléfono → `origen`+`origen_ref`) + `update_contact`.

## 3. Reparto (dueño)

| Modo (lab) | Implementación |
|---|---|
| Round-robin entre owners HubSpot | `pick_next_owner()` sobre lista de owners del portal |
| Lista fija | `ROUND_ROBIN_OWNER_IDS` en `.env` (opcional) |

- Sin owners en HubSpot → excepción (no asignar a ciegas).
- En Witei cliente: reglas nativas Smart Inbox / Coordinador — ver doc Witei.

## 4. SLA

| Evento | Default (lab) |
|---|---|
| Primera respuesta / intento registrado | `SLA_MINUTES` en `.env` (default 60) |
| Sin dueño tras alta | No aplica si round-robin asigna en ingest |

Incumplimiento → visible en métricas (`sla_rotos`), cola (`SLA_ROTO` en lectura) y tabla del panel; escalado manual en MVP.

## 5. Siguiente acción

Tras asignar (lead nuevo):

- Texto en `siguiente_accion` (p. ej. “Contactar lead en 1 h”).
- Tarea HubSpot opcional si el scope `crm.objects.tasks.write` está disponible.

Sin siguiente acción → tratar como excepción operativa.

## 6. Reasignación y escalado

1. Alerta al dueño actual (fuera de automatización MVP lab).
2. PATCH `/leads/{id}` para resolver excepciones manualmente desde panel.
3. Escalado a ops/gerente: proceso humano documentado en manual.

## 7. Cola humana

`GET /leads/exceptions` — contactos con `lead_estado=excepcion` **o** `exception_code` presente (incl. `SLA_ROTO` en lectura).  
Panel `/` muestra cola. Nadie cierra excepción sin dejar resultado o nueva siguiente acción.

## 8. Lo que no hacen las reglas

- Enviar mensajes al lead sin aprobación humana (MVP).
- Cambiar precios, rechazar por scoring automático.
- Sobreescribir notas humanas sin traza.
