---
name: Clinical Longformer
slug: clinical-longformer
kind: method
canonical_source: corpus
unverified: true
tags:
  - nlp
  - transformer
  - clinical-notes
  - long-context
processed_by: crosslinker
processed_at: 2026-04-30
---

# Clinical Longformer

## Overview

Clinical Longformer is a transformer-based natural language processing (NLP) model pre-trained and fine-tuned on clinical text corpora (including radiology, pathology, and physician notes). It is based on the Longformer architecture, which uses sparse attention to handle long input sequences — enabling processing of lengthy clinical documents that exceed the context window of standard BERT-class models. Clinical Longformer is used for information extraction tasks such as identifying prior outside treatments, HER2/hormone receptor status, and radiology-based prognostication from CT chest/abdomen/pelvis reports.

## Used by

- Applied in the MSK-CHORD clinicogenomic harmonization pipeline at Memorial Sloan Kettering Cancer Center (MSK) to extract prior outside treatment and HER2/hormone receptor status from 705,241 radiology and clinical notes; a specialized `radLongformer` variant was fine-tuned on CT chest/abdomen/pelvis reports for 6-month mortality prediction [PMID:39506116](../papers/39506116.md).

## Notes

- Long-context variant of the Longformer architecture; handles clinical documents beyond the 512-token BERT limit.
- Fine-tuned on MSK AACR Project GENIE BPC PRISSMM-schema annotated labels (3,202 patients, 38,719 radiology reports).
- `radLongformer` (a task-specific variant) was prognostic for [OS](../cancer_types/OS.md) in all five cancer types studied in MSK-CHORD but did not additively improve upon engineered feature models when combined with them [PMID:39506116](../papers/39506116.md).
- Used alongside [clinicalbert](../methods/clinicalbert.md) and other transformer models in the MSK-CHORD NLP pipeline [PMID:39506116](../papers/39506116.md).

## Sources

- [PMID:39506116](../papers/39506116.md) — Kather et al. used Clinical Longformer for extraction of prior outside treatment and HER2/hormone receptor status from clinical notes as part of the MSK-CHORD dataset construction pipeline; every NLP model in the pipeline achieved AUC > 0.9 with precision and recall > 0.78 against manually curated MSK-BPC labels [PMID:39506116](../papers/39506116.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
