---
name: Brain Lower Grade Glioma (TCGA, PanCancer Atlas 2018)
studyId: lgg_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 516
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - lgg
  - glioma
  - brain
  - IDH
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Brain Lower Grade Glioma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Brain Lower Grade Glioma PanCancer Atlas 2018 cohort is the [LGG](../cancer_types/LGG.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `lgg_tcga_pan_can_atlas_2018`. It covers approximately 516 lower-grade glioma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [LGG](../cancer_types/LGG.md) is molecularly split by [IDH1](../genes/IDH1.md) mutation status: IDH1-mutant LGG forms the highly homogeneous iCluster C11 (high silhouette score), while IDH1-wildtype LGG co-clusters with [GBM](../cancer_types/GBM.md) in C23. LGG is one of the pivotal examples of TCGA survival-genomic integration: IDH-mutant LGG has substantially longer [OS](../cancer_types/OS.md) than IDH-wildtype, contributing to the WHO 2016 glioma diagnostic update.

## Composition

- Cancer type: Brain Lower Grade Glioma ([LGG](../cancer_types/LGG.md)), OncoTree code LGG.
- Approximately 516 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625055](../papers/29625055.md) — TCGA Pan-Cancer Clinical Data Resource (Liu et al., 2018)

## Notable findings derived from this cohort

- [IDH1](../genes/IDH1.md)-mutant LGG forms iCluster C11, one of the most homogeneous and highest-silhouette pan-cancer iClusters (330/351 samples in methylation cluster 1 are IDH1-mutant); IDH1-wildtype LGG co-clusters with GBM in C23, demonstrating that molecular subtype overrides histologic category. [PMID:29625048](../papers/29625048.md)
- IDH1-driven LGGs fall into methylation cluster 1, while EGFR-driven LGG and GBM fall into methylation cluster 16, despite both groups occupying the same mRNA and RPPA clusters — illustrating distinct cis-regulatory effects of [IDH1](../genes/IDH1.md) vs [EGFR](../genes/EGFR.md) driver mutations. [PMID:29625049](../papers/29625049.md)
- IDH-mutant LGG showed lower [STAT1](../genes/STAT1.md) and reduced [CXCL10](../genes/CXCL10.md) within immune subtype C5, associating with reduced immune infiltration; within C3, BRAF-mutant tumors have higher CD8 T-cell fraction than NRAS-mutant tumors. [PMID:29625049](../papers/29625049.md)
- RTK-RAS pathway alteration rate in IDHwt LGG is 82%; [EGFR](../genes/EGFR.md) alterations in 52% of LGG IDHwt; IDH+PI3K co-targeting opportunity in 14% of IDH-mutant LGG. [PMID:29625049](../papers/29625049.md)
- [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md) mutations are the canonical example in TCGA-CDR of how TCGA survival data produce practice-changing findings: IDH-mutant LGG has substantially longer OS than IDH-wildtype, supporting WHO 2016 glioma classification update. [PMID:29625055](../papers/29625055.md)

## Sources

- cBioPortal study: `lgg_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
