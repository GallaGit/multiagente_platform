# Producto SaaS potencial — Control de Continuidad

## 1. Nombre y estado

**Control de Continuidad Operativa SaaS**  
**Tipo:** producto SaaS B2B potencial  
**Estado:** hipótesis  
**Confianza:** baja

## 2. Problema principal que resuelve

La agencia carece de una vista neutral de los fallos entre herramientas: registros sin responsable, estados incompatibles, duplicados, integraciones detenidas, documentos faltantes y discrepancias de reporting.

**Dolores:** D19–D22 y D29. La oportunidad O15 está respaldada y ocupa el primer puesto; que un SaaS independiente sea el formato correcto no está validado.

## 3. Cliente Ideal

**Inicial potencial:** ICP-01 con stack homogéneo ya observado en varios servicios.  
**Expansión:** ICP-02 para continuidad CRM–PMS y, más tarde, ICP-04 si existe autonomía.

El producto no debe lanzarse para “todas las inmobiliarias”; necesita una combinación concreta de CRM, canal y proceso.

## 4. Objetivo

Proporcionar un control plane que, sin sustituir aplicaciones:

- reciba señales autorizadas;
- aplique controles de calidad y continuidad;
- muestre excepciones;
- asigne owner;
- conserve trazabilidad;
- mida salud del flujo y de los conectores.

## 5. Descripción y alcance

### MVP hipotético

1. un CRM y uno o dos canales;
2. catálogo limitado de controles;
3. panel de excepciones y responsables;
4. alertas, reintentos y auditoría;
5. configuración por plantilla;
6. exportación de datos y logs;
7. administración de permisos;
8. métricas de salud, no de “ROI automático”.

### No incluye

- CRM, PMS, DMS o ERP completo;
- almacenamiento indiscriminado de conversaciones/documentos;
- publicación multiportal universal;
- KYC, pagos o notaría;
- BI financiero completo;
- agente IA autónomo;
- conectores no autorizados o scraping;
- personalización ilimitada.

## 6. Beneficios

- **Tiempo:** centraliza revisión de excepciones.
- **Coste:** potencial menor mantenimiento manual; por demostrar.
- **Productividad:** enfoca al equipo en casos fallidos.
- **Experiencia:** reduce silencios y estados desfasados.
- **Errores:** controles continuos e historial.
- **Ingresos:** protección indirecta del flujo; no cuantificada.
- **Implantación:** media si usa plantillas; alta por nuevo conector.

## 7. Diferenciación

Los CRM controlan su dominio; Make orquesta; Power BI visualiza; suites integran dentro de su perímetro. El SaaS se diferenciaría por:

- neutralidad entre proveedores;
- controles inmobiliarios preconfigurados;
- énfasis en excepción, calidad y portabilidad;
- vista de proceso, no de aplicación;
- implantación ligera derivada de patrones de servicio;
- salida exportable y trazabilidad.

La diferenciación desaparecerá si solo ofrece dashboards o automatizaciones simples. Debe probar menor time-to-value y coste de mantenimiento que iPaaS + BI + consultoría.

## 8. Complejidad de implementación

**Muy alta.** Multi-tenancy, conectores, identidad, permisos, monitorización, esquemas, cambios de API, seguridad, soporte y migración. O15 ya clasifica la interoperabilidad como muy alta.

## 9. Escalabilidad

- **Servicio personalizado:** necesario durante aprendizaje.
- **Producto repetible:** objetivo principal.
- **SaaS:** forma propuesta.
- **Plataforma:** evolución natural si amplía conectores y reglas.
- **Marketplace:** posible para conectores/controles certificados.
- **IA como servicio:** futura para priorizar excepciones, no esencial.

## 10. Dependencias

- repetición demostrada de stacks y controles;
- acuerdos/API y estabilidad de proveedores;
- modelo de datos común;
- identidad, permisos y aislamiento multi-tenant;
- observabilidad, soporte y seguridad;
- canal de distribución;
- economía de onboarding y mantenimiento;
- permiso para procesar datos.

## 11. Riesgos

- **Técnico — muy alto:** conectores y datos legacy.
- **Comercial — muy alto:** ARPU, compra y canal no demostrados.
- **Regulatorio — alto:** tratamiento centralizado y subencargados.
- **Operativo — muy alto:** soporte por cliente puede convertir SaaS en servicios.
- **Competitivo — alto:** incumbentes controlan datos y distribución.

## 12. Hipótesis pendientes

1. Tres o más clientes comparten stack, reglas y valor.
2. El producto puede configurarse sin proyecto.
3. El cliente acepta una capa adicional.
4. Los proveedores permiten integración sostenible.
5. El coste de conector/soporte queda por debajo de la recurrencia.
6. La neutralidad es un criterio de compra real.
7. Los controles reducen incidencias frente a Make/CRM nativos.

## 13. Validación

**Evidencia utilizada**

- M01: mercado grande pero 98,6% micro, tensión para ARPU ([Economía](../../Situacion_en_España/Economía_inmobiliaria.md#1-resumen-ejecutivo)).
- M02: proceso E2E con múltiples sistemas ([Proceso](../../analisis_del_mercado/02-funcionamiento.md)).
- M03: integraciones raras y datos aislados ([Vacíos](../../ecosistema_tecnologico/07_analisis_transversal/vacios-tecnologicos.md)).
- M04: D19–D22 y D29 ([Resumen](../../Modulo-04-Dolor-del-Cliente/Resumen-Ejecutivo.md)).
- M05: interoperabilidad y calidad como espacio estratégico ([Competencia](../../Modulo-05-Competencia/Resumen-Ejecutivo.md#3-interoperabilidad-y-calidad-del-dato-en-el-stack-español)).
- M06: O15, índice 96, complejidad muy alta ([O15](../../Modulo-06-Oportunidades-de-Negocio/Oportunidades/15-Oportunidad.md)).
- M08: ICP-01 es candidato de validación, no compra demostrada ([Resumen ICP](../../Modulo-08-Cliente-Ideal-ICP/Resumen-Ejecutivo.md)).

**Supuestos:** patrones repetibles, APIs y economía favorable.  
**Pendiente:** no construir antes de observar varias implantaciones, aceptación recurrente, coste real de soporte y retención de un servicio gestionado.
