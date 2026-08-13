# Servicio premium — Expediente Operativo Integrado

## 1. Nombre y estado

**Expediente Operativo Integrado de la Operación**  
**Tipo:** implantación premium por proceso  
**Estado:** hipótesis de oferta sobre oportunidad respaldada  
**Confianza:** baja

## 2. Problema principal que resuelve

La documentación, versiones, firmas, responsables e hitos se reparten entre CRM, email, carpetas y proveedores. Esto provoca expedientes incompletos, solicitudes repetidas y poca visibilidad entre encargo, arras, financiación, notaría y archivo.

**Dolores núcleo:** D13 expedientes descoordinados, D16 arras/reservas/firmas y D15 protección de datos. Puede tocar D14 y D17, pero no automatiza decisiones PBC/FT, financiación ni notaría.

## 3. Cliente Ideal

**Principal condicionado:** [ICP-03 — comercializadora de obra nueva](../../Cliente-Ideal-ICP/ICP/ICP-03.md), cuando hay varias unidades, proceso documentado, sponsor y ventana previa al lanzamiento o entrega.

**Secundario:** ICP-01 con volumen suficiente de operaciones y back-office; ICP-05 solo si el patrón de data room se repite.

## 4. Objetivo

Disponer de un expediente operativo con:

- requisitos por etapa y tipo de operación;
- documento vigente y propietario;
- permisos y trazabilidad;
- alertas de falta, caducidad o versión;
- evidencia de firma y retorno al registro;
- handoff visible entre comercial, administración y terceros.

## 5. Descripción y alcance

### Incluye

1. modelo de expediente para un proceso y tipología;
2. checklist por hitos P03, P07, P08, P10 y/o P12;
3. integración acotada CRM–documental–firma;
4. metadatos, versiones, roles y permisos;
5. alertas y cola de excepciones;
6. vista de estado para roles internos;
7. política operativa de archivo, handoff y cierre;
8. pruebas, formación y métricas de completitud.

### No incluye

- asesoramiento jurídico o fiscal;
- decisión automatizada de KYC/PBC/FT;
- interpretación de contratos por IA como fuente de verdad;
- acceso garantizado a banco, FEIN, notaría o Registro;
- custodia de fondos;
- sustitución de DMS, firma o CRM;
- certificación de cumplimiento.

## 6. Beneficios

- **Tiempo:** menos búsqueda, solicitud repetida y conciliación de versiones.
- **Coste:** potencial reducción de retrabajo y retrasos; pendiente de línea base.
- **Productividad:** prioriza expedientes incompletos y responsables.
- **Experiencia:** peticiones y estado más consistentes para cliente y equipos.
- **Errores:** controles de obligatoriedad, vigencia y versión.
- **Ingresos:** protege potencialmente cierres al reducir omisiones; causalidad no demostrada.
- **Implantación:** media-baja facilidad; requiere configuración, permisos y cambio de hábito.

## 7. Diferenciación

Los CRM almacenan adjuntos, Signaturit/DocuSign firman y M-Files gobierna documentos. La propuesta no replica esas capacidades: las conecta a un modelo de operación inmobiliario y controla que el documento correcto regrese al expediente con responsable e hito.

Ventajas:

- continuidad encargo→firma→archivo;
- checklist por etapa y excepción;
- neutralidad entre firma, DMS y CRM;
- métricas de completitud, versiones y retraso;
- implantación y adopción incluidas.

Limitación: proveedores enterprise y configuraciones privadas pueden cubrir parte del flujo; la ausencia debe verificarse cliente a cliente.

## 8. Complejidad de implementación

**Alta.** Requiere metadatos, identidad, permisos, versiones, plantillas, retención, datos sensibles, varias integraciones y excepciones legales. Es muy alta si se incluyen KYC, pagos o terceros regulados.

## 9. Escalabilidad

- **Servicio personalizado:** alto inicialmente.
- **Producto repetible:** medio-alto por tipología y stack.
- **SaaS:** potencial como motor de checklist/estado.
- **Plataforma:** potencial si conecta expediente, firma y terceros.
- **Marketplace:** posible para plantillas validadas por especialistas.
- **IA como servicio:** solo asistencia con revisión humana.

## 10. Dependencias

- CRM, DMS/carpetas y proveedor de firma;
- taxonomía documental del cliente;
- asesoría legal/compliance del cliente para requisitos;
- datos, roles, permisos y política de retención;
- APIs y evidencia de firma;
- proceso interno estable y owner;
- consentimiento y medidas de seguridad.

## 11. Riesgos

- **Técnico — alto:** versiones, sincronización, identidad y migración.
- **Comercial — medio/alto:** venta compleja y comprador/pagador no confirmados.
- **Regulatorio — alto:** RGPD, PBC/FT, eIDAS y conservación.
- **Operativo — alto:** checklist incorrecto puede generar falsa seguridad.
- **Competitivo — medio/alto:** DMS, CRM y suites pueden ampliar módulos.

## 12. Hipótesis pendientes

1. La completitud temprana reduce retrasos o retrabajo de forma pagable.
2. Existe un modelo suficientemente común por segmento.
3. El cliente autoriza integrar documentos sensibles.
4. El pagador es la comercializadora, promotora o agencia.
5. El coste de soporte regulatorio no destruye margen.
6. El alcance puede excluir decisiones legales sin perder valor.

## 13. Validación

**Evidencia utilizada**

- M01: cadena de valor y documentación requerida ([Economía](../../Situacion_en_España/Economía_inmobiliaria.md#2-cadena-de-valor)).
- M02: KYC, arras, financiación y cierre ([Proceso](../../analisis_del_mercado/02-funcionamiento.md#valoración-y-documentación)).
- M03: firma que no vuelve al CRM y checklist incompleto ([Flujo](../../ecosistema_tecnologico/01_arquitectura_y_flujos/flujo-lead-postventa.md#2-traspasos-de-datos-detalle)).
- M04: D13, D15 y D16 ([Resumen](../../Dolor-del-Cliente/Resumen-Ejecutivo.md#tabla-compacta-de-los-30-problemas)).
- M05: expediente E2E sin cobertura uniforme ([Vacíos](../../Competencia/Analisis/Vacios-Competitivos.md#expediente-de-operación-completo)).
- M06: O10, score 94 y complejidad alta ([O10](../../Oportunidades-de-Negocio/Oportunidades/10-Oportunidad.md)).
- M08: ICP-03 y dependencia de timing/pagador ([ICP-03](../../Cliente-Ideal-ICP/ICP/ICP-03.md)).

**Supuestos:** proceso repetible, asesoría del cliente, APIs y sponsor.  
**Pendiente:** auditar expedientes anonimizados, completitud antes de arras, búsquedas, versiones, retrasos, pagador, ventana y piloto por promoción o equipo.
