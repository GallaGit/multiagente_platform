# `.agents/rules/` — norte del proyecto para agentes

Esta carpeta es la **fuente de verdad corta** del *por qué* de este repositorio. Existe para que humanos y agentes de Cursor no pierdan el problema que se resuelve cuando aparecen peticiones de stack, multiagente o plataforma.

## Contenido

| Archivo | Rol |
|---------|-----|
| [PROBLEMA.md](PROBLEMA.md) | Quién, dolor, promesa, métricas, fuera de alcance |
| [ALINEACION.md](ALINEACION.md) | Protocolo: clasificar peticiones y debatir desviaciones |

## Cómo usarlo

1. Antes de implementar o ampliar alcance, leer `PROBLEMA.md` y `ALINEACION.md`.
2. Aplicar el filtro de alineación (estricto con debate).
3. Si la petición se desvía, **debatir** una alternativa más conveniente; no ejecutar a ciegas.

La regla Cursor [`.cursor/rules/alineacion-proyecto.mdc`](../../.cursor/rules/alineacion-proyecto.mdc) (`alwaysApply`) obliga a este comportamiento.

## Documentación de negocio (detalle)

| Ruta | Rol |
|------|-----|
| [docs/CONTEXT.md](../../docs/CONTEXT.md) | Identidad y principios de la empresa |
| [docs/nichos/inmobiliaria/](../../docs/nichos/inmobiliaria/) | Pack del nicho activo |
| [Servicio profesional — Sprint](../../docs/nichos/inmobiliaria/Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md) | Oferta que se vende |
| [mvp/](../../docs/nichos/inmobiliaria/mvp/) | Brief técnico del sprint |
| [plataforma-interna/](../../docs/plataforma-interna/) | SO interno (secundario al producto externo) |

**Prioridad:** producto externo (Sprint de Orquestación de Leads) antes que ampliar la plataforma interna.
