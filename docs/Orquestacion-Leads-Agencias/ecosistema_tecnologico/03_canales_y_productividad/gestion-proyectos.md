# Gestión de proyectos

**Corte:** agosto de 2026 · **Ámbito:** España · agencias · **Confianza:** media-baja en adopción; alta en que el vertical es débil

---

## 1. Función principal

Organizar tareas de equipo (captación, marketing, reformas ligeras, onboarding, apertura de oficina) con tableros/listas: **Trello, Asana, Notion, Microsoft Planner**, etc. En inmobiliaria **compiten con las tareas del CRM**; el encaje vertical es **pobre**: no modelan inmueble, encargo ni comisión.

---

## 2. Usuarios

| Rol | Uso típico |
|-----|------------|
| Dirección / ops | Roadmap interno, checklists de calidad |
| Marketing | Campañas, contenidos, landing |
| Agentes | Poco uso si el CRM ya tiene actividades |
| Franquicia HQ | Playbooks en Notion |

---

## 3. Momento del flujo

Más **interno** que lead-to-cash: lanzamientos, compliance checklist, mudanzas de oficina, proyectos PropTech. En el ciclo de una operación, la «tarea» natural vive en CRM (llamar, visitar, enviar propuesta).

---

## 4. Información gestionada

Tarjetas, asignados, fechas, subtareas, comentarios, a veces docs embebidos. Rara vez referencia registral o ID de portal. Riesgo: datos de clientes pegados en tarjetas Notion/Trello sin DPA claro.

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Planner ↔ Teams/M365; Notion/Asana/Trello con Slack/Google |
| **API** | APIs maduras en Asana/Trello/Notion |
| **Automatización** | iPaaS CRM→tarjeta (poco mantenido) |
| **Manual** | Duplicar tarea CRM + Trello |
| **Inexistente** | PM tool → publicación portal / liquidación honorarios |

---

## 6. Flujo de datos (ASCII)

```text
[Operación inmobiliaria] --> [Tareas CRM] --> [Cierre / comisión]
        |
        x  (a menudo desconectado)
        |
[Proyecto interno] --> [Trello/Asana/Notion/Planner]
        |
        v
[Done]  (sin impacto en inventario)
```

---

## 7. Limitaciones y tareas humanas

- Dos sistemas de tareas → abandono de uno.
- Notion como wiki + mini-CRM improvisado = deuda.
- Poco reporting comercial (embudo, €).
- Licencias por usuario suman sin ROI claro en micro.
- Permisos: externos (fotógrafos) en tableros con datos sensibles.

---

## 8. Costes

| Herramienta | Precio |
|-------------|--------|
| Microsoft **Planner** | Incluido en varios M365 Business (ver ficha M365) |
| Trello / Asana / Notion | Planes freemium + SaaS por usuario; **consultar web oficial** en compra — importes cambian y hay promos |
| CRM tasks | Incluidas en licencia CRM |

No se copian precios de blogs comparativos. Si se necesita cifra: URL + fecha en actualización de esta ficha.

---

## 9. Competencia / enfoques

| Enfoque | Lectura |
|---------|---------|
| **Solo CRM tasks** | Adecuado al ciclo comercial |
| **Planner + Teams** | Natural si ya hay M365 |
| **Notion HQ** | Documentación + ligera gestión; riesgo shadow CRM |
| **Asana/Trello** | Marketing/ops; poco vertical |
| **Jira** | Raro salvo PropTech software |

Conclusión: categoría **poco vertical** para intermediación; valor en ops/marketing, no en sustituir CRM.

---

## 10. Adopción

**Poco utilizada** como sistema core en microagencias. **Habitual** de forma parcial en equipos de marketing/sede de redes. Confianza: **media-baja**.

---

## 11. Madurez

Donde existe: **digitalizada**. Rara vez **automatizada** con el CRM inmobiliario. No impulsada por IA de forma sectorial.

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Poco vertical vs CRM | Alta cualitativa |
| Adopción cuantitativa ES | Pendiente |
| Precios actuales vendors | Verificar web; no fijar aquí sin consulta |

---

← [Calendarios](calendarios.md) | [Índice](../README.md) | [Siguiente: Atención omnicanal →](atencion-omnicanal.md)
