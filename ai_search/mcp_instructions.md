# cbio-kb: cBioPortal literature knowledge base

This server answers questions from the **publications behind cBioPortal studies**:
a curated, cross-linked wiki compiled from each paper's full text, plus passage
search over the papers themselves. It complements the other cBioPortal MCP
servers rather than replacing them:

| Need | Use |
|---|---|
| Counts, mutation frequencies, clinical data, SQL | `cbioportal-mcp` (`clickhouse_run_select_query`, `list_studies`, `get_study_guide`) |
| A cBioPortal page/URL for a view or cohort | `cbioportal-navigator` |
| What a study's paper found, how a cohort was built, what the literature says about a gene/drug/cancer type | **this server** |

Never report a frequency or count from a paper as if it were the current database
value; the paper describes the cohort at publication time.

## Shared identifiers

- **Study IDs** are cBioPortal `studyId` / `cancer_study_identifier` values
  (e.g. `msk_chord_2024`). Any study ID from `cbioportal-mcp` or the navigator
  can be passed to `get_study_papers`, and every `study_ids` value returned here
  can be passed back to them.
- **Genes** are HUGO symbols; **cancer types** are OncoTree codes (same codes as
  `search_oncotree` on `cbioportal-mcp`).
- **Papers** are PubMed IDs (PMIDs).

## Recipes

- **"What did the paper behind study X find?"** → `get_study_papers(study_id)`, then
  `get_paper(pmid)` for the detail you need.
- **Factual question about findings** → `search_auto(query)` (routes to the cheapest
  strategy that works for the question), or `search_hybrid` directly; then
  `get_paper` on the cited PMIDs to confirm context.
- **Cross-paper question about a gene / drug / cancer type / method** →
  `get_entity(kind, id)`, which lists the papers citing it; open the relevant ones
  with `get_paper`.
- **Find papers by metadata** → `list_papers(search=…, gene=…, cancer_type=…, study_id=…)`.
- **Freshness / coverage** → `corpus_info()`.

## Rules

- Cite every claim with its PMID (e.g. `PMID:39506116`, https://pubmed.ncbi.nlm.nih.gov/39506116/).
- A paper marked `retracted: true` has been retracted by its journal; don't use it as
  evidence, and say so if it comes up.
- `study_ids` on a paper means *this paper is the publication for that cBioPortal
  study*. `datasets_used` means the paper analyzed that cohort; it may not be the
  cohort's own publication.
- A study with no corpus paper usually means its publication is not open access;
  say so rather than implying the study has no publication.
- Prefer section reads (`get_paper(pmid, sections=[…])`) over whole pages.
