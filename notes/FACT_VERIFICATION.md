# Idea: Cross-checking paper-compiler output against cBioPortal

Captured 2026-05-15 from a session that built the first ad-hoc verifier
(`scripts/verify_paper.py`). The script hits the public REST API for one
or more PMIDs, cross-checks the wiki page's frontmatter against
`/studies/{id}` + `/molecular-profiles/{id}/mutations/fetch`, and prints
a pass/warn/fail report. The smoke tests against 26901067 / 36577525 /
24735922 caught at least one real metadata error (STMYEC vs MYEC) and
correctly recovered the central CDH1 claim of the plasmacytoid paper (27
/ 34 = 79% truncating, paper says 84%) — so the approach works. This
note captures how to generalize it.

## Two problems, treat them separately

### 1. Metadata verification — "did we extract the right things?"

Four shapes, decreasing tractability:

- **Identity** (`study_id`, `pmid`, `doi`). `/studies/{id}` returns its
  own `pmid`. Match = paper-compiler picked the primary study. Mismatch
  = paper is *citing* the dataset, not authoring it. Today the schema
  conflates both in `study_id:` + `datasets:`. Consider splitting:
  `study_id:` = primary (its API pmid == paper pmid), `datasets:` =
  cited cohorts (API pmid != paper pmid, and that's OK). The current
  verifier flags this as a warn; once the schema is split it can be a
  hard pass/fail.

- **Linkage**. Does the declared `study_id`'s `cancerTypeId` match
  `cancer_types`? Does its panel reference match `methods`? Caught
  STMYEC vs MYEC. Generalizes trivially: dump checks to JSON per paper,
  aggregate → OncoTree drift heatmap across the corpus.

- **Recall** (what did we miss?). Mostly out of reach for the API. One
  cheap API-driven recall check: for each study, the API knows its
  panel; if the panel isn't in the paper's `methods` list, probable
  miss. Real recall needs the source text (`data/raw/papers/{pmid}.md`)
  + a second LLM pass or grep over `genes.json` symbols.

- **Precision** (did we hallucinate?). Needs source-text grounding,
  not API. For each `genes[]` entry: grep raw paper for the symbol; if
  it appears zero times, flag. Cheap, surprisingly effective. Same for
  `drugs[]`, `methods[]`.

### 2. Quantitative-claim verification — "is the 84% real?"

Bounded by what cBioPortal exposes per study.

**Reproducible from the API:**
- cohort size (`sequencedSampleCount`, `cnaSampleCount`)
- per-gene mutation frequency, overall and by mutationType class
- CNA frequency (`/cna/fetch`)
- structural variants
- mutation co-occurrence / mutual exclusivity (intersect sample sets)
- TMB if panel size is resolvable
- survival curves (where `OS_MONTHS` / `OS_STATUS` are uploaded as
  clinical attributes)

**Not reproducible:**
- IHC, CRISPR, cell-line experiments
- pre-deposit cohorts
- supplementary-only data
- p-values (would recompute, not look up)

The structural problem: claims live in prose, so the verifier can only
spot-check things shaped like "study × gene × mutated." To go further
the paper-compiler needs to emit a **claims manifest** — sibling file
`data/claims/{pmid}.json` shaped like:

```json
[
  {"study": "blca_plasmacytoid_mskcc_2016", "gene": "CDH1",
   "metric": "truncating_rate", "value": 0.84, "denom": 31,
   "quote": "84% of plasmacytoid carcinomas", "section": "TL;DR"},
  ...
]
```

Verification then becomes a deterministic walker: each claim maps to a
fixed API query, returns pass/warn/fail + evidence.

## Phase plan

### Phase A — Generalize the existing verifier (no compiler changes)

Roughly: take `scripts/verify_paper.py`, add structured output and batch
mode, run it across all 253 papers, produce an aggregate report.
Catches the bulk of metadata errors. Phase A breaks down further:

- **A1. Identity** — emit `eval/verify/{pmid}.json` per paper with the
  current study identity block (pmid match, cancerTypeId match, sample
  counts). Aggregator surfaces papers where API pmid disagrees with
  paper pmid → schema-split candidates.
- **A2. Linkage** — fold the existing methods cross-check + cancer-type
  cross-check into the JSON. Aggregator surfaces all OncoTree-code
  mismatches across the corpus (the STMYEC class of error).
- **A3. Precision via raw-text grep** — for each `genes[]` / `drugs[]`
  entry, grep `data/raw/papers/{pmid}.md` for the term; zero matches =
  warn. No API needed.
- **A4. Gene-cohort cross-check (existing)** — keep the
  truncating/missense breakdown behind `--gene-limit`. In batch mode,
  cap per study to keep wall-clock bounded.
- **A5. Aggregator** — single command that walks `eval/verify/*.json`
  and emits `eval/verify/REPORT.md` plus a `summary.json` with per-paper
  scores and corpus-wide rollups.

### Phase B — Claims manifest (compiler contract change)

Add an extraction step to paper-compiler (or a sibling agent) that
emits a sidecar `wiki/papers/{pmid}.claims.json` per the schema below.
Hard part isn't the LLM call — it's deciding what counts as a claim
and how to encode modifiers (mutationType class, sample subset,
comparison cohort).

**v1 status (2026-05-15): walker built, extractor still hand-rolled.**

The verifier-side walker is in `scripts/verify_paper.py`
(`check_claims`, `_check_sample_count_claim`, `_check_mutation_rate_claim`).
It reads `wiki/papers/{pmid}.claims.json` if present and emits
findings with `claim.*` codes via the same `Finding` pipeline that
Phase A uses, so the existing aggregator / REPORT.md flow works
unchanged. Two claim kinds supported in v1:

- `sample_count`: claim integer compared to `sequencedSampleCount`.
  Tolerance: `|Δ| ≤ 5` absolute OR `≤ 10%` relative.
- `mutation_rate`: claim fraction compared to
  `unique_samples_with_mutation / sequencedSampleCount`,
  optionally filtered by mutationType class
  (`truncating` / `missense` / `inframe` / `any`).
  Tolerance: `± 5 percentage points`.

Hand-extracted claim files exist for two papers as test data:
- `wiki/papers/26901067.claims.json` — CDH1 plasmacytoid
- `wiki/papers/36577525.claims.json` — myoepithelial soft tissue

What they surface:
- 26901067 sample_count (31 vs API 34): pass — within absolute
  tolerance.
- 26901067 CDH1 truncating (84% vs API 71%): warn — real
  subset-vs-full-cohort issue (paper denominates against 31
  plasmacytoid; API knows 34 total).
- 26901067 TP53 any (59% vs API 59%): pass within 0.2pp.
- 36577525 sample_count (12 vs API 12): pass — exact.

The 84% / 71% discrepancy is a useful surfaced signal — it shows
the walker cannot tell when a paper's denominator is a subset of
the cBioPortal study. Fixing it requires the claim schema to
encode subsets (e.g. `samples_with_panel: IMPACT341`) and the
walker to construct a sample list from clinical attributes. Defer
until a real LLM extractor is in place.

**Update 2026-05-15: extraction agent is live.**

`.claude/agents/claims-extractor.md` (and matching `.gemini/agents/`)
is a sonnet-level agent that reads a compiled paper page, validates
declared studies/genes against the frontmatter, and writes the
sidecar JSON. It correctly returns `[]` for review papers (tested on
PMID 24735922) and produces verifying claims for primary-cohort
papers (tested on PMID 28481359 — all 3 claims pass at exact rates:
sample_count 10945, TP53 41%, KRAS 15%). Skipped-claim list returned
to the orchestrator surfaces per-cancer-type subsets and aggregate
event counts that v1 schema doesn't support — useful signal for v2
schema design. Step 6 of the "Adding one paper" workflow in AGENTS.md
now dispatches it. Pytest emit is step 12 (optional).

**Update 2026-05-16: worked example — tier-mixed denominators.**

Wave 1 of the batch extraction (10 PMIDs, primary-cohort papers) ran
the agent against papers 18948947 / 20579941 / 20601955 / 21252315 /
21720365 / 21796119 / 21798893 / 21798897 / 21909114 / 22158988. The
agent emitted 28 claims (10 `sample_count` + 18 `mutation_rate`). When
those went through the verifier walker, 17 claims passed and 11
warned. **Every single warn was the same shape.**

Canonical case: PMID 21252315, Jiao et al. *Science* 2011 —
"DAXX/ATRX, MEN1 and mTOR Pathway Genes are Frequently Altered in
Pancreatic Neuroendocrine Tumors".

The paper's `## Cohort & data` section says:

> "68 sporadic, non-familial PanNETs (Discovery set n=10, Validation
> set n=58) … whole-exome-seq (Discovery set, Illumina GAIIx) and
> sanger-sequencing (Validation set, targeted genes)."

`## Key findings` reports headline rates over the combined tier:
"MEN1 mutated in 44.1% (30/68)", "DAXX 25% (17/68)", "ATRX 17.6%
(12/68)", "PTEN 7.3% (5/68)", "TSC2 8.8% (6/68)", "PIK3CA 1.4%
(1/68)".

cBioPortal `panet_jhu_2011` deposits **only the WES discovery tier**.
`GET /studies/panet_jhu_2011` returns `sequencedSampleCount: 10`,
description "Whole exome sequencing of 10 pancreatic neuroendocrine
tumor patients". `GET /sample-lists/panet_jhu_2011_sequenced` lists
exactly 10 sample IDs (`PanNET3PT`, `PanNET7PT`, …, `PanNET93PT`).

Mutation fetch over those 10 samples returns:

| Gene   | Paper (n=68) | API (n=10)  | Δ        |
|--------|--------------|-------------|----------|
| MEN1   | 44.1% (30/68)| 50% (5/10)  | +5.9 pp  |
| DAXX   | 25%   (17/68)| 30% (3/10)  | +5.0 pp  |
| ATRX   | 17.6% (12/68)| 10% (1/10)  | −7.6 pp  |
| PTEN   | 7.3%  (5/68) | 20% (2/10)  | +12.7 pp |
| TSC2   | 8.8%  (6/68) | 20% (2/10)  | +11.2 pp |
| PIK3CA | 1.4%  (1/68) | 10% (1/10)  | +8.6 pp  |

Nothing here is wrong. The paper is correct. cBioPortal is correct.
The extractor pulled the verbatim quote and its stated denominator.
The verifier walker is correctly flagging that the paper's headline
denominator (68) does not match the API's `sequencedSampleCount`
(10). The gap is structural: the paper aggregates a two-tier cohort,
the deposit holds one tier.

**Mitigation for v1: the agent now acknowledges this in the prompt.**
The `claims-extractor` agent definition was updated (this same date)
with a new "Multi-tier cohorts" section that:

- Recognises the signal (Cohort & data names ≥2 tiers, headline rate
  uses combined N).
- Emits the `sample_count` claim with the combined N anyway (that is
  what the paper says — the warn downstream is informative).
- Skips `mutation_rate` claims whose denominator is the combined N,
  with `reason: "tier_mixed_denominator"` in the returned skipped
  list. Does NOT recompute a tier-only rate from the API — that is
  the verifier walker's job, not the extractor's.

After this prompt change, the panet case is expected to surface as:
1 sample_count claim (still warn — combined N exceeds deposited N),
0 mutation_rate claims, and 6 entries in the skipped list (one per
combined-tier gene rate). The warn count drops from 6 to 1 without
losing signal about the cohort mismatch.

**Update 2026-05-16: batch paused at 24 / 227 sidecars.**

Ran the batch extractor for two iterations of 5 PMIDs each via
`/loop 30min` (cron `7,37 * * * *`, session-only). Stopped at 24
total primary-cohort sidecars (4 hand-rolled + 10 wave 1 + 10 from
the loop). Cancelled the cron — not blocked, just pausing.

Reason for the pause: **the Hard rule 7 / pre-emit checklist
addition to the `claims-extractor` agent prompt is not load-bearing.**
Tested three times on the canonical PMID 21252315 (`panet_jhu_2011`,
where the paper's headline rates use `n/68` for a deposit that only
holds 10 WES samples). All three runs ignored the rule and emitted
`denominator: 68` mutation_rate claims anyway, even with the
canonical PMID and the explicit "Correct extraction is 0 rate
claims" example called out in-line.

The agent's mandate (per its own opening prose) is "you are not
asserting the claim is true — you are extracting what the paper
says." Asking sonnet to *suppress* claims based on what cBioPortal
*might* deposit conflicts with that mandate. The agent visibly
resists; the resistance is partly principled.

**Two architectural options to resolve before resuming the batch:**

1. **Revert Hard rule 7 + pre-emit checklist** and accept that the
   extractor emits paper-faithful claims (denominator-as-stated).
   Move the tier-mixed/subset/superset detection to the verifier
   walker in `scripts/verify_paper.py` — downgrade
   `claim.mutation_rate` warns to `info` when the walker detects
   `paper_denom != sequencedSampleCount` and the paper page's
   `## Cohort & data` section names a multi-tier breakdown that
   sums to the paper denom. Cleaner separation of concerns.
   Architecturally consistent with the original FACT_VERIFICATION
   design philosophy.

2. **Add a single optional `denominator_basis` schema field**
   (`deposit | tier_mixed | subset | superset`). The agent
   *labels* the denominator basis (it's good at labeling, just not
   at suppressing). The walker reads the field and decides how to
   compare. Minimal schema change; the agent's contract is
   preserved (it still emits what the paper says, plus an
   annotation about denominator structure).

(1) is less work and architecturally cleaner. (2) is more
information-preserving. Either way the batch is resumable once the
contract is settled — the 24 existing sidecars are paper-faithful
extractions and don't need to be re-run unless schema (2) is
adopted.

**Open items for v2:**
- Additional claim kinds: `cna_rate` (amp/del), `co_occurrence`
  (two-gene intersect), `median_survival_months`, `tmb_median`.
- Subset/cohort encoding for cases like 26901067 (denominator is
  panel-subsetted) and 21252315 (denominator is tier-aggregated),
  with the walker constructing the sample list from clinical
  attributes before computing rates. The schema would need either
  a `denominator_in_api: false` flag (converts warns to info) or
  a `cohort: discovery_only | full` discriminator (walker picks the
  matching sample list, or downgrades to info if absent).
- Aggregator drilldown table for `claim.*` warns (today they
  appear in the by-code table but not in their own section).

## Tradeoffs

- **Phase A**: a few hundred lines, zero coordination cost, no
  paper-compiler changes. Catches entity-level errors at corpus scale.
- **Phase B**: most of a sprint. Forces nailing down the claim schema
  (which is harder than it sounds — one sentence often carries several
  overlapping claims). Pays off in true quantitative coverage.

Order: A first, see where failures cluster, let that shape B.

## File touch-points

- `scripts/verify_paper.py` — existing, will grow into the batch tool
- `eval/verify/{pmid}.json` — new, one per paper
- `eval/verify/REPORT.md`, `summary.json` — new, aggregate outputs
- `data/raw/papers/{pmid}.md` — read-only input for precision grep
- `schema/templates/paper.md` — eventual schema split (`study_id` vs
  `datasets`) belongs here, not in Phase A
- `data/claims/{pmid}.json` — Phase B only
