# MVP técnico — Sprint de Orquestación de Leads

Brief técnico del **producto que se vende**. No sustituye la oferta comercial ni la plataforma interna.

| Capa | Doc |
|---|---|
| Oferta / mercado | [Servicio profesional](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) |
| Este brief | `docs/nichos/inmobiliaria/mvp/` |
| SO interno (después) | [plataforma-interna](../../plataforma-interna/) |

## Objetivo técnico

Que cada lead del alcance quede en el CRM con **origen**, **responsable**, **SLA**, **siguiente acción** y **resultado trazable** — medido antes/después.

## Stack del laboratorio (este repo)

| Pieza | Elección |
|---|---|
| CRM | **HubSpot** (Private App, Contacts + propiedades custom) |
| Canal | **Simulado** — `POST /leads/ingest` o `POST /webhooks/lead` (equivalente a portal/formulario) |
| Motor | FastAPI [`api/leads/orchestrator.py`](../../../api/leads/orchestrator.py) |
| Panel | Dashboard React (`/`) — KPIs, tabla, cola excepciones |
| Evidencia | [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md) |

## Stack de entrega a cliente (referencia mercado España)

| Pieza | Elección típica ICP-01 |
|---|---|
| CRM | Witei, Inmovilla u otro CRM activo del cliente |
| Canal | Portal email / Smart Inbox / formulario web |
| Referencia investigación | [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md) (no es el camino activo de este repo) |

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
| [04-integraciones.md](04-integraciones.md) | HubSpot + canal simulado |
| [05-reglas.md](05-reglas.md) | Dedupe, reparto, SLA, cola |
| [06-metricas.md](06-metricas.md) | Baseline y antes/después |
| [07-criterios-hecho.md](07-criterios-hecho.md) | Cuándo el piloto “funcionó” |
| [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md) | Prueba activa del lab |
| [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md) | Referencia mercado / entrega cliente |

## Estado

Spec técnica **redactada**. **Lab HubSpot operativo** en este repo (API + dashboard + props custom).

Prueba Witei en cuenta real: **diferida** — solo con cliente/piloto en producción.

Norte del nicho: [README](../README.md). Norte de la empresa: [docs/README.md](../../README.md).
