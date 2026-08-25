from fastapi.testclient import TestClient

from api.main import app
from api.orchestrate import extract_cities, parse_route, run_chat
from api.research import run_research
from api.search import SearchHit, parse_ddg_html


def test_parse_route_backend():
    agent, reason, brief = parse_route(
        '{"agent":"backend","reason":"API y webhook","brief":"Objetivo: webhook. Alcance: ingest."}'
    )
    assert agent == "backend"
    assert "API" in reason
    assert "webhook" in brief.lower()


def test_parse_route_frontend():
    agent, reason, brief = parse_route(
        '{"agent":"frontend","reason":"panel UI","brief":"Objetivo: panel de excepciones."}'
    )
    assert agent == "frontend"
    assert "panel" in reason.lower()
    assert "excepciones" in brief.lower()


def test_parse_route_fallback_on_invalid_json():
    agent, reason, brief = parse_route("no es json")
    assert agent == "backend"
    assert "fallback" in reason
    assert brief == ""


def test_parse_route_wrapped_in_markdown():
    raw = (
        'Aquí va:\n```json\n{"agent":"frontend","reason":"UI",'
        '"brief":"Login React"}\n```'
    )
    agent, reason, brief = parse_route(raw)
    assert agent == "frontend"
    assert reason == "UI"
    assert brief == "Login React"


def test_parse_route_unknown_agent_falls_back():
    agent, reason, brief = parse_route(
        '{"agent":"research","reason":"listar ICP","brief":"no aplica"}',
        valid_agents={"frontend", "backend"},
        fallback="backend",
    )
    assert agent == "backend"
    assert "inactivo" in reason
    assert brief == "no aplica"


def test_extract_cities_valencia_alicante():
    cities = extract_cities("Busca agencias ICP en Valencia y Alicante")
    assert "Valencia" in cities
    assert "Alicante" in cities


def test_run_chat_routes_api_to_backend():
    calls: list[tuple[str, str]] = []

    def fake_complete(system: str, user: str) -> str:
        calls.append((system, user))
        if "ÚNICAMENTE con JSON" in system or "Delegar la implementación" in system:
            return (
                '{"agent":"backend","reason":"API y FastAPI",'
                '"brief":"Objetivo: API REST. Alcance: CRM. Entregables: endpoints."}'
            )
        assert "Brief del Orchestrator" in user
        return "Enfoque técnico: endpoints REST, modelos Pydantic."

    result = run_chat(
        "Necesito una API REST en FastAPI para el CRM",
        fake_complete,
    )
    assert result.routed_to == "backend"
    assert "REST" in result.reply or "endpoints" in result.reply.lower()
    assert result.reason == "API y FastAPI"
    assert "API REST" in result.documentation
    assert len(calls) == 2
    assert "Backend Agent" in calls[1][0]


def test_run_chat_routes_ui_to_frontend():
    def fake_complete(system: str, user: str) -> str:
        if "ÚNICAMENTE con JSON" in system or "Delegar la implementación" in system:
            return (
                '{"agent":"frontend","reason":"panel de excepciones",'
                '"brief":"Objetivo: UI de cola de excepciones."}'
            )
        assert "Brief del Orchestrator" in user
        return "Propongo lista filtrable con estado y CTA resolver."

    result = run_chat(
        "Diseña la pantalla de cola de excepciones de leads",
        fake_complete,
    )
    assert result.routed_to == "frontend"
    assert "lista" in result.reply.lower() or "excepciones" in result.reply.lower()
    assert "excepciones" in result.documentation.lower()


def test_run_chat_does_not_route_research():
    def fake_complete(system: str, user: str) -> str:
        if "ÚNICAMENTE con JSON" in system or "Delegar la implementación" in system:
            assert "- research:" not in system
            return '{"agent":"research","reason":"buscar ICP","brief":""}'
        return "Respuesta backend por fallback."

    result = run_chat(
        "Busca clientes ideales en Valencia",
        fake_complete,
    )
    assert result.routed_to == "backend"
    assert "inactivo" in result.reason or "fallback" in result.reason


def test_run_research_without_hits_does_not_require_web():
    def fake_complete(system: str, user: str) -> str:
        assert "ningún resultado" in user
        return "No hay evidencia pública en esta corrida. No invento agencias."

    result = run_research(
        ["Valencia"],
        complete_fn=fake_complete,
        hits=[],
        queries=["inmobiliaria independiente Valencia"],
    )
    assert result.hits == 0
    assert "No invento" in result.reply


def test_research_endpoint_503_when_inactive(monkeypatch):
    monkeypatch.setattr("api.main.is_active", lambda name: False)
    client = TestClient(app)
    response = client.post("/research", json={"cities": ["Valencia"]})
    assert response.status_code == 503
    assert "inactivo" in response.json()["detail"]


def test_parse_ddg_html_extracts_result():
    html = """
    <a rel="nofollow" class="result__a" href="https://agencia-demo.example/equipo">Demo Agencia</a>
    <a class="result__snippet">Equipo de 6 personas en Valencia</a>
    """
    hits = parse_ddg_html(html, "q")
    assert len(hits) == 1
    assert hits[0].url == "https://agencia-demo.example/equipo"
    assert "Demo" in hits[0].title


def test_run_research_still_works_with_hits():
    hits = [
        SearchHit(
            title="Inmobiliaria Norte Valencia",
            url="https://norte-valencia.example/equipo",
            snippet="Equipo de 8 agentes. Residencial.",
            query="inmobiliaria Valencia",
        )
    ]

    def fake_complete(system: str, user: str) -> str:
        assert "norte-valencia.example" in user
        return (
            "| Agencia | Ciudad | Web | Encaje | Oportunidad de proceso | Señales | "
            "Descalificadores | Rol a contactar | Fuente | Confianza | Pregunta de discovery |\n"
            "| Norte | Valencia | https://norte-valencia.example/equipo | media | leads sin dueño | "
            "8 agentes | | gerente | https://norte-valencia.example/equipo | baja | ¿quién asigna? |"
        )

    result = run_research(
        ["Valencia"],
        complete_fn=fake_complete,
        hits=hits,
        queries=["inmobiliaria Valencia"],
    )
    assert result.hits == 1
    assert "Norte" in result.reply
