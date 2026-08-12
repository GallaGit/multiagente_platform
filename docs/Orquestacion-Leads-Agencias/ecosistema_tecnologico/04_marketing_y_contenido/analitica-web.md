# Analítica web y medición digital

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** GA4 · Search Console · Tag Manager · reporting

---

## 1. Función principal

Medir tráfico, fuentes, comportamiento en web/landings y conversiones (formulario, clic a WhatsApp, llamada). Orientar SEO y campañas. No sustituye al reporting comercial del CRM (visitas, ofertas, cierres).

---

## 2. Usuarios

Marketing, titular de oficina, agencia externa SEO/SEM, a veces franquiciador (consolas multi-propiedad). Agentes raramente consultan GA4 día a día.

---

## 3. Momento del flujo

Transversal a captación digital (web, ads, SEO). Interviene antes y durante la generación de leads; casi nunca en pipeline post-visita salvo dashboards BI corporativos.

---

## 4. Información gestionada

- Eventos y páginas (GA4), consultas y cobertura (Search Console)
- Contenedores de etiquetas (GTM): Pixel Meta, Google Ads, consent mode
- Conversiones definidas (lead, llamada, WhatsApp)
- Dimensiones de campaña (UTM)
- En grandes: exportación a BigQuery / BI (capacidad; no uso típico micro)

**No incluye** por defecto: tasa de cierre CRM, calidad de lead ni comisiones.

---

## 5. Integraciones (tipo)

| Conexión | Tipo |
|----------|------|
| Web → GA4 / GTM | Nativa (script / contenedor) |
| Search Console ↔ GA4 | Nativa (vinculación Google) |
| Ads Meta/Google ↔ GA4 | Nativa / API (conversiones) |
| GA4 → CRM | API / automatización / inexistente en micro |
| GA4 → Looker Studio / Power BI | Nativa / API |
| Portales → analítica de agencia | Inexistente (datos del portal no se vuelcan a GA4 de la agencia) |

---

## 6. Flujo de datos (ASCII)

```text
Usuario web/app
    │
    ▼
GTM (consent + tags) ──► GA4 ──► informes / Looker Studio
    │                     │
    ├─► Pixel Meta        └─► (raro) CRM / BI
    └─► Google Ads
Search Console ◄──► sitio (indexación / queries)
```

---

## 7. Limitaciones y tareas humanas

- Consentimiento cookies reduce volumen medible (AEPD / ePrivacy).
- WhatsApp y teléfono como conversión: tracking incompleto sin call tracking.
- Leads de portales **no** pasan por GA4 → sesgo si se optimiza solo la web.
- Configuración GA4/GTM suele ser externa; eventos mal definidos = vanidad métricas.
- Capacidad anunciada de “analítica avanzada” ≠ cultura de decisión basada en datos.

---

## 8. Costes (solo públicos)

| Producto | Precio público |
|----------|----------------|
| Google Analytics 4 (estándar) | Gratuito |
| Google Search Console | Gratuito |
| Google Tag Manager | Gratuito |
| GA360 / enterprise | no público / bajo presupuesto |
| Call tracking / BI embebido | no público (terceros) |

Consulta fabricante Google (productos gratuitos) · **[Alta]**

---

## 9. Competencia / enfoques comparados

| Enfoque | Qué optimiza | Qué pierde |
|---------|--------------|------------|
| Solo GA4 + Search Console | SEO/SEM y web propia | Visión portal-dominada del negocio |
| CRM reports (leads/cierres) | Embudo comercial | Origen digital fino |
| BI corporativo (grandes) | Multi-oficina, KPIs | Coste/implantación; INE BI 16,1% en ≥10 emp. |
| Informes del portal (Idealista Tools, etc.) | Rendimiento de anuncios en portal | No unifica con web/ads |

Relación con dato INE: **Business Intelligence 16,1%** en empresas CNAE 68 con 10+ empleados (T1 2023). Es proxy de madurez analítica **interna**, no de instalación de GA4. **[Alta cifra; baja representatividad del tejido micro]** · [INE](https://www.ine.es/jaxi/Tabla.htm?tpx=59889)

Analítica interna (concepto INE): **36,6%** mismo universo. **[Alta]**

---

## 10. Adopción + confianza

| Señal | Lectura | Confianza |
|-------|---------|-----------|
| GA4/GTM en webs de agencias | Habitual en quien tiene web activa | Media-baja (sin censo) |
| Uso decisional diario | Poco utilizada fuera de marketing/franquicia | Baja |
| BI formal (INE 16,1%) | Poco utilizada en ≥10; desconocida en micro | Alta (dato); baja (extrapolación) |
| CBRE madurez 5,2/10 · IA gen. 71% | Muestra grandes; no comparable con INE | Media |

---

## 11. Madurez + justificación

Uso típico: **Digitalizada** (tags instalados, informes básicos).  
**Automatizada** solo si eventos → CRM/BI sin Excel.  
No clasificar el sector como “impulsado por IA” en analítica: sin evidencia homogénea. **[Media]**

---

## 12. Validación

| Afirmación | Evidencia | Pendiente |
|------------|-----------|-----------|
| BI 16,1% / analítica interna 36,6% (CNAE 68 ≥10) | INE T1 2023 | Adopción <10 empleados |
| GA4 gratuito | Documentación Google | — |
| % webs agencia con GA4 + consent mode correcto | — | Auditoría muestra |
| Correlación gasto ads ↔ cierres | — | Datos internos |

---

← [Web/CMS](web-cms-captacion.md) | [Índice](../README.md) | [Siguiente: Home staging →](home-staging.md)
