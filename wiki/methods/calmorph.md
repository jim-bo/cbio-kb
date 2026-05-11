---
name: CalMorph
slug: calmorph
kind: method
canonical_source: corpus
unverified: true
tags: [high-content-imaging, morphological-profiling, yeast]
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# CalMorph

## Overview

CalMorph is a high-content image-analysis pipeline for quantifying yeast cell morphology. It extracts 501 morphological parameters spanning three cellular compartments — cell wall / overall shape (C\* parameters), actin cytoskeleton (A\* parameters), and nucleus (D\* parameters) — from fluorescence micrographs of fixed *Saccharomyces cerevisiae* cells. Statistical comparisons across strains (e.g., generalised linear models, one-way ANOVA with FDR correction) identify which parameters are significantly altered by a genetic perturbation. Principal component analysis (PCA) followed by linear discriminant analysis (LDA) of the high-dimensional feature vector can separate functionally distinct variant classes.

## Used by

- CalMorph v1.3 (501 morphological parameters: cell wall, actin, nucleus) applied to ≥200 cells × 5 replicates per RHOA-mutant yeast strain; 164 parameters were significantly altered (FDR<0.05); LDA on top-17 PCs cleanly separated GOF from LOF mutants [PMID:24816253](../papers/24816253.md)

## Notes

- Requires fluorescence staining of fixed yeast cells (e.g., DAPI for nucleus, rhodamine-phalloidin or GFP-tagged actin markers for actin, calcofluor or similar for cell wall).
- Statistical power scales with biological replicates and number of cells imaged per replicate; ≥200 cells × ≥5 replicates is a typical recommendation.
- The 501-parameter space is highly correlated; dimensionality reduction (PCA) prior to discriminant analysis is standard practice.
- Developed in the context of systematic yeast deletion / mutation screens; a reference database of morphological phenotypes for ~4,700 yeast deletion mutants exists (Ohya et al. 2005).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
