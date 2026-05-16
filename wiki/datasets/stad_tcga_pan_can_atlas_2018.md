---
name: Stomach Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: stad_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 443
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - stad
  - stomach
  - gastric
  - adenocarcinoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Stomach Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Stomach Adenocarcinoma PanCancer Atlas 2018 cohort is the [STAD](../cancer_types/STAD.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `stad_tcga_pan_can_atlas_2018`. It covers approximately 443 stomach adenocarcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [STAD](../cancer_types/STAD.md) was among cancer types with substantial intra-type molecular heterogeneity (<50% in any single iCluster), reflecting its four established molecular subtypes (EBV, MSI, GS, CIN). STAD samples contribute to three distinct pan-GI iClusters (C1: EBV-CIMP, C4: pan-GI CIN, C18: MSI) and the ERBB2-amplified C2 iCluster. All four clinical endpoints are recommended without reservation for STAD by TCGA-CDR.

## Composition

- Cancer type: Stomach Adenocarcinoma ([STAD](../cancer_types/STAD.md)), OncoTree code STAD.
- Approximately 443 tumor samples; encompasses EBV, MSI, GS (genomically stable), and CIN (chromosomal instability) molecular subtypes.
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

## Notable findings derived from this cohort

- STAD contributes to three distinct pan-cancer iClusters: C1:STAD (EBV-CIMP, hypermethylated EBV-associated tumors), C4:pan-GI (CIN, COAD/READ + non-squamous [ESCA](../cancer_types/ESCA.md)), and C18:pan-GI (MSI, mostly STAD+[COAD](../cancer_types/COAD.md)); STAD was among 8 cancer types with <50% of samples in any single iCluster. [PMID:29625048](../papers/29625048.md)
- ERBB2-amplified STAD co-clusters in pan-cancer C2:[BRCA](../cancer_types/BRCA.md) (HER2 amp) alongside BRCA and [BLCA](../cancer_types/BLCA.md) — a cross-tissue ERBB2-amplified subtype supporting HER2-directed agents beyond breast cancer; [ERBB2](../genes/ERBB2.md) alterations in chromosomally-unstable esophagogastric CIN subtype (~26%). [PMID:29625048](../papers/29625048.md)
- MSI-H STAD tumors over-express immune effectors GZMA/PRF1/GZMK/GZMH (Kolmogorov-Smirnov P<0.01); EBV+ esophagogastric shows PI3K pathway alteration in 80% of samples; PI3K+MEK co-targeting opportunity in 10% of EBV+ stomach. [PMID:29625049](../papers/29625049.md)
- All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for STAD by TCGA-CDR. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `stad_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
