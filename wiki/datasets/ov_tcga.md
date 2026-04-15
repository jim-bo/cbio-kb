---
name: TCGA Ovarian Serous Cystadenocarcinoma (OV)
studyId: ov_tcga
institution: The Cancer Genome Atlas (TCGA) Research Network
size: 606
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - copy-number-alteration
panels: []
tags:
  - hgsoc
  - ovarian-cancer
  - tcga
  - genomics
  - public-dataset
processed_by: crosslinker
processed_at: 2026-04-16
---

# TCGA Ovarian Serous Cystadenocarcinoma (OV)

## Overview

The TCGA ovarian serous cystadenocarcinoma study — canonical cBioPortal studyId `ov_tcga` — is the landmark multi-platform genomic characterization of high-grade serous ovarian cancer ([HGSOC](../cancer_types/HGSOC.md)) conducted by The Cancer Genome Atlas Research Network. SNV and CNA calls are publicly available via cBioPortal and from Synapse (syn11801889 for mutational signature data). Reference genome: hg19. [PMID:35764743](../papers/35764743.md)

## Composition

- Cancer type: [HGSOC](../cancer_types/HGSOC.md), predominantly stage III/IV.
- 148 TCGA-OV patients contributed to the Boehm et al. 2022 multimodal HGSOC cohort (296 MSKCC + 148 TCGA-OV, total N=444). [PMID:35764743](../papers/35764743.md)
- TCGA-OV cases used for CNA and SNV calls downloaded from cBioPortal, plus SBS3 frequencies from Synapse (syn11801889). HRD/HRP classification applied to TCGA cases using these calls. [PMID:35764743](../papers/35764743.md)

## Assays / panels (linked)

- Whole-exome sequencing, RNA-seq, copy-number alteration profiling (multi-platform).

## Papers using this cohort

- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*: 148 TCGA-OV patients (stage III/IV HGSOC) integrated with 296 MSKCC cases in a multimodal late-fusion prognostic model combining CT radiomics, H&E histopathology, and genomics.

## Notable findings derived from this cohort

- CNA and SNV calls from TCGA-OV cBioPortal + SBS3 frequencies from Synapse were used to assign HRD/HRP/ambiguous status; combined with MSKCC [MSK-IMPACT](../methods/msk-impact-panel.md) HRD calls, training split was 119 HRD / 218 HRP / 67 ambiguous. [PMID:35764743](../papers/35764743.md)
- Availability of only CT imaging (not H&E WSIs or clinical sequencing) for all TCGA-OV cases constrained the full multimodal integrator; adding clinical features including RD-status and PARP-inhibitor annotation was not possible for TCGA-OV cases. [PMID:35764743](../papers/35764743.md)

## Sources

- cBioPortal study: https://www.cbioportal.org/study/summary?id=ov_tcga
- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*.

*This page was processed by **crosslinker** on **2026-04-16**.*
