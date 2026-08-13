# IA generativa

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** ChatGPT · Copilot · Gemini · IA embebida en CRM · polarización de adopción

---

## 1. Función principal

Asistir en **redacción y síntesis** (anuncios, emails, resúmenes de visitas, traducción) y, en stacks avanzados, en **cualificación, extracción documental o scoring** conectados al CRM.

Dos modos que no deben confundirse:

1. **Uso informal:** empleado pega texto en ChatGPT/Gemini/Copilot personal o de oficina.  
2. **IA embebida:** módulo del CRM, bot WhatsApp/API o agente privado con historial y permisos.

Capacidad de marketing PropTech ≠ penetración en microagencias. **[Media]**

---

## 2. Usuarios

| Rol | Patrón |
|-----|--------|
| Agente | Redacción de fichas, respuestas a leads |
| Marketing | Copy ads, landings, RRSS |
| Admin | Resúmenes, plantillas |
| Ops digital / PropTech | Bots, prompts versionados, RAG sobre inventario |
| Dirección (grandes) | Políticas de uso, Copilot M365 |

---

## 3. Momento del flujo

Más frecuente en **captación y nurturing** (ficha, primer contacto, follow-up). También en documentación (resumen de contratos) con riesgo RGPD. Menos en cierre notarial (dominio humano/legal). Postventa: borradores de review request / referidos.

---

## 4. Información gestionada

- Textos de anuncios, emails, scripts de llamada  
- Resúmenes de conversaciones (si se pegan o se conectan)  
- En embebido: campos CRM, inventario, historial de lead  
- En malas prácticas: DNI, nóminas, datos de menores o salud pegados al chat público  

Tratamiento de datos personales: responsabilidad del responsable del tratamiento (agencia). Ver [gobierno-calidad-datos.md](gobierno-calidad-datos.md) y [ciberseguridad-identidad.md](ciberseguridad-identidad.md).

---

## 5. Integraciones (tipo)

| Modo | Tipo |
|------|------|
| Chat web ChatGPT / Gemini | Manual (copiar-pegar) |
| Microsoft Copilot (M365) | Nativa en apps Office/Teams (según licencia) |
| Gemini en Workspace | Nativa (según plan Google) |
| “IA” botón en CRM vertical | Nativa fabricante (alcance desigual) |
| Bot WhatsApp + LLM | API / automatización + BSP |
| Agente privado ↔ CRM | API / iPaaS — poco habitual en micro |

---

## 6. Flujo de datos (ASCII)

```text
                    +-- [ChatGPT / Gemini / Copilot]  (informal)
                    |         ^
[Agente] --pega texto---------+----devuelve borrador--> [Portal / Email / WA]
                    |
                    +-- [Módulo IA CRM / bot API] ----> [CRM] (registro + auditoría)
                              |
                              v
                         [Inventario / lead]
```

---

## 7. Limitaciones y tareas humanas

- Alucinaciones en precios, m², régimen (VPO, protección) o normativa autonómica.  
- Tonos y claims publicitarios: responsabilidad de la agencia (publicidad engañosa).  
- Fuga de datos a modelos públicos sin DPA adecuado.  
- Sin conexión al CRM: no hay histórico ni medición de conversión.  
- “IA escribe anuncios” no arregla leads sin respuesta humana/API.

---

## 8. Costes (solo públicos)

| Concepto | Dato | Fuente |
|----------|------|--------|
| ChatGPT Free / Plus / Team / Enterprise | Planes públicos OpenAI; importes y límites **consultar** en la fecha de compra (cambian) | [OpenAI / ChatGPT pricing](https://openai.com/chatgpt/pricing/) · verificar · **[Media-alta]** |
| Google Gemini / Workspace AI | Según plan Workspace; **consultar fabricante** | Google Workspace |
| Microsoft Copilot | Add-on / incluido según SKU M365; precio de lista **consultar** Microsoft en mercado ES | Microsoft · no inventar € |
| Módulo IA del CRM vertical | Incluido o upsell — **no público** homogéneo | Fabricante CRM |
| Bot + LLM + WhatsApp API | Tokens + BSP + iPaaS — TCO bajo presupuesto | no público pack inmobiliario |

No se usan cifras de ROI de `analisis_del_mercado/context.md` (p. ej. 5,36:1) como evidencia. **[Baja; hipótesis]**

---

## 9. Competencia / enfoques comparados

| Enfoque | Pros | Contras |
|---------|------|---------|
| Chat genérico informal | Cero fricción | Sin trazabilidad; riesgo datos |
| Copilot / Gemini oficina | Integrado en docs/email | Coste licencia; no sabe el inventario |
| IA embebida CRM | Contexto de ficha/lead | Calidad desigual por fabricante |
| Agente cualificador 24/7 + CRM | Cierra el hueco de respuesta | Implantación, compliance WA, supervisión |
| Solo plantillas humanas | Control | Escalado pobre |

Competencia real del “asistente”: el tiempo del agente y las plantillas del CRM, no otro LLM.

---

## 10. Adopción + confianza

| Fuente | Cifra | Lectura | Confianza |
|--------|-------|---------|-----------|
| **INE** TIC, CNAE 68, **≥10** empleados, T1 2023 | **Alguna IA 9,35%**; de usuarios IA, 22,6% en automatización/decisiones | **Emergente** en el segmento medido; no representa micro | **[Alta]** dato; **baja** representatividad |
| **CBRE** Madurez Digital ES 2025–2026 (principales compañías) | **IA generativa 71%**; usos: contenido 86% · datos 81% · docs 76% | Habitual en **grandes** | **[Media]**; **no comparable** con INE |
| Uso informal ChatGPT en micro | Emergente–habitual cualitativo | Baja–media |
| IA embebida CRM + WhatsApp API | Emergente / poco utilizada | Media |

**Regla:** no promediar 9,35% e 71%. Universos distintos (INE ≥10 vs muestra CBRE de grandes). Polarización por tamaño. Fuentes: [INE IA](https://www.ine.es/jaxi/Tabla.htm?L=0&tpx=59891) · [CBRE](https://www.cbre.es/press-releases/el-sector-inmobiliario-aprueba-en-madurez-digital-por-primera-vez).

---

## 11. Madurez + justificación

Uso típico micro/mediana: **Digitalizada** con bolsas de uso informal de genAI (capa “impulsada por IA” solo en tareas de texto).  
Con bot+CRM gobernado: hacia **Impulsada por IA** con supervisión.  
Tejido agregado: **no** madurez “IA-first”; ancla INE 9,35% en ≥10 y vacío en <10. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| INE 9,35% / CBRE 71% | Registrados; no comparables · **[Alta metodológica]** |
| ROI / % leads recuperados de `context.md` | **Excluidos** como hecho |
| % App ChatGPT vs módulo CRM en agencias ES | Pendiente |
| Políticas AEPD sobre uso de LLM con datos de clientes | Seguir guías AEPD; caso a caso |

---

← [Business Intelligence](business-intelligence.md) | [Índice](../README.md) | [Siguiente: Gobierno de datos →](gobierno-calidad-datos.md)
