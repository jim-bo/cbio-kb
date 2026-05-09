---
name: ccRCC — UTokyo 2013 (manifest label)
studyId: ccrcc_utokyo_2013
institution: unknown (manifest mismatch — see note)
size:
reference_genome:
canonical_source: cbioportal
unverified: false
assays: []
panels: []
tags:
  - ccRCC
  - kidney
  - clear-cell
  - manifest-mismatch
processed_by: crosslinker
processed_at: 2026-05-09
---

# ccRCC — UTokyo 2013 (manifest label)

## Overview

**Manifest mismatch — read this note before using this page.**

The study ID `ccrcc_utokyo_2013` was assigned by the orchestrator manifest to PMID:23797736. However, the paper at PMID:23797736 is Lima et al. (2025, GEO GSE282887 / GSE253168), a mouse scRNA-seq study of conditional *Vhl*-knockout proximal tubular cells performed at a non-UTokyo institution. That paper uses TCGA-KIRC ([kirc_tcga](../datasets/kirc_tcga.md)) as a secondary human-validation dataset only; it does not generate a new clinical ccRCC cohort.

It is likely that `ccrcc_utokyo_2013` is a legitimate cBioPortal study unrelated to PMID:23797736 — the manifest may have mislabeled the PMID. This page should be revisited once the correct paper for `ccrcc_utokyo_2013` is identified.

## Composition

- Not determinable from PMID:23797736 (Lima et al. 2025 mouse model study).
- PMID:23797736 primary data: 147,045 single cells from *Pax8-CreERT2*-driven conditional *Vhl*-knockout mice (4 genotypes × 4 mice each); scRNA-seq deposited at GEO GSE282887.
- Human validation in PMID:23797736: secondary GSEA of TCGA ccRCC vs. normal kidney data (accessed April 2025) — linked to [kirc_tcga](../datasets/kirc_tcga.md), not this study ID.

## Assays / panels (linked)

Not determinable from the associated paper (see manifest mismatch note above).

## Papers using this cohort

- [PMID:23797736](../papers/23797736.md) — Lima et al. 2025, mouse scRNA-seq study of HIF1A/HIF2A isoform-specific roles in Vhl-null renal proximal tubule cells *(assigned to this study ID by orchestrator manifest; actual cohort linkage unresolved)*.

## Notable findings derived from this cohort

- PMID:23797736 used [kirc_tcga](../datasets/kirc_tcga.md) TCGA data (not `ccrcc_utokyo_2013`) to validate that HIF1A- and HIF2A-specific murine transcriptional programs are active in human ccRCC vs. normal kidney [PMID:23797736](../papers/23797736.md).
- HIF2A drives a late dedifferentiation/adaptive transcriptional program in Vhl-null renal proximal tubular cells that is conserved in human ccRCC by TCGA cross-validation [PMID:23797736](../papers/23797736.md).
- Findings support early therapeutic targeting of HIF2A with [belzutifan](../drugs/belzutifan.md) in [VHL](../genes/VHL.md) disease to prevent expansion of Vhl-null cancer-of-origin cells [PMID:23797736](../papers/23797736.md).

## Sources

- [PMID:23797736](../papers/23797736.md) *(assigned by manifest; cohort linkage uncertain)*

*This page was processed by **crosslinker** on **2026-05-09**.*
