# Readiness — Lab, piloto y producción

Veredicto explícito de qué está listo **hoy** con este repositorio y qué requiere trabajo aparte.

| Listo para | Estado |
|------------|--------|
| **Demo interna / laboratorio HubSpot** | Sí — orquestación, 3 casos, panel, KPIs con filtro MVP y baseline |
| **Discovery comercial** (entrevistas, mostrar panel) | Sí — con guion y límites ([checklist discovery](nichos/inmobiliaria/operacion/CHECKLIST-discovery-90d.md)) |
| **Piloto pagado en CRM del cliente** | No automático — implantación aparte, contrato, acceso ([checklist piloto](nichos/inmobiliaria/operacion/CHECKLIST-piloto-pagado.md)) |
| **Producción SaaS / clientes reales en este repo** | **No** — sin auth, sin deploy, canal simulado, SSL dev |

---

## Matriz por área

| Área | Lab (hoy) | Piloto cliente | Producción SaaS |
|------|-----------|----------------|-----------------|
| Orquestación leads | OK — HubSpot + `/leads/ingest` | Re-implantar en CRM cliente (Witei/Inmovilla/…) | N/A en este repo |
| Auth / multi-tenant | No | N/A (cuenta única cliente) | Requerido |
| Deploy / observabilidad | No (uvicorn local) | Manual, entrega proyecto | Requerido |
| Canal real | Simulado (JSON ingest) | Email/portal real del cliente | Por cliente |
| RGPD / LSSI outreach | Manual | Contrato + DPA | Requerido |
| Métricas baseline | OK — `POST/GET /leads/baseline`, panel delta | Medir en CRM cliente | Producto |
| Filtro métricas MVP | OK — `mvp_only=true` (default) | Propiedades equivalentes en CRM cliente | Producto |
| Mediana 1ª respuesta | OK si ≥2 leads con timestamps | Depende de registro fiable en CRM | Producto |
| Agentes / chat interno | OK (Groq, orquestador FE/BE) | Fuera de alcance piloto v1 | Plataforma interna |
| Research ICP | OK (evidencia pública) | No sustituye discovery | Manual + cumplimiento |

---

## Lab HubSpot — capacidades actuales

- Ingesta simulada portal → contacto HubSpot con owner, SLA, siguiente acción
- Dedupe por email/teléfono, excepción `DATOS_INSUFICIENTES`
- Panel `/` con KPIs, tabla, cola excepciones
- Métricas solo leads MVP (`lead_origen`) por defecto
- Snapshot baseline local (`data/baseline.json`) y comparación en panel
- Prueba técnica documentada: [08-prueba-tecnica-hubspot.md](nichos/inmobiliaria/mvp/08-prueba-tecnica-hubspot.md)

---

## Camino recomendado

```text
Lab (este repo) → Discovery + baseline manual en agencias
                → Piloto pagado en CRM cliente (entrega aparte)
                → Oferta repetible → eventual SaaS (otro esfuerzo)
```

No usar este stack como despliegue multi-cliente sin auth, aislamiento de datos y canal real.

---

## Enlaces

- [README del repo](../README.md)
- [06-metricas (baseline)](nichos/inmobiliaria/mvp/06-metricas.md)
- [Checklist discovery 90d](nichos/inmobiliaria/operacion/CHECKLIST-discovery-90d.md)
- [Checklist piloto pagado](nichos/inmobiliaria/operacion/CHECKLIST-piloto-pagado.md)
- [Alineación agentes](../.agents/rules/ALINEACION.md)
