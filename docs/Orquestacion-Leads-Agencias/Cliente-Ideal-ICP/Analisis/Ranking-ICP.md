# Ranking de ICP

## Matriz puntuada

Escala 1–5. Pesos: problema 20, presupuesto 15, digitalización 10, implantación 15, decisión 10, mercado 10, competencia 10 y riesgo 10.

| ICP | Problema | Presupuesto | Digital | Implantación | Decisión | Mercado | Competencia | Riesgo | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Independiente profesionalizada | 5 | 3 | 4 | 4 | 4 | 4 | 3 | 3 | **77** |
| Agencia mixta venta/alquiler | 5 | 4 | 4 | 3 | 3 | 2 | 3 | 3 | **71** |
| Comercializadora obra nueva | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | **69** |
| Boutique comercial/industrial | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 2 | **61** |
| Franquiciado multi-oficina | 4 | 3 | 4 | 2 | 2 | 4 | 2 | 2 | **59** |

## Clasificación

| Orden base | ICP | Categoría comercial | Score ajustado | Decisión por evidencia |
|---:|---|---|---:|---|
| 1 | Independiente profesionalizada | Muy recomendable | **49** | Experimento barato |
| 2 | Agencia mixta venta/alquiler | Muy recomendable | **44** | En espera / reformular |
| 3 | Comercializadora obra nueva | Recomendable | **39** | En espera / reformular |
| 4 | Boutique comercial/industrial | Recomendable | **32** | En espera / reformular |
| 5 | Franquiciado multi-oficina | Recomendable | **37** | En espera / reformular |

No hay “cliente excelente”. Tampoco hay candidato a piloto: faltan entrevistas, líneas base, pruebas técnicas, coste de implantación y evidencia de pago.

## Cálculo del ajuste

Leyenda: A = alta 1,00; M = media 0,85; B = baja 0,65; S = supuesto 0,40.

| ICP | Problema | Presupuesto | Digital | Implantación | Decisión | Mercado | Competencia | Riesgo | Confianza ponderada |
|---|---|---|---|---|---|---|---|---|---:|
| Independiente | A | S | B | S | S | M | M | S | 64% |
| Agencia mixta | A | S | B | S | S | B | M | S | 62% |
| Obra nueva | M | S | B | S | S | S | M | S | 56% |
| Boutique | B | S | B | S | S | S | M | S | 52% |
| Franquicia | M | B | B | S | S | B | M | S | 62% |

El score ajustado es el score base por esa confianza, redondeado a entero. “Supuesto” domina presupuesto, implantación, decisión y riesgo porque no hay evidencia de campo.

## Justificación por perfil

### Independiente profesionalizada

Máxima intensidad por P19–P21, base digital e independencia de proveedor. O01 propone contrastar 3–20 agentes, pero no existe un recuento público de ese perfil; las 850 empresas CNAE 683 de 10–49 son solo un ancla parcial e incluyen administración.

### Agencia mixta venta/alquiler

Problema recurrente, P18 y vacío documentado entre CRM de venta y PMS. Los especialistas ya cubren mejor P18; falta delimitar cuántas agencias mixtas tienen cartera y presupuesto.

### Comercializadora de obra nueva

P12 hace el problema visible y medible. Resta incertidumbre sobre pagador, número de cuentas, ciclo por proyecto e integración con promotor.

### Boutique comercial/industrial

Cliente profesional y capacidad potencial, pero mercado, frecuencia y stack no están cuantificados; riesgo de personalización alto.

### Franquiciado multi-oficina

El dolor aumenta con oficinas, agentes y splits, pero stack obligatorio, central y propiedad de datos penalizan implantación, decisión y riesgo.

## Secuencia de validación

1. 10 entrevistas a independientes profesionalizadas.
2. 8 entrevistas a gestores con cartera recurrente.
3. 6 entrevistas a obra nueva separando promotor/comercializadora.
4. 4 entrevistas a franquiciados multi-oficina con contrato disponible.
5. 4 entrevistas a boutiques comercial/industrial.

Las cantidades son diseño de investigación, no tamaño de muestra estadísticamente representativo.

## Criterio para cambiar ranking

Recalcular cuando un perfil tenga:

- al menos cinco cuentas puntuadas;
- evidencia de presupuesto en tres;
- dos pilotos aceptados;
- una compra o compromiso económico;
- coste y tiempo de implantación observados.

## ICP Prioritarios para Validación Comercial

1. **Agencia independiente profesionalizada:** mejor equilibrio entre dolor, autonomía y facilidad.
2. **Agencia mixta con gestión recurrente:** doble stack y problema operacional auditable.
3. **Comercializadora de obra nueva:** dolor segmentario intenso, condicionado a validar pagador y timing.

## Validación

**Confianza:** media-baja.  
**Evidencia:** Módulos 01–05 disponibles y oportunidades H1–H8.  
**Limitación:** scoring analítico no calibrado.  
**Pendiente:** ventas reales, win/loss, CAC, ciclo y renovación.
