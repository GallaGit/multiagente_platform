# 01 — Alcance

Oferta de referencia: [Servicio profesional — Sprint de Orquestación de Leads](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md).

## Cliente

**ICP-01:** agencia residencial independiente, 3–20 agentes, CRM activo (referencia: Witei), más de un canal de demanda, responsable interno de CRM/ops, dirección con autonomía de compra.

Fuera de foco: equipos 0–2 sin capacidad, franquiciados sin autonomía tech, grandes operadores, agencias sin CRM.

## Incluye

- Diagnóstico corto y **línea base** (métricas en [06-metricas.md](06-metricas.md)).
- Diseño de reglas: entrada, deduplicación, reparto, SLA, seguimiento ([05-reglas.md](05-reglas.md)).
- Integración de **un CRM (Witei)** + **un canal** prioritario ([04-integraciones.md](04-integraciones.md)).
- Campos y estados mínimos ([03-modelo-datos.md](03-modelo-datos.md)).
- Alertas de excepción y cola de revisión humana.
- Panel operativo básico (vista CRM nativa, lista filtrada o tablero iPaaS — lo más simple que cumpla).
- Pruebas: caso normal, duplicado, fallo de sync.
- Manual breve de operación / ownership / handoff.
- Medición antes/después en el periodo acordado.

## No incluye

- Bot autónomo de venta o scoring discriminatorio.
- Sustitución o migración de CRM.
- Captación / compra de leads / campañas.
- WhatsApp personal, voz, cobertura de todos los portales.
- Expediente, KYC/AML, firma, pagos, notaría.
- Garantía de conversión, captación o ingresos.
- Producto SaaS multi-cliente.

## Duración orientativa del sprint

| Fase | Orientación |
|---|---|
| Diagnóstico + baseline | 3–5 días laborables |
| Diseño reglas + campos | 2–4 días |
| Integración + pruebas | 5–10 días (depende de API/permisos) |
| Operación asistida + medición | 2–4 semanas |

Cifras orientativas; el contrato comercial las fija por cliente. Sin acceso API o datos de prueba, el calendario se alarga o se reformula.

## Stack fijado en este brief

- CRM: **Witei**
- Canal: **uno** (portal→email/webhook **o** formulario web)
- Motor: **n8n o Make** + configuración CRM

Variante Inmovilla: mismo alcance funcional; otra ficha de integración ([04-integraciones.md](04-integraciones.md)).
