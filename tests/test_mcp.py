"""cbio-kb MCP server: tool contracts over the real wiki, via an in-memory client."""
import asyncio
import json

import pytest

pytest.importorskip("fastmcp")
from fastmcp import Client  # noqa: E402

import ai_search.mcp as m  # noqa: E402


def call(tool: str, **args):
    async def _go():
        async with Client(m.mcp) as c:
            res = await c.call_tool(tool, args, raise_on_error=False)
            if res.structured_content is not None:
                return res.structured_content.get("result", res.structured_content)
            return json.loads(res.content[0].text)
    return asyncio.run(_go())


def test_tools_and_instructions_are_exposed():
    async def _go():
        async with Client(m.mcp) as c:
            names = {t.name for t in await c.list_tools()}
            return names, c.initialize_result.instructions
    names, instructions = asyncio.run(_go())
    assert {"get_study_papers", "get_paper", "list_papers", "get_entity", "read_wiki_page",
            "corpus_info", "search_hybrid", "search_dense", "search_auto", "route_query"} <= names
    # Must not collide with cbioportal-mcp / cbioportal-navigator tool names.
    assert not names & {"list_studies", "get_study_guide", "list_guides", "read_guide",
                        "search_oncotree", "resolve_and_route", "clickhouse_run_select_query"}
    assert "cbioportal-mcp" in instructions


def test_study_to_paper_bridge():
    out = call("get_study_papers", study_id="MSK_CHORD_2024")  # case-insensitive
    assert out["study_id"] == "msk_chord_2024"
    assert out["cbioportal_url"].endswith("id=msk_chord_2024")
    assert [p["pmid"] for p in out["papers"] if p["in_corpus"]] == ["39506116"]


def test_study_whose_paper_is_not_open_access():
    out = call("get_study_papers", study_id="nsclc_tracerx_2017")
    by_pmid = {p["pmid"]: p for p in out["papers"]}
    # 28445112 (NEJM) is not in PMC; the page once filed under it was a citing paper.
    assert by_pmid["28445112"]["in_corpus"] is False


def test_unknown_study_is_not_called_nonexistent():
    out = call("get_study_papers", study_id="msk_chord")
    assert "does not prove it doesn't exist" in out["error_message"]
    assert "msk_chord_2024" in [s["study_id"] for s in out["similar_studies"]]


def test_get_paper_sections_and_study_ids():
    out = call("get_paper", pmid="PMID:39506116", sections=["key"])
    assert out["pmid"] == "39506116"
    assert "msk_chord_2024" in out["study_ids"]
    assert list(out["sections"]) == ["Key findings"]


def test_get_paper_for_study_publication_outside_corpus():
    out = call("get_paper", pmid="28445112")
    assert "nsclc_tracerx_2017" in out["error_message"]
    assert out["study_ids"] == ["nsclc_tracerx_2017"]


def test_get_entity_resolution():
    gene = call("get_entity", kind="gene", id="egfr", section="Overview")
    assert gene["id"] == "EGFR" and gene["cited_by_total"] > 0
    assert gene["content"].startswith("## Overview")
    luad = call("get_entity", kind="cancer_type", id="Lung Adenocarcinoma", max_chars=500)
    assert luad["id"] == "LUAD"
    miss = call("get_entity", kind="gene", id="EGFRR")
    assert "EGFR" in miss["did_you_mean"]


def test_read_wiki_page_accepts_links_and_blocks_traversal():
    ok = call("read_wiki_page", path="../papers/39506116.html", heading="TL;DR")
    assert ok["path"] == "papers/39506116.md" and ok["content"].startswith("## TL;DR")
    assert "error_message" in call("read_wiki_page", path="../../pyproject.toml")


def test_list_papers_filters():
    out = call("list_papers", study_id="msk_chord_2024", limit=100)
    assert "39506116" in [p["pmid"] for p in out["papers"]]
    ranked = call("list_papers", search="clonal hematopoiesis", limit=3)
    assert len(ranked["papers"]) == 3 and ranked["papers"][0]["score"] > 0


def test_corpus_info_reports_coverage():
    info = call("corpus_info")
    assert info["papers"] >= 377
    assert 0 < info["cbioportal_publications_in_corpus"] <= info["cbioportal_publications"]


def test_search_without_index_returns_error_message(tmp_path, monkeypatch):
    monkeypatch.setattr(m, "INDEX_DIR", tmp_path)
    out = call("search_hybrid", query="KRAS G12C")
    assert "Passage index not found" in out["error_message"]


def test_run_config(monkeypatch):
    for k in ("SERVER_TRANSPORT", "BIND_HOST", "BIND_PORT", "HTTP_PATH", "FORWARDED_ALLOW_IPS"):
        monkeypatch.delenv(f"CBIO_KB_MCP_{k}", raising=False)
    assert m.run_config([]) == {"transport": "stdio"}
    assert m.run_config(["--port", "9000"]) == {"transport": "http", "host": "127.0.0.1", "port": 9000}
    monkeypatch.setenv("CBIO_KB_MCP_SERVER_TRANSPORT", "http")
    monkeypatch.setenv("CBIO_KB_MCP_HTTP_PATH", "/lit/mcp")
    monkeypatch.setenv("CBIO_KB_MCP_FORWARDED_ALLOW_IPS", "*")
    cfg = m.run_config([])
    assert cfg["path"] == "/lit/mcp" and cfg["port"] == 8124
    assert cfg["uvicorn_config"] == {"proxy_headers": True, "forwarded_allow_ips": "*"}


def test_health_route():
    from starlette.testclient import TestClient

    with TestClient(m.mcp.http_app()) as client:
        r = client.get("/health")
    assert r.status_code == 200 and r.json()["service"] == "cbio-kb"
