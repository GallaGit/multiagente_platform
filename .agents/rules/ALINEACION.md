# Protocolo de alineación

Filtro **estricto con debate**. El agente no acepta ni implementa a ciegas peticiones que se salgan del problema activo.

Leer primero: [PROBLEMA.md](PROBLEMA.md).

## Prioridad

1. **Producto externo** — Sprint de Orquestación de Leads (+ diagnóstico) hasta trabajo repetible / piloto.
2. **Plataforma interna** — secundaria; solo lo que desbloquea entrega o venta del sprint.
3. No construir “multiagente genérico”, memoria, LangGraph, ni roles de empresa completos por defecto.

## Clasificación de peticiones

Antes de implementar o ampliar alcance, clasificar la petición:

| Clase | Criterio | Acción |
|-------|----------|--------|
| `alineada` | Reduce leads perdidos o mejora trazabilidad del sprint (registro → owner → SLA → siguiente acción → excepción → métrica) | Proceder |
| `parcial` | Útil pero no es el núcleo (p. ej. polish de UI, refactor, research genérico) | Debatir; no implementar hasta OK explícito |
| `desviada` | Plataforma, agentes, memoria, nuevas fases, features no ligadas al dolor | Debatir alternativa alineada; no implementar hasta OK explícito (“hazlo igual” cuenta) |

### Pregunta de filtro

> ¿Esto mejora *registro → owner → SLA → siguiente acción → excepción → métrica* del Sprint de Leads?  
> Si no → `parcial` o `desviada`.

## Plantilla de debate (parcial / desviada)

Responder de forma breve con:

1. **Clasificación:** `parcial` o `desviada`.
2. **Por qué se desvía** del problema activo (1–2 frases).
3. **Alternativa más conveniente** alineada al sprint o al discovery comercial.
4. **Qué haría falta** para aceptarla igual (p. ej. “OK, hazlo igual”, métrica, decisión de piloto).
5. **No implementar** hasta confirmación explícita.

Ejemplo:

> Clasificación: `desviada`.  
> Pediste completar las fases 2–6 de la plataforma interna; eso no reduce leads perdidos ni cierra el sprint.  
> Alternativa: cerrar 3 casos HubSpot / métricas del panel de leads / discovery ICP.  
> ¿Confirmas la plataforma igual, o priorizamos el sprint?

## Ejemplos rápidos

| Petición | Clase |
|----------|-------|
| Mejorar dedupe, SLA, excepciones, webhook de leads | `alineada` |
| Panel leads + KPIs de baseline | `alineada` |
| Prueba HubSpot lab (3 casos demo) / discovery comercial | `alineada` |
| README / docs que refuerzan el problema | `alineada` |
| Realinear FE/BE del módulo delivery solo para un entregable del sprint | `parcial` → debatir alcance |
| Fases 2–6 roadmap, memoria, LangGraph, más agentes | `desviada` |
| Chat multiagente genérico como producto | `desviada` |

## Confirmación explícita

Valen: “adelante”, “hazlo igual”, “implementa la desviación”, “OK con parcial”.  
No valen: silencio, “mira opciones”, o reformular sin autorizar ejecución.
