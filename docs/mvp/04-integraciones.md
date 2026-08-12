# 04 — Integraciones

Stack de referencia: **Witei** + **1 canal** + **n8n o Make**.  
No se inventan endpoints: lo no verificado en prueba queda marcado.

## Arquitectura de implantación

```text
Canal (portal email/webhook | form web)
        ↓
n8n / Make  (normalizar, dedupe ligera, reintentos)
        ↓
Witei (alta/update, dueño, tarea/nota, estados)
        ↓
Alertas (email/Slack/CRM) ← excepciones
```

Código propio (FastAPI u otro) solo si iPaaS no cubre auth, transformaciones o límites.

## CRM — Witei (referencia)

| Tema | Estado |
|---|---|
| Rol | Sistema de registro del lead en el MVP |
| Mecanismos esperados | API y/o automatizaciones nativas / webhooks — **pendiente de prueba técnica** por plan y permisos |
| Necesidades del sprint | Crear/actualizar contacto-demanda; asignar usuario; registrar nota/tarea/siguiente acción; filtrar por estado/origen |
| Riesgos | Campos custom limitados; rate limits; planes freemium vs pago; export/lock-in |

### Checklist de prueba técnica (Witei)

- [ ] Auth (token/OAuth) documentada y usable en sandbox o cuenta piloto
- [ ] Crear lead/contacto con origen y datos mínimos
- [ ] Asignar responsable
- [ ] Crear tarea o equivalente a siguiente acción + fecha
- [ ] Leer/listar leads filtrados (para panel/métricas)
- [ ] Webhook o polling viable para eventos nuevos
- [ ] Límites de rate y campos obligatorios del plan del cliente
- [ ] Exportación / salida documentada (portabilidad)

## Canal — uno solo

Elegir **una** opción por piloto:

| Opción | Entrada típica | Notas |
|---|---|---|
| A — Portal | Email parseado o webhook del portal/tools | Formato email varía; parsers frágiles |
| B — Web | Formulario → webhook iPaaS | Más controlable; volumen puede ser bajo |

WhatsApp personal: **fuera**. WhatsApp Business API: fuera del primer brief (permisos, coste, consentimiento).

### Checklist de prueba técnica (canal)

- [ ] Payload de ejemplo real (anonimizado)
- [ ] Campos: nombre, contacto, ref inmueble, timestamp
- [ ] Identificador estable de origen (`origen_ref`)
- [ ] Latencia y duplicados del canal
- [ ] Consentimiento / base legal si se automatiza respuesta (MVP no envía mensajes autónomos)

## Variante Inmovilla

Mismo flujo lógico ([02-flujo.md](02-flujo.md)) y modelo ([03-modelo-datos.md](03-modelo-datos.md)).  
Sustituye la ficha Witei por checklist equivalente sobre API/conectores Inmovilla. No mezclar ambos CRM en el mismo piloto MVP.

## Límites conocidos (mercado)

- APIs de CRM verticales españoles: cobertura desigual ([ecosistema CRM](../Orquestacion-Leads-Agencias/ecosistema_tecnologico/02_sistemas_core/crm-inmobiliarios.md)).
- Portales: sync y calidad variables; bi-dirección no asumida.
- Fallos silenciosos y duplicados son el riesgo técnico medio del servicio.

## Decisión de go/no-go técnico

| Resultado prueba | Decisión |
|---|---|
| Alta + asignación + tarea posibles | Seguir con iPaaS |
| Solo export/import manual | Reformular a semi-manual + reglas CRM; no prometer sync |
| Sin permisos API | Pausar piloto técnico; volver a discovery |
