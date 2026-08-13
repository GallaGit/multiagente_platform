# Research Agent — cuentas ICP

Agente de **plataforma interna** (capa comercial). No es el producto que se vende al cliente.

## Qué hace

Dadas una o más ciudades, busca resultados **públicos** y lista **cuentas del ICP del conocimiento activo** donde haya **oportunidad de optimizar o automatizar procesos** (canales sueltos, CRM, leads, equipo, fricción). No basta con “ser del sector”. Un humano aprueba cada contacto.

`research` **requiere nicho**: si el pack activo en `docs/nichos/` no tiene manifiesto válido o está `enabled: false`, el agente no entra en el orquestador y `POST /research` responde **503**. Ver [registro.md](registro.md).

## Qué no hace

- Enviar email, WhatsApp, SMS o LinkedIn.
- Inventar cuentas si la búsqueda no devuelve fuentes.
- Sustituir la oferta del nicho activo.

## Cómo usarlo

Con API (requiere `LLM_API_KEY`):

```bash
curl -s http://127.0.0.1:8000/research ^
  -H "Content-Type: application/json" ^
  -d "{\"cities\":[\"Valencia\",\"Alicante\"],\"limit\":15}"
```

O por chat: `Busca clientes ideales en Valencia y Alicante` → el Orchestrator enruta a `research`.

CLI:

```bash
python -m api.research Valencia Alicante --limit 15
```

## Cumplimiento

Solo datos profesionales públicos. Canal de contacto y envío: decisión humana. Cumplimiento del nicho activo: [Prospección en España](../../nichos/inmobiliaria/Orquestacion-Leads-Agencias/Estrategia-Comercial/Cumplimiento/Prospeccion-en-Espana.md).
