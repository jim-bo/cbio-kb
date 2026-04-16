---
name: MSK SPECTRUM Tumor Microenvironment Study (2022)
studyId: msk_spectrum_tme_2022
institution: Memorial Sloan Kettering Cancer Center
size: 36
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - copy-number-alteration
panels:
  - IMPACT468
tags:
  - hgsoc
  - ovarian-cancer
  - msk-spectrum
  - tumor-microenvironment
  - genomics
  - public-dataset
processed_by: crosslinker
processed_at: 2026-04-16
---

# MSK SPECTRUM Tumor Microenvironment Study (2022)

## Overview

The MSK-SPECTRUM project (canonical cBioPortal studyId `msk_spectrum_tme_2022`) is a prospective cohort study at Memorial Sloan Kettering Cancer Center characterizing the tumor microenvironment in high-grade serous ovarian cancer ([HGSOC](../cancer_types/HGSOC.md)). Genomic profiling performed with [MSK-IMPACT](../methods/msk-impact-panel.md) targeted hybrid-capture sequencing. Reference genome: hg19. [PMID:35764743](../papers/35764743.md)

## Composition

- Cancer type: [HGSOC](../cancer_types/HGSOC.md), predominantly stage III/IV.
- 36 prospective MSK-SPECTRUM patients contributed to the Boehm et al. 2022 multimodal cohort (as part of 296 total MSKCC cases). [PMID:35764743](../papers/35764743.md)
- MSK-IMPACT clinical sequencing used to infer HRD status via HRD-DDR gene variants (including [BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md)) and CCNE1 CNA, plus COSMIC SBS3 detection via [SigMA](../methods/sigma-mutational-signatures.md). [PMID:35764743](../papers/35764743.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted hybrid-capture sequencing (HRD-DDR gene variants, CCNE1 CNA).

## Papers using this cohort

- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*: 36 MSK-SPECTRUM patients (prospective arm) included as part of the 296-patient MSKCC cohort in the multimodal HGSOC late-fusion prognostic model.

## Notable findings derived from this cohort

- HRD status inferred from MSK-IMPACT sequencing plus SigMA COSMIC SBS3 detection; 130 MSKCC cases had research consent for HRD calling (high-confidence SBS3 n=48, low-confidence n=30). [PMID:35764743](../papers/35764743.md)
- The full MSK-SPECTRUM + MSKCC cohort contributed CT imaging (adnexal and omental), H&E WSIs, and genomic data; the multimodal late-fusion model leveraged partial-data cases to avoid restricting training to the 114 patients with complete four-modality data. [PMID:35764743](../papers/35764743.md)

## Sources

- cBioPortal study: https://www.cbioportal.org/study/summary?id=msk_spectrum_tme_2022
- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*.

*This page was processed by **crosslinker** on **2026-04-16**.*
