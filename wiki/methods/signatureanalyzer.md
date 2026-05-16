---
name: SignatureAnalyzer
slug: signatureanalyzer
kind: method
canonical_source: corpus
unverified: true
tags:
  - mutational-signatures
  - bayesian-nmf
  - whole-exome-seq
  - dlbcl
  - somatic-mutations
processed_by: crosslinker
processed_at: 2026-05-16
---

# SignatureAnalyzer

## Overview

SignatureAnalyzer is a Bayesian non-negative matrix factorization (NMF) framework for de novo mutational signature discovery. Unlike fixed-rank NMF, it uses an automatic relevance determination (ARD) prior to infer the optimal number of signatures from the data without requiring a pre-specified number of components. It decomposes a mutation count matrix (samples × mutation contexts) into signature profiles and exposure weights, enabling quantification of mutational processes contributing to each tumor's somatic mutation burden.

## Used by

- Applied to 304 DLBCLs (WES, median 87.6× coverage) to discover de novo mutational signatures; identified three dominant processes: aging/CpG deamination (~80% of mutations), canonical AID (cAID) at RCY motifs, and a non-canonical AID2 at WA motifs (resembling COSMIC Signature 9); cAID activity localized to known aberrant somatic hypermutation targets ([BCL2](../genes/BCL2.md), [SGK1](../genes/SGK1.md), [PIM1](../genes/PIM1.md), [IGLL5](../genes/IGLL5.md)) [PMID:29713087](../papers/29713087.md)

## Notes

- Corpus-derived slug; not a cBioPortal canonical gene-panel identifier.
- Implemented as part of the Broad Institute's genomic analysis toolkit; closely related to the Bayesian NMF approach described in the SignatureAnalyzer-GPU framework.
- The ARD prior allows the model to automatically prune redundant signatures, making it suitable for cohorts where the number of active mutational processes is unknown.
- Results from SignatureAnalyzer are often cross-referenced against COSMIC reference signatures for biological interpretation.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
