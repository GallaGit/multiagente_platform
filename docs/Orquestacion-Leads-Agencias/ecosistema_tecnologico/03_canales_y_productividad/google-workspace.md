# Google Workspace

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza:** alta en precios/listado oficial Help; media en adopción sectorial inmobiliaria

---

## 1. Función principal

Suite de productividad cloud: **Gmail**, Calendar, Drive, Docs/Sheets/Slides, Meet, Chat. En la agencia sustituye o complementa el «office» local y centraliza correo de dominio, archivos compartidos y agenda de visitas.

---

## 2. Usuarios

| Rol | Apps núcleo |
|-----|-------------|
| Agente | Gmail, Calendar, Drive (fotos/fichas), Meet |
| Admin | Drive compartido, Sheets (pipeline improvisado), Docs |
| Dirección | Drive + Sheets reporting ligero |
| Franquiciado | A veces Workspace impuesto / recomendado por marca |

---

## 3. Momento del flujo

Transversal: recepción de leads (Gmail), coordinación de visitas (Calendar), trabajo documental pre-firma (Drive/Docs), reuniones internas/cliente (Meet). No cubre por sí solo CRM inmobiliario ni publicación en portales.

---

## 4. Información gestionada

Correo, calendarios, archivos (contratos, planos, fotos), hojas de cálculo usadas como CRM/PMS ligero, grabaciones Meet (según plan). Datos personales de clientes → obligaciones RGPD (responsable: la agencia).

---

## 5. Integraciones

| Tipo | Situación |
|------|-----------|
| **Nativa** | Idealista Tools ↔ Google Calendar (documentado); muchos CRM con Gmail/Calendar |
| **API** | Gmail API, Calendar API, Drive API, Admin SDK |
| **Automatización** | Zapier/Make/n8n; Apps Script |
| **Manual** | Export CSV, adjuntos a portales/CRM |
| **Inexistente** | Workspace ≠ MLS ni portal; no liquida comisiones |

---

## 6. Flujo de datos (ASCII)

```text
[Portal lead] --> [Gmail] --> (manual/API) --> [CRM]
[Visita] <--> [Google Calendar] <--> [CRM / Idealista Tools]
[Fotos/CEE/arras] --> [Drive] --> [Firma / email / WhatsApp]
[Equipo] <--> [Chat / Meet]
```

---

## 7. Limitaciones y tareas humanas

- Drive/Sheets como CRM genera versiones y permisos caóticos.
- Sin gobierno: fotos de inmuebles y DNI en carpetas personales.
- Meet no sustituye WhatsApp con el demandante final.
- Límites de almacenamiento por edición; basura digital acumula coste.
- Identidad: cuentas personales mezcladas con dominio → sombra IT.

---

## 8. Costes

Precios de lista **Business** (Google Help; moneda EUR; impuestos según checkout):

| Edición | Plan flexible (usuario/mes) | Plan anual (usuario/mes) |
|---------|----------------------------|---------------------------|
| Business Starter | **8,1 €** | **6,8 €** |

Fuente: [Comparar plan flexible vs anual](https://support.google.com/a/answer/1247360?hl=es) · consulta ago. 2026 · **[Alta]**

Business Standard / Plus: consultar [pricing oficial](https://workspace.google.com/pricing?hl=es) (la UI puede mostrar USD u ofertas de lanzamiento). Revendedores ES citan orientativos flexibles Starter 8,10 / Standard 16,20 / Plus 25,30 € usuario·mes — **[Media; no sustituye checkout Google]**.

Enterprise: bajo presupuesto. Impuestos y promos de nuevos clientes: verificar en compra.

---

## 9. Competencia / enfoques

| Alternativa | Diferencia relevante |
|-------------|----------------------|
| Microsoft 365 | Outlook/Teams/SharePoint; fuerte en oficinas Windows |
| Solo Gmail gratuito | Sin control admin ni Drive corporativo |
| CRM + storage propio | Menos dependencia Drive; más coste SaaS vertical |
| Solo WhatsApp + Excel | Stack micro; sin correo de dominio |

Elección suele ser **identidad de correo + hábito del equipo**, no feature inmobiliaria.

---

## 10. Adopción

**Habitual** en medianas digitales y PropTech-agencia; **irregular** en micro (mezcla personal/corporativo). Confianza: **media-baja** (sin censo CNAE 683).

INE TIC no publica «% Workspace» para inmobiliarias.

---

## 11. Madurez

Uso típico: **digitalizada**. **Automatizada** solo con integraciones Calendar/Gmail→CRM y reglas. Gemini en Workspace = capacidad anunciada; adopción inmobiliaria ES **no medida** → no subir madurez sectorial a «IA».

---

## 12. Validación

| Ítem | Confianza |
|------|-----------|
| Precios Starter EUR Help | Alta |
| Sync Calendar con Idealista Tools | Media-alta (doc fabricante) |
| Penetración en agencias ES | Baja — pendiente encuesta |
| Sheets como CRM de facto | Media cualitativa |

---

← [Email](email.md) | [Índice](../README.md) | [Siguiente: Microsoft 365 →](microsoft-365.md)
