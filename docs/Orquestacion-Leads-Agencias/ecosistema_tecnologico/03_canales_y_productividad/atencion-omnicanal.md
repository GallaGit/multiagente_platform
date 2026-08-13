# Atención omnicanal

**Corte:** agosto de 2026 · **Ámbito:** España · agencias inmobiliarias · **Confianza:** media en tendencia; baja en penetración

---

## 1. Función principal

**Inbox unificado** que concentra WhatsApp, web chat, Instagram/Facebook DM, email y a veces SMS/voz en una cola con asignación a agentes. Objetivo: que el lead no se pierda entre apps y que el historial quede en un solo hilo (idealmente ligado al CRM).

Categoría **emergente** en intermediación ES: más madura en retail/telco que en la microagencia típica.

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Agente / closer | Cola de conversaciones, plantillas, handoff |
| Team lead | SLA, distribución, escuchas |
| Marketing | Chat web en landing; widgets |
| IT / vendor | BSP WhatsApp + conectores |

---

## 3. Momento del flujo

Primera respuesta y cualificación 24/7 (humano o bot) → pase a visita/CRM. Menor peso en fase notarial. También soporte postventa en agencias con alquiler gestionado.

---

## 4. Información gestionada

Hilos multi-canal, etiquetas, estado de conversación, adjuntos, identidad del contacto (si se resuelve), métricas SLA. Bridge hacia ficha CRM (contacto, inmueble de interés).

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Suites omnicanal con WhatsApp API + web widget; algunos CRM verticales añaden inbox |
| **API** | WhatsApp Cloud API, Meta Messaging, webhooks chat |
| **Automatización** | Bots de cualificación → CRM |
| **Manual** | Seguir usando WA App + email aparte (status quo) |
| **Inexistente** | Omnicanal «de serie» en la mayoría de micros |

---

## 6. Flujo de datos (ASCII)

```text
[Web chat] ----+
[WhatsApp API]-+--> [Inbox unificado] --> [Agente / bot]
[IG / FB DM] --+           |
[Email] -------+           +--> [CRM contacto + timeline]
                           |
                     [Sin omnicanal]
                           |
              [App WA] + [Gmail] + [teléfono]  (fragmentado)
```

---

## 7. Limitaciones y tareas humanas

- Coste y complejidad Meta Business + BSP.
- Agentes deben abandonar el chat personal — cambio cultural duro.
- Resolución de identidad (mismo cliente en web y WA).
- Horarios y guardias: la herramienta no crea capacidad humana.
- Chat web vacío si el tráfico real está en portales, no en la web propia.

---

## 8. Costes

| Capa | Observabilidad |
|------|----------------|
| Plataforma omnicanal | SaaS por puesto / conversación — **listas públicas variables** |
| WhatsApp API | Tarificación Meta (ver ficha WhatsApp) |
| Widget chat web | Freemium o incluido en marketing suites |
| Implantación / bots | Presupuesto profesional |

No publicar «precio medio agencia» sin fuente. Pendiente: TCO omnicanal vs App Business gratuita.

---

## 9. Competencia / enfoques

| Enfoque | Notas |
|---------|-------|
| Inbox del CRM vertical | Menos herramientas; coverage canal desigual |
| Suite omnicanal genérica | Potente; poco «inmobiliario» |
| Solo WhatsApp API | Primer paso frecuente |
| Idealista Tools inbox leads | Unifica leads de portales, no todo el social |
| Status quo fragmentado | Dominante en micro |

---

## 10. Adopción

**Emergente** en el tejido CNAE 683 (sobre todo micro). Más visible en PropTech-agencia, lead-gen y redes con sede digital. Confianza: **media** en la etiqueta «emergente»; **baja** en %.

Alinear con README: fricción WhatsApp fuera del CRM = motor de demanda de esta categoría.

---

## 11. Madurez

Sector típico: aún **digitalizado fragmentado**. Early adopters: **automatizada** (routing + bot + CRM). Capa IA conversacional: anunciada por vendors; no elevar madurez del sector completo.

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Problema (canales dispersos) | Media-alta |
| Penetración omnicanal en agencias ES | Pendiente / emergente |
| Chat web vs portal como origen de lead | Pendiente |
| Comparativa vendors ES | Ver módulo 07 cuando exista |

**Siguiente módulo de carpeta:** marketing y contenido (ads, web, creatividades) — el chat web suele nacer ahí, no en el CRM.

---

← [Gestión de proyectos](gestion-proyectos.md) | [Índice](../README.md) | [Siguiente: Herramientas de marketing →](../04_marketing_y_contenido/herramientas-marketing.md)
