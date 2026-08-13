# Property Management (PMS)

**Corte:** agosto de 2026 · **Ámbito:** España · administración de alquileres / fincas vs intermediación

---

## 1. Función principal / problema que resuelve

Software de **gestión de carteras de alquiler y/o comunidades**: contratos, rentas, fianzas, derramas, incidencias, proveedores, liquidaciones a propietarios.

**No es** el CRM de compraventa (pipeline de leads y visitas de venta). Algunos CRM verticales incluyen **módulo de alquiler**, pero un PMS maduro cubre ciclo de vida del contrato y cobros recurrentes.

| | CRM compraventa | PMS alquiler/admin |
|--|-----------------|---------------------|
| Objeto | Operación puntual | Contrato y cartera |
| Dinero | Honorario / comisión | Rentas, derramas, honorarios de gestión |
| Tiempo | Semanas–meses | Meses–años |

**Capacidad anunciada:** rent roll, portal inquilino, incidencias, SEPA.  
**Integración disponible:** bancos, contabilidad, a veces CRM.  
**Uso real:** fuerte en administradores de fincas y gestores de alquiler; débil en agencias 6831 puras. **[Media]**

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Administrador de fincas / gestor de alquiler | Cartera diaria |
| Propietario (portal) | Extractos, incidencias |
| Inquilino (portal) | Pagos, tickets |
| Contabilidad / asesoría | Liquidaciones |
| Agencia mixta (venta+alquiler) | Módulo o herramienta aparte |

---

## 3. Momento del flujo operativo

Tras captación de alquiler (o mandato de gestión): contrato → fianza → cobros mensuales → incidencias/mantenimiento → renovaciones → salida / liquidación. Puede coexistir con CRM en la captación inicial.

---

## 4. Información gestionada

- Unidades, contratos, cláusulas, IPC/actualizaciones
- Calendario de rentas, impagos, reclamaciones
- Fianzas y depósitos
- Incidencias, órdenes de trabajo, proveedores
- Liquidaciones a propietarios / comunidades
- Documentación contractual y comunicaciones

---

## 5. Integraciones

| Destino | Tipo habitual |
|---------|---------------|
| Banca / remesas SEPA | Nativa / API / fichero |
| Contabilidad | Export / nativa |
| CRM de captación | Manual o módulo interno |
| Firma electrónica | Nativa / API / manual |
| Portales de alquiler | Nativa parcial / manual |
| WhatsApp / email | Manual dominante en incidencias |

---

## 6. Flujo de datos (ASCII)

```text
[Captación alquiler / CRM] --> [Contrato + fianza]
                                    |
                                    v
                              [PMS / admin]
                               /    |    \
                         rentas  incidencias  liquidaciones
                             |      |            |
                             v      v            v
                          [Banco] [Proveedor] [Propietario]
```

---

## 7. Limitaciones y tareas humanas

- Agencias de venta “con algo de alquiler” usan Excel o módulo CRM insuficiente.
- Incidencias reales viven en WhatsApp/teléfono.
- Cumplimiento LAU, actualizaciones de renta y depósitos: reglas humanas + plantillas.
- Doble stack venta/alquiler sin vista unificada del cliente.

---

## 8. Costes

Precios de Sigo, Community, soluciones “Alquiler Seguro” tech y PMS verticales: en general **no público** de forma homogénea (demo/presupuesto) o sujetos a packs de servicio (gestión + software).

Módulos alquiler de CRM verticales: incluidos o add-on — **verificar por fabricante**; si no figura en web: **no público**.

---

## 9. Competencia / enfoques

| Enfoque | Ejemplos tipo | Lógica |
|---------|---------------|--------|
| **PMS administrador de fincas** | Sigo, Community (y pares sectoriales) | Comunidades + derramas + contabilidad de fincas |
| **Gestión de alquileres / PropTech** | Plataformas ligadas a operadores (p. ej. ecosistema Alquiler Seguro) | Operativa de rentas + servicios |
| **Módulo alquiler en CRM** | Inmovilla/Witei/etc. (si activado) | Suficiente para pocos contratos; limitado en escala |
| **ERP/contabilidad + Excel** | Holded + hojas | Microgestores |

Enfoque PMS especializado escala en **cartera recurrente**; CRM-módulo prioriza no cambiar de herramienta en agencias mixtas pequeñas.

---

## 10. Nivel de adopción + confianza

Adopción **habitualmente mayor en CNAE 6832** (gestión/administración) que en **6831** (intermediación). Evidencia: lógica operativa + observación sectorial; **no hay % INE específico PMS**. **[Media-baja cuantitativa; media cualitativa]**

En 6831: poco utilizada salvo línea de alquiler relevante.

---

## 11. Nivel de madurez + justificación

**Digitalizada** en administradores establecidos; **tradicional/Excel** en micro. Portales de inquilino e incidencias móvil: hacia automatizada en proveedores líderes (capacidad anunciada > uso uniforme). **[Media]**

---

## 12. Validación

- Confirmar features públicas de Sigo/Community sin inventar cuotas de mercado.
- Mapear qué CRM ES publican módulo alquiler con API.
- No mezclar métricas de “PropTech alquiler” con adopción en agencias de venta.

---

← [ERP](erp.md) | [Índice](../README.md) | [Siguiente: MLS →](mls.md)
