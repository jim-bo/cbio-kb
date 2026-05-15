---
name: TCGA Sarcoma (SARC)
studyId: sarc_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 206
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - hm450-methylation-array
  - affymetrix-snp6
  - rppa
panels: []
tags:
  - tcga
  - sarcoma
  - soft-tissue-sarcoma
  - leiomyosarcoma
  - liposarcoma
  - scna-driven
  - immune-microenvironment
  - multi-platform
processed_by: crosslinker
processed_at: 2026-05-15
---

# TCGA Sarcoma (SARC)

## Overview

The TCGA Sarcoma Analysis Working Group profiled 206 adult soft tissue sarcomas spanning six major histologies using WES/WGS, RNA-seq, miRNA-seq, DNA methylation, SNP6 copy number, and RPPA. All cases were treatment-naive. Published in *Cell* (2017), the study establishes that complex-karyotype sarcomas are dominated by somatic copy-number alterations with low mutation burden, defines integrated molecular subtypes with distinct prognosis within each histology, and characterizes histology-specific immune microenvironment signatures.

## Composition

- **206 primary adult soft tissue sarcomas** from 32 contributing centers, all treatment-naive. Median age 60 (range 20–90); 93% intermediate-to-high grade; 84% deep soft tissue or visceral.
- **Histology breakdown:** 80 [LMS](../cancer_types/LMS.md) (53 somatic/skeletal-type STLMS + 27 uterine [ULMS](../cancer_types/ULMS.md)), 50 [DDLPS](../cancer_types/DDLS.md), 44 [UPS](../cancer_types/USARC.md), 17 [MFS](../cancer_types/MFS.md), 10 [SS](../cancer_types/SS.md), 5 [MPNST](../cancer_types/MPNST.md).
- 437 samples received; 206 passed [BCR](../genes/BCR.md) QC and pathology review.

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — n=205
- [whole-genome sequencing](../methods/whole-genome-seq.md) — n=37
- [RNA-seq](../methods/rna-seq.md)
- [miRNA-seq](../methods/mirna-seq.md)
- [HM450 methylation array](../methods/hm450-methylation-array.md)
- [Affymetrix SNP6](../methods/affymetrix-snp6.md) — SCNA profiling; [GISTIC](../methods/gistic.md) for peaks; [ABSOLUTE](../methods/absolute.md) for purity/ploidy
- [RPPA](../methods/rppa.md) — protein expression
- [iCluster](../methods/icluster.md) — cross-platform integrative clustering
- [PARADIGM](../methods/paradigm.md) — pathway inference
- [MuSiC](../methods/mutsig.md) and [Genome MuSiC](../methods/genome-music.md) — significantly mutated gene analysis
- [ESTIMATE](../methods/estimate.md) / Bindea — immune-cell-infiltration scoring

## Papers using this cohort

- [PMID:29100075](../papers/29100075.md) — TCGA Research Network, *Cell* (2017): Comprehensive and Integrated Genomic Characterization of Adult Soft Tissue Sarcomas.

## Notable findings derived from this cohort

- **Pan-sarcoma significantly mutated genes (FDR < 0.05): only [TP53](../genes/TP53.md), [ATRX](../genes/ATRX.md), and [RB1](../genes/RB1.md).** 67% (138/206) of tumors carried at least one variant in a known cancer gene, but few hit known hotspots; mean mutation rate 1.06 mut/Mb. [PMID:29100075](../papers/29100075.md)
- **Complex-karyotype sarcomas are SCNA-driven.** DDLPS had the highest SCNA frequency of any TCGA tumor type, driven by recurrent 12q13~15 amplification ([MDM2](../genes/MDM2.md) 100%, [CDK4](../genes/CDK4.md) 92%, [HMGA2](../genes/HMGA2.md) 76%, [FRS2](../genes/FRS2.md) 96%). [PMID:29100075](../papers/29100075.md)
- **DDLPS molecular subtypes predict disease-specific survival.** Three SCNA clusters (K1 [JUN](../genes/JUN.md)-amplified; K2 [TERT](../genes/TERT.md)-amplified; K3 6q25.1-amplified) combined with methylation (Meth1 hypo / Meth2 hyper) yield groups with different DSS (p=0.001); Meth2 HR=4.4 vs Meth1 (p=0.002). [PMID:29100075](../papers/29100075.md)
- **[LMS](../cancer_types/LMS.md) molecular split:** iCluster separates by site (ULMS vs STLMS); within STLMS, C1 (hypermethylated, [RB1](../genes/RB1.md)-mutation-enriched) has worse RFS (p=0.0002) and DSS (p=0.008) than C2. AKT-pathway alterations in 84% of ULMS+STLMS C1 vs 44% of STLMS C2 (p=1e–4). [PMID:29100075](../papers/29100075.md)
- **miR-181b-5p is an independent RFS predictor in LMS** — multivariate HR 7.4 (95% CI 3.1–17.8, p=9e–6). [PMID:29100075](../papers/29100075.md)
- **UPS and [MFS](../cancer_types/MFS.md) form a single molecular spectrum;** clustering on myxoid-stroma-associated genes is the primary discriminator. Hippo-pathway [VGLL3](../genes/VGLL3.md)/[YAP1](../genes/YAP1.md) amplifications in 11%/3% of UPS/MFS. [PMID:29100075](../papers/29100075.md)
- **Synovial sarcoma ([SS](../cancer_types/SS.md)) is genomically distinct:** 100% carry [SS18](../genes/SS18.md)–[SSX1](../genes/SSX1.md) or [SS18](../genes/SS18.md)–[SSX2](../genes/SSX2.md) fusions; fewest mutations and SCNAs. [PMID:29100075](../papers/29100075.md)
- **Recurrent [TRIO](../genes/TRIO.md)–[TERT](../genes/TERT.md) fusions** (n=3) drive highest [TERT](../genes/TERT.md) expression in the cohort. [PMID:29100075](../papers/29100075.md)
- **Immune microenvironment is histology-specific and prognostic.** STLMS has highest [CD274](../genes/CD274.md) (PD-L1) expression among sarcoma subtypes (p=4e–5 vs ULMS). NK-cell infiltration correlates with improved DSS across histologies. UPS/MFS dendritic-cell signatures predict improved DSS; nominated for checkpoint-inhibitor trials. [PMID:29100075](../papers/29100075.md)
- Nuclear pleomorphism score correlates with whole-genome doublings (p=0.003), subclonal genome fraction (p=4e–6), and aneuploidy (p=5e–6). [PMID:29100075](../papers/29100075.md)
- Mutational signatures are clock-like: 90% attributable to COSMIC5 (53%) and COSMIC1 (37%); two hypermutators carry [MSH6](../genes/MSH6.md) frameshift / low [MSH2](../genes/MSH2.md) expression (COSMIC6 MMR signature). [PMID:29100075](../papers/29100075.md)

## Sources

- cBioPortal study ID: sarc_tcga_pub
- TCGA data portal / GDC

*This page was processed by **crosslinker** on **2026-05-15**.*
