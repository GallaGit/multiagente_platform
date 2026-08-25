# Nicho: inmobiliaria

Mercado **España**. Primera oferta: continuidad operativa de leads para agencias residenciales independientes.

Contrato runtime: [`manifest.json`](manifest.json).  
Negocio del nicho: [`CONTEXTO.md`](CONTEXTO.md).

## Mapa

| Ruta | Rol |
|---|---|
| [`CONTEXTO.md`](CONTEXTO.md) | Identidad, ICP, problemas y estrategia del nicho |
| [`Orquestacion-Leads-Agencias/`](Orquestacion-Leads-Agencias/) | Investigación y oferta (fuente de verdad de mercado) |
| [`mvp/`](mvp/) | Brief técnico del Sprint de Orquestación de Leads |
| [`operacion/`](operacion/) | Checklists discovery 90d y piloto pagado |
| [`roadmap/producto.md`](roadmap/producto.md) | Cadena Diagnóstico → Sprint → SaaS |
| [`runtime/icp-research.md`](runtime/icp-research.md) | Rúbrica que inyecta el Research Agent |

## Norte de producto

| Elemento | Referencia |
|---|---|
| Decisión de portafolio | [Oferta — Resumen ejecutivo](Orquestacion-Leads-Agencias/Oferta/Resumen-Ejecutivo.md) |
| MVP recomendado | [Sprint de Orquestación de Leads](Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) |
| Entrada | [Servicio inicial](Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Inicial.md) |
| Cliente prioritario | ICP-01 (agencia residencial independiente, 3–20 agentes) |
| Validación comercial | [Plan comercial 90 días](Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md) |

Cadena: `Diagnóstico → Sprint de Leads → Automatizaciones → Gestionado → SaaS`.

## Siguiente paso

1. ~~Cerrar 3 casos demo HubSpot~~ ([08-prueba-tecnica-hubspot.md](mvp/08-prueba-tecnica-hubspot.md)).
2. ~~Baseline/métricas en panel Leads~~ ([06-metricas.md](mvp/06-metricas.md)).
3. Discovery comercial — [CHECKLIST-discovery-90d.md](operacion/CHECKLIST-discovery-90d.md) · [plan 90 días](Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md).
4. Lista ICP: `POST /research` o panel Research.
5. Piloto pagado — [CHECKLIST-piloto-pagado.md](operacion/CHECKLIST-piloto-pagado.md) (CRM del cliente en producción).

Readiness: [docs/READINESS.md](../../READINESS.md).

Última sesión: [operacion/SESION-2026-08-26.md](operacion/SESION-2026-08-26.md).

Plataforma interna (multi-nicho): [docs/plataforma-interna](../../plataforma-interna/).
