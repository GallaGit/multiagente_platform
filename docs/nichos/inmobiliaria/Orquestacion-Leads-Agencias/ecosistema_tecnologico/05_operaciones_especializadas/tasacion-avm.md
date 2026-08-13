# Tasación y AVM

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Sociedades de tasación BdE · AVM PropTech · idealista/data

---

## 1. Función principal

Estimar el valor de un inmueble. Distinguir:

1. **Tasación homologada** (Orden ECO/805/2003 y marco Rd 775/1997): válida para finalidades financieras/hipotecarias cuando la emite sociedad inscrita en el Banco de España.  
2. **AVM / valoración automatizada u orientativa**: apoyo a captación, pricing de anuncio o carteras; **no sustituye** por sí sola la tasación hipotecaria presencial regulada. **[Alta]**

---

## 2. Usuarios

Banco (expediente hipoteca), sociedad de tasación, comprador/vendedor, agente (argumentario de precio), fondos/servicers (AVM de cartera), idealista/data y otros proveedores de datos.

---

## 3. Momento del flujo

- **Captación:** valoración orientativa / comparables.  
- **Hipoteca:** tasación oficial post-arras/pre-escritura.  
- **Carteras institucionales:** AVM recurrente (uso no típico de microagencia).

---

## 4. Información gestionada

- Características del inmueble, visita técnica (tasación ECO), fotos, comparables
- Informe de tasación, valor de seguro, condicionantes
- En AVM: inputs catastrales/oferta/transacciones modelizadas, score de confianza
- idealista/data: testigos, métricas de zona, widgets/API (B2B)

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Banco ↔ tasadora | Nativa / portal | Flujo hipotecario |
| Agencia ↔ tasadora | Manual (pedido) | Agente no “emite” tasación ECO |
| AVM web (ST, Tinsa, portales, PropTech) | Nativa web / API | Orientativo |
| idealista/data API / widgets | API / nativa B2B | Precio **no público** |
| CRM agencia ↔ AVM | Manual / API rara | |
| Catastro → AVM | API / datos abiertos (inputs) | Ver ficha geo |

---

## 6. Flujo de datos (ASCII)

```text
[Captación]
Agente ──comparables/AVM orientativo──► precio de anuncio
                │
                ▼
[Hipoteca]
Banco ──encarga──► Sociedad tasación BdE ──informe ECO──► Banco
                │
                └──► Agencia / comprador (resultado)

[Datos B2B]
idealista/data / PropTech AVM ──API/fichero──► CRM / pricing tool
```

---

## 7. Limitaciones y tareas humanas

- Solo sociedades del [registro BdE](https://sedeelectronica.bde.es/sede/es/tramites/homologacion-sociedades-tasacion-servicios-p22.html) para efectos del RD 775/1997. **[Alta]**
- AVM ≠ tasación hipotecaria; confundirlos es riesgo comercial y de compliance.
- El agente sigue haciendo “pricing” humano con portales + experiencia.
- Condicionantes del informe (obras, ocupación) requieren lectura humana.
- Cuotas de mercado de tasadoras en blogs: tratar con cautela si no hay ranking auditado citado con metodología. **[Media-baja]**

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Informe tasación hipotecaria | Precio al particular/banco: **no público homogéneo** (por tipología/ubicación) |
| AVM / widgets idealista/data | **no público** (contacto comercial) · [idealista/data](https://www.idealista.com/data/) · **[Alta sobre el hueco]** |
| Consultas Catastro básicas | Gratuita / tasas según servicio (ver Sede Catastro) |
| Valoraciones online gratuitas de portales/tasadoras | Freemium marketing; condiciones en cada web |

No inventar “precio medio de tasación en España”.

---

## 9. Competencia / enfoques comparados

| Enfoque | Validez típica | Usuario primario |
|---------|----------------|------------------|
| Sociedad homologada BdE (visita + ECO) | Hipoteca / finalidades reguladas | Banco |
| AVM de tasadoras | Carteras, actualización garantías (marco supervisor en evolución) | Banca / institucionales |
| idealista/data / portales | Pricing, testigos, estudios | Agencias, inversores, tech |
| Comparables manuales del agente | Captación diaria | Agencia |
| RICS / valuation advisory | Inversión/comercial | Consultoras |

Enfoques distintos: **no son sustitutos** en hipoteca residencial. **[Alta]**

---

## 10. Adopción + confianza

| Práctica | Adopción en agencias | Confianza |
|----------|----------------------|-----------|
| Pedir/recibir tasación en ventas con hipoteca | Muy extendida (proceso banco) | Alta |
| AVM embebido en CRM | Poco utilizada / emergente | Baja |
| idealista/data de pago | Nicho (medianas+ / PropTech) | Media |
| Valoración “de portal” gratuita en captación | Habitual | Media |

---

## 11. Madurez + justificación

Proceso hipotecario: **Digitalizada** (encargos electrónicos) con núcleo técnico regulado.  
Pricing de agencia: mezcla **Tradicional** (criterio) + **Digitalizada** (portales).  
AVM industrial: más maduro en banca que en microagencia. Uso típico agencia: **Digitalizada**. **[Media]**

---

## 12. Validación

| Ítem | Evidencia | Pendiente |
|------|-----------|-----------|
| Homologación BdE / ECO 805 | BOE / sede BdE | — |
| Precio API idealista/data | Hueco declarado | Solicitar tarifa |
| Orden ECM/599/2025 y circular AVM | Seguir desarrollo supervisor | Lectura jurídica actualizada |
| % captaciones con AVM formal | — | Encuesta |

---

← [Software hipotecario](software-hipotecario.md) | [Índice](../README.md) | [Siguiente: Datos geo →](datos-geoespaciales.md)
