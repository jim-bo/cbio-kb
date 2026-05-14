---
name: abiraterone
targets: [CYP17A1]
drug_class: androgen biosynthesis inhibitor (CYP17A1 inhibitor)
canonical_source: corpus
unverified: true
tags: [targeted-therapy, hormone-therapy, prostate-cancer]
processed_by: crosslinker
processed_at: 2026-05-14
---

# abiraterone

## Overview

Abiraterone acetate is a selective, irreversible inhibitor of CYP17A1 (17α-hydroxylase/C17,20-lyase), blocking androgen biosynthesis in the testes, adrenal glands, and tumor tissue. It is used in combination with [prednisone](../drugs/prednisone.md) for metastatic castration-resistant and castration-sensitive prostate cancer. In the MSK-CHORD dataset it appears as a recorded systemic therapy for prostate cancer patients.

## Evidence in the corpus

- Abiraterone is listed as a tracked systemic therapy drug in the MSK-CHORD ([msk_chord_2024](../datasets/msk_chord_2024.md)) dataset covering 3,211 [PRAD](../cancer_types/PRAD.md) patients. NLP-based annotation of prior treatment history (using transformer models) was used to identify patients who had received abiraterone, enabling post-treatment alteration enrichment analyses including [AR](../genes/AR.md) and [TP53](../genes/TP53.md) enrichment after prior systemic therapy in prostate cancer. [PMID:39506116](../papers/39506116.md)
- Abiraterone pre-treatment context: AR-V7 splice variant was detectable at low ratios in most pre-abiraterone/enzalutamide mCRPC cases; recurrent [AR](../genes/AR.md) hotspots (T878A, W742C, L702H) that confer agonism predict differential responses to ADT including abiraterone [PMID:26000489](../papers/26000489.md)

## Resistance mechanisms

- [AR](../genes/AR.md) and [TP53](../genes/TP53.md) alterations are enriched in [PRAD](../cancer_types/PRAD.md) patients with prior systemic therapy (annotated by NLP from clinical notes), consistent with the endocrine-resistance signature seen after androgen deprivation and androgen-receptor–targeted agents including abiraterone. [PMID:39506116](../papers/39506116.md)

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) — metastatic prostate cancer; documented systemic therapy in the MSK-CHORD cohort.

## Sources

- [PMID:39506116](../papers/39506116.md) — Al Shihabi et al. (Nature 2024). MSK-CHORD clinicogenomic dataset; abiraterone recorded as a systemic therapy agent for prostate cancer patients; NLP-extracted prior-treatment annotations enabled post-treatment genomic enrichment analysis.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26000489](../papers/26000489.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
