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
            "corpus_info", "search_hybrid", "search_dense", "search_auto", "route_query",
            "get_passage", "verify_quote"} <= names
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


@pytest.fixture
def paper_index(tmp_path, monkeypatch):
    """A two-paper passage index chunked like build-papers: each chunk repeats
    the last `overlap` characters of the one before it."""
    overlap = 20
    papers = {
        "18948947": ["KRAS mutations correlate with smoker status (P=0.021).",
                     ("The negative correlation of mutations in EGFR and KRAS was confirmed "
                      "(P < 1 × 10-07), with no sample having both."),
                     "Mutations at non- synonymous sites were common."],
        "25079552": ["Cancer-associated mutations in KRAS (32%, n =74) were common.",
                     "This increases the fraction with RTK/RAS/RAF activation from 62% to 76%."],
        # A reference number glued to a word, as PDF extraction leaves it.
        "41895280": [("In addition to the previously reported RRAS2 Q72 hotspot24 (n = 49 mutated "
                      "tumors), we identified two other hotspot residues.")],
        # Two-column PDF text with the spaces lost.
        "29657128": [("HighTMBcorrelateswithefficacyofcombinationimmunotherapy in patients "
                      "Wesoughttoexaminethemolecularfeaturescorrelatedwith response ") * 3],
    }
    lines = []
    for pmid, sentences in papers.items():
        prev = ""
        for i, s in enumerate(sentences):
            text = f"{prev[-overlap:]} {s}" if prev else s
            lines.append(json.dumps({"pmid": pmid, "chunk_id": i, "text": text}))
            prev = text
    (tmp_path / "meta.jsonl").write_text("\n".join(lines) + "\n")
    (tmp_path / "index_config.json").write_text(json.dumps({"overlap": overlap}))
    monkeypatch.setattr(m, "INDEX_DIR", tmp_path)
    m._paper_texts.cache_clear()
    m._loose_corpus.cache_clear()
    yield
    m._paper_texts.cache_clear()
    m._loose_corpus.cache_clear()


def test_get_passage_returns_text_without_chunk_overlap(paper_index):
    out = call("get_passage", pmid="18948947", chunk_id=1, context=1)
    assert [p["chunk_id"] for p in out["passages"]] == [0, 1, 2]
    assert out["passages"][1]["text"].startswith("The negative correlation")
    assert out["text_source"].startswith("paper_text")
    assert out["pmc_url"] == "https://pmc.ncbi.nlm.nih.gov/articles/PMC2694412/"
    assert "passages 0-2" in call("get_passage", pmid="18948947", chunk_id=9)["error_message"]


def test_verify_quote_exact_across_a_chunk_boundary(paper_index):
    out = call("verify_quote", pmid="PMID:18948947",
               quote="“with no sample having both. Mutations at non- synonymous sites”")
    assert out["verified"] and out["match"] == "exact" and out["chunk_id"] == 1
    link = call("verify_quote", pmid="18948947",
                quote="KRAS mutations correlate with smoker status (P=0.021)")["pmc_link"]
    assert link == ("https://pmc.ncbi.nlm.nih.gov/articles/PMC2694412/"
                    "#:~:text=KRAS%20mutations%20correlate%20with%20smoker%20status")


@pytest.mark.parametrize("quote, level", [
    ("mutations in EGFR and KRAS was confirmed (P < 1 × 10–07)", "normalized"),  # en dash
    ("Mutations at non-synonymous sites were common", "normalized"),             # hyphenation
    ("Mutations at nonsynonymous sites were common", "loose"),
    ("KRAS mutations correlate with smoker status ... negative correlation of mutations", "exact"),
])
def test_verify_quote_match_levels(paper_index, quote, level):
    out = call("verify_quote", pmid="18948947", quote=quote)
    assert out["verified"] and out["match"] == level
    if level != "exact":
        assert "paper_wording" in out["note"]


def test_verify_quote_miss_points_to_closest_and_the_right_paper(paper_index):
    out = call("verify_quote", pmid="18948947", quote="Cancer-associated mutations in KRAS (32%, n =74)")
    assert out["verified"] is False
    assert [p["pmid"] for p in out["found_in_other_papers"]] == ["25079552"]
    made_up = call("verify_quote", pmid="25079552",
                   quote="RTK/RAS/RAF activation was found in 62-85% of tumours")
    assert made_up["verified"] is False and "62% to 76%" in made_up["closest"][0]["text"]


def test_verify_quote_ignores_glued_reference_numbers_but_not_gene_digits(paper_index):
    out = call("verify_quote", pmid="41895280",
               quote="the previously reported RRAS2 Q72 hotspot (n = 49 mutated tumors)")
    assert out["verified"] and out["match"] == "normalized"
    assert "hotspot (n = 49" in out["paper_wording"]            # marker dropped for quoting
    assert call("verify_quote", pmid="41895280",
                quote="RRAS2 Q72 hotspot24 (n = 49 mutated")["match"] == "exact"
    dropped_gene_digit = call("verify_quote", pmid="41895280",
                              quote="the previously reported RRAS Q72 hotspot (n = 49 mutated tumors)")
    assert dropped_gene_digit["verified"] is False


def test_garbled_paper_is_flagged(paper_index):
    out = call("verify_quote", pmid="29657128", quote="High TMB correlates with efficacy of immunotherapy")
    assert out["verified"] is False and out["closest"] == []
    assert out["text_quality"].startswith("garbled")
    assert call("get_passage", pmid="29657128", chunk_id=0)["text_quality"].startswith("garbled")
    assert "text_quality" not in call("get_passage", pmid="18948947", chunk_id=0)
    passages = m._passage_view([{"pmid": "29657128", "chunk_id": 0, "text": "…"},
                                {"pmid": "18948947", "chunk_id": 0, "text": "…"}], top_k=5)
    assert [p.get("text_quality", "")[:7] for p in passages] == ["garbled", ""]


def test_verify_quote_errors(paper_index, tmp_path):
    assert "too short" in call("verify_quote", pmid="18948947", quote="KRAS")["error_message"]
    assert "not in the corpus" in call("verify_quote", pmid="1", quote="some long enough quote")["error_message"]
    (tmp_path / "meta.jsonl").unlink()
    assert "Passage index not found" in call("get_passage", pmid="18948947", chunk_id=0)["error_message"]


def test_wiki_results_are_labeled_as_summaries():
    assert call("get_paper", pmid="39506116")["text_source"].startswith("wiki_summary")
    assert call("get_entity", kind="gene", id="EGFR", max_chars=500)["text_source"].startswith("wiki_summary")


@pytest.mark.skipif(not (m.INDEX_DIR / "meta.jsonl").exists(), reason="needs the built passage index")
def test_verify_quote_on_the_real_index():
    out = call("verify_quote", pmid="18948947", quote="KRAS mutations correlate with smoker status (P=0.021)")
    assert out["verified"] and out["match"] == "exact"


def test_retracted_paper_is_flagged():
    # PMID 32214244 (Poore et al. 2020) was retracted in 2024 but is still attached
    # to cBioPortal's TCGA PanCancer studies.
    out = call("get_paper", pmid="32214244", sections=["TL;DR"])
    assert out["retracted"] is True
    study = call("get_study_papers", study_id="brca_tcga_pan_can_atlas_2018")
    assert any(p.get("retracted") for p in study["papers"] if p["pmid"] == "32214244")
