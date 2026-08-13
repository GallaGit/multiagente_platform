# ERP (planificación de recursos)

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida

---

## 1. Función principal / problema que resuelve

Integra **finanzas, compras, inventario/operaciones y a veces RRHH** en un sistema de registro administrativo. En agencias, el “ERP” real suele ser **facturación + contabilidad + tesorería**, no un ERP industrial completo.

**Capacidad anunciada (ERP general):** módulos contables, facturación, CRM ligero, proyectos, bank feed.  
**Integración disponible:** bancos (open banking), e-factura, APIs según producto.  
**Uso real en agencia típica:** Holded/Contasimple/asesoría; ERP completo solo en redes grandes. **[Media]**

Distinción clave: **ERP inmobiliario vertical** (promoción, activos, rentas) ≠ **ERP general** adaptado a una intermediaria (CNAE 6831).

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Administración / finanzas | Facturas, cobros, conciliación |
| Dirección | Márgenes, cash, reporting |
| Asesoría externa | Contabilidad oficial, impuestos |
| TI (grandes) | Integraciones, master data |

Agentes comerciales: uso residual (partes de horas, liquidaciones) si el ERP lo permite.

---

## 3. Momento del flujo operativo

Tras el cierre comercial (o en paralelo en alquiler): emisión de honorarios, control de anticipos/arras contables, pagos a colaboradores, reporting fiscal. No gestiona pipeline de visitas (eso es CRM).

---

## 4. Información gestionada

- Clientes/proveedores (terceros)
- Facturas emitidas/recibidas, cobros/pagos
- Plan contable, asientos, impuestos (IVA, IRPF)
- Proyectos/centros de coste (oficina, agente) — si se configura
- Activos / inmuebles en balance: más propio de **promotor/PMS/SOCIMI** que de intermediario puro

---

## 5. Integraciones

| Destino | Tipo | Notas |
|---------|------|-------|
| Banca (PSD2 / bank feed) | Nativa / API | Holded y similares; Exact/Sage según pack |
| Facturación electrónica / Verifactu-TicketBAI | Nativa / API | Contexto ES en evolución; ver [facturacion.md](facturacion.md) |
| CRM inmobiliario | Manual / automatización / API | Puente débil en pymes |
| Contabilidad oficial (asesoría) | Export (XML/Excel) / API | Muy frecuente |
| Nóminas / RRHH | Módulo o inexistente | A3 ecosistema; Odoo apps |

---

## 6. Flujo de datos (ASCII)

```text
[CRM / operación] --honorarios, cliente--> [Facturación / ERP]
                                              |
                                              +--asientos--> [Contabilidad]
                                              |
                                              +--cobros----> [Bancos / open banking]
                                              |
                                              v
                                         [Asesoría / AEAT]
```

---

## 7. Limitaciones y tareas humanas

- Intermediación no encaja en “inventario de producto” estándar: se modelan servicios/comisiones.
- Liquidación multiagente y franquicia: a menudo Excel al margen del ERP.
- Doble sistema: CRM comercial + ERP/asesoría sin master data único.
- Implantación Odoo/Sage/Exact: coste y tiempo **no públicos** de forma homogénea.

---

## 8. Costes

| Proveedor | Precio público relevante | Notas |
|-----------|--------------------------|-------|
| Holded | Planes SaaS públicos en web (consultar fabricante; no fijar aquí importes no verificados en esta consulta) | Orientado pyme; CRM/facturación |
| Contasimple | no consolidar cifra sin página vigente citada | Autónomos/pymes |
| Sage, A3, Exact | **no público** tipicamente (presupuesto + partner) | Canal distribuidores |
| Odoo | Community gratis / Enterprise **bajo presupuesto** o listados partner | Personalización cara |
| “ERP inmobiliario” vertical | **no público** | Suele ser licencia + consultoría |

Si no hay página de precios clara y estable: **no público**.

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos | Encaje agencia 6831 | Encaje 6832 / activos |
|---------|----------|---------------------|------------------------|
| **ERP/contabilidad pyme cloud** | Holded, Contasimple | Alto para honorarios y caja | Medio |
| **Suite asesorial ES** | A3, ContaPlus legacy→A3 | Alto vía asesoría | Alto |
| **ERP mid-market** | Sage, Exact | Medianas/redes | Medianas |
| **ERP open + partners** | Odoo | Flexible; requiere integrador | Flexible |
| **Vertical inmobiliario / property** | Soluciones asset/PMS+ERP | Bajo-medio (overkill) | Alto |

**ERP inmobiliario vs general:** el vertical prioriza activos, rent rolls y obras; el general prioriza PGC y fiscalidad. Una agencia de compraventa suele necesitar **general ligero + CRM vertical**, no un ERP de promoción. **[Media]**

---

## 10. Nivel de adopción + confianza

- INE TIC, CNAE 68, **≥10 empleados**, T1 2023: **ERP 60,6%**. **[Alta]**
- En micro: muchas “tienen ERP” vía **asesoría** (software del despacho), no instalación propia. **[Media]**
- No hay censo público Holded vs Sage en agencias.

**Clasificación:** habitual en ≥10; en micro = externalizado. **[Media]**

---

## 11. Nivel de madurez + justificación

**Digitalizada** dominante: facturación digital + contabilidad en asesoría.  
**Automatizada** solo donde hay bank feed + reglas + puente CRM (minoritario).  
No confundir con madurez PropTech de CBRE (muestra grandes).

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| INE ERP 60,6% CNAE 68 ≥10 | Ancla oficial del módulo |
| Precios Exact/Sage/A3 | Pendiente captura página/partner |
| Distinción 6831 vs software de promoción | Cualitativa; validar con casos |

---

← [CRM](crm-inmobiliarios.md) | [Índice](../README.md) | [Siguiente: PMS →](property-management.md)
