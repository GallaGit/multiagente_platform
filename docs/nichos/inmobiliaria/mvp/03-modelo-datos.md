# 03 — Modelo de datos mínimo

Campos lógicos del MVP. En el **lab HubSpot** se mapean a propiedades custom de **Contacts** (ver [`api/leads/hubspot.py`](../../../api/leads/hubspot.py)).

## Entidad Lead (demanda)

| Campo lógico | HubSpot (lab) | Obligatorio | Notas |
|---|---|---|---|
| `lead_id` | `id` (Contact) | sí | ID HubSpot |
| `origen` | `lead_origen` | sí | portal, web, email, otro |
| `origen_ref` | `lead_origen_ref` | recomendado | ID anuncio / campaña / form |
| `nombre` | `firstname` | recomendado | |
| `email` | `email` | condicional | Al menos email **o** teléfono |
| `telefono` | `phone` | condicional | Al menos email **o** teléfono |
| `inmueble_ref` | `inmueble_ref` | si aplica | Referencia del interés |
| `responsable_id` | `hubspot_owner_id` | sí tras asignación | Owner HubSpot |
| `estado` | `lead_estado` | sí | Ver catálogo abajo |
| `siguiente_accion` | `siguiente_accion` | sí tras asignación | Texto |
| `sla_primera_respuesta_at` | `sla_primera_respuesta_at` | sí tras asignación | Deadline datetime |
| `primera_respuesta_at` | `primera_respuesta_at` | cuando ocurra | |
| `exception_code` | `exception_code` | si excepción | Ver catálogo |
| `dedupe_key` | `dedupe_key` | sí (calculada) | email o E.164 teléfono |
| `created_at` | `createdate` | sí | |
| `updated_at` | `lastmodifieddate` | sí | |

Setup de propiedades: `python -m api.hubspot_setup`.

## Estados mínimos

| Estado | Valor HubSpot | Significado |
|---|---|---|
| `nuevo` | `nuevo` | Ingestado, aún sin dueño o recién creado |
| `asignado` | `asignado` | Tiene responsable y siguiente acción |
| `en_seguimiento` | `en_seguimiento` | Hubo al menos un intento registrado |
| `excepcion` | `excepcion` | En cola humana (datos, SLA, sync) |
| `cerrado_corto` | `cerrado_corto` | Resultado de ciclo corto registrado |

## Catálogo de excepciones (cola)

| Código | Descripción |
|---|---|
| `SIN_DUENO` | Sin responsable tras umbral |
| `SLA_ROTO` | Primera respuesta fuera de plazo |
| `DATOS_INSUFICIENTES` | Sin email ni teléfono |
| `DUPLICADO_CONFLICTO` | Dedupe ambiguo |
| `SYNC_FALLIDO` | Fallo de integración |

## Qué no se modela en el MVP

- Expediente documental, KYC, firma.
- Historial completo de WhatsApp.
- Scoring de lead o capacidad financiera.

## Nota entrega cliente

En Witei/Inmovilla los nombres de campo difieren por instancia. El modelo lógico se mantiene; el mapeo se define en implantación.
