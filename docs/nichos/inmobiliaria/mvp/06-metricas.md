# 06 — Métricas

Medir **ejecución** del proceso, no inventar ROI de conversión. La oferta no promete ingresos hasta medirlos en cliente.

## Baseline (antes)

Periodo: 1–2 semanas previas o muestra acordada del mismo canal.

| Métrica | Definición | Fuente |
|---|---|---|
| Leads entrados | Conteo en el canal/CRM | Canal + CRM |
| % sin responsable | Leads sin dueño a las 24 h | CRM |
| % sin siguiente acción | Asignados sin próxima acción | CRM |
| Tiempo a 1ª respuesta | Mediana/p90 hasta primer intento registrado | CRM / agenda |
| % en excepción / abandono opaco | Sin trazabilidad de resultado corto | CRM + muestra manual |

Si el CRM no tiene el dato, se estima con muestra anotada y se documenta la limitación.

## Durante / después

Mismas métricas en el periodo del sprint (p. ej. 2–4 semanas).

| Comparación | Cómo interpretarla |
|---|---|
| Mejora de % con dueño y siguiente acción | Éxito de orquestación |
| Mejora de tiempo a 1ª respuesta | Éxito de SLA (si el registro es fiable) |
| Conversión a visita/cierre | **Observacional**; no se atribuye causalmente al sprint sin diseño de control |

## Operativas de entrega

| Métrica interna | Uso |
|---|---|
| Incidencias de sync / semana | Calidad del conector |
| Horas de soporte post-go-live | Margen del servicio |
| Excepciones abiertas > 48 h | Adopción / diseño de reglas |

## Tablero mínimo

Una vista: leads del canal, dueño, SLA, estado, excepción.  
Sin BI enterprise en el MVP.

## Anti-métricas (no usar como promesa)

- “+X% conversión” sin baseline comparable.
- “Ahorro de Y horas” sin diario de tiempos.
- Benchmarks genéricos de mercado no medidos en el cliente.
