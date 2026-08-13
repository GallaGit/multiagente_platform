# Hipótesis de oportunidades

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Naturaleza:** sección final del entregable de análisis transversal.  
**Contiene:** áreas con **potencial** (hipótesis), evidencia que las sustenta, y separación **hecho vs supuesto**.  
**No contiene:** propuesta de producto/servicio, features, ni arquitectura a construir.

> Las cifras de `analisis_del_mercado/context.md` (ROI, % leads perdidos) **no** se tratan como hechos.

---

## 1. Cómo leer este documento

| Etiqueta | Significado |
|----------|-------------|
| **Hecho** | Dato o patrón anclado en fuente del módulo (INE, CBRE, PwC, precios, norma, ficha) |
| **Supuesto** | Inferencia plausible no censada; requiere validación de campo |
| **Hipótesis de oportunidad** | Área donde un problema recurrente + vacío sugiere potencial de valor — **sin** especificar la forma de la oferta |

Confianza de las hipótesis: **baja–media** hasta encuesta o pilotos medibles.

---

## 2. Hipótesis (solo áreas)

### H1 — Trazabilidad lead ↔ conversación ↔ resultado

| | |
|--|--|
| **Área** | Registro continuo del ciclo comercial cuando la conversación vive fuera del CRM |
| **Hechos** | WhatsApp es canal dominante de conversación; CRM concentra inventario/contactos si se usa; integración WA↔CRM débil en micro ([whatsapp](../03_canales_y_productividad/whatsapp-business.md), [crm](../02_sistemas_core/crm-inmobiliarios.md)). Triple dependencia portales–CRM–WA (README). |
| **Supuestos** | La pérdida de contexto entre sistemas reduce conversión y aprendizaje organizativo; el dolor es mayor en micro/mediana que en stacks API de grandes. |
| **Por qué hay potencial** | Fricción F1 de alto impacto y frecuencia ([puntos-de-friccion.md](puntos-de-friccion.md)); vacío de timeline auditado ([vacios-tecnologicos.md](vacios-tecnologicos.md)). |

---

### H2 — Reducción de reescritura manual multi-sistema

| | |
|--|--|
| **Área** | Menos copia entre portal, CRM, facturación y documental |
| **Hechos** | Matriz de integraciones: tramos manuales frecuentes (portal→CRM, CRM→factura, docs). CRM vertical con connectors uneven. |
| **Supuestos** | Horas de agente en tareas de bajo valor son materialmente relevantes en TCO oculto (tiempo **no cuantificado** públicamente). |
| **Por qué hay potencial** | F3 (manual) + vacíos de integración CRM–finanzas; alineado con TCO cualitativo «tiempo > cuota CRM» ([costes-tco.md](costes-tco.md)). |

---

### H3 — Consistencia de inventario y leads multi-portal

| | |
|--|--|
| **Área** | Un solo estado de verdad de precio/disponibilidad/origen ante varios portales |
| **Hechos** | Portales críticos e ineludibles en intermediación típica; tarifas **no públicas**; sync calidad variable; CNMC: plataformas de anuncios. |
| **Supuestos** | Desync y duplicados generan coste comercial (cliente mal informado, doble contacto) de forma recurrente. |
| **Por qué hay potencial** | Dependencia crítica de portales + sustituibilidad baja del canal ([dependencias-sustituibilidad.md](dependencias-sustituibilidad.md)); vacío de consistencia multi-portal. |

---

### H4 — Cierre documental y compliance operativo (pre-notarial)

| | |
|--|--|
| **Área** | Encargo / arras / alquiler / KYC con menos dispersión de PDFs e identidad débil |
| **Hechos** | Firma eIDAS usable; precios Signaturit **35/57 €** documentados; escritura ordinaria no generalizada por videoconferencia (Ley 11/2023); AML Ley 10/2010 aplica a intermediarios; KYC E2E raro en CRM vertical típico. |
| **Supuestos** | El cuello de botella es orquestación y evidencia, no la mera existencia de un prestador de firma. |
| **Por qué hay potencial** | Vacío compliance E2E + fricción F5; ancla legal clara (hecho) vs adopción uneven (supuesto de gap). |

---

### H5 — Liquidación y dinero alineados a la operación

| | |
|--|--|
| **Área** | De operación cerrada en CRM a factura/cobro/split sin Excel paralelo |
| **Hechos** | Facturación suele vivir fuera del CRM; contabilidad vía asesoría/A3 frecuente; INE ERP **60,6%** en ≥10 emp. (no equivale a puente CRM–finance en micro). |
| **Supuestos** | Errores de split y re-tecleo son frecuentes en redes multiagente; el dolor escala con franquicia/oficina. |
| **Por qué hay potencial** | Vacío liquidación multiagente + integración CRM–factura débil; dependencia de cobro crítica. |

---

### H6 — Polarización de analítica e IA: capa «media» del tejido

| | |
|--|--|
| **Área** | Capacidad de decisión y asistencia por encima del Excel y por debajo del stack CBRE |
| **Hechos** | INE: BI **16,1%**, IA **9,35%** (CNAE 68, ≥10, T1 2023). CBRE: madurez **5,2/10**, IA gen. **71%** (grandes; no comparable). PwC ~**700 PropTech**. Uso IA informal (copiar-pegar) documentado como patrón. |
| **Supuestos** | Existe un segmento mediana (y micros ambiciosas) con CRM+portales pero sin BI/IA de proceso; la oferta PropTech no se traduce automáticamente en adopción. |
| **Por qué hay potencial** | Hueco entre anclas INE y CBRE; vacío de BI unificado y de IA ligada al registro — **área**, no producto. |

---

### H7 — Portabilidad y riesgo de lock-in (CRM / red / portal-tools)

| | |
|--|--|
| **Área** | Reducir coste de cambio y pérdida de histórico al salir de un stack |
| **Hechos** | CRM sustituible con coste; export limitado señalado en ficha CRM; franquicia impone stack; Idealista Tools acopla canal+CRM; precio Tools **no público**. Inmovilla **79 €/mes** muestra SaaS asequible ≠ bajo switching cost. |
| **Supuestos** | Agencias subestiman el coste de salida hasta el momento del cambio o fin de franquicia. |
| **Por qué hay potencial** | Dependencia «sustituible con coste» mal precificada; vacío de backup/export usable. |

---

### H8 — Identidad, dispositivo y continuidad del agente

| | |
|--|--|
| **Área** | Accesos, números y datos de cliente no atados al móvil personal del comercial |
| **Hechos** | Patrón WA personal/Business App; riesgo al offboarding; marco RGPD/AEPD; sin % MFA sectorial. |
| **Supuestos** | Incidentes de pérdida de cartera/datos al rotar agentes son materialmente relevantes aunque no haya estadística inmobiliaria pública citada. |
| **Por qué hay potencial** | Vacío identidad/continuidad + dependencia socialmente crítica de WhatsApp. |

---

## 3. Tabla de priorización relativa (cualitativa)

| Hipótesis | Impacto potencial percibido | Madurez de evidencia | Arquetipos más expuestos |
|-----------|----------------------------|----------------------|--------------------------|
| H1 Trazabilidad conversación | Alto | Media | Micro, mediana |
| H2 Menos reescritura | Alto | Media | Micro, mediana |
| H3 Multi-portal consistencia | Alto | Media | Todos excepto PropTech puro |
| H4 Documental / KYC | Medio-alto | Media-alta (norma) | Mediana, grande, redes |
| H5 Liquidación / cobro | Medio-alto | Media-baja | Mediana, franquicia, grande |
| H6 Analítica / IA de proceso | Medio | Alta en polarización; baja en demanda | Mediana; grande ya parcial |
| H7 Portabilidad / lock-in | Medio | Media | Franquicia, Tools-céntricos |
| H8 Identidad agente | Medio | Media-baja cuant. | Micro, mediana |

Orden **no** implica hoja de ruta comercial.

---

## 4. Qué queda fuera (explícito)

- Cualquier definición de MVP, pricing de oferta o nombre de solución  
- Uso de ROI 5,36:1 o «recuperar 60% de leads» de `context.md` como prueba  
- Ranking de proveedores «ganadores»  
- Afirmar tamaño de mercado € de cada hipótesis  

---

## 5. Validación pendiente (para falsar o reforzar hipótesis)

1. Encuesta anonimizada: % leads solo en WhatsApp; tiempo semanal de copia manual  
2. Tarifas/gasto portal vs CRM en muestra real  
3. Tasa de firma electrónica en encargos/arras  
4. Frecuencia de Excel de splits en redes  
5. Disposición a pagar por portabilidad/export (declarativa ≠ compra)  

---

## 6. Cierre del módulo

Este archivo cierra el **análisis transversal** del ecosistema tecnológico (corte ago. 2026). Las hipótesis H1–H8 delimitan **dónde** podría haber valor; no **qué** construir.

Volver al índice del ecosistema para navegar metodología y fichas de categoría.

---

← [Vacíos tecnológicos](vacios-tecnologicos.md) | [Índice del ecosistema →](../README.md)
