# Adopción y madurez por arquetipos

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Regla:** no promediar INE y CBRE; microagencias **no censadas** de forma homogénea.

Criterios: [criterios-adopcion-madurez.md](../00_metodologia/criterios-adopcion-madurez.md).

---

## 1. Anclas cuantitativas (universos distintos)

### INE TIC — CNAE 68, empresas **≥10 empleados**, T1 2023

| Tecnología | % | Lectura de adopción |
|------------|---|---------------------|
| CRM | **57,9%** | Habitual en ≥10; desconocida en micro |
| ERP | **60,6%** | Habitual en ≥10 |
| Analítica interna | 36,6% | Habitual-baja (referencia criterios) |
| BI | **16,1%** | Poco utilizada |
| Alguna IA | **9,35%** | Emergente / polarizada |

Fuentes: [INE CRM](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) · [INE IA](https://www.ine.es/jaxi/Tabla.htm?L=0&tpx=59891) · **[Alta; baja representatividad del tejido]**

### CBRE Madurez Digital España 2025–2026 (principales compañías)

| Indicador | Valor | Lectura |
|-----------|-------|---------|
| Madurez digital | **5,2 / 10** | Aprobado; no = digitalización de micro |
| IA generativa | **71%** | Uso en muestra grande; **no comparable** con INE 9,35% |

Fuente: [CBRE](https://www.cbre.es/press-releases/el-sector-inmobiliario-aprueba-en-madurez-digital-por-primera-vez) · **[Media]**

### Ecosistema

~**700 PropTech** y **170 ConTech** (PwC 2025): oferta de herramientas ≠ adopción en agencias. **[Media]**

---

## 2. Niveles usados en tablas

**Adopción:** muy extendida · habitual · poco utilizada · emergente · incierta (micro)  
**Madurez de uso típico:** tradicional · digitalizada · automatizada · impulsada por IA

---

## 3. Adopción y madurez por categoría

| Categoría | Adopción (lectura ES) | Madurez de uso típico | Confianza | Ancla |
|-----------|----------------------|------------------------|-----------|-------|
| Portales | Muy extendida | Digitalizada → automatización parcial | Alta cual. / baja cuant. | CNMC; sin cuota % |
| Email | Muy extendida | Digitalizada | Alta | Práctica universal |
| WhatsApp (app) | Muy extendida | Digitalizada; fuera del CRM | Media-alta | Observación sectorial |
| WhatsApp API + CRM | Emergente / poco | Automatizada (si existe) | Media | Distinción app≠API |
| CRM | Habitual ≥10; incierta en micro | Digitalizada; auto. parcial | Alta (INE); baja micro | INE 57,9% |
| ERP / finanzas formales | Habitual ≥10 | Digitalizada (asesoría frecuente) | Alta (INE); media uso | INE 60,6% |
| Facturación SaaS | Habitual | Digitalizada | Media | Sin censo marca |
| Firma electrónica | Habitual creciente mediana | Digitalizada; auto. minoritaria | Media-baja | Sin % INE |
| MLS / colaboración | Irregular | Digitalizada | Media-baja | Riesgo CNMC histórico |
| BI / analítica avanzada | Poco utilizada | Digitalizada (Excel) → BI en grandes | Alta (INE BI) | INE 16,1% |
| Automatización iPaaS | Poco / emergente | Automatizada en islas | Media | Make/Zapier puntuales |
| IA (alguna) | Emergente polarizada | Informal o impulsada (grandes) | Alta (INE); media CBRE | 9,35% vs 71% |
| KYC-AML digital E2E | Poco / emergente | Tradicional→digitalizada | Media | Sujetos Ley 10/2010 |
| AVM / tasación avanzada | Nicho / grande | Variable | Media | Ops especializadas |
| Ciberseguridad MFA/backups | Irregular | Digitalizada parcial | Media-baja | Sin % sectorial |

---

## 4. Adopción y madurez por arquetipo

| Categoría | Micro | Mediana | Grande | Franquicia | PropTech |
|-----------|-------|---------|--------|------------|----------|
| **Portales** | Muy ext. · digit. | Muy ext. · digit./auto. parcial | Muy ext. · auto. islas | Muy ext. · según red | Variable · producto |
| **WhatsApp** | CRM de facto · digit. | Crítico · sync débil | API + inbox posible | Crítico · sombra local | Chat in-app / API |
| **CRM** | Opcional / Tools · digit. o Excel | Núcleo vertical · digit. | Vertical o enterprise · auto. | Impuesto · digit. | Propio / SF · auto./IA |
| **Firma** | Puntual · trad./digit. | Habitual · digit. | Programática · auto. | Según red | API |
| **Finanzas** | Asesoría + factura ligera | Holded/A3 · digit. | ERP · digit./auto. | Local + royalties | Stack propio |
| **BI** | Excel | Informes CRM | BI dedicado | Reporting red | Product analytics |
| **IA** | Informal (chat) | Puntal / botón CRM | Programática (CBRE) | Según red | Producto |
| **Madurez global típica** | Digit. fragmentada | Digit. → auto. puntual | Auto. en islas; IA emergente | Digit. + lock-in | Auto./IA producto |

Confianza del mapa por arquetipo: **media** (síntesis cualitativa; sin censo de stacks). · [stacks-por-arquetipo.md](../01_arquitectura_y_flujos/stacks-por-arquetipo.md)

---

## 5. Polarización (lectura transversal)

```text
INE ≥10 emp.          CBRE grandes           Micro (~mayoría tejido)
CRM 57,9%             Madurez 5,2            Adopción CRM desconocida
IA 9,35%              IA gen 71%             WA + Excel frecuentes
BI 16,1%              Analytics equipos      Sin BI
```

**Hecho:** las cifras oficiales/consultora existen y no son comparables.  
**Supuesto de trabajo (no censo):** la mediana digitaliza CRM+portales; la micro digitaliza canales pero no procesos. **[Media]**

---

## 6. Capacidad ≠ adopción ≠ madurez

| Señal | Ejemplo | Error a evitar |
|-------|---------|----------------|
| Capacidad anunciada | «IA» en CRM vertical | Asumir uso sistemático |
| Integración disponible | API portales | Asumir sync bi-direccional real |
| Uso real | Lead en email → copia a CRM | Confundir con automatizada |
| Muestra CBRE | 71% IA gen. | Extender a CNAE 683 micro |

---

## 7. Validación

| Ítem | Estado |
|------|--------|
| INE CRM/ERP/BI/IA | Verificado · **[Alta]** |
| CBRE 5,2 / 71% | Citado · **[Media]** |
| % adopción por marca/provincia | Pendiente |
| Tablas arquetipo | Síntesis · **[Media]** |

**No usar** % leads perdidos / ROI de `context.md` como evidencia de madurez.

---

← [Costes TCO](costes-tco.md) | [Índice](../README.md) | [Siguiente: Puntos de fricción →](puntos-de-friccion.md)
