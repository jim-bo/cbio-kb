---
name: ClinicalBERT
slug: clinicalbert
kind: method
canonical_source: corpus
unverified: true
tags:
  - nlp
  - transformer
  - clinical-notes
  - bert
processed_by: crosslinker
processed_at: 2026-04-30
---

# ClinicalBERT

## Overview

ClinicalBERT is a BERT-based transformer model pre-trained on clinical notes (originally on MIMIC-III discharge summaries) and fine-tuned for clinical information extraction tasks. It applies standard bidirectional attention over 512-token windows and is used to classify or extract structured entities from clinical text, including tumor site annotations and binary labels relevant to cancer staging and treatment status.

## Used by

- Applied in the MSK-CHORD clinicogenomic harmonization pipeline at Memorial Sloan Kettering Cancer Center to classify tumor sites (ten binary multi-label) from clinical and radiology notes across 24,950 patients spanning five cancer types [PMID:39506116](../papers/39506116.md).

## Notes

- BERT-base architecture pre-trained or fine-tuned on clinical text; handles up to 512 tokens per document.
- Used for multi-label tumor-site extraction (ten binary outputs) in the MSK-CHORD pipeline [PMID:39506116](../papers/39506116.md).
- NLP-derived tumor-site annotations (from ClinicalBERT) outperformed ICD billing codes for patient-level metastatic-site annotation, with precision/recall improvements of 0.03–0.32 [PMID:39506116](../papers/39506116.md).
- Used alongside [clinical-longformer](../methods/clinical-longformer.md), RoBERTa, and BERT-base-uncased in the same pipeline [PMID:39506116](../papers/39506116.md).

## Sources

- [PMID:39506116](../papers/39506116.md) — Kather et al. used ClinicalBERT for ten-binary multi-label tumor-site extraction from clinical and radiology notes in the MSK-CHORD dataset (24,950 patients); NLP-derived tumor sites were the most prognostic single modality for [OS](../cancer_types/OS.md) in stage-IV patients across all five cancer types in the random survival forest models [PMID:39506116](../papers/39506116.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
