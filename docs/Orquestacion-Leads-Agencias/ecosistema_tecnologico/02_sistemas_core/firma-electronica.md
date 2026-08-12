# Firma electrónica

**Corte:** agosto de 2026 · **Ámbito:** España · encargos, arras, alquileres (no escritura ordinaria por videoconferencia general)

---

## 1. Función principal / problema que resuelve

Capturar **consentimiento firmado** con evidencia (quién, cuándo, qué documento), reduciendo papel y desplazamientos en documentos pre-notariales y contratos de intermediación/alquiler.

Marco: **eIDAS** (SES / AES / QES); **Ley 6/2020** de servicios electrónicos de confianza; **Ley 11/2023** (digitalización notarial — la compraventa ordinaria **no** se generaliza como escritura por videoconferencia para el público general). **[Alta]**

**Capacidad anunciada:** firma simple/avanzada/cualificada, plantillas, API, OTP.  
**Integración disponible:** CRM connectors, Zapier/Salesforce (p. ej. Signaturit Business+), API Enterprise.  
**Uso real:** creciente en encargos/arras/alquiler; escritura sigue notarial presencial/régimen legal aplicable. **[Media]**

---

## 2. Usuarios

Agentes/back-office (envían); propietarios e inquilinos/compradores (firman); legal interno; notaría (fuera del circuito SES típico de la agencia).

---

## 3. Momento del flujo operativo

Encargo/exclusiva → reserva/arras → anexo → contrato de alquiler → occasionally NDAs o encargos de hipoteca. **No** sustituye la escritura pública en el régimen general.

---

## 4. Información gestionada

PDF/contratos, metadatos de firma, evidencias/audit trail, identidad (OTP, biometría, certificado), a veces documentos adjuntos del firmante.

---

## 5. Integraciones

| Destino | Tipo |
|---------|------|
| CRM inmobiliario | Nativa / API / manual (descarga PDF) |
| Drive / documental | Manual / automatización |
| Email | Nativa (canal de envío) |
| Autofirma / certificados FNMT | Flujo distinto (empleado/AAPP); no “DocuSign-like” |
| ERP/facturación | Inexistente / irrelevante |

---

## 6. Flujo de datos (ASCII)

```text
[Plantilla / PDF en CRM o Drive]
            |
            v
     [Proveedor firma] --email/SMS--> [Firmante(s)]
            |
            +--evidencia + PDF firmado--> [Carpeta operación]
            |
            v
     [Archivo CRM / email]     [Notaría: circuito aparte]
```

---

## 7. Limitaciones y tareas humanas

- Elegir nivel SES/AES/QES adecuado al riesgo del documento.
- Identidad débil (solo email) en operaciones de alto valor.
- Clientes sin smartphone/digital skills.
- Confusión legal: “firmado electrónicamente” ≠ escritura.
- Autofirma/FNMT: útil para trámites con certificado, no UX de consumidores masivos.

---

## 8. Costes

| Proveedor | Precio público (pago anual, por usuario·mes) | Fuente |
|-----------|-----------------------------------------------|--------|
| **Signaturit** Business | **35 €** | [signaturit.com/es/precios](https://www.signaturit.com/es/precios/) · ago. 2026 · **[Alta]** |
| **Signaturit** Business+ | **57 €** | Idem · **[Alta]** |
| Signaturit Enterprise | **no público** (volumen) | Idem |
| DocuSign, Yousign | Planes públicos globales variables; **verificar web** — no fijar aquí sin captura | — |
| Autofirma / FNMT | Certificado: tasas FNMT / entidad; herramienta Autofirma gratuita | Contexto AAPP |

Límites de envíos/créditos según plan (Signaturit: p. ej. 60/240 envíos año en Business/Business+ anuales). **[Alta]**

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos | Encaje |
|---------|----------|--------|
| **Prestador cloud ES/EU** | Signaturit (Namirial) | UX + eIDAS; precios claros |
| **Global enterprise** | DocuSign | Multinacionales; coste/integración |
| **EU challenger** | Yousign | Similar a Signaturit en pyme EU |
| **Certificado local** | Autofirma + FNMT/otros PSC | Trámites cualificados; mala UX consumidor |
| **Firma en portal/CRM** | Módulos embebidos | Conveniente; auditar nivel eIDAS |

Comparar por **nivel de firma + evidencia + integración CRM**, no solo marca.

---

## 10. Nivel de adopción + confianza

Habitual creciente en medianas; irregular en micro (PDF escaneado / presencial). % sectorial **no publicado** por INE. **[Media-baja]**

---

## 11. Nivel de madurez + justificación

Herramientas: maduras (eIDAS). Uso agencia: **digitalizada** con bolsas de **tradicional**. Automatización CRM→firma→archivo: minoritaria. **[Media]**

---

## 12. Validación

- Precios Signaturit verificados en página oficial (ago. 2026).
- Ley 11/2023: no afirmar escritura general por videoconferencia.
- Pendiente: tasa real de arras firmadas electrónicamente por provincia.

---

← [Documental](gestores-documentales.md) | [Índice](../README.md) | [Siguiente: Contabilidad →](contabilidad.md)
