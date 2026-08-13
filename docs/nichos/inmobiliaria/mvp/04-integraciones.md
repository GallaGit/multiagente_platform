# 04 — Integraciones

Stack de referencia: **Witei** + **1 canal** + **Smart Inbox** (email) + **n8n/Make/Zapier** como generador/reenviador.  
Prueba técnica de escritorio: [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md) (2026-08-12).

## Arquitectura de implantación (post-prueba)

```text
Canal (portal email | form web)
        ↓
n8n / Make / Zapier  (opcional: normalizar → email formato Smart Inbox)
        ↓
Witei Smart Inbox  (*@inbox.witei.com)
        ↓
Contacto + asignación nativa + tarea "Solicitud de Contacto"
        ↓
Vistas CRM + alertas humanas (excepciones / SLA)
```

**API Clientes Witei:** no disponible de inmediato (solicitud 2–3 semanas; experimental). No es dependencia del primer piloto.  
Código propio solo si hace falta un endpoint receptor o normalizador de emails/payloads.

## CRM — Witei (referencia)

| Tema | Estado tras prueba |
|---|---|
| Rol | Sistema de registro del lead |
| Mecanismo MVP | **Smart Inbox** (email), no REST público abierto |
| API Clientes | Bajo petición; token por usuario; docs en cuenta; experimental |
| Webhooks oficiales | Salientes de **inmuebles**, no ingest de leads |
| Necesidades del sprint | Alta contacto + dueño (reglas nativas) + tarea solicitud; SLA/cola vía proceso + vistas |
| Riesgos | Parseo email frágil; límites de contactos del plan; sin listados REST verificados; API experimental |

### Checklist de prueba técnica (Witei)

- [x] Auth documentada — **sí**, pero API Clientes no inmediata (2–3 semanas + experimental)
- [x] Crear lead/contacto — **sí** vía Smart Inbox
- [x] Asignar responsable — **parcial** (reglas nativas documentadas)
- [x] Tarea / siguiente acción — **parcial** (“Solicitud de Contacto”)
- [ ] Leer/listar leads vía API — **no verificado** (usar vistas CRM)
- [x] Webhook — **sí saliente inmuebles**; **no** para alta de leads
- [x] Límites / campos mínimos — email o teléfono; Smart Inbox cuenta en cupo contactos
- [x] Exportación / salida — XML / export documentados a nivel producto
- [ ] Prueba en **cuenta real** (3 emails: nuevo, duplicado, insuficiente) — pendiente operativo

Detalle y go/no-go: [08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md).

## Canal — uno solo

| Opción | Entrada | Camino verificado |
|---|---|---|
| A — Portal | Notificación email del portal → Smart Inbox | Documentado por Witei |
| B — Web | Formulario → email con formato Smart Inbox (directo o vía iPaaS) | Formato oficial publicado |

WhatsApp personal / WA Business API: **fuera** del primer brief.

### Checklist de prueba técnica (canal)

- [x] Payload de ejemplo (especificación oficial) — ver [08](08-prueba-tecnica-witei.md)
- [x] Campos nombre, contacto, ref — en formato Smart Inbox
- [x] Identificador origen (`Referencia`) — case-sensitive vs cartera Witei
- [x] Duplicados — fusión si mismo email/teléfono; si no, ficha nueva
- [ ] Latencia medida en cuenta real — pendiente
- [x] Consentimiento — MVP no exige auto-respuesta; auto-reply es opt-in de plan

## Variante Inmovilla

Mismo flujo lógico ([02-flujo.md](02-flujo.md)). Requiere **otra** prueba técnica (API/conectores Inmovilla). No mezclar ambos CRM en el mismo piloto.

## Límites conocidos

- Sin conector oficial Make; Zapier documentado vía webhooks salientes + email a Smart Inbox.
- Webhooks de inmuebles: timeout 15 s, reintentos, ventana ~5 min, desactivación si falla el endpoint.
- No asumir sync bidireccional portal↔CRM más allá de pasarelas/Smart Inbox del cliente.

## Decisión de go/no-go técnico

| Resultado | Decisión |
|---|---|
| Smart Inbox usable en cuenta piloto | **GO** — camino MVP |
| Cliente exige REST sin espera de API Clientes | **NO GO** / reformular |
| Solo export manual semanal | Reformular oferta semi-manual |
| API Clientes habilitada y estable | Ampliar automatización (listados, tareas custom) |
