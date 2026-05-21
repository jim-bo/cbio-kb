---
name: Random survival forest
slug: random-survival-forest
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, survival-analysis, computational, liquid-biopsy]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Random survival forest

## Overview

Random survival forest (RSF) is an ensemble machine-learning method that extends the random forest algorithm to right-censored time-to-event data. It can capture non-linear relationships and interactions between features without requiring proportional hazards assumptions [PMID:39147831](../papers/39147831.md).

## Used by

- [PMID:39147831](../papers/39147831.md) — a random survival forest (LB+ model) incorporating liquid biopsy variables (ctDNA detection, cfDNA concentration, specific gene alterations) plus cancer type and chemotherapy receipt was trained on 4,141 patients and validated prospectively on 1,426 patients; achieved c-indices of 0.74 (discovery), 0.73 (validation), and 0.67 (generalizability for [NSCLC](../cancer_types/NSCLC.md) ctDx Lung cohort), substantially outperforming Khorana score (0.57, 0.61, 0.54) and RAM (0.62) for cancer-associated VTE prediction [PMID:39147831](../papers/39147831.md).
- [PMID:39506116](../papers/39506116.md) — RSF (n_trees=1,000, min_splits=10, min_samples_per_leaf=15) was the primary [OS](../cancer_types/OS.md) prediction model in the MSK-CHORD clinicogenomic dataset (24,950 patients); multi-modal RSF combining NLP-derived features (tumor sites, prior treatment), genomics, structured data, and imaging outperformed any single-modality model in all five cancer types; c-indices ranged from 0.58 (stage IV [PAAD](../cancer_types/PAAD.md)) to 0.83 (stage I–III [BRCA](../cancer_types/BRCA.md)); NLP-derived tumor-site features were the single most prognostic modality in stage-IV patients [PMID:39506116](../papers/39506116.md).
- Conditional random-forest (cforest) variable-importance modeling of overall survival in de novo [AML](../cancer_types/AML.md) patients (n=298); nominated age, mutated [TP53](../genes/TP53.md), and WGCNA module 3 (hub gene [PEAR1](../genes/PEAR1.md)) as the strongest predictors; module 3 was the dominant determinant in young (<45 y) and TP53-wild-type middle-age (45–60 y) patients [PMID:35868306](../papers/35868306.md)

## Notes

- RSF outperformed traditional clinical risk scores for VTE prediction by capturing interactions between ctDNA variables and clinical features [PMID:39147831](../papers/39147831.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:39147831](../papers/39147831.md)
- [PMID:39506116](../papers/39506116.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35868306](../papers/35868306.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
