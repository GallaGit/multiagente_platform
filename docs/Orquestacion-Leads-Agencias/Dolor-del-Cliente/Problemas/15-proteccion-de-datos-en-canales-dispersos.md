# Protección de datos en canales dispersos

**Corte:** 12 de agosto de 2026  
**Ámbito:** agencias de intermediación residencial en España y su red de proveedores.

| Dimensión | Evaluación |
| --- | --- |
| Frecuencia | Frecuente como exposición; incidentes sectoriales no cuantificados |
| Impacto | Muy alto |
| Impacto económico | Alto potencial por fraude, respuesta a incidentes y sanción |
| Impacto operativo | Alto; inventario, permisos, retención, derechos y brechas |
| Frustración | Alta para clientes, agentes, dirección y proveedores |
| Urgencia | Muy alta durante todo el ciclo |
| Personas afectadas | Leads, clientes, agentes, back-office, dirección y terceros que reciben documentación |

## 1. Nombre del problema

Los datos personales y documentos sensibles circulan y permanecen en CRM, correo, WhatsApp, móviles y carpetas con controles desiguales.

## 2. Descripción

La agencia trata identidad, contacto, solvencia, cuentas bancarias, contratos, escrituras y comunicaciones. Una misma copia puede quedar en el móvil del agente, correo, CRM, carpeta compartida y proveedor de firma. La dispersión dificulta informar correctamente, limitar accesos, responder derechos, aplicar plazos y conocer qué datos fueron expuestos en un incidente.

Debe distinguirse:

- **Obligación normativa:** licitud, transparencia, minimización, seguridad, confidencialidad y responsabilidad demostrable.
- **Caso probado:** la AEPD apercibió en 2025 a una inmobiliaria por información de protección de datos desactualizada.
- **Inferencia operativa:** el uso simultáneo de varios canales incrementa copias y superficies de acceso. No existe una serie pública de brechas específica de agencias inmobiliarias.

## 3. Evidencias

### Fuente 1

- **Organización/autor:** Agencia Española de Protección de Datos.
- **Título:** *PA-00032-2025, expediente EXP202414045*.
- **Fecha:** 2025.
- **Tipo/calidad:** resolución administrativa primaria; **alta**.
- **URL directa:** <https://www.aepd.es/documento/pa-00032-2025.pdf>
- **Respaldo exacto:** apercibe a BH Realty Móstoles por infracción del artículo 13 RGPD y ordena adecuar documentos en papel que todavía citaban la derogada Ley Orgánica 15/1999. Es un caso probado, no una muestra sectorial.

### Fuente 2

- **Organización/autor:** Parlamento Europeo y Consejo.
- **Título:** *Reglamento (UE) 2016/679, Reglamento General de Protección de Datos*.
- **Fecha:** 27 de abril de 2016.
- **Tipo/calidad:** legislación europea primaria; **alta**.
- **URL directa:** <https://boe.es/buscar/doc.php?id=DOUE-L-2016-80807>
- **Respaldo exacto:** establece minimización, transparencia, limitación de conservación y medidas técnicas y organizativas proporcionales al riesgo. Acredita obligaciones, no frecuencia de incidentes.

### Fuente 3

- **Organización/autor:** Instituto Nacional de Ciberseguridad, INCIBE.
- **Título:** *Fraude email comprometido*.
- **Fecha:** sin fecha visible; consultada el 12 de agosto de 2026.
- **Tipo/calidad:** orientación técnica oficial; **media**.
- **URL directa:** <https://www.incibe.es/empresas/te-ayudamos/fraude-email-comprometido>
- **Respaldo exacto:** describe acceso a buzones, reglas de reenvío, modificación de cuentas y permanencia del atacante antes de ejecutar el fraude; exige valorar notificación de brecha cuando se accede a datos personales. Es riesgo empresarial general, no medición inmobiliaria.

### Fuente 4

- **Organización/autor:** Agencia Española de Protección de Datos.
- **Título:** *Resoluciones*.
- **Fecha:** consulta del 12 de agosto de 2026.
- **Tipo/calidad:** repositorio administrativo oficial; **alta**, no independiente de la fuente 1.
- **URL directa:** <https://www.aepd.es/informes-y-resoluciones/resoluciones>
- **Respaldo exacto:** el filtro histórico mostraba 451 entradas clasificadas como actividades inmobiliarias. El contador incluye distintos años y procedimientos y no equivale a 451 sanciones recientes.

## 4. Personas afectadas

- Leads y clientes cuyos datos se recogen antes, durante y después de la operación.
- Agentes que usan correo, teléfono, CRM y mensajería.
- Dirección y responsable del tratamiento.
- Franquiciadores, otras agencias, firma electrónica, broker, banco, gestoría y notaría.
- Personal que debe atender derechos o investigar una brecha.

## 5. Proceso afectado

- [Captación](../../analisis_del_mercado/02-funcionamiento.md#captación): incorporación de propietarios y contactos.
- [Gestión de demanda](../../analisis_del_mercado/02-funcionamiento.md#gestión-de-demanda): contacto, solvencia, visitas, ofertas y seguimiento.
- [Valoración y documentación](../../analisis_del_mercado/02-funcionamiento.md#valoración-y-documentación): documentación de identidad, titularidad y operación.
- [Cierre y posventa](../../Situacion_en_España/Economía_inmobiliaria.md#cierre-y-posventa): escritura, pagos, archivo e incidencias.

## 6. Herramientas implicadas

- [Ciberseguridad, identidad y continuidad](../../ecosistema_tecnologico/06_datos_automatizacion_e_ia/ciberseguridad-identidad.md).
- [CRM inmobiliarios](../../ecosistema_tecnologico/02_sistemas_core/crm-inmobiliarios.md).
- [Gestores documentales](../../ecosistema_tecnologico/02_sistemas_core/gestores-documentales.md).
- [Email](../../ecosistema_tecnologico/03_canales_y_productividad/email.md).
- [WhatsApp Business](../../ecosistema_tecnologico/03_canales_y_productividad/whatsapp-business.md).
- [Firma electrónica](../../ecosistema_tecnologico/02_sistemas_core/firma-electronica.md).
- [Gobierno y calidad de datos](../../ecosistema_tecnologico/06_datos_automatizacion_e_ia/gobierno-calidad-datos.md).

## 7. Consecuencias

- Acceso o comunicación no autorizada de documentación personal.
- Imposibilidad de localizar todas las copias al ejercer derechos o aplicar borrado.
- Fraude mediante suplantación o cambio de una cuenta de pago.
- Notificación de brecha y medidas correctoras cuando procedan.
- Pérdida de confianza del cliente y dificultad para acreditar cumplimiento.
- Accesos que permanecen activos después de que un agente abandone la empresa.

## 8. Frecuencia

**Frecuente.** La exposición es transversal y su prevalencia es desconocida. Toda agencia que trata datos está sometida al RGPD. El caso AEPD prueba un incumplimiento concreto y el repositorio muestra actividad supervisora, pero ninguno permite calcular la proporción de agencias afectadas.

## 9. Impacto

**Muy alto.** El daño potencial es crítico: puede combinar daño a personas, fraude económico, interrupción operativa y actuación regulatoria. No se asigna una pérdida media por incidente porque no existe una estadística sectorial española utilizable.

## 10. Urgencia

**Muy alta.** La urgencia es continua: los datos se copian desde el primer contacto y una credencial comprometida puede afectar conversaciones y documentos antes de ser detectada.

## 11. Soluciones actuales

- Cláusulas informativas y registro de actividades de tratamiento.
- Contratos con encargados y control de proveedores.
- CRM y almacenamiento corporativo con permisos.
- MFA, cuentas individuales, gestores de contraseñas y registro de accesos.
- Políticas de conservación, bloqueo y borrado.
- Formación en phishing y verificación de cambios bancarios por un canal independiente.
- Procedimientos de gestión y notificación de brechas.

## 12. Limitaciones de las soluciones actuales

- Una cláusula correcta no controla copias en dispositivos o canales personales.
- El almacenamiento cloud no garantiza por sí solo permisos, retención ni copias de seguridad adecuadas.
- MFA puede estar disponible pero no forzada en todos los sistemas.
- Los datos obligatorios para PBC requieren plazos y accesos diferentes de los datos comerciales.
- La verificación por correo falla si el propio buzón está comprometido.
- Los proveedores añaden responsables, encargados y transferencias que deben delimitarse.

## 13. Nivel de evidencia

**Medio.** La evidencia es alta sobre obligaciones y existencia de casos, media sobre la fricción operativa y baja sobre prevalencia. Procede de tres organismos independientes y es primaria y técnica, pero el riesgo BEC de INCIBE no está cuantificado específicamente para inmobiliarias.

## Validación

- **Nivel de confianza:** Medio. La confianza es alta en la existencia y gravedad potencial, y baja en la frecuencia sectorial.
- **Número de fuentes consultadas:** 4 documentos; 3 organismos independientes.
- **Calidad de las fuentes:** 3 altas y 1 media.
- **Posibles contradicciones:** la conservación PBC durante el plazo legal es compatible con RGPD si tiene base, finalidad, seguridad y acceso restringido; no autoriza conservación indiscriminada.
- **Aspectos pendientes de confirmar:** brechas por canal, uso de cuentas personales, adopción real de MFA, tiempo de revocación de accesos y volumen de copias por expediente.

---

← [Anterior: cumplimiento PBC/AML difícil de ejecutar](14-cumplimiento-pbc-aml-dificil-de-ejecutar.md) | [Índice](../README.md) | [Siguiente: arras, reservas y firmas mal definidas →](16-arras-reservas-y-firmas-mal-definidas.md)
