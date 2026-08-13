# Ciberseguridad, identidad y continuidad

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** MFA · backups · phishing · accesos de agentes · AEPD

---

## 1. Función principal

Proteger la **identidad de usuarios**, la **disponibilidad** de CRM/email/archivos y la **confidencialidad** de datos de clientes y operaciones frente a phishing, cuentas compartidas, pérdida de dispositivos y ransomware.

En la agencia típica el riesgo no es solo “hackeo sofisticado”, sino **credenciales de agente + WhatsApp/email sin MFA** y documentos en Drive personal. Marco de cumplimiento: RGPD + guías AEPD; sector no tiene censo público de incidentes inmobiliarios. **[Media]**

---

## 2. Usuarios

| Rol | Riesgo / control |
|-----|------------------|
| Agente | Dispositivo móvil, WA, email; vector phishing |
| Admin IT / titular | Altas/bajas, MFA, backups |
| Franquiciador | Políticas y SSO a veces |
| Encargados (CRM SaaS, Google, Microsoft) | Seguridad del cloud + DPA |
| Cliente | Envía DNI por chat — riesgo compartido |

---

## 3. Momento del flujo

Transversal. Picos de riesgo: onboarding de agente, despido/salida, campañas de phishing (falso notario, falso portal, falso banco), envío de KYC, y restauración tras borrado accidental o ransomware.

---

## 4. Información gestionada

- Identidades: usuarios CRM, M365/Workspace, portales profesionales  
- Secretos: contraseñas, API keys iPaaS, tokens WhatsApp BSP  
- Copias: backups CRM (si el fabricante ofrece export), Drive, buzones  
- Logs de acceso (en planes superiores)  
- Datos personales y documentación de compraventa/alquiler  

---

## 5. Integraciones (tipo)

| Control | Tipo habitual |
|---------|---------------|
| MFA en Google / Microsoft | Nativa |
| MFA en CRM vertical | Nativa (no siempre forzada) |
| SSO / SAML | Nativa en enterprise; rara en micro |
| Backup CRM | Export manual / nativa fabricante |
| Backup endpoint | Manual / EDR (grandes) |
| Gestor de contraseñas | Manual adopción |
| iPaaS con OAuth | Automatización — riesgo de over-permission |

---

## 6. Flujo de datos (ASCII)

```text
[Agente] --login--> [Email / CRM / Portales / WA]
              │
              ├─ MFA? ── no ──► cuenta vulnerable
              │
              v
        [Phishing / dispositivo perdido]
              │
              v
        ¿Backup + revocación accesos?
              │
         sí / no ──► continuidad o pérdida de leads/docs
              │
              v
        [Notificación AEPD si hay brecha personal]  (si procede)
```

---

## 7. Limitaciones y tareas humanas

- Cuentas compartidas (“la de la oficina”) sin trazabilidad.  
- Agentes que usan Gmail/WhatsApp personal para clientes.  
- Phishing de falsa transferencia / falsa nota simple.  
- Backups: muchas agencias confían solo en el SaaS sin probar restore.  
- Salida de empleado: no revocar a tiempo accesos a Idealista Tools, CRM, Drive.  
- Envío de DNI por WhatsApp: mala práctica persistente.

---

## 8. Costes (solo públicos)

| Concepto | Dato |
|----------|------|
| MFA Google / Microsoft | Incluido en planes habituales Workspace/M365 |
| Licencias M365 / Workspace con seguridad avanzada | Según SKU — **consultar fabricante** |
| CRM: MFA / logs | Según plan — a menudo sin desglose de precio |
| Backup dedicado / EDR | Bajo presupuesto — **no público** sectorial |
| Gestor de contraseñas (1Password, Bitwarden, etc.) | Planes públicos del fabricante — citar URL al comprar; no inventar aquí |
| Ciberseguro pyme | Prima **no pública** homogénea |
| Sanción / notificación AEPD | Caso a caso — no es “coste de producto” |

---

## 9. Competencia / enfoques comparados

| Enfoque | Encaje | Fricción |
|---------|--------|----------|
| Solo contraseña compartida | Micro (mal default) | Alto riesgo |
| MFA + altas/bajas disciplinadas | Mediana | Cultura |
| SSO + MDM + EDR | Grandes / franquicia | Coste y IT |
| Seguridad “la del CRM cloud” | Confianza excesiva | Responsabilidad compartida |
| Formación phishing | Todas | Hay que repetirla |

---

## 10. Adopción + confianza

| Práctica | Adopción | Confianza |
|----------|----------|-----------|
| MFA en email corporativo | Habitual en medianas M365/Google; irregular en micro | Media |
| MFA forzada en CRM | Emergente / irregular | Baja–media |
| Backups con prueba de restore | Poco utilizada | Baja |
| Política de accesos al salir el agente | Irregular | Media cualitativa |
| Conciencia AEPD / RGPD básica | Habitual formal; uneven en praxis | Media |
| Incidentes tipificados sector inmobiliario | Sin serie pública usable aquí | — |

Referencia normativa/orientación: [AEPD](https://www.aepd.es/) · obligaciones del responsable · **[Alta]**

---

## 11. Madurez + justificación

Uso típico micro: **Tradicional/Digitalizada** (cloud sin higiene de identidades).  
Mediana con MFA email + CRM y bajas ordenadas: **Digitalizada**.  
Gran empresa con IAM/SSO: hacia **Automatizada** (provisioning).  
Madurez asignada intermediación: **Digitalizada débil en identidad**. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Marco RGPD / AEPD | Norma · **[Alta]** |
| % agencias con MFA en CRM | Pendiente |
| Frecuencia phishing inmobiliario ES | Sin estadística sectorial citada aquí |
| SLA de backup/export por CRM ES | Revisar por fabricante en stacks |

---

← [Gobierno de datos](gobierno-calidad-datos.md) | [Índice](../README.md) | [Siguiente: Comparativa proveedores →](../07_analisis_transversal/comparativa-proveedores.md)
