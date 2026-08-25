# 08 — Prueba técnica Witei + canal

> **Nota:** referencia de **mercado / entrega a cliente** (agencias ICP-01 en España). **No es el camino activo de este repo.**  
> Lab dev activo: [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md).

**Fecha:** 12-08-2026  
**Tipo:** prueba de escritorio sobre documentación oficial (sin cuenta API habilitada ni sandbox propio).  
**Objetivo:** cerrar el checklist de [04-integraciones.md](04-integraciones.md) con evidencia pública y decisión go/no-go.

## Fuentes

| Fuente | URL | Uso |
|---|---|---|
| API / API Clientes | https://faq.witei.com/es/articles/2038460-api | Auth, disponibilidad, límites |
| Webhooks | https://faq.witei.com/es/articles/134658-como-puedo-usar-los-webhooks | Eventos salientes |
| Smart Inbox | https://faq.witei.com/es/articles/113854-smart-inbox-registro-automatico-en-tu-crm-de-contactos-recibidos-via-email | Ingesta de leads |
| Zapier | https://faq.witei.com/es/articles/1502139-zapier | Camino iPaaS oficial documentado |

**Confianza:** alta sobre lo publicado por Witei; baja sobre endpoints internos de “API Clientes” (docs técnicas solo tras habilitación en cuenta).

## Resumen ejecutivo

| Capacidad MVP | Resultado | Implicación |
|---|---|---|
| Auth REST inmediata | **No** (solicitud 2–3 semanas; experimental) | No construir el piloto sobre API pública abierta |
| Crear contacto desde canal | **Sí** vía **Smart Inbox** (email con formato) | Camino principal del MVP |
| Asignar responsable | **Parcial** — reglas nativas Smart Inbox | Cubrir SLA/reasignación con proceso + alertas, no solo API |
| Tarea / siguiente acción | **Parcial** — crea “Solicitud de Contacto” si ya existe ficha | Validar en cuenta piloto el resto de tareas |
| Listar / filtrar leads | **No verificado** sin API | Panel = vistas CRM nativas o export |
| Webhook eventos | **Sí, pero saliente de inmuebles** | No sirve para ingresar leads |
| Export / salida | **Sí** (XML / exportación documentada en ecosistema Witei) | Portabilidad OK a nivel producto |

**Decisión:** **GO condicionado** — implantar con **canal → Smart Inbox → reglas nativas Witei (+ iPaaS que genere el email)**. **NO GO** a prometer integración REST bidireccional en el primer piloto sin API Clientes habilitada.

---

## Checklist Witei (resultado)

### Auth (token/OAuth)

| Estado | Hallazgo |
|---|---|
| Parcial / bloqueado para MVP inmediato | No hay API pública de uso inmediato. “API Clientes” requiere solicitud a Witei (objetivo, volumen, IPs, frecuencia); validación **2–3 semanas**. Tras aprobación: usuario no-admin con permiso “Acceso API”, token en Configuración > Integraciones > API. Documentación de endpoints **solo dentro de la cuenta**. API marcada como **experimental**; Witei **no recomienda producción crítica**. |

### Crear lead/contacto con origen

| Estado | Hallazgo |
|---|---|
| Cumple vía Smart Inbox | Bandeja `*@inbox.witei.com`. Extrae nombre, email, teléfono, referencia inmueble, comentario. Crea contacto o, si existe, tarea “Solicitud de Contacto”. Orígenes tipicos: notificaciones de portales o email con formato fijo desde web/Zapier. |

### Asignar responsable

| Estado | Hallazgo |
|---|---|
| Parcial (nativo) | Orden documentado: (1) si contacto existe → comercial actual; (2) usuario Coordinador; (3) responsable del inmueble si hay referencia; (4) Delegado; (5) admin más antiguo. **No** hay API pública verificada para forzar round-robin custom sin API Clientes. |

### Crear tarea / siguiente acción + fecha

| Estado | Hallazgo |
|---|---|
| Parcial | Alta nueva → ficha; contacto existente → tarea “Solicitud de Contacto”. SLA y “siguiente acción” genérica del brief requieren configuración CRM + disciplina o API Clientes (pendiente cuenta). |

### Leer/listar leads filtrados

| Estado | Hallazgo |
|---|---|
| No verificado por API | Sin docs públicas de listados REST. MVP: vistas/filtros Witei + export. API Clientes podría cubrirlo tras habilitación (**pendiente prueba en cuenta**). |

### Webhook o polling de eventos nuevos

| Estado | Hallazgo |
|---|---|
| Webhook ≠ ingest de leads | Webhooks Witei: POST JSON al crear/modificar **inmueble**; timeout 15 s; 2 reintentos; ventana ~5 min; fallo 4xx/5xx desactiva webhook. Útil para sync saliente de inventario, **no** para alta de demanda. Polling REST: no documentado públicamente. |

### Rate limits / campos obligatorios del plan

| Estado | Hallazgo |
|---|---|
| Parcial | Smart Inbox cuenta para límite de contactos del plan CRM. API experimental: volumen debe acordarse en la solicitud. Campos mínimos Smart Inbox: **email o teléfono**; nombre opcional (“Desconocido”); referencia case-sensitive para cruzar inmueble. |

### Exportación / portabilidad

| Estado | Hallazgo |
|---|---|
| Cumple (producto) | Alternativas oficiales: XML, exportación de datos, migración documentada. Suficiente para criterio de salida del servicio. |

---

## Checklist canal (resultado)

Elección de referencia del brief: **Opción A (portal → email Smart Inbox)** o **Opción B (web → email formato Smart Inbox)**. Ambas convergen en el mismo mecanismo.

| Ítem | Estado | Notas |
|---|---|---|
| Payload de ejemplo | Cumple (especificación oficial) | Ver sección siguiente |
| Campos nombre, contacto, ref, timestamp | Parcial | Timestamp lo aporta el email/headers; cuerpo define Mensaje/Nombre/Teléfono/Email/Referencia |
| `origen_ref` estable | Parcial | Usar `Referencia` del inmueble; debe coincidir exacta con Witei |
| Latencia / duplicados | Documentado | Dedupe por email o teléfono entre mails sucesivos; sin evidencia → ficha nueva |
| Consentimiento | Fuera de auto-respuesta MVP | Respuesta automática Smart Inbox existe (plan Normal+); el MVP del sprint **no** la exige |

### Payload de ejemplo (web → Smart Inbox)

Formato oficial para web externa / Zapier → dirección Smart Inbox:

```text
Mensaje: Interesado en visitar esta semana
Nombre: Ana Ejemplo
Teléfono: 612345678
Email: ana.ejemplo@example.com
Referencia: REF-001
```

**Prueba en piloto (cuenta real):**

1. Activar Smart Inbox y copiar `*@inbox.witei.com`.
2. Enviar el email de prueba con el formato anterior.
3. Verificar ficha + asignación según reglas.
4. Reenviar mismo email/teléfono → debe fusionar / crear tarea, no segundo dueño absurdo.
5. Enviar sin email ni teléfono → no debe crear contacto usable (control negativo).

### Opción portal

Configurar notificaciones del portal hacia la dirección Smart Inbox (o reenvío). Revisar “Ver correos recibidos” si falla el parseo. Limitación: un perfil de portal → una Smart Inbox (no multi-espacio con el mismo perfil).

---

## Arquitectura revisada del MVP (post-prueba)

```text
Portal o formulario web
        ↓
Email (formato Smart Inbox)  ← n8n/Make/Zapier puede generar/reenviar
        ↓
Witei Smart Inbox
        ↓
Contacto + asignación nativa + tarea solicitud
        ↓
Reglas operativas del sprint (SLA, cola) sobre vistas CRM
        + alertas humanas (email/Slack) si iPaaS monitorea copia del correo
```

**API Clientes** = mejora futura (listados, tareas custom, automatización dura), no dependencia del primer piloto.

---

## Go / no-go

| Escenario | Decisión |
|---|---|
| Piloto con Witei sin API Clientes aún | **GO** vía Smart Inbox + reglas nativas |
| Cliente exige REST inmediato sin espera 2–3 semanas | **NO GO** / reformular expectativas o CRM alternativo |
| Solo se puede trabajar con export manual semanal | **NO GO** al sync continuo; oferta semi-manual distinta |
| API Clientes habilitada en cuenta piloto | Reabrir checklist REST (crear, asignar, listar) en esta misma ficha |

## Pendiente en cuenta real (siguiente micro-paso)

- [ ] Cuenta Witei de prueba (freemium vale para Smart Inbox).
- [ ] Enviar 3 emails de prueba (nuevo, duplicado, datos insuficientes).
- [ ] Anotar captura de asignación real vs reglas documentadas.
- [ ] Solicitar API Clientes solo si el piloto lo necesita (métricas automatizadas / tareas custom).
- [ ] Si el cliente usa Inmovilla: repetir ficha equivalente (otro doc).

## Impacto en el brief

- [01-alcance.md](01-alcance.md): implantación prioriza Smart Inbox; iPaaS = generador/reenviador de email, no conector REST mágico.
- [05-reglas.md](05-reglas.md): el reparto custom puede chocar con el orden nativo Witei — diseñar reglas **compatibles** o capa de alerta post-asignación.
- [07-criterios-hecho.md](07-criterios-hecho.md): “integración API” se interpreta como **ingesta fiable Smart Inbox** hasta tener API Clientes.
