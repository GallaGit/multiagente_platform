# Resumen ejecutivo

## Decisión

El portafolio debe comenzar como un servicio medible de integración operativa para agencias residenciales independientes profesionalizadas, no como un SaaS horizontal ni como un “agente IA” autónomo.

La evidencia converge en cuatro hechos:

1. España tiene una base amplia y atomizada —58.106 empresas CNAE 6831 y 98,6% de microempresas en CNAE 683—, pero la capacidad de implantación y pago del tejido pequeño no está demostrada ([Módulo 01](../Situacion_en_España/Economía_inmobiliaria.md#1-resumen-ejecutivo)).
2. El proceso inmobiliario cruza captación, publicación, conversación, documentación, financiación, notaría, cobro y postventa ([Módulo 02](../analisis_del_mercado/02-funcionamiento.md#21-compraventa-residencial-paso-a-paso)).
3. CRM, portales, WhatsApp, firma, carpetas y facturación están digitalizados, pero los traspasos siguen siendo manuales y opacos ([Módulo 03](../ecosistema_tecnologico/01_arquitectura_y_flujos/flujo-lead-postventa.md#2-traspasos-de-datos-detalle)).
4. Los problemas D19–D21 —fragmentación, automatización parcial y reporting poco fiable— están triangulados; la continuidad entre herramientas está peor cubierta que las funciones aisladas ([Módulo 04](../Modulo-04-Dolor-del-Cliente/Resumen-Ejecutivo.md#problemas-raíz-repetidos), [Módulo 05](../Modulo-05-Competencia/Resumen-Ejecutivo.md#1-tesis)).

## Portafolio inicial

| Nivel | Oferta | Resultado principal | Estado |
|---|---|---|---|
| Entrada | Diagnóstico de Continuidad Operativa | Línea base y caso priorizado con evidencia | Respaldada; pago por validar |
| Profesional | Sprint de Orquestación de Leads | Lead asignado, trazable y con siguiente acción | MVP recomendado |
| Premium | Expediente Operativo Integrado | Requisitos, versiones y responsables visibles | Hipótesis de oferta |
| Gestionado | Continuidad Operativa Gestionada | Monitorización y mantenimiento recurrentes | Hipótesis de oferta |
| Consultoría | Diseño de Procesos y Gobierno del Dato | Modelo operativo, roles y métricas comunes | Respaldada; demanda por validar |
| A medida | Automatización de Flujos Críticos | Menos re-tecleo y excepciones visibles | Respaldada por caso |
| IA | Copiloto de Operaciones | Resumen y propuesta de siguiente acción con revisión | Hipótesis |
| SaaS | Control de Continuidad | Alertas y calidad transversal repetibles | Hipótesis |
| Futuro | Plataforma Operativa Interoperable | Capa común de operación y datos | Hipótesis de largo plazo |

## Cliente prioritario

El destinatario inicial es el [ICP-01](../Modulo-08-Cliente-Ideal-ICP/ICP/ICP-01.md): agencia residencial independiente con 3–20 agentes, al menos cinco usuarios activos, CRM vertical, más de dos canales, WhatsApp o Excel fuera del registro, datos exportables y propietario-gerente accesible.

No se recomienda empezar por:

- equipos de 0–2 personas, por presupuesto y capacidad operativa inciertos;
- franquiciados sin autonomía tecnológica;
- grandes operadores, por seguridad, procurement e integración;
- agencias sin CRM o sin responsable interno;
- clientes que esperan “IA” sin cambiar disciplina de proceso.

## Por qué compraría el cliente

La razón de compra debe ser un resultado observable, no la tecnología:

- conocer cuántos leads quedan sin responsable o siguiente acción;
- reducir reintroducciones y conciliaciones manuales;
- recuperar trazabilidad cuando una conversación sale del CRM;
- identificar fallos antes de que lleguen al cliente o al cierre;
- disponer de una línea base y evidencia del cambio.

No se promete ahorro, conversión ni ingresos hasta medirlos en el cliente.

## Diferenciación

La oferta no compite frontalmente con Inmovilla, Witei, idealista/tools, Make, Power BI, Signaturit o DocuSign. Los usa cuando encajan y se diferencia en:

1. **neutralidad sobre el stack instalado**;
2. **continuidad entre sistemas**, no otra función aislada;
3. **implantación con proceso, datos, adopción y control de excepciones**;
4. **medición antes/después** con criterios acordados;
5. **adaptación a canales y regulación española**;
6. **salida y portabilidad documentadas**, reduciendo lock-in.

La competencia puede replicar módulos concretos y ya dispone de distribución. La defensa futura deberá provenir de conectores mantenidos, modelo de datos, biblioteca de controles, evidencia operativa y conocimiento vertical; no de usar IA.

## Secuencia económica y de escalabilidad

`diagnóstico → sprint profesional → automatizaciones → mantenimiento → SaaS`

- Los servicios iniciales descubren patrones y reducen riesgo.
- Las automatizaciones convierten patrones repetidos en activos reutilizables.
- El mantenimiento aporta recurrencia y telemetría.
- El SaaS solo se justifica tras demostrar repetición entre stacks comparables.
- La plataforma futura exige suficiente base instalada, permisos y economía de soporte.

## Riesgos decisivos

- **Comercial:** no hay disposición a pagar observada.
- **Técnico:** APIs incompletas, canales personales, datos deficientes y límites de portales.
- **Operativo:** personalización excesiva puede impedir margen y escalabilidad.
- **Regulatorio:** RGPD, PBC/FT, identidad y pagos elevan responsabilidad.
- **Competitivo:** CRM e iPaaS existentes pueden ampliar cobertura.
- **Segmentación:** “microagencia” es amplia y no equivale al ICP-01.

## Oferta Recomendada para el MVP

Priorizar el **Sprint de Orquestación de Leads**, con un diagnóstico corto como fase cero.

La prioridad significa **primera oferta a validar**, no autorización inmediata de piloto: el Módulo 07 conserva todas sus candidatas sin puntuación ni decisión final.

Es la mejor combinación actual porque:

- aborda D07, D19 y D20, problemas documentados y observables;
- cubre P05–P07, al inicio del flujo donde una omisión todavía puede corregirse;
- aprovecha H01–H04 y H14 existentes sin reemplazar el CRM;
- tiene complejidad media, menor exposición regulatoria que expediente, KYC o pagos;
- encaja con el ICP-01, que tiene autonomía y base digital;
- permite validar tiempo de respuesta, asignación y seguimiento sin inventar ROI;
- crea conectores y reglas reutilizables para la oferta gestionada y el SaaS.

No se propone aumentar el volumen de leads. El Módulo 02 advierte que una cartera captada, documentada y valorada correctamente puede ser más determinante que la demanda bruta. El MVP controla la ejecución sobre leads existentes; captación y valoración requieren discovery propio.

**Confianza:** media. El problema y el encaje técnico están respaldados; el alcance comprable, el coste de implantación, el resultado económico y la voluntad de pago siguen pendientes de entrevistas y piloto.
