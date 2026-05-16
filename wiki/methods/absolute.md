---
name: ABSOLUTE
slug: absolute
kind: method
canonical_source: corpus
unverified: false
tags:
  - copy-number
  - tumor-purity
  - clonality
  - somatic-copy-number
processed_by: wiki-cli
processed_at: 2026-05-16
---

# ABSOLUTE

## Overview

ABSOLUTE (Absolute quantification of somatic DNA alterations Using Tumor Heterogeneity) is a computational method that infers tumor purity, ploidy, and the absolute allele-specific copy number of somatic alterations from high-throughput sequencing or SNP-array data. By modeling the distribution of variant allele fractions alongside copy-number profiles, ABSOLUTE converts relative copy-number signals into integer absolute copy numbers and estimates the cancer cell fraction (clonality) of each mutation. It was developed at the Broad Institute and is widely applied in cancer genome studies requiring accurate purity correction before downstream SCNA or mutation analyses.

## Used by

- Used in the WGS-based chromoplexy study of 57 prostate tumors alongside ChainFinder, CLONET, MuTect, Indelocator, dRanger, BreakPointer, and GISTIC v2 for comprehensive somatic variant characterization; WGS-vs-ABSOLUTE purity concordance was R²=0.99 [PMID:23622249](../papers/23622249.md)
- Applied to 203 multiple myeloma tumor/normal pairs for tumor purity estimation, integer copy-number reconstruction, LOH inference, and cancer-cell-fraction (CCF) estimation; enabled characterization of pervasive subclonal architecture including detection of subclonal driver mutations in [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), and [BRAF](../genes/BRAF.md) [PMID:24434212](../papers/24434212.md)
- Used to estimate tumor purity and ploidy for copy-number calling from WES of 39 aggressive cSCC tumors; ABSOLUTE-adjusted copy number revealed gains on chr7, 8q, 9q and losses on 3p, 9p including [CDKN2A](../genes/CDKN2A.md) focal deletions [PMID:25303977](../papers/25303977.md)
- Used to estimate cancer cell fractions (CCFs) for [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), and [EIF1AX](../genes/EIF1AX.md) driver mutations in 402 PTCs; all driver mutations were confirmed as largely clonal, with one exception showing subclonal [EIF1AX](../genes/EIF1AX.md) on a background of clonal [KRAS](../genes/KRAS.md) and [BRAF](../genes/BRAF.md) mutations [PMID:25417114](../papers/25417114.md)
- ABSOLUTE used to estimate copy-number purity and ploidy from Affymetrix SNP 6.0 data in 333 cutaneous melanoma samples as part of the TCGA [SKCM](../cancer_types/SKCM.md) integrative analysis. [PMID:26091043](../papers/26091043.md)
- Used as copy-number absolute quantification method in whole-exome sequencing analysis of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- Applied in the TCGA breast cancer ILC/IDC multi-platform study (n=817) to estimate tumor purity and ploidy, supporting clonality-corrected genomic comparisons between invasive lobular and ductal carcinoma [PMID:26451490](../papers/26451490.md)
- Used in whole-exome sequencing of 538 CLL samples (CLL8 trial cohort) to estimate tumor purity and clonal fractions, enabling CCF-based temporal ordering of driver acquisition and tracking of clonal shifts at relapse [PMID:26466571](../papers/26466571.md)
- Used in the TCGA prostate cancer study to estimate tumor purity in 333 primary prostate adenocarcinomas, alongside other DNA/RNA-based methods, as part of integrated multi-platform molecular characterization [PMID:26544944](../papers/26544944.md).
- Used for tumor purity and ploidy estimation in 1,144 NSCLC exome pairs to enable accurate somatic copy-number and mutation calling [PMID:27158780](../papers/27158780.md)
- ABSOLUTE-style cancer cell fraction (CCF) framework applied after Sequenza tumor purity estimation to 216 metastatic breast cancer exomes; revealed ESR1 mutations were subclonal in 14/21 (67%) of cases [PMID:28027327](../papers/28027327.md).
- ABSOLUTE used for allelic copy number, tumor purity, and ploidy estimation in 164 oesophageal carcinomas and 359 gastric adenocarcinomas as part of the TCGA esophageal/stomach study [PMID:28052061](../papers/28052061.md).
- ABSOLUTE used for clonality estimation in 173 PCPG tumors in the TCGA PCPG study [PMID:28162975](../papers/28162975.md).
- Used with Affymetrix SNP6 data to estimate tumor purity, ploidy, and cancer cell fraction (CCF) in 412 BLCA tumors; CCF used to characterize clonality of APOBEC mutations [PMID:28988769](../papers/28988769.md)
- ABSOLUTE used to estimate tumor purity and ploidy in 206 TCGA sarcomas; 54% of BLCA tumors showed whole-genome doubling; enabled clonal mutation fraction calculations [PMID:29100075](../papers/29100075.md)
- Used to estimate clonality of PBRM1 truncating mutations in 35 metastatic [CCRCC](../cancer_types/CCRCC.md) WES samples; most PBRM1-LOF alterations were predicted to be clonal [PMID:29301960](../papers/29301960.md)
- ABSOLUTE v1.0.6 integrated with FACETS segmentation to estimate clonality of HER2 mutations in the SUMMIT basket trial; 95% (70/74) of HER2 mutations were clonal (CCF >0.85); none of 4 patients with subclonal HER2 mutations achieved clinical benefit [PMID:29420467](../papers/29420467.md)
- ABSOLUTE-style framework used alongside FACETS for cancer-cell fraction (clonality) estimates across 1,013 prostate tumor/normal pairs [PMID:29610475](../papers/29610475.md)
- Applied to Affymetrix SNP 6.0 array data from 10,522 TCGA pan-cancer samples to produce segmented absolute copy number, purity, ploidy, and whole-genome-doubling calls; forms the basis of the arm-level aneuploidy score [PMID:29622463](../papers/29622463.md)
- Applied alongside GISTIC 2.0 to Affymetrix SNP6 data for subclonal copy-number estimation in the TCGA PanCancer Atlas integrative multi-platform analysis of ~10,000 tumors across 33 cancer types [PMID:29625048](../papers/29625048.md).
- Used in DLBCL WES analysis of 304 tumors to estimate tumor purity, ploidy, and cancer cell fractions (CCFs) for clonality analysis across the five genetic subtypes [PMID:29713087](../papers/29713087.md)
- Used for clonality, purity, and ploidy estimation across 249 MSS tumor/normal WES samples in the ICB response study; clonal TMB derived via ABSOLUTE was a stronger predictor of CR/PR than total TMB [PMID:30150660](../papers/30150660.md)

## Notes

- Requires matched tumor/normal data and a copy-number profile (from SNP arrays or WGS).
- Purity and ploidy estimates are presented as a ranked list of solutions; manual review of the top solutions is recommended.
- Output is used to determine whether mutations are clonal or subclonal based on cancer cell fraction.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25303977](../papers/25303977.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26466571](../papers/26466571.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28162975](../papers/28162975.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29301960](../papers/29301960.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
