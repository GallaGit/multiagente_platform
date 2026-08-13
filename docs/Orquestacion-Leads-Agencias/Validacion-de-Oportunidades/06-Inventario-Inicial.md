# Inventario inicial de oportunidades

**Estado:** candidatas por validar; no constituyen productos definidos ni prioridades aprobadas.  
**Origen principal:** [hipótesis de oportunidades del ecosistema tecnológico](../ecosistema_tecnologico/07_analisis_transversal/hipotesis-de-oportunidades.md).

## Regla de uso

Este inventario evita perder trazabilidad entre investigación y validación. No asigna puntuaciones porque los documentos anteriores contienen evidencia de mercado y vacíos, pero todavía no aportan de forma homogénea:

- entrevistas recientes por segmento;
- líneas base operativas;
- disposición efectiva a pagar;
- pruebas técnicas sobre sistemas reales;
- coste de implantación y soporte;
- resultados de pilotos comparables.

Asignar 4 o 5 sin esos datos generaría una precisión falsa.

## Candidatas

| ID | Área de oportunidad | Segmento inicial por contrastar | Dolor relacionado | Incertidumbre decisiva |
|---|---|---|---|---|
| O01 | Trazabilidad entre lead, conversación y resultado | Agencias residenciales de 3–20 agentes con WhatsApp y CRM | Conversaciones fuera del registro, seguimiento discontinuo y pérdida de contexto | Magnitud atribuible de la pérdida y acceso estable a canales/CRM |
| O02 | Reducción de reescritura manual multisistema | Micro y pequeñas agencias con portal, CRM, documentos y facturación separados | Duplicidad, errores y tiempo administrativo | Horas evitables reales y variación entre stacks |
| O03 | Consistencia de inventario y leads multiportal | Agencias con publicación simultánea en varios portales | Estados, precios, disponibilidad y origen divergentes | Frecuencia del desajuste y límites de integración de cada portal |
| O04 | Cierre documental y cumplimiento pre-notarial | Agencias medianas, redes y operadores con alto volumen | Expedientes incompletos, KYC/PBC, firma y versiones dispersas | Comprador, responsabilidad legal y disposición a sustituir procesos |
| O05 | Liquidación, factura, cobro y reparto alineados a la operación | Franquicias, redes y agencias multiagente | Reintroducción, Excel paralelo, errores de reparto y cobro tardío | Frecuencia económica del error y diversidad de reglas contables |
| O06 | Analítica e IA de proceso para el segmento medio | Agencias con CRM y portales pero sin BI integrado | Reporting tardío, baja trazabilidad y decisiones manuales | Decisiones que cambiarían y valor incremental frente a BI genérico |
| O07 | Portabilidad y reducción de lock-in | Agencias que migran de CRM, red o portal-tools | Exportación incompleta, pérdida de histórico y alto coste de cambio | Frecuencia de compra: necesidad puntual frente a servicio recurrente |
| O08 | Identidad, dispositivo y continuidad del agente | Agencias con uso de móviles o números personales | Accesos, datos y relaciones ligados a personas clave | Urgencia, incidencia observada y fricción de adopción |

## Vínculos con dolores documentados

| Oportunidad | Problemas del Módulo 04 que debe contrastar |
|---|---|
| O01 | [P02](../Modulo-04-Dolor-del-Cliente/Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md), [P07](../Modulo-04-Dolor-del-Cliente/Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P08](../Modulo-04-Dolor-del-Cliente/Problemas/08-comunicacion-irregular-y-poca-visibilidad.md), [P20](../Modulo-04-Dolor-del-Cliente/Problemas/20-automatizacion-parcial-del-flujo-comercial.md) |
| O02 | [P13](../Modulo-04-Dolor-del-Cliente/Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md), [P19](../Modulo-04-Dolor-del-Cliente/Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P20](../Modulo-04-Dolor-del-Cliente/Problemas/20-automatizacion-parcial-del-flujo-comercial.md) |
| O03 | [P06](../Modulo-04-Dolor-del-Cliente/Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md), [P05](../Modulo-04-Dolor-del-Cliente/Problemas/05-dependencia-de-los-grandes-portales.md), [P22](../Modulo-04-Dolor-del-Cliente/Problemas/22-desincronizacion-en-multipublicacion-y-portales.md) |
| O04 | [P13](../Modulo-04-Dolor-del-Cliente/Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md), [P14](../Modulo-04-Dolor-del-Cliente/Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md), [P15](../Modulo-04-Dolor-del-Cliente/Problemas/15-proteccion-de-datos-en-canales-dispersos.md), [P16](../Modulo-04-Dolor-del-Cliente/Problemas/16-arras-reservas-y-firmas-mal-definidas.md) |
| O05 | [P21](../Modulo-04-Dolor-del-Cliente/Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md), [P27](../Modulo-04-Dolor-del-Cliente/Problemas/27-rentabilidad-volatil-e-ingresos-contingentes.md) |
| O06 | [P21](../Modulo-04-Dolor-del-Cliente/Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md), [P25](../Modulo-04-Dolor-del-Cliente/Problemas/25-brecha-de-formacion-profesional-y-digital.md) |
| O07 | [P05](../Modulo-04-Dolor-del-Cliente/Problemas/05-dependencia-de-los-grandes-portales.md), [P19](../Modulo-04-Dolor-del-Cliente/Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P23](../Modulo-04-Dolor-del-Cliente/Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md) |
| O08 | [P15](../Modulo-04-Dolor-del-Cliente/Problemas/15-proteccion-de-datos-en-canales-dispersos.md), [P24](../Modulo-04-Dolor-del-Cliente/Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md), [P29](../Modulo-04-Dolor-del-Cliente/Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md) |

## Cola inicial de validación

El orden siguiente responde a **reducción de incertidumbre**, no a atractivo final:

1. entrevistar sobre O01 y O02 en la misma muestra, observando el recorrido portal–WhatsApp–CRM;
2. auditar una muestra pequeña de registros para cuantificar reintroducción y pérdida de trazabilidad;
3. ejecutar pruebas técnicas de acceso antes de prometer integración;
4. contrastar O04 con responsables de cumplimiento y expedientes;
5. buscar evidencia de pago o presupuesto para O05–O08 antes de ampliar investigación.

## Próxima salida

Crear una ficha independiente mediante la [plantilla](03-Ficha-y-Matriz.md) para cada candidata que entre en validación. El identificador se mantiene aunque cambie el nombre o se reformule el alcance.

