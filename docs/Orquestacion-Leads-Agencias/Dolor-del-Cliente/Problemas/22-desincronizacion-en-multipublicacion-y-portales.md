# Desincronización en multipublicación y portales

**Corte:** 12 de agosto de 2026  
**Ámbito:** agencias inmobiliarias en España; evidencia internacional solo como contraste de software equivalente

**Evaluación:**

- **Frecuencia:** Ocasional por ficha y recurrente como riesgo en operaciones multiportal; sin tasa nacional
- **Impacto:** Alto
- **Impacto económico:** Alto cuando afecta captación o leads; sin cuantía demostrada
- **Impacto operativo:** Alto y sensible al tiempo
- **Frustración:** alta
- **Urgencia:** alta para precio, reserva, venta o retirada
- **Personas afectadas:** captadores, agentes, marketing, administración, propietarios y demandantes

## 1. Nombre del problema

Desincronización de fichas, estados, precios y leads entre CRM, web, MLS y portales inmobiliarios.

## 2. Descripción

La multipublicación permite mantener varios escaparates desde una ficha central, pero depende del alcance del conector, las reglas de cada portal y la calidad del dato de origen. Un cambio puede no propagarse, llegar tarde o ser rechazado.

Además, un mismo inmueble puede aparecer publicado por diferentes agencias o por el propietario, con precio, fotos o estado distintos. No todo duplicado es un fallo técnico: los encargos abiertos también generan duplicidad legítima, aunque igualmente confunden al mercado.

## 3. Evidencias

### Idealista/tools

- **Organización/autor:** Idealista
- **Título:** *Control de duplicados*
- **Fecha:** sin fecha visible; consultado el 12 de agosto de 2026
- **Tipo/calidad:** documentación oficial de producto; **alta para la función**
- **URL:** <https://www.idealista.com/tools/centrodeayuda/it/articulos/controllo-dei-duplicati/>
- **Respaldo exacto:** describe detección en tiempo real de anuncios duplicados publicados por otra agencia o particular, incluidos cambios de precio, nuevas publicaciones y desactivaciones en otros portales. Confirma que la duplicidad multiportal es un fenómeno que la herramienta monitoriza.

### Idealista/tools

- **Organización/autor:** Idealista
- **Título:** *¿Cómo editar las características de un inmueble?*
- **Fecha:** sin fecha visible; consultado el 12 de agosto de 2026
- **Tipo/calidad:** documentación oficial de producto; pertenece a la misma organización que la fuente anterior
- **URL:** <https://www.idealista.com/tools/centrodeayuda/articulos/como-editar-las-caracteristicas-de-un-inmueble/>
- **Respaldo exacto:** documenta la edición de datos de la ficha y la publicación en todos los portales disponibles desde un solo menú. Acredita el mecanismo centralizado, no una tasa de fallos.

### Comisión Nacional de los Mercados y la Competencia

- **Organización/autor:** CNMC
- **Título:** *La CNMC multa con 1,25 millones a varias empresas por imponer comisiones mínimas en la intermediación inmobiliaria*
- **Fecha:** 9 de diciembre de 2021
- **Tipo/calidad:** resolución y comunicación de regulador; **alta**
- **URL:** <https://www.cnmc.es/prensa/sancionador-proptech-cnmc-intermediacion-inmobiliaria-cnmc-20211209>
- **Respaldo exacto:** documenta el funcionamiento de una base MLS compartida y la compatibilidad desarrollada entre Habitania/Idealista Tools, Inmovilla y otros sistemas. Demuestra la interdependencia tecnológica del intercambio de inmuebles; el expediente no estudia calidad de sincronización.

### Trustpilot

- **Organización/autor:** Trustpilot; usuarios de Reapit
- **Título:** *Reapit Reviews*
- **Fecha:** consulta del 12 de agosto de 2026
- **Tipo/calidad:** 103 reseñas mostradas; **baja/complementaria**
- **URL:** <https://www.trustpilot.com/review/www.reapit.com>
- **Respaldo exacto:** incluye una experiencia donde propiedades dejaron de mostrarse y páginas de ventas fallaron. También contiene opiniones que describen el software como fiable y eficiente.

### National Association of REALTORS

- **Organización/autor:** National Association of REALTORS
- **Título:** *2025 REALTORS Technology Survey*
- **Fecha:** 18 de septiembre de 2025
- **Tipo/calidad:** encuesta profesional estadounidense, 1.241 respuestas; **media**
- **URL:** <https://cms.nar.realtor/sites/default/files/2025-09/2025-realtors-technology-survey-report-09-18-2025.pdf>
- **Respaldo exacto:** solo el 9% señaló sindicación o portales como la tecnología que aportaba más leads de calidad, frente al 23% para CRM. Es contraste de valor percibido en Estados Unidos, no medición de sincronización ni del mercado español.

Las dos páginas de Idealista cuentan como una sola fuente independiente. En total se emplean cuatro organizaciones independientes.

## 4. Personas afectadas

- Captadores responsables de la exactitud de la cartera.
- Agentes que reciben consultas.
- Marketing y administración de publicaciones.
- Propietarios, al ver información desactualizada.
- Demandantes, al consultar activos no disponibles.
- Equipos de soporte del CRM y del portal.

## 5. Proceso afectado

Incide directamente en la [comercialización](../../analisis_del_mercado/02-funcionamiento.md#comercialización): preparación, publicación, modificación y retirada del anuncio.

También afecta a la [producción y comercialización](../../Situacion_en_España/Economía_inmobiliaria.md#producción-y-comercialización), especialmente a inventario, generación de contactos y seguimiento.

## 6. Herramientas implicadas

- [Portales inmobiliarios](../../ecosistema_tecnologico/03_canales_y_productividad/portales-inmobiliarios.md)
- [CRM inmobiliarios](../../ecosistema_tecnologico/02_sistemas_core/crm-inmobiliarios.md)
- [MLS](../../ecosistema_tecnologico/02_sistemas_core/mls.md)
- [Web/CMS de captación](../../ecosistema_tecnologico/04_marketing_y_contenido/web-cms-captacion.md)
- [Email](../../ecosistema_tecnologico/03_canales_y_productividad/email.md)
- [Gobierno de datos y automatización](../../ecosistema_tecnologico/00_metodologia/alcance-y-taxonomia.md#datos-automatización-e-ia) — **categoría planificada**

## 7. Consecuencias

- Anuncios activos después de reserva o venta.
- Precios o características diferentes por canal.
- Duplicados con otros anunciantes.
- Leads sobre inmuebles no disponibles.
- Reclamaciones y pérdida de confianza del propietario.
- Correcciones manuales en varios portales.
- Métricas de rendimiento y origen incompletas.
- Amplificación del error al publicar simultáneamente.

## 8. Frecuencia

**Ocasional.** Por ficha y recurrente como riesgo operativo, con confianza media. Las fuentes demuestran la existencia de duplicados, multipublicación y fallos concretos, pero no cuántas fichas españolas sufren desincronización.

No se etiqueta como “muy frecuente” porque falta telemetría de CRM y portales.

## 9. Impacto

**Alto.** Una actualización errónea puede afectar simultáneamente varios canales y provocar contactos improductivos. No se cuantifican leads o ingresos perdidos.

## 10. Urgencia

**Alta** para cambios que alteran disponibilidad, precio o situación contractual. Una demora breve puede ser material cuando continúan entrando consultas.

## 11. Soluciones actuales

- Ficha maestra y multipublicación desde CRM.
- APIs o feeds contratados.
- Monitor de duplicados.
- Alertas de rechazo o estado de publicación.
- Activación y validación portal por portal.
- Reconciliación periódica de cartera.
- Reglas de retirada al reservar o vender.
- Revisión humana de una muestra publicada.

## 12. Limitaciones de las soluciones actuales

- El alcance y la bidireccionalidad de APIs no son homogéneos.
- Cada portal aplica campos y reglas distintos.
- Un feed correcto no elimina duplicados de otros anunciantes.
- La alerta detecta un problema, pero no siempre lo corrige.
- Los accesos pueden depender del contrato profesional.
- Las incidencias implican varios proveedores y dificultan atribuir responsabilidad.
- Las reseñas individuales no permiten estimar prevalencia.

## 13. Nivel de evidencia

**Alto.** La evidencia es alta para la existencia y baja para la frecuencia.

La documentación oficial y la CNMC confirman la arquitectura y la duplicidad observable. Las reseñas aportan un fallo concreto y una contradicción positiva. Falta una tasa operativa.

## Validación

- **Nivel de confianza:** Alto. La confianza es baja para la frecuencia.
- **Número de fuentes consultadas:** 4 organizaciones independientes; 5 documentos o plataformas
- **Calidad de las fuentes:** 2 altas, 1 media y 1 complementaria
- **Posibles contradicciones:** la multipublicación funciona correctamente en numerosas configuraciones y ahorra trabajo. Reapit también recibe elogios de fiabilidad. Un duplicado puede proceder de un encargo abierto y no de un fallo.
- **Aspectos pendientes de confirmar:** errores por portal; demora de actualización; rechazos de feeds; porcentaje de leads por API frente a email; duplicados técnicos frente a comerciales; tiempo de corrección.

---

← [Anterior: Reporting poco fiable y dependiente de Excel](21-reporting-poco-fiable-y-dependiente-de-excel.md) | [Índice](../README.md) | [Siguiente: UX móvil, complejidad y soporte del CRM →](23-ux-movil-complejidad-y-soporte-del-crm.md)
