# Pipeline token budget — single-paper baseline

**PMID:** 20601955 — *Subtype-specific genomic alterations define new targets for soft tissue sarcoma therapy* (Barretina et al., Nat Genet 2010)
**Raw `char_count`:** 40,378
**Date:** 2026-05-04
**Branch:** `bench-tokens-single-paper-2026-05-04`

Entities returned by the compiler: **13 genes**, **8 cancer types**, **1 dataset** (`sarc_mskcc`), **3 drugs**, **4 methods**. Sent in the *unsharded* configuration (genes-shard count = 13 — already under the 25-gene threshold where `CLAUDE.md` recommends bucketing, so no sharding decision was forced).

## Per-stage usage

| # | Stage                          | Agent                | Tier (declared) | Tokens   | Tool uses | Wall (s) |
|--:|--------------------------------|----------------------|-----------------|---------:|----------:|---------:|
| 1 | Compile paper                  | paper-compiler       | opus            |   53,832 |        16 |    798.8 |
| 2a | Genes (13)                     | entity-page-writer   | sonnet          |   55,264 |        90 |    655.1 |
| 2b | Cancer types (8)               | entity-page-writer   | sonnet          |   39,283 |        47 |    658.2 |
| 2c | Datasets (1)                   | entity-page-writer   | sonnet          |   19,096 |         8 |     53.7 |
| 2d | Drugs (3)                      | entity-page-writer   | sonnet          |   24,757 |        25 |    110.7 |
| 2e | Methods (4)                    | entity-page-writer   | sonnet          |   34,532 |        30 |    134.7 |
| 3 | Crosslink (paper + 30 touched) | crosslinker          | haiku           |   31,636 |        15 |     85.5 |
| 4 | build-index + build-graph + lint | (deterministic CLI)| —               |        0 |         — |     2.0 |
|   | **Total — sub-agent tokens**   |                      |                 | **258,400** |   **231** |          |
|   | Wall (sequential sum)          |                      |                 |          |           |  2,498.7 |
|   | Wall (effective, with stage-2 parallel fan-out) |     |                 |          |           |  ≈1,544  |

Wall calc: stage 1 (799 s) + max of stage 2 fan-out (658 s) + stage 3 (85 s) + stage 4 (2 s) ≈ 1,544 s.

## Token share by stage

| Stage                   | Tokens   | Share |
|-------------------------|---------:|------:|
| paper-compiler          |   53,832 |  20.8% |
| entity-page-writer (Σ)  |  172,932 |  66.9% |
| crosslinker             |   31,636 |  12.2% |

Within entity-page-writer the five fan-outs split roughly 32% genes / 23% c.types / 20% methods / 14% drugs / 11% datasets — i.e. cost tracks entity count, not entity kind, *except* that the cancer-types fan-out spent unusually high tokens-per-page (3 new pages with extensive prose).

## Tokens per entity touched (efficiency lens)

| Stage                 | Entities | Tokens / entity |
|-----------------------|---------:|----------------:|
| genes                 |       13 |        4,251 |
| cancer types          |        8 |        4,910 |
| datasets              |        1 |       19,096 |
| drugs                 |        3 |        8,252 |
| methods               |        4 |        8,633 |
| **entity-writer avg** |       29 |        5,963 |
| crosslinker (touched) |       30 |        1,055 |

Datasets has a single entity but pulls a full template + ontology lookup per dispatch — so the per-entity cost is misleading; the **fixed prompt overhead** is significant (≈19k for 1 dataset entity vs. ≈55k for 13 genes ⇒ marginal cost ≈ 3k/gene).

## Known gaps

- **Orchestrator (main-loop) tokens are not captured** — the `<usage>` block only reports per-sub-agent usage. Roughly: my own conversation processing this paper has cost on the order of tens of thousands of tokens additionally, but it is not directly observable.
- **`total_tokens` lumps input+output**; per-direction breakdown is not exposed by the Agent tool, so we cannot distinguish prompt-padding from generation cost.
- **Cache hits not visible** — sub-agents that re-read the same templates / ontology JSONs may benefit from prompt caching, but we cannot tell from this telemetry.

---

## Reflection — token-efficiency levers

Numbers below are grounded in this baseline plus the prior 5-paper batch (PR #15) where genes-shard was 174k tokens / 372 tool_uses for ~76 genes.

### 1. Gene-shard size — non-issue at the single-paper scale, real at batch scale
Single-paper: 13 genes ⇒ 55k tokens, marginal cost ~3k/gene after a ~16k fixed prompt overhead. Five-paper batch: 76 genes ⇒ 174k. Linear extrapolation says the unsharded fan-out is roughly *additive* in gene count, not super-linear, so the optimization play here is **parallel wall-time, not tokens**: shard genes A–F / G–M / N–T / U–Z to cut wall time ~4×, tokens roughly equal (4 × ~16k overhead added). Recommendation: shard on `genes_count > 25` *only when wall time matters*; do not shard for token economy alone.

### 2. Read+Edit-per-page overhead in entity-page-writer — biggest concrete win
Genes fan-out: 90 tool_uses for 13 genes ⇒ ~7 tool calls per gene (Read + Edit + ontology lookup + verification). For the 11 *existing* genes the work is largely deterministic: **append a bullet, append a `Sources` row, bump `processed_at`**. A new CLI command — e.g. `uv run cbio-kb wiki append-citation --kind gene --id TP53 --pmid 20601955 --bullet "..."` — could short-circuit ~80% of the merge cases. Estimated savings: drop the genes-fan-out from ~55k to ~15k (only the 2 new pages and any prose-update cases need the LLM). **Expected single-paper win: ≈40k tokens (~15% of total).**

### 3. Crosslinker over-reach
Crosslinker reported "1,019 links added across 403 pages" for a single new paper that touches 30 entity pages. That suggests it walked far beyond the explicit "paper page + touched pages" scope. Even at haiku's pricing this is wasteful relative to scope. Recommendation: pass the crosslinker an **explicit allow-list** of file paths (the 31 it should touch) rather than letting it discover globally. Estimated savings on this run: small (haiku is cheap), but at batch scale the multiplier is bigger.

### 4. Paper-compiler raw-md size — not the bottleneck for moderate papers
40k char input ⇒ 53k tokens out, with 16 tool calls. Matches expectations. The earlier 5-paper batch showed paper-compiler scaling roughly linearly with `char_count` (see PMID 39185963 at 123k chars → 60k tokens). For papers >100k chars, *outline-then-fill* (use `wiki outline` over the raw-md only the first time, then targeted Reads) would help — but it is not yet a problem at typical sizes.

### 5. Model tier audit
The `<usage>` block does not report which model actually answered. Tiers are declared in the agent frontmatter (`opus` / `sonnet` / `haiku`) but unverified at runtime. Recommendation: add a one-line model echo to each agent's system prompt ("I am running on `${MODEL}`") and capture that in the response so we can confirm. Without this, a silent tier upgrade (e.g. opus on something marked sonnet) would not be visible in token counts alone.

### 6. Parallelism vs. token cost — make the trade-off explicit
The five entity-page-writer fan-outs run in parallel and finish in `max(t)` ≈ 658 s instead of `Σt` ≈ 1,612 s — a ~2.4× wall-time speedup at zero token cost. This is the right default. **But**: if the user pivots to "minimize tokens, latency irrelevant," merging genes+cancer_types+datasets+drugs+methods into a single dispatch could remove ~4× the per-fan-out fixed prompt overhead (estimated ~40-60k of the ~173k entity-writer total). Worth a follow-up benchmark.

### Priority ranking (best ROI first)

1. **Append-citation CLI for entity-page-writer simple-merge case** (lever #2). One-time engineering cost; ~15-25% pipeline savings on every future paper.
2. **Scoped crosslinker** (lever #3). Trivial change (pass file allow-list); compounds at batch scale.
3. **Single-dispatch entity-page-writer when fan-out is small** (lever #6 sub-case). Cheap to try; gates on whether single-prompt routing actually amortizes the overhead.
4. **Runtime model-tier echo** (lever #5). Defensive — small effort, prevents silent regressions.
5. **Outline-first paper-compiler for >100k char papers** (lever #4). Defer until we ingest more giant papers.

## Verification (pipeline-correctness checklist)

- [x] `wiki/papers/20601955.md` written with frontmatter (paper-compiler verified `study_id: sarc_mskcc`).
- [x] All 30 touched entity pages exist; 13 created (YEATS4, ERBB4, DDLS, MRLS, PLLS, sarc_mskcc, nutlin-3a, affymetrix-250k-snp-array, shrna-rnai-screen, sequenom-genotyping) + 17 updated.
- [x] `uv run cbio-kb wiki build-index` regenerated `wiki/index.md` (deterministic).
- [x] `uv run cbio-kb wiki build-graph` → 782 nodes / 781 tree edges / 7889 cross edges.
- [x] `uv run cbio-kb lint`: 0 warnings, 0 stubs, 18 pre-existing unverified terms (radiomics datasets) — no new structural errors.
- [ ] `quarto render` from `wiki/` not re-run on this branch (was clean on the prior branch).
