> **Estado:** evolución de la **plataforma interna** (SO de la empresa).  
> Norte: [docs/README.md](../README.md) · [roadmap de producto](../roadmap/producto.md) · [plataforma](README.md) · [arquitectura-flujo.md](arquitectura-flujo.md)  
> Producto vendible: [Sprint de Orquestación de Leads](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md).

La plataforma crece por **capacidades de empresa**. Orchestrator / Frontend / Backend son el **módulo de delivery**, no el sistema completo.

Orden de capas:

```text
Comercial → Ops del sprint → Delivery (Orch + FE + BE) → QA → Entrega/soporte
```

# Fase 1. Módulo delivery (base técnica)

No empieces con diez agentes de empresa.

Primera pieza técnica reutilizable: **Orchestrator** documenta el encargo de delivery y delega. No implementa UI ni API. No dirige comercial ni ops.

```
Encargo de delivery
    │
    ▼
Orchestrator (brief + elige)
    │
 ┌──┴─────────────┐
 │                │
Frontend          Backend
(paneles/demos)   (API/conectores)
```

En esta fase los agentes pueden ser prompts. Sin LangGraph / AutoGen / CrewAI.

Detalle de contratos: [fase_1/](fase_1/README.md).

---

# Fase 2. Separar el conocimiento

En lugar de poner todo dentro del prompt, cada agente tendrá su propia carpeta.

```
agents/

    orchestrator/     # delivery
        system.md
        rules.md

    frontend/         # delivery
        system.md

    backend/          # delivery
        system.md
        coding_rules.md

    sales/            # empresa
        system.md
        sales_process.md

    ops/              # empresa — sprint leads
        system.md
```

Así el dominio (hoy: inmobiliario / orquestación de leads) vive en `knowledge/`, no solo en el prompt.

Si mañana cambia el nicho, se cambia el conocimiento; los roles de empresa y el módulo delivery se mantienen.

---

# Fase 3. Herramientas

Ahora sí los agentes pueden usar herramientas.

Delivery (Frontend / Backend)

* GitHub, terminal, Docker (cuando aplique)

Ops / Sprint

* CRM inmobiliario, webhooks, Make/n8n

Sales

* Gmail, CRM comercial, Notion

Cada agente sólo tiene acceso a las herramientas que necesita.

---

# Fase 4. Memoria

Aquí empieza a parecerse a un empleado.

Cada agente recuerda cosas distintas.

Backend / Frontend (delivery)

* arquitectura del sprint, bugs, conectores

Ops

* reglas de lead, excepciones, baselines por cliente

Sales

* clientes, reuniones, propuestas

No necesitan compartir toda la memoria.

---

# Fase 5. Orquestación de empresa

El orquestador de **empresa** (distinto del Orchestrator de delivery) reparte trabajo entre etapas.

Ejemplo:

> Prepara el sprint de orquestación de leads para la agencia X (CRM Witei + leads de portal).

```
Sales / discovery
        ↓
Ops (reglas, SLA, métricas)
        ↓
Delivery (Orchestrator → FE|BE)
        ↓
QA (casos y baseline)
        ↓
Entrega / soporte
```

---

# Fase 6. Automatización

Cuando el flujo manual sea estable, conectar automatizaciones del nicho.

```
Lead entra por portal / formulario
        ↓
Ops / reglas (dueño, SLA)
        ↓
CRM actualizado
        ↓
Excepción → alerta humana
        ↓
Delivery solo si hace falta nuevo conector o panel
```

---

# Tecnologías que usaría

No usaría nada demasiado complejo al principio.

| Necesidad        | Recomendación             |
| ---------------- | ------------------------- |
| Lenguaje         | Python                    |
| API              | FastAPI                   |
| LLM              | OpenAI o Groq             |
| Agentes          | Solo prompts al principio |
| Base de datos    | SQLite                    |
| Memoria          | TinyDB o SQLite           |
| Frontend         | Ninguno al inicio         |
| Automatizaciones | n8n (más adelante)        |

No usaría CrewAI, AutoGen o LangGraph desde el primer día.

---

# ¿Y cuándo usar LangGraph?

Cuando empieces a tener flujos como:

```
Si ocurre A

↓

pregunta al Developer

↓

si responde X

↓

pregunta al Finance

↓

si responde Y

↓

volver al Marketing

↓

esperar aprobación

↓

continuar
```

Ahí sí LangGraph aporta valor porque permite modelar flujos complejos con estados y ramificaciones.

---

# La arquitectura del repositorio

Todo vive en la **raíz del proyecto** (no hay carpeta envoltorio `business-ai/`):

```
├── agents/
│   ├── orchestrator/     # delivery
│   ├── frontend/         # delivery
│   ├── backend/          # delivery
│   ├── sales/            # empresa (futuro)
│   ├── ops/              # empresa (futuro)
│   ├── research/         # empresa (futuro)
│   ├── qa/               # empresa (futuro)
│   └── support/          # empresa (futuro)
│
├── knowledge/
│   └── inmobiliario_leads/   # nicho actual (desde Orquestacion-Leads-Agencias)
│
├── memory/
├── tools/
├── workflows/
├── api/
├── tests/
└── docs/
```

**`knowledge`** separado de **`agents`**: el nicho actual es orquestación de leads para agencias; no `software_business` genérico ni vacaciones.

## Enfoque de negocio

1. **Producto externo** — Sprint de Leads (+ diagnóstico) hasta trabajo repetible.
2. **Plataforma** — roles de empresa alrededor del módulo delivery ([arquitectura-flujo.md](arquitectura-flujo.md)).
3. **Módulo delivery** ([fase_1/](fase_1/README.md)) — Orchestrator + FE + BE cuando haya encargos técnicos reales del servicio.

Base del módulo delivery: [fase_1/](fase_1/README.md).
