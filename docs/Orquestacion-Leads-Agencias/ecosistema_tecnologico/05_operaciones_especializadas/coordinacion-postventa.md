# Coordinación postventa

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Llaves · incidencias · reviews · referidos

---

## 1. Función principal

Cerrar el ciclo tras arras/escritura o firma de alquiler: entrega de llaves, lecturas, incidencias de primeros días, documentación al cliente, solicitud de reseñas y activación de referidos. En agencias de solo intermediación suele ser **ligera**; en las que gestionan alquiler o “llaves en mano” es operativa continua (lindante con PMS).

---

## 2. Usuarios

Agente que cerró la operación, admin de oficina, propietario, comprador/inquilino, proveedores (cerrajero, cleaning), comunidad/administradores, a veces broker (seguimiento satisfacción).

---

## 3. Momento del flujo

Post-firma (compraventa o alquiler) → entrega → periodo de incidencias → archivo comercial → marketing de reviews/referidos. Puede reabrir el embudo (segunda operación, captación por referido).

---

## 4. Información gestionada

- Inventario de llaves, alarmas, códigos, citas de entrega
- Checklist de entrega (lecturas, inventarios de mobiliario en alquiler)
- Tickets de incidencias y proveedores
- Enlaces a Google/portales de opiniones
- Contactos para referidos; estado de “cliente feliz”
- En alquiler gestionado: fianza, averías (más PMS que CRM puro)

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| CRM tarea postventa | Nativa / manual | Muchos CRM tienen etapa; uso irregular |
| WhatsApp con cliente | Manual | Canal real dominante |
| Ticketing (Freshdesk, etc.) | Poco vertical inmobiliario | Más en grandes |
| Google Business / reseñas | Manual / automatización recordatorio | |
| PMS alquiler ↔ incidencias | Nativa en PMS | Si la agencia gestiona patrimonio |
| Firma inventarios | Nativa firma / manual PDF | |
| Contabilidad (comisión cobrada) | Manual / API | Cierre económico |

---

## 6. Flujo de datos (ASCII)

```text
Escritura / contrato alquiler
         │
         ▼
Checklist entrega + llaves ──► Cliente
         │
         ├─► Incidencias ──WhatsApp/tel──► Agente / proveedor
         ├─► Pedido review (Google / portal)
         └─► Pedido referidos ──► nuevos leads CRM
                │
                ▼
         Archivo / NPS interno (si existe)
```

---

## 7. Limitaciones y tareas humanas

- Postventa “invisible” en CRM: se gestiona por WhatsApp y se pierde trazabilidad. **[Media]**
- Reviews: sesgo y riesgo de prácticas prohibidas (reseñas ficticias); cumplimiento normas plataformas y publicidad.
- Referidos: sin programa estructurado, solo favor personal.
- Compraventa: tras cobro de honorarios el incentivo de seguimiento cae.
- Alquiler: Ley 12/2023 asigna gastos de gestión al arrendador en vivienda — afecta quién paga la “postventa” de formalización, no elimina incidencias. **[Alta]** · [BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203)

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Módulo postventa CRM | Suele incluido en SaaS; sin desglose (ej. pack Inmovilla **79 €/mes**) | [Inmovilla](https://inmovilla.com/precios/) · **[Alta]** |
| Google Business Profile | Gratuito |
| Software ticketing genérico | Según fabricante; no tarifa sectorial única |
| Incentivos por referido | no público (política comercial) |
| PMS si hay gestión alquiler | no público / plan del fabricante |

---

## 9. Competencia / enfoques comparados

| Enfoque | Encaje | Fricción |
|---------|--------|----------|
| Nada formal (solo WhatsApp) | Micro compraventa | Sin métricas ni escalado |
| Etapas CRM + recordatorios | Mediana | Disciplina de uso |
| PMS / property management | Carteras de alquiler | Otro sistema además del CRM de venta |
| Plataformas de reviews + automatización email | Marca local | Dependencia de buzones y consentimiento |
| Central franquicia (CSAT/NPS) | Redes | Datos pueden no quedar en la agencia local |

No hay “estándar postventa” nacional publicado para agencias. **[Alta sobre el hueco]**

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| Entrega de llaves coordinada por agente | Muy extendida | Alta |
| Ticketing formal | Poco utilizada | Baja |
| Programa sistemático de reviews | Habitual-baja | Media-baja |
| Referidos medidos en CRM | Poco utilizada | Baja |
| Postventa alquiler gestionado | Habitual en admin. fincas / 6832 | Media |

---

## 11. Madurez + justificación

Uso típico intermediación pura: **Tradicional** (teléfono/WhatsApp).  
Con CRM disciplinado: **Digitalizada**.  
Automatización de reviews/referidos: minoritaria.  
Madurez asignada al arquetipo intermediación: **Tradicional/Digitalizada**. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Rol postventa en cadena de valor | Cualitativo (`analisis_del_mercado/02-funcionamiento.md`) |
| % agencias con SLA postventa | Pendiente |
| Impacto referidos en captación | Sin serie oficial → no inventar ROI |
| Solape CRM venta vs PMS alquiler | Mapear por arquetipo en stacks |

---

← [KYC-AML](kyc-aml-compliance.md) | [Índice](../README.md) | [Siguiente: Automatización →](../06_datos_automatizacion_e_ia/automatizacion.md)
