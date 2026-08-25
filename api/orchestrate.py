import json
import re
from dataclasses import dataclass
from typing import Callable

from api.niche import prefix_tokens, skip_tokens
from api.prompts import load_orchestrator_prompt, load_system_prompt
from api.registry import fallback_agent, routable_agents

CompleteFn = Callable[[str, str], str]

DELIVERY_AGENTS = frozenset({"frontend", "backend"})


@dataclass
class OrchestrationResult:
    routed_to: str
    reply: str
    reason: str
    documentation: str = ""


def _extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise
        return json.loads(match.group(0))


def parse_route(
    raw: str,
    valid_agents: set[str] | None = None,
    *,
    fallback: str | None = None,
) -> tuple[str, str, str]:
    """Return (agent, reason, brief)."""
    allowed = valid_agents if valid_agents is not None else set(routable_agents())
    fallback_name = fallback if fallback is not None else fallback_agent()
    try:
        data = _extract_json(raw)
        agent = str(data.get("agent", "")).strip().lower()
        reason = str(data.get("reason", "")).strip() or "sin motivo"
        brief = str(data.get("brief", "")).strip()
        if agent in allowed:
            return agent, reason, brief
        if agent:
            return (
                fallback_name,
                f"fallback: agente '{agent}' inactivo o desconocido",
                brief,
            )
    except (json.JSONDecodeError, TypeError, AttributeError):
        pass
    return (
        fallback_name,
        "fallback: respuesta del orchestrator inválida",
        "",
    )


def extract_cities(message: str) -> list[str]:
    """Ciudades tras 'en' / 'para'. Si no hay, el caller usa un ámbito por defecto."""
    match = re.search(r"(?:en|para)\s+(.+?)(?:\.|$)", message.strip(), re.IGNORECASE)
    if not match:
        return []
    chunk = match.group(1)
    parts = re.split(r"\s*,\s*|\s+y\s+", chunk)
    skip = skip_tokens()
    prefixes = "|".join(re.escape(t) for t in prefix_tokens())
    cities = []
    for part in parts:
        token = re.sub(r"[^A-Za-zÁÉÍÓÚÑáéíóúñ\- ]", "", part).strip()
        if prefixes:
            token = re.sub(
                rf"^({prefixes})\s+",
                "",
                token,
                flags=re.IGNORECASE,
            ).strip()
        if not token or token.lower() in skip:
            continue
        cities.append(token)
    return cities


def _agent_user_message(message: str, brief: str) -> str:
    if not brief:
        return message
    return (
        f"Encargo del usuario:\n{message}\n\n"
        f"Brief del Orchestrator (especificación):\n{brief}"
    )


def run_chat(
    message: str,
    complete: CompleteFn,
    *,
    niche_present: bool | None = None,
) -> OrchestrationResult:
    routable = routable_agents(niche_present=niche_present)
    fallback = fallback_agent(niche_present=niche_present)
    orch_system = load_orchestrator_prompt(routable, niche_present=niche_present)
    route_raw = complete(orch_system, message)
    agent, reason, brief = parse_route(
        route_raw, set(routable), fallback=fallback
    )
    if agent not in DELIVERY_AGENTS:
        agent = fallback if fallback in DELIVERY_AGENTS else "backend"
        reason = f"fallback: agente no es frontend|backend ({reason})"
        if not brief:
            brief = "Brief no disponible; implementar el encargo con foco backend."

    agent_system = load_system_prompt(agent)
    reply = complete(agent_system, _agent_user_message(message, brief))
    return OrchestrationResult(
        routed_to=agent,
        reply=reply,
        reason=reason,
        documentation=brief,
    )
