---
name: Rectal Cancer Clinical Cohort (MSK, 2019)
studyId: rectal_msk_2019
institution: Memorial Sloan Kettering Cancer Center
size: 287
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
panels:
  - msk-impact-panel
tags:
  - rectal-cancer
  - colorectal-cancer
  - msk-impact
  - organoid
  - mutation-landscape
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Rectal Cancer Clinical Cohort (MSK, 2019)

## Overview

A clinical cohort of 287 rectal cancers ([READ](../cancer_types/READ.md)) resected at Memorial Hospital, Memorial Sloan Kettering Cancer Center, and sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md). The cohort serves as a comparator reference for the mutation landscape of rectal adenocarcinoma and was specifically used to validate the genomic fidelity of a patient-derived organoid (tumoroid) biorepository established from the same institution [PMID:31591597](../papers/31591597.md).

## Composition

- **287 resected rectal adenocarcinomas** from Memorial Hospital patients profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) [PMID:31591597](../papers/31591597.md).
- **Cancer type:** [Rectal adenocarcinoma (READ)](../cancer_types/READ.md), a subtype of [colorectal cancer (COADREAD)](../cancer_types/COADREAD.md) [PMID:31591597](../papers/31591597.md).
- **Treatment context:** Reflects tri-modal neoadjuvant chemoradiation + surgery + 5-FU-based adjuvant chemotherapy pathways standard at MSKCC [PMID:31591597](../papers/31591597.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) ([IMPACT468](../methods/IMPACT468.md)) — FDA-cleared targeted tumor profiling panel on resected specimens [PMID:31591597](../papers/31591597.md).

## Papers using this cohort

- [PMID:31591597](../papers/31591597.md) — Ganesh et al. Organoid-based rectal cancer tumoroid biorepository; the 287-patient MSK RC cohort is used as the reference mutation landscape to confirm that the top mutated genes in organoids ([APC](../genes/APC.md), [TP53](../genes/TP53.md), [KRAS](../genes/KRAS.md), [FBXW7](../genes/FBXW7.md)) match the clinical cohort.

## Notable findings derived from this cohort

- Top mutated genes in the 287-patient clinical cohort — [APC](../genes/APC.md), [TP53](../genes/TP53.md), [KRAS](../genes/KRAS.md), [FBXW7](../genes/FBXW7.md) — mirror those observed in matched patient-derived rectal tumoroids, confirming organoid genomic fidelity [PMID:31591597](../papers/31591597.md).
- The MSK-IMPACT rectal cohort mutation landscape is consistent with the 5–6% MMR-deficient rate in clinical rectal cancer, as reflected in the organoid biorepository where only 2/65 tumoroids were MMR-deficient [PMID:31591597](../papers/31591597.md).
- 62% RAS-mutant prevalence observed in the derived organoid panel, consistent with the landscape in the MSK rectal cohort, with [KRAS](../genes/KRAS.md)-mutant status confirming anti-[EGFR](../genes/EGFR.md) [cetuximab](../drugs/cetuximab.md) resistance ex vivo [PMID:31591597](../papers/31591597.md).

## Sources

- cBioPortal study: `rectal_msk_2019`
- Primary publication: [PMID:31591597](../papers/31591597.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
