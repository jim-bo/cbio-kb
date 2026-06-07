"""Tests for the auto-mode query router.

Exercises only the network-free pieces: the lexical-heuristic classifier, the
eval-derived category->mode policy, and the graceful kNN->heuristic fallback
when embeddings are unavailable. Vertex embedding (the kNN primary path) is an
integration concern and is not exercised here.
"""
from __future__ import annotations

import pytest

from ai_search import router
from ai_search.router import MODE_BY_CATEGORY, RouteDecision, classify_heuristic


# ---------------------------------------------------------------------------
# Policy: the eval-derived mapping is the contract other code relies on
# ---------------------------------------------------------------------------


def test_policy_maps_factual_to_hybrid_and_complex_to_agentic() -> None:
    assert MODE_BY_CATEGORY["lookup"] == "hybrid"
    assert MODE_BY_CATEGORY["definition"] == "hybrid"
    assert MODE_BY_CATEGORY["list"] == "agentic"
    assert MODE_BY_CATEGORY["synthesis"] == "agentic"


# ---------------------------------------------------------------------------
# Heuristic classifier
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "query,expected",
    [
        ("List all papers that used MSK-IMPACT.", "list"),
        ("Which studies profiled lung adenocarcinoma?", "list"),
        ("Compare KRAS mutation rates across the corpus.", "synthesis"),
        ("What is the relationship between TMB and immunotherapy response?", "synthesis"),
        ("What is MSK-IMPACT?", "definition"),
        ("Define tumor mutational burden.", "definition"),
        ("What percentage of LUAD patients harbored SETD2 mutations?", "lookup"),
        ("How many samples were in the MSK-CHORD cohort?", "lookup"),
    ],
)
def test_heuristic_classification(query: str, expected: str) -> None:
    category, cues = classify_heuristic(query)
    assert category == expected
    assert cues, "expected at least one matched cue"


def test_heuristic_defaults_to_lookup_when_no_cue() -> None:
    category, cues = classify_heuristic("SETD2 lung adenocarcinoma frequency")
    assert category == "lookup"
    assert cues == []


def test_synthesis_cue_beats_definition_cue() -> None:
    # "what is" (definition) + "relationship between"/"across" (synthesis):
    # the stronger intent cue must win.
    category, _ = classify_heuristic(
        "What is the relationship between EGFR and ALK across these studies?"
    )
    assert category == "synthesis"


# ---------------------------------------------------------------------------
# route() with the heuristic strategy (no network)
# ---------------------------------------------------------------------------


def test_route_heuristic_lookup_to_hybrid() -> None:
    d = router.route("How many samples were in the cohort?", strategy="heuristic")
    assert isinstance(d, RouteDecision)
    assert d.category == "lookup"
    assert d.mode == "hybrid"
    assert d.method == "heuristic"
    assert "hybrid" in d.rationale


def test_route_heuristic_list_to_agentic() -> None:
    d = router.route("List every study that used whole-genome sequencing.", strategy="heuristic")
    assert d.category == "list"
    assert d.mode == "agentic"


def test_route_to_dict_is_json_friendly() -> None:
    import json

    d = router.route("Compare survival across subtypes.", strategy="heuristic")
    blob = json.dumps(d.to_dict())  # must not raise
    assert "mode" in blob and "rationale" in blob


def test_route_knn_falls_back_to_heuristic_offline(monkeypatch) -> None:
    """With kNN requested but embeddings broken, route() must degrade to the
    heuristic rather than raising."""
    def _boom(*a, **k):
        raise RuntimeError("no GCP_PROJECT")

    # Break the embedding path the QuestionBank uses.
    import cbio_kb.index.papers as papers_mod

    monkeypatch.setattr(papers_mod, "embed_texts", _boom)
    # Ensure no cached bank shortcuts the failure.
    monkeypatch.setattr(router.QuestionBank, "_instance", None, raising=False)

    d = router.route("List all datasets in the corpus.", strategy="knn")
    assert d.mode == "agentic"
    assert d.method == "heuristic"
    assert "unavailable" in d.rationale
