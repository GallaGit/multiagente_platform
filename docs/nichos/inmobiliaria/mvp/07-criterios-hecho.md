# 07 — Criterios de hecho

Cuándo el piloto técnico-operativo del sprint se considera **cumplido**. Distinto de “negocio validado” (pago recurrente).

## Hecho técnico-operativo (lab HubSpot)

- [x] Canal simulado ingestando a HubSpot con origen visible (`lead_origen`).
- [ ] ≥ 95 % de leads del periodo con responsable asignado según regla (o excepción documentada).
- [ ] ≥ 95 % de asignados con siguiente acción registrada.
- [x] SLA definido y medible; rupturas visibles en panel/métricas (KPI `sla_rotos`, SLA vencido en tabla, registro de 1ª respuesta desde panel).
- [x] Duplicados del caso de prueba no crean dos dueños (email/teléfono/origen+origen_ref).
- [x] Datos insuficientes terminan en cola `DATOS_INSUFICIENTES`, no en silencio.
- [x] Baseline y métricas post documentadas ([06-metricas.md](06-metricas.md)).
- [ ] Manual de ownership entregado (o borrador para lab).
- [x] API HubSpot + props custom operativas ([08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md)).
- [x] 3 casos operativos ejecutados y documentados (nuevo, duplicado, insuficiente) — [08-prueba-tecnica-hubspot.md](08-prueba-tecnica-hubspot.md) 2026-08-26

## Hecho técnico en cliente (producción, diferido)

- [ ] Prueba en CRM del cliente (Witei Smart Inbox u otro) — solo con piloto pagado.
- [x] Prueba de escritorio Witei cerrada ([08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md)) — referencia mercado, no lab activo.

## Hecho comercial (fuera de este brief, pero relacionado)

- [ ] Entrevistas / casos del [plan 90 días](../Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md).
- [ ] Piloto **pagado** o compromiso económico verificable.
- [ ] Disposición a mantener reglas tras el sprint.

Sin hecho comercial, el MVP técnico es demostración, no producto validado.

## No-go (parar o reformular)

- Imposible asignar dueño o registrar estado vía API/proceso acordado.
- Cliente exige WhatsApp personal o cobertura total de canales en el MVP.
- Sin sponsor interno ni acceso a datos de baseline.
- Expectativa de “IA que vende sola” como criterio de éxito.

## Siguiente después del hecho

1. Biblioteca de reglas/conectores reutilizables (mismo patrón CRM–canal).
2. Oferta gestionada / mantenimiento.
3. Solo entonces valorar capa SaaS o copiloto (roadmap de oferta).
4. Encargos de delivery en [plataforma-interna](../../plataforma-interna/) cuando haya trabajo técnico repetible.
