# Calendarios

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza:** media-alta en integraciones documentadas; media en adopción

---

## 1. Función principal

Coordinar **visitas a inmuebles**, captaciones, firmas, notaría y disponibilidad del equipo. Suelen convivir **Google Calendar / Outlook** con la **agenda del CRM**; el conflicto entre ambos es una fricción operativa recurrente.

---

## 2. Usuarios

| Rol | Calendario que usa |
|-----|--------------------|
| Agente | Móvil (Google/Outlook) como verdad diaria |
| CRM | Actividades de visita/llamada |
| Admin | Calendarios compartidos de oficina |
| Cliente | Links de reserva / confirmaciones WhatsApp |

---

## 3. Momento del flujo

Tras cualificación del lead → **agenda de visita** → recordatorios → feedback post-visita. También hitos: firma de encargo, arras, escritura. Pico de complejidad: multi-agente y llaves compartidas.

---

## 4. Información gestionada

Fecha/hora, duración, inmueble, asistentes (agente, comprador, propietario), dirección, estado (confirmada/cancelada), a veces resultado. Datos personales del visitante → RGPD.

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Idealista Tools ↔ Google Calendar; CRM con sync Google/Outlook |
| **API** | Google Calendar API; Microsoft Graph calendar |
| **Automatización** | Booking links → CRM; Zapier/Make |
| **Manual** | Agente apunta en móvil y no en CRM (muy frecuente) |
| **Inexistente** | Disponibilidad de llaves/propietario en un solo sistema |

---

## 6. Flujo de datos (ASCII)

```text
[Lead cualificado]
      |
      +--> [Agenda CRM: crear visita]
      |           |
      |           +--sync?--> [Google / Outlook]
      |
      +--> [Solo WhatsApp: "quedamos a las 18h"]
                  |
                  v
           [Calendario personal]
           (CRM desactualizado)
```

---

## 7. Limitaciones y tareas humanas

- Doble agenda → no-shows y solapes.
- Cancelaciones por WhatsApp no revierten el evento CRM.
- Recursos: llaves, coche, fotógrafo no modelados.
- Zonas horarias / visitas back-to-back sin buffers.
- Calendarios personales con datos de clientes al cambiar de móvil.

---

## 8. Costes

| Pieza | Coste |
|-------|-------|
| Google Calendar / Outlook Calendar | Incluidos en Workspace / M365 (ver fichas) |
| Módulo agenda CRM | Suele ir en licencia CRM |
| Bookings (Microsoft) | Incluido en varios planes M365 Business |
| Appointment schedules (Google) | Según edición Workspace |
| Herramientas tipo Calendly | SaaS propio — consultar web vendor; no asumir pack inmobiliario |

Sin precio público específico «calendario inmobiliario» aparte del CRM/suite.

---

## 9. Competencia / enfoques

| Enfoque | Cuándo aparece |
|---------|----------------|
| Solo móvil Google/Outlook | Microagencia |
| Agenda CRM como master | Medianas con disciplina |
| Sync bidireccional | Objetivo; calidad desigual |
| Enlaces de reserva web | PropTech / equipos marketing |
| WhatsApp como «calendario» | Muy extendido informalmente |

La competencia no es Calendly vs Outlook: es **disciplina de registro** vs chat.

---

## 10. Adopción

Calendario digital personal: **muy extendida**.  
Agenda CRM usada de verdad: **habitual** en medianas; **incierta/baja** en micro. Sync estable: **poco uniforme**. Confianza: **media**.

---

## 11. Madurez

**Digitalizada**. **Automatizada** solo con sync + recordatorios + escritura de resultado en CRM. IA de scheduling: capacidad de mercado general, no madurez sectorial inmobiliaria ES.

---

## 12. Validación

| Ítem | Confianza |
|------|-----------|
| Sync Tools ↔ Google Calendar | Media-alta (doc Idealista) |
| Fricción doble agenda | Media (cualitativa) |
| % visitas solo-WhatsApp | Pendiente |
| No-show rate nacional | Hueco |

---

← [Telefonía VoIP](telefonia-voip.md) | [Índice](../README.md) | [Siguiente: Gestión de proyectos →](gestion-proyectos.md)
