# 05 — Reglas operativas

Valores por defecto del brief; se ajustan con el cliente en el diagnóstico. Toda regla tiene **owner humano**.

## 1. Entrada

- Solo el canal acordado en el alcance.
- Origen obligatorio (`origen` + `origen_ref` si existe).
- Si faltan email **y** teléfono → `DATOS_INSUFICIENTES` (no asignar).

## 2. Deduplicación

| Prioridad de clave | Uso |
|---|---|
| 1. Email normalizado | Match fuerte |
| 2. Teléfono E.164 | Match fuerte |
| 3. `origen` + `origen_ref` | Match de evento |

- Ventana típica: 30 días (configurable).
- Si match: actualizar registro existente; conservar historial; no crear segundo responsable salvo regla explícita.
- Si conflicto (dos contactos distintos con mismo teléfono): `DUPLICADO_CONFLICTO` → cola.

## 3. Reparto (dueño)

Opciones (elegir una por piloto):

| Modo | Cuándo |
|---|---|
| Round-robin entre agentes activos | Equipo homogéneo |
| Por zona / cartera de inmuebles | Si el CRM ya segmenta así |
| Cola única a responsable de 1ª respuesta | Equipos pequeños |

- Fuera de horario laboral: acumular y asignar al abrir; o guardar en cola `nuevo` hasta apertura (definir con cliente).
- No asignar a usuarios inactivos / de vacaciones (lista mantenida por el cliente).

## 4. SLA

| Evento | Default sugerido |
|---|---|
| Primera respuesta / intento registrado | ≤ 15–60 min en horario (fijar uno) |
| Sin dueño tras alta | ≤ 5–15 min |

Incumplimiento → `SLA_ROTO` → reasignación o escalado a responsable de ops.

## 5. Siguiente acción

Tras asignar, obligatorio:

- Tipo (llamar, email, cualificar, agendar visita, otro)
- Fecha/hora objetivo
- Visible en CRM

Sin siguiente acción → tratar como excepción operativa.

## 6. Reasignación y escalado

1. Alerta al dueño actual.
2. Si no hay actividad en X minutos tras SLA: reasignar según modo de reparto.
3. Segunda ruptura en 24 h: escalar a owner del proceso (gerente/ops).

## 7. Cola humana

Vista única (filtro CRM o tablero) con códigos de [03-modelo-datos.md](03-modelo-datos.md).  
Nadie cierra una excepción sin dejar resultado o nueva siguiente acción.

## 8. Lo que no hacen las reglas

- Enviar mensajes al lead sin aprobación humana (MVP).
- Cambiar precios, rechazar por scoring automático.
- Sobreescribir notas humanas sin traza.
