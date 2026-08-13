# Software hipotecario y financiación

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Brokers hipotecarios · simuladores · banca · comisiones

---

## 1. Función principal

Facilitar la viabilidad financiera del comprador (simulación, comparación de ofertas, tramitación con entidades) para que la operación no caiga entre arras y escritura. La agencia puede **referir** a un broker, operar mesa propia, o dejar al cliente con su banco. Forma parte de la agencia extendida: datos sensibles circulan fuera del CRM inmobiliario.

---

## 2. Usuarios

Comprador, agente inmobiliario (cualificación LTV/plazo), broker hipotecario / intermediario de crédito, entidad financiera, tasadora (flujo paralelo). En franquicias: partner financiero homologado.

---

## 3. Momento del flujo

Cualificación temprana de demanda → oferta/arras → tramitación hipoteca → tasación → aprobación → firma notarial. También en captación (“te ayudo con la hipoteca”) como argumento comercial.

---

## 4. Información gestionada

- Ingresos, deudas, scoring interno, ratio esfuerzo
- Simulaciones (cuota, TIN/TAE, plazos)
- Documentación KYC/solvencia del comprador
- Estado del expediente con el banco
- En modelos de referidos: ID de operación y comisión de success fee

Tratamiento RGPD estricto; a menudo el broker es responsable o encargado distinto de la agencia.

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Simulador web banco / broker → usuario | Nativa web | |
| Broker SaaS ↔ bancos | API / nativa / portal banco | Capacidad según proveedor; no universal |
| Agencia CRM ↔ broker | Manual (WhatsApp/email) / automatización rara | Uso real: manual dominante **[Media]** |
| CRM ↔ core bancario | Inexistente para agencia típica | |
| Tasación ↔ expediente hipoteca | Proceso banco/tasadora | Agencia solo recibe resultado |

---

## 6. Flujo de datos (ASCII)

```text
Lead comprador (CRM agencia)
        │  cualificación / referido
        ▼
Broker / banco (simulador + expediente)
        │
        ├─► Documentación solvencia
        ├─► Tasadora homologada BdE
        └─► Aprobación / denegación
                │
                ▼
         Notaría ←→ Agencia (cierre / comisión)
```

---

## 7. Limitaciones y tareas humanas

- Regulación de intermediarios de crédito inmobiliario (transparencia TAE, información precontractual): compliance del broker, no “feature” del CRM. **[Alta]**
- Agencia sin licencia/rol de intermediario no debe presentar el servicio como propio sin marco claro.
- Caídas de operación por denegación: seguimiento humano entre tres partes.
- Simuladores públicos ≠ oferta vinculante.
- Comisión de referido: contractual y variable; opacidad frecuente hacia el comprador si no se informa.

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Simuladores de bancos (web) | Gratuitos para el usuario |
| SaaS de brokers / agregadores | no público / bajo presupuesto (B2B) |
| Comisión intermediación hipoteca | Modelo success fee / % sobre préstamo; **importes no homogéneos públicos** → no inventar media ES **[Alta sobre el hueco]** |
| Comisión referido agencia→broker | no público (acuerdo privado) |
| Tipos de interés / TAE de mercado | Publicados por BdE/INE y bancos; no son “precio del software” |

---

## 9. Competencia / enfoques comparados

| Enfoque | Quién captura el margen | Fricción para la agencia |
|---------|-------------------------|--------------------------|
| Cliente solo con su banco | Banco | Menos control; más caídas sorpresa |
| Referido a broker externo | Broker (+ posible fee a agencia) | Handoff manual; pérdida de visibilidad |
| Mesa hipotecaria interna / JV | Agencia o filial | Compliance y coste de estructura |
| Simulador genérico en web agencia | Lead magnet | Sin tramitación real |

No proponer producto: el mapa muestra dependencia de terceros regulados. **[Alta]**

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| Hablar de hipoteca en venta residencial | Muy extendida | Alta |
| Software dedicado en la agencia | Poco utilizada (externalizado) | Media |
| Integración CRM↔broker | Emergente / manual | Baja |
| % operaciones que caen por financiación | Sin estadística nacional abierta usable aquí | — |

---

## 11. Madurez + justificación

En la agencia típica: **Tradicional/Digitalizada** (email, PDFs, Excel de seguimiento).  
El broker puede estar más **Automatizado** hacia bancos.  
No asignar madurez “IA” al cierre hipotecario residencial medio sin evidencia. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Rol notario/banco/tasador en hipoteca | Documentado (Notariado) **[Alta]** |
| Comisiones medias broker ES 2024–2026 | Pendiente (no inventar) |
| Penetración mesas propias en agencias | Pendiente |
| APIs banco–PropTech en producción | Capacidad selectiva; inventario pendiente |

---

← [Vídeo/tour](../04_marketing_y_contenido/video-tour-virtual.md) | [Índice](../README.md) | [Siguiente: Tasación/AVM →](tasacion-avm.md)
