---
name: Pheochromocytoma and Paraganglioma (TCGA, PanCancer Atlas 2018)
studyId: pcpg_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 179
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - pcpg
  - pheochromocytoma
  - paraganglioma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Pheochromocytoma and Paraganglioma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Pheochromocytoma and Paraganglioma PanCancer Atlas 2018 cohort is the [PCPG](../cancer_types/PCPG.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `pcpg_tcga_pan_can_atlas_2018`. It covers approximately 179 pheochromocytoma and paraganglioma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [PCPG](../cancer_types/PCPG.md) is notable for the near-absence of usable clinical endpoints: per TCGA-CDR, **no endpoint** can be recommended for PCPG due to insufficient event rates and follow-up, making it the only cancer type in the 33-tumor pan-cancer cohort with this restriction.

## Composition

- Cancer type: Pheochromocytoma and Paraganglioma ([PCPG](../cancer_types/PCPG.md)), OncoTree code PHEO.
- Approximately 179 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)

## Notable findings derived from this cohort

- PCPG included in pan-cancer integrative molecular analysis (33 cancer types, 11,286 tumors); enriched for [GNAQ](../genes/GNAQ.md)/[GNA11](../genes/GNA11.md) mutual exclusivity (these dominate uveal melanoma) and for Ras-pathway exclusivity maintained across cancer types. [PMID:29625048](../papers/29625048.md)
- TCGA-CDR endpoint assessment: **no endpoint** ([OS](../cancer_types/OS.md), PFI, DFI, or DSS) is recommended for PCPG — the only cancer type among 33 with this restriction, due to too few events and insufficient follow-up in this predominantly indolent disease. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `pcpg_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
