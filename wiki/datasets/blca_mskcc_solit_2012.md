---
name: MSKCC High-Grade Bladder Cancer 2012 (Solit)
studyId: blca_mskcc_solit_2012
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 97
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - array-cgh-agilent-1m
  - sequenom-genotyping
  - sanger-sequencing
  - illumina-microarray
panels: []
tags:
  - bladder-cancer
  - high-grade-urothelial-carcinoma
  - actionable-alterations
  - copy-number-alterations
  - pi3k-akt-mtor-pathway
processed_by: entity-page-writer
processed_at: "2026-05-09"
---

# MSKCC High-Grade Bladder Cancer 2012 (Solit)

## Overview

Multi-platform integrated genomic study of 97 high-grade urothelial carcinomas of the bladder assembled at Memorial Sloan Kettering Cancer Center, published in 2013 by Iyer, Solit and colleagues. The dataset underpins the cBioPortal study `blca_mskcc_solit_2012` and was built to catalogue potentially actionable genomic alterations across the RTK–RAS–RAF, PI3K/AKT/mTOR, and G1–S cell-cycle pathways. 61% of tumors harbored at least one such alteration.

## Composition

- **Cancer type:** [BLCA](../cancer_types/BLCA.md) — high-grade urothelial carcinoma of the bladder.
- **Samples:** 97 tumors (94 cystectomy, 1 nephroureterectomy, 2 TURBT); macro-dissected to ≥60% tumor content.
- **Demographics:** median age 73 (range 42–89); 72 male / 25 female.
- **Stage (95 evaluable):** pTa/pTis 4, I 11, II 15, III 33, IV 32; 34 (35%) received neoadjuvant chemotherapy.
- **Histology:** 57 (59%) TCC NOS; 30 (31%) TCC with minor variant components; 10 (10%) predominantly neuroendocrine.
- **Comparator:** 285 consecutively treated MSKCC patients (cystectomy 2007–2010) with comparable median overall survival (38 vs 35.2 months; P=.19).
- Reference genome: NCBI build 36.1 (hg18). [PMID:23897969](../papers/23897969.md)

## Assays / panels (linked)

- [array-cgh-agilent-1m](../methods/array-cgh-agilent-1m.md) — Agilent 1M human oligonucleotide aCGH; co-hybridized with reference normal DNA; segmented by circular binary segmentation; analyzed with the RAE algorithm at FDR <1%.
- [sequenom-genotyping](../methods/sequenom-genotyping.md) — mass-spectrometry iPLEX hotspot genotyping panel covering recurrent oncogene/tumor-suppressor hotspots.
- [sanger-sequencing](../methods/sanger-sequencing.md) — all coding exons of 15 selected oncogenes/tumor suppressors.
- [illumina-microarray](../methods/illumina-microarray.md) — Illumina HumanHT-12 expression BeadChip, quantile-normalized.

## Papers using this cohort

- [PMID:23897969](../papers/23897969.md) — Iyer G et al., "Prevalence and Co-Occurrence of Actionable Genomic Alterations in High-Grade Bladder Cancer", *J Clin Oncol* 2013.

## Notable findings derived from this cohort

- 61% (59/97) of high-grade bladder tumors harbored at least one potentially actionable alteration — defined as a validated drug target in another tumor type or a target with an inhibitor in clinical investigation. [PMID:23897969](../papers/23897969.md)
- Unsupervised hierarchical clustering of aCGH data identified two subsets (high-CNA-burden vs low-CNA-burden); high-burden bladder tumors ranked second only to serous ovarian in structural-aberration load across 14 reference tumor types (n=5,135). [PMID:23897969](../papers/23897969.md)
- [TP53](../genes/TP53.md) mutations (34%) and [RB1](../genes/RB1.md) alterations (15%) were significantly enriched in high-CNA-burden tumors (P<.001 and P<.003). [PMID:23897969](../papers/23897969.md)
- [ERBB2](../genes/ERBB2.md) was focally amplified in 6.2% (6/97) with concordant mRNA up-regulation and 3+ HER2 IHC; [E2F3](../genes/E2F3.md) amplified in 21% (vs 4.9% across 1,932 non-urothelial epithelial tumors). [PMID:23897969](../papers/23897969.md)
- RTK–RAS–RAF pathway altered in 35% of samples; PI3K/AKT/mTOR pathway in 30% — with [TSC1](../genes/TSC1.md)-null tumors resistant to [MK-2206](../drugs/mk-2206.md) despite AKT inhibition. [PMID:23897969](../papers/23897969.md)

## Sources

- cBioPortal study: `blca_mskcc_solit_2012`
- [PMID:23897969](../papers/23897969.md) — primary publication

*This page was processed by **entity-page-writer** on **2026-05-09**.*
