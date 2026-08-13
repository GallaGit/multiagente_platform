import json

from api.niche import (
    clear_niche_cache,
    has_valid_niche,
    load_niche,
    query_templates,
)
from api.search import build_queries


def _write_niche(folder, *, with_manifest=True, with_context=True, queries=None):
    folder.mkdir(parents=True, exist_ok=True)
    if with_context:
        runtime = folder / "runtime"
        runtime.mkdir(exist_ok=True)
        (runtime / "icp-research.md").write_text("# ICP-01 test\n", encoding="utf-8")
    if with_manifest:
        payload = {
            "id": folder.name,
            "label": "Test niche",
            "market": "España",
            "entity": {
                "singular": "agencia",
                "plural": "agencias",
                "skip_tokens": ["agencias"],
            },
            "context_files": ["runtime/icp-research.md"],
            "search": {
                "query_templates": queries
                or ["demo {city} CRM"],
                "skip_hosts": ["example-portal.com"],
            },
        }
        (folder / "manifest.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )


def test_has_valid_niche_with_real_inmobiliaria():
    assert has_valid_niche("inmobiliaria") is True


def test_has_niche_false_without_manifest(tmp_path):
    empty = tmp_path / "vacio"
    empty.mkdir()
    assert has_valid_niche("vacio", root=tmp_path) is False


def test_has_niche_false_manifest_without_files(tmp_path):
    folder = tmp_path / "roto"
    _write_niche(folder, with_context=False)
    assert has_valid_niche("roto", root=tmp_path) is False


def test_load_niche_reads_context(tmp_path):
    folder = tmp_path / "demo"
    _write_niche(folder)
    pack = load_niche("demo", root=tmp_path)
    assert pack is not None
    assert "ICP-01" in pack.context_text
    assert pack.entity_plural == "agencias"


def test_build_queries_uses_templates():
    queries = build_queries("Valencia", templates=["foo {city} bar"])
    assert queries == ["foo Valencia bar"]


def test_query_templates_from_active_inmobiliaria():
    clear_niche_cache()
    templates = query_templates()
    assert any("{city}" in t and "inmobiliaria" in t for t in templates)
