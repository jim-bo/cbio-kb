---
name: PARADIGM
slug: paradigm
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, integrative-genomics, multi-platform, signaling]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# PARADIGM

## Overview

PARADIGM (PAthway Recognition Algorithm using Data Integration on Genomic Models) is a probabilistic graphical model that integrates multi-platform genomic data (copy number, gene expression, methylation) with curated pathway knowledge to infer pathway-level activity (Integrated Pathway Activities, IPAs) for individual samples. By propagating observed genomic alterations through signaling and regulatory network graphs, PARADIGM identifies which upstream or downstream pathway nodes are functionally activated or inactivated, going beyond single-gene mutation analysis to capture convergent pathway effects.

## Used by

- Used in the TCGA breast cancer ILC/IDC multi-platform integrative analysis (n=817) to infer pathway-level activity differences between invasive lobular and invasive ductal carcinoma; contributed to the characterization of AKT/mTOR pathway hyperactivation in [ILC](../cancer_types/ILC.md) (highest pAKT of any breast subtype) and identification of convergent upstream RTK/PTEN/PIK3CA alterations in 40-45% of [ILC](../cancer_types/ILC.md) samples. [PMID:26451490](../papers/26451490.md)
- PARADIGM used for integrative pathway inference combining genomic, transcriptomic, and copy-number data across 1,122 TCGA diffuse gliomas to model signaling pathway activity [PMID:26824661](../papers/26824661.md)
- PARADIGM pathway inference applied to 206 TCGA sarcomas to model pathway activity from multi-platform genomic data [PMID:29100075](../papers/29100075.md)
- Applied to infer activity of ~19,000 pathway features across the 9,759-tumor TCGA PanCancer Atlas cohort for characterization of the 28 integrated molecular subtypes [PMID:29625048](../papers/29625048.md).

## Notes

- Original PARADIGM algorithm published by Vaske et al. (Bioinformatics, 2010).
- Requires curated pathway databases (e.g., NCI Pathway Interaction Database, KEGG) as input network structure.
- PARADIGM output (IPAs) can be used as features for clustering, survival analysis, or comparison across tumor subtypes.
- Computationally intensive; typically run on an HPC cluster for cohort-scale analyses.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
