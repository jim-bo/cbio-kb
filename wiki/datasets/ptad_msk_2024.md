---
name: Pituitary Neuroendocrine Tumors (MSK, 2024)
slug: ptad_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 92
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [targeted-panel, whole-exome-seq]
panels: []
tags:
  - pituitary
  - neuroendocrine
  - PitNET
  - LOH
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# Pituitary Neuroendocrine Tumors (MSK, 2024)

## Overview

Two-arm MSK cohort designed to characterize the genomic landscape of treatment-refractory and benign pituitary neuroendocrine tumors (PitNETs). A retrospective arm (n = 26) enriched for aggressive/treatment-refractory tumors (85% treatment-refractory, 38% metastatic) was profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) and whole-exome sequencing. A prospective arm (n = 66) captured unselected patients presenting for pituitary surgery. Data deposited in cBioPortal as `ptad_msk_2024` and dbGaP (phs001783). [PMID:38758238](../papers/38758238.md)

## Composition

- Retrospective cohort: 26 patients with aggressive/treatment-refractory or higher-risk PitNETs (22/26 treatment-refractory; 10/26 metastatic).
- Prospective cohort: 66 unselected patients undergoing pituitary surgery at MSKCC.
- Analytic groups after stratification by radiotherapy response: 23 treatment-refractory vs. 69 benign PitNETs.
- Cancer type: pituitary adenoma / PitNET ([PTAD](../cancer_types/PTAD.md)).
- All tumors sequenced via [MSK-IMPACT](../methods/msk-impact-panel.md); retrospective cohort also underwent whole-exome sequencing for [USP8](../genes/USP8.md) mutation detection. [PMID:38758238](../papers/38758238.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — primary somatic mutation and copy-number profiling.
- [Whole-exome sequencing](../methods/whole-exome-seq.md) — retrospective arm only, for [USP8](../genes/USP8.md) mutations not covered by IMPACT.
- [FACETS](../methods/facets.md) v0.5.6 — allele-specific copy-number and LOH inference.
- [FISH](../methods/fish.md) — five patients to validate chromosomal losses.

## Papers using this cohort

- [PMID:38758238](../papers/38758238.md) — Genome-wide loss of heterozygosity predicts aggressive, treatment-refractory behavior in pituitary neuroendocrine tumors.

## Notable findings derived from this cohort

- Treatment-refractory PitNETs had significantly higher TMB (p = 1.3 × 10^-10) and fraction of LOH (p = 8.5 × 10^-9) compared to benign tumors. [PMID:38758238](../papers/38758238.md)
- [TP53](../genes/TP53.md) mutations were the most common alteration in treatment-refractory tumors (12/23 vs. 1/69 benign; p = 4.2 × 10^-8); 11/12 were clonal. [PMID:38758238](../papers/38758238.md)
- A recurrent chromosomal LOH (rcLOH) pattern involving chromosomes 1, 2, 3, 4, 6, 10, 11, 15, 17, 18, 21, and 22 was identified in 11/14 treatment-refractory corticotroph PitNETs vs. 1/14 benign (p = 1.7 × 10^-4). [PMID:38758238](../papers/38758238.md)
- A binary LOH threshold of 0.11 achieved AUC = 0.87, accuracy = 0.88 (sensitivity 0.83, specificity 0.90) for predicting treatment-refractory behavior. [PMID:38758238](../papers/38758238.md)
- Five treatment-refractory corticotroph tumors harbored mismatch repair mutations ([MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [MLH1](../genes/MLH1.md)); 3/4 pre-treatment tumors were MSI-high. [PMID:38758238](../papers/38758238.md)
- [ATRX](../genes/ATRX.md), [DAXX](../genes/DAXX.md), [TERT](../genes/TERT.md), and [TSC2](../genes/TSC2.md) mutations were unique to treatment-refractory corticotroph tumors. [PMID:38758238](../papers/38758238.md)

## Sources

- cBioPortal study `ptad_msk_2024`. [PMID:38758238](../papers/38758238.md)
- dbGaP accession phs001783.

*This page was processed by **entity-page-writer** on **2026-04-11**.*
