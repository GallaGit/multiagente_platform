# Contexto del negocio

## Propósito

Este repositorio construye una **empresa digital especializada en optimización de procesos para inmobiliarias en España**, operada progresivamente mediante agentes, automatizaciones y supervisión humana.

La empresa no se define por una tecnología concreta. Investiga el negocio del cliente, diagnostica sus procesos, propone una mejora, la implementa, la prueba, la entrega y, cuando existe valor recurrente, la mantiene.

**No vendemos tecnología. Vendemos resultados operativos medibles.**

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

Ayudar a inmobiliarias a reducir tiempo, costes, errores y pérdida de trazabilidad mediante:

- optimización de procesos;
- automatización de tareas repetitivas;
- integración de sistemas;
- gobierno del dato;
- inteligencia artificial cuando aporte una ventaja demostrable.

El orden es:

`Problema → Diagnóstico → Optimización → Automatización → Integración → IA`

Nunca al revés.

---

# Nicho inicial

El mercado inicial es **España** y el primer nicho son las **agencias inmobiliarias**.

El cliente prioritario actual es una agencia residencial independiente profesionalizada, con CRM activo, varios canales y autonomía para cambiar procesos e integraciones.

Después de validar y repetir el modelo podrán añadirse otros actores del mismo ecosistema:

- promotoras y comercializadoras de obra nueva;
- administradores de fincas;
- gestoras patrimoniales y empresas de alquiler;
- constructoras y empresas de reformas.

La expansión no debe ocurrir antes de demostrar capacidad de venta, entrega y mantenimiento en el nicho inicial.

---

# Problemas que resolvemos

Las inmobiliarias operan procesos distribuidos entre CRM, portales, email, WhatsApp, hojas de cálculo, calendarios y carpetas. Los fallos aparecen principalmente en los traspasos entre herramientas y personas.

Áreas observadas:

- entrada, asignación y seguimiento de leads;
- conversaciones que no regresan al CRM;
- programación de visitas y coordinación de agendas;
- gestión documental y expedientes;
- publicación y actualización de inmuebles;
- comunicación con clientes y propietarios;
- reporting y calidad de datos;
- integración entre plataformas;
- continuidad cuando cambia o falta una persona.

La empresa no automatiza un proceso por ser manual. Primero confirma frecuencia, impacto, owner, viabilidad técnica y disposición a pagar.

---

# Qué somos y qué no somos

## Somos

- una empresa vertical de optimización y automatización para inmobiliarias;
- una firma de investigación, consultoría e implementación;
- una operación documentada que acumula conocimiento reutilizable;
- una empresa asistida por agentes, con control humano.

## No somos

- una agencia de desarrollo web o software generalista;
- una empresa de chatbots;
- una consultoría tecnológica para cualquier sector;
- un proveedor que vende “IA” sin proceso ni evidencia;
- un SaaS horizontal desde el primer día;
- un experimento académico o proyecto de aprendizaje.

Podemos desarrollar software para entregar una solución, pero el cliente compra un resultado de negocio, no “horas de programación”.

---

# Arquitectura del negocio: dos capas

## 1. Producto y servicios externos

Es lo que la empresa vende al cliente.

La primera oferta priorizada es el **Sprint de Orquestación de Leads**, precedido por un diagnóstico corto. Busca que cada lead del alcance tenga origen, responsable, SLA, siguiente acción y resultado trazable.

Esta oferta no define toda la empresa. Es el primer vehículo para:

- obtener clientes e ingresos;
- aprender con operaciones reales;
- validar disposición a pagar;
- descubrir patrones repetibles;
- crear activos para futuras ofertas.

Documentación:

- investigación y oferta: [`Orquestacion-Leads-Agencias/`](Orquestacion-Leads-Agencias/);
- brief técnico: [`mvp/`](mvp/);
- roadmap comercial: [`roadmap/producto.md`](roadmap/producto.md).

## 2. Plataforma interna

Es el sistema operativo con el que la empresa ejecutará su propio trabajo:

`Comercial → Operaciones → Delivery técnico → QA → Entrega → Soporte`

Roles futuros:

- estrategia y orquestación de empresa;
- research / inteligencia de mercado;
- sales / discovery / propuestas;
- legal y compliance;
- operaciones e implantación;
- delivery técnico;
- QA y seguridad;
- despliegue y entrega;
- soporte, mantenimiento y finanzas.

El módulo **Orchestrator + Frontend + Backend** vive dentro de **delivery técnico**. No representa toda la empresa:

- Orchestrator: convierte un encargo aprobado en un brief y lo enruta;
- Frontend: implementa paneles, interfaces y experiencia de usuario;
- Backend: implementa APIs, datos, webhooks y conectores.

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

1. [`CONTEXT.md`](CONTEXT.md): identidad, visión y límites de la empresa.
2. [`Orquestacion-Leads-Agencias/`](Orquestacion-Leads-Agencias/): fuente de verdad de mercado, problemas, ICP, competencia y oferta.
3. [`mvp/`](mvp/): especificación técnica de la primera oferta.
4. [`plataforma-interna/`](plataforma-interna/): arquitectura del sistema operativo interno.
5. [`roadmap/producto.md`](roadmap/producto.md): secuencia activa de validación y crecimiento.

Cada decisión relevante debe incluir:

- evidencia y fecha;
- supuesto o limitación;
- responsable;
- métrica o criterio de hecho;
- próximo experimento;
- condición de avance, pausa o descarte.

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

---

# Estrategia de crecimiento

## Etapa 1 — Especialización y primera oferta

- consolidar conocimiento de agencias inmobiliarias;
- validar el Sprint de Orquestación de Leads;
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
- expansión al ecosistema inmobiliario;
- internacionalización cuando el modelo local sea estable.

---

# Estado actual

**Estado: transición de investigación estratégica a validación técnica y comercial.**

Completado:

- investigación del mercado y ecosistema inmobiliario;
- análisis de dolores, competencia, oportunidades e ICP;
- definición del portafolio y primera oferta priorizada;
- brief técnico del Sprint de Orquestación de Leads;
- prueba de escritorio sobre Witei y Smart Inbox;
- alineación inicial de la plataforma interna con el flujo de empresa.

Pendiente inmediato:

1. crear una cuenta Witei y ejecutar la prueba real de Smart Inbox;
2. registrar resultados de alta, duplicado, asignación y datos insuficientes;
3. realizar discovery con agencias del ICP;
4. confirmar problema pagable, baseline y acceso técnico;
5. proponer y cerrar un piloto pagado;
6. automatizar la plataforma interna solo a partir de trabajo real y repetible.

No estamos construyendo todavía un SaaS ni una empresa completamente autónoma. Estamos construyendo una empresa real, vertical y asistida por agentes, empezando por una oferta concreta que permita vender, entregar y aprender con evidencia.
