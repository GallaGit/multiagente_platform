# Ficha y matriz

Copiar estas plantillas en un archivo independiente por oportunidad. No completar campos con estimaciones presentadas como hechos.

## 1. Ficha de alcance

```markdown
# Oportunidad OXX — [Nombre descriptivo]

**Estado:** Borrador  
**Versión de matriz:** v1.0  
**Responsable:**  
**Fecha de evaluación:**  
**Próxima revisión:**  

## Hipótesis

Para [segmento y rol] que sufre [problema observable] durante [proceso],
existe una oportunidad de lograr [resultado medible] porque [mecanismo],
frente a [alternativa actual].

## Alcance

- Segmento:
- Comprador económico:
- Usuario:
- Beneficiario:
- Geografía:
- Proceso:
- Resultado:
- Alternativa actual:
- Exclusiones:

## Métrica principal

- Indicador:
- Línea base:
- Objetivo:
- Ventana temporal:
- Fuente:

## Supuestos críticos

| ID | Supuesto | Cómo se falsará | Fecha límite | Estado |
|---|---|---|---|---|
| S1 |  |  |  | Pendiente |

## Condiciones eliminatorias

| Condición | Sí/No | Evidencia | Mitigación | Responsable |
|---|---|---|---|---|
| Ilegalidad o incumplimiento no mitigable |  |  |  |  |
| Acceso inviable |  |  |  |  |
| Daño desproporcionado |  |  |  |  |
| Economía estructural negativa |  |  |  |  |
| Dependencia única no controlable |  |  |  |  |
| Ausencia de problema |  |  |  |  |
```

## 2. Registro de evidencia

| ID | Hallazgo | Tipo | Fuente/enlace | Fecha | Segmento | Confianza | Limitación |
|---|---|---|---|---|---|---|---|
| E01 |  | Entrevista/registro/prueba/contrato/fuente |  |  |  | A/M/B/S |  |

Códigos: `A = alta`, `M = media`, `B = baja`, `S = supuesto`.

No usar una misma fuente independiente como si fueran varias evidencias. Registrar relaciones entre fabricante, distribuidor, medio y estudio patrocinado.

## 3. Matriz individual

| Criterio | Unidades | Puntos 1–5 | Confianza | Factor | Puntos × unidades | Evidencia | Justificación |
|---|---:|---:|---|---:|---:|---|---|
| Dolor del cliente | 3 |  |  |  |  |  |  |
| Facilidad técnica | 3 |  |  |  |  |  |  |
| ROI para el cliente | 3 |  |  |  |  |  |  |
| Competencia | 2 |  |  |  |  |  |  |
| Escalabilidad | 3 |  |  |  |  |  |  |
| Ticket medio | 3 |  |  |  |  |  |  |
| Tiempo de implementación | 2 |  |  |  |  |  |  |
| **Total** | **19** |  |  |  |  |  |  |

### Cálculos

- Suma ponderada: `____ / 95`
- Puntuación base: `suma ponderada / 95 × 100 = ____`
- Confianza global: `Σ(factor × unidades) / 19 = ____`
- Puntuación ajustada: `base × confianza global = ____`

## 4. Comparador de cartera

| ID | Oportunidad | Dolor | Técnica | ROI | Comp. | Escala | Ticket | Tiempo | Base | Conf. | Ajustada | Gate | Estado |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| O01 |  |  |  |  |  |  |  |  |  |  |  |  |  |

Los siete criterios se muestran en escala 1–5. `Gate` indica `Libre`, `En revisión` o `Bloqueada`.

## 5. Acta de decisión

```markdown
## Decisión

- Resultado: Priorizar / Validar / Mantener / En espera / Descartar
- Fecha:
- Participantes:
- Puntuación base:
- Puntuación ajustada:
- Condición eliminatoria:
- Evidencia determinante:
- Incertidumbre principal:
- Motivo:
- Próximo paso:
- Presupuesto o tiempo autorizado:
- Criterio de éxito:
- Criterio de parada:
- Fecha de revisión:
```

## 6. Ejemplo aritmético

Ejemplo ficticio, no evidencia de una oportunidad real:

| Criterio | Unidades | Puntos | Producto |
|---|---:|---:|---:|
| Dolor | 3 | 4 | 12 |
| Técnica | 3 | 3 | 9 |
| ROI | 3 | 4 | 12 |
| Competencia | 2 | 3 | 6 |
| Escalabilidad | 3 | 4 | 12 |
| Ticket | 3 | 3 | 9 |
| Tiempo | 2 | 4 | 8 |
| **Total** | **19** |  | **68** |

`Base = 68 / 95 × 100 = 71,58`

Si la confianza global fuera `0,78`:

`Ajustada = 71,58 × 0,78 = 55,83`

La diferencia indica que la prioridad aparente depende todavía de supuestos y requiere validación antes de inversión relevante.

