# Email (Outlook / Gmail)

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria · **Confianza:** media-alta en rol operativo; baja en cuotas de proveedor

---

## 1. Función principal

Bandeja de entrada de **leads de portales**, comunicación con propietarios/compradores, envío de documentación y, con frecuencia, **archivo informal de contratos y hilos** fuera del CRM. Es dependencia crítica: si el email cae o no se lee, se pierden oportunidades aunque el CRM esté licenciado.

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Agente | Responder leads, coordinar visitas, adjuntos |
| Admin / back-office | Contratos, facturas, notaría, proveedores |
| Dirección | Negociación, reporting por reenvío |
| Particular (cliente) | Canal «oficial» frente a WhatsApp informal |

---

## 3. Momento del flujo

Todo el ciclo: lead portal → cualificación → envío de fichas/propuestas → arras/documentación → postventa administrativa. Punto de mayor densidad: **primeras 24–48 h del lead** y envíos documentales pre-firma.

---

## 4. Información gestionada

| Tipo | Ejemplos | Riesgo |
|------|----------|--------|
| Lead | Nombre, teléfono, referencia anuncio | No entra al CRM |
| Conversación comercial | Precios, disponibilidad, objeciones | Historial fuera de expediente |
| Documentos | DNI, notas simples, borradores arras, CEE | RGPD / retención descontrolada |
| Operativa interna | Reenvíos, CC masivos | Duplicidad y pérdida de versión |

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Outlook ↔ Microsoft 365; Gmail ↔ Google Workspace; sync email en algunos CRM (captura de mensajes) |
| **API** | Microsoft Graph, Gmail API; webhooks de CRM; parsers de lead |
| **Automatización** | Power Automate, Zapier, Make, n8n: email → CRM / Slack / hoja |
| **Manual** | Dominante en micro: copiar datos del lead al Excel/CRM |
| **Inexistente** | Trazabilidad completa lead→cierre solo con email |

---

## 6. Flujo de datos (ASCII)

```text
[Portal] --email lead--> [Outlook / Gmail]
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
         [CRM sync]     [Copia manual]   [WhatsApp]
         (si existe)     (frecuente)     (continúa chat)
              |               |
              v               v
         [Expediente]    [Hilo suelto / carpeta]
```

---

## 7. Limitaciones y tareas humanas

- El email **no es CRM**: sin campos de estado, scoring ni pipeline.
- Leads fuera de horario se enfrían si no hay reglas/alertas.
- Adjuntos sensibles en buzones personales o alias compartidos.
- Alias genéricos (`info@`) sin asignación clara de responsable.
- Hilos largos sustituyen al expediente digital.

---

## 8. Costes

| Producto | Precio público (consulta ago. 2026) | Notas |
|----------|-------------------------------------|-------|
| Gmail personal | Gratuito | Uso frecuente en micro; dominio no profesional |
| Google Workspace (incluye Gmail) | Ver [google-workspace.md](google-workspace.md) | SaaS por usuario |
| Microsoft 365 (incluye Outlook) | Ver [microsoft-365.md](microsoft-365.md) | SaaS por usuario |
| Solo Exchange Online / planes mail | Variable según SKU Microsoft | Consultar ficha M365 |
| Coste de **no** integrar leads | No cuantificado públicamente | Pendiente |

No se estiman «€/lead perdidos» sin fuente.

---

## 9. Competencia / enfoques

| Enfoque | Quién | Encaje agencia |
|---------|-------|----------------|
| Buzón M365 + Outlook | Microsoft | Oficinas ya en ecosistema Windows/Teams |
| Buzón Workspace + Gmail | Google | Agencias cloud-first / móviles |
| Alias + reenvío a agentes | DIY | Micro; fricción alta |
| Captura nativa CRM | Inmovilla, Witei, Idealista Tools, etc. | Reduce copia manual **si se configura** |

El «competidor» real del email corporativo no es otro cliente de correo, sino **WhatsApp** como canal conversacional y el **CRM** como sistema de registro.

---

## 10. Adopción

**Muy extendida** — prácticamente universal. **[Alta]**

Matiz: en micro es habitual Gmail/Outlook personal; en mediana/grande, dominio corporativo. No hay censo CNAE 683 de proveedor de correo. Confianza en el matiz: **media-baja**.

---

## 11. Madurez

**Digitalizada** en el sentido de canal digital ubicuo; **tradicional** en proceso cuando el buzón es el sistema de registro.

Paso a **automatizada** solo cuando hay reglas de enrutado + captura CRM + retención documentada. Uso de IA en bandeja (resúmenes Copilot/Gemini) = capacidad de fabricante, adopción en inmobiliarias ES **no censada** → no clasificar el sector como «impulsado por IA» por email.

---

## 12. Validación

| Punto | Estado |
|-------|--------|
| Email como bandeja de leads de portales | Práctica documentada (Tools importa leads por email) · **[Media-alta]** |
| Dependencia crítica operativa | Consistente con mapa de fricciones del README · **[Media]** |
| % leads solo-email vs API | **Pendiente** |
| Split Outlook vs Gmail en CNAE 683 | **Pendiente** |

No usar cifras de `context.md` (leads perdidos / ROI) como evidencia.

---

← [Portales](portales-inmobiliarios.md) | [Índice](../README.md) | [Siguiente: Google Workspace →](google-workspace.md)
