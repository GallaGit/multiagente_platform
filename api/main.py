from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from api.llm import LLMError, complete
from api.orchestrate import run_chat

app = FastAPI(title="Multiagent Business", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    routed_to: str
    reply: str
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest) -> ChatResponse:
    message = body.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="message must not be empty")

    try:
        result = run_chat(message, complete)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return ChatResponse(
        routed_to=result.routed_to,
        reply=result.reply,
        reason=result.reason,
    )
