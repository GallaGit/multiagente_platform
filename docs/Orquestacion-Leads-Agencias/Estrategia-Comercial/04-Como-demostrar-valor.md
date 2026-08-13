# 04 — Cómo demostrar valor

## Regla

Una demo enseña capacidad. Una prueba de valor demuestra un cambio relevante para una cuenta.

La secuencia es:

`caso reciente → baseline → mecanismo → prueba pequeña → resultado → decisión`

No atribuir ventas, ingresos o ahorro al producto si la medición no permite separar otros factores.

## Escalera de evidencia

| Nivel | Evidencia | Compromiso del cliente |
|---:|---|---|
| 1 | Caso reciente documentado | Tiempo y relato |
| 2 | Mapa del flujo actual | Usuario y owner participan |
| 3 | Baseline reproducible | Datos minimizados |
| 4 | Prototipo/prueba técnica | Feedback y acceso controlado |
| 5 | Piloto pagado | Presupuesto, responsable y contrato |
| 6 | Resultado antes/después | Revisión del aprobador |
| 7 | Renovación o expansión | Uso repetido y valor sostenido |

Elogios, clics y asistencia a una demo no sustituyen los niveles 3–7.

## Elegir la métrica

### O01 — Trazabilidad

- porcentaje de leads con owner;
- porcentaje con estado y siguiente acción;
- tiempo desde entrada hasta asignación;
- conversaciones que quedan fuera del registro;
- handoffs sin contexto completo.

### O02 — Reintroducción

- minutos semanales de copia y reconciliación;
- campos introducidos más de una vez;
- registros duplicados o inconsistentes;
- expedientes afectados;
- correcciones por semana.

### Obra nueva

- expedientes completos a fecha objetivo;
- tickets con owner y SLA;
- tiempo de resolución;
- reaperturas;
- consultas repetidas por falta de estado.

Elegir una métrica principal y dos guardrails. No usar “más ventas” como primera métrica si el ciclo, la demanda y la atribución impiden demostrar causalidad.

## Construir el baseline

1. Definir evento inicial y final.
2. Definir numerador, denominador y periodo.
3. Tomar una muestra de registros, no solo recuerdos.
4. Documentar herramientas y trabajo manual.
5. Separar datos faltantes de valor cero.
6. Registrar estacionalidad, cambios de equipo y campañas.
7. Obtener aceptación del owner.

Ejemplo:

> Durante 10 días laborables, medir todos los leads de dos canales desde recepción hasta primera acción registrada. Baseline: proporción con owner y siguiente acción dentro de 24 horas. Guardrails: errores de asignación y minutos de revisión del responsable.

Es un diseño de ejemplo, no un benchmark.

## Diagnóstico de una página

Debe mostrar:

- flujo actual;
- evidencia observada;
- punto de pérdida o repetición;
- coste proxy y supuestos;
- alternativa actual;
- dato que falta;
- prueba mínima;
- riesgo y criterio de parada.

No usar un “informe gratuito” como táctica ilimitada. Limitarlo a un flujo y reservar el trabajo de implantación para un piloto pagado.

## Demo con caso del cliente

### Agenda de 30 minutos

| Minutos | Acción |
|---:|---|
| 0–5 | Reconfirmar problema y criterio |
| 5–10 | Mostrar el flujo actual acordado |
| 10–20 | Ejecutar un caso representativo |
| 20–25 | Probar excepción, permisos y reversión |
| 25–30 | Medir ajuste y acordar siguiente prueba |

### Debe enseñar

- entrada, transformación y salida;
- qué queda en CRM/PMS;
- permisos y trazabilidad;
- intervención humana;
- error y recuperación;
- exportación y reversibilidad;
- límite conocido.

No ocultar pasos manuales de un concierge ni presentar mockups como integración terminada.

## Business case

### Valor operativo

`Horas evitables × coste horario cargado`

### Error evitable

`Casos afectados × coste medio verificable × reducción atribuible`

### Valor total conservador

`beneficio operativo + error evitado − coste de cambio − coste recurrente`

### ROI

`(beneficio atribuible − coste total) / coste total`

### Payback

`coste inicial / beneficio neto mensual`

Construir escenarios pesimista, base y optimista. Si un supuesto no tiene evidencia, mostrarlo como variable. No monetizar riesgo legal o reputacional sin método acordado.

## Diseño del piloto

| Elemento | Decisión obligatoria |
|---|---|
| Flujo | Uno |
| Equipo | Un owner y grupo acotado |
| Duración | Ventana suficiente para observar casos |
| Datos | Minimizados, anonimizados cuando sea posible |
| Baseline | Aprobado antes de intervenir |
| Métrica | Una principal |
| Guardrails | Calidad, seguridad, carga o adopción |
| Integración | La mínima viable |
| Soporte | Horario, canal y responsable |
| Éxito | Umbral acordado por la cuenta |
| Parada | Riesgo o resultado que detiene |
| Precio | Fijo por alcance |
| Revisión | Fecha con aprobador |

El umbral no debe ser universal. Una reducción del 30 % puede servir como ejemplo para negociar, pero solo el baseline y el coste de la cuenta justifican el objetivo.

## Confianza y seguridad

Antes del piloto:

- diagrama de datos;
- roles responsable/encargado;
- DPA cuando corresponda;
- subencargados y transferencias;
- permisos de mínimo privilegio;
- registro y retención;
- borrado y exportación;
- plan de reversión;
- gestión de incidentes;
- supervisión de salidas de IA.

La seguridad no se deja para procurement; forma parte de la demostración.

## Caso de éxito defendible

Solo publicar con permiso y método:

1. contexto e ICP;
2. proceso y baseline;
3. intervención y duración;
4. resultado y distribución;
5. guardrails;
6. limitaciones y cambios externos;
7. coste y tiempo de implantación;
8. cita aprobada.

Anonimizar no basta si la cuenta puede reidentificarse por contexto.

## Criterio de avance

Avanzar a propuesta si:

- el problema aparece en registros;
- el owner acepta la línea base;
- existe una intervención aislable;
- el coste potencial justifica probar;
- el aprobador revisará el resultado;
- los requisitos legales y técnicos son viables.

Detener si el CRM actual ya resuelve el caso, los registros contradicen el relato, no se puede medir, el acceso es desproporcionado o no existe owner.
