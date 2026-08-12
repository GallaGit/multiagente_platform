# CRM inmobiliarios

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Confianza metodológica:** alta en cifras oficiales/precios públicos; media-baja en adopción real por marca

---

## 1. Función principal / problema que resuelve

Sistema de registro comercial de **contactos, leads, encargos e inventario** (venta/alquiler intermediado). Centraliza pipeline, visitas, seguimiento y publicación hacia portales.

**Capacidad anunciada:** pipeline, MLS, publicación multiportal, WhatsApp/email, firma, informes.  
**Integración disponible:** connectors portales, API/webhooks variables por fabricante.  
**Uso real típico:** inventario + fichas + leads de portales; conversación comercial sigue en WhatsApp/email fuera del CRM. **[Media]**

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Agente / comercial | Leads, visitas, seguimiento |
| Captador | Encargos, exclusivas, fotos/fichas |
| Responsable de oficina | Pipeline, reparto, reporting |
| Admin / back-office | Usuarios, plantillas, calidad de datos |
| Franquiciador (si aplica) | Stack impuesto, reporting de red |

---

## 3. Momento del flujo operativo

Captación de propietario → alta de inmueble → captación de demanda (portales/web/WhatsApp) → cualificación → visitas → oferta/negociación → documentación pre-cierre → postventa ligera.

No sustituye PMS de alquiler administrativo ni contabilidad/ERP.

---

## 4. Información gestionada

- Contactos (propietarios, demandantes, colaboradores)
- Inmuebles (atributos, estado, exclusividad, fotos, CEE)
- Actividades (llamadas, visitas, tareas)
- Orígenes de lead y estados de oportunidad
- Comisiones / liquidaciones (capacidad uneven; uso irregular)
- Documentos adjuntos (notas simples, contratos borrador)

Datos sensibles (DNI, IBAN, KYC): a menudo **fuera** o en carpetas paralelas. **[Media]**

---

## 5. Integraciones

| Destino | Tipo habitual | Notas |
|---------|---------------|-------|
| Portales (Idealista, Fotocasa, etc.) | Nativa / API | Calidad y bi-dirección variables |
| MLS / colaboración | Nativa (según CRM) | Ver [mls.md](mls.md); riesgo competencia histórico |
| Email / calendario | Nativa o manual | Sync incompleto frecuente |
| WhatsApp | API / automatización / manual | Uso real: app personal o Business no CRM |
| Firma electrónica | Nativa / API / manual | No universal |
| Contabilidad / facturación | Manual / automatización | Rara vez nativa completa |
| ERP genérico | API / inexistente | Grandes: Salesforce/HubSpot + middleware |
| Drive / documental | Manual / automatización | Carpetas por operación |

---

## 6. Flujo de datos (ASCII)

```text
[Portal / Web / WhatsApp]
        |  lead / consulta
        v
   [CRM inmobiliario] ----publicación----> [Portales]
        |  contacto + inmueble
        +----colaboración----> [MLS / otras agencias]
        |
        +----doc/firma------> [Gestor / Firma]  (a menudo manual)
        |
        v
   [Agente]  <----conversación paralela----> [WhatsApp / Email]
```

---

## 7. Limitaciones y tareas humanas

- CRM como “licencia” vs sistema de registro real (WhatsApp gana la conversación).
- Duplicados de contactos; campos vacíos; estados inconsistentes.
- Publicación multiportal: reescritura o desync de precios/estado.
- Reporting de comisiones multiagente incompleto.
- Migración entre CRM: export limitado; coste de cambio alto (no cuantificado públicamente).

---

## 8. Costes

| Proveedor | Modelo / precio público | Fuente | Confianza |
|-----------|-------------------------|--------|-----------|
| **Inmovilla** Full Edition | **79 €/mes** hasta 7 usuarios; **+12 €/usuario** extra; impuestos no incluidos en ficha típica | [inmovilla.com/precios](https://inmovilla.com/precios/) · ago. 2026 | **[Alta]** |
| **Witei** | Freemium + planes de pago; importes en web **promocionales/variables** | [get.witei.com/es/precios-crm](https://get.witei.com/es/precios-crm/) | **[Media]** |
| Inmoweb, InmoCMS | no público (presupuesto / pack web+CRM) | — | — |
| Idealista/tools Office | no público | — | — |
| Salesforce / HubSpot | no público en pack “inmobiliaria ES”; licencia por usuario + impl. | — | — |
| Implantación / migración | no público | — | — |

Coste dominante suele ser **tiempo + portales**, no la cuota CRM. **[Media-baja]**

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos | Pros | Contras |
|---------|----------|------|---------|
| **Vertical ES** | Inmovilla, Witei, Inmoweb, InmoCMS | Inventario, portales, MLS, jerga local | Lock-in; reporting BI limitado; APIs desiguales |
| **Portal-adjacente** | Idealista/tools Office | Proximidad al canal de demanda | Dependencia del ecosistema portal; precio no público |
| **Genérico enterprise** | Salesforce, HubSpot | Automatización, IAM, ecosistema apps | Coste/impl.; hay que modelar “inmueble” y publicación |
| **Sin CRM / Excel** | Microagencias | Bajo coste aparente | Pérdida de leads, sin trazabilidad |

**Vertical vs genérico:** el vertical gana en *time-to-value* comercial ES; el genérico gana en integración corporativa y gobernanza cuando hay TI. **[Media]**

---

## 10. Nivel de adopción + confianza

- INE TIC, actividades inmobiliarias (CNAE 68), empresas **≥10 empleados**, T1 2023: **CRM 57,9%**. **[Alta]** · [INE](https://www.ine.es/jaxi/Tabla.htm?tpx=59889)
- Representatividad sobre microagencias (~mayoría del tejido CNAE 683): **baja** — adopción real desconocida; Excel/WhatsApp frecuentes. **[Alta sobre el hueco]**
- Ranking de cuota por marca: **no público / no censado**. Afirmaciones tipo “X% de MLS” en blogs: **no verificadas**. **[Baja]**

**Clasificación:** habitual en medianas/grandes; incierta en micro. **[Media]**

---

## 11. Nivel de madurez + justificación

**Digitalizada** (uso típico ES): hay CRM, pero automatización lead→visita→cierre es parcial; IA anunciada ≠ uso sistemático.

Frontera de fabricantes: hacia **automatizada** (webhooks, scoring). Uso impulsado por IA: emergente y polarizado (ver INE IA sectorial vs CBRE grandes). **[Media]**

---

## 12. Validación

| Evidencia | Estado |
|-----------|--------|
| Precio Inmovilla / Signaturit (otras fichas) / INE CRM | Verificado con fuente |
| Precios Witei absolutos | Promocionales → no fijar cifra estable |
| Penetración por marca y provincia | Pendiente |
| % leads gestionados solo en WhatsApp | Pendiente (cualitativo) |
| Discrepancia blogs “90% MLS / miles de agencias” | No usar como hecho |

---

← [Datos y registro](../01_arquitectura_y_flujos/modelos-datos-sistemas-registro.md) | [Índice](../README.md) | [Siguiente: ERP →](erp.md)
