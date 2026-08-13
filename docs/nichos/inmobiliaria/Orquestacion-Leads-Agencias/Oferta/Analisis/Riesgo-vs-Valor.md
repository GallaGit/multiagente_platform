# Riesgo vs. valor

## Método

Clasificación cualitativa basada en:

- valor: cercanía a tiempo, error, experiencia, cierre o control;
- dificultad: integraciones, datos, terceros, regulación y cambio;
- riesgo empresarial: compra, margen, repetibilidad, dependencia y competencia.

No es un business case ni sustituye pilotos.

## Matriz

| Oferta | Valor esperado cliente | Dificultad | Riesgo empresarial | Posición | Decisión |
|---|---|---|---|---|---|
| Diagnóstico | Medio-alto | Baja–media | Medio | Quick win de aprendizaje | Ofrecer como fase cero |
| Sprint de Leads | Alto | Media | Medio | Mejor equilibrio | Validar primero |
| Expediente | Alto | Alta | Alto | Apuesta selectiva | Pilotar por segmento |
| Gestionado | Alto sostenido | Media | Alto | Recurrencia potencial | Solo tras implantación |
| Consultoría | Medio-alto | Media | Medio | Habilitador | Combinar con diagnóstico |
| Automatización | Alto por caso | Media–alta | Medio-alto | Rentable si repetible | Limitar catálogo |
| Copiloto IA | Medio potencial | Alta | Muy alto | Experimento | Posponer |
| Control SaaS | Alto potencial | Muy alta | Muy alto | Opción de escala | No construir aún |
| Plataforma | Muy alto potencial | Muy alta | Muy alto | Visión de largo plazo | No priorizar |

## Cuadrantes

### Alto valor / menor dificultad

**Sprint de Leads.** El problema aparece al inicio del embudo, se puede medir y O05 tiene complejidad media. Sigue dependiendo de APIs y disciplina.

**Diagnóstico.** Reduce riesgo y crea línea base, aunque su valor independiente y pago están por validar.

### Alto valor / alta dificultad

**Expediente.** Protege completitud y trazabilidad, pero introduce permisos, versiones y regulación.

**Automatizaciones avanzadas.** Multiportal y reporting pueden aportar valor, pero aumentan dependencia técnica.

**Servicio gestionado.** Su valor aumenta con criticidad, igual que el coste y la responsabilidad.

### Valor medio / dificultad media

**Consultoría de gobierno.** Habilita el resto, pero necesita sponsor y ejecución.

### Valor potencial / riesgo muy alto

**Copiloto IA, SaaS y plataforma.** Tienen lógica tecnológica, pero no demanda, economía ni repetición demostradas.

## Riesgos por oferta

| Oferta | Técnico | Comercial | Regulatorio | Operativo | Competitivo |
|---|---|---|---|---|---|
| Diagnóstico | Bajo–medio | Medio–alto | Medio | Medio | Medio |
| Sprint de Leads | Medio | Medio | Medio | Medio–alto | Medio–alto |
| Expediente | Alto | Medio–alto | Alto | Alto | Medio–alto |
| Gestionado | Medio–alto | Alto | Medio–alto | Alto | Alto |
| Consultoría | Bajo | Medio–alto | Medio | Alto | Medio |
| Automatización | Medio–alto | Medio | Medio | Alto | Alto |
| Copiloto IA | Alto | Alto | Alto | Alto | Muy alto |
| Control SaaS | Muy alto | Muy alto | Alto | Muy alto | Alto |
| Plataforma | Muy alto | Muy alto | Muy alto | Muy alto | Muy alto |

## Condiciones eliminatorias

No avanzar con una oferta si:

1. no hay proceso semanal observable;
2. no existe responsable interno;
3. el dato no es exportable o el contrato prohíbe el acceso;
4. el cliente no acepta una línea base;
5. la función ya está disponible y configurarla es claramente mejor;
6. el caso exige decisión legal, financiera o PBC/FT autónoma;
7. el soporte esperado no puede delimitarse;
8. el usuario busca sustitución humana sin supervisión.

## Reducción de riesgo

- Empezar con lectura/exportación antes de escritura.
- Limitar canales, CRM, proceso y tipología.
- Diseñar fallback, logs y parada segura.
- Minimizar datos y heredar permisos.
- Separar reglas legales aportadas por el cliente.
- Medir incidencias y horas de soporte.
- Convertir patrones en catálogo solo tras repetición.
- Construir SaaS únicamente cuando el servicio sea configurable y recurrente.

## Conclusión

La prioridad no debe seguir el valor potencial máximo. Debe seguir la mejor relación entre valor observable y riesgo reversible. Ese criterio coloca primero el Sprint de Leads, con diagnóstico previo, y deja expediente, IA y plataforma en etapas sucesivas.
