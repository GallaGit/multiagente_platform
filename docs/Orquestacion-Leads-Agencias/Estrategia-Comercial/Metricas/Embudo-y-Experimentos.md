# Embudo, métricas y experimentos

## Propósito

Medir aprendizaje y avance real. No existen benchmarks internos: todas las tasas comienzan como `NP` y se calculan con datos observados.

## Etapas del embudo

| Etapa | Definición de entrada | Salida obligatoria |
|---|---|---|
| Cuenta | Empresa identificada | ICP, señal y fuente |
| Priorizada | Score suficiente | Rol y canal evaluado |
| Conversación | Interacción bilateral | Encaje o descalificación |
| Discovery | Caso reciente revisado | Problema y siguiente evidencia |
| Cualificada | Puertas comerciales mínimas | Plan de cuantificación |
| Baseline | Métrica reproducible | Aceptación del owner |
| Prueba | Intervención evaluada | Resultado técnico/operativo |
| Propuesta | Alcance y precio presentados | Decisión y plan mutuo |
| Piloto | Acuerdo pagado/firmado | Inicio y revisión |
| Ganada | Contrato de continuidad | Onboarding |
| Perdida | Decisión negativa | Razón y evidencia |

No saltar de “conversación” a “propuesta” porque alguien pidió precio.

## Campos CRM

### Cuenta

- identificador y razón social;
- ICP y subsegmento;
- zona y oficinas;
- tamaño observado o `NP`;
- stack y fuentes;
- señal con fecha;
- score de prioridad;
- owner/champion/aprobador/firmante;
- datos y condición de contacto;
- oposición/supresión.

### Oportunidad

- problema y último caso;
- métrica/base;
- alternativa;
- evento de compra;
- presupuesto;
- integración;
- etapa y fecha de entrada;
- próxima acción, dueño y fecha;
- importe;
- fecha esperada;
- confianza basada en evidencia;
- razón de pérdida.

## Métricas del canal

| Métrica | Fórmula |
|---|---|
| Acceso a rol | conversaciones con rol correcto / cuentas contactadas |
| Entrevista | discoveries realizados / conversaciones |
| Evidencia | discoveries con caso concreto / discoveries |
| Baseline | cuentas con baseline / discoveries con evidencia |
| Propuesta | propuestas / cuentas cualificadas |
| Piloto | pilotos pagados / propuestas |
| Ciclo | fecha de firma − primera conversación |
| Coste por discovery | coste de canal / discoveries |
| Coste de adquisición | coste comercial total / clientes ganados |

No comparar canales con pocos casos como si fueran estadísticamente estables.

## Métricas de calidad

- porcentaje de cuentas con fuente y señal;
- porcentaje con rol correcto;
- porcentaje de registros completados el mismo día;
- oportunidades sin próxima acción;
- días por etapa;
- oportunidades estancadas;
- propuestas sin aprobador;
- oposiciones ejecutadas en plazo interno;
- datos vencidos o sin base revisada.

## Métricas económicas

| Métrica | Cálculo |
|---|---|
| ACV | valor anual contratado |
| Ingreso piloto | precio pagado del piloto |
| Margen piloto | ingreso − coste variable de entrega |
| Horas onboarding | suma de horas reales |
| Payback CAC | CAC / margen mensual |
| Expansión | ingreso adicional en cuenta |
| Retención | cuentas/ingreso renovado |

No usar ACV proyectado de una continuidad no firmada.

## Forecast por evidencia

En fase inicial, usar categorías, no porcentajes inventados:

| Categoría | Evidencia |
|---|---|
| Exploración | Conversación o discovery |
| Posible | Problema + owner + próximo paso |
| Cualificada | Baseline + aprobador + viabilidad |
| Propuesta activa | Precio revisado + plan mutuo |
| Compromiso | Contrato en revisión final y fecha |
| Cerrada | Firma y condición de pago |

El forecast financiero solo incluye contratos firmados o una ponderación calibrada con historial suficiente.

## Experimentos

### Ficha

| Campo | Registro |
|---|---|
| ID y fecha |  |
| Hipótesis |  |
| ICP |  |
| Variable que cambia |  |
| Grupo/comparación |  |
| Señal primaria |  |
| Guardrail |  |
| Duración/muestra |  |
| Resultado |  |
| Limitación |  |
| Decisión |  |

### Reglas

1. Cambiar una variable principal.
2. Definir señal antes de ejecutar.
3. Medir casos concretos, no aperturas como objetivo final.
4. No reutilizar una muestra hasta agotarla con cadencias.
5. Respetar canal, permiso y oposición.
6. Registrar resultados negativos.
7. No generalizar desde una cuenta.

## Revisión semanal

Responder:

1. ¿Qué etapa perdió más cuentas y por qué?
2. ¿Qué ICP aportó casos más concretos?
3. ¿Qué canal llegó al owner con menor coste?
4. ¿Qué objeción revela falta de valor?
5. ¿Qué oportunidad no tiene próximo paso?
6. ¿Qué dato contradice la tesis?
7. ¿Qué se dejará de hacer?

## Revisión tras 30 oportunidades

- comparar score inicial con discovery, baseline, propuesta y cierre;
- recalibrar pesos del ICP;
- medir ciclo por etapa;
- separar razones de pérdida controlables;
- estimar primer CAC;
- comparar precio con coste de entrega;
- decidir si existe repetibilidad.

Treinta oportunidades siguen siendo una muestra pequeña, pero permiten reemplazar parte de los supuestos por observación.

## Dashboard mínimo

Mostrar:

- cuentas por ICP y etapa;
- entradas/salidas semanales;
- días medianos por etapa;
- baselines, pruebas, propuestas y pilotos;
- importe firmado y cobrado;
- razones de pérdida;
- coste y horas;
- experimentos activos;
- incidencias de cumplimiento.

Evitar un dashboard con impresiones, seguidores y aperturas sin conexión con conversaciones o evidencia.
