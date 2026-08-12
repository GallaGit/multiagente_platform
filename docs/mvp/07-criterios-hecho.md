# 07 — Criterios de hecho

Cuándo el piloto técnico-operativo del sprint se considera **cumplido**. Distinto de “negocio validado” (pago recurrente).

## Hecho técnico-operativo (piloto)

- [ ] Canal único ingestando a Witei con origen visible.
- [ ] ≥ 95 % de leads del periodo con responsable asignado según regla (o excepción documentada).
- [ ] ≥ 95 % de asignados con siguiente acción registrada.
- [ ] SLA definido y medible; rupturas generan alerta/cola.
- [ ] Duplicados del caso de prueba no crean dos dueños.
- [ ] Fallo de sync simulado termina en cola `SYNC_FALLIDO`, no en silencio.
- [ ] Baseline y métricas post documentadas ([06-metricas.md](06-metricas.md)).
- [ ] Manual de ownership entregado al cliente.
- [x] Prueba técnica de escritorio Witei cerrada ([08-prueba-tecnica-witei.md](08-prueba-tecnica-witei.md)): ingesta = Smart Inbox.
- [ ] Prueba operativa en cuenta real (3 emails: nuevo, duplicado, insuficiente).
- [ ] Limitaciones API Clientes explícitas al cliente (no REST inmediato salvo habilitación).

## Hecho comercial (fuera de este brief, pero relacionado)

- [ ] Entrevistas / casos del [plan 90 días](../Orquestacion-Leads-Agencias/Estrategia-Comercial/06-Plan-comercial-90-dias.md).
- [ ] Piloto **pagado** o compromiso económico verificable.
- [ ] Disposición a mantener reglas tras el sprint.

Sin hecho comercial, el MVP técnico es demostración, no producto validado.

## No-go (parar o reformular)

- Imposible asignar dueño o tareas vía API/proceso acordado.
- Cliente exige WhatsApp personal o cobertura total de canales en el MVP.
- Sin sponsor interno ni acceso a datos de baseline.
- Expectativa de “IA que vende sola” como criterio de éxito.

## Siguiente después del hecho

1. Biblioteca de reglas/conectores reutilizables (mismo CRM–canal).
2. Oferta gestionada / mantenimiento.
3. Solo entonces valorar capa SaaS o copiloto (roadmap de oferta).
4. Encargos de delivery en [plataforma-interna](../plataforma-interna/) cuando haya trabajo técnico repetible.
