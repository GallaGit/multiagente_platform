# Telefonía VoIP / centralitas cloud

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza:** media (mercado fragmentado; precios poco homogéneos)

---

## 1. Función principal

Voz sobre IP y **centralitas cloud** (PBX hosted): números geográficos/900, colas, IVR, extensión móvil, a menudo **grabación de llamadas** y **click-to-call** desde el CRM. Sustituye o complementa la línea fija tradicional de oficina.

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Agente | Softphone / app; llamadas a leads y propietarios |
| Recepción / admin | Colas, transferencia, horarios |
| Dirección | Escucha de calidad (si hay grabación), reporting |
| Compliance | Retención de grabaciones, aviso legal |

---

## 3. Momento del flujo

Captación telefónica, devolución de leads de portal, confirmación de visitas, negociación, coordinación con notaría/banco. Convive con WhatsApp; en muchos equipos la voz queda para «serio» o primer contacto si no hay móvil del lead.

---

## 4. Información gestionada

CDRs (quién/cuándo/duración), grabaciones, notas post-llamada, CLI del llamante, a veces screening. Idealmente vínculo `llamada ↔ contacto CRM ↔ inmueble`.

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Connectors en CRM inmobiliarios (click-to-call, popup ficha) — cobertura desigual por fabricante |
| **API** | Webhooks CDR, APIs de operadores cloud (Ringover, Vonage, 3CX cloud, operators ES…) |
| **Automatización** | CDR → CRM actividad; Power Automate / Make |
| **Manual** | Marcar a mano y anotar en WhatsApp/CRM |
| **Inexistente** | Grabación + CRM unificado en muchas micros |

---

## 6. Flujo de datos (ASCII)

```text
[Lead con teléfono]
      |
      v
[Click-to-call CRM] -----> [Centralita cloud / VoIP]
      |                         |
      |                         +--> [Grabación + CDR]
      v                         |
[Ficha contacto] <----- sync? --+
      |
      v
[Nota manual si no hay integración]
```

---

## 7. Limitaciones y tareas humanas

- Sin integración: la llamada no deja rastro en el expediente.
- Grabación: obligación de informar; política de retención; espacio.
- Números personales de agentes bypasean la centralita.
- Calidad Wi-Fi / móvil en visitas presenciales.
- Multi-sede: enrutado complejo vs coste.

---

## 8. Costes

| Componente | Observabilidad |
|------------|----------------|
| Centralita cloud / usuario o extensión | Listas públicas **variables** por vendor; muchas bajo presupuesto o promo |
| Números geográficos / portabilidad | Fee alta + mensual — según operador |
| Grabación / almacenamiento | A menudo módulo extra |
| Minutos / planes ilimitados | Condiciones comerciales |
| Conector CRM | Incluido o setup |

**No se fija un «precio medio España inmobiliario».** Citar solo tarifas de un vendor concreto tras consulta de su web en fecha. Pendiente de investigación TCO voz vs WhatsApp.

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos de categoría (no ranking) |
|---------|-------------------------------------|
| Centralita cloud PYME | Operadores ES + PBX cloud internacionales |
| Softphone integrado CRM | Vendors con marketplace inmobiliario |
| Móvil corporativo MDM | Sin IVR; más simple |
| Solo WhatsApp voice/calls | Evita PBX; pierde número fijo profesional |
| Telefonía tradicional RTB | En declive en agencias digitalizadas |

No hay «VoIP inmobiliario» vertical dominante público comparable a Idealista en portales.

---

## 10. Adopción

**Habitual** en medianas/multi-oficina; **poco uniforme** en micro (móvil personal). Click-to-call CRM: **poco utilizada–habitual** según madurez del CRM. Confianza: **media-baja**.

---

## 11. Madurez

**Digitalizada** donde hay cloud PBX. **Automatizada** solo con CDR/grabación ligadas al CRM. Asistentes de voz IA: **emergentes** en marketing de vendors; adopción real en agencias ES no censada.

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Rol de centralita + click-to-call | Media (práctica + docs CRM) |
| Penetración por arquetipo | Pendiente |
| Precios comparables | Hueco — no inventar |
| % llamadas vs WhatsApp en cierre | Pendiente |

---

← [WhatsApp Business](whatsapp-business.md) | [Índice](../README.md) | [Siguiente: Calendarios →](calendarios.md)
