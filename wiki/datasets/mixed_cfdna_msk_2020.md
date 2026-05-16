---
name: MSK Pan-Cancer cfDNA Pilot Cohort (MSK, Genome Medicine 2021)
studyId: mixed_cfdna_msk_2020
institution: Memorial Sloan Kettering Cancer Center
size: 118
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - cf-impact
  - msk-access
  - whole-exome-seq
  - whole-genome-seq
panels:
  - IMPACT410
  - ACCESS129
tags:
  - liquid-biopsy
  - cfdna
  - pan-cancer
  - tumor-fraction
  - cfDNA-triage
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# MSK Pan-Cancer cfDNA Pilot Cohort (MSK, Genome Medicine 2021)

## Overview

Prospective/retrospective plasma cell-free DNA (cfDNA) profiling cohort of 118 patients with metastatic solid tumors enrolled at Memorial Sloan Kettering Cancer Center under IRB protocol NCT01775072. The study piloted a tumor fraction-guided multi-assay cfDNA strategy: each sample was first analyzed by cf-IMPACT (the plasma version of the 410-gene MSK-IMPACT panel), then triaged by shallow whole-genome sequencing (sWGS)-derived genome-wide z-score to either MSK-ACCESS (for low-tumor-fraction negatives) or whole-exome sequencing of cfDNA (for high-tumor-fraction negatives). Raw WGS/WES data were deposited in dbGaP (accession phs002290.v1.p1). [PMID:34059130](../papers/34059130.md)

## Composition

- 118 patients with metastatic solid tumors; tumor types: [BLCA](../cancer_types/BLCA.md), [PRAD](../cancer_types/PRAD.md), [BRCA](../cancer_types/BRCA.md), [TGCT](../cancer_types/TGCT.md), [MEL](../cancer_types/MEL.md), [NSCLC](../cancer_types/NSCLC.md).
- Matched tumor MSK-IMPACT data available for 76/118 patients; 42 had no available tumor data or failed tumor profiling.
- Reference genome: GRCh37. [PMID:34059130](../papers/34059130.md)

## Assays / panels (linked)

- [cf-IMPACT (IMPACT410)](../methods/IMPACT410.md) — plasma 410-gene panel, ~631× depth; detects mutations at 1% VAF (genotyping) or 2%/5% VAF (de novo hotspot/non-hotspot).
- [MSK-ACCESS (ACCESS129)](../methods/ACCESS129.md) — ultra-deep (>12,000×), UMI error-corrected, 129-gene panel, detection down to 0.1% VAF.
- [Whole exome sequencing](../methods/whole-exome-seq.md) of cfDNA (cf-WES), mean depth 384×, NimbleGen SeqCap Exome platform.
- [Shallow whole genome sequencing](../methods/whole-genome-seq.md) (sWGS, ~10M reads/sample) with [ichorCNA](../methods/ichorcna.md) for tumor-fraction estimation.
- [MSIsensor](../methods/msisensor.md) for MSI status; [FACETS](../methods/facets.md) for tumor clonality; [OncoKB](../methods/oncokb-annotation.md) for actionability annotation. [PMID:34059130](../papers/34059130.md)

## Papers using this cohort

- [PMID:34059130](../papers/34059130.md) — Tsui et al., *Genome Medicine* 2021: Tumor fraction-guided three-assay cfDNA strategy (cf-IMPACT + MSK-ACCESS + cf-WES) detected mutations in 90/118 (76%) patients vs 71/118 (60%) by cf-IMPACT alone; 25% (30/118) had OncoKB level 1–4 actionable variants. sWGS-based z-score outperformed fragment-size ratio for tumor-fraction prediction (AUC 0.925 vs 0.828). [PMID:34059130](../papers/34059130.md)

## Notable findings derived from this cohort

- cf-IMPACT alone detected somatic mutations in 71/118 (60%) patients; the three-assay strategy raised yield to 90/118 (76%). [PMID:34059130](../papers/34059130.md)
- MSK-ACCESS detected mutations in 14/29 (48%) cf-IMPACT-negative low-tumor-fraction samples; 7/19 (34%) of these were OncoKB-actionable. [PMID:34059130](../papers/34059130.md)
- cf-WES recovered mutations in all 5 high-tumor-fraction cf-IMPACT-negative samples; 99% of mutations fell outside the cf-IMPACT panel footprint. [PMID:34059130](../papers/34059130.md)
- MSI-High and high TMB identified from cf-IMPACT alone in an mCRPC patient with failed biopsies; later confirmed by bone biopsy, leading to [pembrolizumab](../drugs/pembrolizumab.md) response (PSA 118 → <10, sustained >1 year). [PMID:34059130](../papers/34059130.md)
- Tumor-plasma TMB concordance was 0.894 (p=1.7e−09) for high-tumor-fraction samples (z-score ≥5) vs 0.476 (p=0.0079) for low-tumor-fraction samples. [PMID:34059130](../papers/34059130.md)

## Sources

- cBioPortal study `mixed_cfdna_msk_2020`.
- dbGaP accession phs002290.v1.p1 (raw WGS/WES data).
- Tsui DWY, et al. *Tumor fraction-guided cell-free DNA profiling in metastatic solid tumor patients.* Genome Medicine. 2021. [PMID:34059130](../papers/34059130.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
