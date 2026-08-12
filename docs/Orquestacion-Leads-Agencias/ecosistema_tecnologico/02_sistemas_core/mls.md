# MLS / colaboración entre agencias

**Corte:** agosto de 2026 · **Ámbito:** España · exclusivas compartidas / bolsas de colaboración

---

## 1. Función principal / problema que resuelve

Permitir que una agencia **comparta un encargo** (típicamente en exclusiva) con otras para ampliar demanda, repartiendo honorarios si otra oficina cierra.

**Capacidad anunciada:** bolsa de inmuebles, reglas de co-broke, sync con CRM.  
**Integración disponible:** nativa en varios CRM verticales ES (históricamente ligada a software de red).  
**Uso real:** desigual por provincia/red; no equivalente al MLS estadounidense. **[Media]**

---

## 2. Usuarios

Agentes captadores y vendedores; brokers de red/franquicia; admins de reglas de colaboración. Comprador/vendedor final no usa el MLS directamente.

---

## 3. Momento del flujo operativo

Tras captación (y según mandato): publicación interna en bolsa → otra agencia aporta demandante → visita/oferta → cierre y liquidación compartida. Paralelo a portales públicos.

---

## 4. Información gestionada

- Ficha de inmueble compartida (atributos, estado, exclusividad)
- Oficina captadora / oficina cerradora
- Condiciones de colaboración y % de reparto (comerciales; **no deben ser mínimos anticompetitivos**)
- Histórico de interesados entre oficinas (según sistema)

Intercambio de información sensible de precios/comisiones: zona de **riesgo de competencia**.

---

## 5. Integraciones

| Destino | Tipo |
|---------|------|
| CRM vertical (Inmovilla, Witei, Idealista Tools, etc.) | Nativa / API histórica |
| Portales | Indirecta (cada oficina publica) |
| Contabilidad / liquidación | Manual frecuente |
| Firmas / encargos | Manual |

---

## 6. Flujo de datos (ASCII)

```text
[Agencia A: captura] --alta MLS--> [Bolsa compartida]
                                      |
                                      v
                               [Agencia B: demanda]
                                      |
                                      v
                               [Cierre + split comisión]
                                      |
                                      v
                         [Liquidación (a menudo Excel)]
```

---

## 7. Limitaciones y tareas humanas

- Confianza entre oficinas; calidad de datos de la ficha compartida.
- Acuerdos de colaboración bilaterales fuera de plataforma.
- Cumplimiento post-CNMC: reglamentos con **comisiones mínimas** son de alto riesgo.
- No inventar ni publicar “cuotas de mercado MLS” sin censo.

---

## 8. Costes

Cuotas de asociación MLS / módulos CRM: **no público** de forma homogénea (a menudo embebido en licencia CRM o canon de franquicia). No estimar.

---

## 9. Competencia / enfoques

| Enfoque | Lógica | Riesgo / fricción |
|---------|--------|-------------------|
| **MLS de red/franquicia** | Inventario interno de marca | Lock-in; reglas de red |
| **MLS multi-software** | Interoperabilidad entre CRM | Complejidad; precedente CNMC |
| **Colaboración ad hoc** | WhatsApp/email entre agentes | Sin trazabilidad; informal |
| **Solo portales** | Demanda vía Idealista/Fotocasa | Sin split formal; competencia abierta |

Comparar enfoques por **gobernanza y competencia**, no solo por lista de marcas.

---

## 10. Nivel de adopción + confianza

Sin censo público nacional de participación MLS 2024–2026. Adopción: **habitual en algunas redes**; **poco utilizada** en independientes. **[Baja cuantitativa]**

---

## 11. Nivel de madurez + justificación

**Digitalizada** donde hay CRM+bolsa; muchas colaboraciones siguen **tradicionales** (teléfono). Automatización de liquidaciones: limitada. **[Media]**

---

## 12. Validación — riesgo CNMC 2021

La CNMC sancionó (dic. 2021) a Anaconda, Idealista, Inmovilla, Look & Find, MLS, Remax y Witei por acuerdos que, vía sistema MLS, imponían **comisiones mínimas** (p. ej. 4% venta / 1 mes alquiler en el relato del expediente) e intercambio de información que restringía la competencia. Multa conjunta ~**1,25 M€**. Fuente: [nota CNMC](https://www.cnmc.es/prensa/sancionador-proptech-cnmc-intermediacion-inmobiliaria-cnmc-20211209). **[Alta]**

Implicación para el stack: integración MLS↔CRM es **técnica**; las **reglas comerciales** deben evitar mínimos e intercambio anticompetitivo.

Pendiente: estado actual de bolsas post-sanción (sin inventar).

---

← [PMS](property-management.md) | [Índice](../README.md) | [Siguiente: Documental →](gestores-documentales.md)
