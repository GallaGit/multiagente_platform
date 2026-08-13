# Contabilidad

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria (honorarios, gastos, impuestos)

---

## 1. Función principal / problema que resuelve

Llevar el **registro contable** (PGC), impuestos y reporting financiero legal. En la mayoría de micro/pequeñas agencias la contabilidad oficial vive en la **asesoría externa**; internamente hay Excel + herramienta de facturación.

**Capacidad anunciada (suites):** asientos, IVA, modelos, analítica.  
**Integración disponible:** importación de facturas, bank feed, puentes A3.  
**Uso real:** asesoría + extractos; ContaPlus legacy en transición a A3/cloud. **[Media]**

---

## 2. Usuarios

Asesoría/gestoría; admin interna; dirección (P&L resumido); auditores en redes grandes.

---

## 3. Momento del flujo operativo

Continuo mensual/trimestral: facturas → asientos → modelos fiscales → cierre anual. Desacoplado del ritmo diario de visitas del CRM.

---

## 4. Información gestionada

Plan contable, diario, IVA soportado/repercutido, IRPF, inmovilizado (si aplica), conciliaciones, reporting a socios.

Datos de **arras en custodia** deben distinguirse de ingresos por honorarios (error frecuente en Excel).

---

## 5. Integraciones

| Origen/destino | Tipo |
|----------------|------|
| Facturación (Holded, Contasimple, etc.) | Nativa / export |
| Banca | Nativa PSD2 / ficheros / manual |
| CRM | Manual / inexistente |
| Nóminas | Módulo A3 u otro |
| AEAT | Presentación vía asesoría / software |

---

## 6. Flujo de datos (ASCII)

```text
[Facturas honorarios / gastos] --> [Facturación SaaS o Excel]
              |                           |
              v                           v
        [Asesoría / A3] <---export---- [Admin agencia]
              |
              +--modelos--> [AEAT]
              |
              +--informes--> [Dirección]
```

---

## 7. Limitaciones y tareas humanas

- Desfase CRM (operaciones) vs libros (cobrado).
- Clasificación errónea de cobros de clientes (arras vs comisión).
- ContaPlus legacy: riesgo de obsolescencia / migración.
- Coste oculto: horas de “enviar Excel al gestor”.

---

## 8. Costes

| Enfoque | Precio |
|---------|--------|
| A3 (Wolters Kluwer) | **no público** homogéneo (canal partner + asesoría) |
| ContaPlus (legacy) | Histórico; no usar precios de foros |
| Holded (contabilidad en suite) | Ver planes públicos Holded — no inventar |
| Asesoría externa | **no público** (cuota mensual variable por volumen) |
| Excel | Licencia Office/Workspace ya existente |

---

## 9. Competencia / enfoques

| Enfoque | Quién | Lógica |
|---------|-------|--------|
| **Asesoría + A3** | Dominante pyme ES | Cumplimiento; la agencia no “tiene contable” |
| **Suite all-in-one** | Holded (y similares) | Facturación+contabilidad en la empresa |
| **ERP mid-market** | Sage, Exact | Medianas con controlador |
| **Excel-first** | Micros | Frágil; cierra con gestor a final de trimestre |

Comparar por **quién es el sistema de registro fiscal** (asesoría vs in-house), no por marca sola.

---

## 10. Nivel de adopción + confianza

Contabilidad formal: **obligada** (uso 100% legal vía alguien). Software propio vs externalizado: sin % público inmobiliario. Relacionable con INE ERP 60,6% ≥10 (CNAE 68), sin igualar “ERP = contabilidad in-house”. **[Media]**

---

## 11. Nivel de madurez + justificación

**Digitalizada** vía asesoría. **Automatizada** solo con bank feed + reglas + API facturación. Madurez baja en vínculo operación-comercial. **[Media]**

---

## 12. Validación

- No citar precios ContaPlus de mercado secundario.
- Validar en campo: % agencias con Holded contable vs solo facturación.
- Cruzar con [facturacion.md](facturacion.md) y [bancos.md](bancos.md).

---

← [Firma](firma-electronica.md) | [Índice](../README.md) | [Siguiente: Facturación →](facturacion.md)
