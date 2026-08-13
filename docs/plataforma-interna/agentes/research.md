# Research Agent — cuentas ICP

Agente de **plataforma interna** (capa comercial). No es el producto que se vende al cliente.

## Qué hace

Dadas una o más ciudades, busca resultados **públicos** y lista agencias donde haya **oportunidad de optimizar o automatizar procesos** (canales sueltos, CRM, leads, equipo, fricción). No basta con “ser inmobiliaria”. Un humano aprueba cada contacto.

## Qué no hace

- Enviar email, WhatsApp, SMS o LinkedIn.
- Inventar agencias si la búsqueda no devuelve fuentes.
- Sustituir el Sprint de Leads ni Witei.

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

Solo datos profesionales públicos. Canal de contacto y envío: decisión humana. Ver [Prospección en España](../../Orquestacion-Leads-Agencias/Estrategia-Comercial/Cumplimiento/Prospeccion-en-Espana.md).
