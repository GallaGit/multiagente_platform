# KYC, AML y compliance

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** PBC/FT · sujetos obligados · herramientas KYC · RGPD asociado

---

## 1. Función principal

Identificar al cliente, titular real y origen de fondos cuando la agencia actúa como **sujeto obligado** en prevención de blanqueo, conservar documentación y reportar indicios a SEPBLAC. En paralelo: bases RGPD para tratar datos de leads y clientes. No es un “extra comercial”: es obligación legal en el perímetro definido por la norma.

---

## 2. Usuarios

Responsable PBC / titular de agencia, agentes (recogida documental), compliance externo, SEPBLAC (destino de comunicaciones), notaría (control en cierre, distinto rol), proveedores KYC (ID, screening listas).

---

## 3. Momento del flujo

Desde captación seria / mandato y, en todo caso, antes de intermediación de compraventa con las obligaciones aplicables; actualización en cambios de intervinientes; archivo post-operación (plazos legales). En alquiler: umbrales específicos.

---

## 4. Información gestionada

- DNI/NIE/pasaporte, poderes, estructura societaria, titular real
- Declaración origen de fondos / mediación
- Resultados screening (sanciones, PEP) si se usa herramienta
- Expediente PBC, alertas, reportes
- Consentimientos y bases RGPD / LSSI (marketing vs operación)

Marco: [Ley 10/2010](https://www.boe.es/buscar/act.php?id=BOE-A-2010-6737). Compraventa: intermediarios obligados; alquiler si renta ≥ **10.000 €/mes** o **120.000 €/año** (umbrales de la ley). Conservación: **10 años**. **[Alta]**

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| KYC SaaS ↔ CRM | API / nativa / manual | Capacidad selectiva |
| Verificación documental (OCR/NFC) | API proveedor | |
| Screening listas PEP/sanciones | API | |
| CRM “checklists” PBC | Nativa | A menudo sin screening real |
| Firma electrónica de declaraciones | Nativa / API | |
| SEPBLAC | Portal / procedimientos oficiales | No es integración CRM típica |
| Portales | Inexistente para KYC | Lead ≠ cliente identificado |

---

## 6. Flujo de datos (ASCII)

```text
Lead / mandato
     │
     ▼
¿Sujeto obligado aplica? ──no──► RGPD mínimo / archivo comercial
     │ sí
     ▼
KYC (ID + titular real + fondos)
     │
     ├─► Tool KYC / checklist CRM / PDF carpeta
     ├─► Alertas → análisis → SEPBLAC si procede
     └─► Archivo 10 años
              │
              ▼
        Operación / notaría (controles propios)
```

---

## 7. Limitaciones y tareas humanas

- Microagencias: cumplimiento irregular o delegado a gestoría; riesgo sancionador. **[Media]**
- Confundir “tener DNI en el Drive” con expediente PBC completo.
- Tools KYC no eximen de análisis del riesgo ni de formación.
- Separar base jurídica comercial (lead) vs diligencia debida (cliente).
- Capacidad anunciada de CRM “AML ready” ≠ supervisión efectiva.

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Expediente manual (carpeta/Drive) | Coste = tiempo interno (no tarifa software) |
| KYC SaaS / screening | **no público** / bajo presupuesto (B2B) |
| Firma electrónica (declaraciones) | Ej. Signaturit Business **35 €/usuario·mes** (anual) / Business+ **57 €** — [Signaturit](https://www.signaturit.com/es/precios/) · **[Alta]**; no es producto AML completo |
| Consultoría PBC / DPD | no público |
| Sanciones | Régimen Ley 10/2010 (no “precio de software”) |

---

## 9. Competencia / enfoques comparados

| Enfoque | Cobertura | Riesgo residual |
|---------|-----------|-----------------|
| Carpeta documental + Excel | Mínimo viable | Olvidos, sin screening |
| Checklist en CRM inmobiliario | Trazabilidad operativa | Puede carecer de listas/PEP |
| Suite KYC/AML horizontal | ID + screening + audit log | Integración CRM y coste |
| Externalización a despacho | Expertise | Latencia; datos fuera |
| “Lo hace el notario” | Falso alivio | Obligaciones propias del intermediario |

Franquicias: a veces protocolo central + tool; el sujeto obligado local sigue siendo la agencia. **[Alta]** · contexto en `Situacion_en_España/Franquicias_y_comparación_global.md`

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| Conciencia formal AML en compraventa | Habitual–muy extendida (obligación) | Alta norma; Media praxis |
| Software KYC dedicado en micro | Poco utilizada | Baja |
| Protocolo franquicia | Habitual en redes | Media |
| Tasa de incumplimiento / sanciones sector | No usada aquí como serie (hueco) | — |

---

## 11. Madurez + justificación

Uso típico micro: **Tradicional/Digitalizada** (PDF + Drive).  
Medianas con tool: **Digitalizada**, rara vez **Automatizada** end-to-end (onboarding → screening → archivo).  
IA de lectura documental: capacidad emergente; no madurez media del tejido. **[Media]**

---

## 12. Validación

| Ítem | Evidencia | Pendiente |
|------|-----------|-----------|
| Umbrales alquiler y archivo 10 años | Ley 10/2010 **[Alta]** | Reformas posteriores a vigilar |
| Precios Signaturit | Página oficial | — |
| % agencias con tool KYC | — | Encuesta |
| Cobertura real de módulos “PBC” en CRM ES | — | Revisión por fabricante |

---

← [Datos geo](datos-geoespaciales.md) | [Índice](../README.md) | [Siguiente: Postventa →](coordinacion-postventa.md)
