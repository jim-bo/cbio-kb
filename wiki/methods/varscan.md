---
name: VarScan
slug: varscan
kind: method
canonical_source: corpus
unverified: true
tags:
  - variant-calling
  - somatic
  - bioinformatics
processed_by: wiki-cli
processed_at: 2026-05-14
---

# VarScan

## Overview

VarScan is a platform-independent variant detection tool for next-generation sequencing data. It uses a heuristic/statistic approach to call somatic mutations (SNVs and indels) and copy-number alterations in paired tumor-normal samples.

## Used by

- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) [PMID:25240281](../papers/25240281.md)
- Used alongside MuTect for somatic variant calling in 78 gastric adenocarcinoma WES samples; joint calling identified a high-clonality (HiC) subtype with distinct C>G mutational enrichment (25% vs. 9% in low-clonality; P=0.002) [PMID:25583476](../papers/25583476.md)
- Used for somatic variant calling in the AA CRC WES pipeline alongside MuTect, contributing to the mutational landscape analysis of 103 African American MSS colorectal cancers [PMID:25583493](../papers/25583493.md)

## Notes

- Commonly paired with MuTect and Strelka in multi-caller somatic variant detection pipelines.
- Corpus-derived slug; not in cBioPortal gene panel ontology.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
