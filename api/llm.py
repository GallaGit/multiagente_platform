import httpx
from groq import Groq

from api.config import get_settings


class LLMError(Exception):
    """Raised when the LLM provider call fails."""


def complete(system: str, user: str) -> str:
    settings = get_settings()
    if not settings.llm_api_key:
        raise LLMError("LLM_API_KEY is not set")
    if settings.llm_provider != "groq":
        raise LLMError(
            f"Unsupported LLM_PROVIDER={settings.llm_provider!r}; MVP only supports 'groq'"
        )

    http_client = httpx.Client(verify=settings.llm_verify_ssl)
    client = Groq(api_key=settings.llm_api_key, http_client=http_client)
    try:
        response = client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
            max_completion_tokens=2048,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
        )
    except Exception as exc:  # noqa: BLE001 — surface provider errors as 502
        raise LLMError(str(exc)) from exc
    finally:
        http_client.close()

    content = response.choices[0].message.content
    if not content:
        raise LLMError("Empty response from LLM")
    return content.strip()
