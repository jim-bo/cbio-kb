---
name: Reverse-Phase Protein Array (RPPA)
slug: rppa
kind: PROTEIN_LEVEL
canonical_source: corpus
unverified: true
tags: [proteomics, protein-expression, rppa]
processed_by: crosslinker
processed_at: 2026-05-09
---

# Reverse-Phase Protein Array (RPPA)

## Overview

Reverse-phase protein array (RPPA) is a high-throughput antibody-based platform for quantifying protein and phosphoprotein expression levels across many samples simultaneously. Lysates from tumor tissue are arrayed on nitrocellulose slides and probed with validated antibodies; signal intensity is normalized and used to estimate relative protein abundance. RPPA enables pathway-level proteomics in large cohorts.

## Used by

- Applied to 214 [GBM](../cancer_types/GBM.md) samples (171 antibodies) as part of TCGA GBM 2013 multi-platform analysis; 127/171 antibodies correlated with transcriptomic subtype; revealed non-linear genotype-to-signaling relationships (e.g., RTK-amplified samples had lower downstream p-AKT/S6K/MAPK signaling than expected) [PMID:24120142](../papers/24120142.md)

## Notes

- Coverage is limited to antibodies in the validated panel; cannot detect novel proteins or isoforms without prior selection.
- Non-linear genotype-to-protein relationships observed in GBM (e.g., PI3K-mutant samples with lower p-AKT than PI3K-WT) highlight the complexity of translating genomic to proteomic signals.
- Widely used in TCGA pan-cancer studies for pathway activation profiling.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
