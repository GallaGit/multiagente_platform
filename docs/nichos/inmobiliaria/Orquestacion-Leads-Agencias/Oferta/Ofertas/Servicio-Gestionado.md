# Servicio gestionado — Continuidad Operativa Gestionada

## 1. Nombre y estado

**Continuidad Operativa Gestionada**  
**Tipo:** mantenimiento y operación recurrente  
**Estado:** hipótesis de oferta  
**Confianza:** baja

## 2. Problema principal que resuelve

Una automatización implantada puede degradarse por cambios de API, credenciales, campos, usuarios, reglas o hábitos. El Módulo 05 documenta que BI, gobierno documental, ciberseguridad e iPaaS están diseñados para roles que la microagencia normalmente no tiene; la intensidad concreta debe validarse por cliente.

**Dolores:** D19–D22, D23 y D29. La existencia del mantenimiento técnico está respaldada; que el ICP prefiera externalizarlo y pagarlo de forma recurrente no lo está.

## 3. Cliente Ideal

**Principal:** ICP-01 después de completar una implantación y demostrar valor.  
**Secundario:** ICP-02 con PMS/CRM y operación recurrente.  
**Condicionado:** ICP-04 solo con autonomía contractual y acceso confirmado.

No se ofrece como entrada a clientes sin proceso, owner o línea base.

## 4. Objetivo

Mantener saludables las integraciones y controles implantados:

- detectar fallos y colas;
- corregir reglas bajo gobierno de cambios;
- vigilar calidad mínima;
- gestionar accesos técnicos;
- informar incidencias y tendencias;
- sostener la adopción y la documentación.

## 5. Descripción y alcance

### Incluye

1. monitorización de automatizaciones acordadas;
2. revisión de errores, reintentos y colas;
3. control de credenciales y caducidades;
4. chequeos de duplicidad, completitud y estados;
5. mantenimiento menor de reglas y mapeos;
6. reporte periódico de operación;
7. reunión de gobierno y backlog;
8. documentación de cambios y soporte acotado.

### No incluye

- soporte general de todos los proveedores;
- administración total del CRM;
- desarrollo ilimitado;
- operación comercial en nombre del cliente;
- SOC, pentest, DPO, compliance o asesoría legal;
- disponibilidad 24/7 salvo alcance futuro validado;
- garantía sobre APIs o servicios de terceros.

## 6. Beneficios

- **Tiempo:** evita que el equipo investigue fallos técnicos recurrentes.
- **Coste:** convierte mantenimiento ad hoc en capacidad planificada; ahorro por validar.
- **Productividad:** conserva reglas y paneles utilizables.
- **Experiencia:** reduce incidencias silenciosas que afectan respuesta o estado.
- **Errores:** detecta cambios, duplicados y colas antes.
- **Ingresos:** protege continuidad del flujo, sin atribución económica garantizada.
- **Implantación:** alta para clientes ya implantados; baja para un cliente nuevo.

## 7. Diferenciación

Make ofrece ejecución y logs; CRM y SaaS soportan su producto; consultoras mantienen proyectos. Esta oferta gestiona el **resultado transversal** de una combinación concreta:

- SLA operativo sobre el flujo, no sobre una aplicación;
- reglas y métricas inmobiliarias;
- registro de excepciones y cambios;
- revisión de calidad y adopción;
- portabilidad y runbook de salida.

No sustituye el soporte del fabricante y depende de sus SLA. La ventaja solo será defendible si se acumulan conectores, controles y benchmarks propios.

## 8. Complejidad de implementación

**Media.** Es sencilla tras una implantación estandarizada, pero crece con número de conectores, criticidad, horarios, personalizaciones y dependencia de terceros.

## 9. Escalabilidad

- **Servicio personalizado:** medio.
- **Producto repetible:** alto con catálogo limitado.
- **SaaS:** alto; monitorización y controles pueden productizarse.
- **Plataforma:** posible como control plane.
- **Marketplace:** futuro para conectores mantenidos.
- **IA como servicio:** útil para clasificación de incidentes, con revisión.

## 10. Dependencias

- oferta profesional o automatización previa;
- telemetría, logs y permisos;
- APIs y contratos de terceros;
- inventario de cambios y responsables;
- canal de soporte y escalado;
- política de accesos, backup y continuidad;
- catálogo de qué está dentro/fuera.

## 11. Riesgos

- **Técnico — medio/alto:** cambios externos y fallos no observables.
- **Comercial — alto:** recurrencia y disposición a pagar no demostradas.
- **Regulatorio — medio/alto:** acceso persistente a datos y credenciales.
- **Operativo — alto:** soporte personalizado, guardias y alcance difuso pueden erosionar margen.
- **Competitivo — alto:** fabricantes o MSP generalistas pueden absorber la función.

## 12. Hipótesis pendientes

1. El cliente valora prevención frente a soporte reactivo.
2. La frecuencia de incidencias justifica recurrencia.
3. Un catálogo limitado cubre la mayoría de casos.
4. El soporte puede prestarse con márgenes sostenibles.
5. Los límites y SLA son comprensibles.
6. Los datos operativos pueden usarse de forma agregada y autorizada para mejorar controles.

## 13. Validación

**Evidencia utilizada**

- M01: tejido micro y margen proxy sectorial limitado ([Economía](../../Situacion_en_España/Economía_inmobiliaria.md#1-resumen-ejecutivo)).
- M02: proceso con múltiples terceros ([Funcionamiento](../../analisis_del_mercado/02-funcionamiento.md)).
- M03: microagencia sin capacidad iPaaS y flujo fragmentado ([Fricciones](../../ecosistema_tecnologico/07_analisis_transversal/puntos-de-friccion.md)).
- M04: D19–D23 y D29 ([Resumen](../../Dolor-del-Cliente/Resumen-Ejecutivo.md)).
- M05: las plataformas horizontales exigen mantenimiento y las microagencias carecen normalmente de roles dedicados ([Competencia](../../Competencia/Analisis/Vacios-Competitivos.md)).
- M06: O15 y dependencias muy altas ([O15](../../Oportunidades-de-Negocio/Oportunidades/15-Oportunidad.md)).
- M08: ICP-01 tiene base digital y un posible champion de operaciones/CRM ([ICP-01](../../Cliente-Ideal-ICP/ICP/ICP-01.md)).

**Supuestos:** base instalada, telemetría y alcance estable.  
**Pendiente:** registrar incidencias por conector, horas, cambios, tiempos de resolución, churn, coste de soporte y aceptación de mantenimiento recurrente en al menos tres clientes.
