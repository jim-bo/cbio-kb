---
name: Rhabdoid Cancer
oncotree_code: MRT
main_type: Rhabdoid Cancer
parent: KIDNEY
tags:
  - rhabdoid
  - pediatric
  - SMARCB1
  - SWI-SNF
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Rhabdoid Cancer (MRT)

## Overview

Rhabdoid cancer (MRT in OncoTree; also called malignant rhabdoid tumor of the kidney) is a rare, highly aggressive pediatric malignancy defined by biallelic inactivation of [SMARCB1](../genes/SMARCB1.md), a core subunit of the SWI/SNF chromatin-remodelling complex. In the OncoTree hierarchy it is a child of KIDNEY under the Rhabdoid Cancer main type. Extra-cranial MRT encompasses tumors of the kidney (majority), soft tissue, and liver; the liver variant is separately coded as [MRTL](../cancer_types/MRTL.md). Despite a near-uniform single driver, MRT splits into reproducible miRNA, mRNA, and DNA-methylation sub-groups with distinct developmental and epigenetic signatures. Overall 4-year survival is ~23.2%.

## Cohorts in the corpus

- [mrt_bcgsc_2016](../datasets/mrt_bcgsc_2016.md): 67 primary extra-cranial MRTs (58 kidney, 7 soft tissue, 2 liver) banked through the TARGET initiative and Children's Oncology Group; 40 tumor/normal pairs for WGS; 66 miRNA-Seq; 40 RNA-Seq + WGBS; 35 H3K27me3 ChIP-Seq; 10 H3K27ac ChIP-Seq; data in NCBI dbGaP phs000470 [PMID:26977886](../papers/26977886.md)

## Recurrent alterations

- [SMARCB1](../genes/SMARCB1.md) — biallelic inactivation (mutations, deletions, somatic LOH) in 39/40 cases; the dominant and near-universal driver; loss causes downstream loss of H3K27me3 at homeobox promoters and gain of MRT-specific super-enhancers at HOX clusters [PMID:26977886](../papers/26977886.md)
- [SMARCA4](../genes/SMARCA4.md) — sole driver in the one SMARCB1-intact case (somatic LOH plus germline one-base deletion) [PMID:26977886](../papers/26977886.md)
- [DSCAM](../genes/DSCAM.md) — recurrent (2/40) heterozygous somatic missense substitutions (p.Val424Ile, p.Ser1354Thr); only non-SMARCB1 recurrently mutated gene; possibly passenger [PMID:26977886](../papers/26977886.md)
- [SPECC1L](../genes/SPECC1L.md) — intronic mutations in 6/40 cases associated with decreased expression; fusion partner in 4/7 SMARCB1-deletion-driven fusions [PMID:26977886](../papers/26977886.md)
- [KCNJ3](../genes/KCNJ3.md) — intronic mutations in 8/40 cases associated with increased expression [PMID:26977886](../papers/26977886.md)
- [NF2](../genes/NF2.md), [LIF](../genes/LIF.md) — focally deleted in the only chromosome-22 deletions that spare [SMARCB1](../genes/SMARCB1.md) [PMID:26977886](../papers/26977886.md)
- Quiet somatic genome: median 612.5 SNVs/case (0.231 mutations/Mb), 97.1% non-coding; median 5 non-synonymous substitutions/case [PMID:26977886](../papers/26977886.md)
- PIPseq cohort included rhabdoid tumor cases; SMARCB1 homozygous deletion of chr22q11.23 with biallelic loss of expression identified as EZH2-inhibitor target [PMID:28007021](../papers/28007021.md)
- All extracranial MRT PDX models in PPTC cohort (n=261) carried inactivating alterations of SMARCB1 and/or SMARCA4; hedgehog, TNFα, and p53 signaling enriched by GSEA [PMID:31693904](../papers/31693904.md).

## Subtypes

- **miRNA sub-group 1** (n=57/66): clusters with normal cerebellum and TCGA pheochromocytoma/paraganglioma; lower miR-200 family expression (suggesting active EMT) [PMID:26977886](../papers/26977886.md)
- **miRNA sub-group 2** (n=9/66): clusters with synovial sarcomas; higher miR-200 family expression [PMID:26977886](../papers/26977886.md)
- **mRNA sub-group 1** (AT/RT-like): enriched for extra-renal cases; over-expresses [BMP4](../genes/BMP4.md), [DLK1](../genes/DLK1.md), [MEOX2](../genes/MEOX2.md) [PMID:26977886](../papers/26977886.md)
- **mRNA sub-group 2** (RTK-like): over-expresses [WNT5A](../genes/WNT5A.md), [PCDH18](../genes/PCDH18.md), [TCF21](../genes/TCF21.md), [MEIS1](../genes/MEIS1.md) [PMID:26977886](../papers/26977886.md)
- **Methylation sub-group A**: higher promoter CGI methylation; enriched for age >1 year at diagnosis; gains methylation at tumor-suppressor promoters ([RASSF1](../genes/RASSF1.md), IRX1, TWIST2, DLEC1, TBX5) [PMID:26977886](../papers/26977886.md)
- **Methylation sub-group B**: clusters with hESC; enriched for age <1 year [PMID:26977886](../papers/26977886.md)

## Therapeutic landscape

- No prospective treatment data reported in the corpus [PMID:26977886](../papers/26977886.md)
- Epigenetic vulnerabilities (H3K27me3 loss at homeobox promoters, MRT-specific HOX-cluster super-enhancers, [HOTAIR](../genes/HOTAIR.md) over-expression) are candidate therapeutic dependencies [PMID:26977886](../papers/26977886.md)

## Sources

- [PMID:26977886](../papers/26977886.md) — Chun et al., integrative multi-omic reference of 40 extra-cranial MRTs (WGS + WGBS + RNA-Seq + miRNA-Seq + ChIP-Seq)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28007021](../papers/28007021.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
