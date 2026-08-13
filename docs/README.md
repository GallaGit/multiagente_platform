# Documentación del negocio

## Qué es

Empresa B2B de **continuidad operativa**: diagnosticar, orquestar y entregar procesos medibles. El **nicho activo** define a quién se vende; la **plataforma interna** es cómo opera la empresa.

Hoy el nicho activo es [inmobiliaria](nichos/inmobiliaria/) (agencias en España, Sprint de Orquestación de Leads).

## Dos capas

| Capa | Qué es | Dónde |
|---|---|---|
| **Producto (externo)** | Lo que se vende en el nicho activo | [`nichos/inmobiliaria/`](nichos/inmobiliaria/) |
| **Plataforma (interna)** | SO de la empresa: comercial → ops → delivery → QA → soporte | [`plataforma-interna/`](plataforma-interna/) |

## Qué no es

- Un SaaS horizontal genérico como primer lanzamiento
- Un bot autónomo de ventas como oferta inicial al cliente
- Vender “sistema multiagente genérico”; los agentes son capacidad interna

## Mapa de esta carpeta

| Ruta | Rol |
|---|---|
| [`CONTEXT.md`](CONTEXT.md) | Identidad y principios (válidos si cambia el nicho) |
| [`nichos/`](nichos/) | Packs de nicho: mercado, oferta, MVP, contexto ejecutable |
| [`plataforma-interna/`](plataforma-interna/) | Arquitectura de agentes y delivery |

Norte del nicho activo: [nichos/inmobiliaria/README.md](nichos/inmobiliaria/README.md).
