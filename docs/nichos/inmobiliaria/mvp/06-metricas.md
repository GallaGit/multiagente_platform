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

## Procedimiento lab (HubSpot)

En el laboratorio de este repo, las métricas del panel usan por defecto **solo leads MVP** (`lead_origen` poblado por el orquestador). Contactos HubSpot legacy se excluyen salvo activar “Incluir todos los contactos HubSpot”.

### Capturar baseline → operar → comparar

1. **Día 0** — Con API y panel en marcha, capturar baseline:
   - Panel: botón **Capturar baseline**, o
   - API: `POST /leads/baseline` con body opcional `{"note":"Lab día 0","mvp_only":true}`
2. **Operar 1–2 semanas** — Ingesta simulada, resolución de excepciones, registrar `primera_respuesta_at` cuando aplique (botón **Marcar 1ª respuesta** en la tabla del panel o `PATCH /leads/{id}`).
3. **Comparar** — Panel muestra delta vs baseline en cada KPI; API: `GET /leads/metrics?mvp_only=true` devuelve `{ current, baseline, delta }`.
4. **Archivo local** — Snapshot en `data/baseline.json` (gitignored). Plantilla: `data/baseline.example.json`.

### Campos API relevantes

| Endpoint | Uso |
|---|---|
| `GET /leads/metrics?mvp_only=true` | Métricas actuales + delta vs baseline |
| `POST /leads/baseline` | Guardar snapshot |
| `GET /leads/baseline` | Leer snapshot (404 si no existe) |

### Mediana 1ª respuesta

- Campo `mediana_tiempo_respuesta_min` en métricas.
- Calculada solo si hay **≥2** leads con `created_at` y `primera_respuesta_at`.
- En piloto cliente, depende de que el equipo registre el primer contacto en CRM.

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

## Enlaces

- [Prueba técnica HubSpot](08-prueba-tecnica-hubspot.md)
- [Readiness producción](../../../READINESS.md)
- [Checklist piloto](../operacion/CHECKLIST-piloto-pagado.md)
