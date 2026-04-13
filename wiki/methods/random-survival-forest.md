---
name: Random survival forest
slug: random-survival-forest
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, survival-analysis, computational, liquid-biopsy]
processed_by: crosslinker
processed_at: 2026-04-11
---

# Random survival forest

## Overview

Random survival forest (RSF) is an ensemble machine-learning method that extends the random forest algorithm to right-censored time-to-event data. It can capture non-linear relationships and interactions between features without requiring proportional hazards assumptions [PMID:39147831](../papers/39147831.md).

## Used by

- [PMID:39147831](../papers/39147831.md) — a random survival forest (LB+ model) incorporating liquid biopsy variables (ctDNA detection, cfDNA concentration, specific gene alterations) plus cancer type and chemotherapy receipt was trained on 4,141 patients and validated prospectively on 1,426 patients; achieved c-indices of 0.74 (discovery), 0.73 (validation), and 0.67 (generalizability for [NSCLC](../cancer_types/NSCLC.md) ctDx Lung cohort), substantially outperforming Khorana score (0.57, 0.61, 0.54) and RAM (0.62) for cancer-associated VTE prediction [PMID:39147831](../papers/39147831.md).

## Notes

- RSF outperformed traditional clinical risk scores for VTE prediction by capturing interactions between ctDNA variables and clinical features [PMID:39147831](../papers/39147831.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:39147831](../papers/39147831.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
