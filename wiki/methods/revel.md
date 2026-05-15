---
name: REVEL (Rare Exome Variant Ensemble Learner)
slug: revel
kind: method
canonical_source: corpus
unverified: true
tags: [variant-scoring, pathogenicity, ensemble-method]
processed_by: crosslinker
processed_at: 2026-05-14
---

# REVEL (Rare Exome Variant Ensemble Learner)

## Overview

REVEL is an ensemble method for predicting the pathogenicity of missense variants, combining scores from 13 individual tools (including MutPred, FATHMM, VEST3, PolyPhen-2, SIFT, CADD, DANN, MetaSVM, MetaLR, MutationAssessor, MutationTaster, LRT, and GERP++) using a random forest classifier. It was trained on rare missense variants from ClinVar disease mutations versus common non-disease variants. Scores range from 0 to 1, with higher scores indicating greater predicted pathogenicity.

## Used by

- Applied to score somatic variants in endometrial polyps; [UBE2A](../genes/UBE2A.md) p.(Arg6Trp) received a REVEL score of 0.56, contributing to its multi-tool functional characterization as a likely driver alteration [PMID:28445112](../papers/28445112.md)

## Notes

- Pre-computed scores available for all possible human missense SNVs via the REVEL database.
- Scores >0.5 are associated with pathogenicity in most calibration studies.
- Ensemble approach leverages complementary strengths of 13 underlying tools.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
