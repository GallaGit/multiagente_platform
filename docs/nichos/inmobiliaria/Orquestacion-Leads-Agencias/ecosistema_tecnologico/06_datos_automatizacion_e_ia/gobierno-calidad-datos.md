# Gobierno y calidad de datos

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Duplicados · RGPD · sistemas de registro · calidad CRM

---

## 1. Función principal

Asegurar que la información de **contactos, inmuebles y operaciones** sea única, actual, legítima y utilizable: quién es el sistema de registro, cómo se evitan duplicados, qué campos son obligatorios y bajo qué base jurídica se tratan datos personales.

Sin gobierno, el CRM, el BI y la automatización amplifican el error. El problema dominante no es “falta de herramienta de MDM”, sino **múltiples fuentes de verdad** (CRM + WhatsApp + Excel + portal). **[Media]**

---

## 2. Usuarios

| Rol | Responsabilidad |
|-----|-----------------|
| Admin CRM / oficina | Altas, fusiones, reglas de campos |
| Agentes | Crean y ensucian datos en el día a día |
| DPO / responsable RGPD (si existe) | Bases legales, derechos, encargados |
| Franquiciador | Diccionario de datos y reporting de red |
| Integrador | Mapeos iPaaS que pueden duplicar registros |

---

## 3. Momento del flujo

Desde el primer lead o encargo hasta archivo postventa. Crítico en: importación de portales, fusión de demandantes, cambio de agente, baja de exclusivas, ejercicio de derechos ARCO/RGPD, y al conectar automatizaciones.

---

## 4. Información gestionada

- Identificadores: teléfono, email, NIF/NIE (cuando procede), referencia catastral / interna  
- Estados de oportunidad e inmueble  
- Origen del lead y consentimiento de comunicaciones comerciales  
- Documentación adjunta (ubicación, retención)  
- Encargados del tratamiento (CRM SaaS, portales, BSP WhatsApp, firma)  

Datos de categoría especial: no habituales; si aparecen, minimización estricta.

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Riesgo de calidad |
|----------|------|-------------------|
| Portal → CRM | Nativa / API | Duplicados por cada consulta |
| WhatsApp → CRM | Manual / API | Conversación sin ficha |
| Excel sombra ↔ CRM | Manual | Doble verdad |
| Firma / Drive | Manual / nativa | Docs fuera del expediente |
| iPaaS | Automatización | Altas duplicadas si no hay match key |
| Franquicia hub | API / export | IDs distintos oficina vs red |

---

## 6. Flujo de datos (ASCII)

```text
[Portal] ──lead──┐
[Web]    ──form──┤
[WA]     ──chat──┼──► ¿Match teléfono/email? ──sí──► Update CRM
[Excel]  ──pega──┘              │
                                no
                                ▼
                         Alta nueva (¿duplicado?)
                                │
                                ▼
              [CRM = sistema de registro deseado]
                                │
              +----- paralelo -----+
              v                    v
        [Chat WhatsApp]      [Carpeta Drive]
         (sombra)              (sombra)
```

---

## 7. Limitaciones y tareas humanas

- **Duplicados:** mismo demandante con varios móviles; mismo inmueble republicado.  
- Campos libres vs taxonomía (tipología, estado): imposibilitan reporting.  
- Consentimiento marketing vs interés legítimo comercial: mal documentado.  
- Baja de agente: números personales se llevan el histórico.  
- Encargados: contratos DPA incompletos con vendors.  
- RGPD: derechos de acceso/supresión chocan con obligaciones AML de conservación (tensión a gestionar, no a ignorar). Ver KYC en `05_.../kyc-aml-compliance.md`.

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Módulo calidad / dedupe CRM | Suele incluido o no desglosado — **no público** homogéneo |
| Herramientas MDM enterprise | Bajo presupuesto / licencia — **consultar fabricante** |
| Consultoría RGPD / DPO externo | Mercado libre — **no público** estándar sectorial |
| Tiempo interno de limpieza | Coste dominante; no cuantificado oficialmente |
| Multas AEPD | Caso a caso; no usar como “tarifa” |

No inventar precios de “paquete calidad de datos inmobiliario”.

---

## 9. Competencia / enfoques comparados

| Enfoque | Encaje | Fricción |
|---------|--------|----------|
| Disciplina + campos obligatorios CRM | Mediana | Cultura de uso |
| Excel como registro | Micro | Escalado y RGPD |
| Deduplicación nativa CRM | Si existe y se usa | Reglas flojas |
| Hub franquicia | Redes | Portabilidad limitada |
| MDM / CDP | Grandes / PropTech | Sobrepeso |
| “No gobernar” | Default del tejido | BI e IA inútiles |

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| CRM como registro *deseado* | Habitual en medianas (≥10: CRM 57,9% INE) | Alta dato ≥10; baja en micro |
| CRM como registro *real* (incluye WA) | Irregular | Media cualitativa |
| Política escrita de calidad de datos | Poco utilizada | Baja |
| DPA con encargados cloud | Habitual-formal en medianas; irregular en micro | Media |
| Deduplicación sistemática | Emergente / irregular | Baja |

INE CRM: [tpx=59889](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) · **[Alta; baja representatividad micro]**

---

## 11. Madurez + justificación

Uso típico: **Digitalizada** con registro fragmentado (Tradicional en la práctica de WhatsApp).  
Con diccionario de datos + matching + DPA: **Digitalizada → Automatizada** en altas.  
Madurez asignada: **Digitalizada / registro dual CRM–WhatsApp**. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| RGPD como marco | Norma · **[Alta]** · [AEPD obligaciones](https://www.aepd.es/) |
| Tasa de duplicados en agencias ES | Pendiente (sin censo) |
| % agencias con DPO / registro de actividades | Pendiente |
| Conflicto retención AML vs derecho de supresión | Cualitativo; protocolo legal externo |

---

← [IA generativa](ia-generativa.md) | [Índice](../README.md) | [Siguiente: Ciberseguridad →](ciberseguridad-identidad.md)
