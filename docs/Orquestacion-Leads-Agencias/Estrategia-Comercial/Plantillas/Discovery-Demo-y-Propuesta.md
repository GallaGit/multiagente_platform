# Plantillas — Discovery, demo y propuesta

## Ficha de discovery

### Cuenta

| Campo | Registro |
|---|---|
| Empresa / ICP |  |
| Fecha / participantes |  |
| Rol usuario / champion / aprobador |  |
| Señal que inició contacto |  |
| Fuente y condición de contacto |  |

### Último caso

| Pregunta | Evidencia |
|---|---|
| ¿Qué ocurrió? |  |
| ¿Cuándo? |  |
| ¿Qué lo inició? |  |
| ¿Qué sistemas intervinieron? |  |
| ¿Quién hizo qué? |  |
| ¿Dónde hubo espera, copia o error? |  |
| ¿Qué consecuencia tuvo? |  |
| ¿Qué registro lo prueba? |  |

### Patrón

| Variable | Registro |
|---|---|
| Frecuencia |  |
| Volumen/denominador |  |
| Tiempo/coste/riesgo |  |
| Variación por canal/equipo |  |
| Solución actual |  |
| Herramientas ya pagadas |  |
| Prioridad y evento |  |

### Compra

| Campo | Registro |
|---|---|
| Champion |  |
| Aprobador |  |
| Firmante |  |
| Presupuesto/fuente |  |
| Proceso y plazo |  |
| Alternativa/competidor |  |
| Bloqueador |  |

### Próximo paso

- Supuesto más incierto:
- Evidencia necesaria:
- Dueño:
- Fecha:
- Criterio de parada:

## Mapa del flujo actual

```text
[Evento]
   ↓  dato / sistema / owner / tiempo
[Paso 1]
   ↓  traspaso / excepción
[Paso 2]
   ↓
[Resultado]
```

Para cada paso:

| Paso | Entrada | Sistema | Owner | Salida | Tiempo | Error/excepción |
|---|---|---|---|---|---:|---|
|  |  |  |  |  |  |  |

## Diseño de baseline

| Elemento | Definición |
|---|---|
| Pregunta |  |
| Evento inicial/final |  |
| Población |  |
| Muestra |  |
| Periodo |  |
| Numerador |  |
| Denominador |  |
| Fuente |  |
| Exclusiones |  |
| Datos faltantes |  |
| Owner que acepta |  |

### Resultado

| Métrica | Pesimista | Base observado | Objetivo acordado |
|---|---:|---:|---:|
| Principal |  |  |  |
| Guardrail 1 |  |  |  |
| Guardrail 2 |  |  |  |

## Guion de demo

### Antes

- problema y caso confirmados;
- usuarios invitados;
- datos sintéticos/anonimizados;
- integración y pasos manuales declarados;
- escenario de error preparado;
- próxima decisión acordada.

### Durante

1. Repetir criterio de éxito.
2. Mostrar el flujo actual.
3. Ejecutar el caso principal.
4. Ejecutar una excepción.
5. Mostrar permisos, registro y reversión.
6. Pedir al usuario que explique cómo lo usaría.
7. Recoger brecha, no elogio.

### Después

| Pregunta | Respuesta |
|---|---|
| ¿Qué impediría uso real? |  |
| ¿Qué parte ya cubre el stack? |  |
| ¿Qué dato/integración falta? |  |
| ¿Qué cambió frente al baseline? |  |
| ¿Quién debe evaluar ahora? |  |

## One-page de prueba

### Situación

[Hechos y baseline]

### Hipótesis

Si [intervención], entonces [métrica] cambiará de [baseline] a [umbral], porque [mecanismo].

### Alcance

- flujo:
- equipo:
- sistemas:
- datos:
- periodo:

### Guardrails

- calidad:
- seguridad:
- carga:

### Decisión

- avanzar si:
- corregir si:
- parar si:
- aprobador:
- fecha:

## Propuesta de piloto

### 1. Contexto acordado

- Proceso:
- Evidencia:
- Baseline:
- Consecuencia:
- Prioridad:

### 2. Resultado

- Métrica principal:
- Umbral:
- Guardrails:
- Método:

### 3. Alcance

**Incluye**

- [flujo];
- [integración];
- [usuarios];
- [soporte];
- [informe].

**No incluye**

- migración completa;
- desarrollos no listados;
- garantías sobre ventas;
- cumplimiento legal ajeno al alcance.

### 4. Plan

| Fase | Salida | Cliente | Proveedor | Fecha |
|---|---|---|---|---|
| Preparación |  |  |  |  |
| Configuración |  |  |  |  |
| Operación |  |  |  |  |
| Medición |  |  |  |  |
| Decisión |  |  |  |  |

### 5. Comercial

| Campo | Condición |
|---|---|
| Precio fijo |  |
| Forma de pago |  |
| Impuestos |  |
| Vigencia |  |
| Inicio |  |
| Terminación |  |

### 6. Riesgo y datos

- DPA/roles:
- subencargados:
- acceso:
- retención:
- borrado/exportación:
- reversión:
- incidentes:

### 7. Aceptación

- aprobador:
- firmante:
- criterio de aceptación:
- fecha de firma:

## Revisión final del piloto

| Dimensión | Baseline | Resultado | Confianza | Decisión |
|---|---:|---:|---|---|
| Métrica principal |  |  |  |  |
| Guardrail 1 |  |  |  |  |
| Guardrail 2 |  |  |  |  |
| Uso/adopción |  |  |  |  |
| Coste de entrega |  |  |  |  |

Documentar cambios externos, excepciones y trabajo manual antes de atribuir el resultado.
