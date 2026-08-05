from pathlib import Path

from api.config import ROOT_DIR

AGENTS_DIR = ROOT_DIR / "agents"


def load_system_prompt(agent_name: str) -> str:
    path = AGENTS_DIR / agent_name / "system.md"
    if not path.is_file():
        raise FileNotFoundError(f"Prompt not found: {path}")
    return path.read_text(encoding="utf-8").strip()
