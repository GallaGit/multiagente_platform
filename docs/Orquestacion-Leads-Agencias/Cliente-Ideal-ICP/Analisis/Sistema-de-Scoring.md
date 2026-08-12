# Sistema de scoring de clientes

## Propósito

La matriz sirve para calificar cuentas concretas y ordenar discovery. No estima probabilidad estadística de compra.

## Criterios y pesos

| Criterio | Peso | 1 punto | 3 puntos | 5 puntos |
|---|---:|---|---|---|
| Intensidad del problema | 20 | Ocasional, sin impacto | Recurrente, impacto cualitativo | Frecuente, medido y con owner |
| Presupuesto | 15 | No existe | Partida posible | Partida aprobada/sponsor |
| Digitalización | 10 | Sin sistema | CRM/PMS con silos | Core estable, API/export |
| Facilidad de implantación | 15 | Migración/integración crítica | Integración moderada | Piloto aislable y datos listos |
| Rapidez de decisión | 10 | Procurement >6 meses | 2–6 meses | Dueño decide en <2 meses |
| Tamaño del mercado | 10 | Nicho no cuantificado | Segmento identificable | Muchas cuentas accesibles |
| Competencia existente | 10 | Solución madura dominante | Cobertura parcial | Vacío claro y baja sustitución |
| Riesgo comercial | 10 | Alto CAC/churn/regulación | Riesgo manejable | Retención/compra previsibles |
| **Total** | **100** |  |  |  |

En competencia y riesgo, 5 siempre significa situación favorable para vender.

## Fórmula

`Score total = Σ (puntuación de 1–5 / 5 × peso)`

Ejemplo: intensidad 4 con peso 20 aporta `4/5 × 20 = 16`.

### Ajuste por confianza

Cada criterio recibe un factor heredado del Módulo 07:

| Evidencia | Factor |
|---|---:|
| Alta | 1,00 |
| Media | 0,85 |
| Baja | 0,65 |
| Supuesto sin contraste de campo | 0,40 |

`Confianza ponderada = Σ (factor × peso) / 100`

`Score ajustado = Score base × confianza ponderada`

La clasificación comercial solicitada usa el score base. El avance de inversión usa el ajustado: 75+ candidato a piloto; 60–74 validar supuestos; 45–59 solo experimento barato; menos de 45 en espera o reformulación. Ningún ICP de este informe supera 60 ajustado.

## Clasificación

| Score | Clase |
|---:|---|
| 85–100 | Cliente excelente |
| 70–84 | Cliente muy recomendable |
| 55–69 | Cliente recomendable |
| 40–54 | Cliente poco recomendable |
| 0–39 | Cliente a evitar |

## Reglas de evidencia

1. No asignar 5 a presupuesto sin partida o aprobación comprobable.
2. No asignar 5 a problema sin métrica, ejemplo reciente y responsable.
3. No confundir “tener CRM” con adopción; comprobar actividad y datos.
4. Si el stack es impuesto por franquicia, implantación no puede superar 3 sin permiso.
5. Si no se conoce firmante/aprobador, rapidez no puede superar 3.
6. Una función competidora no prueba que el problema esté resuelto; pedir uso real.
7. Registrar fuente y fecha de cada puntuación.

## Ficha de cuenta

| Campo | Registro |
|---|---|
| Empresa |  |
| Segmento / ICP |  |
| Empleados / oficinas / usuarios |  |
| Stack |  |
| Problema observado y frecuencia |  |
| Métrica base |  |
| Champion |  |
| Aprobador / firmante |  |
| Presupuesto |  |
| Integraciones y datos |  |
| Competidores / alternativa |  |
| Evento de compra |  |

## Score de cuenta

| Criterio | Peso | Puntos 1–5 | Evidencia | Confianza | Aporte |
|---|---:|---:|---|---|---:|
| Intensidad | 20 |  |  |  |  |
| Presupuesto | 15 |  |  |  |  |
| Digitalización | 10 |  |  |  |  |
| Implantación | 15 |  |  |  |  |
| Decisión | 10 |  |  |  |  |
| Mercado | 10 |  |  |  |  |
| Competencia | 10 |  |  |  |  |
| Riesgo | 10 |  |  |  |  |
| **Total** | **100** |  |  |  |  |

Registrar también confianza ponderada y score ajustado; no usar decimales para aparentar precisión.

## Condiciones eliminatorias

Aunque el score sea alto, no avanzar si:

- no existe base jurídica/permisos para usar los datos;
- no hay acceso al aprobador o al pagador;
- el sistema core no permite exportar/integrar;
- se exige ROI no medible o promesa basada en datos no validados;
- el piloto compromete operación crítica sin reversibilidad;
- no hay usuario responsable de adopción.

## Confianza

**Confianza del marco:** media.  
**Evidencia:** metodología y reglas del Módulo 07, problemas, competencia y madurez del Módulo 03.  
**Limitación:** pesos analíticos, no calibrados con ventas históricas.  
**Pendiente:** recalibrar tras 30 oportunidades y comparar score con reunión, piloto, cierre y renovación.
