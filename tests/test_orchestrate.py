from api.orchestrate import extract_cities, parse_route, run_chat
from api.search import SearchHit, parse_ddg_html
from api.research import run_research


def test_parse_route_developer():
    agent, reason = parse_route(
        '{"agent":"developer","reason":"petición técnica de API"}'
    )
    assert agent == "developer"
    assert "técnica" in reason


def test_parse_route_business():
    agent, reason = parse_route(
        '{"agent":"business","reason":"propuesta comercial"}'
    )
    assert agent == "business"
    assert "comercial" in reason


def test_parse_route_research():
    agent, reason = parse_route(
        '{"agent":"research","reason":"listar ICP en Valencia"}'
    )
    assert agent == "research"


def test_parse_route_fallback_on_invalid_json():
    agent, reason = parse_route("no es json")
    assert agent == "business"
    assert "fallback" in reason


def test_parse_route_wrapped_in_markdown():
    raw = 'Aquí va:\n```json\n{"agent":"developer","reason":"código"}\n```'
    agent, reason = parse_route(raw)
    assert agent == "developer"
    assert reason == "código"


def test_extract_cities_valencia_alicante():
    cities = extract_cities("Busca agencias ICP en Valencia y Alicante")
    assert "Valencia" in cities
    assert "Alicante" in cities


def test_run_chat_routes_technical_to_developer():
    calls: list[tuple[str, str]] = []

    def fake_complete(system: str, user: str) -> str:
        calls.append((system, user))
        if "decidir qué agente" in system or "Orchestrator" in system:
            return '{"agent":"developer","reason":"API y FastAPI"}'
        return "Enfoque técnico: endpoints REST, modelos Pydantic, SQLite."

    result = run_chat(
        "Necesito estimar una API REST en FastAPI para un CRM",
        fake_complete,
    )
    assert result.routed_to == "developer"
    assert "técnico" in result.reply.lower() or "REST" in result.reply
    assert result.reason == "API y FastAPI"
    assert len(calls) == 2
    assert "Developer Agent" in calls[1][0]


def test_run_chat_routes_commercial_to_business():
    def fake_complete(system: str, user: str) -> str:
        if "Orchestrator" in system:
            return '{"agent":"business","reason":"propuesta a agencia"}'
        return "Propuesta: diagnóstico y sprint de leads. Siguiente paso discovery."

    result = run_chat(
        "Prepara una propuesta para una agencia que pierde leads",
        fake_complete,
    )
    assert result.routed_to == "business"
    assert "sprint" in result.reply.lower() or "Propuesta" in result.reply


def test_run_chat_research_uses_provided_hits_not_invention():
    hits = [
        SearchHit(
            title="Inmobiliaria Norte Valencia",
            url="https://norte-valencia.example/equipo",
            snippet="Equipo de 8 agentes. Residencial.",
            query="inmobiliaria Valencia",
        )
    ]

    def fake_complete(system: str, user: str) -> str:
        if "Orchestrator" in system:
            return '{"agent":"research","reason":"buscar ICP"}'
        assert "norte-valencia.example" in user
        assert "Research Agent" in system or "ICP-01" in system
        return (
            "| Agencia | Ciudad | Web | Encaje | Oportunidad de proceso | Señales | Descalificadores | "
            "Rol a contactar | Fuente | Confianza | Pregunta de discovery |\n"
            "| Norte | Valencia | https://norte-valencia.example/equipo | media | leads sin dueño | 8 agentes | | "
            "gerente | https://norte-valencia.example/equipo | baja | ¿quién asigna el lead? |"
        )

    result = run_chat(
        "Busca clientes ideales en Valencia",
        fake_complete,
        search_hits=hits,
        search_queries=["inmobiliaria Valencia"],
    )
    assert result.routed_to == "research"
    assert "Norte" in result.reply
    assert "No enviar mensajes" in result.reply


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


def test_parse_ddg_html_extracts_result():
    html = """
    <a rel="nofollow" class="result__a" href="https://agencia-demo.example/equipo">Demo Agencia</a>
    <a class="result__snippet">Equipo de 6 personas en Valencia</a>
    """
    hits = parse_ddg_html(html, "q")
    assert len(hits) == 1
    assert hits[0].url == "https://agencia-demo.example/equipo"
    assert "Demo" in hits[0].title
