"""Carga el pack de nicho activo (manifest + archivos de contexto)."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from api.config import NICHE_ROOT, get_settings

GENERIC_SKIP_HOSTS = (
    "duckduckgo.com",
    "youtube.com",
    "facebook.com",
    "instagram.com",
    "wikipedia.org",
    "linkedin.com",
)
GENERIC_SKIP_TOKENS = frozenset(
    {"españa", "espana", "clientes", "cuentas", "el", "la", "las", "los"}
)


@dataclass(frozen=True)
class NichePack:
    id: str
    label: str
    market: str
    entity_singular: str
    entity_plural: str
    skip_tokens: tuple[str, ...]
    context_files: tuple[str, ...]
    query_templates: tuple[str, ...]
    skip_hosts: tuple[str, ...]
    root: Path
    context_text: str = ""
    extra: dict = field(default_factory=dict)


def niche_dir(niche_id: str | None = None, *, root: Path | None = None) -> Path:
    base = root if root is not None else NICHE_ROOT
    name = niche_id if niche_id is not None else get_settings().active_niche
    return base / name


def _read_manifest(folder: Path) -> dict | None:
    path = folder / "manifest.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _context_paths(folder: Path, names: list[str]) -> list[Path]:
    paths = []
    for name in names:
        path = folder / name
        if path.is_file():
            paths.append(path)
    return paths


def has_valid_niche(
    niche_id: str | None = None,
    *,
    root: Path | None = None,
) -> bool:
    folder = niche_dir(niche_id, root=root)
    raw = _read_manifest(folder)
    if not raw:
        return False
    files = raw.get("context_files") or []
    return bool(_context_paths(folder, list(files)))


def load_niche(
    niche_id: str | None = None,
    *,
    root: Path | None = None,
) -> NichePack | None:
    folder = niche_dir(niche_id, root=root)
    raw = _read_manifest(folder)
    if not raw:
        return None
    files = list(raw.get("context_files") or [])
    paths = _context_paths(folder, files)
    if not paths:
        return None
    entity = raw.get("entity") or {}
    search = raw.get("search") or {}
    context = "\n\n".join(p.read_text(encoding="utf-8") for p in paths)
    skip_tokens = tuple(
        str(t).lower() for t in (entity.get("skip_tokens") or [])
    )
    return NichePack(
        id=str(raw.get("id") or folder.name),
        label=str(raw.get("label") or folder.name),
        market=str(raw.get("market") or ""),
        entity_singular=str(entity.get("singular") or "cuenta"),
        entity_plural=str(entity.get("plural") or "cuentas"),
        skip_tokens=skip_tokens,
        context_files=tuple(files),
        query_templates=tuple(search.get("query_templates") or []),
        skip_hosts=tuple(search.get("skip_hosts") or []),
        root=folder,
        context_text=context,
    )


@lru_cache
def active_niche() -> NichePack | None:
    return load_niche()


def load_niche_context() -> str:
    pack = active_niche()
    return pack.context_text if pack else ""


def query_templates() -> list[str]:
    pack = active_niche()
    if pack and pack.query_templates:
        return list(pack.query_templates)
    return ["{city} empresa equipo CRM"]


def skip_hosts() -> tuple[str, ...]:
    pack = active_niche()
    extra = pack.skip_hosts if pack else ()
    return GENERIC_SKIP_HOSTS + extra


def skip_tokens() -> set[str]:
    pack = active_niche()
    extra = set(pack.skip_tokens) if pack else set()
    return set(GENERIC_SKIP_TOKENS) | extra


def entity_plural() -> str:
    pack = active_niche()
    return pack.entity_plural if pack else "cuentas"


def prefix_tokens() -> tuple[str, ...]:
    pack = active_niche()
    extra = set(pack.skip_tokens) if pack else set()
    extra.update({"clientes", "cuentas"})
    extra -= {"el", "la", "las", "los", "españa", "espana"}
    return tuple(sorted(extra, key=len, reverse=True))


def clear_niche_cache() -> None:
    active_niche.cache_clear()
    get_settings.cache_clear()
