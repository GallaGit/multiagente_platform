# Dependencias y sustituibilidad

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Objetivo:** distinguir qué es **crítico** (difícil operar sin ello) de qué es **sustituible** (con coste, tiempo o riesgo). Sin recomendar proveedores.

---

## 1. Criterios

| Etiqueta | Definición operativa |
|----------|----------------------|
| **Crítico** | Sin ello se pierde demanda, conversación o cumplimiento esencial |
| **Sustituible con coste** | Hay alternativas, pero migración/formación/lock-in son caros |
| **Sustituible fácil** | Cambio de herramienta con bajo riesgo de negocio |
| **Socialmente crítico** | El cliente o el mercado imponen el canal, más allá del software |
| **Regulatoriamente anclado** | Marco legal limita la sustitución digital |

---

## 2. Mapa de dependencias

| Sistema / canal | Criticidad | Sustituibilidad | Notas |
|-----------------|------------|-----------------|-------|
| **Portales** (Idealista, Fotocasa, etc.) | **Crítica** | Baja | Escaparate de demanda; particular compite en el mismo canal (CNMC). Sin cuota % pública. |
| **WhatsApp** | **Crítica socialmente** | Muy baja a corto plazo | Cliente espera chat; app ≠ API. Histórico en móvil = riesgo. |
| **Email** | Crítica (identidad + leads + contratos) | Baja | Identidad profesional y canal formal. |
| **Teléfono / VoIP** | Alta | Media | Sustituible de operador; no del canal voz. |
| **CRM** | Alta operativa (mediana+) | **Sustituible con coste** | Inventario/pipeline; migración y re-captura **no cuantificadas públicamente**. |
| **Idealista Tools** | Alta si el stack es Idealista-céntrico | Baja dentro del ecosistema portal | Precio **no público**; dependencia de canal. |
| **MLS / red franquicia** | Alta en redes | Baja (lock-in de red) | Salir = pérdida de colaboración/brand. |
| **Firma electrónica** | Media-alta (creciente) | Media | Signaturit/DocuSign/Yousign/módulo CRM intercambiables a nivel SES/AES; auditar eIDAS. |
| **Facturación SaaS** | Media | Media-alta | Holded ↔ Contasimple ↔ asesoría; puente fiscal. |
| **Contabilidad / A3 vía gestoría** | Alta cumplimiento | Baja de *función*; media de *software* | La obligación fiscal no se sustituye; el software sí vía partner. |
| **Google Workspace / M365** | Alta productividad | Media | Cambio de suite costoso en hábitos. |
| **Drive / carpetas** | Alta de facto | Media | Sustituible de tool; no del hábito documental. |
| **BI dedicado** | Baja en micro; media en grande | Alta (Excel→BI) | INE BI **16,1%** ≥10 emp. |
| **IA genérica (ChatGPT etc.)** | Baja operativa | Alta | Informal; no sistema de registro. |
| **Notaría / escritura** | Crítica legal | **Anclada** | Ley 11/2023: compraventa ordinaria no generalizada por videoconferencia. **[Alta]** |
| **Bancos / cobro honorarios** | Crítica cobro | Baja de función | Conciliación software sí; entidad bancaria es decisión aparte. |

---

## 3. Críticas vs sustituibles (síntesis)

### Críticas (si fallan, se para o se degrada el negocio)

```text
Portales ──► demanda / leads
WhatsApp ──► conversación comercial (social)
Email     ──► identidad + leads + documentos
Cobro     ──► facturación ↔ banco
Cumplimiento fiscal / AML según caso
```

### Sustituibles con coste

```text
CRM vertical A ↔ CRM vertical B ↔ (grande) Salesforce/HubSpot
Firma proveedor X ↔ Y (mismo nivel eIDAS)
Facturación Holded ↔ Contasimple ↔ módulo asesor
iPaaS Make ↔ Zapier ↔ n8n
```

Coste típico no publicado: export limitado, re-alta de inmuebles, formación, pérdida de histórico, conectores a rehacer. **[Media-baja sobre magnitud]**

### Fácilmente sustituibles (relativo)

- Plantillas Word; herramientas puntuales de copy  
- Chat IA informal (cambiar de marca de LLM)  
- Calendario (Google ↔ Outlook) con fricción media-baja  

---

## 4. Triple dependencia estructural

```text
[Portales]     concentran DEMANDA
[CRM]          concentra INVENTARIO + contactos (si se usa)
[WhatsApp]     concentra CONVERSACIÓN
```

Ninguno sustituye a los otros. La fricción nace de esa **triple dependencia** (README del módulo). **[Media-alta]**

| Componente | ¿Se puede «apagar»? |
|------------|---------------------|
| Portales | En intermediación residencial típica: **casi no** sin perder demanda |
| CRM | Sí (volver a Excel/Tools); coste en trazabilidad y escala |
| WhatsApp | Teóricamente sí (solo email/tel); en práctica **rechazo de cliente** |

---

## 5. Dependencias por arquetipo

| Arquetipo | Crítico adicional | Sustituibilidad del core |
|-----------|-------------------|--------------------------|
| Micro | Portales + WA + email | CRM opcional / Tools |
| Mediana | + CRM vertical | Cambio CRM doloroso pero posible |
| Grande | + ERP/IAM/middleware | Core más rígido; apps periféricas más flexibles |
| Franquicia | Stack de red | Baja mientras dure el contrato |
| PropTech | Producto propio | Portales a veces secundarios |

---

## 6. Precios y lock-in (solo hechos documentados)

| Hecho | Implicación de dependencia |
|-------|----------------------------|
| Inmovilla **79 €/mes** público | Cuota CRM visible ≠ coste de salida |
| Signaturit **35/57 €** | Firma sustituible; coste de cambio bajo vs CRM |
| Portales **sin tarifa pública** | Dependencia opaca: difícil comparar TCO de canal |
| Witei freemium / precios variables | Entrada fácil; evaluar exportación antes de crecer |

---

## 7. Validación

| Afirmación | Confianza |
|------------|-----------|
| Portales críticos cualitativamente | **[Alta]** |
| WA crítico socialmente | **[Media-alta]** |
| CRM sustituible con coste | **[Media]** |
| Coste € de migración | **No público** |

---

← [Puntos de fricción](puntos-de-friccion.md) | [Índice](../README.md) | [Siguiente: Vacíos tecnológicos →](vacios-tecnologicos.md)
