# Flujo completo de la información: lead → postventa

**Corte:** agosto de 2026 · Relacionado: [02-funcionamiento](../../analisis_del_mercado/02-funcionamiento.md)

---

## 1. Vista extremo a extremo

```text
Demanda                Oferta (paralelo)
───────                ────────────────
Lead portal/web   Propietario / captación
   │                     │
   ▼                     ▼
Email/CRM inbox     Valoración + mandato
   │                     │
   ▼                     ▼
WhatsApp/tel        Foto / staging / ficha
   │                     │
   ▼                     ▼
Cualificación  ◄──►  Publicación portales
   │                     │
   └────────┬────────────┘
            ▼
         Visita (calendar)
            ▼
      Oferta / negociación
            ▼
   Reserva-arras + firma e
            ▼
   Hipoteca / tasación / KYC
            ▼
      Notaría / Registro
            ▼
   Factura honorarios + cobro
            ▼
         Postventa
```

---

## 2. Traspasos de datos (detalle)

| # | Etapa | Origen | Destino | Dato | Mecanismo | Fallo habitual |
|---|-------|--------|---------|------|-----------|----------------|
| 1 | Entrada lead | Portal | Email/CRM | Nombre, teléfono, inmueble | Nativa/email | Lead solo en bandeja |
| 2 | Primer contacto | Email/CRM | WhatsApp | Teléfono | Manual | Sin registro en CRM |
| 3 | Cualificación | WhatsApp | CRM | Presupuesto, plazo, zona | Manual/auto | Notas incompletas |
| 4 | Match | CRM | CRM | Demanda↔oferta | Nativa/manual | Cruce en cabeza del agente |
| 5 | Visita | CRM | Calendar + WA | Fecha, dirección | Nativa/manual | Doble reserva |
| 6 | Feedback visita | WA/tel | CRM | Interés | Manual | No se documenta |
| 7 | Oferta | Email/WA | CRM + PDF | Precio, condiciones | Manual | Versiones divergentes |
| 8 | Arras | Plantilla | Firma e-sign | Contrato | Nativa/auto | Copia no vuelve al CRM |
| 9 | Docs legales | Email/Registro | Carpeta/CRM | Nota simple, CEE… | Manual | Checklist incompleto |
| 10 | Hipoteca | Cliente/banco | Email agencia | Preaprobación | Manual | Agente fuera del loop |
| 11 | Tasación | Tasadora | Banco (+ agencia) | Informe | Manual | Agente sin acceso |
| 12 | Escritura | Notaría | Registro | Escritura | Canal notarial | Fuera del stack agencia |
| 13 | Cobro | Facturación | Banco | Honorarios | Transfer/recibo | Descuadre comisión |
| 14 | Postventa | WA | — | Incidencias, review | Manual | Sin owner claro |

---

## 3. Flujo de captación de inmueble (oferta)

```text
Prospecto propietario
        ↓
Valoración (comparables / AVM / criterio)
        ↓
Mandato (firma electrónica o papel)
        ↓
KYC vendedor + documentación
        ↓
Brief foto / staging
        ↓
Ficha CRM (texto, fotos, extras)
        ↓
Publicación multiportal + web
        ↓
Portal del propietario (si Tools/CRM)
```

---

## 4. Dónde se rompe el flujo (preview)

Orden preliminar por impacto (detalle en [puntos-de-friccion](../07_analisis_transversal/puntos-de-friccion.md)):

1. Lead sin respuesta rápida / sin ficha CRM  
2. Conversación WhatsApp opaca  
3. Documentación y KYC manuales  
4. Desalineación precio/comparables  
5. Comisión/splits fuera de sistema  
6. Postventa sin proceso digital  

---

## Validación

- Proceso alineado con cadena de valor del módulo de mercado. **[Alta en el proceso de negocio]**
- Mecanismos tech: **media** (varían por arquetipo).
- Pendiente: tiempos medios lead→primer contacto por canal en España.

---

← [Integraciones](mapa-integraciones.md) | [Índice](../README.md) | [Siguiente: Datos →](modelos-datos-sistemas-registro.md)
