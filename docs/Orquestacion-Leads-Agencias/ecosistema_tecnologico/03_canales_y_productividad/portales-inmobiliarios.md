# Portales inmobiliarios

**Corte:** agosto de 2026 · **Ámbito:** España · **Confianza global de la ficha:** media-alta en rol regulatorio; baja en cuotas y tarifas

---

## 1. Función principal

Escaparate digital de oferta (venta/alquiler) y canal de captación de demanda. Generan leads (consultas) hacia la agencia; **no** son intermediarios jurídicos de la operación.

La CNMC trata Idealista y Fotocasa como **plataformas de anuncios** (no intermediarios): permiten venta directa y, en el caso de Idealista, ofrecen herramientas CRM a agencias. [CNMC S/0003/20](https://www.cnmc.es/sites/default/files/3831141.pdf) · **[Alta]**

---

## 2. Usuarios

| Rol | Uso típico |
|-----|------------|
| Agente / comercial | Publicar, responder leads, destacar anuncios |
| Captador / director | Packs, posicionamiento, reporting de contactos |
| Propietario particular | Anuncio directo (competencia de la agencia en el mismo canal) |
| Admin / CRM | Importar leads, sincronizar inventario |

---

## 3. Momento del flujo

Captación de **oferta** (encargos publicados) y **demanda** (leads) → cualificación → visita. También refuerzo de marca local vía presencia continua. Intervienen poco en firma, hipoteca o postventa.

---

## 4. Información gestionada

| Dato | Origen | Destino habitual |
|------|--------|------------------|
| Ficha inmueble (precio, m², fotos, CEE…) | Agencia / particular | Portal |
| Consulta / lead (nombre, email, teléfono, mensaje) | Demandante vía portal | Email de la agencia · API · inbox CRM |
| Estadísticas de contacto / visitas anuncio | Portal | Panel profesional |
| Inventario publicado | CRM o carga manual | Portal |

---

## 5. Integraciones

| Tipo | Situación observada |
|------|---------------------|
| **Nativa** | Idealista Tools (Starter/Office) como CRM del propio Idealista; connectors CRM↔portal en varios fabricantes ES |
| **API** | APIs profesionales / partners para publicación y, en algunos casos, leads; acceso y alcance **bajo contrato**, no homogéneo público |
| **Automatización** | Parsing de emails de lead (iPaaS, Idealista Tools «importación de leads de otros portales») |
| **Manual** | Muy frecuente: copiar lead del email al CRM; republicar fichas |
| **Inexistente** | Cuota de mercado pública comparable 2024–2026; tarifa pública homogénea de packs |

---

## 6. Flujo de datos (ASCII)

```text
[Inventario agencia]
        |  carga manual / API / CRM
        v
[Idealista | Fotocasa | Habitaclia | Pisos.com | Milanuncios]
        |  lead (email / API / inbox Tools)
        v
[Bandeja email / Idealista Tools / CRM]
        |  a menudo copia manual
        v
[WhatsApp / llamada / visita]
```

---

## 7. Limitaciones y tareas humanas

- Respuesta rápida al lead: el portal no cualifica ni agenda por la agencia.
- Duplicidad de fichas entre portales y desfase de precio/estado.
- Lead llega sin contexto CRM; riesgo de no registrar canal ni resultado.
- Particular compite en el mismo escaparate (efecto CNMC).
- Dependencia de packs/destacados **opacos** en precio.

---

## 8. Costes

| Concepto | Dato público | Fuente |
|----------|--------------|--------|
| Packs Idealista / Fotocasa / Habitaclia / Pisos.com | **No público / bajo presupuesto** (sin tarifa homogénea comparable 2024–2026) | Metodología costes del módulo · **[Alta sobre el hueco]** |
| Idealista Tools Starter / Office | Precio **no publicado** en ficha de ayuda consultada | [Idealista Tools Office](https://www.idealista.com/tools/centrodeayuda/articulos/descubre-la-version-office-de-idealista-tools/) · **[Media]** |
| Milanuncios (clasificados) | Modelos freemium/destacados variables; no tratar blogs como tarifa oficial | — · **[Baja]** |

**No se inventan** importes de «Gold/Premium» a partir de blogs. Pendiente: tarifas reales por provincia/pack.

---

## 9. Competencia / enfoques

| Actor | Enfoque |
|-------|---------|
| **Idealista** | Portal dominante percibido + Idealista Tools (CRM) + leads email/API |
| **Fotocasa** (Adevinta) | Portal generalista; packs profesionales |
| **Habitaclia** | Fuerte en Catalunya / Baleares (ecosistema Adevinta) |
| **Pisos.com** | Alternativa nacional; presencia irregular según zona |
| **Milanuncios** | Clasificados; mezcla particular/profesional; menor «producto agencia» |

Sin cuota pública reciente: **no asignar % de mercado**. **[Alta sobre el hueco]** · Ver [Mercado_y_tendencias §5](../../Situacion_en_España/Mercado_y_tendencias.md).

---

## 10. Adopción

| Nivel | Lectura |
|-------|---------|
| **Muy extendida** | Casi imposible operar intermediación residencial sin al menos un portal grande |
| Confianza | **Alta** cualitativa; **baja** cuantitativa (sin panel de gasto/uso por agencia) |

Microagencias: a menudo 1–2 portales + email. Medianas/grandes: multi-portal + CRM sync.

---

## 11. Madurez

**Digitalizada → parcialmente automatizada** en uso típico ES:

- Publicación y leads son digitales.
- La sincronización CRM↔portal y el cierre del embudo siguen siendo manuales en muchas micro/medianas.
- Idealista Tools acerca un CRM nativo del canal, pero no elimina la fragmentación multi-portal ni WhatsApp.

No es «impulsada por IA» a escala de agencia media pese a features de recomendación en el lado consumidor.

---

## 12. Validación

| Afirmación | Evidencia | Confianza | Pendiente |
|------------|-----------|-----------|-----------|
| Portales = plataformas de anuncios, no intermediarios | CNMC PDF | Alta | — |
| Sin cuota pública Idealista/Fotocasa 2024–2026 | Hueco declarado módulo + Situacion_en_España | Alta | Estudio audiencia/cuota comparable |
| Leads por email / API / Tools | Docs Tools + práctica sectorial | Media-alta | % real API vs email |
| Gasto portal = partida tech dominante | Observación sectorial | Media-baja | Contabilidad anonimizada |

**Discrepancia:** blogs asignan cuotas/%; este informe **no las reproduce**.

---

← [Bancos](../02_sistemas_core/bancos.md) | [Índice](../README.md) | [Siguiente: Email →](email.md)
