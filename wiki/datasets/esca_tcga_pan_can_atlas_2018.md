---
name: Esophageal Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: esca_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 185
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - esca
  - esophageal
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Esophageal Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Esophageal Carcinoma PanCancer Atlas 2018 cohort is the [ESCA](../cancer_types/ESCA.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `esca_tcga_pan_can_atlas_2018`. It covers approximately 185 esophageal carcinoma samples (encompassing both adenocarcinoma [EAC] and squamous cell carcinoma [ESCC](../cancer_types/ESCC.md) histologies) with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. ESCA is among the cancer types with substantial intra-type molecular heterogeneity — less than 50% of samples cluster into any single iCluster — due to the two distinct molecular subtypes (squamous and adenocarcinoma) mixed within the TCGA ESCA cohort.

## Composition

- Cancer type: Esophageal Carcinoma ([ESCA](../cancer_types/ESCA.md)), containing both adenocarcinoma and squamous cell carcinoma subtypes.
- Approximately 185 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)

## Notable findings derived from this cohort

- ESCA was among 8 cancer types with <50% of samples in any single iCluster, reflecting the two molecular subtypes (squamous ESCC and adenocarcinoma EAC) coexisting in this dataset; squamous ESCA co-clusters with pan-squamous iClusters (C10, C27) while EAC co-clusters with pan-GI EBV+/CIN subtypes. [PMID:29625048](../papers/29625048.md)
- NRF2/oxidative-stress pathway peak alteration rate in esophagogastric squamous ([ESCC](../cancer_types/ESCC.md)) is 23%; EBV+ esophagogastric shows PI3K pathway alteration in 80% of samples; [ERBB2](../genes/ERBB2.md) alterations concentrate in chromosomally-unstable esophagogastric (CIN subtype). [PMID:29625048](../papers/29625048.md)
- All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for ESCA by the TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR), making this one of 13 cancer types with the highest endpoint reliability. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `esca_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
