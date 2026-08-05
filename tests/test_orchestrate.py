from api.orchestrate import parse_route, run_chat


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


def test_parse_route_fallback_on_invalid_json():
    agent, reason = parse_route("no es json")
    assert agent == "business"
    assert "fallback" in reason


def test_parse_route_wrapped_in_markdown():
    raw = 'Aquí va:\n```json\n{"agent":"developer","reason":"código"}\n```'
    agent, reason = parse_route(raw)
    assert agent == "developer"
    assert reason == "código"


def test_run_chat_routes_technical_to_developer():
    calls: list[tuple[str, str]] = []

    def fake_complete(system: str, user: str) -> str:
        calls.append((system, user))
        if "CEO Orchestrator" in system:
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
        if "CEO Orchestrator" in system:
            return '{"agent":"business","reason":"propuesta a clínica"}'
        return "Propuesta: web para clínica, siguiente paso reunión de discovery."

    result = run_chat(
        "Prepara una propuesta para una clínica que quiere una web",
        fake_complete,
    )
    assert result.routed_to == "business"
    assert "clínica" in result.reply.lower() or "Propuesta" in result.reply
    assert result.reason == "propuesta a clínica"
