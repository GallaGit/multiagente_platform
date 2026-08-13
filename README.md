# Multiagent Business

MVP de una plataforma multiagente para investigar, vender y desarrollar soluciones de continuidad operativa. El nicho activo (hoy inmobiliaria) vive en [`docs/nichos/inmobiliaria/`](docs/nichos/inmobiliaria/).

El sistema expone una API con FastAPI que utiliza un agente orquestador para dirigir cada solicitud al agente especializado adecuado:

- **Research:** investigación de cuentas ICP del nicho activo con evidencia pública.
- **Business:** discovery, propuestas, precios y estrategia comercial.
- **Developer:** arquitectura, APIs, código e integraciones.

> El producto externo del nicho activo está en [`docs/nichos/inmobiliaria/mvp/`](docs/nichos/inmobiliaria/mvp/). El código actual implementa el MVP de la plataforma multiagente interna.

## Arquitectura

```text
Cliente HTTP o CLI
        |
        v
   FastAPI API
        |
        v
  Orchestrator
   /    |     \
  v     v      v
Research Business Developer
  |       |       |
  +-------+-------+
          |
        Groq
```

El agente `research` también consulta resultados públicos mediante DuckDuckGo antes de generar su respuesta.

## Tecnologías

- Python 3
- FastAPI y Uvicorn
- Groq como proveedor LLM
- Pydantic
- HTTPX
- Pytest

## Requisitos

- Python 3 instalado.
- Una clave de API de [Groq](https://console.groq.com/keys).
- Acceso a Internet para Groq y las búsquedas de investigación.

## Instalación

Clona el repositorio y entra en su directorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd "Multiagent business"
```

Crea y activa un entorno virtual.

En Windows con Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

En Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Crea el archivo de configuración:

```bash
cp .env.example .env
```

Completa `.env` con tu clave:

```env
LLM_API_KEY=tu_clave_de_groq
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile
```

Actualmente, `groq` es el único proveedor LLM soportado.

## Ejecución

Inicia la API en modo desarrollo:

```bash
uvicorn api.main:app --reload
```

La aplicación estará disponible en:

- API: <http://127.0.0.1:8000>
- Swagger UI: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/health>

## Uso de la API

### Comprobar el estado

```bash
curl http://127.0.0.1:8000/health
```

Respuesta:

```json
{
  "status": "ok"
}
```

### Enviar una solicitud al orquestador

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"Busca clientes ideales en Valencia y Alicante\"}"
```

Ejemplo de respuesta:

```json
{
  "routed_to": "research",
  "reply": "Respuesta generada por el agente...",
  "reason": "La solicitud requiere investigación de prospectos."
}
```

El campo `routed_to` puede ser `research`, `business` o `developer`.

### Ejecutar una investigación directa

```bash
curl -X POST http://127.0.0.1:8000/research \
  -H "Content-Type: application/json" \
  -d "{\"cities\":[\"Valencia\",\"Alicante\"],\"limit\":15}"
```

La respuesta contiene el informe, las consultas realizadas, el número de resultados encontrados y una nota de cumplimiento.

También puedes ejecutar el agente desde la terminal:

```bash
python -m api.research Valencia Alicante --limit 15
```

## Tests

Ejecuta la suite con:

```bash
python -m pytest
```

Los tests utilizan mocks para el LLM, por lo que no requieren una clave de Groq.

## Estructura del proyecto

```text
.
├── agents/                  # Prompts y reglas de los agentes
│   ├── orchestrator/
│   ├── research/
│   ├── business/
│   └── developer/
├── api/                     # API, orquestación, LLM y búsqueda web
├── docs/                    # Empresa, plataforma y packs de nicho
│   └── nichos/inmobiliaria/ # Nicho activo (investigación + runtime)
├── tests/                   # Pruebas automatizadas
├── .env.example             # Plantilla de configuración
├── pytest.ini
└── requirements.txt
```

Consulta [`docs/README.md`](docs/README.md) para acceder a la documentación extendida sobre la visión, el ICP, la oferta, el MVP y la arquitectura interna.

## Limitaciones actuales

- No existe persistencia ni memoria entre sesiones.
- La API no incluye autenticación; no debe exponerse directamente en producción.
- Solo se admite Groq como proveedor LLM.
- La búsqueda depende del HTML público de DuckDuckGo.
- Las integraciones reales con CRM todavía no están implementadas.
- El agente de investigación no envía mensajes ni contacta prospectos. Cada contacto y canal debe ser aprobado por una persona.

## Cumplimiento

La investigación utiliza únicamente evidencia pública. El uso de los resultados debe respetar el RGPD, la LSSI y las políticas de cada canal. Este proyecto no automatiza el envío de correos, mensajes ni acciones comerciales.
