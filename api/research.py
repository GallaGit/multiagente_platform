"""Pipeline de research ICP: busca fuentes públicas y puntúa. No envía mensajes."""

from __future__ import annotations

from dataclasses import dataclass

from api.config import ROOT_DIR
from api.llm import complete
from api.prompts import load_system_prompt
from api.search import SearchHit, search_cities


@dataclass
class ResearchResult:
    reply: str
    queries: list[str]
    hits: int
    note: str = "No enviar mensajes. Un humano debe aprobar cada contacto y el canal."


def _extra_context() -> str:
    parts: list[str] = []
    for path in (
        ROOT_DIR / "agents" / "research" / "rules.md",
        ROOT_DIR / "knowledge" / "inmobiliario_leads" / "icp-research.md",
    ):
        if path.is_file():
            parts.append(path.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def _format_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "(ningún resultado web recuperado)"
    lines = []
    for i, hit in enumerate(hits, start=1):
        lines.append(
            f"{i}. título: {hit.title}\n"
            f"   url: {hit.url}\n"
            f"   snippet: {hit.snippet}\n"
            f"   consulta: {hit.query}"
        )
    return "\n".join(lines)


def build_user_prompt(
    cities: list[str],
    limit: int,
    hits: list[SearchHit],
    queries: list[str],
) -> str:
    cities_txt = ", ".join(cities)
    return (
        f"Ciudades pedidas: {cities_txt}\n"
        f"Máximo de cuentas a listar: {limit}\n\n"
        "Consultas usadas:\n- "
        + "\n- ".join(queries)
        + "\n\nResultados públicos (ÚNICA evidencia permitida):\n"
        + _format_hits(hits)
        + "\n\nInstrucción: lista solo agencias de esos resultados con oportunidad de "
        "optimizar o automatizar procesos (canales, CRM, leads, equipo, fricción). "
        "No listes inmobiliarias genéricas sin esa señal. No inventes filas. No envíes emails."
    )


def run_research(
    cities: list[str],
    *,
    limit: int = 15,
    complete_fn=complete,
    hits: list[SearchHit] | None = None,
    queries: list[str] | None = None,
) -> ResearchResult:
    cities = [c.strip() for c in cities if c.strip()]
    if not cities:
        raise ValueError("indica al menos una ciudad")
    limit = max(1, min(limit, 20))

    if hits is None or queries is None:
        hits, queries = search_cities(cities)

    system = load_system_prompt("research")
    extra = _extra_context()
    if extra:
        system = f"{system}\n\n{extra}"

    user = build_user_prompt(cities, limit, hits, queries)
    reply = complete_fn(system, user)
    return ResearchResult(reply=reply, queries=queries, hits=len(hits))


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Lista candidatas ICP-01. No envía mensajes."
    )
    parser.add_argument("cities", nargs="+", help="Ciudades, p.ej. Valencia Alicante")
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args()
    result = run_research(args.cities, limit=args.limit)
    print(result.reply)
    print("\n---")
    print(result.note)
    print(f"Consultas: {len(result.queries)} | Hits: {result.hits}")


if __name__ == "__main__":
    main()
