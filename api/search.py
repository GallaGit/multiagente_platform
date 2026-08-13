"""Búsqueda web pública mínima (DuckDuckGo HTML). Sin scraping de fichas privadas."""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import parse_qs, unquote, urlparse

import httpx

from api.niche import query_templates, skip_hosts

DDG_URL = "https://html.duckduckgo.com/html/"
USER_AGENT = (
    "Mozilla/5.0 (compatible; MultiagentBusinessResearch/0.1; "
    "+https://localhost research-only)"
)


@dataclass(frozen=True)
class SearchHit:
    title: str
    url: str
    snippet: str
    query: str


def build_queries(city: str, templates: list[str] | None = None) -> list[str]:
    city = city.strip()
    patterns = templates if templates is not None else query_templates()
    return [pattern.format(city=city) for pattern in patterns]


def _unwrap_ddg(href: str) -> str:
    if href.startswith("//"):
        href = "https:" + href
    parsed = urlparse(href)
    if "duckduckgo.com" in parsed.netloc and "uddg" in parsed.query:
        values = parse_qs(parsed.query).get("uddg", [])
        if values:
            return unquote(values[0])
    return href


def _host(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def parse_ddg_html(html: str, query: str) -> list[SearchHit]:
    hits: list[SearchHit] = []
    pattern = re.compile(
        r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>'
        r'.*?class="result__snippet"[^>]*>(.*?)</(?:a|td|div)',
        re.IGNORECASE | re.DOTALL,
    )
    for href, title_html, snippet_html in pattern.findall(html):
        url = _unwrap_ddg(href.replace("&amp;", "&"))
        if not url.startswith("http"):
            continue
        if any(skip in _host(url) for skip in skip_hosts()):
            continue
        title = re.sub(r"<[^>]+>", "", title_html)
        snippet = re.sub(r"<[^>]+>", "", snippet_html)
        title = re.sub(r"\s+", " ", title).strip()
        snippet = re.sub(r"\s+", " ", snippet).strip()
        if title and url:
            hits.append(SearchHit(title=title, url=url, snippet=snippet, query=query))
    return hits


def search_web(query: str, *, limit: int = 8, client: httpx.Client | None = None) -> list[SearchHit]:
    own_client = client is None
    http = client or httpx.Client(timeout=20.0, follow_redirects=True, headers={"User-Agent": USER_AGENT})
    try:
        response = http.post(DDG_URL, data={"q": query, "kl": "es-es"})
        response.raise_for_status()
        hits = parse_ddg_html(response.text, query)
        return hits[:limit]
    finally:
        if own_client:
            http.close()


def search_cities(cities: list[str], *, per_query: int = 6) -> tuple[list[SearchHit], list[str]]:
    queries: list[str] = []
    seen_urls: set[str] = set()
    results: list[SearchHit] = []
    with httpx.Client(timeout=20.0, follow_redirects=True, headers={"User-Agent": USER_AGENT}) as client:
        for city in cities:
            for query in build_queries(city):
                queries.append(query)
                try:
                    hits = search_web(query, limit=per_query, client=client)
                except httpx.HTTPError:
                    continue
                for hit in hits:
                    key = hit.url.rstrip("/").lower()
                    if key in seen_urls:
                        continue
                    seen_urls.add(key)
                    results.append(hit)
    return results, queries
