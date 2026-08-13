# Business Intelligence y reporting

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Power BI · Looker Studio · Excel · analytics de brokerage

---

## 1. Función principal

Convertir datos operativos (leads, visitas, encargos, comisiones, origen de captación) en **cuadros de mando y reporting** para dirección de oficina o red. Resuelve “¿cómo vamos?” más allá del pipeline diario del CRM.

No sustituye la decisión comercial del agente ni la analítica web (GA4). En brokerage grande, alimenta equipos de **research/analytics** de mercado (ej. CBRE); en la agencia típica, el “BI” suele ser **Excel exportado del CRM**. **[Media]**

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Titular / director de oficina | KPIs semanales/mensuales |
| Responsable comercial | Conversión por agente/origen |
| Franquiciador | Reporting homogenizado de red |
| Analista / research (grandes) | Dashboards de mercado e inversión |
| Agente | Rara vez consume BI; mira CRM o WhatsApp |

---

## 3. Momento del flujo

Transversal y **retrospectivo**: tras captar actividad en CRM/portales/ads. Interviene en control de gestión, no en el minuto del lead (salvo alertas). En grandes: también ciclo de publicación de market reports.

---

## 4. Información gestionada

- Leads, visitas, ofertas, cierres, ticket medio, tiempo en pipeline  
- Origen (portal, web, referido, captación propia)  
- Inventario activo vs caducado; exclusivas  
- Comisiones y liquidaciones (si el CRM las tiene bien)  
- En grandes: series de mercado, ocupación, investment volumes  

Calidad del dashboard = calidad del CRM. Duplicados y etapas mal usadas invalidan el BI. Ver [gobierno-calidad-datos.md](gobierno-calidad-datos.md).

---

## 5. Integraciones (tipo)

| Origen → BI | Tipo habitual |
|-------------|---------------|
| CRM → Excel | Manual (export) — dominante en micro/mediana |
| CRM → Power BI | API / conector / export automatizado |
| Sheets / Drive → Looker Studio | Nativa Google |
| GA4 → Looker Studio / Power BI | Nativa / API |
| Portales → BI de agencia | Inexistente o manual (datos del portal no se ceden) |
| Contabilidad → BI | Manual / ERP (grandes) |
| Data warehouse | Solo grandes / PropTech |

---

## 6. Flujo de datos (ASCII)

```text
[CRM] --export/API--> [Excel / Sheets] ----+
[GA4 / Ads] -------------------------------+--> [Looker Studio | Power BI]
[ERP / contabilidad] --(grandes)-----------+            |
                                                         v
                                              [Director / franquicia]
                                                         |
                              (brokerage nacional)       v
                                              [Equipo analytics / research]
```

---

## 7. Limitaciones y tareas humanas

- Sin disciplina de etapas en CRM, el embudo BI miente.  
- Comisiones multiagente y colaboraciones: a menudo fuera del modelo de datos.  
- Portales no entregan dataset usable a la agencia para BI propio.  
- Licencias Power BI vs necesidad real: muchas oficinas se quedan en Excel.  
- Franquicia: el dato puede estar en el centro; la oficina local ve PDF, no modelo.

---

## 8. Costes (solo públicos)

| Concepto | Dato | Fuente |
|----------|------|--------|
| **Looker Studio** | Gratuito (Google); límites de conectores/partners pueden tener coste | [Looker Studio](https://lookerstudio.google.com/) · **[Alta sobre gratuidad base]** |
| **Excel / Microsoft 365** | Incluido en planes M365; ver licencia Workspace/M365 de la oficina | Consultar fabricante · pack M365 |
| **Power BI Pro** | **14 $/usuario/mes** (pago anual, precio marketing USD) | [Power BI pricing](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) · **[Alta]** |
| **Power BI Premium Per User** | **24 $/usuario/mes** (pago anual, USD marketing) | Misma URL · **[Alta]** |
| Power BI Embedded / Fabric capacity | Variable / contactar ventas | no público homogéneo |
| Implantación dashboards | Bajo presupuesto (consultoría) | no público |
| Herramientas research CBRE-like | Internas / no vendidas a agencias locales | no público |

Precios Microsoft: país, divisa e impuestos en checkout; no inventar € fijos.

---

## 9. Competencia / enfoques comparados

| Enfoque | Encaje | Fricción |
|---------|--------|----------|
| Excel / Sheets | Micro y mediana | Sin versión única; errores |
| Looker Studio | Bajo coste, stack Google | Gobernanza débil |
| Power BI | Medianas M365 / grandes | Licencia + modelo de datos |
| Informes nativos del CRM | Rápido | Poco flexible; “caja negra” |
| Equipos analytics brokerage (CBRE, etc.) | Grandes operadores | No transferible a microagencia |
| Tableau / Qlik | Enterprise | Sobrepeso para intermediación típica |

---

## 10. Adopción + confianza

| Señal | Lectura | Confianza |
|-------|---------|-----------|
| **INE TIC** CNAE 68, empresas **≥10** empleados, T1 2023: **BI 16,1%** | **Poco utilizada** en el segmento medido | **[Alta]** dato; **baja** representatividad del tejido (~98% micro CNAE 683 fuera) |
| Analítica interna INE (mismo corte) **36,6%** | Habitual-baja (≥10) | Alta dato |
| Excel como reporting | Muy extendida (cualitativo) | Media |
| Power BI / Looker en micro | Emergente / irregular | Baja |
| CBRE y peers: equipos analytics / research | Habitual en grandes | Media (prensa/sectorial) |

Fuentes INE: [tabla CRM/TIC](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) (contexto adopción digital; BI en serie TIC sectorial citada en metodología del módulo). Ver también [`Mercado_y_tendencias.md`](../../Situacion_en_España/Mercado_y_tendencias.md).

CBRE Madurez Digital 5,2/10 (muestra principales compañías) **no** equivale a adopción BI INE. No promediar. **[Alta metodológica]**

---

## 11. Madurez + justificación

Uso típico intermediación: **Tradicional/Digitalizada** (Excel + informe CRM).  
Mediana con Looker/Power BI conectado: **Digitalizada**, rara vez **Automatizada** (refresco programado + gobierno).  
Brokerage nacional con analytics: **Automatizada** / data-driven en research; no es el arquetipo dominante.  
Madurez asignada: **Digitalizada (Excel-first)** · BI formal **poco utilizada** (ancla INE 16,1% ≥10). **[Alta ancla; media extrapolación]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| BI 16,1% INE CNAE 68 ≥10 T1 2023 | Registrado · **[Alta]** |
| % Power BI vs Looker vs Excel en agencias | Pendiente |
| Precios Power BI Pro/PPU | Página Microsoft · **[Alta]** |
| Inventario de dashboards típicos (KPIs mínimos) | Cualitativo; estandarizar en stacks |

---

← [Automatización](automatizacion.md) | [Índice](../README.md) | [Siguiente: IA generativa →](ia-generativa.md)
