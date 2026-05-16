---
name: Ollivier-Ricci Curvature (Network Geometry Biomarker)
slug: ollivier-ricci-curvature
kind: method
canonical_source: corpus
unverified: true
tags: [network-analysis, copy-number, graph-theory, biomarker, bioinformatics, novel-method]
processed_by: crosslinker
processed_at: 2026-05-16
---

# Ollivier-Ricci Curvature (Network Geometry Biomarker)

## Overview

Ollivier-Ricci (OR) curvature is a discrete geometric measure borrowed from optimal transport theory that quantifies the local "curvature" of edges in a network. Applied to cancer genomics, the method maps gene-level copy-number alteration (CNA) profiles from individual tumors onto a fixed protein–protein interaction (PPI) network (e.g., HPRD-derived). For each edge (u, v) in the network, the OR curvature κ(u, v) is computed as 1 minus the Wasserstein-1 (earth mover's) distance between the normalized CNA distributions of the neighborhoods of u and v. Summing edge curvatures over the entire network yields a patient-level total curvature κ_G, which serves as a single scalar biomarker capturing the network-level coherence of the tumor's CNA landscape.

## Used by

- Applied to CNA profiles of 45 [HGSOC](../cancer_types/HGSOC.md) patients treated with immune checkpoint inhibitors (ICIs) at MSK; total curvature κ_G stratified [OS](../cancer_types/OS.md) with log-rank p = 0.00047 (median OS 7.4 mo low-curvature vs 20.3 mo high-curvature), outperforming TMB (p = 0.032), LST (p = 0.43), and [FGA](../genes/FGA.md) (p = 0.20) as ICI-response predictors; curvature was not prognostic in HGSOC patients not receiving ICI, suggesting ICI-specificity [PMID:34819508](../papers/34819508.md)

## Notes

- The PPI network used was HPRD-restricted to the largest connected component intersecting the data: 3,489 genes, 9,710 edges (mean degree 5.57).
- CNA input: FACETS-derived integer copy numbers per gene mapped to GRCh37 gene coordinates from MSK-IMPACT and whole-exome segments.
- The 25th-percentile cutoff used for Kaplan-Meier stratification was chosen by inspection; a maximally-selected log-rank cutoff yielded a similar split.
- [TP53](../genes/TP53.md) ranked #1 by positive Δκ_risk (0.209) across all sub-analyses, validating biological plausibility.
- Validated as a prognostic signal in METABRIC breast cancer (n = 1,903) in a supplementary analysis.
- A key limitation is that the method requires only DNA copy-number data and a PPI scaffold, making it applicable to any MSK-IMPACT-style CNA assay without RNA or protein data.

## Sources

- [PMID:34819508](../papers/34819508.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
