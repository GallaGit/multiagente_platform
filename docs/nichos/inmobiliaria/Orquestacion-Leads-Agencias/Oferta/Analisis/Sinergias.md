# Sinergias y dependencias estratégicas

## Principio

Las ofertas aumentan valor cuando comparten línea base, modelo de datos, conectores, reglas y telemetría. No deben apilarse para inflar alcance: cada transición requiere una necesidad demostrada.

## Cadena principal

`Diagnóstico → Sprint de Leads → Automatización → Servicio Gestionado → SaaS → Plataforma`

### Diagnóstico → Sprint

- El diagnóstico reduce incertidumbre técnica y evita automatizar el problema equivocado.
- La línea base se convierte en criterio de éxito.
- El mapa de permisos y exportabilidad previene bloqueos.

### Sprint → Automatizaciones

- El primer conector revela identificadores, excepciones y hábitos.
- Solo se añaden módulos si el cliente demuestra otro traspaso frecuente.
- Las reglas probadas alimentan una biblioteca reutilizable.

### Automatizaciones → Gestionado

- Logs e incidencias permiten ofrecer mantenimiento con alcance real.
- El runbook reduce dependencia de personas.
- La recurrencia financia mantenimiento de conectores, si el cliente la valora.

### Gestionado → SaaS

- La telemetría muestra qué controles son comunes.
- Las tareas repetidas de soporte señalan qué debe configurarse.
- La retención valida que el problema persiste después de implantar.

### SaaS → Plataforma

- Un modelo estable habilita API y partners.
- La base instalada puede atraer especialistas.
- El marketplace solo tiene sentido con suficiente demanda y oferta.

## Ramas complementarias

### Consultoría + cualquier implantación

La consultoría define ownership, sistema de registro, estados y calidad. Reduce el riesgo de que una integración técnicamente correcta fracase por proceso.

**Combinación recomendada:** diagnóstico + taller de gobierno + sprint.

### Expediente + servicio gestionado

El expediente requiere controlar versiones, permisos y requisitos que cambian. El mantenimiento puede gestionar controles técnicos, pero las reglas legales siguen bajo responsabilidad del cliente y sus asesores.

### Reporting + automatizaciones

No debe venderse un dashboard antes de conciliar fuentes. La secuencia correcta es:

`definición KPI → calidad → integración → discrepancias → visualización`

### Copiloto IA + datos gobernados

El copiloto depende de fuentes citables, permisos y estados. No es una entrada independiente. Puede añadirse para resumen/handoff solo después de que el flujo produzca contexto fiable.

### ICP-02 + expediente/gestionado

Una agencia mixta puede combinar:

- integración CRM–PMS;
- gestión de incidencias;
- reporting de cartera;
- mantenimiento.

La oferta debe demostrar valor incremental frente al PMS y separar alquiler habitual de vacacional, temporada y otros usos.

### ICP-03 + expediente/postventa

En obra nueva:

- expediente organiza reserva, documentación e hitos;
- automatización enruta tickets;
- reporting consolida por promoción;
- gestionado sostiene el pico de entrega.

La contratación depende del pagador y de entrar antes de la fase crítica.

## Dependencias entre ofertas

| Oferta | Requiere | Habilita |
|---|---|---|
| Diagnóstico | Acceso, sponsor, proceso | Todas las implantaciones |
| Consultoría | Usuarios y decisiones | Datos, adopción, automatización |
| Sprint de Leads | Diagnóstico, CRM, canal | Mantenimiento y SaaS |
| Automatización | Caso estable y API | Catálogo y gestionado |
| Expediente | Modelo, asesoría y permisos | Controles y copiloto |
| Gestionado | Base instalada y logs | Recurrencia y telemetría |
| Copiloto IA | Datos gobernados y evaluación | IA como servicio |
| SaaS | Repetición y economía | API/plataforma |
| Plataforma | SaaS, partners y base | Marketplace |

## Aumento de valor por cliente

El valor por cuenta puede aumentar de forma legítima mediante:

1. mayor cobertura del mismo flujo, después de medir el primero;
2. mantenimiento de activos ya implantados;
3. extensión a otra oficina con patrón idéntico;
4. controles y reporting sobre los mismos datos;
5. expediente o IA solo si el proceso y riesgo lo justifican.

No se considera sinergia:

- vender más herramientas sin eliminar handoffs;
- duplicar capacidades nativas;
- extender a procesos regulados sin especialista;
- personalizar sin posibilidad de reutilización;
- añadir IA sin línea base.

## Riesgos de combinación

- alcance difuso y proyecto permanente;
- credenciales excesivas;
- dependencia de un proveedor o consultor;
- duplicación de licencias;
- soporte no rentable;
- falsa seguridad por dashboard o IA;
- dificultad para atribuir resultados a cada módulo.

## Reglas de empaquetado

- Un owner y una métrica por módulo.
- Alcance, exclusiones y fallback explícitos.
- Cada módulo debe poder desactivarse.
- Datos y configuraciones exportables.
- Mantenimiento separado de nuevas funcionalidades.
- Revisión de alternativas nativas antes de desarrollar.
- No definir todavía precios ni estrategia comercial.

## Conclusión

La mayor sinergia proviene del aprendizaje acumulado: cada servicio reduce el riesgo del siguiente y crea activos reutilizables. La cadena comienza con evidencia y termina, solo si se demuestra repetición, en producto.
