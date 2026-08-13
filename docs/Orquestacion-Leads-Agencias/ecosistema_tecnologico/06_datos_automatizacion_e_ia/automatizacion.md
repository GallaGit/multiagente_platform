# Automatización (iPaaS / RPA ligero)

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Zapier · Make · n8n · Power Automate · puentes CRM–WhatsApp–portales–firma

---

## 1. Función principal

Conectar sistemas que la agencia ya usa (CRM, email, hojas, WhatsApp API, firma, formularios web) para **mover datos y disparar acciones sin reescritura manual**: alta de lead, notificación al agente, publicación o sincronización de ficha, recordatorio de visita, envío a firma.

No sustituye al CRM como sistema de registro comercial; es **capa de orquestación**. Capacidad anunciada ≠ adopción masiva en microagencias. **[Media]**

---

## 2. Usuarios

| Rol | Uso típico |
|-----|------------|
| Ops / admin de oficina | Construye y mantiene escenarios |
| Responsable comercial | Recibe alertas; no diseña flujos |
| Agente | Consume el resultado (tarea CRM, WA) |
| Integrador / PropTech | n8n self-host o API a medida |
| Franquiciador | Automatizaciones centralizadas (si hay stack común) |

---

## 3. Momento del flujo

Transversal: lead (portal/web) → CRM → notificación → nurturing → firma/documentos → postventa (reviews). El mayor valor percibido está en **respuesta rápida al lead** y en evitar doble tecleo portal↔CRM. Post-cierre: menor uso salvo checklists.

---

## 4. Información gestionada

- Eventos: nuevo lead, cambio de etapa, nueva visita, documento firmado  
- Payloads: contacto, referencia de inmueble, URL, etiquetas  
- Credenciales OAuth/API de apps conectadas  
- Logs de ejecución (éxito/fallo)  

Datos sensibles (DNI, KYC) no deberían circular por iPaaS sin minimización y base jurídica. **[Alta normativa]**

---

## 5. Integraciones (tipo)

| Puente | Tipo habitual | Notas |
|--------|---------------|-------|
| Portal → CRM | Nativa CRM / API / automatización | Calidad bi-dirección irregular |
| Web form → CRM | Automatización / nativa | Muy frecuente |
| CRM → WhatsApp | API + BSP / automatización / manual | App Business ≠ API |
| CRM ↔ email/calendario | Nativa o automatización | Sync incompleto frecuente |
| CRM → firma electrónica | Nativa / automatización | Ver `02_sistemas_core/firma-electronica.md` |
| CRM → Drive/Sheets | Automatización | “CRM sombra” en Excel |
| Contabilidad / facturación | Manual / automatización | Rara vez nativa completa |

---

## 6. Flujo de datos (ASCII)

```text
[Portal / Web / Email]
        |  webhook / polling / export
        v
   [iPaaS: Zapier | Make | n8n | Power Automate]
        |
        +----► [CRM]  (alta / update lead)
        +----► [WhatsApp API / BSP]  (aviso / plantilla)
        +----► [Firma]  (envío documento)
        +----► [Slack / Teams / email interno]
        |
        v
   [Agente]  <---- conversación real ----> [WhatsApp App]  (a menudo fuera del flujo)
```

---

## 7. Limitaciones y tareas humanas

- Conectores “existen” pero el mapeo de campos inmobiliarios (referencia, exclusividad, comisión) suele ser **manual y frágil**.  
- WhatsApp App personal **no** se automatiza bien; hace falta API + consentimiento/plantillas Meta.  
- Fallos silenciosos: lead no llega al CRM; nadie monitoriza el historial de runs.  
- Gobernanza: quien mantiene el escenario (titular vs empleado) y rotación de claves.  
- Franquicia: el franquiciado puede no poder tocar el middleware central.

---

## 8. Costes (solo públicos)

Precios en **USD** según páginas oficiales; factura en EUR/IVA y tipo de cambio varían. Consulta: ago. 2026.

| Herramienta | Dato público | Fuente |
|-------------|--------------|--------|
| **Make** | Free (1.000 créditos/mes); Core **12 $/mes**, Pro **21 $/mes**, Teams **38 $/mes** (base 10k créditos; facturación anual mostrada en web); Enterprise custom | [Make pricing](https://www.make.com/en/pricing) · **[Alta]** |
| **Zapier** | Free (100 tasks/mes); Professional desde **19,99 $/mes** anual (750 tasks) / **29,99 $** mensual; Team desde **69 $/mes** anual (2.000 tasks); Enterprise custom | [Zapier pricing](https://zapier.com/pricing) · **[Alta]** |
| **Power Automate** | Premium **15 $/usuario/mes** (pago anual); Process **150 $/bot/mes**; Hosted Process **215 $/bot/mes** (precios marketing USD; país/divisa en checkout) | [Power Automate](https://www.microsoft.com/en-us/power-platform/products/power-automate/pricing) · **[Alta]** |
| **n8n Cloud** | Starter **20 €/mes**, Pro **50 €/mes** (facturación anual); Business **667 €/mes** anual (self-host con licencia); Enterprise custom; Community self-host gratuita | [n8n pricing](https://n8n.io/pricing/) · **[Alta]** |
| Conectores CRM vertical | Incluidos o módulo — según fabricante; sin tarifa sectorial única | no público homogéneo |

Implantación, mantenimiento de escenarios y costes BSP WhatsApp: **no públicos** como pack inmobiliario.

---

## 9. Competencia / enfoques comparados

| Enfoque | Encaje | Fricción |
|---------|--------|----------|
| Zapier | Rapidez, catálogo amplio | Coste por task a volumen; vendor US |
| Make | Escenarios visuales complejos, créditos | Curva de aprendizaje; créditos AI |
| n8n | Control / self-host / coste infra | Ops técnica; compliance hosting |
| Power Automate | Stack Microsoft 365 | Licenciamiento; menos “apps PropTech” |
| Solo conectores nativos CRM | Menos piezas | Huecos portal/WA/firma |
| Scripts / API a medida | Grandes / PropTech | Coste desarrollo |

No hay estándar nacional de iPaaS en agencias. **[Alta sobre el hueco]**

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| iPaaS en micro (1–5) | Emergente / irregular | Baja–media |
| iPaaS o flujos en **medianas** | **Habitual–emergente** (según madurez CRM) | Media |
| Power Automate en oficinas M365 | Habitual en entornos Microsoft | Media |
| n8n self-host | Poco utilizada (técnicos/PropTech) | Baja |
| Puente CRM–WhatsApp API | Emergente | Media |
| Sync portal↔CRM solo nativo | Habitual | Media |

Ancla cuantitativa: INE no publica “% iPaaS” para CNAE 68. Se infiere de polarización digital (CRM 57,9% en ≥10; micro no censada). **[Alta sobre el hueco]**

---

## 11. Madurez + justificación

Uso típico micro: **Tradicional/Digitalizada** (copiar-pegar).  
Mediana con CRM + 2–5 escenarios: **Digitalizada → Automatizada** parcial.  
Gran brokerage / PropTech: **Automatizada** (a veces con RPA).  
Madurez asignada al tejido intermediación: **Digitalizada**, con bolsas **Automatizadas** en medianas. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Precios Make / Zapier / Power Automate / n8n Cloud | Páginas oficiales ago. 2026 · **[Alta]** |
| % agencias ES con iPaaS | Pendiente (sin serie INE) |
| Calidad real sync Idealista/Fotocasa ↔ CRM | Capacidad ≠ uso; mapear por fabricante |
| ROI de automatización de leads (`context.md`) | **No usar como hecho** · hipótesis no verificada |

---

← [Coordinación postventa](../05_operaciones_especializadas/coordinacion-postventa.md) | [Índice](../README.md) | [Siguiente: BI →](business-intelligence.md)
