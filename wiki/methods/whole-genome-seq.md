---
name: Whole-genome sequencing (WGS)
slug: whole-genome-seq
kind: method
canonical_source: 
unverified: true
tags: [sequencing, wgs]
processed_by: wiki-cli
processed_at: 2026-05-11
---

# Whole-genome sequencing (WGS)

## Overview

Unbiased short-read sequencing of the entire tumor (and matched normal) genome, used in the corpus for structural variant detection, mutational signature analysis at non-coding sites, evolutionary timing, and microbiome read mining.

## Used by

- [PMID:35927489](../papers/35927489.md) — 177 WGS samples in the CLL-map cohort; identified 681 SV breakpoints in 141 patients (~4.8/patient), [BCL2](../genes/BCL2.md) translocations predominantly in M-CLL via aberrant V(D)J, and a recurrent 37-Mb chr14 deletion disrupting [ZFP36L1](../genes/ZFP36L1.md) (and [DICER1](../genes/DICER1.md), [TRAF3](../genes/TRAF3.md)) in U-CLL via class-switch recombination. Supported mutational signature analysis (canonical AID SBS84 enriched in U-CLL clustered mutations; non-canonical AID SBS85 enriched in M-CLL, p=1.6×10^-9; plus SBS18) [PMID:35927489](../papers/35927489.md).
- [PMID:36723991](../papers/36723991.md) — WGS on FACS-purified Hodgkin and Reed Sternberg cells from 25 cHL patients with matched intratumoral T cells as germline; established the first comprehensive WGS landscape of cHL, with median post-artifact-removal mutational burden of 5,279 SBS+indels per genome (range 1,880–18,883), prevalent APOBEC mutagenesis (SBS2/SBS13), AID off-target activity, chromothripsis, and timing of WGD as a late event [PMID:36723991](../papers/36723991.md).
- [PMID:37202560](../papers/37202560.md) — tumor WGS in the AC-ICAM colon cancer atlas, used for microbiome read mining alongside 16S rRNA sequencing [PMID:37202560](../papers/37202560.md).
- [PMID:37730754](../papers/37730754.md) — shallow WGS used for CNV assessment from 62 plasma samples (10 patients) in the longitudinal ctDNA arm of the rhabdomyosarcoma progression/relapse study [PMID:37730754](../papers/37730754.md).
- [PMID:38117484](../papers/38117484.md) — WGS on a subset of 64 glioma patients in the GLASS International consortium; integrated with 450K/EPIC methylation arrays and RNA-seq [PMID:38117484](../papers/38117484.md).
- [PMID:38412093](../papers/38412093.md) — WGS on 9 of 141 characterized anaplastic thyroid carcinoma regions (the remaining 132 underwent WES) [PMID:38412093](../papers/38412093.md).
- [PMID:38488813](../papers/38488813.md) — WGS at 30X on 44 prostate cancer PDX models; paired with targeted sequencing (T200.1 panel) and RNA-seq for integrative multi-platform molecular characterization [PMID:38488813](../papers/38488813.md).
- [PMID:39305899](../papers/39305899.md) — WGS (BWA-MEM2, MuSE, Mutect2, SomaticSniper, Strelka2, Battenberg/ASCAT) on a subset of the UCLA sarcoma biobank (194 specimens from 126 patients); used alongside [DFCI-ONCOPANEL-3](../methods/DFCI-ONCOPANEL-3.md) targeted DNA and bulk RNA-seq to characterize 24 bone and soft-tissue sarcoma subtypes; enabled CNV analysis including whole-genome duplications in intra-patient heterogeneity studies and functional-vs-genomic concordance analyses [PMID:39305899](../papers/39305899.md).
- Low-pass WGS (5x) applied to 51 primary and 102 metastatic breast cancer specimens in AURORA cohort; 11 DNA segments more frequently amplified in metastases (q<0.05), including [MYC](../genes/MYC.md) and [MDM4](../genes/MDM4.md) regions [PMID:36585450](../papers/36585450.md)
- Applied to primary tumors from 2 MEC patients (Patient 1: 29x tumor/25x normal; Patient 2: 22x tumor/15x normal; GRCh37/hg19); revealed >30-way biallelic chromoplexy event in MEC1 and double-minute [ELK4](../genes/ELK4.md) amplification in MEC2 [PMID:36577525](../papers/36577525.md)
- Applied to 40 treatment-naive [HGSOC](../cancer_types/HGSOC.md) tumor-normal pairs; mutational signature inference classified tumours into HRD-Dup (n=16), HRD-Del (n=6), and FBI (n=14) subtypes [PMID:36517593](../papers/36517593.md)
- Applied to 14 NHL cases (DLBCL and [FL](../cancer_types/FL.md)) with matched tumor/normal pairs in the BCGSC study; identified 109 recurrently mutated genes including [KMT2D](../genes/KMT2D.md) and [MEF2B](../genes/MEF2B.md) as major histone-modifier drivers [PMID:21796119](../papers/21796119.md)
- Two HNSCC tumors underwent whole-genome sequencing at 31x mean coverage in the Broad HNSCC study, complementing whole-exome sequencing of 74 tumors [PMID:21798893](../papers/21798893.md)
- WGS applied to 65 breast tumors (BCCRC) to characterize structural rearrangements and somatic mutation landscapes [PMID:22495314](../papers/22495314.md)
- WGS of 25 melanoma tumors used to identify [PREX2](../genes/PREX2.md) recurrent mutations and characterize KIT/BRAF alteration patterns [PMID:22622578](../papers/22622578.md)
- WGS used in [HCC](../cancer_types/HCC.md) genomic studies to identify [TERT](../genes/TERT.md) promoter mutations, [CTNNB1](../genes/CTNNB1.md), and [TP53](../genes/TP53.md) alterations [PMID:22634756](../papers/22634756.md)
- Used for WGS of 103 breast cancer tumors in the Broad cohort ([brca_broad](../datasets/brca_broad.md)), enabling structural variant and fusion discovery including MAGI3-AKT3 [PMID:22722202](../papers/22722202.md)
- Used for WGS of 37 medulloblastoma tumors in the PCGP cohort ([mbl_pcgp](../datasets/mbl_pcgp.md)), identifying [KDM6A](../genes/KDM6A.md), [DDX3X](../genes/DDX3X.md), and [SMARCA4](../genes/SMARCA4.md) as driver genes [PMID:22722829](../papers/22722829.md)
- 97 of 276 TCGA colorectal carcinoma pairs analyzed by low-pass whole-genome sequencing (~3-4X coverage) for structural variant detection alongside WES [PMID:22810696](../papers/22810696.md)
- 39 of 125 pediatric medulloblastoma pairs (ICGC) analyzed by deep whole-genome sequencing at 35-fold mean coverage; identified tetraploidy as frequent early event in Group 3 and 4 tumors and described first medulloblastoma fusion genes [PMID:22832583](../papers/22832583.md)
- Applied alongside WES in Genentech colorectal cohort to detect structural variants including RSPO2/RSPO3 fusions [PMID:22895193](../papers/22895193.md)
- Applied to [SCLC](../cancer_types/SCLC.md) tumors in CLCGP study (29 cases) to detect structural rearrangements and copy number alterations in TP53/RB1-null tumors [PMID:22941188](../papers/22941188.md)
- Used in JHU [SCLC](../cancer_types/SCLC.md) study (36 tumors) to complement WES and characterise copy number landscape including SOX2/MYCL amplifications [PMID:22941189](../papers/22941189.md)
- Applied to subset of TCGA [LUSC](../cancer_types/LUSC.md) tumors (178-tumor cohort) to detect structural variants alongside WES-based somatic mutation calling [PMID:22960745](../papers/22960745.md)
- Applied in Broad [LUAD](../cancer_types/LUAD.md) WES study (183 tumors) to characterise structural variation and somatic copy number alterations [PMID:22980975](../papers/22980975.md)
- WGS of 87 neuroblastoma tumor/normal pairs from the Broad cohort; detected structural variants including [MYCN](../genes/MYCN.md) amplifications and [ALK](../genes/ALK.md) rearrangements [PMID:23334666](../papers/23334666.md)
- WGS of 7 ETP-ALL tumor/normal pairs at St. Jude; revealed complex structural rearrangements in [FLT3](../genes/FLT3.md), JAK1/2, and cytokine receptor genes [PMID:23334668](../papers/23334668.md)
- Whole-genome sequencing (~49× tumor / 30× germline; 101 bp paired reads) on 16 esophageal adenocarcinoma pairs; rearrangements called by dRanger yielded 2,952 candidate events; no recurrent fusions found [PMID:23525077](../papers/23525077.md)
- Whole-genome sequencing (mean 61× tumor / 34× normal; Illumina GAIIx paired-end 101 bp) on 57 prostate tumor/normal pairs; identified 5,596 somatic rearrangements by dRanger and characterized chromoplexy chains in 88% of tumors [PMID:23622249](../papers/23622249.md)
- Whole-genome sequencing (mean 30.54× coverage) on 50 [AML](../cancer_types/AML.md) tumor/normal-skin pairs in TCGA [AML](../cancer_types/AML.md) study; VAF-based clonal architecture analysis showed >50% of tumors had ≥1 subclone [PMID:23634996](../papers/23634996.md)
- Applied in 5 of 60 ACC tumor/normal pairs (Illumina HiSeq 2000, mean coverage 37x) for structural variant detection using CREST; complemented whole-exome sequencing for comprehensive somatic alteration characterization [PMID:23685749](../papers/23685749.md)
- Applied to 96 pediatric pilocytic astrocytoma tumor/blood pairs (Illumina HiSeq2000, BWA + samtools + Picard, hg19); mean somatic mutation rate <0.1/Mb; PINDEL, CREST, and DELLY used for SV detection revealing [KIAA1549](../genes/KIAA1549.md):[BRAF](../genes/BRAF.md) fusions and novel BRAF/NTRK2 fusions [PMID:23817572](../papers/23817572.md)
- Applied to 42 deep-coverage [GBM](../cancer_types/GBM.md) tumor/normal pairs; detected 238 high-confidence somatic rearrangements including [EGFR](../genes/EGFR.md) intragenic events and one case of chromothripsis; identified [TERT](../genes/TERT.md) promoter mutations in 84% [PMID:24120142](../papers/24120142.md)
- Applied at fourfold mean haploid coverage in 99 [BLCA](../cancer_types/BLCA.md) tumors; WGS mate-pair reads confirmed FGFR3-TACC3 fusion junctions detected by RNA-seq [PMID:24121792](../papers/24121792.md)
- Applied to 4 [MCL](../cancer_types/MCL.md) tumor/normal pairs; detected ~3,700 somatic mutations per tumor (1.2/Mb) and identified kataegis foci in 3/4 cases around the t(11;14) breakpoint and Ig loci [PMID:24145436](../papers/24145436.md)
- Paired tumor/normal whole-genome sequencing on Illumina (hg19, BWA alignment) for 28 metastatic neuroendocrine neoplasms in the BC Cancer POG program; combined with RNA-seq in an integrated WGTA approach that identified actionable alterations in 24/28 patients [PMID:24326773](../papers/24326773.md).
- Applied to 26 of 203 multiple myeloma tumor/normal pairs at ~30× average depth; all 26 samples harbored structural variants; enabled identification of SVs and complemented WES-based mutation calling [PMID:24434212](../papers/24434212.md)
- Applied to 44 rhabdomyosarcoma tumor/normal pairs on Complete Genomics platform at mean 105× depth with 97% genome coverage; identified 553 somatic SVs affecting 419 genes and established the PAX-fusion-positive vs PAX-fusion-negative [RMS](../cancer_types/RMS.md) classification [PMID:24436047](../papers/24436047.md)
- Low-pass paired-end WGS (6–8× coverage) of 114 bladder carcinoma tumors; identified 3 in-frame FGFR3-TACC3 fusions and 4 [ERBB2](../genes/ERBB2.md) rearrangements with different fusion partners; average 22 genomic rearrangements per sample [PMID:24476821](../papers/24476821.md)
- Referenced in HCC genomic landscape review as part of next-generation sequencing approaches that identified novel HCC driver genes including TERT, ARID1A, ARID2, RPS6KA3, PIK3CA, IRF2, NFE2L2, and KEAP1 [PMID:24735922](../papers/24735922.md)
- Germline WGS cited as the sequencing approach used for identifying candidate FNHGC predisposition variants in CDH1-negative families, including DOT1L, INSR, FBXO24, and CTNND1 [PMID:24816255](../papers/24816255.md)
- Low-pass WGS (1-3x coverage) from 100-250 ng input DNA (KAPA LTP / Illumina HiSeq 2000) applied to four FFPE prostate needle biopsies; CNA profiles concordant with high-resolution aCGH, enabling pre-treatment CNA burden assessment [PMID:25024180](../papers/25024180.md)
- Low-pass WGS (<6x coverage) on 107 tumor/germline pairs from the TCGA gastric adenocarcinoma cohort (stad_tcga_pub) to detect structural rearrangements, including CLDN18-ARHGAP26 and CLDN18-ARHGAP6 interchromosomal fusions [PMID:25079317](../papers/25079317.md)
- Low-pass WGS on 93 of 230 lung adenocarcinomas (luad_tcga_pub) identified an average of 36 gene-gene/gene-inter-gene rearrangements per tumor; chromothripsis detected in 6/93 (6%); ALK, ROS1, RET fusions detected exclusively in transversion-low tumors [PMID:25079552](../papers/25079552.md)

## Notes

- Small WGS cohorts in some corpus papers (e.g., n=25 in cHL, 177 in CLL) are repeatedly cited as a limitation for SV and rare-variant inference [PMID:35927489](../papers/35927489.md) [PMID:36723991](../papers/36723991.md).
- HRS-cell WGS in cHL required whole-genome amplification, introducing palindromic SBS artifacts that had to be computationally removed [PMID:36723991](../papers/36723991.md).

## Sources

- [PMID:35927489](../papers/35927489.md)
- [PMID:36723991](../papers/36723991.md)
- [PMID:37202560](../papers/37202560.md)
- [PMID:37730754](../papers/37730754.md)
- [PMID:38117484](../papers/38117484.md)
- [PMID:38412093](../papers/38412093.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:39305899](../papers/39305899.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:36585450](../papers/36585450.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:36517593](../papers/36517593.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:21796119](../papers/21796119.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:21798893](../papers/21798893.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22495314](../papers/22495314.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22622578](../papers/22622578.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22634756](../papers/22634756.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22722202](../papers/22722202.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22722829](../papers/22722829.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22832583](../papers/22832583.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22895193](../papers/22895193.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22941188](../papers/22941188.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22941189](../papers/22941189.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22980975](../papers/22980975.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23334668](../papers/23334668.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23525077](../papers/23525077.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23622249](../papers/23622249.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23634996](../papers/23634996.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23817572](../papers/23817572.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24120142](../papers/24120142.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24121792](../papers/24121792.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24145436](../papers/24145436.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24326773](../papers/24326773.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24735922](../papers/24735922.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:24816255](../papers/24816255.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
