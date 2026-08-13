# Plataforma interna — sistema operativo de la empresa

> **Norte:** [docs/README.md](../README.md) · [roadmap de producto](../roadmap/producto.md)  
> **Flujo detallado:** [arquitectura-flujo.md](arquitectura-flujo.md)

## Propósito

Operar la empresa B2B de continuidad operativa para agencias inmobiliarias: comercial, operaciones del sprint, delivery técnico, QA, entrega y soporte — con agentes cuando aporte margen.

No sustituye lo que se **vende** al cliente ([Sprint de Orquestación de Leads](../Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md)). La investigación de mercado vive en [`Orquestacion-Leads-Agencias/`](../Orquestacion-Leads-Agencias/).

## Decisión de alineación

**Orchestrator, Frontend y Backend siguen existiendo**, pero no son el techo del sistema. Son la **capa de delivery técnico** dentro del flujo de la empresa.

| Capa | Agentes / roles | Función |
|---|---|---|
| Empresa | **Research** (cuentas ICP), comercial, ops, QA, soporte | Pipeline interno |
| Delivery | **Orchestrator → Frontend \| Backend** | Brief + construcción de UI/API/conectores del servicio |

El dominio de conocimiento es el nicho inmobiliario (leads, CRM, canales, métricas del sprint), no “software genérico”.

## Flujo de empresa (resumen)

```text
Research (cuentas ICP) → Comercial / discovery
        ↓
Operaciones del sprint (reglas, CRM, canales, métricas)
        ↓
Delivery técnico  ←  Orchestrator + Frontend + Backend
        ↓
QA / pruebas
        ↓
Entrega / soporte al cliente
```

## Prioridad

1. Producto externo (diagnóstico + sprint) hasta trabajo repetible.
2. Luego ampliar roles de empresa alrededor del módulo delivery.
3. No vender esta plataforma como “multiagente genérico”.

## Contenido

| Ruta | Descripción |
|---|---|
| [arquitectura-flujo.md](arquitectura-flujo.md) | Empresa vs delivery; ubicación del trío |
| [agentes/research.md](agentes/research.md) | Agente interno: buscar y puntuar ICP (sin outreach) |
| [roadmap-fase_1.md](roadmap-fase_1.md) | Evolución de capacidades (knowledge, tools, memoria…) |
| [fase_1/](fase_1/) | Módulo delivery: contratos técnicos Orchestrator / FE / BE |
