# Costes y TCO por arquetipo

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Principio:** solo componentes **documentados**; el resto se marca **no público / pendiente**.  
**No se usa** el ROI de `analisis_del_mercado/context.md` como hecho.

---

## 1. Marco TCO (recordatorio)

| Componente | Observabilidad |
|------------|----------------|
| Licencia / SaaS | A veces pública |
| Implantación / migración | Suele ser presupuesto |
| Integraciones (API, iPaaS) | Variable |
| Canales (portales, ads, WA API) | Portales: **opacos** |
| Operación (tiempo agentes, admin) | Rara vez cuantificado |
| Cumplimiento (firma, KYC, backups) | Parcial |
| Cambio / salida | Casi nunca publicado |

Metodología: [metodologia-costes.md](../00_metodologia/metodologia-costes.md).

---

## 2. Anclas de precio público (ago. 2026)

| Concepto | Importe documentado | Fuente | Confianza |
|----------|---------------------|--------|-----------|
| Inmovilla Full Edition | **79 €/mes** (≤7 usuarios); **+12 €/usuario** | [Inmovilla](https://inmovilla.com/precios/) | **[Alta]** |
| Signaturit Business | **35 €**/usuario·mes (pago anual) | [Signaturit](https://www.signaturit.com/es/precios/) | **[Alta]** |
| Signaturit Business+ | **57 €**/usuario·mes (pago anual) | Idem | **[Alta]** |
| Witei | Freemium + planes; cifras web **variables** | [Witei](https://get.witei.com/es/precios-crm/) | **[Media]** |
| Packs Idealista / Fotocasa / Habitaclia / Pisos.com | **No público** | Hueco declarado | **[Alta sobre el hueco]** |
| Idealista Tools Office | **No publicado** en ficha de ayuda consultada | Idealista Tools | **[Media]** |
| Holded / Contasimple / A3 | Planes o partner — **no fijar €** aquí sin captura | Fabricantes | — |
| WhatsApp Business App | Gratuita (app) | Meta | **[Alta]** |
| WhatsApp Cloud API / BSP | Tarifa Meta por conversación + margen BSP — **sin pack «agencia ES»** | Meta pricing | **[Media]** |
| Salesforce / HubSpot (pack inmobiliaria ES) | **No público** | — | — |
| Implantación / migración CRM | **No público** | — | — |

---

## 3. Lectura cualitativa dominante

En muchas agencias el **coste tecnológico dominante no es la cuota del CRM**, sino:

1. **Portales** (packs/destacados bajo presupuesto)  
2. **Tiempo humano** en herramientas desconectadas (copiar leads, WhatsApp fuera del CRM, Excel de comisiones)

Evidencia: observación sectorial + metodología del módulo. Cuantificación agregada **no pública**. **[Media-baja]**

El ancla Inmovilla (79 €/mes) ilustra un SaaS CRM asequible frente a partidas de canal **opacas** y de mayor peso relativo percibido. **No** se deduce un ratio numérico sin contabilidad anonimizada.

---

## 4. TCO por arquetipo — solo documentado

Leyenda: **D** = dato público · **NP** = no público · **Cual.** = cualitativo

### 4.1 Micro (1–5 personas)

| Componente | Estado | Nota |
|------------|--------|------|
| CRM (si existe) | D / NP | Witei freemium o Tools **NP**; alternativa Excel = 0 licencia |
| Portales (1–2) | **NP** | Partida percibida crítica |
| WhatsApp App | D (0 € app) | Coste oculto = tiempo agente |
| Email / Workspace o M365 | D parcial | Según plan Google/Microsoft (no detallar € sin ficha) |
| Firma puntual | D si Signaturit | 35/57 € usuario·mes si adoptan ese plan |
| Facturación | NP / web | Contasimple/Holded: consultar web |
| Asesoría | **NP** | Suele superar SaaS CRM en peso |
| Integraciones iPaaS | NP / 0 | Frecuente: manual |

**TCO numérico agregado:** **no calculable** con fuentes públicas.  
**Perfil:** bajo SaaS visible; alto coste de canal + fricción operativa. **[Media]**

### 4.2 Mediana

| Componente | Estado | Nota |
|------------|--------|------|
| CRM vertical | D posible | p. ej. Inmovilla **79 €/mes** (+ extras) |
| Multi-portal | **NP** | Suele ser > CRM en percepción de gasto |
| Firma | D posible | Signaturit 35/57 € |
| WhatsApp | App 0 € o API **NP** | API + BSP bajo presupuesto |
| Facturación / Holded | Web / NP | Separado del CRM |
| Automatización Make/Zapier | NP | Puntal |
| Formación / admin CRM | **NP** (tiempo) | Coste oculto |

**Lectura:** CRM documentable; **TCO real incompleto** sin tarifas portal. **[Media]**

### 4.3 Grande / brokerage

| Componente | Estado | Nota |
|------------|--------|------|
| CRM enterprise o vertical + middleware | **NP** | Licencia + impl. |
| ERP / finance | **NP** | Relacionable con INE ERP 60,6% (≥10 emp.) — no = coste |
| BI / data | **NP** | INE BI 16,1% ≥10 — adopción, no precio |
| IAM / SSO / DLP | **NP** | |
| Portales + web + partners | **NP** | |
| IA (Copilot / genAI) | NP / licencia M365 | CBRE: 71% IA gen. en muestra grandes — no coste |

**TCO:** dominado por impl., middleware y personal tech — **sin cifras públicas sectoriales**. **[Media-baja]**

### 4.4 Franquicia

| Componente | Estado | Nota |
|------------|--------|------|
| CRM / MLS de red | **NP** | A menudo en cánones / pack franquiciador |
| Portales | **NP** | Local ± centralizado |
| Royalties / brand tech | **NP** | Fuera de software puro |
| Shadow IT (WA, Excel splits) | Cual. | Coste de riesgo, no factura |

Pendiente: TCO franquicia (cánones tech vs software propio). · Metodología §6.

### 4.5 PropTech / digital-first

| Componente | Estado | Nota |
|------------|--------|------|
| Ingeniería / CRM propio | **NP** | Capex/opex producto |
| Cloud / data / IA | **NP** | |
| Portales | Variable / **NP** | Canal secundario o supply |

PwC ~**700 PropTech** (2025): recuento de empresas ≠ gasto medio de agencia. **[Media]**

---

## 5. Qué NO se incluye como hecho

- ROI 5,36:1 ni % leads perdidos de `context.md`  
- «Precio medio Idealista Gold / Fotocasa Premium» de blogs  
- Extrapolación Inmovilla 79 € → TCO total de la agencia  
- Estimaciones de migración CRM en € sin fuente  

---

## 6. Pendientes de investigación

1. Tarifas reales de portales por provincia/pack  
2. Coste Idealista Tools / Office  
3. Factura típica WA API + BSP en agencias ES  
4. Horas/€ de migración CRM  
5. Contabilidad anonimizada: ratio portales / CRM / tiempo  

---

## 7. Validación

| Ítem | Confianza |
|------|-----------|
| Anclas Inmovilla / Signaturit | **[Alta]** |
| Portales = partida mayor cualitativa | **[Media-baja]** |
| TCO numérico por arquetipo | **No disponible** — correcto dejarlo abierto |

---

← [Comparativa proveedores](comparativa-proveedores.md) | [Índice](../README.md) | [Siguiente: Adopción y madurez →](adopcion-madurez-arquetipos.md)
