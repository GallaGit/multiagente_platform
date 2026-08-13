# Mapa maestro de integraciones

**Corte:** agosto de 2026 · **Confianza:** media

---

## 1. Diagrama global (agencia mediana típica)

```text
                    ┌─────────────┐
                    │   Portales  │
                    │ Idealista…  │
                    └──────┬──────┘
                           │ email / API / tools
                           ▼
┌──────────┐      ┌────────────────┐      ┌──────────────┐
│ Web/CMS  │─────►│      CRM       │◄────►│  MLS / red   │
└──────────┘      │ (inventario +  │      └──────────────┘
                  │  contactos)    │
                  └───────┬────────┘
        ┌─────────┬───────┼───────┬─────────┬──────────┐
        ▼         ▼       ▼       ▼         ▼          ▼
   WhatsApp    Email   VoIP   Calendar   Firma      Docs
   Business             /tel              e-sign    Drive
        │         │       │       │         │          │
        └─────────┴───────┴───────┴─────────┴────┬─────┘
                                                 ▼
                                         Facturación
                                         Contabilidad
                                         Banco
                                                 │
                                                 ▼
                                              BI/Excel
```

---

## 2. Matriz de conexiones habituales

| Origen → Destino | Mecanismo típico | Calidad |
|------------------|------------------|---------|
| Portal → CRM | Nativa (CRM) / email parse / Idealista Tools | Irregular |
| CRM → Portales | Nativa multipublicación | Habitual en verticales |
| CRM → Calendar | Nativa o Google/Outlook sync | Habitual |
| CRM ↔ WhatsApp | Manual / automatización / API Business | Débil en micro |
| CRM → Firma | Nativa o Zapier/Make | Habitual en medianas |
| CRM → Facturación | Manual / API Holded / inexistente | Débil |
| Email → CRM | Captura BCC / manual | Parcial |
| VoIP → CRM | Click-to-call / CTI | Poco en micro |
| Docs → CRM | Adjuntos / Drive link | Manual frecuente |
| Banco → Contabilidad | Open banking / extracto | Habitual en SaaS finanzas |
| CRM → BI | Export / conector | Poco en micro |
| Catastro/Registro → CRM | Consulta manual / API parcial | Mayormente manual |

---

## 3. Integraciones críticas vs frágiles

**Críticas (si fallan, se para el negocio):**

- Portal ↔ CRM (publicación y leads)
- Teléfono / WhatsApp ↔ persona comercial
- Email (identidad y contratos)
- Facturación ↔ banco (cobro honorarios)

**Frágiles (rompen trazabilidad):**

- WhatsApp fuera del CRM
- Documentación en carpetas personales
- Splits de comisión en Excel
- KYC en hilos de email
- Leads de portal solo en bandeja sin ficha

---

## 4. Mapa por tipo de mecanismo

```text
NATIVA          API            AUTOMATIZACIÓN     MANUAL
CRM↔Portales    Holded API     Make: WA→CRM       Copiar lead email
CRM↔Calendar    Firma API      Zapier: firma→Drive Reenviar PDF
Idealista Tools Meta WA API    Power Automate     Excel splits
                Portal APIs    n8n self-host      Foto→ficha a mano
```

---

## 5. Integraciones inexistentes o raras en la práctica

- Conversación WhatsApp completa como timeline auditado en CRM (salvo setups avanzados)
- KYC-AML embebido extremo a extremo en CRM vertical típico
- Liquidación multioficina/multiagente nativa robusta (frecuente Excel) — evidencia cualitativa blogs/consultores **[Baja-media]**
- Escritura notarial digital genérica en el flujo de agencia (limitación legal Ley 11/2023) **[Alta]**
- BI unificado portal+CRM+ads+WhatsApp sin ingeniería

---

## Validación

- Basado en documentación de fabricantes, CNMC (rol portales), fichas de categoría y patrones de iPaaS.
- Discrepancia: marketing de «todo integrado» vs uso real con WhatsApp/Excel sombra.
- Pendiente: inventario de conectores certificados por CRM líder en ES.

---

← [Stacks](stacks-por-arquetipo.md) | [Índice](../README.md) | [Siguiente: Flujo →](flujo-lead-postventa.md)
