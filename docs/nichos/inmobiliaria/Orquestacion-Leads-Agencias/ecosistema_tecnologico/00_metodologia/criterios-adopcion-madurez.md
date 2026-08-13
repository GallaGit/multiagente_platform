# Criterios de adopción y madurez

**Corte:** agosto de 2026

---

## 1. Nivel de adopción (por categoría)

| Nivel | Criterio operativo en España |
|-------|------------------------------|
| **Muy extendida** | Presente en la mayoría de arquetipos; difícil operar sin ella (ej. portales, email, WhatsApp) |
| **Habitual** | Frecuente en medianas/grandes; irregular en micro |
| **Poco utilizada** | Nicho o solo grandes / PropTech |
| **Emergente** | Crecimiento visible, penetración aún baja o desigual |

Cada clasificación lleva **confianza** (alta/media/baja) porque la adopción en microagencias **no está censada** de forma homogénea.

### Ancla cuantitativa disponible

Empresas de actividades inmobiliarias (CNAE 68) con **10+ empleados**, INE TIC T1 2023:

| Tecnología | % | Lectura |
|------------|---|---------|
| CRM | 57,9% | Habitual en empresas ≥10; desconocida en micro |
| ERP | 60,6% | Habitual en ≥10 |
| Analítica interna | 36,6% | Habitual-baja |
| BI | 16,1% | Poco utilizada |
| Alguna IA | 9,35% | Emergente / polarizada |

Fuentes: [INE CRM](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) · [INE IA](https://www.ine.es/jaxi/Tabla.htm?L=0&tpx=59891) · **[Alta; baja representatividad del tejido]**

CBRE Madurez Digital España 2025–2026 (muestra de principales compañías): madurez **5,2/10**; IA generativa **71%**. **[Media; no comparable con INE]**  
Fuente: [CBRE](https://www.cbre.es/press-releases/el-sector-inmobiliario-aprueba-en-madurez-digital-por-primera-vez)

---

## 2. Nivel de madurez tecnológica (por categoría)

| Nivel | Definición | Señal observable |
|-------|------------|------------------|
| **Tradicional** | Papel, Excel, teléfono, procesos personales | Sin sistema de registro único |
| **Digitalizada** | Herramientas digitales aisladas | CRM o portal + email, poca sincronización |
| **Automatizada** | Flujos entre sistemas sin reescritura manual | Webhooks, API, RPA/iPaaS, reglas |
| **Impulsada por IA** | Modelos asisten o ejecutan tareas con supervisión | Cualificación, redacción, scoring, extracción documental |

La madurez se asigna al **uso típico en agencias españolas**, no a la frontera tecnológica del fabricante.

---

## 3. Tipos de integración

| Tipo | Definición |
|------|------------|
| **Nativa** | Connector oficial del fabricante, mantenido |
| **API** | Integración vía API documentada (propia o de tercero) |
| **Automatización** | iPaaS (Zapier, Make, n8n, Power Automate) o scripts |
| **Manual** | Export/import, copiar-pegar, reenvío email |
| **Inexistente** | No hay puente habitual; se rehace el dato |

---

## 4. Reglas de interpretación

1. **No promediar INE y CBRE.** Miden universos distintos.
2. **Capacidad ≠ adopción.** Una API pública no implica uso masivo.
3. **Franquicia ≠ independiente.** El stack puede venir impuesto.
4. **WhatsApp/email pueden ser el CRM de facto** aunque exista licencia de CRM.
5. Ante duda de adopción en micro: clasificar como **habitual en medianas / incierta en micro** y bajar confianza.

---

## 5. Discrepancias conocidas

| Afirmación A | Afirmación B | Resolución |
|--------------|--------------|------------|
| IA 9,35% (INE) | IA gen. 71% (CBRE) | Polarización por tamaño/muestra |
| Cloud inmobiliario ~50% (prensa sobre INE) | Madurez 5,2/10 (CBRE) | Cloud ≠ madurez de procesos |
| «Inmovilla en 90% MLS» (blogs comerciales) | Sin censo público | Tratar como **no verificado** |

---

← [Alcance](alcance-y-taxonomia.md) | [Índice](../README.md) | [Siguiente: Costes →](metodologia-costes.md)
