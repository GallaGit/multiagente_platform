# Agente IA especializado — Copiloto de Operaciones

## 1. Nombre y estado

**Copiloto IA de Seguimiento y Expediente**  
**Tipo:** IA asistiva con revisión humana  
**Estado:** hipótesis  
**Confianza:** baja

## 2. Problema principal que resuelve

Los agentes y back-office deben reconstruir contexto entre conversaciones, CRM, tareas y documentos. En handoffs o ausencias se pierde continuidad y se repite trabajo.

**Dolores:** D08 comunicación irregular, D13 expediente descoordinado, D20 automatización parcial y D29 dependencia de personas. La existencia del dolor está respaldada; que un agente IA sea la mejor solución no lo está.

## 3. Cliente Ideal

**Primario futuro:** ICP-01 que ya haya normalizado CRM, canal corporativo, permisos y seguimiento mediante ofertas previas.  
**Secundario condicionado:** ICP-03 para resumir tickets/postventa dentro de un proceso aprobado.

No encaja con datos dispersos sin gobierno, canales personales, ausencia de owner o expectativa de autonomía total.

## 4. Objetivo

Ayudar al usuario a:

- resumir contexto autorizado;
- proponer siguiente acción según reglas;
- identificar campos o documentos faltantes;
- preparar borradores;
- facilitar handoff;
- citar siempre la fuente interna y solicitar aprobación antes de escribir o enviar.

## 5. Descripción y alcance

### Incluye en un piloto

1. un único caso de uso y rol;
2. recuperación desde fuentes aprobadas;
3. permisos heredados y minimización;
4. respuesta con citas/enlaces al registro;
5. salida estructurada y nivel de incertidumbre;
6. aprobación humana para acciones;
7. logging, evaluación y botón de rechazo;
8. conjunto de pruebas con casos normales y adversos.

### No incluye

- decisión autónoma de precio, solvencia, KYC/PBC, contrato o pago;
- envío automático a cliente en el MVP;
- acceso indiscriminado a WhatsApp, correo o carpetas;
- asesoramiento jurídico;
- entrenamiento con datos del cliente sin acuerdo;
- promesa de exactitud total;
- sustitución del CRM o back-office.

## 6. Beneficios

- **Tiempo:** potencial reducción de lectura, resumen y preparación.
- **Coste:** por demostrar frente a búsqueda y plantillas.
- **Productividad:** facilita siguiente acción y handoff.
- **Experiencia:** borradores más consistentes, siempre revisados.
- **Errores:** puede detectar faltantes; también puede inventar, por lo que exige cita y aprobación.
- **Ingresos:** no atribuible con evidencia actual.
- **Implantación:** baja solo sobre datos ya gobernados; alta sobre stack fragmentado.

## 7. Diferenciación

CRM ya incorporan IA, Structurely automatiza conversación y herramientas horizontales resumen texto. Esta propuesta solo sería diferente si:

- recupera contexto operativo español desde varias fuentes autorizadas;
- cita el registro en cada afirmación;
- conoce estados, checklist y excepciones del flujo;
- respeta permisos y handoff humano;
- mide aceptación, corrección y tiempo ahorrado;
- no se vende como chat genérico.

La IA horizontal se abarata; sin datos, workflow y distribución propios no hay defensa competitiva.

## 8. Complejidad de implementación

**Alta.** Integración, permisos, recuperación, evaluación, alucinaciones, datos personales y cambio de proceso. Pasa a muy alta si actúa externamente o interviene en decisiones reguladas.

## 9. Escalabilidad

- **Servicio personalizado:** alto en piloto.
- **Producto repetible:** medio si hay modelo de datos común.
- **SaaS:** alto potencial técnico, no comercialmente validado.
- **Plataforma:** posible como capa asistiva.
- **Marketplace:** no prioritario.
- **IA como servicio:** forma objetivo, condicionada a evaluación y coste.

## 10. Dependencias

- datos limpios y fuente de verdad;
- integraciones y permisos por usuario;
- taxonomía de proceso y reglas;
- base documental controlada;
- proveedor/modelo y residencia/tratamiento adecuados;
- evaluaciones, logs y supervisión;
- política de retención, uso y no entrenamiento;
- fallback manual.

## 11. Riesgos

- **Técnico — alto:** alucinación, contexto incompleto y deriva.
- **Comercial — alto:** funciones similares pueden venir incluidas en el CRM.
- **Regulatorio — alto:** RGPD, perfilado, transparencia y posible AI Act según uso.
- **Operativo — alto:** confianza excesiva, revisión superficial y prompts cambiantes.
- **Competitivo — muy alto:** modelos y copilotos horizontales evolucionan rápido.

## 12. Hipótesis pendientes

1. El resumen/handoff es frecuente y costoso.
2. El usuario confía en una respuesta citada, pero mantiene revisión.
3. Hay datos suficientes y permisos coherentes.
4. La precisión supera plantillas/búsqueda con coste aceptable.
5. La tasa de aceptación y el tiempo ahorrado justifican el producto.
6. El caso queda fuera de decisiones de alto riesgo.

## 13. Validación

**Evidencia utilizada**

- M01: adopción de IA polarizada; no hay media representativa ([Mercado](../../Situacion_en_España/README.md#cifras-clave-atajo)).
- M02: múltiples etapas y actores ([Proceso](../../analisis_del_mercado/02-funcionamiento.md)).
- M03: IA desconectada del registro y datos aislados ([Vacíos](../../ecosistema_tecnologico/07_analisis_transversal/vacios-tecnologicos.md#26-datos-bi-e-ia)).
- M04: D08, D13, D20 y D29 ([Resumen](../../Dolor-del-Cliente/Resumen-Ejecutivo.md)).
- M05: frontera competitiva = datos, permisos y handoff ([Competencia](../../Competencia/Resumen-Ejecutivo.md#6-nivel-de-innovación)).
- M06: O19 es hipótesis; O10/O15 están respaldadas ([O19](../../Oportunidades-de-Negocio/Oportunidades/19-Oportunidad.md)).
- M08: ICP-01 exige cambio de proceso, no “añadir IA” ([ICP-01](../../Cliente-Ideal-ICP/ICP/ICP-01.md)).

**Supuestos:** base de datos gobernada, caso frecuente y usuario revisor.  
**Pendiente:** evaluación ciega sobre casos anonimizados: exactitud factual, citas correctas, omisiones, aceptación, tiempo, coste por tarea, incidentes y preferencia frente a alternativa sin IA.
