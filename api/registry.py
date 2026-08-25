"""Registro de agentes: quién está activo y quién requiere nicho."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from api.config import ROOT_DIR
from api.niche import has_valid_niche

REGISTRY_PATH = ROOT_DIR / "agents" / "registry.json"
ORCHESTRATOR = "orchestrator"
RESEARCH = "research"
FALLBACK_AGENT = "backend"


@dataclass(frozen=True)
class AgentSpec:
    name: str
    enabled: bool
    requires_niche: bool
    role: str


def _load_raw(path: Path = REGISTRY_PATH) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Registry not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache
def load_registry(path: str | None = None) -> dict[str, AgentSpec]:
    raw = _load_raw(Path(path) if path else REGISTRY_PATH)
    agents = raw.get("agents") or {}
    specs: dict[str, AgentSpec] = {}
    for name, data in agents.items():
        specs[name] = AgentSpec(
            name=name,
            enabled=bool(data.get("enabled", True)),
            requires_niche=bool(data.get("requires_niche", False)),
            role=str(data.get("role", "")).strip(),
        )
    return specs


def has_niche() -> bool:
    return has_valid_niche()


def is_active(
    name: str,
    *,
    specs: dict[str, AgentSpec] | None = None,
    niche_present: bool | None = None,
) -> bool:
    registry = specs if specs is not None else load_registry()
    spec = registry.get(name)
    if spec is None or not spec.enabled:
        return False
    if spec.requires_niche and not (
        has_niche() if niche_present is None else niche_present
    ):
        return False
    return True


def active_agents(
    *,
    specs: dict[str, AgentSpec] | None = None,
    niche_present: bool | None = None,
) -> dict[str, AgentSpec]:
    registry = specs if specs is not None else load_registry()
    present = has_niche() if niche_present is None else niche_present
    return {
        name: spec
        for name, spec in registry.items()
        if is_active(name, specs=registry, niche_present=present)
    }


def routable_agents(
    *,
    specs: dict[str, AgentSpec] | None = None,
    niche_present: bool | None = None,
) -> dict[str, AgentSpec]:
    """Agentes del módulo delivery para POST /chat. Excluye research (POST /research)."""
    return {
        name: spec
        for name, spec in active_agents(
            specs=specs, niche_present=niche_present
        ).items()
        if name not in {ORCHESTRATOR, RESEARCH}
    }


def fallback_agent(
    *,
    specs: dict[str, AgentSpec] | None = None,
    niche_present: bool | None = None,
) -> str:
    routable = routable_agents(specs=specs, niche_present=niche_present)
    if FALLBACK_AGENT in routable:
        return FALLBACK_AGENT
    if routable:
        return next(iter(routable))
    raise RuntimeError("no hay agentes activos para enrutar")


def format_agent_list(agents: dict[str, AgentSpec]) -> str:
    lines = []
    for name, spec in agents.items():
        role = spec.role or name
        lines.append(f"- {name}: {role}")
    return "\n".join(lines)
