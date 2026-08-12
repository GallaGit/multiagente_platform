# MVP técnico — Sprint de Orquestación de Leads

Brief técnico del **producto que se vende**. No sustituye la oferta comercial ni la plataforma interna.

| Capa | Doc |
|---|---|
| Oferta / mercado | [Servicio profesional](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) |
| Este brief | `docs/mvp/` |
| SO interno (después) | [plataforma-interna](../plataforma-interna/) |

## Objetivo técnico

Que cada lead del alcance quede en el CRM con **origen**, **responsable**, **SLA**, **siguiente acción** y **resultado trazable** — medido antes/después.

## Stack de referencia (primer brief)

| Pieza | Elección |
|---|---|
| CRM | **Witei** |
| Canal | **1** entrada: lead de portal (email/webhook) **o** formulario web |
| Implantación | **n8n o Make** + reglas/campos en CRM |
| Código propio | Solo si el conector no basta |
| Variante documentada | Inmovilla (mismo flujo; otra API) — no es el alcance del primer piloto |

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

## Estado

Spec técnica **redactada**. Pruebas reales de API y piloto pagado: **pendientes**. Donde falte evidencia de fabricante, se marca *pendiente de prueba técnica* (no se inventan endpoints).

Norte del negocio: [docs/README.md](../README.md).
