# Matriz de cobertura

## Convenciones

- Procesos y herramientas siguen la [taxonomía del Módulo 06](../../Oportunidades-de-Negocio/Metodologia.md#5-taxonomía-de-trazabilidad).
- Dolores D01–D30 corresponden al [Módulo 04](../../Dolor-del-Cliente/README.md#índice-de-problemas).
- ICP-01–ICP-05 corresponden al [Módulo 08](../../Cliente-Ideal-ICP/README.md).
- **Núcleo** indica cobertura directa. **Adyacente** indica beneficio posible, no alcance comprometido.

## Cobertura por oferta

| Oferta | Problemas núcleo | Procesos núcleo | Herramientas implicadas | ICP principal | Oportunidades |
|---|---|---|---|---|---|
| Diagnóstico | D19–D21, D29 | P05, P07, P14, P15; seleccionable | H01–H16 según stack | ICP-01 | O15, O16 |
| Sprint de Leads | D07, D19, D20 | P05–P07 | H01–H04, H14 | ICP-01 | O05, O06 |
| Expediente | D13, D15, D16 | P03, P07, P08, P10, P12 | H01, H08, H13, H15 | ICP-03 | O10 |
| Gestionado | D19–D23, D29 | Procesos implantados; P14–P15 | H01–H16 acotadas | ICP-01 posimplantación | O15, O16 |
| Consultoría | D19–D21, D25, D29 | P01–P15, un flujo por encargo | H01–H16 | ICP-01 | O15, O16, O19 |
| Automatización | D06, D07, D19–D22 | P04–P07, P12, P14 o P15 | H01–H16 según módulo | ICP-01 | O05, O09, O15, O16 |
| Copiloto IA | D08, D13, D20, D29 | P05, P07, P12, P15 | H01, H03, H08, H14, H16 | ICP-01 maduro | O10, O19 |
| Control SaaS | D19–D22, D29 | P04–P07, P14–P15 inicialmente | H01–H06, H13–H16 | ICP-01 homogéneo | O15, O16 |
| Plataforma | D13–D22, D24, D29 | P01–P15 por fases | H01–H16 | Varios, tras validación | O10, O11, O15, O16, O20 |

## Problemas frente a ofertas

| Problema | DIAG | LEAD | EXP | MGT | CONS | AUTO | IA | SAAS | PLAT |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| D06 Anuncios inconsistentes |  |  |  |  |  | N |  | A | A |
| D07 Respuesta tardía | A | N |  | A | A | N | A | N | A |
| D08 Comunicación irregular | A | A | A | A | A | A | N | A | A |
| D13 Expediente incompleto | A |  | N | A | A | N | N | A | N |
| D14 PBC/FT | A |  | A |  | A |  |  |  | A |
| D15 Datos dispersos | A | A | N | A | N | A | A | A | N |
| D16 Arras/firma |  |  | N | A | A | A | A | A | N |
| D17 Hipoteca/notaría |  |  | A |  | A |  |  |  | A |
| D19 Stack fragmentado | N | N | A | N | N | N | A | N | N |
| D20 Automatización parcial | N | N | A | N | N | N | N | N | N |
| D21 Reporting poco fiable | N | A | A | N | N | N | A | N | N |
| D22 Desincronización | A |  |  | N | A | N |  | N | N |
| D23 UX/soporte CRM | A |  |  | N | A | A |  | A | A |
| D24 Ciberseguridad | A |  | A | A | A | A | A | A | N |
| D25 Formación | A | A | A | A | N | A | A | A | A |
| D29 Personas clave | N | A | A | N | N | N | N | N | N |

**Leyenda:** N = núcleo; A = adyacente. Una celda adyacente no autoriza ampliar el alcance sin nueva validación.

## Procesos y herramientas críticas para el MVP

| Elemento | Papel |
|---|---|
| P05 Entrada, reparto y cualificación | Punto de inicio del MVP |
| P06 Agenda, visita y feedback | Evidencia de progresión |
| P07 Oferta y negociación | Límite inicial; no automatizar decisión |
| H01 CRM | Sistema de registro acordado |
| H02 Portales | Canal de entrada, sujeto a acceso |
| H03 WhatsApp/omnicanal | Dependencia crítica; alcance regulado y corporativo |
| H04 Email/VoIP/calendario | Señales y siguiente acción |
| H14 iPaaS/automatización | Orquestación y logs |
| H13 BI/calidad | Métricas y excepciones |

## Vacíos deliberadamente no cubiertos en el MVP

- captación de propietarios D01 y valoración D03;
- KYC/PBC D14 como decisión;
- financiación/FEIN/notaría D17;
- pagos, custodia y liquidación;
- operación completa de alquiler D18;
- ciberseguridad integral D24;
- IA autónoma;
- reemplazo de CRM o portal.

Estas exclusiones reducen riesgo y evitan presentar como producto lo que la evidencia solo identifica como oportunidad.
