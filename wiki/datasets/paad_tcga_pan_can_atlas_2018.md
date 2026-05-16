---
name: Pancreatic Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: paad_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 185
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - paad
  - pancreatic
  - adenocarcinoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Pancreatic Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Pancreatic Adenocarcinoma PanCancer Atlas 2018 cohort is the [PAAD](../cancer_types/PAAD.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `paad_tcga_pan_can_atlas_2018`. It covers approximately 185 pancreatic adenocarcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [PAAD](../cancer_types/PAAD.md) is notable for the highest [KRAS](../genes/KRAS.md) hotspot rate (72%) of any cancer type in the pan-cancer cohort, and for the context-dependent co-occurrence of [TP53](../genes/TP53.md) and [KRAS](../genes/KRAS.md) mutations (mutually exclusive in COAD/LUAD but significantly co-occurring in PAAD). All four clinical endpoints are recommended without reservation for PAAD by TCGA-CDR.

## Composition

- Cancer type: Pancreatic Adenocarcinoma ([PAAD](../cancer_types/PAAD.md)), OncoTree code PAAD.
- Approximately 185 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- PAAD has the highest [KRAS](../genes/KRAS.md) hotspot rate (72%) of any cancer type in the pan-cancer cohort; RTK-RAS pathway altered in 78% of PAAD; [ERBB2](../genes/ERBB2.md) + MEK co-targeting opportunity in 7% of PAAD. [PMID:29625049](../papers/29625049.md)
- [TP53](../genes/TP53.md) and [KRAS](../genes/KRAS.md) are mutually exclusive in COAD/READ and [LUAD](../cancer_types/LUAD.md) but **significantly co-occur in PAAD** — a key context-dependent driver interaction demonstrating that pan-cancer mutual-exclusivity does not hold tissue-by-tissue. [PMID:29625049](../papers/29625049.md)
- PAAD included in pan-cancer integrative molecular analysis (33 cancer types); pan-GI clustering includes PAAD in co-occurrence networks with STAD/COAD. [PMID:29625048](../papers/29625048.md)
- Stage-specific Cox HRs not significantly different by any endpoint in TCGA-CDR (alongside [MESO](../cancer_types/MESO.md) and [UVM](../cancer_types/UVM.md)); however, all four endpoints are recommended without reservation — note that the non-significant stage HR reflects disease-specific clinical behavior. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `paad_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
