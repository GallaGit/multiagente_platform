# O18 — Seguridad de identidad, documentos y pagos

**Categoría:** Seguridad  
**Clasificación:** Respaldada  
**Nivel de evidencia:** Alto  
**Nivel de confianza:** Alto

## 1. Descripción

Reducir credenciales comprometidas, exposición documental, ransomware, BEC, accesos huérfanos y fraude de transferencia. Aparece en **P03, P07, P08, P09, P10, P11, P15** y deriva de **D15, D24, D29**. Delimita una oportunidad, no un producto.

## 2. Problemas relacionados

- **D15, D24, D29.** [Índice del Módulo 4](../../Modulo-04-Dolor-del-Cliente/README.md#índice-de-problemas).
- Frecuencia, impacto y urgencia son cualitativos; no tasas nacionales.

## 3. Procesos afectados

- **P03, P07, P08, P09, P10, P11, P15.** [Taxonomía](../Metodologia.md#taxonomía-de-trazabilidad).
- [Funcionamiento](../../analisis_del_mercado/02-funcionamiento.md) · [Flujo lead–postventa](../../ecosistema_tecnologico/01_arquitectura_y_flujos/flujo-lead-postventa.md).

## 4. Herramientas implicadas

- **H01, H03, H08, H10, H15, H16.** [Catálogo normalizado](../Metodologia.md#taxonomía-de-trazabilidad).

## 5. Competencia existente

- **Competidores:** C01, C05, C08.
- **Cobertura y límites:** Suites cloud, firma, M-Files y CRM ofrecen controles parciales. MFA no corrige pagos mal diseñados; backups no impiden exfiltración; canales personales dificultan bajas.
- **Sin resolver:** cobertura extremo a extremo, adopción efectiva y resultado por segmento.
- [Módulo 5](../../Modulo-05-Competencia/README.md) · [Comparativa M3](../../ecosistema_tecnologico/07_analisis_transversal/comparativa-proveedores.md).

## 6. Personas beneficiadas

Dirección, administración, agentes, clientes y responsables de datos.

## 7. Beneficio esperado

Menor pérdida y error crítico; continuidad, cumplimiento y confianza. No se asigna ROI sin medición de campo.

## 8. Complejidad estimada

**Alta.** Debe abarcar personas, dispositivos, proveedores, respuesta y pagos.

## 9. Nivel de innovación

**Incremental.** Amplía o hace más fiable un proceso ya atendido por herramientas existentes; no cambia la lógica de intermediación.

## 10. Evidencia y validación

- **Evidencias:** D15, D24, D29; P03, P07, P08, P09, P10, P11, P15; H01, H03, H08, H10, H15, H16; C01, C05, C08; [vacíos tecnológicos](../../ecosistema_tecnologico/07_analisis_transversal/vacios-tecnologicos.md).
- **Calidad:** fichas trianguladas del M4 y documentación del M3; detalle competitivo del M5 incompleto.
- **Limitaciones:** No existe incidencia CNAE 6831 ni pérdida media por agencia.
- **Pendiente:** Auditar MFA, backups, accesos e IBAN; realizar ejercicios BEC.

## 11. Riesgos

| Riesgo | Evaluación |
|---|---|
| Tecnológico | Alta: integración, datos y terceros según alcance. |
| Comercial | Medio: disposición a pagar no demostrada. |
| Regulatorio | Medio; alto si trata identidad, contratos, pagos o datos sensibles. |
| Adopción | Medio-alto: depende de registro consistente y hábitos. |
| Competitivo | Medio-alto: proveedores existentes tienen distribución y datos. |

## 12. Criterio de clasificación

**Respaldada.** Problema, proceso y vacío funcional triangulados; demanda y economía siguen pendientes.

---

[Índice](../README.md) · [Cobertura](../Analisis/Mapa-de-Cobertura.md) · [Riesgos](../Analisis/Riesgos.md)
