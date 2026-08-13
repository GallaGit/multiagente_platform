# Modelos de datos y sistemas de registro

**Corte:** agosto de 2026 · **Confianza:** media

---

## 1. Entidades mínimas del dominio

| Entidad | Atributos clave | Sistema de registro deseable |
|---------|-----------------|------------------------------|
| Persona / cuenta | Identidad, roles (comprador, vendedor, inquilino), consentimientos | CRM |
| Inmueble | Ref. catastral, dirección, tipología, estado, precio, exclusividad | CRM / PMS |
| Encargo / mandato | Tipo, vigencia, honorarios, exclusividad | CRM + documental firmado |
| Lead / oportunidad | Fuente, score, estado embudo, propietario comercial | CRM |
| Actividad | Llamada, WA, email, visita, tarea | CRM (+ canal origen) |
| Visita | Fecha, asistentes, feedback | CRM + calendario |
| Oferta | Importe, condiciones, validez | CRM + documental |
| Contrato | Arras, alquiler, anexos, hash firma | Documental + firma |
| Expediente AML | KYC, origen fondos, riesgo | Compliance / documental |
| Factura / cobro | Base, IVA, estado, split | Facturación |
| Publicación | Portal, ID anuncio, fechas, stats | CRM / portal |

---

## 2. Quién es «source of truth» (ideal vs real)

```text
IDEAL                         REAL FRECUENTE (micro/mediana)
─────                         ──────────────────────────────
CRM = contactos + inmuebles   WhatsApp = conversación
Documental = contratos        Email = contratos y leads
Facturación = dinero          Banco = dinero
Calendario = visitas          Calendario personal + WA
Portal = audiencia            Portal = audiencia (igual)
```

Cuando hay dos verdades, gana la herramienta que el comercial abre cada hora — a menudo WhatsApp — no el CRM. **[Media; cualitativo]**

---

## 3. Flujos de sincronización de identidad

| Problema | Síntoma | Causa tech |
|----------|---------|------------|
| Duplicados de contacto | Mismo móvil en 3 fichas | Lead portal + alta manual + WA |
| Duplicados de inmueble | Mismo piso en dos refs | Colaboración MLS + alta local |
| Identidad débil | Nombre distinto en arras vs CRM | Sin ID único / DNI solo en PDF |
| Consentimiento opaco | No se sabe base RGPD del lead | Formulario portal ≠ CRM |

---

## 4. Datos que rara vez se estructuran

- Motivo real de pérdida de oportunidad  
- Capacidad financiera verificada (vs declarada)  
- Tiempo de primera respuesta por canal  
- Coste de adquisición por lead y por portal  
- Feedback cualitativo de visitas  
- Evidencia AML reutilizable entre operaciones  
- Atribución marketing (ads → visita → cierre)

Estos huecos alimentan el análisis de [vacíos](../07_analisis_transversal/vacios-tecnologicos.md).

---

## 5. Retención y portabilidad

| Activo | Riesgo al cambiar de herramienta |
|--------|----------------------------------|
| Histórico CRM | Export incompleto de actividades |
| Anuncios portal | IDs y stats no migran al CRM nuevo |
| Conversaciones WA | Quedan en el teléfono del agente |
| Firmas | Certificados en proveedor e-sign |
| Leads de red franquicia | Pueden no ser propiedad de la oficina |

Relacionado: riesgos tecnológicos en [09-riesgos](../../analisis_del_mercado/09-riesgos.md).

---

## Validación

- Modelo conceptual estándar de intermediación + observaciones de stack.  
- Confianza **media**.  
- Pendiente: esquema de campos reales exportados por Inmovilla/Witei/Idealista Tools.

---

← [Flujo](flujo-lead-postventa.md) | [Índice](../README.md) | [Siguiente: CRM →](../02_sistemas_core/crm-inmobiliarios.md)
