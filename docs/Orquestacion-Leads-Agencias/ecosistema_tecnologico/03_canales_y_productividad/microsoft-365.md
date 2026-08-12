# Microsoft 365 (y Teams)

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza:** alta en precios web ES; media en adopción inmobiliaria

---

## 1. Función principal

Suite productiva empresarial: **Outlook**, Exchange, OneDrive, Word/Excel/PowerPoint (según plan), SharePoint, **Microsoft Teams** (chat, reuniones, archivos). En agencias con cultura Windows es el backbone de correo, reuniones internas y repositorio documental ligero.

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Agente | Outlook, Teams móvil, OneDrive, Bookings (si se activa) |
| Back-office | SharePoint/OneDrive, Excel comisiones, correo notaría |
| Dirección / multi-oficina | Teams (canales), Planner (ver gestión-proyectos) |
| IT / franquicia | Entra ID, políticas, licencias |

---

## 3. Momento del flujo

Transversal operativo e interno. **Teams** concentra coordinación de equipo y videollamadas; el cliente final sigue mayoritariamente en **WhatsApp/teléfono/email**. Momentos densos: briefings de captación, traspaso de encargos, cierre documental.

---

## 4. Información gestionada

Correo, calendarios Outlook, chats Teams, grabaciones de reunión (según políticas), archivos de operación, Excel de pipeline/comisiones. Datos de clientes en buzones y OneDrive → RGPD.

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | CRM con add-in Outlook; Dynamics (poco habitual en microagencia ES); Bookings |
| **API** | Microsoft Graph (mail, calendar, Teams, files) |
| **Automatización** | **Power Automate** (ventaja vs Workspace en shops Microsoft) |
| **Manual** | Export a CRM/portales; copiar leads |
| **Inexistente** | Teams no publica en Idealista ni sustituye portal |

---

## 6. Flujo de datos (ASCII)

```text
[Portal] --> [Outlook] --> [CRM / copia manual]
[Agenda visitas] <--> [Outlook Calendar] <--> [CRM]
[Equipo multi-oficina] <--> [Teams canales + reuniones]
[Docs operación] --> [OneDrive / SharePoint] --> [Firma / email]
[Power Automate] --> reglas mail/Teams --> CRM / Excel
```

---

## 7. Limitaciones y tareas humanas

- Teams **interno** ≠ canal comercial dominante con el lead.
- Shadow IT: grupos Teams sin retención ni clasificación.
- Excel de comisiones fuera del CRM → doble verdad.
- Licenciamiento confuso (con/sin Teams, Copilot aparte).
- Coste Copilot elevado frente a ticket medio de microagencia.

---

## 8. Costes

Precios públicos web España (sin IVA; suscripción anual mostrada; consulta ago. 2026):

| Plan | Precio lista | Incluye Teams (chat/reuniones) |
|------|--------------|--------------------------------|
| Microsoft 365 Empresa **Básico** | **5,20 €**/usuario·mes (anual) | Sí |
| Microsoft 365 Empresa **Estándar** | **10,83 €**/usuario·mes (anual) | Sí |

Fuentes: [Planes M365 empresas ES](https://www.microsoft.com/es-es/microsoft-365/business/compare-all-microsoft-365-business-products-b) · [Business Basic](https://www.microsoft.com/es-es/microsoft-365/business/microsoft-365-business-basic) · **[Alta]**

Notas:

- Pago mensual suele ser mayor (ej. Basic ~6,24 € en ficha).
- **Copilot** para empresas: ficha lista **18,20 €**/usuario·mes anual (complemento) — mismo comparador · **[Alta]**
- Aviso de **actualización de precios** Microsoft a partir de **1 jul 2026** en SKUs comerciales (impacto local según canal/contrato). Tratar importes web como **vigentes en consulta**, no perpetuos · **[Media]**
- Premium / Enterprise: consultar ficha; no inventar.

---

## 9. Competencia / enfoques

| Enfoque | Notas |
|---------|-------|
| Google Workspace | Alternativa cloud; Meet vs Teams |
| Solo Outlook.com / correo hosting | Más barato; menos colaboración |
| Slack + Google | Híbridos PropTech |
| CRM con chat interno | Reduce Teams para operación comercial |

En franquicias y redes, M365 suele venir **impuesto o preacordado**.

---

## 10. Adopción

**Habitual** en medianas/grandes y oficinas tradicionales Windows; **irregular** en micro. Teams: habitual como chat interno donde ya hay M365; **poco** como canal cliente. Confianza: **media**.

---

## 11. Madurez

**Digitalizada** (correo + archivos + Teams). **Automatizada** si Power Automate + Graph alimentan CRM. Copilot = capa IA del fabricante; uso inmobiliario ES **no censado**.

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Precios Basic/Standard ES | Alta (web Microsoft) |
| Teams como hub interno | Media cualitativa |
| % agencias M365 vs Workspace | Pendiente |
| Uso real Copilot en CNAE 683 | Pendiente / emergente |

---

← [Google Workspace](google-workspace.md) | [Índice](../README.md) | [Siguiente: WhatsApp Business →](whatsapp-business.md)
