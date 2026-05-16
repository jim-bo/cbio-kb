---
name: t-SNE (t-Distributed Stochastic Neighbor Embedding)
slug: tsne
kind: method
canonical_source: corpus
unverified: true
tags: [dimensionality-reduction, visualization, transcriptomics, single-cell]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# t-SNE (t-Distributed Stochastic Neighbor Embedding)

## Overview

t-SNE is a nonlinear dimensionality-reduction algorithm that maps high-dimensional data (e.g., gene expression profiles, single-cell counts) to two or three dimensions for visualization. It minimizes the Kullback-Leibler divergence between a Student-t distribution in the low-dimensional embedding and a Gaussian distribution over pairwise distances in the high-dimensional space. A perplexity hyperparameter controls the effective number of neighbors considered. t-SNE preserves local structure well but does not reliably preserve global cluster distances; results depend on the random seed, perplexity, and number of iterations.

## Used by

- Used to visualize transcriptome relationships among 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) alongside consensus hierarchical clustering; confirmed that POG NENs cluster together and away from TCGA primary tumours in a 1,553-gene discriminator embedding [PMID:40328872](../papers/40328872.md).
- t-SNE on the 12,454 most-variable methylation probes (s.d. > 0.25) across 740 Group 3/4 medulloblastoma cases resolved eight molecular subtypes (I–VIII), each with distinctive driver-event enrichment; subtype structure stabilised at ≥500 samples [PMID:28726821](../papers/28726821.md)
- Applied to the top 10,000 variably methylated CpGs from 165 schwannomatosis-associated schwannomas for visualization of four DNA-methylation subgroups segregating by anatomic location [PMID:33025139](../papers/33025139.md)

## Notes

- t-SNE should not be used for quantitative distance comparisons between clusters; UMAP is a common alternative with better global structure preservation.
- Typically applied after initial PCA or top-variable-gene selection to reduce noise and compute time.
- Reference implementation: Rtsne (R) or scikit-learn/MulticoreTSNE (Python).

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:28726821](../papers/28726821.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:33025139](../papers/33025139.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
