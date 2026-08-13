# Stacks tecnológicos por arquetipo

**Corte:** agosto de 2026 · **Confianza:** media (síntesis cualitativa; sin censo de stacks)

---

## 1. Lectura previa

Los stacks siguientes son **arquitecturas típicas observadas en el mercado español**, no inventarios auditados. En microagencias el «sistema de registro» suele ser WhatsApp + Excel aunque exista CRM. Ver [criterios](../00_metodologia/criterios-adopcion-madurez.md).

---

## 2. Inmobiliaria pequeña / micro (1–5 personas)

```text
[Portales] ──email/lead──► [Gmail/Outlook]
                              │
                              ├──► [WhatsApp personal/Business App]
                              ├──► [Excel / Drive]
                              └──► [CRM ligero opcional: Witei / Idealista Tools]
                                       │
                                       └── publicación multiportal (si está)

Firma: PDF + a veces Signaturit/DocuSign
Facturación: Contasimple / Holded / asesoría
Calendario: Google Calendar
```

| Capa | Herramientas habituales |
|------|-------------------------|
| Captación | Idealista + Fotocasa (+ 1–2 portales) |
| Conversación | WhatsApp, teléfono, email |
| Inventario | CRM entry o Excel |
| Cierre | Plantillas Word + firma puntual |
| Admin | Asesoría + facturación básica |

**Madurez típica:** digitalizada fragmentada · **[Media]**

---

## 3. Inmobiliaria mediana

```text
Portales ──API/email──► CRM vertical (Inmovilla / Witei / Inmoweb)
                           │
           ┌───────────────┼────────────────┐
           ▼               ▼                ▼
     WhatsApp/VoIP    Calendar/Web      Firma electrónica
           │               │                │
           └──────► Documentos (Drive/SharePoint/CRM)
                           │
                    Facturación / Holded
                           │
                    Banco (conciliación parcial)
```

| Capa | Habitual |
|------|----------|
| Core | CRM vertical + web propia |
| Canales | Portales + WhatsApp Business + email |
| Ops | Firma + gestor documental básico |
| Finance | Facturación SaaS; contabilidad en asesoría o Holded |
| Datos | Informes CRM; poco BI |

**Madurez típica:** digitalizada → automatización puntual (Make/Zapier) · **[Media]**

---

## 4. Gran empresa / brokerage

```text
Portales / web / partners
        │
        ▼
   CRM enterprise o vertical + middleware
        │
   ┌────┼────┬──────────┬─────────┐
   ▼    ▼    ▼          ▼         ▼
 VoIP  WA API  Firma   DMS/ECM   ERP/Finance
   │    │      │        │         │
   └────┴──────┴────────┴────► Data warehouse / BI
                                  │
                                  ▼
                            IAM / SSO / DLP
```

| Capa | Habitual |
|------|----------|
| Core | CRM + ERP/finanzas + PMS si hay alquiler |
| Integración | API + iPaaS + desarrollos a medida |
| Analytics | Power BI / Looker; equipos analytics (CBRE) |
| Compliance | KYC/AML, RGPD, SSO |
| IA | Copilot / genAI contenido y documentos (muestra CBRE) |

**Madurez típica:** automatizada en islas; IA emergente en grandes · **[Media]**

---

## 5. Franquicia

```text
Franquiciador
   ├── CRM / MLS de red (a menudo obligatorio)
   ├── Branding, leads nacionales, formación
   └── Reglas de colaboración y reporting
          │
          ▼
   Oficina franquiciada
   ├── Portales locales (a veces centralizados)
   ├── WhatsApp/email locales (frecuente sombra)
   └── Facturación local + royalties
```

**Riesgos tech:** lock-in, baja portabilidad al salir, Excel paralelo para splits. Ver módulo franquicias. **[Media]**

---

## 6. PropTech / agencia digital-first

```text
App/Web propia ──► Backend (CRM propio o Salesforce)
                      │
         Lead scoring / chat / scheduling
                      │
         Portales como canal secundario o supply
                      │
         BI + experimentación + IA producto
```

Stack API-first; menos dependencia de CRM vertical clásico; más ingeniería. Representan minoría del tejido. **[Media]**

---

## 7. Comparativa rápida

| Componente | Micro | Mediana | Grande | Franquicia | PropTech |
|------------|-------|---------|--------|------------|----------|
| CRM vertical | Opcional | Núcleo | Núcleo o enterprise | Impuesto por red | Propio |
| Portales | Críticos | Críticos | Críticos | Críticos | Variable |
| WhatsApp | CRM de facto | Crítico | API + inbox | Crítico | In-app chat |
| BI | Excel | Informes CRM | BI dedicado | Reporting red | Product analytics |
| IA | Informal | Puntal | Programática | Según red | Producto |

---

## Validación

- Evidencia: síntesis de fichas de categoría + INE/CBRE/PwC + observación sectorial.
- Confianza del mapa: **media**.
- Pendiente: encuesta anonimizada de stack real por arquetipo.

---

← [Fuentes](../00_metodologia/registro-de-fuentes.md) | [Índice](../README.md) | [Siguiente: Integraciones →](mapa-integraciones.md)
