---
name: radLongformer
slug: radlongformer
kind: method
canonical_source: corpus
unverified: true
tags: [nlp, transformer, radiology, prognostic, deep-learning]
processed_by: crosslinker
processed_at: 2026-04-30
---

# radLongformer

## Overview

radLongformer is a Clinical-Longformer transformer variant fine-tuned directly on raw radiology free-text (CT chest/abdomen/pelvis reports) to predict 6-month mortality. It is an end-to-end approach that bypasses structured feature extraction, taking raw radiology note text as input and outputting a prognostic score for overall survival.

## Used by

- [PMID:39506116](../papers/39506116.md) — radLongformer was trained end-to-end on 705,241 CT-CAP radiology reports in the MSK-CHORD clinicogenomic dataset (24,950 patients) and was prognostic for [OS](../cancer_types/OS.md) in all five cancer types ([NSCLC](../cancer_types/NSCLC.md), [BRCA](../cancer_types/BRCA.md), [COADREAD](../cancer_types/COADREAD.md), [PRAD](../cancer_types/PRAD.md), [PAAD](../cancer_types/PAAD.md)). However, adding radLongformer scores to the [random survival forest](../methods/random-survival-forest.md) did not improve overall prognostic power beyond interpretable NLP-derived features — "black-box" radiology text did not add beyond engineered features; it was superior to tumor-site features alone only in stage-IV CRC [PMID:39506116](../papers/39506116.md).

## Notes

- Derived from the Clinical-Longformer architecture; the "rad" prefix indicates fine-tuning on radiology (CT-CAP) reports specifically for 6-month mortality prediction.
- The finding that radLongformer did not improve RSF models suggests that explicitly engineered NLP features (tumor sites, prior treatment) capture most of the prognostic signal already present in radiology free text.
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:39506116](../papers/39506116.md)

*This page was processed by **crosslinker** on **2026-04-30**.*
