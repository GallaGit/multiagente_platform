import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

DEFAULT_MODEL = "llama-3.3-70b-versatile"


class Settings:
    def __init__(self) -> None:
        self.llm_api_key = os.getenv("LLM_API_KEY", "").strip()
        self.llm_provider = os.getenv("LLM_PROVIDER", "groq").strip().lower()
        self.llm_model = os.getenv("LLM_MODEL", DEFAULT_MODEL).strip()


@lru_cache
def get_settings() -> Settings:
    return Settings()
