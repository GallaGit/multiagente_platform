# Ecosistema tecnológico de la inmobiliaria en España

**Corte:** agosto de 2026  
**Ámbito:** España · agencia inmobiliaria y sistemas con los que intercambia datos  
**Objetivo:** mapear herramientas, flujos, integraciones, fricciones y vacíos **sin proponer todavía un producto**.

> Complementa [`../analisis_del_mercado/`](../analisis_del_mercado/README.md) y [`../Situacion_en_España/`](../Situacion_en_España/README.md). Aquí el foco es el **stack tecnológico operativo**, no el tamaño de mercado ni las comisiones.

---

## Resumen ejecutivo

1. La agencia española típica opera un **stack fragmentado**: CRM o Excel + portales + WhatsApp + email + firma/documentos dispersos. El CRM no siempre es el sistema de registro real. **[Media]**
2. Los **portales** concentran demanda y leads; el CRM concentra inventario y contactos; WhatsApp concentra la conversación comercial. Esa triple dependencia genera duplicidades y pérdida de trazabilidad. **[Media-alta]**
3. La digitalización está **polarizada**: INE (CNAE 68, 10+ empleados, T1 2023) CRM 57,9% · ERP 60,6% · BI 16,1% · IA 9,35%. CBRE (muestra de grandes) madurez 5,2/10 e IA generativa 71%. Las cifras **no son comparables** ni representan microagencias (~98% del tejido CNAE 683). **[Alta sobre el dato; baja representatividad]**
4. España cuenta con ~**700 PropTech** y **170 ConTech** (PwC 2025), pero el 50% factura ≤500 k€: abundan herramientas, no necesariamente integración. **[Media]**
5. Las fricciones de mayor impacto están en: captación/respuesta de leads, sincronización portal↔CRM, conversaciones fuera del CRM (WhatsApp), documentación/KYC manual, y liquidación/comisiones multiagente. **[Media]**
6. Las cifras de `context.md` (30–45% leads perdidos, ROI 5,36:1) **no se usan como evidencia** en este módulo. **[Baja; no verificadas]**

---

## Conclusiones ejecutivas (atajo)

| Tema | Documento |
|------|-----------|
| Stacks por tamaño / modelo | [stacks-por-arquetipo.md](01_arquitectura_y_flujos/stacks-por-arquetipo.md) |
| Cómo se conectan los sistemas | [mapa-integraciones.md](01_arquitectura_y_flujos/mapa-integraciones.md) |
| Lead → postventa | [flujo-lead-postventa.md](01_arquitectura_y_flujos/flujo-lead-postventa.md) |
| Fricciones priorizadas | [puntos-de-friccion.md](07_analisis_transversal/puntos-de-friccion.md) |
| Vacíos sin solución diseñada | [vacios-tecnologicos.md](07_analisis_transversal/vacios-tecnologicos.md) |
| Hipótesis de oportunidades | [hipotesis-de-oportunidades.md](07_analisis_transversal/hipotesis-de-oportunidades.md) |

---

## Índice

| # | Carpeta | Contenido |
|---|---------|-----------|
| 0 | [00_metodologia/](00_metodologia/alcance-y-taxonomia.md) | Alcance, taxonomía, adopción/madurez, costes, registro de fuentes |
| 1 | [01_arquitectura_y_flujos/](01_arquitectura_y_flujos/stacks-por-arquetipo.md) | Stacks por arquetipo, mapa de integraciones, flujo lead→postventa, datos |
| 2 | [02_sistemas_core/](02_sistemas_core/crm-inmobiliarios.md) | CRM, ERP, PMS, MLS, documental, firma, contabilidad, facturación, bancos |
| 3 | [03_canales_y_productividad/](03_canales_y_productividad/portales-inmobiliarios.md) | Portales, email, Workspace, M365, WhatsApp, VoIP, calendarios, proyectos |
| 4 | [04_marketing_y_contenido/](04_marketing_y_contenido/herramientas-marketing.md) | Marketing, web/CMS, analítica, staging, foto, vídeo/tour |
| 5 | [05_operaciones_especializadas/](05_operaciones_especializadas/software-hipotecario.md) | Hipoteca, tasación/AVM, datos, KYC-AML, postventa |
| 6 | [06_datos_automatizacion_e_ia/](06_datos_automatizacion_e_ia/automatizacion.md) | Automatización, BI, IA, gobierno de datos, ciberseguridad |
| 7 | [07_analisis_transversal/](07_analisis_transversal/comparativa-proveedores.md) | Proveedores, TCO, adopción, fricciones, dependencias, vacíos, hipótesis |

```text
README
  → 00 Metodología / fuentes
  → 01 Arquitectura y flujos
  → 02–06 Categorías de software
  → 07 Análisis transversal + hipótesis de oportunidades
```

---

## Cómo leer confianza y evidencia

| Etiqueta | Significado |
|----------|-------------|
| **[Alta]** | Norma, estadística oficial, documentación/API/precios del fabricante con fecha |
| **[Media]** | Triangulación sectorial, consultoras, asociaciones |
| **[Baja]** | Observación comercial, estimación no homogénea, hipótesis |

Distinguimos siempre:

- **Capacidad anunciada** (marketing del fabricante)
- **Integración técnicamente disponible** (API/nativa documentada)
- **Uso real demostrado** en agencias españolas (evidencia limitada)

---

## Documentos relacionados

- [analisis_del_mercado/08-tendencias.md](../analisis_del_mercado/08-tendencias.md) — tendencias macro (resumen)
- [analisis_del_mercado/09-riesgos.md](../analisis_del_mercado/09-riesgos.md) — riesgos tecnológicos
- [analisis_del_mercado/context.md](../analisis_del_mercado/context.md) — hipótesis IA (no evidenciadas)
- [Situacion_en_España/Mercado_y_tendencias.md](../Situacion_en_España/Mercado_y_tendencias.md) — CRM/IA/PropTech en cifras España

---

**Siguiente →** [00_metodologia/alcance-y-taxonomia.md](00_metodologia/alcance-y-taxonomia.md)
