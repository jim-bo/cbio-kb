---
name: DPClust
slug: dpclust
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [clonality, subclonal-architecture, dirichlet-process, wgs]
processed_by: crosslinker
processed_at: 2026-05-16
---

# DPClust

## Overview

DPClust (Dirichlet Process Clustering) is a computational tool for reconstructing the subclonal architecture of tumours from somatic mutation data. It groups somatic mutations into clusters based on their cancer-cell fractions using a Dirichlet process mixture model, enabling inference of clonal and subclonal populations and evolutionary trajectories.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to infer subclonal mutation clusters and tumour evolutionary timing in the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)

## Notes

- Requires high-quality allele-specific copy-number calls (e.g., from Battenberg) as input to [estimate](../methods/estimate.md) cancer-cell fractions.
- Output clusters are used to distinguish clonal drivers (present at MRCA) from subclonal events that arose later.
- In the Sherlock-Lung study, DPClust was used to determine that [TP53](../genes/TP53.md), [EGFR](../genes/EGFR.md), and [KRAS](../genes/KRAS.md) mutations generally preceded whole-genome doubling events.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
