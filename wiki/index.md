---
title: "cbio-kb"
subtitle: "A living knowledge base of cBioPortal publications"
toc: false
---

**cbio-kb** is a structured, cross-linked reading of the primary literature
behind [cBioPortal](https://www.cbioportal.org/) studies. It follows the
[LLM knowledge base pattern described by Andrej Karpathy](https://x.com/karpathy/status/2039805659525644595)
([idea file gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)):
raw source documents are incrementally compiled by an LLM into a directory of
interlinked Markdown pages, with the LLM maintaining summaries, backlinks,
and indexes as the corpus grows.

Every paper in the corpus is distilled into a standardized page — cohort, methods, key findings,
clinical implications, open questions — and every gene, cancer type, dataset,
drug, and assay mentioned gets its own page that aggregates what the corpus
collectively says about it.

The goal is to make it fast to answer questions like:

- *What has been published about* **[FGFR3](genes/FGFR3.md)** *in* **[urothelial carcinoma](cancer_types/BLCA.md)** *?*
- *Which studies profiled the* **[MSK-IMPACT](datasets/msk_impact_2017.md)** *cohort, and what did they find?*
- *Where has* **[erdafitinib](drugs/erdafitinib.md)** *resistance been characterized?*
- *What methods have been used to detect clonal hematopoiesis in solid-tumor sequencing?*

Every claim on an entity page is traceable back to a specific paper via
`PMID:` citations, and every paper page links out to the entities it touches.
Nothing is invented — unverified terms are flagged rather than canonicalized.

## Browse

| Section | Count | What you'll find |
|---|---|---|
| [Papers](papers/index.qmd) | 20 | Per-publication summaries: cohort, methods, findings, citations |
| [Genes](genes/index.qmd) | 131 | Alterations, co-occurrence, therapeutic relevance across the corpus |
| [Cancer types](cancer_types/index.qmd) | 43 | OncoTree-anchored disease pages linking studies and alterations |
| [Datasets](datasets/index.qmd) | 23 | cBioPortal studies with cohort details and linked publications |
| [Drugs](drugs/index.qmd) | 37 | Targeted therapies, resistance patterns, evidence in the corpus |
| [Methods](methods/index.qmd) | 33 | Sequencing assays, gene panels, and analytical pipelines |
| [Themes](themes/index.qmd) | — | Cross-cutting syntheses (in progress) |

## How to read a page

- **Paper pages** follow a fixed template — start with *TL;DR*, then *Cohort &
  data*, *Key findings*, *Clinical implications*, and *Limitations & open
  questions*. Every section cites back to the source PMID.
- **Entity pages** (genes, cancer types, drugs, etc.) aggregate everything the
  corpus says about that entity, with every claim tied to the paper it came
  from. If an entity has only one citing paper, the page will be short — that
  is expected.
- **Unverified flags.** When an entity couldn't be validated against OncoTree,
  HUGO, or cBioPortal's study/panel catalogs, its page carries an
  `unverified: true` flag. Treat those pages as provisional.

## About this site

This site is built from a Markdown vault that lives in a git repository. The
content is maintained by a small set of sub-agents (paper compiler, entity
writer, crosslinker, linter) that read raw paper text and write into the
wiki. The rendering, search, and navigation you see here are from
[Quarto](https://quarto.org/). For the full pipeline and engineering details,
see the [project repository](https://github.com/jim-bo/cbio-kb).
