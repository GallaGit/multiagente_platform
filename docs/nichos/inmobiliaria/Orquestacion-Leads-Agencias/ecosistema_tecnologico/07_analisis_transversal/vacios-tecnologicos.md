# Vacíos tecnológicos

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Alcance:** describir **necesidades no cubiertas** y huecos de digitalización.  
**Prohibido aquí:** diseñar soluciones, proponer productos, listar features o vendors «ideales».

---

## 1. Cómo se identifica un vacío

| Señal | Ejemplo en el módulo |
|-------|----------------------|
| Proceso sigue manual pese a herramientas | Lead email → copia a CRM |
| Integración inexistente o rara | CRM ↔ facturación robusta |
| Dato aislado en silo | Chat WhatsApp fuera del registro |
| Capacidad anunciada ≠ uso | «IA» en CRM sin flujo lead→cierre |
| Hueco de evidencia | Sin % adopción micro; portales sin tarifa pública |

Confianza: **media** (síntesis cualitativa). Donde hay ancla cuantitativa se cita.

---

## 2. Necesidades no cubiertas (por área)

### 2.1 Captación y demanda

| Vacío | Qué falta en la práctica típica |
|-------|---------------------------------|
| Cierre del embudo portal→resultado | Motivo de pérdida / visita / oferta no sistemático en un registro |
| Respuesta fuera de horario | Cobertura desigual; no cuantificar % aquí (`context.md` excluido) |
| Multi-portal unificado de lead | Inbox fragmentado email/Tools/API |
| Atribución de canal limpia | Duplicados y orígenes incompletos |

### 2.2 Conversación comercial

| Vacío | Qué falta |
|-------|-----------|
| Timeline auditado WhatsApp↔CRM | App Business no es registro inmobiliario |
| Handoff entre agentes | Historial en móvil personal |
| Opt-in / plantillas a escala micro | API existe; adopción emergente |

### 2.3 Inventario y publicación

| Vacío | Qué falta |
|-------|-----------|
| Consistencia precio/estado multi-portal | Desync frecuente |
| Calidad de ficha (CEE, fotos, atributos) | Campos vacíos; sin gobierno |
| Colaboración MLS sin fricción/riesgo | Historial competencia CNMC; adopción irregular |

### 2.4 Documentación, firma y compliance

| Vacío | Qué falta |
|-------|-----------|
| Circuito KYC-AML embebido E2E en CRM vertical típico | Evidencia: rareza en mapa de integraciones |
| Archivo único de operación (encargo→arras→postventa) | Carpetas Drive personales / email |
| Escritura en el flujo digital de la agencia | Límite legal (Ley 11/2023) — vacío **normativo**, no solo tech **[Alta]** |
| Nivel eIDAS alineado al riesgo del documento | Uso uneven SES vs AES/QES |

### 2.5 Dinero y liquidación

| Vacío | Qué falta |
|-------|-----------|
| Puente CRM→factura→cobro sin re-tecleo | Manual dominante |
| Splits multiagente / multioficina | Excel sombra frecuente **[Media-baja]** |
| Distinción arras en custodia vs honorarios | Error contable típico en Excel |

### 2.6 Datos, BI e IA

| Vacío | Qué falta |
|-------|-----------|
| BI unificado portal + CRM + ads + WhatsApp | Sin ingeniería; INE BI **16,1%** ≥10 |
| Gobierno de calidad de datos CRM | Duplicados, estados inconsistentes |
| IA conectada al sistema de registro | INE IA **9,35%** ≥10 vs uso informal de chats; CBRE 71% solo grandes |
| Métricas de ciclo (tiempo a primer contacto, conversión) | Reporting CRM limitado / Excel |

### 2.7 Identidad y continuidad

| Vacío | Qué falta |
|-------|-----------|
| MFA y bajas de acceso sistemáticas | Sin % sectorial |
| Backup/export usable al cambiar de CRM | SLA por fabricante uneven |
| Separación dispositivo personal / corporativo en agentes | WA y fotos de DNI en móvil |

---

## 3. Procesos aún no digitalizados (o solo «a medias»)

| Proceso | Estado típico micro/mediana |
|---------|----------------------------|
| Cualificación estructurada del lead | Informal en chat/llamada |
| Agenda de visitas con confirmación registrada | Calendario + WA; poco en ficha |
| Checklist documental pre-notaría | Human-driven; plantillas Word |
| Postventa / referidos | Disperso |
| Valoración con comparables sistemáticos | Experiencia agente ± tools; AVM nicho |
| Onboarding/offboarding de agente (accesos, números, leads) | Ad hoc |

Madurez dominante: **digitalizada fragmentada**, no automatizada E2E. · [adopcion-madurez-arquetipos.md](adopcion-madurez-arquetipos.md)

---

## 4. Integraciones inexistentes o raras

Del [mapa-integraciones.md](../01_arquitectura_y_flujos/mapa-integraciones.md):

- Conversación WhatsApp completa como timeline auditado en CRM (salvo setups avanzados)  
- KYC-AML extremo a extremo en CRM vertical típico  
- Liquidación multioficina/multiagente nativa robusta  
- BI unificado sin ingeniería  
- Escritura notarial digital genérica en flujo de agencia  

---

## 5. Datos aislados (silos)

```text
Portal (estadísticas anuncio)     ≠  CRM (pipeline)
WhatsApp (conversación)           ≠  CRM (actividades)
Drive personal (PDFs, DNI)        ≠  Gestor documental
Excel comisiones                  ≠  Facturación / contabilidad
Ads / web analytics               ≠  Origen de lead en CRM
```

Resultado: decisiones por intuición o export puntual; alineado con baja adopción BI (INE **16,1%** ≥10). **[Alta sobre el dato INE; media sobre silos]**

---

## 6. Tareas repetitivas persistentes

1. Copiar leads de email a CRM  
2. Reescribir/adaptar fichas por portal  
3. Resumir chats WA para el compañero o el jefe  
4. Buscar el PDF «final» en carpetas  
5. Re-teclear datos a facturación  
6. Actualizar precio en N sitios cuando baja  
7. Pegar textos en ChatGPT para anuncios (IA informal, sin traza)

Estas tareas existen **aunque** haya ~**700 PropTech** (PwC): abundancia de herramientas ≠ cobertura del proceso agencia. **[Media]**

---

## 7. Vacíos de evidencia (investigación)

No son vacíos de software, pero limitan el diagnóstico:

- Adopción CRM/IA en empresas **&lt;10** empleados  
- Tarifas y gasto real en portales  
- % leads gestionados solo en WhatsApp  
- Penetración firma en encargos/arras por provincia  
- Calidad media de datos CRM  

---

## 8. Validación

| Ítem | Estado |
|------|--------|
| Lista de vacíos = síntesis del módulo | **[Media]** |
| Propuestas de producto | **Ninguna** (correcto) |
| Cifras inventadas | **Ninguna** |

---

← [Dependencias](dependencias-sustituibilidad.md) | [Índice](../README.md) | [Siguiente: Hipótesis de oportunidades →](hipotesis-de-oportunidades.md)
