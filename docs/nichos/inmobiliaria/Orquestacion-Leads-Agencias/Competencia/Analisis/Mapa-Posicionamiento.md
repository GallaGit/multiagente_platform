# Mapa de posicionamiento

## Método

Puntuación analítica ordinal, no métrica de rendimiento:

- **Complejidad:** 1 = autoservicio/tarea única; 5 = implantación enterprise/múltiples procesos.
- **Precio/TCO:** 1 = entrada gratuita o baja; 5 = presupuesto enterprise, integración y servicios.
- **IA:** 1 = sin IA central; 5 = IA vertical/agéntica como núcleo.
- **Especialización:** 1 = horizontal; 5 = vertical inmobiliario.
- **Valor potencial:** amplitud y criticidad del proceso cubierto, no ROI demostrado.

## 1. Tabla de codificación

| Empresa | Complejidad | TCO | IA | Especialización | Valor potencial |
|---|:---:|:---:|:---:|:---:|:---:|
| Inmovilla | 3 | 2 | 2 | 5 | 4 |
| Witei | 2 | 2 | 2 | 5 | 4 |
| idealista/tools | 2 | 3 | 2 | 5 | 4 |
| Prinex | 5 | 5 | 2 | 5 | 5 |
| Floorfy | 2 | 2 | 3 | 5 | 3 |
| Nodalview | 2 | 3 | 4 | 5 | 3 |
| Signaturit | 2 | 3 | 2 | 2 | 4 |
| DocuSign | 4 | 4 | 4 | 1 | 5 |
| Avantio | 4 | 4 | 3 | 5 | 5 |
| AppFolio | 4 | 4 | 4 | 5 | 5 |
| Trioteca | 3 | 3 | 3 | 5 | 4 |
| M-Files | 4 | 5 | 4 | 2 | 5 |
| Power BI | 4 | 3 | 4 | 1 | 5 |
| Make | 3 | 2 | 4 | 1 | 4 |
| Structurely | 3 | 4 | 5 | 5 | 4 |
| Restb.ai | 4 | 4 | 5 | 5 | 4 |

**Confianza:** media. Las puntuaciones sintetizan producto, contratación y esfuerzo de adopción; el TCO real no es público para la mayoría.

## 2. Complejidad frente a simplicidad

```mermaid
quadrantChart
    title Complejidad de implantación vs amplitud funcional
    x-axis Simple --> Complejo
    y-axis Tarea acotada --> Plataforma amplia
    quadrant-1 Suite enterprise
    quadrant-2 Suite accesible
    quadrant-3 Herramienta puntual
    quadrant-4 Especialista complejo
    Witei: [0.28, 0.65]
    Inmovilla: [0.42, 0.72]
    Idealista Tools: [0.32, 0.58]
    Prinex: [0.92, 0.92]
    Floorfy: [0.25, 0.42]
    Nodalview: [0.30, 0.40]
    Signaturit: [0.30, 0.48]
    DocuSign: [0.72, 0.72]
    Avantio: [0.76, 0.84]
    AppFolio: [0.80, 0.90]
    Trioteca: [0.52, 0.55]
    M-Files: [0.80, 0.76]
    Power BI: [0.72, 0.70]
    Make: [0.52, 0.60]
    Structurely: [0.55, 0.54]
    Restb.ai: [0.70, 0.48]
```

## 3. Precio/TCO frente a valor potencial

```mermaid
quadrantChart
    title TCO relativo vs valor potencial
    x-axis TCO bajo --> TCO alto
    y-axis Valor acotado --> Valor amplio
    quadrant-1 Estratégico enterprise
    quadrant-2 Alto valor accesible
    quadrant-3 Compra táctica
    quadrant-4 Especialista premium
    Witei: [0.28, 0.72]
    Inmovilla: [0.30, 0.74]
    Idealista Tools: [0.52, 0.70]
    Prinex: [0.92, 0.92]
    Floorfy: [0.32, 0.45]
    Nodalview: [0.48, 0.50]
    Signaturit: [0.50, 0.68]
    DocuSign: [0.75, 0.82]
    Avantio: [0.76, 0.86]
    AppFolio: [0.78, 0.90]
    Trioteca: [0.50, 0.65]
    M-Files: [0.88, 0.80]
    Power BI: [0.48, 0.78]
    Make: [0.30, 0.66]
    Structurely: [0.72, 0.68]
    Restb.ai: [0.76, 0.62]
```

El “valor” es potencial funcional. No implica que el cliente obtenga retorno; datos deficientes pueden reducir drásticamente el valor de BI, automatización e IA.

## 4. Nivel de IA frente a especialización

```mermaid
quadrantChart
    title Intensidad de IA vs especialización inmobiliaria
    x-axis Horizontal --> Vertical inmobiliario
    y-axis Sin IA central --> IA como núcleo
    quadrant-1 IA vertical
    quadrant-2 IA horizontal
    quadrant-3 Software horizontal
    quadrant-4 Vertical digital
    Inmovilla: [0.90, 0.32]
    Witei: [0.90, 0.36]
    Idealista Tools: [0.94, 0.35]
    Prinex: [0.92, 0.32]
    Floorfy: [0.90, 0.48]
    Nodalview: [0.92, 0.72]
    Signaturit: [0.30, 0.30]
    DocuSign: [0.12, 0.68]
    Avantio: [0.92, 0.48]
    AppFolio: [0.90, 0.75]
    Trioteca: [0.92, 0.52]
    M-Files: [0.32, 0.68]
    Power BI: [0.10, 0.72]
    Make: [0.08, 0.72]
    Structurely: [0.90, 0.94]
    Restb.ai: [0.96, 0.96]
```

## 5. Implicaciones

1. **Verticales españoles:** alto encaje inicial y menor complejidad, pero IA y gobierno de datos desiguales.
2. **Suites enterprise:** mayor amplitud, coste de implantación y dependencia de configuración.
3. **IA vertical:** gran especialización técnica; el reto competitivo se desplaza a integración, idioma, normativa y volumen.
4. **Plataformas horizontales:** menor conocimiento inmobiliario nativo, pero ecosistemas y capacidad de extensión superiores.
5. **Especialistas de contenido/firma:** adopción sencilla en una tarea; no eliminan la fragmentación si el resultado vuelve manualmente al CRM.

## 6. Pendientes

- TCO comparable a 12 y 36 meses.
- Tiempo de implantación y porcentaje de clientes que usan cada módulo.
- Disponibilidad real de IA por país, idioma y plan.
- Benchmark técnico de APIs, latencia, errores y exportabilidad.
- Valor observado por arquetipo de agencia.
