---
name: CIBERSORTx
slug: cibersortx
kind: method
canonical_source: corpus
unverified: true
tags: [immune-deconvolution, digital-cytometry, rna-seq, tumor-microenvironment]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# CIBERSORTx

## Overview

CIBERSORTx is a computational deconvolution algorithm that estimates the relative and absolute fractions of immune and stromal cell populations from bulk gene expression data (RNA-seq or microarray). It uses support vector regression (SVR) against a reference gene expression matrix (LM22 leukocyte signature matrix or custom signatures) to infer cell-type proportions without requiring physical cell sorting. The "X" version adds batch correction to reduce technology-dependent effects when applying a reference matrix across different profiling platforms. It is widely used for tumor microenvironment (TME) characterization in clinical cohorts where only bulk RNA-seq is available.

## Used by

- Applied to bulk RNA-seq from 176 metastatic urothelial carcinoma patients in UC-GENOME to estimate immune cell fractions; identified enrichment of plasma cells, memory B cells, and activated dendritic cells in luminal subtypes (LumP), and higher T cell inflamed and [IFNG](../genes/IFNG.md) signature scores in Ba/Sq tumors [PMID:36333289](../papers/36333289.md)
- CIBERSORT applied to RNA-seq data from 45 melanoma biopsies for immune cell deconvolution; CD8+ T cells and NK cells increased and M1 macrophages decreased on-therapy in responders [PMID:29033130](../papers/29033130.md)

## Notes

- CIBERSORTx requires a pre-defined reference signature matrix; results may be sensitive to choice of reference and to batch effects between training and test cohorts.
- Imperfect in distinguishing closely related cell subtypes (e.g., [CD4](../genes/CD4.md)+ T cell subsets) without high-resolution reference signatures.
- Total RNA-seq (as used in UC-GENOME) vs. capture-based RNA-seq may introduce systematic differences in deconvolution results.
- Absolute mode estimates depend on a calibration step that can vary across platforms; relative mode (fraction) estimates are more comparable across studies.

## Sources

- [PMID:36333289](../papers/36333289.md) — UC-GENOME metastatic UC study; CIBERSORTx immune deconvolution of bulk RNA-seq to characterize TME composition by molecular subtype.

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
