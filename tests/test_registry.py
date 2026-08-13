from api.prompts import load_orchestrator_prompt
from api.registry import (
    AgentSpec,
    active_agents,
    fallback_agent,
    has_niche,
    is_active,
    routable_agents,
)


def _specs(*, research_enabled: bool = True) -> dict[str, AgentSpec]:
    return {
        "orchestrator": AgentSpec("orchestrator", True, False, "Decide ruta"),
        "developer": AgentSpec("developer", True, False, "Código"),
        "business": AgentSpec("business", True, False, "Propuestas"),
        "research": AgentSpec(
            "research", research_enabled, True, "Cuentas ICP"
        ),
    }


def test_has_niche_true_with_active_pack():
    assert has_niche() is True


def test_research_active_when_niche_present():
    assert is_active("research") is True
    assert "research" in routable_agents()


def test_research_inactive_without_niche():
    specs = _specs()
    assert is_active("research", specs=specs, niche_present=False) is False
    assert "research" not in routable_agents(specs=specs, niche_present=False)
    assert "developer" in routable_agents(specs=specs, niche_present=False)
    assert "business" in routable_agents(specs=specs, niche_present=False)


def test_enabled_false_disables_even_with_niche():
    specs = _specs(research_enabled=False)
    assert is_active("research", specs=specs, niche_present=True) is False
    assert "research" not in active_agents(specs=specs, niche_present=True)


def test_fallback_is_business_when_available():
    assert fallback_agent(specs=_specs(), niche_present=False) == "business"


def test_orchestrator_prompt_omits_inactive_research():
    specs = _specs()
    routable = routable_agents(specs=specs, niche_present=False)
    prompt = load_orchestrator_prompt(routable, niche_present=False)
    assert "- research:" not in prompt
    assert "- developer:" in prompt
    assert "- business:" in prompt


def test_orchestrator_prompt_includes_research_when_active():
    specs = _specs()
    routable = routable_agents(specs=specs, niche_present=True)
    prompt = load_orchestrator_prompt(routable, niche_present=True)
    assert "- research:" in prompt
