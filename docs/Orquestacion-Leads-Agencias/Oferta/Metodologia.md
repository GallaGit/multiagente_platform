# Metodología

## 1. Principio

Una oferta solo entra en el portafolio si puede enlazarse con:

1. un contexto o segmento de mercado del Módulo 01;
2. uno o más procesos observables del Módulo 02;
3. herramientas, integraciones o fricciones del Módulo 03;
4. problemas triangulados del Módulo 04;
5. cobertura y límites competitivos del Módulo 05;
6. una oportunidad clasificada en el Módulo 06;
7. un ICP explícito del Módulo 08.

El Módulo 07 aporta reglas de validación, pero su inventario no contiene todavía resultados de entrevistas o pilotos. Por tanto, ninguna propuesta se presenta como demanda validada.

### Colisión de identificadores M06/M07

Los códigos `O01–O08` del Módulo 07 no son los mismos que `O01–O08` del Módulo 06. En este módulo:

- `Oxx` sin prefijo siempre significa **M06-Oxx**;
- una candidata del marco de validación se escribe **M07-Oxx**;
- M07-O01 (trazabilidad lead–conversación) se relaciona con M06-O05, M06-O06 y M06-O15;
- M07-O02 (reescritura multisistema) se relaciona principalmente con M06-O15.

Las candidatas M07 no tienen puntuación final ni decisión. El “MVP recomendado” significa **primera oferta a validar**, no autorización de piloto o construcción.

## 2. Fuentes obligatorias

| Módulo | Uso en el diseño | Fuente principal |
|---|---|---|
| M01 Mercado | tamaño, atomización, economía y segmentos | [Situación en España](../Situacion_en_España/README.md) |
| M02 Procesos | etapas, actores y dependencias | [Funcionamiento](../analisis_del_mercado/02-funcionamiento.md) |
| M03 Software | stack, integraciones, fricciones y vacíos | [Ecosistema tecnológico](../ecosistema_tecnologico/README.md) |
| M04 Problemas | dolor, impacto, frecuencia y evidencia | [Resumen de dolores](../Modulo-04-Dolor-del-Cliente/Resumen-Ejecutivo.md) |
| M05 Competencia | alternativas, límites y espacios | [Resumen competitivo](../Modulo-05-Competencia/Resumen-Ejecutivo.md) |
| M06 Oportunidades | trazabilidad y priorización | [Ranking general](../Modulo-06-Oportunidades-de-Negocio/Analisis/Ranking-General.md) |
| M07 Validación | estados, umbrales y experimentos | [Reglas del módulo](../Modulo-07-Validacion-de-Oportunidades/README.md) |
| M08 ICP | destinatario, DMU, señales y objeciones | [Ranking de ICP](../Modulo-08-Cliente-Ideal-ICP/Analisis/Ranking-ICP.md) |

## 3. Regla de clasificación

### Respaldada

Se usa cuando problema, proceso, herramientas y cobertura parcial están documentados. No significa que el cliente pagará ni que el alcance propuesto produzca ROI.

### Hipótesis de oferta

Se usa si falta uno o más de estos elementos:

- disposición a pagar;
- comprador o firmante;
- repetibilidad entre clientes;
- acceso técnico;
- magnitud del resultado;
- coste de entrega;
- responsabilidad regulatoria asumible.

Los productos SaaS, agentes IA, servicio gestionado y plataforma futura permanecen como hipótesis aunque se apoyen en dolores respaldados.

## 4. Escalas

### Confianza

- **Alta:** evidencia convergente y alcance de oferta estrecho; aún puede faltar voluntad de pago.
- **Media:** problema sólido, pero existen dependencias o supuestos relevantes.
- **Baja:** solución, segmento o economía dependen principalmente de validación futura.

### Complejidad

- **Baja:** sin integración crítica; datos accesibles; cambio limitado.
- **Media:** 1–3 integraciones, reglas acotadas, pruebas y adopción.
- **Alta:** varios sistemas, permisos, migración, excepciones o datos sensibles.
- **Muy alta:** terceros regulados, identidad/pagos, plataforma multi-tenant o cobertura E2E.

### Valor esperado

Alto, medio o bajo según cercanía a ingreso/cierre, tiempo, coste, riesgo y experiencia. Es una clasificación cualitativa; no un ROI.

### Escalabilidad

Se analiza en seis formas: servicio personalizado, producto repetible, SaaS, plataforma, marketplace e IA como servicio. “Potencial” no equivale a viabilidad probada.

## 5. Taxonomía

Se reutilizan sin alterar los identificadores del [Módulo 06](../Modulo-06-Oportunidades-de-Negocio/Metodologia.md#5-taxonomía-de-trazabilidad):

- **Procesos P01–P15:** captación, valoración, KYC, publicación, demanda, visitas, negociación, firma, financiación, notaría, cobro, postventa, alquiler, reporting y continuidad.
- **Herramientas H01–H16:** CRM, portales, WhatsApp, productividad, MLS, web, datos, documental, KYC, banca, PMS, ERP, BI, automatización, seguridad y workspace.
- **Competidores C01–C11:** CRM españoles, idealista/tools, Prinex, especialistas visuales, firma, PMS, hipoteca, DMS, Power BI, Make y Structurely.

Los dolores se citan como **D01–D30** según el [índice del Módulo 04](../Modulo-04-Dolor-del-Cliente/README.md#índice-de-problemas). Los ICP se citan como **ICP-01–ICP-05**.

## 6. Evaluación obligatoria por oferta

Cada ficha contiene:

1. nombre y estado;
2. problema principal;
3. cliente ideal;
4. objetivo;
5. alcance incluido y excluido;
6. beneficios en siete dimensiones;
7. diferenciación frente a alternativas;
8. complejidad;
9. escalabilidad;
10. dependencias;
11. cinco riesgos;
12. hipótesis pendientes;
13. confianza, evidencia, supuestos y validación.

## 7. Regla de beneficios

Los beneficios se expresan como mecanismos, no como promesas:

- “reduce re-tecleo” es válido si se elimina un traspaso manual;
- “puede reducir coste” requiere medir tiempo y coste antes/después;
- “incrementa ingresos” solo se formula como potencial si mejora seguimiento;
- no se asignan porcentajes, ahorros o conversiones sin datos del cliente.

## 8. Criterios de priorización

La prioridad combina:

- dolor y urgencia del Módulo 04;
- posición de oportunidad del Módulo 06;
- encaje del ICP-01 del Módulo 08;
- facilidad técnica y tiempo de implantación;
- capacidad de observar una línea base;
- riesgo regulatorio;
- reutilización de activos;
- dependencia de APIs o terceros.

No se usa el score del Módulo 06 como forecast ni TAM.

## 9. Reglas de validación

Antes de llamar “validada” a una oferta:

1. al menos cinco empresas del mismo ICP deben mostrar evidencia del proceso;
2. tres deben aceptar una métrica;
3. una debe aceptar piloto pagado o compromiso económico verificable;
4. deben registrarse tiempo y coste de implantación;
5. debe comprobarse acceso a datos, APIs y responsable interno;
6. deben documentarse incidentes, excepciones y resultados antes/después.

Hasta superar esos umbrales, el trabajo autorizado es entrevista, acceso de lectura, cuantificación y prueba técnica reversible. Ninguna oferta de este módulo queda autorizada automáticamente para piloto por su posición en el portafolio.

## 10. Exclusiones metodológicas

- No se usan las cifras “30–45% de oportunidades perdidas”, “60% de leads” o “ROI 5,36:1” de `context.md`.
- CNAE 68 no se trata como sinónimo de agencias.
- La disponibilidad de una API no se trata como integración funcional.
- La capacidad anunciada de un proveedor no demuestra adopción.
- Una obligación legal no demuestra incumplimiento ni disposición a pagar.
- Un prototipo de IA no se considera autónomo, fiable ni conforme por defecto.

## 11. Control documental

Todos los enlaces internos usan rutas relativas; las fuentes externas conservan sus URL verificables. Los archivos emplean identificadores estables y lenguaje compatible con GitHub, Obsidian y sistemas RAG. Cada ficha separa evidencia, inferencia y supuesto. Ningún archivo debe superar 300 líneas.
