---
name: CADD (Combined Annotation Dependent Depletion)
slug: cadd
kind: method
canonical_source: corpus
unverified: true
tags: [variant-scoring, pathogenicity, functional-annotation]
processed_by: crosslinker
processed_at: 2026-05-21
---

# CADD (Combined Annotation Dependent Depletion)

## Overview

CADD (Combined Annotation Dependent Depletion) is a framework for scoring the deleteriousness of single nucleotide variants and small indels in the human genome. It integrates over 60 functional annotations using a support vector machine trained on simulated de novo variants versus fixed variants in the human lineage. CADD Phred-scaled scores ≥20 indicate the top 1% of deleterious variants; ≥30 indicates the top 0.1%.

## Used by

- Used to annotate functional impact of somatic variants in endometrial polyps; [UBE2A](../genes/UBE2A.md) p.(Arg6Trp) received a CADD score of 24.4, supporting its classification as a deleterious driver alteration [PMID:28445112](../papers/28445112.md)
- Used as one component of annotation in the three-tool consensus driver-calling pipeline (OncodriveFML, MutSigCV, dNdScv) for WGS-based driver identification in 25 metastatic [CSCC](../cancer_types/CSCC.md) tumors [PMID:35982973](../papers/35982973.md)

## Notes

- Phred-scaled C-score ≥20 = top 1% most deleterious variants; ≥30 = top 0.1%.
- Covers all possible SNVs genome-wide (pre-computed) and can score small indels.
- Often used alongside REVEL, AlphaMissense, and population-frequency tools for comprehensive variant interpretation.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
