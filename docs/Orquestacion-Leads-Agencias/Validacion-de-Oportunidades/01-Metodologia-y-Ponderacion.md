# Metodología y ponderación

## 1. Unidad de evaluación

La unidad evaluada es una combinación concreta de:

`segmento + problema + resultado esperado + contexto de uso`

“Automatización inmobiliaria” no es evaluable por ser demasiado amplia. Un alcance válido sería: “reducir la reintroducción manual de datos de leads en agencias residenciales de 3 a 20 agentes que usan portal, WhatsApp y CRM”.

Si cambia el segmento o el resultado esperado, debe crearse otra ficha.

## 2. Escala común

Todos los criterios se puntúan de **1 a 5**:

| Valor | Interpretación |
|---:|---|
| 1 | Muy desfavorable |
| 2 | Desfavorable |
| 3 | Intermedio o incierto |
| 4 | Favorable |
| 5 | Muy favorable |

En **competencia**, una puntuación alta significa un espacio más defendible. En **tiempo de implementación**, una puntuación alta significa menos tiempo hasta entregar valor.

No se permite usar 0 para castigar una oportunidad. Los riesgos que impiden continuar se tratan como condiciones eliminatorias.

## 3. Ponderación

La prioridad original se traduce así:

- Alto = 3 unidades.
- Medio = 2 unidades.
- Total = `5 × 3 + 2 × 2 = 19`.

| Criterio | Unidades | Peso exacto |
|---|---:|---:|
| Dolor del cliente | 3 | 3/19 |
| Facilidad técnica | 3 | 3/19 |
| ROI para el cliente | 3 | 3/19 |
| Competencia | 2 | 2/19 |
| Escalabilidad | 3 | 3/19 |
| Ticket medio | 3 | 3/19 |
| Tiempo de implementación | 2 | 2/19 |

## 4. Fórmula

### Puntuación base

`Puntuación base = Σ (puntuación del criterio × unidades del criterio) / 95 × 100`

El máximo es `5 × 19 = 95`. El resultado se expresa sobre 100 y se redondea a dos decimales al final.

### Confianza de la evidencia

Cada criterio recibe además una confianza:

| Confianza | Factor | Condición mínima |
|---|---:|---|
| Alta | 1,00 | Datos observados, contratos, registros, pruebas o varias fuentes independientes |
| Media | 0,85 | Entrevistas convergentes y alguna evidencia operativa |
| Baja | 0,65 | Opiniones, fuentes secundarias o muestra insuficiente |
| Supuesto | 0,40 | Inferencia sin contraste de campo |

`Confianza global = Σ (factor de confianza × unidades del criterio) / 19`

`Puntuación ajustada = Puntuación base × Confianza global`

La puntuación ajustada impide que una hipótesis atractiva pero sin evidencia compita en igualdad con una oportunidad observada.

## 5. Calidad mínima de evidencia

Una puntuación de 4 o 5 necesita:

1. fuente identificable;
2. fecha o periodo;
3. segmento al que aplica;
4. medida o conducta observable;
5. limitaciones registradas.

La declaración de un proveedor prueba que ofrece una función, no que el cliente obtenga el resultado. Una entrevista prueba percepción, no prevalencia sectorial. Una obligación legal prueba exposición o carga, no voluntad de pago.

## 6. Condiciones eliminatorias

Se revisan antes de ordenar la matriz. Si una condición es `Sí`, la oportunidad queda en espera o descartada aunque su puntuación sea alta.

| Condición | Pregunta |
|---|---|
| Ilegalidad o incumplimiento no mitigable | ¿El modelo exige tratar datos, captar clientes o ejecutar actos fuera del marco aplicable? |
| Acceso inviable | ¿Es imposible acceder legal y técnicamente a datos, canal, sistema o decisor esencial? |
| Daño desproporcionado | ¿El fallo puede causar un perjuicio no aceptable sin control humano o reversibilidad? |
| Economía estructural negativa | ¿El coste mínimo de servir supera de forma persistente el ingreso defendible? |
| Dependencia única no controlable | ¿Una plataforma o proveedor puede inutilizar la solución sin alternativa razonable? |
| Ausencia de problema | ¿La evidencia de campo contradice que exista un dolor relevante en el segmento? |

Una condición eliminatoria debe incluir responsable, evidencia, mitigación posible y fecha de revisión.

## 7. Reglas anti-sesgo

- Puntúan al menos dos personas de forma independiente antes de consensuar.
- Cada puntuación incluye una frase de justificación y un enlace a evidencia.
- No se cambia la rúbrica para favorecer una oportunidad concreta.
- La identidad del defensor no forma parte del criterio.
- Primero se puntúa; después se muestra el total.
- Los desacuerdos de dos o más puntos se conservan y requieren nueva evidencia.
- “No sabemos” se puntúa como 3 con confianza `Supuesto`, no como 5 optimista.
- No se suman criterios nuevos durante una comparación; cualquier cambio crea una nueva versión para todas las oportunidades.

## 8. Versionado

Cada evaluación registra:

- versión de la matriz;
- fecha;
- evaluadores;
- evidencia nueva desde la versión anterior;
- puntuación anterior y actual;
- motivo del cambio;
- decisión resultante.

La matriz inicial es `v1.0`. Los pesos solo cambian tras revisar todas las oportunidades con la nueva versión.

