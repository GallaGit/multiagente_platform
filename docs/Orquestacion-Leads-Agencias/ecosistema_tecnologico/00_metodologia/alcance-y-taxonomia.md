# Alcance y taxonomía

**Corte:** agosto de 2026 · **Confianza metodológica:** alta

---

## 1. Alcance geográfico y operativo

| Dimensión | Inclusión | Exclusión |
|-----------|-----------|-----------|
| País | España | Benchmarks UE/EEUU salvo contraste puntual |
| Actor | Agencia de intermediación (CNAE 6831) y actores con los que intercambia datos | Operativa interna completa de promotoras, fondos, SOCIMI o servicers |
| Sistemas externos | Portales, bancos, tasadoras, notaría/registro, franquiciador, MLS, firmas, WhatsApp, etc. | Stack completo de cada tercero como objeto principal |
| Producto | Mapa del ecosistema | Diseño de producto SaaS (módulo posterior) |

**Agencia extendida** = la agencia + los sistemas/actores con los que mueve información a lo largo de captación → postventa.

---

## 2. Arquetipos de agencia

| Arquetipo | Rasgo operativo | Implicación tecnológica |
|-----------|-----------------|-------------------------|
| Pequeña / micro | 1–5 personas; ~98% del tejido CNAE 683 es <10 ocupados | Stack mínimo; Excel/WhatsApp frecuentes |
| Mediana | Varias oficinas o equipo comercial estable | CRM dedicado + portales + firma + facturación |
| Gran empresa | Redes, brokerage nacional, multi-marca | CRM/ERP, BI, IAM, integraciones a medida |
| Franquicia | Marca + procesos + tech del franquiciador | Lock-in; portabilidad limitada |
| PropTech-agencia | Modelo digital-first o iBuying/lead-gen | Stack propio; API-first |

Fuente estructural del tejido: [INE 36179](https://www.ine.es/jaxiT3/Tabla.htm?t=36179) · [Alta]

---

## 3. Taxonomía de categorías

### Core comercial y administrativo

CRM · ERP · Property Management (PMS) · MLS · Gestores documentales · Firma electrónica · Contabilidad · Facturación · Banca/tesorería

### Canales y productividad

Portales · Email · Google Workspace · Microsoft 365 · WhatsApp Business · VoIP · Calendarios · Gestión de proyectos · Atención omnicanal

### Marketing y contenido

Marketing automation / ads · Web/CMS · Analítica web · Home staging · Fotografía · Vídeo / tour virtual

### Operaciones especializadas

Software hipotecario · Tasación / AVM · Datos inmobiliarios / geoespaciales · KYC-AML / compliance · Coordinación postventa

### Datos, automatización e IA

Zapier / Make / n8n / Power Automate · BI · IA generativa · Gobierno y calidad de datos · Ciberseguridad / identidad / backups

Categorías adicionales detectadas (incluidas): **omnicanal**, **datos/geo**, **KYC-AML**, **gobierno de datos**, **ciberseguridad**.

---

## 4. Plantilla de análisis por categoría

Cada ficha responde obligatoriamente a:

1. Función principal / problema que resuelve  
2. Usuarios  
3. Momento del flujo operativo  
4. Información gestionada  
5. Integraciones (nativa / API / automatización / manual / inexistente)  
6. Flujo de datos (ASCII)  
7. Limitaciones y tareas humanas  
8. Costes (solo datos públicos; si no hay → «no público»)  
9. Competencia / enfoques de proveedores  
10. Nivel de adopción + confianza  
11. Nivel de madurez + justificación  
12. Validación (evidencia, discrepancias, pendientes)

---

## 5. Relación con módulos previos

| Tema | Dónde está el resumen | Dónde está el detalle |
|------|----------------------|------------------------|
| Adopción CRM/IA | `Situacion_en_España/Mercado_y_tendencias.md` | Este módulo |
| Riesgos tech / RGPD | `analisis_del_mercado/09-riesgos.md` | `06_.../ciberseguridad` + fricciones |
| Hipótesis IA no verificadas | `analisis_del_mercado/context.md` | Solo como hipótesis, no como dato |

---

← [Índice](../README.md) | [Siguiente: Criterios →](criterios-adopcion-madurez.md)
