# Servicio profesional — Sprint de Orquestación de Leads

## 1. Nombre y estado

**Sprint de Orquestación de Leads y Seguimiento**  
**Tipo:** implantación profesional productizada  
**Estado:** oferta respaldada; **MVP recomendado para validación, no piloto autorizado**  
**Confianza:** media

## 2. Problema principal que resuelve

Los leads entran por portal, web, email, teléfono o mensajería; la conversación cambia de canal y el resultado no siempre vuelve al CRM. Aparecen respuestas tardías, consultas sin dueño, notas incompletas y abandono después del primer intento.

**Dolores:** D07 respuesta tardía, D19 fragmentación y D20 automatización parcial. D02 y D08 son adyacentes, pero no se promete mejorar intención del lead ni toda la comunicación de la operación.

El servicio no genera demanda ni corrige una cartera mal captada o sobrevalorada. M02 indica que la calidad de la oferta puede pesar más que el volumen bruto de leads; por ello, el alcance se limita a ejecutar mejor sobre demanda ya existente.

## 3. Cliente Ideal

**Principal:** [ICP-01](../../Modulo-08-Cliente-Ideal-ICP/ICP/ICP-01.md), agencia independiente de 3–20 agentes con CRM activo, más de dos canales, responsable de CRM/operaciones y dirección con autonomía.

**Condicionado:** ICP-03 en fase de lanzamiento de promoción, si pagador, volumen y ventana de implantación están confirmados.

## 4. Objetivo

Conseguir que cada lead del alcance:

1. se registre con origen e identidad mínimos;
2. tenga responsable y SLA interno;
3. genere siguiente acción;
4. escale o se reasigne cuando se incumple la regla;
5. deje un resultado trazable en el sistema acordado.

## 5. Descripción y alcance

### Incluye

- diagnóstico corto y línea base;
- diseño de reglas de entrada, deduplicación, reparto y seguimiento;
- integración de uno o dos canales prioritarios con un CRM;
- estados y campos mínimos;
- alertas de excepción y cola de revisión humana;
- panel operativo básico;
- pruebas con casos normales, duplicados y fallos;
- manual de operación, ownership y handoff;
- medición antes/después durante el periodo acordado.

### No incluye

- bot autónomo de venta;
- sustitución del CRM;
- campañas de marketing o compra de leads;
- cobertura universal de WhatsApp personal, voz y todos los portales;
- scoring financiero o discriminatorio;
- garantía de conversión, captación o ingresos;
- expediente, KYC, firma, pagos o notaría.

## 6. Beneficios

- **Tiempo:** reduce copia manual y persecución de responsables.
- **Coste:** puede disminuir tiempo administrativo; se mide, no se presupone.
- **Productividad:** prioriza excepciones y siguientes acciones.
- **Experiencia:** aumenta consistencia de primera respuesta y continuidad.
- **Errores:** reduce leads duplicados, sin origen o sin responsable.
- **Ingresos:** potencial al evitar omisiones de seguimiento; sin promesa causal.
- **Implantación:** aprovecha CRM y canales existentes; alcance de 1–2 integraciones.

## 7. Diferenciación

Inmovilla y Witei gestionan CRM y tareas; idealista/tools concentra parte de la demanda; Make automatiza conexiones; Structurely demuestra conversación automatizada en EE. UU.

La oferta se diferencia por:

- implantación neutral sobre el CRM existente;
- reglas de excepción, reasignación y supervisión, no solo automatización “feliz”;
- medición del retorno al registro después de la conversación;
- adaptación al canal y consentimiento aplicables en España;
- diseño de ownership y adopción junto al conector;
- portabilidad y documentación de salida.

No supera la distribución ni todas las APIs de los proveedores instalados. Su ventaja es el time-to-value sobre un flujo acotado y la responsabilidad operativa transversal.

## 8. Complejidad de implementación

**Media.** O05 del Módulo 06 la clasifica media: hay conectores maduros, pero identidad, deduplicación, reasignación, horarios, fallos y actividad fuera del CRM exigen pruebas y cambio de proceso.

## 9. Escalabilidad

- **Servicio personalizado:** medio; reglas y conectores varían.
- **Producto repetible:** alto para combinaciones CRM–canal recurrentes.
- **SaaS:** alto potencial como monitor y motor de reglas.
- **Plataforma:** posible tras varios conectores.
- **Marketplace:** futuro para plantillas/conectores validados.
- **IA como servicio:** opcional y posterior; no necesaria para el MVP.

## 10. Dependencias

- API, webhook, email estructurado o exportación del canal;
- permisos y límites del CRM;
- identificadores de lead, contacto e inmueble;
- números/canales corporativos y consentimiento cuando proceda;
- responsable de reglas y horario;
- calidad mínima de datos y entorno de prueba;
- proceso de escalado humano.

## 11. Riesgos

- **Técnico — medio:** APIs incompletas, duplicados y fallos silenciosos.
- **Comercial — medio:** el CRM puede afirmar que ya cubre el caso.
- **Regulatorio — medio:** RGPD, consentimiento y mensajería; mayor si se capturan conversaciones.
- **Operativo — medio/alto:** automatizar un reparto mal diseñado amplifica conflictos.
- **Competitivo — medio/alto:** CRM, portal e iPaaS pueden añadir capacidades equivalentes.

## 12. Hipótesis pendientes

1. El tiempo/responsabilidad es un dolor pagable, no solo disciplinario.
2. Uno o dos canales concentran suficiente volumen.
3. El cliente aceptará canal corporativo y estados mínimos.
4. La mejora de trazabilidad se mantiene tras el sprint.
5. Los conectores se reutilizan sin soporte desproporcionado.
6. Existe diferencia medible frente a configurar mejor el CRM actual.

## 13. Validación

**Evidencia utilizada**

- M01: tejido atomizado y margen proxy limitado, que favorecen un alcance acotado ([Economía](../../Situacion_en_España/Economía_inmobiliaria.md#1-resumen-ejecutivo)).
- M02: gestión de demanda y secuencia contacto→seguimiento ([Proceso](../../analisis_del_mercado/02-funcionamiento.md#gestión-de-demanda)).
- M03: fallos en entrada, WhatsApp, CRM y feedback ([Flujo](../../ecosistema_tecnologico/01_arquitectura_y_flujos/flujo-lead-postventa.md#2-traspasos-de-datos-detalle)).
- M04: D07, D19 y D20 ([Ranking](../../Modulo-04-Dolor-del-Cliente/Analisis/Ranking.md)).
- M05: línea omnicanal y continuidad insuficientes ([Competencia](../../Modulo-05-Competencia/Resumen-Ejecutivo.md#7-necesidades-sin-cobertura-suficiente)).
- M06: O05, score 89 y facilidad de medición ([O05](../../Modulo-06-Oportunidades-de-Negocio/Oportunidades/05-Oportunidad.md)).
- M08: ICP-01 y DMU directa ([ICP-01](../../Modulo-08-Cliente-Ideal-ICP/ICP/ICP-01.md)).

**Supuestos:** APIs disponibles, volumen semanal, sponsor y línea base accesible.  
**Pendiente:** medir por canal tiempo a primera respuesta, porcentaje con responsable/siguiente acción, segundos contactos, progresión, incidencias y horas de soporte. La disposición a pagar requiere piloto.
