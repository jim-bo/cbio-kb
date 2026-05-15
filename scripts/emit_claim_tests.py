"""Emit pytest test files from claim manifests.

For each `wiki/papers/{pmid}.claims.json`, writes
`tests/claims/test_{pmid}.py` — one pytest function per claim. The
emitted tests are runnable independently via
`pytest tests/claims/test_{pmid}.py::{test_name} -v` and produce
human-readable failure messages with the API value, the claim value,
and the delta.

Idempotent — overwrites existing files. The test files themselves
are gitignored; the manifest (`*.claims.json`) is the source of truth.

Usage:
    uv run python scripts/emit_claim_tests.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_PAPERS = REPO_ROOT / "wiki" / "papers"
OUT_DIR = REPO_ROOT / "tests" / "claims"

_HEADER = '''"""Auto-generated from wiki/papers/{pmid}.claims.json — do not edit by hand.
Re-emit with: uv run python scripts/emit_claim_tests.py
"""
from tests.claims._cbio import sample_count, mutation_rate
'''


def _slug(s: str | None) -> str:
    if not s:
        return ""
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def _format_quote(quote: str | None, max_len: int = 100) -> str:
    if not quote:
        return ""
    q = quote.replace("\n", " ").strip()
    if len(q) > max_len:
        q = q[:max_len - 1].rstrip() + "…"
    return q


def _emit_sample_count(claim: dict) -> str:
    study = claim["study"]
    value = claim["value"]
    name = f"test_{_slug(study)}__sample_count"
    quote = _format_quote(claim.get("quote"))
    section = claim.get("section") or "?"
    return f'''

# Section: {section}
# Quote: "{quote}"
def {name}():
    """sample_count claim: {value} samples in {study}"""
    api = sample_count("{study}")
    claim = {value}
    delta = abs(api - claim)
    assert delta <= 5 or delta / max(1, api) <= 0.10, (
        f"sample_count: claim={{claim}}, API={{api}}, Δ={{delta}}"
    )
'''


def _emit_mutation_rate(claim: dict) -> str:
    study = claim["study"]
    gene = claim["gene"]
    modifier = (claim.get("modifier") or "any").lower()
    value = claim["value"]
    name = f"test_{_slug(study)}__{_slug(gene)}_{_slug(modifier)}__mutation_rate"
    quote = _format_quote(claim.get("quote"))
    section = claim.get("section") or "?"
    return f'''

# Section: {section}
# Quote: "{quote}"
def {name}():
    """mutation_rate claim: {value:.0%} {gene} {modifier} in {study}"""
    rate, n, denom = mutation_rate("{study}", "{gene}", "{modifier}")
    claim = {value}
    delta_pp = abs(rate - claim)
    assert delta_pp <= 0.05, (
        f"mutation_rate {gene} {modifier}: "
        f"claim={{claim:.0%}}, API={{rate:.0%}} ({{n}}/{{denom}}), "
        f"Δ {{delta_pp*100:.1f}}pp"
    )
'''


_EMITTERS = {
    "sample_count": _emit_sample_count,
    "mutation_rate": _emit_mutation_rate,
}


def emit_file(pmid: str, claims: list[dict]) -> str:
    parts = [_HEADER.format(pmid=pmid)]
    n_emitted = 0
    n_skipped = 0
    for claim in claims:
        kind = claim.get("kind")
        emitter = _EMITTERS.get(kind)
        if emitter is None:
            parts.append(f"\n# SKIPPED: unsupported claim kind {kind!r}\n")
            n_skipped += 1
            continue
        parts.append(emitter(claim))
        n_emitted += 1
    body = "".join(parts)
    return body, n_emitted, n_skipped


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifests = sorted(WIKI_PAPERS.glob("*.claims.json"))
    if not manifests:
        print("no claim manifests found in wiki/papers/")
        return 0
    total_emitted = total_skipped = 0
    for manifest in manifests:
        pmid = manifest.stem.replace(".claims", "")
        claims = json.loads(manifest.read_text())
        body, n_emitted, n_skipped = emit_file(pmid, claims)
        out_path = OUT_DIR / f"test_{pmid}.py"
        out_path.write_text(body)
        total_emitted += n_emitted
        total_skipped += n_skipped
        print(f"  {out_path.relative_to(REPO_ROOT)}  ({n_emitted} test(s)"
              f"{f', {n_skipped} skipped' if n_skipped else ''})")
    print(f"\nwrote {len(manifests)} file(s); {total_emitted} test(s) total"
          f"{f', {total_skipped} skipped' if total_skipped else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
