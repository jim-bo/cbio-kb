---
name: WGCNA (Weighted Gene Co-expression Network Analysis)
slug: wgcna
kind: method
canonical_source: corpus
unverified: true
tags:
  - co-expression
  - network-analysis
  - transcriptomics
  - bioinformatics
processed_by: crosslinker
processed_at: 2026-05-21
---

# WGCNA (Weighted Gene Co-expression Network Analysis)

## Overview

WGCNA is an unsupervised computational method for constructing gene co-expression networks from bulk RNA-seq or microarray data. Genes are grouped into modules (clusters) based on correlated expression patterns across samples. Module eigengenes (representative expression profiles) are then correlated with sample traits, phenotypes, or mutation profiles to identify biologically coherent gene programs. WGCNA is implemented as an R package and produces hierarchical clustering of co-expressed genes that can be used for downstream pathway enrichment, survival analysis, and drug-response modeling.

## Used by

- Applied in the Beat [AML](../cancer_types/AML.md) study ([aml_ohsu_2018](../datasets/aml_ohsu_2018.md)) to identify 14 co-expression gene clusters across 451 [AML](../cancer_types/AML.md) RNA-seq specimens (411 patients); lasso regression linked specific mutation × expression-cluster combinations to ex vivo drug sensitivity. A 345-gene "turquoise" cluster enriched for immune pathways co-occurred with FLT3-ITD and predicted [ibrutinib](../drugs/ibrutinib.md) sensitivity (overlap with 17-gene signature: representation factor 13.6, P<1.734e-04); a 110-gene "magenta" subnetwork predicted [ibrutinib](../drugs/ibrutinib.md) resistance and tracked with adverse ELN 2017 risk [PMID:30333627](../papers/30333627.md).
- Applied to AML RNA-seq data (Beat AML Waves 1–4, n=942 specimens); identified 13 module eigengenes with 98% concordance between Waves 1+2 and Waves 3+4; modules 3, 9, and 12 associated with shorter [OS](../cancer_types/OS.md); module 3 hub gene [PEAR1](../genes/PEAR1.md) nominated as single-gene prognostic biomarker [PMID:35868306](../papers/35868306.md)

## Notes

- Results are hypothesis-generating; WGCNA modules and their drug associations are correlative and require prospective validation.
- Module membership and cluster labels (e.g. "turquoise", "magenta") are data-set-specific and depend on the set of input samples.
- Canonical WGCNA reference: Langfelder P & Horvath S, BMC Bioinformatics 2008.

## Sources

- [PMID:30333627](../papers/30333627.md) — Tyner et al. 2018, Beat AML multi-omics drug-sensitivity profiling.

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35868306](../papers/35868306.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
