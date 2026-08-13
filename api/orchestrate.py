import json
import re
from dataclasses import dataclass
from typing import Callable, Literal

from api.prompts import load_system_prompt
from api.research import run_research
from api.search import SearchHit

AgentName = Literal["developer", "business", "research"]
VALID_AGENTS = frozenset({"developer", "business", "research"})
CompleteFn = Callable[[str, str], str]


@dataclass
class OrchestrationResult:
    routed_to: AgentName
    reply: str
    reason: str


def _extract_json(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise
        return json.loads(match.group(0))


def parse_route(raw: str) -> tuple[AgentName, str]:
    try:
        data = _extract_json(raw)
        agent = str(data.get("agent", "")).strip().lower()
        reason = str(data.get("reason", "")).strip() or "sin motivo"
        if agent in VALID_AGENTS:
            return agent, reason  # type: ignore[return-value]
    except (json.JSONDecodeError, TypeError, AttributeError):
        pass
    return "business", "fallback: respuesta del orchestrator inválida"


def extract_cities(message: str) -> list[str]:
    """Ciudades tras 'en' / 'para'. Si no hay, el caller usa un ámbito por defecto."""
    match = re.search(r"(?:en|para)\s+(.+?)(?:\.|$)", message.strip(), re.IGNORECASE)
    if not match:
        return []
    chunk = match.group(1)
    parts = re.split(r"\s*,\s*|\s+y\s+", chunk)
    skip = {
        "españa",
        "espana",
        "agencias",
        "inmobiliarias",
        "clientes",
        "cuentas",
        "el",
        "la",
        "las",
        "los",
    }
    cities = []
    for part in parts:
        token = re.sub(r"[^A-Za-zÁÉÍÓÚÑáéíóúñ\- ]", "", part).strip()
        token = re.sub(
            r"^(agencias|inmobiliarias|clientes)\s+",
            "",
            token,
            flags=re.IGNORECASE,
        ).strip()
        if not token or token.lower() in skip:
            continue
        cities.append(token)
    return cities


def run_chat(
    message: str,
    complete: CompleteFn,
    *,
    search_hits: list[SearchHit] | None = None,
    search_queries: list[str] | None = None,
) -> OrchestrationResult:
    orch_system = load_system_prompt("orchestrator")
    route_raw = complete(orch_system, message)
    agent, reason = parse_route(route_raw)

    if agent == "research":
        cities = extract_cities(message) or ["España"]
        result = run_research(
            cities,
            complete_fn=complete,
            hits=search_hits,
            queries=search_queries if search_queries is not None else (
                [] if search_hits is not None else None
            ),
        )
        reply = result.reply
        if result.note not in reply:
            reply = f"{reply}\n\n{result.note}"
        return OrchestrationResult(routed_to=agent, reply=reply, reason=reason)

    agent_system = load_system_prompt(agent)
    reply = complete(agent_system, message)
    return OrchestrationResult(routed_to=agent, reply=reply, reason=reason)
