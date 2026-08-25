from api.prompts import load_orchestrator_prompt
from api.registry import (
    AgentSpec,
    active_agents,
    fallback_agent,
    has_niche,
    is_active,
    load_registry,
    routable_agents,
)


def _specs(*, research_enabled: bool = True) -> dict[str, AgentSpec]:
    return {
        "orchestrator": AgentSpec("orchestrator", True, False, "Decide ruta"),
        "frontend": AgentSpec("frontend", True, False, "UI"),
        "backend": AgentSpec("backend", True, False, "API"),
        "developer": AgentSpec("developer", False, False, "Legacy código"),
        "business": AgentSpec("business", False, False, "Legacy propuestas"),
        "research": AgentSpec(
            "research", research_enabled, True, "Cuentas ICP"
        ),
    }


def test_has_niche_true_with_active_pack():
    assert has_niche() is True


def test_research_active_when_niche_present_but_not_routable():
    load_registry.cache_clear()
    assert is_active("research") is True
    assert "research" not in routable_agents()
    assert "frontend" in routable_agents()
    assert "backend" in routable_agents()


def test_research_inactive_without_niche():
    specs = _specs()
    assert is_active("research", specs=specs, niche_present=False) is False
    assert "research" not in routable_agents(specs=specs, niche_present=False)
    assert "frontend" in routable_agents(specs=specs, niche_present=False)
    assert "backend" in routable_agents(specs=specs, niche_present=False)


def test_enabled_false_disables_even_with_niche():
    specs = _specs(research_enabled=False)
    assert is_active("research", specs=specs, niche_present=True) is False
    assert "research" not in active_agents(specs=specs, niche_present=True)


def test_fallback_is_backend_when_available():
    assert fallback_agent(specs=_specs(), niche_present=False) == "backend"


def test_orchestrator_prompt_lists_delivery_agents_only():
    specs = _specs()
    routable = routable_agents(specs=specs, niche_present=True)
    prompt = load_orchestrator_prompt(routable, niche_present=True)
    assert "- research:" not in prompt
    assert "- frontend:" in prompt
    assert "- backend:" in prompt
    assert "- developer:" not in prompt
    assert "- business:" not in prompt


def test_legacy_agents_disabled_in_real_registry():
    load_registry.cache_clear()
    assert is_active("developer") is False
    assert is_active("business") is False
    assert is_active("frontend") is True
    assert is_active("backend") is True
