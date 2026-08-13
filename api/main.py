from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from api.llm import LLMError, complete
from api.orchestrate import run_chat
from api.registry import is_active
from api.research import run_research

app = FastAPI(title="Multiagent Business", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    routed_to: str
    reply: str
    reason: str


class ResearchRequest(BaseModel):
    cities: list[str] = Field(..., min_length=1)
    limit: int = Field(default=15, ge=1, le=20)


class ResearchResponse(BaseModel):
    reply: str
    queries: list[str]
    hits: int
    note: str


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


@app.post("/research", response_model=ResearchResponse)
def research(body: ResearchRequest) -> ResearchResponse:
    if not is_active("research"):
        raise HTTPException(
            status_code=503,
            detail="research está inactivo: requiere nicho activo en docs/nichos/ o está deshabilitado",
        )
    cities = [c.strip() for c in body.cities if c.strip()]
    if not cities:
        raise HTTPException(status_code=400, detail="cities must not be empty")
    try:
        result = run_research(cities, limit=body.limit, complete_fn=complete)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return ResearchResponse(
        reply=result.reply,
        queries=result.queries,
        hits=result.hits,
        note=result.note,
    )
