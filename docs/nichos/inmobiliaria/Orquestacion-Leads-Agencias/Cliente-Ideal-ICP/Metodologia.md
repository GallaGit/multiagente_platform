# Metodología

## 1. Alcance

El ICP se construye exclusivamente con archivos disponibles de los módulos previos:

| Entrada solicitada | Evidencia disponible usada |
|---|---|
| Módulo 01 — Mercado | `analisis_del_mercado/` y `Situacion_en_España/` |
| Módulo 02 — Procesos | `analisis_del_mercado/02-funcionamiento.md` y flujo lead→postventa |
| Módulo 03 — Software | `ecosistema_tecnologico/` |
| Módulo 04 — Problemas | `Dolor-del-Cliente/` |
| Módulo 05 — Competencia | Metodología, fuentes y cinco análisis disponibles; fichas de empresa ausentes |
| Módulo 06 — Oportunidades | No existe como carpeta; proxy: hipótesis/vacíos tecnológicos |
| Módulo 07 — Validación | Metodología, rúbricas, matriz, proceso, reglas e inventario O01–O08 |

No se ha añadido investigación externa nueva. Los enlaces externos se heredan de los módulos.

## 2. Exclusiones

- Porcentajes de pérdida de leads y ROI de `context.md`, expresamente no validados.
- Cifras de prevalencia derivadas de reseñas o entrevistas aisladas.
- Presupuestos, facturación, empleados u operaciones segmentarios no publicados.
- Funciones de proveedores como prueba automática de adopción o resultado.
- Benchmarks de grandes empresas o EEUU aplicados a microagencias españolas.

## 3. Unidad de análisis

Se distinguen tres unidades:

1. **Segmento:** modelo operativo/económico, por ejemplo alquiler o obra nueva.
2. **Arquetipo organizativo:** independiente, franquicia, micro, mediana o gran operador.
3. **ICP:** combinación concreta de segmento, tamaño, madurez, dolor y compra.

Franquicia e independencia son mecanismos organizativos, no segmentos económicos puros; se mantienen como capítulos porque el encargo los exige y alteran autonomía, stack y compra.

## 4. Escala de confianza

| Nivel | Regla |
|---|---|
| Alto | Fuente oficial/norma o afirmación triangulada de alta calidad |
| Medio | Síntesis coherente de varias fuentes, sin medición segmentaria |
| Bajo | Inferencia comercial explícita o dato pendiente de campo |

Cada documento contiene:

- evidencia utilizada;
- limitaciones;
- información pendiente;
- confianza global.

## 5. Digitalización

| Nivel | Evidencia observable |
|---|---|
| Muy bajo | Papel, teléfono y hojas sin sistema de registro |
| Bajo | Canales digitales, pero inventario y seguimiento manuales |
| Medio | CRM/PMS y firma/facturación parciales; silos frecuentes |
| Alto | Sistemas core integrados, automatizaciones y reporting estable |
| Muy alto | Arquitectura API-first, gobierno de datos, BI e IA operativa |

La clasificación por segmento es una síntesis, no un censo. INE solo mide de forma comparable empresas CNAE 68 con 10+ empleados.

## 6. Tamaño y capacidad económica

Se usan las clases oficiales:

- Micro: menos de 10 empleados y hasta 2 M€.
- Pequeña: menos de 50 y hasta 10 M€.
- Mediana: menos de 250 y hasta 50 M€.
- Grande: 250+ y más de 50 M€.

Los rangos operativos del Módulo 01 se citan como heurísticos y nunca sustituyen datos de un prospecto. Cuando no hay facturación, oficinas, operaciones o presupuesto por segmento se marca **NP — no público**.

La capacidad de pago es cualitativa:

- Baja: presupuesto no identificado y fuerte sensibilidad.
- Media: software ya adquirido y decisión local plausible.
- Alta: función tecnológica/operativa y procurement establecidos.

## 7. Relación problema–oportunidad

Los problemas usan los IDs P01–P30 del Módulo 04. Las oportunidades usan H1–H8:

- H1 trazabilidad conversación;
- H2 reducción de reescritura;
- H3 consistencia multiportal;
- H4 cierre documental/compliance;
- H5 liquidación y cobro;
- H6 analítica/IA de proceso;
- H7 portabilidad;
- H8 identidad y continuidad.

Las oportunidades son hipótesis de potencial, no productos validados.

## 8. Scoring

Cada ICP se puntúa de 1 a 5 en ocho criterios ponderados. El resultado va de 0 a 100:

`Score = Σ (puntuación / 5 × peso)`

Se muestran dos lecturas:

- **Score base:** atractivo relativo si las afirmaciones fueran ciertas.
- **Score ajustado:** score base multiplicado por la confianza ponderada.

Factores heredados del Módulo 07: alta 1,00; media 0,85; baja 0,65; supuesto 0,40. Las puntuaciones no son probabilidades ni autorizan construir. La falta de entrevistas y evidencia de pago mantiene todos los perfiles en validación.

## 9. DMU

Se separa:

- rol que sufre;
- usuario;
- buscador/evaluador;
- aprobador;
- firmante;
- influenciadores.

Los roles de uso están anclados en el Módulo 03. El proceso de compra no fue investigado en los módulos y se etiqueta como hipótesis a validar.

## 10. Reproducibilidad

Todos los enlaces internos apuntan a la fuente heredada. `Bibliografia.md` explica el uso de cada documento y `Enlaces.md` conserva fuentes externas principales. La ausencia de un dato se conserva como resultado, no se rellena mediante estimación.
