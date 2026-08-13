# MVP técnico — Sprint de Orquestación de Leads

Brief técnico del **producto que se vende**. No sustituye la oferta comercial ni la plataforma interna.

| Capa | Doc |
|---|---|
| Oferta / mercado | [Servicio profesional](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) |
| Este brief | `docs/nichos/inmobiliaria/mvp/` |
| SO interno (después) | [plataforma-interna](../../plataforma-interna/) |

## Objetivo técnico

Que cada lead del alcance quede en el CRM con **origen**, **responsable**, **SLA**, **siguiente acción** y **resultado trazable** — medido antes/después.

## Stack de referencia (primer brief)

| Pieza | Elección |
|---|---|
| CRM | **Witei** |
| Canal | **1** entrada: lead de portal (email/webhook) **o** formulario web |
| Implantación | **Smart Inbox** (email) + reglas nativas Witei; **n8n/Make/Zapier** solo para generar/reenviar el email |
| Código propio | Solo normalizador/receptor si hace falta |
| Variante documentada | Inmovilla (otra prueba técnica) — no es el alcance del primer piloto |
| Prueba técnica | [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md) — **GO condicionado** (Smart Inbox; no REST inmediato) |

## Qué no es este MVP

- Sustituir el CRM
- Bot de ventas / IA autónoma
- WhatsApp personal, voz, todos los portales
- Expediente, KYC, firma, pagos
- SaaS multi-tenant

## Mapa

| Doc | Contenido |
|---|---|
| [01-alcance.md](01-alcance.md) | Incluye / no incluye |
| [02-flujo.md](02-flujo.md) | Happy path y excepciones |
| [03-modelo-datos.md](03-modelo-datos.md) | Campos mínimos |
| [04-integraciones.md](04-integraciones.md) | Witei + canal; checklist API |
| [05-reglas.md](05-reglas.md) | Dedupe, reparto, SLA, cola |
| [06-metricas.md](06-metricas.md) | Baseline y antes/después |
| [07-criterios-hecho.md](07-criterios-hecho.md) | Cuándo el piloto “funcionó” |
| [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md) | Resultado go/no-go Witei + canal |

## Estado

Spec técnica **redactada**. Prueba de escritorio Witei **cerrada** (GO condicionado vía Smart Inbox). Prueba en cuenta real y piloto pagado: **pendientes**.

Norte del nicho: [README](../README.md). Norte de la empresa: [docs/README.md](../../README.md).
