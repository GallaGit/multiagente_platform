# Bancos / tesorería y cobros

**Corte:** agosto de 2026 · **Ámbito:** España · open banking, conciliación, arras y custodia

---

## 1. Función principal / problema que resuelve

Canal crítico de **cobros de honorarios, rentas, señales/arras y pagos a colaboradores**. No es un “sistema core de producto” de la agencia (no gestiona inmuebles ni leads), pero **sin banca operativa no hay liquidación**.

**Capacidad anunciada (open banking/PSD2):** agregación de cuentas, iniciación de pagos, conciliación automática en Holded y similares.  
**Integración disponible:** AIS/PIS vía TPPs; bank feed en facturación.  
**Uso real:** transferencias SEPA + conciliación manual o semi; custodia de arras con rigor variable. **[Media]**

---

## 2. Usuarios

Admin/tesorería; dirección; agentes (solo “¿ha entrado la transferencia?”); asesoría; en grandes, controller.

---

## 3. Momento del flujo operativo

Todo el ciclo: reserva/arras → pago de comisión → pagos split multiagente → rentas mensuales (si PMS) → impuestos. Picos en firmas de arras y escrituras.

---

## 4. Información gestionada

IBAN, titulares, extractos, conciliaciones, referencias de transferencia, estados de cobro, (idealmente) **cuenta separada / control de fondos de terceros** para arras.

Datos bancarios de clientes = alta sensibilidad RGPD.

---

## 5. Integraciones

| Destino | Tipo |
|---------|------|
| Holded / facturación cloud | Nativa open banking / bank feed |
| Contabilidad A3/Sage | Ficheros / API / manual |
| PMS alquiler | Remesas SEPA / nativa |
| CRM | Inexistente / nota manual “cobrado” |
| Pasarelas tarjeta | Raro en honorarios; más en proptech alquiler |

---

## 6. Flujo de datos (ASCII)

```text
[Cliente] --transferencia SEPA--> [Cuenta agencia / custodia]
                                         |
                                         v
                              [Extracto / open banking]
                                         |
                    +--------------------+--------------------+
                    v                                         v
            [Conciliación Holded/ERP]                 [Excel / ojo humano]
                    |
                    v
            [Marca cobrado en factura] --(manual)--> [CRM estado]
```

---

## 7. Limitaciones y tareas humanas

- Identificar transferencias sin concepto claro (“casa Calle X”).
- Mezclar fondos propios y de terceros (riesgo operativo/legal).
- PSD2: consentimientos, caducidad de conexiones, bancos no soportados.
- Cheques/efectivo residuales en algunos mercados locales.
- No es sustituible por el CRM: el dinero vive en el banco.

---

## 8. Costes

| Concepto | Precio |
|----------|--------|
| Cuentas/comisiones bancarias empresa | **no público** homogéneo (tarifa por entidad) |
| Open banking embebido en Holded/etc. | Suele ir en el plan SaaS — ver fabricante |
| TPP / iniciación de pagos standalone | **no público** típico para agencia |
| Tiempo de conciliación manual | No tarifado; coste operativo real |

---

## 9. Competencia / enfoques

| Enfoque | Lógica | Fricción |
|---------|--------|----------|
| **Banco tradicional + Excel** | Default micro | Error humano, lentitud |
| **Facturación con bank feed** (Holded…) | Conciliación semi-auto | Sigue faltando vínculo CRM |
| **PMS + remesas** | Alquileres | Poco útil solo para 6831 venta |
| **Custodia / cuenta de clientes** | Buena práctica arras | Disciplina interna; a veces notarial/terceros |

No hay “banco inmobiliario” dominante: compiten **procesos de tesorería**, no marcas PropTech de banca.

---

## 10. Nivel de adopción + confianza

Uso de banca: universal. Open banking en agencias: **emergente/habitual-baja** según herramienta de facturación. Sin estadística INE específica “PSD2 en CNAE 68”. **[Media-baja]**

---

## 11. Nivel de madurez + justificación

Infraestructura bancaria: madura. Proceso agencia: mayoritariamente **digitalizado** (banca online) con conciliación **tradicional/manual**. Automatizada solo con bank feed disciplinado. **[Media]**

---

## 12. Validación

- No inventar comisiones de transferencias ni % de adopción PSD2.
- Documentar políticas de custodia de arras en casos reales (pendiente).
- Cruzar con facturación y PMS.

---

← [Facturación](facturacion.md) | [Índice](../README.md) | [Siguiente: Portales →](../03_canales_y_productividad/portales-inmobiliarios.md)
