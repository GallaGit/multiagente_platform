# WhatsApp Business

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza:** alta en distinción app vs API; media en adopción cualitativa

---

## 1. Función principal

Canal **dominante de conversación comercial** con demandantes y propietarios: cualificación informal, envío de links/fotos, confirmación de visitas y negociación rápida. En la práctica muchas agencias viven en WhatsApp aunque tengan CRM: el chat queda **fuera del sistema de registro**.

---

## 2. Usuarios

| Rol | Patrón |
|-----|--------|
| Agente | App móvil Business (o personal) 24/7 |
| Equipo | Número compartido / etiquetas Business App |
| Ops digital | API Cloud + BSP (proveedor) + CRM/omnicanal |
| Cliente | Espera respuesta en minutos, no en email |

---

## 3. Momento del flujo

Tras el lead (portal/web/llamada) → casi todo el nurturing hasta visita y frecuentemente hasta arras. Menos uso formal en AML/KYC documental (aunque se envíen fotos de DNI — mala práctica). Postventa: incidencias y coordinación notaría.

---

## 4. Información gestionada

Mensajes, audio, fotos de inmuebles, ubicaciones, documentos PDF, datos de contacto. Metadatos de plantillas (API). **No** hay modelo de datos inmobiliario nativo (referencia anuncio, etapa pipeline, comisión).

---

## 5. Integraciones

| Tipo | App Business | API WhatsApp Business (Cloud) |
|------|--------------|-------------------------------|
| **Nativa** | Catálogo, etiquetas, respuestas rápidas | Conectores CRM/BSP oficiales |
| **API** | No (app cerrada) | Sí — Meta Cloud API vía BSP |
| **Automatización** | Limitada / no soportada | iPaaS, bots, routing |
| **Manual** | Copiar resumen al CRM | Menos si hay sync |
| **Inexistente** | Historial unificado multiagente robusto | — |

**Distinción crítica:** App ≠ API. La app no convierte a la agencia en «omnicanal integrado».

---

## 6. Flujo de datos (ASCII)

```text
[Lead portal/email/web]
        |
        v
[Agente inicia / responde en WhatsApp]
        |
   +----+------------------+
   |                       |
   v                       v
[App Business]      [API + BSP + CRM]
 historial en móvil    mensajes en ficha
 copia manual CRM      plantillas + opt-in
```

---

## 7. Limitaciones y tareas humanas

- Conversación **fuera del CRM** → pérdida de trazabilidad y de handoff entre agentes.
- Números personales = riesgo al salir el empleado.
- Políticas Meta: ventanas de 24 h, plantillas aprobadas (API), bloqueos por spam.
- Envío de documentación sensible por chat.
- Doble canal: cliente escribe al móvil del agente, no al de la agencia.

---

## 8. Costes

| Capa | Precio |
|------|--------|
| WhatsApp Business **App** | Gratuita (app) |
| WhatsApp Business **Platform / Cloud API** | Tarificación Meta por conversación / categoría / país; **no hay tarifa única «agencia ES»** publicada como pack inmobiliario |
| BSP (360dialog, MessageBird, Twilio, etc.) | Margen/fee del proveedor — **bajo presupuesto** típico |
| Conector CRM | Incluido o módulo — según fabricante |

No se inventan €/conversación. Consultar [Meta pricing](https://developers.facebook.com/docs/whatsapp/pricing) en la fecha de compra · **[Alta sobre el modelo; media sobre factura real]**.

---

## 9. Competencia / enfoques

| Enfoque | Pros | Contras |
|---------|------|---------|
| App Business sola | Cero fricción | Fuera CRM; frágil |
| API + CRM vertical | Trazabilidad | Coste + compliance plantillas |
| Inbox omnicanal | Unifica web+WA | Adopción emergente |
| SMS / llamada | Formal | Menos adopción cliente ES |
| Telegram/Instagram DM | Nicho | Menor que WA en cierre |

Competencia real: **email** (más lento) y **teléfono**; no otros mensajeros.

---

## 10. Adopción

**Muy extendida** (app / número de agente). **[Alta cualitativa]**  
API Business / BSP: **emergente–poco utilizada** en micro; más en medianas/PropTech. **[Media]**

Pendiente explícito en registro de fuentes: % App vs API.

---

## 11. Madurez

Uso típico: **digitalizada** (chat móvil) pero proceso **tradicional** respecto al expediente. Con API+CRM: hacia **automatizada**. Bots de cualificación = capa IA posible; penetración ES no equivalente a marketing de vendors.

---

## 12. Validación

| Afirmación | Confianza |
|------------|-----------|
| Canal comercial dominante | Media-alta (sectorial; no INE) |
| Fuera del CRM en micro | Media-alta |
| App ≠ API | Alta |
| Coste API homogéneo | Hueco — no inventar |

No citar ROI de `context.md` como hecho.

---

← [Microsoft 365](microsoft-365.md) | [Índice](../README.md) | [Siguiente: Telefonía VoIP →](telefonia-voip.md)
