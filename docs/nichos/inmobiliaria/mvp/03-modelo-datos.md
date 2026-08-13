# 03 — Modelo de datos mínimo

Campos lógicos del MVP. Los nombres reales en Witei se mapean en la implantación (*pendiente de prueba técnica* por instancia/plan).

## Entidad Lead (demanda)

| Campo lógico | Obligatorio | Notas |
|---|---|---|
| `lead_id` | sí | ID en CRM o externo estable |
| `origen` | sí | portal, web, email, otro |
| `origen_ref` | recomendado | ID anuncio / campaña / form |
| `nombre` | recomendado | |
| `email` | condicional | Al menos email **o** teléfono |
| `telefono` | condicional | Al menos email **o** teléfono |
| `inmueble_ref` | si aplica | Referencia del interés |
| `responsable_id` | sí tras asignación | Usuario CRM |
| `estado` | sí | Ver catálogo abajo |
| `siguiente_accion` | sí tras asignación | Texto o tipo + fecha |
| `sla_primera_respuesta_at` | sí tras asignación | Deadline |
| `primera_respuesta_at` | cuando ocurra | |
| `resultado` | cuando cierre ciclo corto | contactado, visita, descartado, sin_respuesta, otro |
| `created_at` | sí | |
| `updated_at` | sí | |
| `dedupe_key` | sí (calculada) | p. ej. normalizar email o E.164 teléfono |

## Estados mínimos

| Estado | Significado |
|---|---|
| `nuevo` | Ingestado, aún sin dueño o recién creado |
| `asignado` | Tiene responsable y siguiente acción |
| `en_seguimiento` | Hubo al menos un intento registrado |
| `excepcion` | En cola humana (datos, SLA, sync) |
| `cerrado_corto` | Resultado de ciclo corto registrado |

No se modela aquí el pipeline completo hasta escritura.

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
