# Vídeo y tour virtual

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Matterport · Kuula · tours 360 · vídeo comercial

---

## 1. Función principal

Permitir visita remota o pre-cualificación (tour 3D/360, vídeo walkthrough, reels) para reducir visitas inútiles y reforzar el anuncio en portales/web/redes. Complementa la fotografía 2D; no sustituye la visita física en la mayoría de compraventas residenciales.

---

## 2. Usuarios

Operador de escáner / fotógrafo 360, agente, marketing, comprador remoto (consumo), portales (embebido o enlace). En grandes: equipos de contents centralizados.

---

## 3. Momento del flujo

Tras mandato y preparación del inmueble; publicación junto al anuncio; uso en nurturing y envío por WhatsApp. Reutilizable en post-captación si el inmueble vuelve al mercado (si la licencia de hosting sigue activa).

---

## 4. Información gestionada

- Nube de puntos / tour ID / escenas 360
- Vídeo (mp4), miniaturas, hotspots, medidas (si el producto las ofrece)
- Enlaces públicos, embeds, permisos de privacidad
- Metadatos de inmueble asociados en CRM (URL del tour)

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Matterport → web / anuncio | Nativa (embed) / manual (URL) | |
| Matterport API / developer tools | API (planes de pago) | Capacidad; uso agencia ES limitado **[Media-baja]** |
| Kuula / viewers 360 → web | Nativa embed / manual | |
| Tour ↔ CRM | Manual (campo URL) / nativa en algunos CRM | |
| Tour ↔ portales | Manual o campo multimedia del CRM | Depende del portal |
| Vídeo YouTube/Vimeo → ficha | Manual | |
| WhatsApp | Manual (enlace) | Canal de distribución real |

---

## 6. Flujo de datos (ASCII)

```text
Escaneo 360 / grabación vídeo
         │
         ▼
Plataforma (Matterport / Kuula / editor vídeo)
         │
         ├─► URL / embed ──► Web / Portales / CRM
         └─► MP4 / Shorts ──► Redes / WhatsApp
                    │
                    ▼
            Pre-visita remota → visita física
```

---

## 7. Limitaciones y tareas humanas

- Coste de cámara Pro + plan cloud vs volumen de cartera.
- Espacios “activos” limitados por plan → baja de tours antiguos.
- Inmuebles ocupados: logística y privacidad.
- Comprador español sigue priorizando visita presencial en residencial (evidencia cualitativa; sin %) **[Media-baja]**.
- Capacidad anunciada de “dollhouse / medidas” ≠ adopción masiva en microagencias.

---

## 8. Costes (solo públicos)

**Matterport** ([Price List](https://support.matterport.com/s/article/Matterport-Price-List?language=en_US) · consulta ago. 2026) · **[Alta]**:

| Plan (ejemplos) | Mensual | Anual |
|-----------------|---------|-------|
| Free | 1 espacio activo | — |
| Starter 5 | **13 €** | **132 €** |
| Starter 20 | **52 €** | **528 €** |
| Professional 20 | **65 €** | **636 €** |
| Professional 50 | **148 €** | **1.476 €** |
| Business 100 | **332 €** | **3.324 €** |
| Enterprise | Contactar ventas | |

También públicos: cámara **Pro3 3.695 €**; planos esquemáticos y add-ons por espacio (p. ej. floor plan regular Starter **20 €**). Impuestos adicionales según fabricante.

| Otros | Dato |
|-------|------|
| Kuula | Planes en web del fabricante; verificar importe vigente (no fijar cifra si la página es dinámica) → **consultar fabricante** / no inventar **[Media]** |
| YouTube | Hosting vídeo gratuito (con condiciones) |
| Operador local de tours | no público / bajo presupuesto |
| Edición vídeo freelance | no público |

---

## 9. Competencia / enfoques comparados

| Enfoque | Fortaleza | Debilidad |
|---------|-----------|-----------|
| Matterport (escáner + cloud) | Estándar de facto 3D dollhouse | Coste hardware + espacios activos |
| Tours 360 (Kuula, Panotour, etc.) | Más barato de entrar | Menos “modelo 3D” percibido |
| Vídeo walkthrough / Reels | Viralidad redes; bajo coste móvil | Menos exploración libre |
| Solo fotos | Mínimo viable | Menos pre-cualificación remota |
| Visita presencial exclusiva | Confianza | Más tiempo agente |

Fragmentación: muchas agencias premium o internacionales usan Matterport; el tejido micro suele quedarse en vídeo móvil o nada. **[Media]**

---

## 10. Adopción + confianza

| Arquetipo | Adopción | Confianza |
|-----------|----------|-----------|
| Luxury / internacionales / grandes | Habitual | Media |
| Mediana residencial | Habitual-baja (selectivo por ticket) | Media-baja |
| Micro | Poco utilizada | Baja |
| Vídeo corto en redes | Emergente–habitual | Media-baja |

Sin censo nacional de tours activos por agencia. **[Alta sobre el hueco]**

---

## 11. Madurez + justificación

Donde existe: **Digitalizada** (tour como activo de marketing).  
**Automatizada** solo con API/CRM y publicación portal sin pegar URL a mano — minoritario.  
Madurez típica del tejido: **Tradicional/Digitalizada** (foto + a veces vídeo). **[Media]**

---

## 12. Validación

| Ítem | Evidencia | Pendiente |
|------|-----------|-----------|
| Precios Matterport EUR | Price List oficial | Cambios de tarifa post-corte |
| % anuncios Idealista con tour | — | Muestreo |
| ROI tours (visitas evitadas) | — | No inventar |
| Integraciones nativas CRM ES | Documentación por fabricante | Inventario sistemático |

---

← [Fotografía](fotografia.md) | [Índice](../README.md) | [Siguiente: Software hipotecario →](../05_operaciones_especializadas/software-hipotecario.md)
