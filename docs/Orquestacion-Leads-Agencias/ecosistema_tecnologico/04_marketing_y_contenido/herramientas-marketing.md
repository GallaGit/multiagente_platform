# Herramientas de marketing y captación de demanda

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Marketing automation / ads / CRM marketing modules

---

## 1. Función principal

Atraer, cualificar y nutrir demanda (compradores/inquilinos) y, en menor medida, oferta (propietarios), mediante publicidad de pago, email marketing, redes sociales y módulos de marketing del CRM. Complementa —no sustituye— a los portales como canal dominante de leads. **[Media]**

---

## 2. Usuarios

| Rol | Uso típico |
|-----|------------|
| Responsable de marketing / oficina | Campañas ads, landing, reporting |
| Agente comercial | Contenido redes, seguimiento de leads de ads |
| Franquiciador / central | Marca, creatividades, plantillas, presupuestos compartidos |
| Agencia externa de marketing | Gestión Meta/Google Ads bajo presupuesto |

---

## 3. Momento del flujo operativo

Captación de **demanda** (anuncio → lead → CRM) y de **oferta** (captación de propietarios). También remarketing tras visitas/web y nurturing post-lead cuando el CRM o ESP tiene automatizaciones. No interviene en escritura ni postventa salvo newsletters de referidos.

---

## 4. Información gestionada

- Audiencias, creatividades, presupuestos y conversiones (Meta Ads, Google Ads)
- Listas de contactos, consentimientos LSSI/RGPD, aperturas/clics (Mailchimp, Brevo, ESP del CRM)
- UTM, eventos de conversión, IDs de campaña
- Leads (nombre, teléfono, email, inmueble de interés) hacia CRM
- Contenido orgánico en redes (no es CRM; suele vivir fuera del sistema de registro)

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Meta Ads / Google Ads → CRM | API / automatización / manual | Capacidad anunciada vía Pixel/GTM + webhooks o iPaaS; uso real irregular en micro **[Media-baja]** |
| Meta/Google → WhatsApp | Nativa (click-to-WhatsApp) / manual | Conversación suele salir del CRM |
| ESP (Mailchimp, Brevo) ↔ CRM | Nativa o API | Depende del CRM; a menudo sync parcial de contactos |
| Módulo marketing del CRM (Witei, Inmovilla, etc.) | Nativa | Email/SMS/landing dentro del mismo stack |
| Redes orgánicas → CRM | Manual / inexistente | DMs fuera del sistema de registro |
| Portales | Inexistente como ads nativos de agencia | Portales son canal propio de leads |

---

## 6. Flujo de datos (ASCII)

```text
[Meta Ads / Google Ads / Redes]
        │  clic / formulario / WhatsApp
        ▼
   Landing / Web / Pixel-GTM
        │
        ├─► CRM (lead + UTM)     [API / nativa / manual]
        ├─► ESP (lista + consentimiento)
        └─► WhatsApp / teléfono   [frecuente: fuera del CRM]
                │
                ▼
         Agente · visita · oferta
```

---

## 7. Limitaciones y tareas humanas

- Consentimiento y base jurídica (RGPD + LSSI art. 21) suelen gestionarse de forma desigual. **[Alta normativa; Media uso]**
- Leads de ads llegan por WhatsApp/email sin campos cualificados → reescritura en CRM.
- Creatividades, segmentación y optimización de puja requieren skill o agencia externa.
- Atribución multi-canal (portal vs ads vs referidos) rara vez es fiable en microagencias.
- Capacidad anunciada de “automatización 360” ≠ uso real demostrable en el tejido CNAE 683. **[Media]**

---

## 8. Costes (solo públicos)

| Concepto | Dato público | Fuente |
|----------|--------------|--------|
| Meta Ads / Google Ads (plataforma) | Sin cuota fija de software; gasto = subasta (CPC/CPM) variable | Documentación anunciantes Meta/Google · **[Alta sobre el modelo; gasto agencia: no público]** |
| Brevo Marketing | Free; Starter desde **7 €/mes**; Standard desde **17 €/mes**; Professional desde **499 €/mes** (escala por volumen de email) | [Ayuda Brevo planes](https://help.brevo.com/hc/en-us/articles/208589409) · consulta ago. 2026 · **[Alta]** |
| Mailchimp | Free + planes Essentials / Standard / Premium por nº de contactos; importes en USD en página de precios (variables por tramo) | [Mailchimp pricing help](https://mailchimp.com/help/about-mailchimp-pricing-plans/) · **[Alta sobre modelo; cifra exacta: consultar pricing page]** |
| Módulos marketing CRM ES | Incluidos o add-on según plan; Inmovilla Full Edition **79 €/mes** (hasta 7 usuarios) — no desglosa marketing por separado | [Inmovilla precios](https://inmovilla.com/precios/) · **[Alta]** |
| Gestión externa / creatividades | no público / bajo presupuesto | — |

---

## 9. Competencia / enfoques comparados

| Enfoque | Lógica | Implicación |
|---------|--------|-------------|
| Ads de pago (Meta/Google) | Compra de atención; control de audiencia | Coste variable; dependencia de Pixel/consentimiento |
| ESP horizontal (Brevo, Mailchimp) | Listas y journeys genéricos | Buena entregabilidad; sync CRM a menudo imperfecto |
| Marketing nativo del CRM inmobiliario | Un solo sistema de contactos + plantillas sectoriales | Menos herramientas; menos sofisticación de ads |
| Redes orgánicas | Marca y captación blanda | Difícil de medir; fuera del CRM |
| Dependencia casi exclusiva de portales | “Marketing” = pack de anuncios en Idealista/Fotocasa | Ads propios opcionales; tarifa portal **no pública** homogénea |

No hay ranking de cuota de gasto publicitario de agencias españolas publicado de forma comparable 2024–2026. **[Alta sobre el hueco]**

---

## 10. Adopción + confianza

| Segmento | Adopción estimada | Confianza |
|----------|-------------------|-----------|
| Medianas / grandes / franquicias | Habitual (ads + email + redes) | Media |
| Micro (mayoría CNAE 683) | Poco utilizada o irregular; WhatsApp + portales dominan | Baja (sin censo) |
| BI / reporting de marketing avanzado | Relacionado con BI INE 16,1% (CNAE 68 ≥10 emp.) — no mide ads | Alta cifra INE; baja representatividad micro |

Fuentes ancla: [INE BI](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) (contexto analítica, no ads) · **[Alta; no extrapolable a micro]**

---

## 11. Madurez + justificación

**Digitalizada** (uso típico España): campañas y email existen, pero atribución y sync CRM son débiles.  
Pocas agencias alcanzan **Automatizada** (eventos → journeys → CRM sin reescritura).  
**Impulsada por IA:** capacidad anunciada en Meta/Google/ESP (copy, audiencias); adopción sectorial no censada — no asignar como madurez típica. **[Media]**

---

## 12. Validación

| Afirmación | Evidencia | Estado |
|------------|-----------|--------|
| Portales siguen siendo canal líder de leads vs ads propios | Observación sectorial + rol CNMC de portales como plataformas de anuncios | Media; falta encuesta de mix de canales |
| Precios Brevo Starter/Standard/Pro | Página ayuda fabricante | Alta (ago. 2026) |
| Gasto medio ads por agencia ES | — | Pendiente |
| % agencias con Pixel + CRM sync | — | Pendiente |
| Penetración módulos marketing CRM | — | Pendiente |

---

← [Atención omnicanal](../03_canales_y_productividad/atencion-omnicanal.md) | [Índice](../README.md) | [Siguiente: Web/CMS →](web-cms-captacion.md)
