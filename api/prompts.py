from api.config import ROOT_DIR
from api.registry import AgentSpec, format_agent_list, routable_agents

AGENTS_DIR = ROOT_DIR / "agents"
AGENTS_PLACEHOLDER = "{{AGENTS}}"


def load_system_prompt(agent_name: str) -> str:
    path = AGENTS_DIR / agent_name / "system.md"
    if not path.is_file():
        raise FileNotFoundError(f"Prompt not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def load_orchestrator_prompt(
    agents: dict[str, AgentSpec] | None = None,
    *,
    niche_present: bool | None = None,
) -> str:
    template = load_system_prompt("orchestrator")
    routable = agents if agents is not None else routable_agents(
        niche_present=niche_present
    )
    listing = format_agent_list(routable)
    names = "|".join(routable) if routable else "backend"
    text = template.replace(AGENTS_PLACEHOLDER, listing or "- (ningún agente activo)")
    text = text.replace("{{AGENT_NAMES}}", names)
    return text
