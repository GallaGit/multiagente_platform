import json
import re
from dataclasses import dataclass
from typing import Callable, Literal

from api.prompts import load_system_prompt

AgentName = Literal["developer", "business"]
VALID_AGENTS = frozenset({"developer", "business"})
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


def run_chat(message: str, complete: CompleteFn) -> OrchestrationResult:
    orch_system = load_system_prompt("orchestrator")
    route_raw = complete(orch_system, message)
    agent, reason = parse_route(route_raw)

    agent_system = load_system_prompt(agent)
    reply = complete(agent_system, message)
    return OrchestrationResult(routed_to=agent, reply=reply, reason=reason)
