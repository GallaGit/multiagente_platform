# Datos inmobiliarios y geoespaciales

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Catastro · Registradores · idealista/data · INE

---

## 1. Función principal

Proveer datos de referencia del activo y del entorno (titularidad/cargas vía registro, descripción fiscal catastral, estadísticas de precios/demografía, oferta de portales) para captación, due diligence, pricing y reporting. La agencia consume; rara vez produce datos oficiales.

---

## 2. Usuarios

Agente (nota simple, referencia catastral), abogado/gestoría, tasadora, analista de expansión, PropTech, notario (verificación en cierre). Marketing usa métricas de zona de forma superficial.

---

## 3. Momento del flujo

Captación y documentación → comercialización (contexto de zona) → due diligence pre-escritura → postventa fiscal puntual. En grandes: estudios de mercado continuos.

---

## 4. Información gestionada

| Fuente | Contenido típico |
|--------|------------------|
| Catastro | Referencia, tipología, superficie, cartografía, valor catastral |
| Registro / Registradores | Titularidad, cargas, nota simple |
| INE | Estadísticas (población, vivienda, precios índices, estructura empresarial) |
| idealista/data | Oferta, demanda, precios, sociodemografía, AVM/API B2B |
| Portales (UI) | Comparables de anuncio (no = transacción cerrada) |

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| Sede Electrónica Catastro / WMS-WFS | API / servicios web / manual | Datos abiertos parciales |
| Registradores (pedido nota) | Portal / manual | Coste por petición |
| CRM ↔ Catastro | API / automatización / manual | Capacidad en algunos CRM; uso irregular |
| idealista/data → sistemas cliente | API / fichero / widget | Contrato B2B |
| INE → BI agencia | Manual (descarga) / API INE | Poco frecuente en micro |
| Notaría ↔ Catastro/Registro | Procesos oficiales | Agencia extendida en cierre |

---

## 6. Flujo de datos (ASCII)

```text
Inmueble
   │
   ├─► Catastro (ref. / mapa / datos fiscales)
   ├─► Registro (nota simple / cargas)
   ├─► INE / open data (contexto zona)
   └─► idealista/data o UI portal (oferta/demanda)
            │
            ▼
     CRM / informe captación / tasación / BI
            │
            ▼
     Decisión de precio · due diligence · anuncio
```

---

## 7. Limitaciones y tareas humanas

- Catastro ≠ Registro: descripciones pueden discrepar; conciliación humana. **[Alta]**
- Comparables de portal son **oferta**, no precio de transacción Registradores/Notariado.
- idealista/data y packs analíticos: fuera del alcance económico de muchas microagencias.
- Licencias y límites de reutilización de datos: restricción legal/contractual.
- Capacidad anunciada de “CRM con Catastro” ≠ calidad de dato siempre actualizada.

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| Consultas Catastro (servicios abiertos básicos) | Gratuitos según servicio en Sede Electrónica |
| Nota simple / productos registrales | Tarifas del Colegio de Registradores / servicio elegido — **consultar tarifa oficial vigente**; no fijar cifra sin URL de tarifa al corte **[Media]** |
| idealista/data | **no público** (presupuesto) · [idealista/data](https://www.idealista.com/data/) |
| Tablas INE | Gratuitas |
| Licencias cartográficas comerciales | no público / bajo presupuesto |

---

## 9. Competencia / enfoques comparados

| Enfoque | Fortaleza | Límite |
|---------|-----------|--------|
| Fuentes oficiales (Catastro, Registro, INE) | Autoridad legal/estadística | UX; no pensado como CRM comercial |
| idealista/data | Granularidad de oferta/demanda portal | Precio opaco; sesgo de anuncio |
| CRM con widgets de zona | Comodidad agente | Profundidad limitada |
| Excel + pantallazos portal | Ubicuo en micro | No auditable ni escalable |
| Consultoras / data rooms | Operaciones high-ticket | Fuera del día a día residencial |

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| Pedir nota simple en compraventa seria | Muy extendida | Alta |
| Consulta Catastro en captación | Habitual | Media-alta |
| idealista/data contratado | Poco utilizada (nicho) | Media |
| BI con INE/open data en agencia | Poco utilizada (alineado con BI INE 16,1% en ≥10 emp.) | Alta cifra INE; baja en micro |

[INE TIC](https://www.ine.es/jaxi/Tabla.htm?tpx=59889) · **[Alta; baja representatividad micro]**

---

## 11. Madurez + justificación

Consumo de datos oficiales: **Digitalizada** (sedes electrónicas).  
Integración continua en CRM: minoritaria → no **Automatizada** de forma típica.  
Madurez uso agencia ES: **Digitalizada**. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Distinción Catastro/Registro | Doctrina y práctica notarial **[Alta]** |
| Tarifas registrales exactas al corte | Verificar en sitio oficial al usar cifra |
| Volumen contratos idealista/data | No público |
| Cobertura API Catastro en CRM ES | Inventario pendiente |

---

← [Tasación/AVM](tasacion-avm.md) | [Índice](../README.md) | [Siguiente: KYC-AML →](kyc-aml-compliance.md)
