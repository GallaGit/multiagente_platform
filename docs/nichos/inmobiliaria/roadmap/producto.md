# Roadmap de producto

Puente corto al roadmap canónico del nicho. **No duplica** el análisis de oferta.

## Cadena principal (lo que se vende)

`Diagnóstico → Sprint de Leads → Automatizaciones → Gestionado → SaaS`

Fuente completa (etapas, gates, no-avances):  
[Orquestacion-Leads-Agencias/Oferta/Analisis/Roadmap.md](../Orquestacion-Leads-Agencias/Oferta/Analisis/Roadmap.md)

Oferta MVP: [Sprint de Orquestación de Leads](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md)  
Decisión de portafolio: [Resumen ejecutivo](../Orquestacion-Leads-Agencias/Oferta/Resumen-Ejecutivo.md)

## Estado actual

| Frente | Estado |
|---|---|
| Investigación de mercado / ICP / oferta | Lista en `Orquestacion-Leads-Agencias/` |
| Spec técnica del sprint | Lista en [`mvp/`](../mvp/); **lab HubSpot operativo** |
| Validación técnica dev (lab) | En curso — 3 casos + métricas ([08-prueba-tecnica-hubspot.md](../mvp/08-prueba-tecnica-hubspot.md)) |
| Prueba Witei cuenta real | **Diferida** — solo con cliente/piloto en producción |
| Validación comercial (entrevistas, piloto) | Pendiente — [plan 90 días](../Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md) |
| Plataforma interna (`docs/plataforma-interna/`) | Fase 1 delivery cerrada; fases 2–6 posteriores |

## Dos capas de CRM

| Capa | CRM | Cuándo |
|---|---|---|
| **Lab dev (este repo)** | HubSpot Private App | Validar orquestación sin cuenta Witei |
| **Entrega cliente (España)** | Witei / Inmovilla / otro del cliente | Piloto pagado en producción |

## Relación con la plataforma interna

[plataforma-interna/](../../../plataforma-interna/) es el SO de la empresa.  
Orchestrator / Frontend / Backend viven en la capa de **delivery técnico** ([arquitectura-flujo.md](../../../plataforma-interna/arquitectura-flujo.md)), no como producto vendible ni como flujo único.

Se amplía (comercial, ops, QA, soporte) cuando el Sprint de Leads genere trabajo repetible.

Norte del nicho: [README del nicho](../README.md). Norte de la empresa: [docs/README.md](../../../README.md).
