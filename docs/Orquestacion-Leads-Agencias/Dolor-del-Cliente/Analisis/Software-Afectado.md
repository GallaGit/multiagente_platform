# Software afectado

**Fecha de corte:** 12 de agosto de 2026  
**Universo:** se cuentan las menciones enlazadas de “Herramientas implicadas” en las 30 fichas.  
**Taxonomía canónica:** [`../../ecosistema_tecnologico/00_metodologia/alcance-y-taxonomia.md`](../../ecosistema_tecnologico/00_metodologia/alcance-y-taxonomia.md).  
**Advertencia de alcance:** una mención significa relación operativa, no que el software cause el problema ni que todas las agencias usen esa categoría.

## Método de conteo

- **Fichas**: número de fichas que mencionan al menos una herramienta de la categoría.
- **Menciones**: enlaces individuales a herramientas de la categoría; una ficha puede aportar varias.
- Se agrupan los enlaces por las cinco categorías canónicas. Dos enlaces a “modelos de datos y sistemas de registro” se informan aparte porque pertenecen a arquitectura y flujos, fuera de esas cinco categorías.
- No se cuentan menciones narrativas, marcas en evidencias ni plataformas sin ficha propia para evitar mezclar contexto con la sección de herramientas.

## Recuento por categoría canónica

| Categoría | Fichas | Menciones | Concentración observada |
|---|---:|---:|---|
| Core comercial y administrativo | 30 | 74 | CRM, gestores documentales, firma, ERP, MLS, facturación, contabilidad, PMS y banca/tesorería |
| Canales y productividad | 24 | 56 | Portales, email, WhatsApp Business, omnicanal, calendarios, VoIP, proyectos y suites de trabajo |
| Marketing y contenido | 9 | 14 | Web/CMS, analítica, marketing, fotografía y vídeo/tour virtual |
| Operaciones especializadas | 10 | 17 | Hipotecario, tasación/AVM, datos/geo, KYC-AML y coordinación postventa |
| Datos, automatización e IA | 17 | 19 | BI, automatización, gobierno/calidad, ciberseguridad e IA |
| **Total canónico** | **no sumable** | **180** | Las fichas se solapan entre categorías |

**Fuera del total canónico:** 2 menciones de arquitectura/modelos de datos, en [P06](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md) y [P13](../Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md).

## Herramientas con mayor presencia

| Herramienta canónica | Fichas que la mencionan | Interpretación prudente |
|---|---:|---|
| CRM | 29 | Es el registro y punto de coordinación más transversal; presencia no equivale a uso correcto ni a causalidad. |
| Gestores documentales | 14 | Aparecen donde hay versiones, expedientes, contratos, cumplimiento o continuidad. |
| Portales | 11 | Son canal de publicación y entrada de demanda; también existe dependencia y desincronización. |
| WhatsApp Business | 11 | Canal donde se manifiestan dispersión y pérdida de contexto, y medio actual de comunicación. |
| Email | 10 | Canal de documentos y coordinación; puede crear versiones paralelas o ser vector de BEC. |
| Firma electrónica | 9 | Palia evidencia y circulación contractual, pero no corrige redacción ni comprensión. |
| Atención omnicanal | 8 | Palia reparto y continuidad entre canales; depende de integración y disciplina. |
| Business Intelligence | 7 | Palia reporting, valoración y planificación; no corrige datos ausentes. |

Los recuentos anteriores son de fichas, no licencias, usuarios, fallos ni intensidad.

## Rol de la tecnología en el problema

### 1. Herramienta o restricción tecnológica que contribuye directamente

- [P05](../Problemas/05-dependencia-de-los-grandes-portales.md): la concentración de audiencia, reglas y datos en portales crea dependencia, aunque el canal también entregue valor.
- [P19](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md): el conjunto de conectores parciales, fuentes múltiples y restricciones de exportación contribuye; no hay un único producto culpable.
- [P22](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md): feeds, mapeos y reglas de CRM, web, MLS y portal pueden fallar o cubrir solo parte del dato; otros duplicados proceden de encargos abiertos.
- [P23](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md): funciones móviles, notificaciones, configuración y soporte son parte explícita de la fricción, con reseñas positivas que impiden generalizar.
- [P24](../Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md): credenciales, proveedores y canales amplían superficie, pero el daño depende también de controles, personas y proceso de pago.

### 2. Canal donde el problema se manifiesta

- Portales/web: [P02](../Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md), [P05](../Problemas/05-dependencia-de-los-grandes-portales.md), [P06](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md), [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P09](../Problemas/09-visitas-poco-productivas.md), [P22](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md) y [P30](../Problemas/30-retirada-de-agencias-del-mercado-de-alquiler.md).
- Email/WhatsApp/teléfono: [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P08](../Problemas/08-comunicacion-irregular-y-poca-visibilidad.md), [P12](../Problemas/12-postventa-saturada-en-obra-nueva.md), [P13](../Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md), [P15](../Problemas/15-proteccion-de-datos-en-canales-dispersos.md), [P16](../Problemas/16-arras-reservas-y-firmas-mal-definidas.md), [P19](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md), [P23](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md), [P24](../Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md) y [P29](../Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md).
- CRM/hojas/reporting: [P02](../Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md), [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P19](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md), [P21](../Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md) y [P23](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md).

### 3. Herramienta usada actualmente para paliarlo

- CRM, calendarios y omnicanal se usan para asignación, siguiente acción y continuidad en [P01](../Problemas/01-escasez-de-producto-y-competencia-por-captacion.md), [P02](../Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md), [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P08](../Problemas/08-comunicacion-irregular-y-poca-visibilidad.md), [P09](../Problemas/09-visitas-poco-productivas.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md) y [P29](../Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md).
- Gestores documentales y firma se usan para versiones, evidencia y archivo en [P04](../Problemas/04-dificultad-para-obtener-exclusivas.md), [P11](../Problemas/11-opacidad-de-honorarios-y-exclusivas.md), [P13](../Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md), [P14](../Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md), [P16](../Problemas/16-arras-reservas-y-firmas-mal-definidas.md), [P17](../Problemas/17-descoordinacion-entre-hipoteca-fein-y-notaria.md) y [P18](../Problemas/18-administracion-de-alquileres-y-normativa-cambiante.md).
- BI, gobierno de datos y automatización se usan para conciliación, control y alertas en [P03](../Problemas/03-valoraciones-poco-defendibles-y-precio-de-salida.md), [P06](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md), [P10](../Problemas/10-brecha-de-valoracion-y-negociacion.md), [P19](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md), [P21](../Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md), [P22](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md), [P27](../Problemas/27-rentabilidad-volatil-e-ingresos-contingentes.md) y [P28](../Problemas/28-estacionalidad-y-sensibilidad-al-ciclo-financiero.md).
- PMS y coordinación postventa se usan en [P12](../Problemas/12-postventa-saturada-en-obra-nueva.md), [P18](../Problemas/18-administracion-de-alquileres-y-normativa-cambiante.md) y [P30](../Problemas/30-retirada-de-agencias-del-mercado-de-alquiler.md), con alcances distintos.
- KYC-AML, identidad, MFA y backups se usan para controles en [P14](../Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md), [P15](../Problemas/15-proteccion-de-datos-en-canales-dispersos.md) y [P24](../Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md).

## Lectura y límites

1. La presencia casi universal del CRM refleja centralidad, no que el CRM sea la causa de 29 problemas.
2. En [P21](../Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md), Excel es una capa de compensación; no es por sí mismo el origen del dato deficiente.
3. En [P06](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md), [P14](../Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md) y [P18](../Problemas/18-administracion-de-alquileres-y-normativa-cambiante.md), una herramienta puede registrar campos sin validar contenido, criterio o legalidad.
4. En [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md) y [P29](../Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md), configuración, adopción, responsables y disciplina pesan tanto como la capacidad técnica.
5. Los precios, integraciones y funcionalidades cambian; el corte no permite atribuir una limitación a todas las versiones o proveedores.
