# Reporting poco fiable y dependiente de Excel

**Corte:** 12 de agosto de 2026  
**Ámbito:** agencias inmobiliarias en España; reseñas internacionales como evidencia de productos equivalentes

**Evaluación:**

- **Frecuencia:** Frecuente de forma cualitativa; sin medición nacional en microagencias
- **Impacto:** Alto
- **Impacto económico:** Alto por decisiones, atribución y control tardíos; sin cuantía demostrada
- **Impacto operativo:** Alto en equipos y redes
- **Frustración:** alta para dirección y administración
- **Urgencia:** Alta
- **Personas afectadas:** dirección, responsables comerciales, marketing, administración y franquiciadores

## 1. Nombre del problema

Reporting comercial y financiero poco fiable, con exportaciones y reconstrucción manual en Excel.

## 2. Descripción

Los informes dependen de que agentes y sistemas registren de forma consistente origen, responsable, actividad, estado, ingresos y costes. Cuando conversaciones o documentos permanecen fuera del CRM, los dashboards ofrecen una visión incompleta.

La agencia termina exportando datos, corrigiendo campos y cruzando CRM, portales y contabilidad en hojas de cálculo. Excel no es el origen del problema, pero se convierte en la capa donde se compensan carencias de modelo, integración y calidad del dato.

## 3. Evidencias

### Instituto Nacional de Estadística

- **Organización/autor:** INE
- **Título:** *Uso, intercambio, analítica y comercio de datos*, tabla 59889
- **Fecha:** primer trimestre de 2023
- **Tipo/calidad:** encuesta TIC oficial; **alta**
- **URL:** <https://www.ine.es/jaxi/Tabla.htm?tpx=59889>
- **Respaldo exacto:** para actividades inmobiliarias y empresas con diez o más empleados, la tabla registra CRM en el 57,9%, BI en el 16,1% y analítica interna en el 36,6%. La diferencia acredita menor extensión de BI que de CRM en ese universo; no describe a microagencias.

### GetApp

- **Organización/autor:** GetApp, familia Gartner Digital Markets
- **Título:** *Follow Up Boss review summaries*
- **Fecha:** consulta del 12 de agosto de 2026
- **Tipo/calidad:** análisis de 58 reseñas verificadas; **media**
- **URL:** <https://www.getapp.com/all-software/a/follow-up-boss/>
- **Respaldo exacto:** algunos usuarios indican que crean sistemas externos de reporting para analizar con mayor profundidad la progresión del lead. También mencionan problemas ocasionales al filtrar o almacenar correctamente la fuente.

### RICS

- **Organización/autor:** Royal Institution of Chartered Surveyors
- **Título:** *RICS Tech Partner Programme Survey 2024*
- **Fecha:** 2024
- **Tipo/calidad:** informe profesional internacional; **media**
- **URL:** <https://www.rics.org/content/dam/ricsglobal/documents/latest-news/Tech-Partner-Programme-Survey-2024.pdf>
- **Respaldo exacto:** vincula la calidad, estructura y estandarización insuficientes de los datos con dificultades para colaboración, analítica y toma de decisiones.

### Idealista/tools

- **Organización/autor:** Idealista
- **Título:** *Informe de inmuebles*
- **Fecha:** actualizado el 24 de marzo de 2020
- **Tipo/calidad:** documentación oficial de producto; **alta para la función descrita**
- **URL:** <https://www.idealista.com/tools/centrodeayuda/articulos/informe-de-inmuebles/>
- **Respaldo exacto:** documenta la descarga en Excel de un informe general con características de inmuebles activos e inactivos. Demuestra que la exportación forma parte del flujo soportado; no demuestra por sí sola que el reporting sea defectuoso.

Las plataformas Capterra, GetApp y Software Advice pertenecen a Gartner Digital Markets y se contabilizan como una sola familia cuando se usan juntas. Aquí solo se utiliza GetApp.

## 4. Personas afectadas

- Dirección y responsables de oficina.
- Coordinadores comerciales.
- Marketing y adquisición.
- Administración y finanzas.
- Franquiciadores y responsables de red.
- Agentes evaluados con datos incompletos.

## 5. Proceso afectado

El reporting intenta resumir la [comercialización y gestión de demanda](../../analisis_del_mercado/02-funcionamiento.md#comercialización), además de ofertas, cierres y cobro.

Debe conectar los [KPIs críticos de captación, comercialización, unit economics y finanzas](../../Situacion_en_España/Economía_inmobiliaria.md#6-kpis-críticos) con eventos registrados en los sistemas.

## 6. Herramientas implicadas

- [CRM inmobiliarios](../../ecosistema_tecnologico/02_sistemas_core/crm-inmobiliarios.md)
- [ERP](../../ecosistema_tecnologico/02_sistemas_core/erp.md)
- [Contabilidad](../../ecosistema_tecnologico/02_sistemas_core/contabilidad.md)
- [Facturación](../../ecosistema_tecnologico/02_sistemas_core/facturacion.md)
- [Portales inmobiliarios](../../ecosistema_tecnologico/03_canales_y_productividad/portales-inmobiliarios.md)
- [Analítica web](../../ecosistema_tecnologico/04_marketing_y_contenido/analitica-web.md)
- [BI y gobierno de datos](../../ecosistema_tecnologico/00_metodologia/alcance-y-taxonomia.md#datos-automatización-e-ia) — **categoría planificada**

## 7. Consecuencias

- Atribución incorrecta de leads y cierres.
- Forecast basado en estados desactualizados.
- Dificultad para comparar agentes, oficinas o portales.
- Cálculos manuales de comisiones y rentabilidad.
- Cierre mensual lento.
- Discusiones sobre qué cifra es correcta.
- Decisiones tardías sobre presupuesto, cartera y capacidad.

## 8. Frecuencia

**Frecuente.** La confianza es media: la baja adopción relativa de BI en empresas inmobiliarias de diez o más empleados y las reseñas sobre informes externos sostienen el mecanismo. No existe porcentaje nacional de agencias que reconstruya reportes en Excel.

La exportación a Excel puede ser una opción legítima y no implica por sí misma baja calidad.

## 9. Impacto

**Alto.** En agencias con varias oficinas, agentes, fuentes de leads o reglas de reparto, el impacto es mayor. En una microagencia puede tolerarse durante más tiempo, aunque siga consumiendo trabajo administrativo.

No se cuantifica pérdida económica: se requiere comparar decisiones, errores y horas de conciliación con datos reales.

## 10. Urgencia

**Alta.** El reporting deficiente no siempre paraliza una operación individual, pero impide corregir problemas de captación, seguimiento y rentabilidad de forma temprana.

## 11. Soluciones actuales

- Informes incluidos en CRM y portales.
- Exportación a Excel o CSV.
- Dashboards en Power BI, Looker Studio o herramientas equivalentes.
- Data warehouse y procesos ETL.
- Campos obligatorios y taxonomía común.
- Conciliación entre CRM, facturación y contabilidad.
- Revisión periódica de calidad y definición de responsables.

## 12. Limitaciones de las soluciones actuales

- Un dashboard no corrige datos ausentes o mal clasificados.
- Los exports crean copias y problemas de versión.
- Los modelos personalizados requieren mantenimiento.
- Integrar costes e ingresos exige enlazar sistemas administrativos.
- Los cambios en campos o APIs pueden romper informes.
- Las herramientas avanzadas pueden resultar desproporcionadas para microagencias.
- La atribución multicanal permanece incompleta si conversaciones y cierres no se registran.

## 13. Nivel de evidencia

**Alto.** La evidencia es alta para la brecha entre CRM y BI y media para la dependencia de informes externos.

La evidencia combina estadística oficial, un informe profesional de calidad de datos, documentación de producto y una síntesis de reseñas verificadas.

## Validación

- **Nivel de confianza:** Alto. La confianza es media para la dependencia de informes externos.
- **Número de fuentes consultadas:** 4 fuentes independientes
- **Calidad de las fuentes:** 2 altas y 2 medias
- **Posibles contradicciones:** Follow Up Boss, Propertybase e Idealista/tools ofrecen informes y reciben valoraciones positivas. Excel puede ser una salida deliberada y eficaz. El dolor aparece cuando sustituye una fuente fiable o exige conciliación reiterada.
- **Aspectos pendientes de confirmar:** horas mensuales de preparación; porcentaje de campos completos; precisión del origen; diferencias CRM-contabilidad; ajustes manuales; uso de BI por tamaño; decisiones modificadas por datos tardíos.

---

← [Anterior: Automatización parcial del flujo comercial](20-automatizacion-parcial-del-flujo-comercial.md) | [Índice](../README.md) | [Siguiente: Desincronización en multipublicación y portales →](22-desincronizacion-en-multipublicacion-y-portales.md)
