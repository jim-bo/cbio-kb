# Eval refresh: full-corpus, fair 3-way (agentic / rag / hybrid)

**Status:** planned, not started. Authored 2026-06-06 after discovering a corpus-size
confound in the existing eval. This doc is the handoff — it is self-contained so a fresh
session can execute it without re-investigating.

---

## TL;DR

The RAG-vs-agentic eval silently became unfair as the wiki grew. **rag** and **hybrid**
retrieve from a frozen FAISS/BM25 index pinned to **56 papers** (`data/paper_index`,
matching `eval/corpus_pmids.txt`), while **agentic** walks the live `wiki/papers/` vault,
which is now **377 papers**. So the 3-way numbers measure corpus size as much as retrieval
strategy. Fix: rebuild the rag/hybrid index over all 377 papers so all three modes share
the same corpus, expand the question set onto the newly-covered themes, regenerate
`list`-question gold against 377, then re-run val+test and refresh the summaries.

---

## What we found (the confound, with evidence)

| mode | corpus actually searched |
|---|---|
| rag | `data/paper_index` — **56 distinct PMIDs**, exact match to `eval/corpus_pmids.txt` |
| hybrid | same 56-PMID index (`RAG_INDEX_DIR` → `data/paper_index`) |
| agentic | walks `wiki/papers/*.md` — **377 papers** (6.7×) |

- Both `data/raw/papers/` and `wiki/papers/` now hold **all 377** PMIDs; their
  intersection is 377, so a fair full-corpus eval is feasible (raw markdowns exist for
  every paper the agent can see).
- Concrete proof of leakage: on val question **S10**, agentic cited `34667026`,
  `34819518`, `35871175` — all **out of the 56-corpus**, i.e. papers rag/hybrid cannot
  retrieve.
- Effect on the (confounded) numbers: agentic's low citation_correctness (2.60) and recall
  (0.550) are partly artifact — gold is defined within the 56-corpus, so agentic's
  out-of-corpus citations score as wrong. Its synthesis completeness/accuracy edge is
  inflated by having ~7× more source material. **The rag-vs-hybrid half is fair** (identical
  56-PMID index); only the agentic column is compromised.

### Today's result dirs — CONFOUNDED, do not cite as findings
- `eval/results/2026-06-06-133624/` — hybrid only, val (56-corpus)
- `eval/results/2026-06-06-135213/` — agentic only, synthesis S10–S12 (377 vs 56 leak)
- `eval/results/2026-06-06-140201/` — matched val, all 3 modes (**confounded**; keep as the
  artifact that demonstrates the asymmetry, not as a result)

The pre-existing April dirs (`eval/results/2026-04-*`) are agentic+rag on a *different,
disjoint* val question set (IDs S13–S15 etc.) — not comparable to current questions either.

---

## Environment (already set up on this VM; re-confirm in fresh context)

- **Deps:** the eval needs the `chat` extra (fastapi/uvicorn/faiss/sentence-transformers/
  torch). Install with `uv sync --extra chat`. (torch comes from the CPU-only index added in
  the ambient `pyproject.toml` WIP — leave that diff unstaged per repo convention.)
- **GCP auth:** rag/hybrid/agentic all embed queries via Vertex `gemini-embedding-001`,
  which needs Application Default Credentials. **ADC is configured** on this VM
  (`gcloud auth application-default login`, quota project `cbioportal-python`). If it's gone,
  redo it; the interactive code-paste step EOFs through the `!` channel — drive it via a FIFO
  or run in a real terminal.
- **`.env`** holds `ANTHROPIC_API_KEY` and `GCP_PROJECT=cbioportal-python` (loaded by the app).
- **Backend:** `uv run python -m uvicorn ai_search.app:app --host 0.0.0.0 --port 8080`
  (NOT `uvicorn …` directly — the console script isn't on PATH; use `python -m`). The runner
  posts to `http://localhost:8080/api/chat`.

---

## The refresh plan (execution order)

### 1. Define the full shared corpus
Write the 377-PMID list and archive the old 56:
```bash
# preserve the v1 56-paper corpus for provenance
cp eval/corpus_pmids.txt eval/corpus_pmids_v1_56.txt
# emit the full corpus = papers present as raw markdown (== wiki coverage, 377)
ls data/raw/papers/*.md | grep -oE '[0-9]+' | sort -u > eval/corpus_pmids.txt
wc -l eval/corpus_pmids.txt   # expect 377
```
Update the header comment + `corpus:` field in `eval/questions/v1.yaml` (says "56 corpus
PMIDs"). Decide (see open questions) whether to bump to `v2.yaml`.

### 2. Rebuild the rag/hybrid index over 377 papers
```bash
uv run cbio-kb index build-papers \
    --papers-dir data/raw/papers \
    --pmid-list  eval/corpus_pmids.txt \
    --index-dir  data/paper_index
uv run cbio-kb index build-bm25 --index-dir data/paper_index
```
- This embeds every chunk via Vertex (rate-limited, retries on 429) — expect minutes and
  real embedding cost for 377 papers. Verify afterwards:
  `python3 -c "import json;print(len({json.loads(l)['pmid'] for l in open('data/paper_index/meta.jsonl')}))"`
  → should print 377.
- `data/index_dir/` (1 PMID) is a stray test index — ignore; the real one is
  `data/paper_index`.
- The **deployed Cloud Run** backend has its own index; rebuilding locally does not touch
  it. Out of scope for the eval; redeploy separately if prod should match.

### 3. Regenerate `list`-question gold against 377  ← highest-risk, mostly manual
`list` gold (LS01–LS10) is the *comprehensive* expected set and drives retrieval recall.
Computed against 56, it is now wrong/incomplete (e.g. LS01 "MSK-IMPACT papers" lists 30 of
56; among 377 there are many more). For each list question, re-enumerate the matching papers
over the full corpus. Useful tooling:
```bash
uv run cbio-kb wiki backlinks --file <entity>     # papers citing an entity page
uv run cbio-kb wiki search-context --query <term> --limit 50
```
Cross-check entity backlinks + a manual read; the entity is in each question's
`gold_entities`. `lookup`/`definition` gold (1–3 specific papers) is usually stable but
spot-check. `synthesis` gold may gain new supporting papers — review.

### 4. Expand the question set (keep the existing themes)
Current set: 50 Q, 4 categories (`lookup`/`list`/`synthesis`/`definition`), split 30/10/10.
Themes already present: MSK-IMPACT panels, CT radiomics (Aerts/MAASTRO), ctDNA/cfDNA,
PD-1/PD-L1 blockade + biomarkers, sarcomas (RMS/angiosarcoma), DNA-damage-response, KRAS,
BRAF, prostate, HNSC, IDH-glioma/GLASS, clonal hematopoiesis. Add questions covering the 321
newly-eligible papers **within these same themes and the 4 categories** — do not invent new
question *types*. Keep each question grounded in ≥1 corpus PMID with curated `gold_pmids` +
`gold_entities`. Target size + split allocation: see open questions.

### 5. Re-run the eval (all three modes, now fair)
```bash
# backend must be running on :8080
uv run python -m eval.run --split val  --mode all   # 3 modes × val
uv run python -m eval.run --split test --mode all   # report numbers — run once
```
`--mode all` = agentic+rag+hybrid. Writes `eval/results/{ts}/runs.jsonl` + `report.md`.

### 6. Build the wiki-embedded report
`build_report.py` is already mode-agnostic (derives modes from records, so hybrid flows
through automatically):
```bash
uv run python -m eval.build_report --run-dir eval/results/{train_ts} \
    --val-dir eval/results/{val_ts} --test-dir eval/results/{test_ts}
uv run python -m eval.build_explorer_data --run-dir eval/results/{train_ts}
```
Check `_compute_stats()` in `build_report.py` for `{stat:…}` names — they were defined for a
2-mode (agentic/rag) narrative; hybrid stats may need new names if narrative.md references them.

### 7. Refresh the summaries
- `eval/README.md` — currently 2-mode, says "56 PMIDs". Update to 3 modes (add `hybrid.py`
  runner to Layout + a Hybrid bullet + `--mode all` in Running) and the new corpus size.
- `eval/narrative.md` — academic abstract for `wiki/experiments/rag-vs-agentic.qmd`. Its
  abstract claims "the agent wins on every dimension" (2-mode, test split). Rewrite the
  headline/takeaways for the fair 3-way **after** the test run produces real numbers; do not
  hand-edit numbers. Section ids are referenced by `build_report.py` — don't rename without
  updating the lookup.
- `schema/templates/index.md` News — optional dated bullet if this lands in the wiki.

### 8. Commit
Scope commits per concern. Leave ambient `pyproject.toml`/`uv.lock` (torch CPU index)
unstaged. Note: pushing to `main` triggers test + Pages + Cloud Run deploy.

---

## Resolved decisions (locked 2026-06-06 with user)

1. **Corpus scope:** ✅ **All 377.** Rebuild rag/hybrid index over the full corpus.
2. **Question set:** ✅ **Expand `v1.yaml` in place → ~80 questions.** Keep the 4 categories
   and existing themes; add questions on the 321 newly-eligible papers. Proposed target:
   lookup 25 / synthesis 25 / list 15 / definition 15 (= 80), split ~60/20/20
   (train 48 / val 16 / test 16). v1's `corpus:` field + header comment get updated in place
   (no v2.yaml).
3. **List-gold regeneration:** ✅ **Semi-automated, user-reviewed.** Enumerate candidate PMIDs
   per `gold_entity` via `wiki backlinks` / `search-context`, propose updated `gold_pmids`,
   user approves before they land. Applies to both the existing LS01–LS10 and any new list Qs.
4. **Today's confounded result dirs:** ✅ **Archive, do not delete.** Move the four
   `2026-06-06-*` dirs under `eval/results/_confounded_2026-06-06/` (or tag in a README) and
   keep as the artifact demonstrating the asymmetry.
5. **narrative.md:** ✅ **Rewrite for the fair 3-way** (agentic / rag / hybrid) **after** the
   test numbers land. Don't hand-edit numbers; preserve section ids referenced by
   `build_report.py`.

## Key file map
- `eval/run.py` — orchestrator (`--split`, `--mode {agentic,rag,hybrid,both,all}`, `--ids`)
- `eval/runners/{base,agentic,rag,hybrid}.py` — base hits `/api/chat` SSE; one thunk per mode
- `eval/judge.py` — opus rubric judge (accuracy/completeness/citation_correctness)
- `eval/build_report.py` / `build_explorer_data.py` — wiki artifacts (mode-agnostic)
- `eval/questions/v1.yaml` — questions + gold + splits
- `eval/corpus_pmids.txt` — shared corpus list (consumed by `cbio-kb index build-papers`)
- `ai_search/{rag,hybrid}.py` — `_INDEX_DIR` → `data/paper_index` (env `RAG_INDEX_DIR`)
- `src/cbio_kb/index/papers.py` — `build-papers` (Vertex embed); `bm25.py` — BM25 sidecar
