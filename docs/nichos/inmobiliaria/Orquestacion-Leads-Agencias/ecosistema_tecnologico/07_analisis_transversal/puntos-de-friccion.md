# Puntos de fricción

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Orden:** por **impacto percibido** en operación e ingreso (cualitativo). Sin proponer remedios de producto.

---

## 1. Criterios de priorización

| Criterio | Pregunta |
|----------|----------|
| **Impacto** | ¿Cuánto afecta a cierre, tiempo o calidad del dato? |
| **Frecuencia** | ¿Cuántas veces al día/semana ocurre? |
| **Riesgo ingreso / datos** | ¿Pierde lead/comisión o expone datos personales? |
| **Sustituibilidad** | ¿Hay alternativa realista sin romper el negocio? |

Escala cualitativa: Alto / Medio / Bajo. Confianza global: **media** (síntesis de fichas + mapa de integraciones; sin encuesta).

---

## 2. Ranking por impacto

### F1 — Pérdida de información y trazabilidad del lead

| Dimensión | Valoración |
|-----------|------------|
| Impacto | **Alto** |
| Frecuencia | Alta (cada lead portal/web/WA) |
| Riesgo ingreso/datos | Alto (oportunidad no registrada; RGPD si datos en móviles personales) |
| Sustituibilidad | Media (CRM existe; conversación sigue en WA) |

**Qué ocurre:** el lead llega por email/portal/Tools; la conversación se mueve a WhatsApp/llamada; el resultado (visita, descarte, motivo) no vuelve al CRM.  
**Evidencia:** patrón documentado en CRM, WhatsApp, portales y mapa de integraciones. **[Media]**  
**Nota:** cifras de % leads perdidos en `context.md` **no** se usan como hecho.

---

### F2 — Duplicidades (contactos, fichas, canales)

| Dimensión | Valoración |
|-----------|------------|
| Impacto | **Alto** |
| Frecuencia | Alta |
| Riesgo ingreso/datos | Medio-alto (doble trabajo; cliente contactado dos veces; precio desfasado) |
| Sustituibilidad | Media (deduplicación manual o reglas CRM desiguales) |

**Qué ocurre:** mismo demandante en Idealista + Fotocasa + web; mismo inmueble con precio distinto entre portales; contacto duplicado en CRM.  
**Evidencia:** limitaciones CRM + portales. **[Media]**

---

### F3 — Trabajo manual repetitivo (reescritura / copia)

| Dimensión | Valoración |
|-----------|------------|
| Impacto | **Alto** |
| Frecuencia | Muy alta |
| Riesgo ingreso/datos | Medio (errores de precio/estado; retraso de respuesta) |
| Sustituibilidad | Media-alta técnicamente; baja en micro (sin iPaaS) |

**Qué ocurre:** copiar lead del email al CRM; republicar fichas; re-teclear cliente/importe a facturación; exportar a Excel de comisiones; pegar DNI en chat.  
**Evidencia:** matriz de integraciones (manual dominante en varios tramos). **[Media-alta]**

---

### F4 — App-switching y stack fragmentado

| Dimensión | Valoración |
|-----------|------------|
| Impacto | **Medio-alto** |
| Frecuencia | Continua en jornada comercial |
| Riesgo ingreso/datos | Medio (fatiga; omisiones; cuentas personales) |
| Sustituibilidad | Baja a corto plazo (cliente exige WA; portales son canal) |

**Qué ocurre:** portal → email → WhatsApp → CRM → Drive → calendario → firma → facturación. Ningún sistema es registro único.  
**Evidencia:** stacks por arquetipo; README ejecutivo. **[Media]**

---

### F5 — Rotura de flujo extremo a extremo (lead → cierre → postventa)

| Dimensión | Valoración |
|-----------|------------|
| Impacto | **Medio-alto** |
| Frecuencia | Por operación (picos en oferta/arras/KYC) |
| Riesgo ingreso/datos | Alto en documentación/AML; medio en postventa |
| Sustituibilidad | Baja (límites legales escritura; KYC uneven) |

**Qué ocurre:** huecos entre CRM y firma/archivo; KYC en hilos; liquidación multiagente en Excel; notaría fuera del circuito digital de la agencia (Ley 11/2023: compraventa ordinaria no generalizada por videoconferencia). **[Alta sobre el marco legal]**  
**Evidencia:** mapa integraciones §3–5; firma; KYC. **[Media]**

---

## 3. Tabla resumen

| # | Fricción | Impacto | Frecuencia | Riesgo ingreso/datos | Sustituibilidad |
|---|----------|---------|------------|----------------------|-----------------|
| F1 | Pérdida info / sin trazabilidad | Alto | Alta | Alto | Media |
| F2 | Duplicidades | Alto | Alta | Medio-alto | Media |
| F3 | Manual / reescritura | Alto | Muy alta | Medio | Media (baja en micro) |
| F4 | App-switching | Medio-alto | Continua | Medio | Baja corto plazo |
| F5 | Rotura de flujo E2E | Medio-alto | Por operación | Alto en doc/AML | Baja |

---

## 4. Fricciones secundarias (impacto medio)

| Fricción | Notas breves |
|----------|--------------|
| Sync portal↔CRM incompleta | Precio/estado desfasados; leads solo en bandeja |
| Números WA personales | Pérdida de histórico al salir el agente |
| Splits de comisión en Excel | Error y conflicto; frecuente en redes |
| Reporting débil | INE BI 16,1% ≥10 — poca analítica formal |
| Identidad débil en firma | Solo email en documentos de alto valor |
| Shadow IT en franquicia | Stack impuesto + herramientas locales paralelas |

---

## 5. Relación con dependencias

Las fricciones F1–F4 se agravan porque **portales** y **WhatsApp** son difíciles de sustituir socialmente/comercialmente, mientras el **CRM** es sustituible con coste de cambio. Ver [dependencias-sustituibilidad.md](dependencias-sustituibilidad.md).

---

## 6. Validación

| Ítem | Estado |
|------|--------|
| Ranking basado en síntesis del módulo | **[Media]** |
| Orden exacto por € perdidos | **No cuantificado** — pendiente encuesta |
| ROI / % de `context.md` | **Excluidos** como evidencia |

---

← [Adopción y madurez](adopcion-madurez-arquetipos.md) | [Índice](../README.md) | [Siguiente: Dependencias →](dependencias-sustituibilidad.md)
