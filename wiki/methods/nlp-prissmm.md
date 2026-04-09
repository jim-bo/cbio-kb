---
name: NLP annotation with PRISSMM curation
slug: nlp-prissmm
kind: method
unverified: true
tags: [nlp, real-world-data, prissmm, genie-bpc, radiology, pathology]
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# NLP annotation with PRISSMM curation

## Overview

Transformer-based NLP models trained on the AACR Project GENIE BPC (Biopharma Collaborative) PRISSMM curation framework to extract structured annotations (sites of disease, progression, metastasis) from free-text clinician, radiology, and pathology notes at scale, using manually curated MSK-BPC labels as ground truth.

## Used by

- [PMID:39506116](../papers/39506116.md) — NLP transformer models trained/validated on Project GENIE BPC (PRISSMM) curation with MSK-BPC (n=3,202 patients, 38,719 radiology reports) as labeled ground truth, then applied to annotate 705,241 radiology reports across 24,950 MSK patients for the MSK-CHORD dataset. Per-site metastasis classification AUCs were generally 0.85–0.99 (bone, liver, lung, lymph node, adrenal, pleura, CNS). NLP-derived clinical features, combined with genomics, outperformed stage- or genomics-only models for overall survival prediction and enabled discovery of [SETD2](../genes/SETD2.md) mutation as a biomarker of lower CNS metastasis and longer immune checkpoint blockade response in [LUAD](../cancer_types/LUAD.md) [PMID:39506116](../papers/39506116.md).

## Notes

- Annotations are not perfect ground truth and may propagate curation biases from PRISSMM/BPC [PMID:39506116](../papers/39506116.md).
- Training cohort is single-institution (MSK); generalizability required external validation [PMID:39506116](../papers/39506116.md).

## Sources

- [PMID:39506116](../papers/39506116.md)

*This page was processed by **entity-page-writer** on **2026-04-08**.*
