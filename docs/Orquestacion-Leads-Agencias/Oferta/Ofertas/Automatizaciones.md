# Automatizaciones personalizadas — Flujos Críticos

## 1. Nombre y estado

**Automatización Controlada de Flujos Críticos**  
**Tipo:** servicio modular a medida con componentes repetibles  
**Estado:** respaldada por caso; cada módulo requiere diagnóstico  
**Confianza:** media

## 2. Problema principal que resuelve

Persisten tareas de copiar leads, reescribir fichas, actualizar estados, buscar documentos, re-teclear facturación y conciliar reportes. La automatización parcial también crea fallos silenciosos cuando no hay monitorización ni propietario.

**Dolores:** D06, D07, D19–D22 y D29. No se ofrece una automatización genérica: solo un traspaso repetido, medible y técnicamente accesible.

## 3. Cliente Ideal

**Principal:** ICP-01 con CRM activo, volumen semanal, owner y datos exportables.  
**Secundario:** ICP-02 para conciliación acotada no bancaria y flujo de incidencias; ICP-03 para reporting o postventa repetibles.

## 4. Objetivo

Eliminar o controlar un traspaso manual concreto sin perder trazabilidad, reversibilidad ni revisión humana.

## 5. Descripción y alcance

### Módulos elegibles, no acumulativos por defecto

1. **Entrada y seguimiento:** canal→CRM→responsable→alerta.
2. **Calidad de inventario:** CRM→control de campos/estado→cola de corrección; la publicación depende de API.
3. **Documentos:** recepción→clasificación determinista→expediente→aviso de falta.
4. **Reporting:** extracciones→modelo común→control de discrepancias→panel.
5. **Handoff:** ausencia/baja→reasignación→checklist de continuidad.

### Incluye

- línea base y diseño de un módulo;
- mapeo, reglas, casos de error y aprobación;
- integración de sistemas acordados;
- logs, alertas, reintentos y parada segura;
- pruebas, documentación y formación;
- medición antes/después.

### No incluye

- automatizar procesos no estables;
- conectores sin acceso autorizado;
- scraping contrario a términos;
- decisiones legales, financieras o de riesgo;
- acciones irreversibles sin control;
- múltiples módulos sin validación incremental;
- disponibilidad indefinida sin mantenimiento contratado.

## 6. Beneficios

- **Tiempo:** elimina re-tecleo o revisión rutinaria definida.
- **Coste:** potencial reducción de horas; se calcula con línea base real.
- **Productividad:** deriva atención a excepciones.
- **Experiencia:** reduce esperas y estados incoherentes.
- **Errores:** validaciones, idempotencia y cola de revisión.
- **Ingresos:** potencial solo en módulos de seguimiento; no garantizado.
- **Implantación:** media si existe API/export; alta si depende de canal cerrado.

## 7. Diferenciación

Make aporta iPaaS; CRM ofrecen automatizaciones nativas; Power BI informa. La oferta añade:

- selección del caso por evidencia y no por herramienta;
- modelo inmobiliario de contacto, inmueble, operación y responsable;
- tratamiento explícito de duplicados, excepciones y fallos;
- control de calidad antes de automatizar;
- documentación, ownership, portabilidad y línea base;
- ruta a mantenimiento.

No pretende superar el catálogo de Make ni capacidades nativas. Las reutiliza cuando son suficientes.

## 8. Complejidad de implementación

**Media**, con rango:

- entrada/alerta con conectores: media;
- reporting multi-fuente: alta;
- multiportal bidireccional: alta;
- documentos sensibles/KYC o pagos: muy alta y fuera del alcance inicial.

## 9. Escalabilidad

- **Servicio personalizado:** medio-alto.
- **Producto repetible:** alto por módulo y combinación de stack.
- **SaaS:** potencial para monitorización y controles.
- **Plataforma:** posible como biblioteca de conectores.
- **Marketplace:** futuro para plantillas verificadas.
- **IA como servicio:** opcional en clasificación no crítica.

## 10. Dependencias

- APIs, webhooks, exportaciones y límites contractuales;
- datos con identificadores y calidad mínima;
- sandbox o conjunto de prueba;
- owner y reglas aprobadas;
- logs, credenciales y gestión de cambios;
- procesos internos y terceros;
- política RGPD y retención.

## 11. Riesgos

- **Técnico — medio/alto:** API, duplicados, concurrencia y fallos silenciosos.
- **Comercial — medio:** fuerte riesgo de proyecto único.
- **Regulatorio — medio:** datos personales; alto si se amplía a KYC/pagos.
- **Operativo — alto:** excepciones y soporte pueden superar el caso feliz.
- **Competitivo — alto:** funciones nativas e iPaaS horizontales.

## 12. Hipótesis pendientes

1. Tres clientes comparten el mismo patrón y stack.
2. El volumen manual justifica integración.
3. Las excepciones son acotables.
4. El cliente acepta cambiar el proceso.
5. El mantenimiento puede separarse del desarrollo.
6. La automatización nativa no resuelve el caso con menor TCO.

## 13. Validación

**Evidencia utilizada**

- M01: costes antes del cobro y margen sensible ([Economía](../../Situacion_en_España/Economía_inmobiliaria.md#5-costes-y-márgenes)).
- M02: tramos del flujo ([Funcionamiento](../../analisis_del_mercado/02-funcionamiento.md)).
- M03: tareas repetitivas y fallos F1–F5 ([Vacíos](../../ecosistema_tecnologico/07_analisis_transversal/vacios-tecnologicos.md#6-tareas-repetitivas-persistentes)).
- M04: D19–D22 ([Resumen](../../Modulo-04-Dolor-del-Cliente/Resumen-Ejecutivo.md)).
- M05: Make es potente, pero exige modelo y mantenimiento ([Competencia](../../Modulo-05-Competencia/Resumen-Ejecutivo.md#plataformas-horizontales)).
- M06: O05, O09, O15 y O16 ([Ranking](../../Modulo-06-Oportunidades-de-Negocio/Analisis/Ranking-General.md)).
- M08: ICP-01 con stack y señales observables ([ICP-01](../../Modulo-08-Cliente-Ideal-ICP/ICP/ICP-01.md)).

**Supuestos:** frecuencia, acceso, reglas estables y owner.  
**Pendiente:** por módulo medir volumen, minutos por caso, tasa de excepción, errores, soporte, reutilización y alternativa nativa.
