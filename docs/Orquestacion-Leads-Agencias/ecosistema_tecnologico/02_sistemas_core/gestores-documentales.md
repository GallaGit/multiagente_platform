# Gestores documentales

**Corte:** agosto de 2026 · **Ámbito:** España · documentación de operaciones inmobiliarias

---

## 1. Función principal / problema que resuelve

Almacenar, versionar y compartir **documentación de encargos, KYC, contratos, notas simples, CEE, escrituras** entre equipo, cliente y terceros (notaría, banco, abogados).

**Capacidad anunciada (Drive/SharePoint/Dropbox):** carpetas, permisos, búsqueda, coedición.  
**Integración disponible:** APIs, SSO, conectores iPaaS; adjuntos en CRM.  
**Uso real:** carpetas por operación + **email como data room de facto**. **[Media-alta]**

---

## 2. Usuarios

Agentes, back-office, dirección; clientes (enlaces compartidos); notarías/bancos (recepción por email); compliance en redes grandes.

---

## 3. Momento del flujo operativo

Desde captación (DNI, notas simples, CEE) hasta post-escritura (copia simple, liquidaciones). Picos en arras, hipoteca y firma notarial.

---

## 4. Información gestionada

| Tipo | Sensibilidad |
|------|--------------|
| Identificación / KYC | Alta |
| Contratos, arras, encargos | Alta |
| Fotos / planos / marketing | Media |
| Extractos, borradores hipoteca | Alta |
| Escrituras / registro | Alta |

---

## 5. Integraciones

| Sistema | Tipo habitual |
|---------|---------------|
| Email | Manual dominante (adjuntos) |
| CRM (carpeta/adjuntos) | Nativa parcial / manual |
| Firma electrónica | Nativa / API / enlace |
| WhatsApp | Manual (fotos/PDFs) |
| Data room dedicado | Nativa (grandes / M&A); raro en pyme |
| Contabilidad | Inexistente / manual |

---

## 6. Flujo de datos (ASCII)

```text
[Cliente / agente]
      |  WhatsApp / email / escaneo
      v
[Carpeta operación: Drive | SharePoint | Dropbox | CRM]
      |
      +----enlace----> [Firma electrónica]
      |
      +----adjunto---> [Notaría / banco / abogado]
      |
      v
[Riesgo: copias en bandejas de email sin inventario]
```

---

## 7. Limitaciones y tareas humanas

- **Dependencia del email:** versiones múltiples, sin índice, fuga RGPD.
- Permisos “cualquiera con el enlace”.
- Naming inconsistente; búsqueda por agente, no por sistema.
- Data rooms profesionales: overkill y **poco usados** en intermediación residencial típica.
- Retención y borrado al fin de operación: a menudo manual.

---

## 8. Costes

| Herramienta | Precio |
|-------------|--------|
| Google Drive (Workspace) | Según plan Workspace — ver ficha canales; no duplicar aquí sin URL de consulta |
| SharePoint / OneDrive (M365) | Según plan M365 |
| Dropbox Business | Planes públicos en fabricante; **consultar web** — no fijar cifra no verificada en esta ficha |
| Adjuntos CRM | Incluidos en licencia CRM |
| Data room (Intralinks, etc.) | **no público** típico (enterprise) |

Si no se cita página en esta consulta: tratar importes concretos como **no fijados aquí**.

---

## 9. Competencia / enfoques

| Enfoque | Pros | Contras |
|---------|------|---------|
| **Drive / Workspace** | Barato, ubicuo, móvil | Gobernanza débil si no hay estructura |
| **SharePoint / M365** | Permisos, compliance, integración Teams | Curva; exceso para micro |
| **Dropbox** | Sync simple, sharing | Solape con Suite ya contratada |
| **Carpetas CRM** | Contexto en la operación | Límites de almacenamiento/búsqueda |
| **Data room** | Auditoría, watermarks | Coste; no encaja en arras residenciales diarias |
| **Solo email** | Cero fricción inicial | Caos documental; riesgo legal |

El enfoque ganador en pyme ES suele ser **Drive/M365 + email**, no un DMS vertical. **[Media]**

---

## 10. Nivel de adopción + confianza

Muy extendida la combinación cloud storage + email. DMS formal / data room: poco utilizada en 6831. **[Media]** (sin encuesta INE específica de “gestor documental inmobiliario”).

---

## 11. Nivel de madurez + justificación

**Digitalizada** (archivos en cloud). Rara vez **automatizada** (metadatos, retención, clasificación IA). Madurez baja en gobierno documental pese a herramientas maduras. **[Media]**

---

## 12. Validación

- Inventariar políticas reales de retención en 3–5 agencias (cualitativo).
- No atribuir % de mercado a Dropbox vs Drive sin fuente.
- Cruzar con ficha firma y KYC.

---

← [MLS](mls.md) | [Índice](../README.md) | [Siguiente: Firma →](firma-electronica.md)
