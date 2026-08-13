# Ranking de problemas

**Fecha de corte:** 12 de agosto de 2026  
**Universo:** las 30 fichas de [`../Problemas/`](../Problemas/).  
**Alcance:** priorización para *discovery* en agencias inmobiliarias españolas; no es una estimación de TAM, prevalencia estadística ni voluntad de pago.

## Método

Se aplica literalmente la fórmula de [`../Metodologia.md`](../Metodologia.md):

`(impacto / 4 × 35) + (frecuencia / 4 × 25) + (urgencia / 4 × 20) + (validabilidad / 4 × 20)`

- Impacto: Muy alto = 4; Alto = 3; Medio = 2; Bajo = 1.
- Frecuencia: Muy frecuente = 4; Frecuente = 3; Ocasional = 2; Poco frecuente = 1.
- Urgencia: Muy alta/Crítica = 4; Alta = 3; Media = 2; Baja = 1.
- Validabilidad adicional: 4 = observación o registro accesible y métrica concreta; 3 = contraste viable, pero exige muestra, permisos o segmentación; 2 = señal principalmente estructural o causalmente difícil; 1 = evidencia adicional difícil de obtener.
- Los decimales se conservan sin normalizar ni convertirlos a variables económicas. En empates, el orden es expositivo.

## Ranking completo

| # | Problema | I | F | U | V | Score | Validabilidad adicional asignada |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | [P01 · Escasez de producto y competencia por captación](../Problemas/01-escasez-de-producto-y-competencia-por-captacion.md) | 4 | 4 | 4 | 3 | 95,00 | Entrevistas y CRM permiten medir intentos por encargo, pero separar escasez de ejecución exige segmentar zona y tipología. |
| 2 | [P27 · Rentabilidad volátil e ingresos contingentes](../Problemas/27-rentabilidad-volatil-e-ingresos-contingentes.md) | 4 | 4 | 3 | 4 | 95,00 | Contabilidad, pipeline y fechas de cobro permiten reconstruir caídas, costes previos y desfase de caja. |
| 3 | [P18 · Administración de alquileres y normativa cambiante](../Problemas/18-administracion-de-alquileres-y-normativa-cambiante.md) | 4 | 3 | 4 | 4 | 93,75 | Contratos, cobros, fianzas e incidencias son auditables por modalidad y comunidad autónoma. |
| 4 | [P24 · Riesgo de ciberseguridad en datos y pagos](../Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md) | 4 | 3 | 4 | 4 | MFA, accesos, backups y protocolos de pago pueden verificarse con auditoría y simulaciones controladas. |
| 5 | [P06 · Anuncios incompletos, inconsistentes o desactualizados](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md) | 3 | 4 | 4 | 4 | Una muestra de anuncios puede cotejarse campo a campo con ficha maestra y documentación vigente. |
| 6 | [P03 · Valoraciones poco defendibles y precio de salida](../Problemas/03-valoraciones-poco-defendibles-y-precio-de-salida.md) | 4 | 3 | 4 | 3 | Es contrastable contra cierres y comparables, aunque el acceso y la heterogeneidad local limitan la muestra. |
| 7 | [P14 · Cumplimiento PBC/AML difícil de ejecutar](../Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md) | 4 | 3 | 4 | 3 | Una auditoría de expedientes muestra trazabilidad, pero el acceso es sensible y el riesgo varía por caso. |
| 8 | [P15 · Protección de datos en canales dispersos](../Problemas/15-proteccion-de-datos-en-canales-dispersos.md) | 4 | 3 | 4 | 3 | El inventario de copias y accesos es observable, aunque requiere permisos y tratamiento de evidencia sensible. |
| 9 | [P30 · Retirada de agencias del mercado de alquiler](../Problemas/30-retirada-de-agencias-del-mercado-de-alquiler.md) | 4 | 3 | 3 | 4 | Encuestas comparables y datos de cartera permiten medir altas, retiradas y peso de cada causa declarada. |
| 10 | [P12 · Postventa saturada en obra nueva](../Problemas/12-postventa-saturada-en-obra-nueva.md) | 3 | 4 | 3 | 4 | Los tickets permiten medir volumen, responsable, reincidencia y tiempo de resolución por promoción. |
| 11 | [P11 · Opacidad de honorarios y exclusivas](../Problemas/11-opacidad-de-honorarios-y-exclusivas.md) | 3 | 3 | 4 | 4 | Encargos, presupuestos y reclamaciones permiten auditar desglose, comprensión y devengo. |
| 12 | [P10 · Brecha de valoración y negociación](../Problemas/10-brecha-de-valoracion-y-negociacion.md) | 4 | 3 | 3 | 3 | Se puede comparar salida, ofertas y cierre, pero faltan datos homogéneos y atribución de la decisión final. |
| 13 | [P05 · Dependencia de los grandes portales](../Problemas/05-dependencia-de-los-grandes-portales.md) | 3 | 4 | 3 | 3 | Facturas y atribución por canal son accesibles, pero los recorridos multicanal dificultan medir dependencia neta. |
| 14 | [P25 · Brecha de formación profesional y digital](../Problemas/25-brecha-de-formacion-profesional-y-digital.md) | 3 | 4 | 3 | 3 | Pruebas y cohortes antes/después son viables, pero aislar formación de experiencia y mercado exige seguimiento. |
| 15 | [P13 · Expedientes incompletos y documentación descoordinada](../Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md) | 3 | 3 | 3 | 4 | Una revisión de expedientes puede medir completitud temprana, versiones, incidencias y retrasos. |
| 16 | [P16 · Arras, reservas y firmas mal definidas](../Problemas/16-arras-reservas-y-firmas-mal-definidas.md) | 3 | 3 | 3 | 4 | Contratos y certificados de firma permiten clasificar cláusulas, versiones y condiciones financieras. |
| 17 | [P17 · Descoordinación entre hipoteca, FEIN y notaría](../Problemas/17-descoordinacion-entre-hipoteca-fein-y-notaria.md) | 3 | 3 | 3 | 4 | Las fechas de arras, tasación, FEIN, acta y escritura hacen medibles demoras y prórrogas. |
| 18 | [P19 · Fragmentación del stack y duplicidad de datos](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md) | 3 | 3 | 3 | 4 | Exportaciones y observación permiten contar duplicados, reintroducciones y actividades fuera del CRM. |
| 19 | [P20 · Automatización parcial del flujo comercial](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md) | 3 | 3 | 3 | 4 | Logs y recorridos de casos permiten contar traspasos manuales, excepciones y fallos silenciosos. |
| 20 | [P21 · Reporting poco fiable y dependiente de Excel](../Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md) | 3 | 3 | 3 | 4 | Se pueden conciliar CRM, hojas, facturación y contabilidad y medir ajustes y horas de cierre. |
| 21 | [P26 · Dificultad para atraer, integrar y retener agentes](../Problemas/26-dificultad-para-atraer-integrar-y-retener-agentes.md) | 3 | 3 | 3 | 4 | Cohortes de altas y bajas permiten medir cobertura, rampa y permanencia a 3, 6 y 12 meses. |
| 22 | [P28 · Estacionalidad y sensibilidad al ciclo financiero](../Problemas/28-estacionalidad-y-sensibilidad-al-ciclo-financiero.md) | 3 | 3 | 3 | 4 | Series internas fechadas permiten separar lead, visita, firma y registro y contrastarlas con crédito. |
| 23 | [P02 · Leads de baja intención y seguimiento deficiente](../Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md) | 3 | 3 | 3 | 3 | El CRM permite cohortes por fuente, pero intención, duplicidad y maduración requieren criterios comunes. |
| 24 | [P04 · Dificultad para obtener exclusivas](../Problemas/04-dificultad-para-obtener-exclusivas.md) | 3 | 3 | 3 | 3 | Contratos y entrevistas permiten comparar modalidades, aunque confianza y presión son difíciles de aislar. |
| 25 | [P07 · Respuesta tardía y seguimiento inicial discontinuo](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md) | 3 | 3 | 3 | 3 | Los tiempos pueden medirse si se integran canales; las conversaciones personales dejan huecos. |
| 26 | [P08 · Comunicación irregular y poca visibilidad](../Problemas/08-comunicacion-irregular-y-poca-visibilidad.md) | 3 | 3 | 3 | 3 | Mensajes, hitos y encuestas permiten medir cadencia, pero atribuir una caída a comunicación exige casos. |
| 27 | [P09 · Visitas poco productivas](../Problemas/09-visitas-poco-productivas.md) | 3 | 3 | 3 | 3 | Agenda y CRM permiten medir asistencia y avance, aunque encaje e intención incluyen juicio comercial. |
| 28 | [P29 · Dependencia de personas clave y traspasos sin continuidad](../Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md) | 3 | 3 | 3 | 3 | Ausencias y handoffs pueden observarse, pero confianza, criterio tácito y pérdida causal son difíciles de medir. |
| 29 | [P22 · Desincronización en multipublicación y portales](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md) | 3 | 2 | 3 | 4 | Una auditoría simultánea de CRM, web, MLS y portales permite medir demora, rechazo y divergencia. |
| 30 | [P23 · UX móvil, complejidad y soporte del CRM](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md) | 3 | 2 | 3 | 4 | Telemetría, tickets y pruebas por dispositivo permiten medir tareas fallidas y tiempo de resolución. |

## Comprobación aritmética y límites

- Ejemplo de máximo observado: P01 = `35 + 25 + 20 + 15 = 95`.
- Ejemplo con frecuencia ocasional: P22 = `26,25 + 12,50 + 15 + 20 = 73,75`.
- Los 30 problemas aparecen una sola vez. La validabilidad es una asignación analítica explícita, no una dimensión ya puntuada en las fichas.
- Las etiquetas cualitativas describen la evidencia disponible; no deben convertirse en porcentajes de prevalencia.
