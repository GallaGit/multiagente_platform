import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

DEFAULT_MODEL = "llama-3.3-70b-versatile"


NICHE_ROOT = ROOT_DIR / "docs" / "nichos"
DEFAULT_NICHE = "inmobiliaria"


def _parse_owner_ids(raw: str) -> list[str]:
    return [part.strip() for part in raw.split(",") if part.strip()]


class Settings:
    def __init__(self) -> None:
        self.llm_api_key = os.getenv("LLM_API_KEY", "").strip()
        self.llm_provider = os.getenv("LLM_PROVIDER", "groq").strip().lower()
        self.llm_model = os.getenv("LLM_MODEL", DEFAULT_MODEL).strip()
        self.active_niche = os.getenv("ACTIVE_NICHE", DEFAULT_NICHE).strip() or DEFAULT_NICHE
        self.hubspot_access_token = os.getenv("HUBSPOT_ACCESS_TOKEN", "").strip()
        self.hubspot_portal_id = os.getenv("HUBSPOT_PORTAL_ID", "").strip()
        self.sla_minutes = int(os.getenv("SLA_MINUTES", "60"))
        self.round_robin_owner_ids = _parse_owner_ids(
            os.getenv("ROUND_ROBIN_OWNER_IDS", "")
        )
        cors_raw = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
        self.cors_origins = [origin.strip() for origin in cors_raw.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
