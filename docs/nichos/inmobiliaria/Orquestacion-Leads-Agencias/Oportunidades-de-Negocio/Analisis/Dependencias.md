# Dependencias entre oportunidades

Una dependencia indica que la evidencia o ejecución de una oportunidad mejora si otra capacidad está resuelta. No establece hoja de ruta.

| Oportunidad dependiente | Depende de | Motivo |
|---|---|---|
| O05 Respuesta | O15 Interoperabilidad | Reparto y seguimiento requieren entrada fiable de portal, CRM y canales. |
| O06 Trazabilidad | O15 Interoperabilidad; O18 Seguridad | Integra conversaciones y datos personales con identidad y retención. |
| O07 Visitas | O04 Cualificación; O06 Trazabilidad | Encaje y feedback necesitan contexto anterior y posterior. |
| O08 Anuncios | O15 Interoperabilidad | Reglas de calidad requieren una fuente de inventario fiable. |
| O09 Multiportal | O08 Anuncios; O15 Interoperabilidad | Sin calidad y reconciliación se propagan estados erróneos. |
| O10 Expediente | O15 Interoperabilidad; O18 Seguridad | Versiones, permisos y retorno de documentos cruzan sistemas. |
| O11 KYC/PBC | O10 Expediente; O18 Seguridad | La decisión regulada requiere documentos íntegros y accesos controlados. |
| O12 Cierre financiero | O10 Expediente; O06 Trazabilidad | Hitos y bloqueos dependen de documentos y comunicaciones. |
| O13 Postventa | O06 Trazabilidad; O10 Expediente | Incidencias necesitan historial, responsable y documentación. |
| O14 Alquiler | O10 Expediente; O18 Seguridad; O20 Finanzas | Contratos, pagos e incidencias son recurrentes. |
| O16 Analítica | O15 Interoperabilidad; O09 Multiportal; O20 Finanzas | BI consume orígenes, estados, costes e ingresos coherentes. |
| O17 Móvil | O15 Interoperabilidad | La UX no resuelve un modelo o sincronización defectuosos. |
| O19 Onboarding | O06 Trazabilidad; O15 Interoperabilidad | El traspaso depende de conocimiento registrado y acceso portable. |
| O20 Finanzas | O15 Interoperabilidad; O18 Seguridad | Cierre, factura, banco y splits requieren enlace y control. |
| O21 Canales propios | O09 Multiportal; O16 Analítica | La atribución necesita origen y resultado reconciliados. |

## Dependencias estructurales

1. **O15** es la base de datos e integración más transversal.
2. **O18** actúa como restricción de seguridad, no como complemento opcional, cuando hay identidad o pagos.
3. **O10** habilita cumplimiento y cierre, pero no sustituye criterio jurídico.
4. **O16** depende de datos operativos; un dashboard no crea información ausente.
5. **O19** condiciona adopción de casi todas las oportunidades, aunque no sea requisito técnico.
