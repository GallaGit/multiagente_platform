# Matriz impacto–frecuencia

**Fecha de corte:** 12 de agosto de 2026  
**Universo:** 30 problemas; cada ID aparece una sola vez.  
**Advertencia de alcance:** la frecuencia es cualitativa según las fichas y no equivale a prevalencia estadística; el impacto es potencial y no estima TAM ni voluntad de pago.

## Cuadrícula 4×4

Columnas: frecuencia. Filas: impacto. Se aplica el mapeo de [`../Metodologia.md`](../Metodologia.md): 4 = Muy alto/Muy frecuente, 3 = Alto/Frecuente, 2 = Medio/Ocasional y 1 = Bajo/Poco frecuente.

| Impacto ↓ / Frecuencia → | 1 · Poco frecuente | 2 · Ocasional | 3 · Frecuente | 4 · Muy frecuente |
|---|---|---|---|---|
| **4 · Muy alto** | — | — | [P03](../Problemas/03-valoraciones-poco-defendibles-y-precio-de-salida.md), [P10](../Problemas/10-brecha-de-valoracion-y-negociacion.md), [P14](../Problemas/14-cumplimiento-pbc-aml-dificil-de-ejecutar.md), [P15](../Problemas/15-proteccion-de-datos-en-canales-dispersos.md), [P18](../Problemas/18-administracion-de-alquileres-y-normativa-cambiante.md), [P24](../Problemas/24-riesgo-de-ciberseguridad-en-datos-y-pagos.md), [P30](../Problemas/30-retirada-de-agencias-del-mercado-de-alquiler.md) | [P01](../Problemas/01-escasez-de-producto-y-competencia-por-captacion.md), [P27](../Problemas/27-rentabilidad-volatil-e-ingresos-contingentes.md) |
| **3 · Alto** | — | [P22](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md), [P23](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md) | [P02](../Problemas/02-leads-de-baja-intencion-y-seguimiento-deficiente.md), [P04](../Problemas/04-dificultad-para-obtener-exclusivas.md), [P07](../Problemas/07-respuesta-tardia-y-seguimiento-inicial.md), [P08](../Problemas/08-comunicacion-irregular-y-poca-visibilidad.md), [P09](../Problemas/09-visitas-poco-productivas.md), [P11](../Problemas/11-opacidad-de-honorarios-y-exclusivas.md), [P13](../Problemas/13-expedientes-incompletos-y-documentacion-descoordinada.md), [P16](../Problemas/16-arras-reservas-y-firmas-mal-definidas.md), [P17](../Problemas/17-descoordinacion-entre-hipoteca-fein-y-notaria.md), [P19](../Problemas/19-fragmentacion-del-stack-y-duplicidad-de-datos.md), [P20](../Problemas/20-automatizacion-parcial-del-flujo-comercial.md), [P21](../Problemas/21-reporting-poco-fiable-y-dependiente-de-excel.md), [P26](../Problemas/26-dificultad-para-atraer-integrar-y-retener-agentes.md), [P28](../Problemas/28-estacionalidad-y-sensibilidad-al-ciclo-financiero.md), [P29](../Problemas/29-dependencia-de-personas-clave-y-traspasos-sin-continuidad.md) | [P05](../Problemas/05-dependencia-de-los-grandes-portales.md), [P06](../Problemas/06-anuncios-incompletos-inconsistentes-o-desactualizados.md), [P12](../Problemas/12-postventa-saturada-en-obra-nueva.md), [P25](../Problemas/25-brecha-de-formacion-profesional-y-digital.md) |
| **2 · Medio** | — | — | — | — |
| **1 · Bajo** | — | — | — | — |

## Control de cobertura

- Impacto muy alto: 9 problemas; impacto alto: 21; impacto medio o bajo: 0.
- Muy frecuentes: 6; frecuentes: 22; ocasionales: 2; poco frecuentes: 0.
- Total de celdas: `9 + 21 = 30` por impacto y `6 + 22 + 2 = 30` por frecuencia.
- Las expresiones calificadas de las fichas —por ejemplo, “frecuente como riesgo”, “muy frecuente dentro de obra nueva” o “ocasional por ficha”— conservan su nivel base, sin ampliar el ámbito.

## Lectura de cuadrantes

### Alto impacto y alta frecuencia

El cuadrante superior derecho reúne 28 problemas si “alta frecuencia” incluye Muy frecuente y Frecuente; los otros dos tienen frecuencia Ocasional. La concentración refleja el criterio de inclusión del inventario: se seleccionaron dolores recurrentes y materialmente relevantes, no una muestra aleatoria de toda fricción posible.

Dentro de él, [P01](../Problemas/01-escasez-de-producto-y-competencia-por-captacion.md) y [P27](../Problemas/27-rentabilidad-volatil-e-ingresos-contingentes.md) combinan los dos máximos. Otros siete problemas tienen impacto Muy alto y frecuencia Frecuente, con especial presencia de cumplimiento, datos/pagos y alquiler.

### Alto impacto y frecuencia ocasional

[P22](../Problemas/22-desincronizacion-en-multipublicacion-y-portales.md) y [P23](../Problemas/23-ux-movil-complejidad-y-soporte-del-crm.md) pueden ser intensos cuando ocurren, pero dependen de ficha, producto, dispositivo, configuración o proveedor. No hay base para elevarlos a Frecuentes.

### Cuadrantes inferiores vacíos

No hay problemas de impacto Medio/Bajo ni Poco frecuente. Esto no demuestra que no existan en el sector: están fuera del inventario validado por diseño metodológico.

## Límites de interpretación

- La cuadrícula no incorpora urgencia ni facilidad de validación; para la priorización de cuatro dimensiones debe usarse [`Ranking.md`](Ranking.md).
- Una obligación recurrente no prueba incumplimiento recurrente, y un riesgo continuo no prueba incidentes frecuentes.
- Los alcances segmentados se mantienen: [P12](../Problemas/12-postventa-saturada-en-obra-nueva.md) se limita a obra nueva y [P30](../Problemas/30-retirada-de-agencias-del-mercado-de-alquiler.md) afecta de forma desigual según especialización.
