# Facturación

**Corte:** agosto de 2026 · **Ámbito:** España · honorarios de intermediación y, si aplica, rentas/gestión

---

## 1. Función principal / problema que resuelve

Emitir **facturas legales** (honorarios de agencia, gastos repercutidos, en gestores también rentas/liquidaciones), controlar cobros y preparar el puente a contabilidad/impuestos.

**Capacidad anunciada:** series, IVA, remesas, CRM ligero, OCR gastos.  
**Integración disponible:** bancos, contabilidad, a veces e-factura.  
**Uso real:** herramienta SaaS pyme o factura del software del asesor; CRM inmobiliario **rara vez** es el facturador oficial. **[Media]**

Contexto normativo ES (evolutivo): **TicketBAI** (PAVAS); **Verifactu** / sistemas de facturación (AEAT) — obligaciones según calendario y sujeto; no simplificar a “ya obligatorio para todos” sin chequear estado vigente en la fecha de operación. **[Alta sobre existencia del marco; media sobre detalle operativo por CCAA]**

---

## 2. Usuarios

Admin/facturación; dirección; asesoría; en alquiler, equipo de cobros.

---

## 3. Momento del flujo operativo

Al devengo o cobro de comisión (según criterio); mensual en gestión de alquileres; rectificativas si cae la operación.

---

## 4. Información gestionada

Clientes fiscales (NIF), conceptos, bases/IVA, vencimientos, estado cobrado/pendiente, ficheros para remesas, enlaces a operación/CRM (si existe referencia manual).

---

## 5. Integraciones

| Destino | Tipo |
|---------|------|
| Contabilidad / A3 | Export / API / manual |
| Banca / conciliación | Nativa (Holded etc.) / manual |
| CRM inmobiliario | Manual dominante |
| TicketBAI / Verifactu / SIF | Nativa en proveedores adaptados / intermediario |
| Portales | Inexistente (no facturan la comisión de la agencia) |

---

## 6. Flujo de datos (ASCII)

```text
[Cierre en CRM] --dato manual--> [Facturación]
                                      |
                                      +--> PDF/email cliente
                                      |
                                      +--> cobro <-- [Banco]
                                      |
                                      v
                                 [Contabilidad / AEAT]
```

---

## 7. Limitaciones y tareas humanas

- Re-teclar cliente e importe desde CRM.
- Anticipos y señales: facturar en momento correcto.
- Multi-oficina / agentes: series y centros de coste.
- Cumplir requisitos de software fiscal según territorio.

---

## 8. Costes

| Proveedor | Precio |
|-----------|--------|
| Holded | Planes SaaS en web pública — **consultar fabricante**; no inventar importe |
| Contasimple | Idem |
| FacturaDirecta | Idem |
| Módulo facturación CRM vertical | Incluido o no — **no público** si no aparece en tarifas |
| Implantación TicketBAI/Verifactu | **no público** (partner + posible hardware) |

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos | Mejor para |
|---------|----------|------------|
| **Facturación pyme cloud** | Holded, Contasimple, FacturaDirecta | Honorarios 6831 |
| **Suite asesorial** | A3 facturación | Quien ya vive en ecosistema asesor |
| **ERP** | Sage, Exact, Odoo | Volumen / grupos |
| **Facturar desde CRM** | Algunos verticales | Pocas facturas; riesgo de no cumplir SIF |

Honorarios vs alquileres: los segundos exigen **recurrencia, recibos y impagos** (más cerca de PMS); los primeros son eventos. Mezclar ambos en Excel es fuente de error.

---

## 10. Nivel de adopción + confianza

Facturación digital: **habitual**. Herramienta concreta: sin censo. Relación con ERP INE: parcial. **[Media]**

---

## 11. Nivel de madurez + justificación

**Digitalizada** generalizada. **Automatizada** (CRM→factura→banco) minoritaria. Presión regulatoria (Verifactu/TicketBAI) empuja madurez del software de facturación. **[Media]**

---

## 12. Validación

- Actualizar calendario Verifactu/TicketBAI en cada revisión (no hardcodear fechas dudosas).
- Verificar precios Holded/Contasimple/FacturaDirecta en URL oficial antes de citar €.
- Distinguir factura de honorarios vs recibo de renta.

---

← [Contabilidad](contabilidad.md) | [Índice](../README.md) | [Siguiente: Bancos →](bancos.md)
