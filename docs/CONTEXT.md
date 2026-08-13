# Contexto del negocio

## Propósito

Este repositorio construye una **empresa digital de continuidad operativa**, operada progresivamente mediante agentes, automatizaciones y supervisión humana.

La empresa no se define por una tecnología concreta. Investiga el negocio del cliente, diagnostica sus procesos, propone una mejora, la implementa, la prueba, la entrega y, cuando existe valor recurrente, la mantiene.

**No vendemos tecnología. Vendemos resultados operativos medibles.**

El nicho activo (hoy: inmobiliaria) vive en [`nichos/`](nichos/). Los agentes son oficios reutilizables; el sector entra por el pack del nicho.

---

# Visión

Construir una empresa rentable, sostenible y escalable capaz de ejecutar el flujo de trabajo de una firma pequeña:

`investigar mercado → encontrar cliente ideal → discovery → propuesta → acuerdo → diagnóstico → implementación → QA → despliegue → entrega → soporte`

Los agentes ayudarán a ejecutar y documentar cada etapa. No sustituyen la responsabilidad empresarial ni las aprobaciones humanas en decisiones comerciales, legales, financieras, de seguridad o de producción.

La evolución prevista es:

1. servicios de diagnóstico e implementación;
2. servicios productizados y mantenimiento;
3. activos reutilizables (reglas, conectores, controles y playbooks);
4. productos propios, copilotos y SaaS cuando exista repetición demostrada.

---

# Misión

Ayudar a empresas del nicho activo a reducir tiempo, costes, errores y pérdida de trazabilidad mediante:

- optimización de procesos;
- automatización de tareas repetitivas;
- integración de sistemas;
- gobierno del dato;
- inteligencia artificial cuando aporte una ventaja demostrable.

El orden es:

`Problema → Diagnóstico → Optimización → Automatización → Integración → IA`

Nunca al revés.

---

# Qué somos y qué no somos

## Somos

- una empresa vertical de optimización y automatización (un nicho a la vez);
- una firma de investigación, consultoría e implementación;
- una operación documentada que acumula conocimiento reutilizable;
- una empresa asistida por agentes, con control humano.

## No somos

- una agencia de desarrollo web o software generalista;
- una empresa de chatbots;
- una consultoría tecnológica para cualquier sector a la vez;
- un proveedor que vende “IA” sin proceso ni evidencia;
- un SaaS horizontal desde el primer día;
- un experimento académico o proyecto de aprendizaje.

Podemos desarrollar software para entregar una solución, pero el cliente compra un resultado de negocio, no “horas de programación”.

---

# Arquitectura del negocio: dos capas

## 1. Producto y servicios externos

Es lo que la empresa vende al cliente. La oferta concreta vive en el [nicho activo](nichos/inmobiliaria/).

Esta oferta no define toda la empresa. Es el vehículo para obtener clientes, aprender con operaciones reales y crear activos.

## 2. Plataforma interna

Es el sistema operativo con el que la empresa ejecutará su propio trabajo:

`Comercial → Operaciones → Delivery técnico → QA → Entrega → Soporte`

El módulo **Orchestrator + Frontend + Backend** vive dentro de **delivery técnico**. No representa toda la empresa.

Documentación: [`plataforma-interna/`](plataforma-interna/).

---

# Flujo operativo objetivo

| Etapa | Resultado | Control humano |
|---|---|---|
| Investigación | ICP, cuenta y problema con evidencia | Aprobar prioridad |
| Prospección | Cuenta contactable y razón de contacto | Cumplimiento y oposición |
| Discovery | Problema, baseline, owner y acceso técnico | Validar necesidad |
| Propuesta | Alcance, precio, métricas y exclusiones | Aprobar oferta |
| Legal | Acuerdo, privacidad, responsabilidades y salida | Firma humana obligatoria |
| Diagnóstico | Mapa de proceso, datos y riesgos | Aprobación del cliente |
| Implementación | Configuración, integración o software | Accesos mínimos |
| QA | Casos normales, duplicados, fallos y rollback | Gate antes de producción |
| Deploy | Cambio controlado y observable | Aprobación de producción |
| Entrega | Handoff, manual, ownership y baseline final | Aceptación del cliente |
| Mantenimiento | Monitorización, incidencias y mejora | Alcance recurrente acordado |

Los agentes pueden proponer, preparar y ejecutar tareas reversibles. No deben firmar contratos, mover dinero, asumir obligaciones legales, desplegar cambios críticos ni comunicarse externamente sin las autorizaciones definidas.

---

# Modelo de conocimiento y documentación

La documentación es la memoria verificable del negocio y el contexto compartido de los agentes.

Jerarquía:

1. [`CONTEXT.md`](CONTEXT.md): identidad, visión y límites de la empresa (transversal).
2. [`nichos/<id>/`](nichos/): mercado, problemas, ICP, oferta y contexto ejecutable del nicho.
3. [`plataforma-interna/`](plataforma-interna/): arquitectura del sistema operativo interno.

Cada decisión relevante debe incluir evidencia, supuesto, responsable, métrica, próximo experimento y condición de avance.

---

# Principios

- Negocio antes que tecnología.
- Problema antes que solución.
- Servicios antes que SaaS.
- Medición antes que promesas de ROI.
- Un flujo acotado antes que una plataforma completa.
- Humano responsable en decisiones irreversibles o sensibles.
- Privilegio mínimo para datos, herramientas y credenciales.
- Automatización observable, con excepciones y salida manual.
- Especialización antes que expansión.
- Activos reutilizables antes que personalización infinita.
- Evidencia real antes que autonomía de agentes.
- El nicho entra por pack (`docs/nichos/`), no por el código de los agentes.

---

# Estrategia de crecimiento

## Etapa 1 — Especialización y primera oferta

- consolidar conocimiento del nicho activo;
- validar la primera oferta productizada;
- ejecutar una prueba técnica real y discovery comercial;
- conseguir al menos un compromiso económico.

## Etapa 2 — Repetición y operación interna

- repetir el mismo problema en clientes comparables;
- medir coste de entrega y soporte;
- crear playbooks, reglas y conectores;
- automatizar partes reales del flujo interno de la empresa.

## Etapa 3 — Servicios avanzados y recurrencia

- mantenimiento y continuidad operativa;
- nuevas automatizaciones del mismo nicho;
- copilotos asistivos sobre datos gobernados.

## Etapa 4 — Producto

- convertir patrones repetidos en producto configurable;
- validar onboarding, soporte, retención y margen.

## Etapa 5 — SaaS y expansión

- SaaS vertical solo con repetición y economía demostradas;
- expansión a actores adyacentes del mismo ecosistema;
- otro nicho solo cuando el modelo local sea estable.

---

# Estado actual

**Estado: transición de investigación estratégica a validación técnica y comercial.**

Nicho activo: [inmobiliaria](nichos/inmobiliaria/CONTEXTO.md). Plataforma: [plataforma-interna](plataforma-interna/).
