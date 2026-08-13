# Home staging (físico y virtual)

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Preparación de inmueble para comercialización

---

## 1. Función principal

Mejorar la percepción del inmueble en visitas y en anuncios (fotos/tours) para acelerar comercialización o sostener precio. El staging **físico** interviene en el espacio real; el **virtual** altera o amuebla imágenes/modelos 3D sin obra material completa.

---

## 2. Usuarios

Agente captador / comercial, propietario (quien suele costear o autorizar), empresas de staging, fotógrafos, editores 3D/virtual staging, a veces franquicia con proveedor homologado.

---

## 3. Momento del flujo

Tras mandato y antes (o en paralelo) de fotografía/publicación en portales y web. A veces re-staging digital si el anuncio no convierte. No forma parte de KYC, hipoteca ni postventa.

---

## 4. Información gestionada

- Brief del inmueble (vacío/ocupado, estilo, presupuesto)
- Inventario de mobiliario (físico) o assets 3D
- Imágenes antes/después; derechos de uso
- En virtual: archivos fuente, capas, marcas de agua “imagen virtualizada” (buena práctica comercial; no siempre aplicada)
- Pedidos y facturas a proveedor (a menudo fuera del CRM)

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Staging → fotos → CRM/portales | Manual | Flujo dominante |
| Software virtual staging → Matterport/tour | Manual / API (casos) | Capacidad ≠ uso masivo ES |
| Pedido staging ↔ CRM tareas | Manual / inexistente | WhatsApp/email habitual |
| Portales | Manual (subida de fotos) | Sin “staging nativo” de agencia |

---

## 6. Flujo de datos (ASCII)

```text
Mandato
   │
   ├─► Staging FÍSICO ──► sesión foto / tour ──► CRM / portales
   │
   └─► Staging VIRTUAL ◄── fotos vacías / tour
              │
              ▼
         Imágenes editadas ──manual──► anuncio
```

---

## 7. Limitaciones y tareas humanas

- Coste y logística del físico (transporte, seguros, tiempos) → muchas microagencias lo omiten o limitan a limpieza/declutter.
- Virtual: riesgo de expectativa engañosa si no se etiqueta; marco publicidad veraz (consumo). **[Alta normativa general; Media praxis]**
- Coordinación propietario–staging–fotógrafo suele ser WhatsApp, sin SLA en CRM.
- No hay estadística oficial de % de anuncios con staging en España. **[Alta sobre el hueco]**

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Servicio staging físico (proveedor local) | no público / bajo presupuesto (varía por m² y ciudad) |
| SaaS / apps de virtual staging | Modelos freemium o por imagen; **precios homogéneos ES no consolidados en fuente única** → tratar importes de blogs como no oficiales **[Media-baja]** |
| Incluido en pack foto de agencia | no público |

Principio metodológico: sin página de fabricante o contrato visible → **no público**.

---

## 9. Competencia / enfoques comparados

| Enfoque | Cuándo aparece | Trade-off |
|---------|----------------|-----------|
| Físico completo | Viviendas vacías alto ticket / exclusivas | Coste y tiempo altos; realismo máximo en visita |
| Declutter + home styling ligero | Volumen residencial | Menor impacto visual en foto |
| Virtual staging 2D | Anuncios de vacíos; presupuesto bajo | Barato/rápido; riesgo reputacional si no se declara |
| Amueblado 3D sobre tour | Tours Matterport / 360 | Integración visual fuerte; coste plataforma + edición |
| Sin staging | Mayoría micro / alquiler rápido | Dependencia de precio y ubicación |

Proveedores: mix de empresas locales de interiorismo + herramientas PropTech de virtual staging (mercado fragmentado; sin censo de cuota). **[Media]**

---

## 10. Adopción + confianza

| Práctica | Adopción aparente | Confianza |
|----------|-------------------|-----------|
| Staging físico sistemático | Poco utilizada / nicho alto valor | Baja |
| Virtual staging ocasional | Emergente–habitual en marketing visual | Media-baja |
| Etiquetado “imagen virtual” | Irregular | Baja |

PwC: ~700 PropTech en España (2025) — incluye players de visualización, **no** mide adopción en agencias. **[Media]** · [PwC](https://www.pwc.es/es/sala-prensa/notas-prensa/2025/record-proptech-contech-espana-impulso-innovacion-inmobiliario.html)

---

## 11. Madurez + justificación

**Tradicional → Digitalizada:** el físico es oficio; el virtual introduce herramienta digital aislada.  
Rara vez **Automatizada** (pedido → render → CRM → portal sin humanos).  
Madurez típica agencia ES: **Tradicional/Digitalizada** según ticket. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Impacto cuantificado en días en mercado (ES) | Sin estadística oficial representativa → no citar cifras |
| Precios medios staging | Pendiente (encuesta proveedores) |
| Obligación legal de marcar fotos virtuales | Buena práctica + normas publicidad; detalle casuístico pendiente |
| Integraciones nativas CRM↔staging | Capacidad limitada; uso real no demostrado |

---

← [Analítica](analitica-web.md) | [Índice](../README.md) | [Siguiente: Fotografía →](fotografia.md)
