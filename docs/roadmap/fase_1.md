Tu idea es buena, pero te recomendaría empezar con un objetivo más pequeño. El error más común es intentar construir un "sistema de agentes" cuando todavía no existe un problema real que resolver. La mayoría de los proyectos fracasan porque empiezan por la arquitectura en lugar del flujo de trabajo.

Dado que ya sé que tu objetivo a largo plazo es crear una empresa de desarrollo de software apoyada por IA, esta sería la ruta que seguiría.

# Fase 1. Crear un solo agente (MVP)

No empieces con diez agentes.

Empieza con uno llamado:

**CEO Orchestrator**

Este agente no hace trabajo técnico. Solo decide quién debe hacer cada tarea.

Ejemplo:

```
Usuario
    │
    ▼
CEO Orchestrator
    │
 ┌──┴─────────────┐
 │                │
Developer Agent
Sales Agent
Marketing Agent
Finance Agent
```

En esta fase los agentes pueden ser simplemente prompts.

No hace falta LangGraph, AutoGen ni CrewAI.

---

# Fase 2. Separar el conocimiento

En lugar de poner todo dentro del prompt, cada agente tendrá su propia carpeta.

```
agents/

    orchestrator/

        system.md

        rules.md

    developer/

        system.md

        coding_rules.md

        architecture.md

    sales/

        system.md

        sales_process.md

    marketing/

        system.md

```

Así cambiar de negocio es sencillo.

Si mañana pasas de software a turismo solo cambias los documentos del agente.

---

# Fase 3. Herramientas

Ahora sí los agentes pueden usar herramientas.

Por ejemplo

Developer

* GitHub
* VS Code
* Docker
* Terminal

Sales

* Gmail
* CRM
* Notion

Finance

* Excel
* Banco
* Facturas

Marketing

* LinkedIn
* X
* Facebook

Cada agente sólo tiene acceso a las herramientas que necesita.

---

# Fase 4. Memoria

Aquí empieza a parecerse a un empleado.

Cada agente recuerda cosas distintas.

Developer

* arquitectura
* bugs
* roadmap

Sales

* clientes
* reuniones

Marketing

* publicaciones
* campañas

Finance

* ingresos
* gastos

No necesitan compartir toda la memoria.

---

# Fase 5. Orquestación

Aquí el orquestador empieza a trabajar.

Le dices

> Consigue un cliente para una web de una clínica.

El orquestador divide el trabajo.

```
Marketing

↓

Encontrar clínicas

↓

Sales

↓

Preparar propuesta

↓

Developer

↓

Estimar horas

↓

Finance

↓

Calcular precio

↓

CEO

↓

Entregar respuesta
```

---

# Fase 6. Automatización

Cuando todo funcione manualmente empiezas a conectar automatizaciones.

Por ejemplo

```
Cliente llena formulario

↓

Orquestador

↓

Sales

↓

Developer

↓

Crear Issue en GitHub

↓

Calendar

↓

Notion

↓

Enviar correo
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
│   ├── orchestrator/
│   ├── developer/
│   ├── finance/
│   ├── sales/
│   ├── marketing/
│   ├── legal/
│   └── support/
│
├── knowledge/
│   ├── software_business/
│   ├── marketing/
│   ├── accounting/
│   └── vacations/
│
├── memory/
├── tools/
├── workflows/
├── api/
├── tests/
└── docs/
```

Observa que **`knowledge`** está separado de **`agents`**. Eso es lo que te permitirá cambiar de nicho. Si un día quieres que el sistema te ayude a planificar unas vacaciones, no necesitas reescribir los agentes: mantienes el mismo orquestador y los mismos roles, pero cambias el conocimiento y, si hace falta, añades un agente especializado en viajes.

## Mi recomendación

Conociendo tu forma de aprender y tus objetivos, construiría este proyecto como un **proyecto académico y de largo plazo**, no como un producto terminado desde el primer día. Cada etapa te enseñará una tecnología útil para tu carrera (FastAPI, IA, bases de datos, APIs, automatización y arquitectura de software), y al final tendrás un sistema que podrás adaptar a distintos negocios.

Empezaría con un objetivo muy concreto: **un orquestador y solo tres agentes**:

1. **Orchestrator**: recibe la petición y decide quién debe actuar.
2. **Developer**: analiza requisitos, arquitectura y código.
3. **Business**: se ocupa de clientes, propuestas y organización.

Cuando ese sistema funcione de forma estable, añadiría el resto de agentes (finanzas, marketing, legal, soporte, etc.). Así cada nueva incorporación se hace sobre una base sólida en lugar de aumentar la complejidad desde el principio.

Guía de implementación del MVP: [docs/fase_1/](../fase_1/README.md).
