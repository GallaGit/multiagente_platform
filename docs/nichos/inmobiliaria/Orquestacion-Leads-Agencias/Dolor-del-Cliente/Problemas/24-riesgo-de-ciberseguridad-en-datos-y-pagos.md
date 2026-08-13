# Riesgo de ciberseguridad en datos y pagos

**Corte:** 12 de agosto de 2026  
**Ámbito:** agencias inmobiliarias en España; evidencia estadounidense solo para contrastar fraude inmobiliario equivalente

**Evaluación:**

- **Frecuencia:** Frecuente como riesgo; incidencia específica en agencias españolas no cuantificada
- **Impacto:** Muy alto
- **Impacto económico:** Muy alto potencial por fraude, interrupción y respuesta; sin pérdida media española demostrada
- **Impacto operativo:** Muy alto
- **Frustración:** muy alta cuando se materializa
- **Urgencia:** muy alta
- **Personas afectadas:** clientes, agentes, administración, dirección, proveedores y encargados del tratamiento

## 1. Nombre del problema

Exposición de datos personales, documentos y pagos inmobiliarios a credenciales comprometidas, brechas, ransomware y fraude BEC.

## 2. Descripción

La agencia concentra datos de identidad, contacto, propiedad, contratos y, según el proceso, información financiera. Estos datos se distribuyen entre CRM, email, mensajería, carpetas y proveedores.

El riesgo no se limita a robo de datos. En el fraude BEC, el atacante compromete o suplanta comunicaciones legítimas y modifica instrucciones de transferencia en el momento del cierre. La urgencia y las cuantías de una operación inmobiliaria aumentan el daño potencial.

## 3. Evidencias

### INCIBE

- **Organización/autor:** Instituto Nacional de Ciberseguridad
- **Título:** *INCIBE presenta su balance de ciberseguridad 2024 con más de 97.000 incidentes gestionados*
- **Fecha:** 20 de marzo de 2025; actualizado el 26 de marzo
- **Tipo/calidad:** balance oficial; **alta**
- **URL:** <https://www.incibe.es/incibe/sala-de-prensa/incibe-presenta-su-balance-de-ciberseguridad-2024-con-mas-de-97000-incidentes>
- **Respaldo exacto:** INCIBE gestionó 97.348 incidentes en 2024, de los cuales 31.540 afectaron a empresas, incluidas pymes, micropymes y autónomos. Registró 42.136 casos de malware, 357 ransomware y 7.470 intrusiones o intentos. No ofrece desglose para agencias inmobiliarias.

### Agencia Española de Protección de Datos

- **Organización/autor:** AEPD
- **Título:** *La AEPD recibió en 2025 más de 2.700 notificaciones de brechas de datos personales*
- **Fecha:** 23 de enero de 2026
- **Tipo/calidad:** autoridad regulatoria; **alta**
- **URL:** <https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-recibio-en-2025-mas-2.700-notificaciones-brechas>
- **Respaldo exacto:** recibió 2.765 notificaciones en 2025, el 80% del sector privado. Las brechas de mayor alcance incluyeron ransomware, exfiltración y ataques a grandes plataformas CRM mediante credenciales comprometidas; identifica el segundo factor como medida especialmente eficaz.

### INCIBE

- **Organización/autor:** INCIBE
- **Título:** *BEC: cómo operan los estafadores y cómo detectarlos*
- **Fecha:** actualizado el 8 de enero de 2026
- **Tipo/calidad:** guía oficial; pertenece a la misma organización que el balance
- **URL:** <https://www.incibe.es/empresas/blog/bec-como-operan-los-estafadores-y-como-detectarlos>
- **Respaldo exacto:** incluye expresamente el fraude inmobiliario: infiltración en comunicaciones entre compradores, vendedores, agentes y abogados y sustitución de instrucciones de transferencia. Recomienda verificación por un canal distinto, aprobación múltiple y validación de cambios bancarios.

### FBI Internet Crime Complaint Center

- **Organización/autor:** Federal Bureau of Investigation, IC3
- **Título:** *2024 Internet Crime Report*
- **Fecha:** 2025
- **Tipo/calidad:** informe oficial estadounidense; **alta**
- **URL:** <https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf>
- **Respaldo exacto:** documenta un BEC en una transacción inmobiliaria con una transferencia fraudulenta de 956.342 dólares, de la que se detuvieron 955.060. Es un caso internacional que demuestra el mecanismo y la urgencia; no se usa para estimar pérdidas en España.

### ENISA

- **Organización/autor:** European Union Agency for Cybersecurity
- **Título:** *NIS Investments 2024*
- **Fecha:** noviembre de 2024
- **Tipo/calidad:** encuesta e informe oficial europeo, 1.350 organizaciones; **alta**, no específico de inmobiliarias
- **URL:** <https://enisa.europa.eu/publications/nis-investments-2024>
- **Respaldo exacto:** muestra limitaciones de presupuesto y conocimiento, especialmente en pymes, y la relevancia del riesgo de cadena de suministro. Aporta contexto de capacidad, no incidencia sectorial.

INCIBE aporta dos documentos pero cuenta como una sola organización. Se utilizan cuatro fuentes institucionales independientes.

## 4. Personas afectadas

- Compradores, vendedores, arrendadores e inquilinos.
- Agentes que reciben documentación y coordinan el cierre.
- Administración y dirección.
- Responsables de protección de datos.
- Bancos, abogados, gestorías y proveedores.
- Encargados de CRM, almacenamiento, firma y mensajería.

## 5. Proceso afectado

El riesgo aparece desde la [valoración y documentación](../../analisis_del_mercado/02-funcionamiento.md#valoración-y-documentación) hasta [financiación y cierre](../../analisis_del_mercado/02-funcionamiento.md#financiación-y-cierre).

También atraviesa el [abastecimiento y captación](../../Situacion_en_España/Economía_inmobiliaria.md#abastecimiento-y-captación) y el [cierre y posventa](../../Situacion_en_España/Economía_inmobiliaria.md#cierre-y-posventa), donde se intercambian identidad, contratos e instrucciones de pago.

## 6. Herramientas implicadas

- [CRM inmobiliarios](../../ecosistema_tecnologico/02_sistemas_core/crm-inmobiliarios.md)
- [Email](../../ecosistema_tecnologico/03_canales_y_productividad/email.md)
- [WhatsApp Business](../../ecosistema_tecnologico/03_canales_y_productividad/whatsapp-business.md)
- [Gestores documentales](../../ecosistema_tecnologico/02_sistemas_core/gestores-documentales.md)
- [Firma electrónica](../../ecosistema_tecnologico/02_sistemas_core/firma-electronica.md)
- [Bancos y tesorería](../../ecosistema_tecnologico/02_sistemas_core/bancos.md)
- [Ciberseguridad, identidad y backups](../../ecosistema_tecnologico/00_metodologia/alcance-y-taxonomia.md#datos-automatización-e-ia) — **categoría planificada**

## 7. Consecuencias

- Desvío de pagos mediante BEC.
- Exfiltración de datos personales y documentos.
- Indisponibilidad por ransomware.
- Paralización de operaciones.
- Obligación de evaluar y, cuando proceda, notificar la brecha.
- Comunicación a personas afectadas si existe alto riesgo.
- Investigación, recuperación y daño reputacional.
- Dependencia de proveedores comprometidos.

## 8. Frecuencia

**Frecuente.** El riesgo es recurrente, pero la frecuencia sectorial no está determinada. INCIBE y AEPD acreditan un volumen relevante en el conjunto empresarial y privado, pero no publican una tasa específica para agencias.

No se trasladan los incidentes generales ni el caso estadounidense a una probabilidad por inmobiliaria española.

## 9. Impacto

**Muy alto.** Puede implicar pérdida de fondos, exposición de identidad, interrupción y obligaciones regulatorias. No se calcula una pérdida media porque no existe una muestra española específica.

## 10. Urgencia

**Muy alta.** En BEC, la verificación debe producirse antes de transferir y la respuesta debe comenzar inmediatamente tras detectar el fraude. La gestión de una brecha sujeta a RGPD tiene plazos y criterios formales.

## 11. Soluciones actuales

- Autenticación multifactor.
- Mínimo privilegio y revisión de accesos.
- Gestor de contraseñas y cuentas nominativas.
- Cifrado en tránsito y almacenamiento.
- Backups aislados y pruebas de restauración.
- Doble aprobación de pagos.
- Verificación de IBAN por canal alternativo conocido.
- Registro, monitorización y alertas.
- Formación frente a phishing y BEC.
- Plan de respuesta y herramientas de la AEPD.

## 12. Limitaciones de las soluciones actuales

- MFA no protege procesos de pago mal diseñados.
- Las personas pueden aprobar solicitudes convincentes.
- Backups no impiden exfiltración.
- Proveedores y credenciales externas amplían la superficie.
- Microagencias carecen a menudo de personal especializado.
- La seguridad del fabricante no sustituye las obligaciones del responsable.
- El uso de canales personales dificulta baja de accesos y auditoría.
- La notificación diligente no elimina el daño ya producido.

## 13. Nivel de evidencia

**Alto.** La evidencia es alta para amenaza, mecanismo y controles, y media para incidencia específica en agencias españolas.

La evidencia es institucional y convergente. La principal limitación es sectorial: no existe denominador público de incidentes en CNAE 6831.

## Validación

- **Nivel de confianza:** Alto.
- **Número de fuentes consultadas:** 4 organizaciones independientes; 5 documentos
- **Calidad de las fuentes:** 4 fuentes institucionales de calidad alta
- **Posibles contradicciones:** notificar una brecha a la AEPD no implica negligencia ni sanción. Un CRM cloud puede ofrecer controles superiores a sistemas locales. El caso FBI demuestra riesgo, no frecuencia española.
- **Aspectos pendientes de confirmar:** uso de MFA; pruebas de backup; accesos compartidos; protocolos de IBAN; incidentes por tamaño; tiempos de detección y recuperación; contratos y controles de proveedores.

---

← [Anterior: UX móvil, complejidad y soporte del CRM](23-ux-movil-complejidad-y-soporte-del-crm.md) | [Índice](../README.md) | [Siguiente: brecha de formación profesional y digital →](25-brecha-de-formacion-profesional-y-digital.md)
