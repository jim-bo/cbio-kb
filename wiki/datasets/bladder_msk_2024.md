---
name: Bladder Cancer (MSK, Eur Urol 2024)
studyId: bladder_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 112
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - rna-seq
panels: []
tags:
  - upper-tract-urothelial-carcinoma
  - immune-checkpoint-blockade
  - molecular-subtyping
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Bladder Cancer (MSK, Eur Urol 2024)

## Overview

An MSK institutional cohort of upper-tract urothelial carcinoma (UTUC) patients: a 100-patient discovery cohort (MSK100) who underwent nephroureterectomy with no metastatic disease at presurgical imaging, plus a 31-patient immune-checkpoint-blockade (ICB) cohort with metastatic disease. Tissue collected under NCT01775072 and MSKCC IRB #89-076/#06-107. cBioPortal study record: 112 samples, hg19. [PMID:39550333](../papers/39550333.md)

## Composition

- Cancer type: [UTUC](../cancer_types/UTUC.md). [PMID:39550333](../papers/39550333.md)
- **Discovery cohort (MSK100):** 100 tumors from 100 patients; 99 had enough tissue for MSK-IMPACT tumor–normal sequencing (hybridization capture, up to 505 genes); median follow-up after nephroureterectomy 60 months (IQR 32.3–86.3). [PMID:39550333](../papers/39550333.md)
- **ICB cohort:** 31 patients treated with ICB for metastatic UTUC — 18 from MSK100 who recurred, plus a 13-patient MSKCC expansion cohort with RNA-seq. [PMID:39550333](../papers/39550333.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) tumor–normal hybridization capture (up to 505 genes); variants annotated oncogenic/likely oncogenic with [OncoKB](../methods/oncokb.md); TMB per covered Mb; MSI via [MSIsensor](../methods/msisensor.md). [PMID:39550333](../papers/39550333.md)
- Whole-transcriptome [RNA-seq](../methods/rna-seq.md) of frozen tissue, with MIBC consensus subtyping. [PMID:39550333](../papers/39550333.md)

## Papers using this cohort

- [PMID:39550333](../papers/39550333.md) — source publication for this cohort (MSK100 + ICB expansion, UTUC molecular subtyping vs TCGA MIBC comparator).

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: bladder_msk_2024 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **entity-page-writer** on **2026-09-10**.*
