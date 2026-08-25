# Checklist — Piloto pagado

Operativa para implantar el Sprint de Orquestación de Leads en el **CRM de producción del cliente**. Este repo (lab HubSpot) valida lógica; el piloto es entrega en su entorno (Witei, Inmovilla u otro).

Referencias: [01-alcance](../mvp/01-alcance.md) · [03-modelo-datos](../mvp/03-modelo-datos.md) · [06-metricas](../mvp/06-metricas.md) · [08-prueba-tecnica-witei](../mvp/08-prueba-tecnica-witei.md) (cuando aplique mercado ES).

---

## Antes de firmar

- [ ] **Baseline acordado** — mismas métricas que [06-metricas](../mvp/06-metricas.md): leads entrados, % sin responsable, % sin siguiente acción, tiempo a 1ª respuesta, excepciones
- [ ] **Un flujo, un canal, un CRM** — sin multi-canal ni multi-sucursal en v1
- [ ] **Champion** operativo identificado (usa el CRM a diario)
- [ ] **Aprobador** económico participó en reunión de criterio de éxito
- [ ] **Acceso técnico** acordado (API, export, usuario admin, ventana de prueba)
- [ ] **Precio fijo**, duración (p. ej. 4–8 semanas), criterio de éxito y **salida** documentados
- [ ] **Alcance y exclusiones** firmados ([01-alcance](../mvp/01-alcance.md))
- [ ] Contrato / DPA / tratamiento de datos según RGPD
- [ ] Manual de ownership interno del cliente (quién resuelve excepciones)

---

## Día 1 piloto

- [ ] Acceso a CRM **producción** (no sandbox genérico sin datos reales)
- [ ] Campos/estados mínimos creados o mapeados ([03-modelo-datos](../mvp/03-modelo-datos.md))
- [ ] Reglas de asignación (round-robin o regla acordada) activas
- [ ] SLA primera respuesta configurado y visible
- [ ] **3 casos en entorno real** verificados:
  - [ ] Lead nuevo → owner + siguiente acción + SLA
  - [ ] Duplicado → mismo owner, sin segundo responsable
  - [ ] Datos insuficientes → excepción trazable
- [ ] Canal real conectado o ingest acordado (email portal, webhook, export programado)
- [ ] Cola de excepciones operativa (persona + SLA de resolución)
- [ ] Baseline “después del go-live técnico” capturado si aplica

---

## Durante el piloto

- [ ] Revisión semanal: excepciones abiertas >48 h, SLA rotos, incidencias de sync
- [ ] Registro de horas implantación y soporte (margen del servicio)
- [ ] Sin ampliar alcance sin change order
- [ ] Métricas semanales vs baseline acordado

---

## Cierre piloto

- [ ] Métricas **después** vs baseline (mismas definiciones)
- [ ] Informe: qué mejoró, qué no, limitaciones de datos
- [ ] Handoff: manual operativo, contactos, credenciales revocadas o rotadas
- [ ] Decisión cliente: continuar / mantenimiento / stop
- [ ] Lecciones para oferta repetible documentadas

---

## Qué no es este piloto

| No incluido | Motivo |
|---|---|
| Desplegar este repo como SaaS | Sin auth, multi-tenant ni deploy productivo |
| Automatizar outreach comercial | RGPD/LSSI — manual |
| Prometer ROI de conversión | Solo métricas de ejecución acordadas |
| Integrar todos los portales | Un canal en v1 |

---

## Enlaces

- [Discovery 90 días](CHECKLIST-discovery-90d.md)
- [Readiness](../../../READINESS.md)
- [Prueba técnica HubSpot (lab)](../mvp/08-prueba-tecnica-hubspot.md)
