---
name: Whole-genome sequencing (WGS)
slug: whole-genome-seq
kind: method
canonical_source: 
unverified: true
tags: [sequencing, wgs]
processed_by: entity-page-writer
processed_at: 2026-05-15
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
- Referenced in [HCC](../cancer_types/HCC.md) genomic landscape review as part of next-generation sequencing approaches that identified novel [HCC](../cancer_types/HCC.md) driver genes including [TERT](../genes/TERT.md), [ARID1A](../genes/ARID1A.md), [ARID2](../genes/ARID2.md), [RPS6KA3](../genes/RPS6KA3.md), [PIK3CA](../genes/PIK3CA.md), [IRF2](../genes/IRF2.md), [NFE2L2](../genes/NFE2L2.md), and [KEAP1](../genes/KEAP1.md) [PMID:24735922](../papers/24735922.md)
- Germline WGS cited as the sequencing approach used for identifying candidate FNHGC predisposition variants in CDH1-negative families, including [DOT1L](../genes/DOT1L.md), [INSR](../genes/INSR.md), [FBXO24](../genes/FBXO24.md), and [CTNND1](../genes/CTNND1.md) [PMID:24816255](../papers/24816255.md)
- Low-pass WGS (1-3x coverage) from 100-250 ng input DNA (KAPA LTP / Illumina HiSeq 2000) applied to four FFPE prostate needle biopsies; CNA profiles concordant with high-resolution aCGH, enabling pre-treatment CNA burden assessment [PMID:25024180](../papers/25024180.md)
- Low-pass WGS (<6x coverage) on 107 tumor/germline pairs from the TCGA gastric adenocarcinoma cohort ([stad_tcga_pub](../datasets/stad_tcga_pub.md)) to detect structural rearrangements, including CLDN18-ARHGAP26 and CLDN18-ARHGAP6 interchromosomal fusions [PMID:25079317](../papers/25079317.md)
- Low-pass WGS on 93 of 230 lung adenocarcinomas ([luad_tcga_pub](../datasets/luad_tcga_pub.md)) identified an average of 36 gene-gene/gene-inter-gene rearrangements per tumor; chromothripsis detected in 6/93 (6%); [ALK](../genes/ALK.md), [ROS1](../genes/ROS1.md), [RET](../genes/RET.md) fusions detected exclusively in transversion-low tumors [PMID:25079552](../papers/25079552.md)
- Used to sequence 50 ChRCC tumors (60× tumor / 30× normal) in the TCGA ChRCC project, enabling detection of structural rearrangements at the [TERT](../genes/TERT.md) promoter and kataegis events via Meerkat. [PMID:25155756](../papers/25155756.md)
- Applied to four CRC primary/metastasis trios (median 87× tumor, 50× normal) at the New York Genome Center to validate MSK-IMPACT findings; confirmed all panel-level calls and revealed genome-wide discordance in heterogeneous cases. [PMID:25164765](../papers/25164765.md)
- Used in Ewing sarcoma WGS of 112 tumors with matched germline on Illumina HiSeq2000 (median 35× tumor depth); BWA alignment to GRCh37-lite; identified [STAG2](../genes/STAG2.md) (17%), [TP53](../genes/TP53.md) (7%), and [EZH2](../genes/EZH2.md) as significantly mutated genes [PMID:25223734](../papers/25223734.md)
- WGS at median 45.1× depth on 47 tumor/xenograft/normal DNA samples from 15 breast cancer PDX series; used to identify somatic SNVs (4.3–27.7×10³ per genome) and SVs driving clonal selection at engraftment [PMID:25470049](../papers/25470049.md)
- Applied to 3 primary-tumor regions plus 2 matched lymph-node metastases each from 2 gastric adenocarcinoma patients (Pt1: 4,082 nonsilent mutations; Pt2: 287); phylogenetic analysis revealed divergence among primary regions with metastases sharing a common clonal ancestor [PMID:25583476](../papers/25583476.md)
- High-coverage WGS performed on 29 [HNSC](../cancer_types/HNSC.md) tumors as part of TCGA profiling; identified 62 structural aberrations per tumor on average, no recurrent ALK/ROS/RET fusions, and FGFR3-TACC3 fusions in 2 HPV(+) tumors [PMID:25631445](../papers/25631445.md)
- Deep WGS on 38 melanoma samples plus low-pass WGS on 119 samples enabled identification of structural rearrangements and complex chromothripsis events (ShatterSeek) enriched in Triple-WT subtype. [PMID:26091043](../papers/26091043.md)
- Whole-genome sequencing used to characterize structural variants and mutational signatures in breast cancer [PMID:26168399](../papers/26168399.md)
- Whole-genome sequencing used to identify somatic mutations and structural rearrangements in colorectal cancer [PMID:26343386](../papers/26343386.md)
- Performed on 56 neuroblastomas (39 high-risk, 17 low-risk) with matched normal controls (Illumina HiSeq 2000, 2x100 nt PE, aligned to hg19 with BWA); identified recurrent 5p15.33 breakpoint cluster upstream of [TERT](../genes/TERT.md) in 12/39 (31%) high-risk tumors; average 13.3 non-synonymous mutations per genome [PMID:26466568](../papers/26466568.md)
- Low-pass WGS on 100 pairs and high-pass on 19 primary prostate adenocarcinomas (TCGA); used to characterize structural variants and mutational burden (median 0.94 mutations/Mb) complementing the primary WES platform [PMID:26544944](../papers/26544944.md).
- Used via Complete Genomics cPAL platform (NCBI Build 37) on 21 salivary adenoid cystic carcinoma test-set tumors; enabled discovery of novel MYBL1-NFIB fusions from t(8;9) translocations and diverse [MYBL1](../genes/MYBL1.md) rearrangements [PMID:26631609](../papers/26631609.md).
- Applied to 14 primary uveal melanoma samples with matched germline; BWA alignment to GRCh37, SAMtools/bcftools variant calling, Janda SV calling, and binocular CNV segmentation; enabled discovery of [PLCB4](../genes/PLCB4.md) p.D630Y hotspot and BRCA-like mutational signature in 79% of samples [PMID:26683228](../papers/26683228.md).
- Used for alignment to GRCh37-lite in 15 matched primary/recurrent medulloblastoma pairs with germline controls plus 18 pairs without germline (46 total samples); demonstrated <12% shared somatic SNVs/indels between primary and recurrent tumors [PMID:26760213](../papers/26760213.md).
- WGS used for telomere-length analysis and TERT-promoter mutation detection in a subset of diffuse gliomas from the TCGA pan-glioma cohort; ATRX-mutant gliomas showed significantly longer telomeres than TERTp-mutant samples (ALT mechanism) [PMID:26824661](../papers/26824661.md)
- WGS on Illumina HiSeq 2500 (100 bp paired-end) of 20 ACC tumors and primagrafts with reads aligned to hg19 by BWA; rearrangements called with dRanger and BreakPointer; identified MYB super-enhancer hijacking mechanism [PMID:26829750](../papers/26829750.md)
- WGS of 25 ACC tumor/normal pairs (mean coverage 65.2× tumor / 38.1× normal) on Illumina HiSeq; identified 253 chromosomal rearrangements including 5 novel NFIB fusion partners and Rho-GTPase pathway disruption in 44% of tumors [PMID:26862087](../papers/26862087.md)
- Whole-genome sequencing data from the BCC/SCC corpus (EGAD0000101525) used as a reference baseline for skin cancer mutation burdens (cSCC mean 50 substitutions/Mb, BCC mean 65 substitutions/Mb) in the NB-UVB surveillance model. [PMID:26950094](../papers/26950094.md)
- Applied to 40 MRT tumor/normal pairs (median tumor content 88.0%); identified near-universal SMARCB1 biallelic inactivation (39/40 cases), quiet overall genomes (median 612.5 SNVs/case, 0.231 mutations/Mb), and Chr22 as the dominant structural variation locus (9/15 recurrent CNA loci, 22/26 verified gene fusions). [PMID:26977886](../papers/26977886.md)
- Whole-genome sequencing cited as reference methodology for comprehensive mutation detection in AML; the primary AMLSG study used a targeted 111-gene panel, with WGS noted as context for driver-gene discovery [PMID:27276561](../papers/27276561.md)
- Whole-genome sequencing used alongside WES and targeted NGS in studies of germline susceptibility and somatic driver characterization in young-onset NSCLC [PMID:27346245](../papers/27346245.md)
- WGS on N=32 B-ALL cases to identify IGH-DUX4 rearrangements and characterize the genomic landscape of the DUX4/ERG B-ALL subtype. [PMID:27776115](../papers/27776115.md)
- Low-pass (6–8×) whole-genome sequencing performed on 51 oesophageal cancers as part of the TCGA esophageal/stomach multi-platform study to characterize structural variants [PMID:28052061](../papers/28052061.md).

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

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36585450](../papers/36585450.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36517593](../papers/36517593.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:21796119](../papers/21796119.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:21798893](../papers/21798893.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22495314](../papers/22495314.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22622578](../papers/22622578.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22634756](../papers/22634756.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22722202](../papers/22722202.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22722829](../papers/22722829.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22832583](../papers/22832583.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22895193](../papers/22895193.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22941188](../papers/22941188.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22941189](../papers/22941189.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22980975](../papers/22980975.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23334668](../papers/23334668.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23525077](../papers/23525077.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23622249](../papers/23622249.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23634996](../papers/23634996.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23817572](../papers/23817572.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24120142](../papers/24120142.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24121792](../papers/24121792.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24145436](../papers/24145436.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24326773](../papers/24326773.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24735922](../papers/24735922.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24816255](../papers/24816255.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25155756](../papers/25155756.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25470049](../papers/25470049.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25631445](../papers/25631445.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26168399](../papers/26168399.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26466568](../papers/26466568.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26631609](../papers/26631609.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26829750](../papers/26829750.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26862087](../papers/26862087.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26950094](../papers/26950094.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26977886](../papers/26977886.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27276561](../papers/27276561.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27346245](../papers/27346245.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27776115](../papers/27776115.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
