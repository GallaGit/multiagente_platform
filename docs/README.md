# Documentación del negocio

## Qué es

Empresa B2B de **continuidad operativa** para agencias inmobiliarias en España: que cada lead tenga responsable, SLA, siguiente acción y trazabilidad en el CRM, sin sustituir el stack instalado.

A medio plazo, el mismo repositorio sostiene el **sistema operativo interno** de la empresa: prospección, delivery, investigación, pruebas y soporte — no como producto que se vende el día 1, sino como infraestructura propia.

La fuente de verdad del mercado y la oferta es [`Orquestacion-Leads-Agencias/`](Orquestacion-Leads-Agencias/). El resto de `docs/` se alinea a esa carpeta.

## Dos capas

| Capa | Qué es | Prioridad |
|---|---|---|
| **Producto (externo)** | Lo que se vende a agencias: diagnóstico + Sprint de Orquestación de Leads | Ahora |
| **Plataforma (interna)** | SO de la empresa: comercial → ops → **delivery (Orch/FE/BE)** → QA → soporte | Después, con trabajo real |

Detalle del flujo interno: [plataforma-interna/arquitectura-flujo.md](plataforma-interna/arquitectura-flujo.md).

## Qué no es

- Un SaaS horizontal genérico como primer lanzamiento
- Un bot autónomo de ventas o “agente IA” como oferta inicial al cliente
- Un curso o proyecto de aprendizaje: es un **negocio**
- Vender “sistema multiagente genérico”; los agentes son capacidad interna (y, más adelante, posible copiloto del portafolio del nicho)

## Norte de producto

| Elemento | Referencia |
|---|---|
| Decisión de portafolio | [Oferta — Resumen ejecutivo](Orquestacion-Leads-Agencias/Oferta/Resumen-Ejecutivo.md) |
| MVP recomendado | [Sprint de Orquestación de Leads](Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) |
| Entrada | Diagnóstico de Continuidad Operativa ([Servicio inicial](Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Inicial.md)) |
| Cliente prioritario | ICP-01 (agencia residencial independiente, 3–20 agentes) — ver resumen de oferta |
| Validación comercial | [Plan comercial 90 días](Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md) |

Cadena corta: `Diagnóstico → Sprint de Leads → Automatizaciones → Gestionado → SaaS`.

Detalle: [roadmap de producto](roadmap/producto.md).

## Mapa de esta carpeta

| Ruta | Rol |
|---|---|
| [`Orquestacion-Leads-Agencias/`](Orquestacion-Leads-Agencias/) | Investigación y oferta (fuente de verdad de mercado) |
| [`mvp/`](mvp/) | Brief técnico del Sprint de Orquestación de Leads |
| [`roadmap/producto.md`](roadmap/producto.md) | Roadmap activo del producto que se vende |
| [`plataforma-interna/`](plataforma-interna/) | SO de la empresa; Orchestrator/FE/BE = módulo **delivery**, no el sistema completo |

## Siguiente paso

1. Prueba en **cuenta real** Witei (checklist en [mvp/08-prueba-tecnica-witei.md](mvp/08-prueba-tecnica-witei.md)).
2. Discovery comercial ([plan 90 días](Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md)).
3. Plataforma interna solo cuando el sprint genere trabajo repetible.
