---
name: degarelix
targets: [GNRHR]
drug_class: GnRH receptor antagonist (androgen deprivation therapy)
canonical_source: corpus
unverified: true
tags: [hormone-therapy, prostate-cancer, androgen-deprivation]
processed_by: crosslinker
processed_at: 2026-04-30
---

# degarelix

## Overview

Degarelix is a GnRH (gonadotropin-releasing hormone) receptor antagonist that rapidly suppresses LH, FSH, and testosterone without an initial testosterone surge. It is FDA-approved for androgen deprivation therapy (ADT) in advanced prostate cancer, offering faster testosterone suppression than GnRH agonists. In the MSK-CHORD dataset it appears as a recorded systemic therapy for prostate cancer patients.

## Evidence in the corpus

- Degarelix is listed as a tracked systemic therapy drug in the MSK-CHORD ([msk_chord_2024](../datasets/msk_chord_2024.md)) dataset covering 3,211 [PRAD](../cancer_types/PRAD.md) patients. NLP-based annotation of prior treatment history (using transformer models) identified patients who had received degarelix, enabling post-treatment alteration enrichment analyses including [AR](../genes/AR.md) and [TP53](../genes/TP53.md) enrichment after prior systemic therapy in prostate cancer. [PMID:39506116](../papers/39506116.md)

## Resistance mechanisms

- [AR](../genes/AR.md) and [TP53](../genes/TP53.md) alterations are enriched in [PRAD](../cancer_types/PRAD.md) patients after prior systemic therapy (NLP-annotated), consistent with known escape mechanisms from androgen deprivation including GnRH-receptor antagonists such as degarelix. [PMID:39506116](../papers/39506116.md)

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) — prostate cancer; androgen deprivation therapy documented in MSK-CHORD cohort.

## Sources

- [PMID:39506116](../papers/39506116.md) — Al Shihabi et al. (Nature 2024). MSK-CHORD clinicogenomic dataset; degarelix recorded as androgen deprivation therapy for prostate cancer patients.

*This page was processed by **crosslinker** on **2026-04-30**.*
