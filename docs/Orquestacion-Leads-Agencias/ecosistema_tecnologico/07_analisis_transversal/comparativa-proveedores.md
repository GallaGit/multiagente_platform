# Comparativa de proveedores y enfoques

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Objetivo:** contrastar **enfoques** (no rankings de cuota). Sin proponer producto.

---

## 1. Criterios de comparación

| Criterio | Qué se mira |
|----------|-------------|
| Tamaño / alcance | Vertical ES vs suite global vs portal-adjacente |
| Mercado objetivo | Micro, mediana, grande, franquicia, PropTech |
| Funcionalidades | Inventario, leads, publicación, firma, finanzas |
| Especialización | Jerga/flujo inmobiliario ES vs plataforma genérica |
| Precio público | Solo cifras con fuente; resto = **no público** |

**Fuera de alcance:** inventar cuotas de marca; usar blogs «X% del MLS» como hecho.

---

## 2. CRM: vertical ES vs genérico vs portal-adjacente

| Enfoque | Ejemplos | Mercado típico | Especialización | Funcionalidades núcleo | Limitaciones |
|---------|----------|----------------|-----------------|------------------------|--------------|
| **Vertical ES** | Inmovilla, Witei, Inmoweb / InmoCMS | Micro→mediana; redes locales | Alta (encargos, MLS, portales ES) | Inventario, pipeline, multipublicación | BI/IAM limitados; lock-in; APIs desiguales |
| **Portal-adjacente** | Idealista Tools (Starter/Office) | Quien vive en Idealista | Alta en canal Idealista | Leads/inbox, inventario ligado al portal | Dependencia ecosistema portal; precio **no público** |
| **Genérico enterprise** | Salesforce, HubSpot | Grandes / PropTech / grupos | Baja out-of-the-box en inmueble ES | Automatización, apps, gobernanza | Hay que modelar inmueble + publicación; impl. cara |
| **Sin CRM / Excel** | Hojas + WhatsApp | Micro | Nula | Contactos ad hoc | Sin trazabilidad |

### Precios públicos documentados (CRM)

| Proveedor | Dato | Fuente | Confianza |
|-----------|------|--------|-----------|
| **Inmovilla** Full Edition | **79 €/mes** hasta 7 usuarios; **+12 €/usuario** extra | [inmovilla.com/precios](https://inmovilla.com/precios/) · ago. 2026 | **[Alta]** |
| **Witei** | Freemium + planes; importes web **promocionales/variables** | [get.witei.com](https://get.witei.com/es/precios-crm/) | **[Media]** |
| Inmoweb / Idealista Tools / Salesforce / HubSpot (pack ES) | **No público** homogéneo | Fichas de categoría | — |

**Lectura:** el vertical gana *time-to-value* comercial ES; el genérico gana integración corporativa cuando hay TI. **[Media]** · Ver [crm-inmobiliarios.md](../02_sistemas_core/crm-inmobiliarios.md).

---

## 3. Portales inmobiliarios

| Actor | Enfoque | Mercado | Especialización | Precio |
|-------|---------|---------|-----------------|--------|
| **Idealista** | Portal + Tools CRM | Nacional percibido dominante | Demanda + herramientas agencia | Packs / Tools: **no público** |
| **Fotocasa** (Adevinta) | Portal generalista | Nacional | Packs profesionales | **No público** |
| **Habitaclia** | Regional fuerte | Catalunya / Baleares | Ecosistema Adevinta | **No público** |
| **Pisos.com** | Alternativa nacional | Irregular por zona | Menor «producto agencia» | **No público** |
| **Milanuncios** | Clasificados | Particular + profesional | Menos flujo agencia | Freemium / destacados variables |

CNMC: Idealista/Fotocasa = **plataformas de anuncios**, no intermediarios jurídicos. **[Alta]**  
**Sin cuota pública** comparable 2024–2026: no asignar %. · [portales-inmobiliarios.md](../03_canales_y_productividad/portales-inmobiliarios.md)

---

## 4. Firma electrónica

| Enfoque | Ejemplos | Mercado objetivo | Especialización | Notas |
|---------|----------|------------------|-----------------|-------|
| **Cloud ES/EU** | Signaturit (Namirial) | Pyme / mediana ES | eIDAS + UX consumidor | Precios claros |
| **Global enterprise** | DocuSign | Multinacionales / grupos | Ecosistema amplio | Planes globales variables |
| **Challenger EU** | Yousign | Pyme UE | Similar a Signaturit | Verificar web; no fijar € aquí |
| **Certificado local** | Autofirma + FNMT | Trámites cualificados | Alta seguridad, mala UX masiva | No sustituye flujo arras tipico |
| **Módulo CRM/portal** | Embebidos | Quien ya está en el stack | Conveniencia | Auditar nivel SES/AES/QES |

### Precios públicos (firma)

| Proveedor | Precio (pago anual, usuario·mes) | Fuente |
|-----------|----------------------------------|--------|
| **Signaturit** Business | **35 €** | [signaturit.com/es/precios](https://www.signaturit.com/es/precios/) · **[Alta]** |
| **Signaturit** Business+ | **57 €** | Idem |
| DocuSign / Yousign | Variables; **no fijar** sin captura de ficha | — |

Comparar por **nivel eIDAS + evidencia + integración CRM**, no solo marca. · [firma-electronica.md](../02_sistemas_core/firma-electronica.md)

---

## 5. Finanzas: facturación y contabilidad

| Enfoque | Ejemplos | Mercado | Especialización inmobiliaria | Funciones |
|---------|----------|---------|------------------------------|-----------|
| **Suite pyme all-in-one** | Holded | Micro→mediana | Marketing vertical; no CRM inmobiliario completo | Factura, banco, contabilidad ligera |
| **Facturación ligera** | Contasimple (y similares) | Micro + asesoría | Baja | Facturas honorarios, IVA |
| **Ecosistema asesorial** | A3 (Wolters Kluwer) | Pyme vía gestoría | Cumplimiento fiscal ES | Contabilidad/nóminas vía partner |
| **ERP mid-market** | Sage, Exact, etc. | Grande / grupo | Baja sectorial | Finance + reporting |

| Concepto | Precio público |
|----------|----------------|
| Holded / Contasimple | Planes en web — **consultar**; no inventar € aquí |
| A3 | **No público** homogéneo (canal partner) |
| Asesoría externa | **No público** (cuota por volumen) |

El CRM vertical **rara vez** es el facturador oficial. · [facturacion.md](../02_sistemas_core/facturacion.md) · [contabilidad.md](../02_sistemas_core/contabilidad.md)

---

## 6. Matriz sintética por arquetipo

| Arquetipo | CRM habitual | Portales | Firma | Finanzas |
|-----------|--------------|----------|-------|----------|
| Micro | Witei / Tools / Excel | 1–2 críticos | Puntual (Signaturit u otra) | Contasimple / Holded / asesoría |
| Mediana | Vertical (p. ej. Inmovilla) | Multi-portal | Habitual creciente | Holded + asesoría / A3 |
| Grande | Vertical o Salesforce/HubSpot | Multi + web | Enterprise / API | ERP / A3 / suite |
| Franquicia | Impuesto por red | Local ± centralizado | Según red | Local + royalties |
| PropTech | Propio / genérico | Secundario o supply | API | Stack finanzas propio |

---

## 7. Validación

| Afirmación | Estado |
|------------|--------|
| Inmovilla 79 €; Signaturit 35/57 € | Verificado fabricante · **[Alta]** |
| Portales sin tarifa pública homogénea | Hueco declarado · **[Alta]** |
| Cuota de marca CRM/portal | **No pública** — no inventar |
| «Mejor» proveedor absoluto | Fuera de alcance de este informe |

---

← [Ciberseguridad](../06_datos_automatizacion_e_ia/ciberseguridad-identidad.md) | [Índice](../README.md) | [Siguiente: Costes TCO →](costes-tco.md)
