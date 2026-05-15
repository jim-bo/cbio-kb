"""Lightweight cBioPortal client for auto-generated claim tests.

Mirrors the production helpers in `scripts/verify_paper.py` on purpose —
keeping them separate lets `pytest tests/claims/` run independently of
the verifier code path. Default `pytest` ignores `tests/claims/`; opt
in explicitly:

    uv run pytest tests/claims/                                 # all claims
    uv run pytest tests/claims/test_26901067.py -v              # one paper
    uv run pytest tests/claims/test_26901067.py::test_blca_plasmacytoid_mskcc_2016__cdh1_truncating__mutation_rate -v
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from functools import lru_cache
from pathlib import Path

CBIO = "https://www.cbioportal.org/api"
REPO_ROOT = Path(__file__).resolve().parents[2]
GENES_JSON = REPO_ROOT / "schema" / "ontology" / "genes.json"

TRUNCATING = frozenset({
    "Nonsense_Mutation", "Frame_Shift_Del", "Frame_Shift_Ins",
    "Splice_Site", "Nonstop_Mutation", "Translation_Start_Site",
})
MISSENSE = frozenset({"Missense_Mutation"})
INFRAME = frozenset({"In_Frame_Del", "In_Frame_Ins"})

_MOD_TO_SET = {
    "truncating": TRUNCATING,
    "missense": MISSENSE,
    "inframe": INFRAME,
    "any": None,
}


def _get(path: str):
    req = urllib.request.Request(f"{CBIO}{path}",
                                  headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def _post(path: str, body: dict):
    req = urllib.request.Request(
        f"{CBIO}{path}",
        data=json.dumps(body).encode(),
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


@lru_cache(maxsize=1)
def _hugo_to_entrez() -> dict[str, int]:
    return {r["hugoGeneSymbol"]: r["entrezGeneId"]
            for r in json.loads(GENES_JSON.read_text())}


def sample_count(study_id: str) -> int:
    """`sequencedSampleCount` from `/studies/{id}`."""
    return _get(f"/studies/{urllib.parse.quote(study_id)}").get("sequencedSampleCount") or 0


def mutation_rate(study_id: str, hugo: str,
                   modifier: str = "any") -> tuple[float, int, int]:
    """Return (rate, n_samples_with_mutation, denominator).

    `modifier` ∈ {"truncating", "missense", "inframe", "any"}.
    Rate is `unique_samples_with_mutation / sequencedSampleCount`.
    """
    entrez = _hugo_to_entrez()[hugo]
    denom = sample_count(study_id)
    muts = _post(
        f"/molecular-profiles/{urllib.parse.quote(study_id)}_mutations/mutations/fetch"
        f"?projection=DETAILED",
        {"entrezGeneIds": [entrez], "sampleListId": f"{study_id}_all"},
    ) or []
    classes = _MOD_TO_SET.get(modifier)
    if classes is not None:
        muts = [m for m in muts if m.get("mutationType") in classes]
    samples = {m.get("sampleId") for m in muts}
    rate = (len(samples) / denom) if denom else 0.0
    return rate, len(samples), denom
