---
name: Head and Neck Squamous Cell Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: hnsc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 530
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - hnsc
  - head-and-neck
  - squamous
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Head and Neck Squamous Cell Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Head and Neck Squamous Cell Carcinoma PanCancer Atlas 2018 cohort is the [HNSC](../cancer_types/HNSC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `hnsc_tcga_pan_can_atlas_2018`. It covers approximately 530 head and neck squamous cell carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [HNSC](../cancer_types/HNSC.md) is among the cancer types with substantial intra-type molecular heterogeneity (less than 50% of samples in any single iCluster), reflecting the HPV+ and HPV- subtypes with distinct molecular profiles.

## Composition

- Cancer type: Head and Neck Squamous Cell Carcinoma ([HNSC](../cancer_types/HNSC.md)), OncoTree code HNSC.
- Approximately 530 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.
- Contains HPV+ and HPV- molecular subtypes with distinct mutational profiles.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- HPV+ HNSC co-clusters with pan-squamous iCluster C27 (alongside HPV+ [CESC](../cancer_types/CESC.md) and some [BLCA](../cancer_types/BLCA.md)); HPV- HNSC co-clusters with other squamous iClusters (C10, C25) sharing chr11 amplification; HNSC was among 8 cancer types with <50% of samples in any single iCluster. [PMID:29625048](../papers/29625048.md)
- Pan-squamous iClusters (C10, C25, C27) including HPV- HNSC share dNp63/TAp63 squamous signaling, proliferation, hypoxia, and basal signaling programs; C3 and C20 (immune-enriched clusters) also contain HNSC samples contributing to JAK2/STAT1/3/6 pathway enrichment. [PMID:29625048](../papers/29625048.md)
- [EGFR](../genes/EGFR.md) alterations in 13% of HPV- HNSC (RTK-RAS pathway); PI3K pathway broadly altered in squamous cancers including HNSC; [FGFR3](../genes/FGFR3.md) mutual exclusivity with PI3K-pathway alterations is a notable cross-pathway interaction in HNSC. [PMID:29625049](../papers/29625049.md)
- All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for HNSC by TCGA-CDR, making this one of 13 cancer types with the highest endpoint reliability. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `hnsc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
