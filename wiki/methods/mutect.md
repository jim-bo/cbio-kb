---
name: MuTect
slug: mutect
kind: method
canonical_source: corpus
unverified: false
tags:
  - somatic-mutation
  - snv-calling
  - whole-exome-seq
  - whole-genome-seq
processed_by: entity-page-writer
processed_at: 2026-05-21
---

# MuTect

## Overview

MuTect is a Bayesian statistical framework for the sensitive and specific detection of somatic single-nucleotide variants (SNVs) in paired tumor/normal sequencing data. Developed at the Broad Institute, it uses a two-sample likelihood model to distinguish somatic mutations from germline variants and sequencing artifacts, with particular attention to low-allele-fraction variants in impure tumor samples. MuTect is widely applied in cancer exome and genome sequencing pipelines, typically paired with Indelocator for indel detection.

## Used by

- Applied alongside Indelocator, dRanger, BreakPointer, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors; detected 356,136 somatic base-pair mutations across the cohort (mean 33 non-silent exonic per primary tumor) [PMID:23622249](../papers/23622249.md)
- Used for somatic SNV calling in 149 esophageal adenocarcinoma WES pairs (and 16 WGS pairs) alongside Indelocator; median 104 non-silent coding mutations per tumor at median genome-wide frequency 9.9/Mb [PMID:23525077](../papers/23525077.md)
- Used alongside SomaticSniper for somatic SNV calling in 60 [ACC](../cancer_types/ACC.md) tumor/normal pairs (55 exome + 5 WGS, Illumina HiSeq 2000); yielded 710 validated nonsynonymous mutations across 643 genes [PMID:23685749](../papers/23685749.md)
- Used to call somatic SNVs from whole-exome data of 45 [BRAF](../genes/BRAF.md) V600 metastatic melanoma FFPE tumors (DeCOG cohort) aligned to hg19 via the Broad Picard/Firehose pipeline [PMID:24265153](../papers/24265153.md).
- Applied for somatic point-mutation calling in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23); mutation validation rate informed by independent re-genotyping [PMID:24336570](../papers/24336570.md)
- Applied for somatic point-mutation calling on the Illumina HiSeq whole-exome arm (13 paired samples) of the rhabdomyosarcoma cohort (147 total tumor/normal pairs); combined with MutSig for significantly mutated gene identification [PMID:24436047](../papers/24436047.md)
- Applied for somatic point-mutation calling on 130 TCGA bladder carcinoma WES tumor/normal pairs; identified mean 302 exonic mutations per sample and APOBEC TpC signature representing 51% of all mutations [PMID:24476821](../papers/24476821.md)
- Used to call SNVs in pre-treatment urothelial carcinoma tumors (n=50), identifying [ERCC2](../genes/ERCC2.md) mutations enriched in [cisplatin](../drugs/cisplatin.md) responders. [PMID:25096233](../papers/25096233.md)
- Used to call somatic SNVs in matched primary/metastasis CRC trios (n=69) as part of the MSK-IMPACT analysis pipeline. [PMID:25164765](../papers/25164765.md)
- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) alongside other callers [PMID:25240281](../papers/25240281.md)
- Used alongside VarScan 2.2.5 for somatic variant calling in 78 gastric adenocarcinoma WES samples; identified 13,866 total somatic mutations including 8,558 missense and 576 nonsense variants [PMID:25583476](../papers/25583476.md)
- Used for somatic SNV and indel calling in the AA CRC WES pipeline (29 discovery tumor/normal pairs), contributing to identification of 20 significantly mutated genes in African American MSS CRC [PMID:25583493](../papers/25583493.md)
- Used for somatic SNV and indel calling (with OxoG artifact filtering) on 29 lymph-node metastases from cSCC patients sequenced with [DFCI-ONCOPANEL-1](../methods/DFCI-ONCOPANEL-1.md) (mean tumor coverage 82×); identified high UV mutation burden (~33 mut/Mb) and recurrent oncogenic alterations [PMID:25589618](../papers/25589618.md)
- MuTect used for SNV calling in 109 microdissected PDA WES samples (≥14 tumor reads, ≥8 normal reads); 92% of 248 non-silent mutations validated by Sanger sequencing. [PMID:25855536](../papers/25855536.md)
- MuTect used for somatic mutation calling in 150 mCRPC whole-exome samples (mean 160×/100× tumor/normal coverage). [PMID:26000489](../papers/26000489.md)
- MuTect used for somatic SNV calling in whole-exome sequencing of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- MuTect used for somatic SNV calling in MSK-IMPACT panel sequencing of pancreatic cancer [PMID:26278805](../papers/26278805.md)
- MuTect used for somatic SNV calling in whole-exome and whole-genome sequencing of colorectal cancer [PMID:26343386](../papers/26343386.md)
- Used for SNV calling alongside MutationSeq in whole-genome sequencing of 46 matched primary/recurrent medulloblastoma samples; contributed to identification of ~5-fold increased mutational burden at recurrence [PMID:26760213](../papers/26760213.md).
- One of four mutation callers (MuTect, Indelocator, VarScan, RADIA) used in ≥2-caller consensus strategy for somatic mutation detection across 820 TCGA diffuse glioma exomes [PMID:26824661](../papers/26824661.md)
- MuTect used for somatic SNV detection in 114 metastatic CRPC biopsies (81 patients); confirmed [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) as top altered genes distinguishing CRPC-NE from CRPC-Adeno [PMID:26855148](../papers/26855148.md)
- Used for somatic mutation calling in the discovery cohort of 6 plasmacytoid-variant bladder tumors profiled by whole-exome sequencing. [PMID:26901067](../papers/26901067.md)
- Used for somatic mutation calling on WES data from 141 tumors (56 men) with metastatic CRPC ([prad_fhcrc](../datasets/prad_fhcrc.md) cohort); identified [AR](../genes/AR.md), [TP53](../genes/TP53.md), [RB1](../genes/RB1.md), and MSH2/MSH6 driver mutations across metastatic sites. [PMID:26928463](../papers/26928463.md)
- Used for SNV calling in 619 CRC FFPE tumor/normal pairs alongside Indelocator (indels) and Strelka (concordant indel filtering) [PMID:27149842](../papers/27149842.md)
- Used for somatic mutation calling in 1,144 [NSCLC](../cancer_types/NSCLC.md) (660 ADC + 484 SqCC) tumor/normal exome pairs in the pan-lung landscape study [PMID:27158780](../papers/27158780.md)
- Used (panel-of-normals filtering analogous to MuTect) for somatic mutation calling in 2,433 primary breast tumours from the METABRIC cohort targeted-sequencing study [PMID:27161491](../papers/27161491.md)
- Used for SNV calling in 62 uRCC tumours profiled with the MSK-IMPACT 230-gene panel (matched normal available in 61/62 cases). [PMID:27713405](../papers/27713405.md)
- SNV calling pipeline applied alongside SNVseeqer on 72 urothelial carcinoma WES samples; only ~28% of mutations were shared between matched pre/post-chemotherapy tumour pairs. [PMID:27749842](../papers/27749842.md)
- Used (MuTect v1.1.7) as the primary substitution caller in analysis of 216 metastatic breast cancer whole-exome sequencing datasets, downstream of BWA-MEM alignment and GATK base recalibration [PMID:28027327](../papers/28027327.md).
- Used MuTect for somatic SNV calling from paired tumor-normal sequencing data [PMID:28373299](../papers/28373299.md)
- Applied MuTect for somatic mutation calling from paired tumor-normal sequencing [PMID:28445112](../papers/28445112.md)
- Used as one of three somatic variant callers (MuTect, Pindel, GATK somatic indel detector) in the MSK-IMPACT SNV/indel pipeline; all calls manually reviewed in IGV [PMID:28481359](../papers/28481359.md)
- Applied for somatic SNV calling on CCA whole-genome and exome sequencing data in the ICGC cholangiocarcinoma cohort (489 tumors across three sequencing platforms) [PMID:28667006](../papers/28667006.md)
- Used for somatic SNV calling (MuTect v1.1.4) in 1001 DLBCL whole-exome sequencing samples [PMID:28985567](../papers/28985567.md)
- Used for SNV calling in 412 [BLCA](../cancer_types/BLCA.md) tumor-normal pairs identifying 128,772 SNVs; confirmed APOBEC-dominated mutational landscape (67% of SNVs) [PMID:28988769](../papers/28988769.md)
- One of four somatic variant callers applied to 68 paired melanoma biopsies in the CA209-038 [nivolumab](../drugs/nivolumab.md) trial; intersection of MuTect 1.1.4, SomaticSniper 1.0.4, VarScan 2.3.7, and Strelka 1.0.13 was used [PMID:29033130](../papers/29033130.md)
- MuTect used for SNV calling in 35 metastatic [CCRCC](../cancer_types/CCRCC.md) paired tumor/normal WES samples to identify [PBRM1](../genes/PBRM1.md) LOF mutations enriched in anti-PD-1 responders [PMID:29301960](../papers/29301960.md)
- MuTect used for SNV calling in 15 vulvar SCC paired tumor/normal WES samples (Korean cohort) aligned to hg19 with BWA v0.7.15 [PMID:29422544](../papers/29422544.md)
- One of seven callers in the TCGA MC3 pipeline; detected the largest number of true positive SNVs and showed highest pair-wise agreement with MuSE; run by Broad Firehose [PMID:29596782](../papers/29596782.md)
- Used to call SNVs (v1.1.6) across 1,013 prostate tumor/normal pairs in the [prad_p1000](../datasets/prad_p1000.md) dataset, identifying 97 SMGs [PMID:29610475](../papers/29610475.md)
- One of seven somatic callers in the MC3 pipeline applied to 11,000 TCGA PanCancer Atlas tumors; consensus calling reduced 22,485,627 raw calls to 2,907,335 high-confidence somatic variants [PMID:29625049](../papers/29625049.md).
- Applied to call somatic variants in 304 DLBCLs (WES with targeted SV bait, median 87.6× tumor coverage); used alongside Indelocator for indel calling [PMID:29713087](../papers/29713087.md)
- Used for somatic variant calling in pediatric WGS samples [PMID:29670109](../papers/29670109.md)
- Applied for somatic mutation calling in the MSK IMPACT neoantigen study cohort [PMID:29657128](../papers/29657128.md)
- Used for somatic SNV calling in the pan-cancer MSI analysis pipeline applied to 11,139 whole-exome tumor-normal pairs [PMID:29850653](../papers/29850653.md)
- Used for somatic SNV calling in the uniform reanalysis of 249 MSS tumor/normal WES samples from seven ICB cohorts; combined with Strelka (indels), Oncotator (annotation), and ABSOLUTE (clonality) [PMID:30150660](../papers/30150660.md)
- MuTect v1.1.7 used for somatic SNV calling from whole-exome sequencing of 622 [AML](../cancer_types/AML.md) specimens in the Beat [AML](../cancer_types/AML.md) study [PMID:30333627](../papers/30333627.md)
- Used for somatic SNV/indel calling in the pan-Asia cHCC-ICC WES/WGS study (133 cases); variant calls subsequently annotated by [annovar](../methods/annovar.md) and analyzed with [mutsigcv](../methods/mutsigcv.md) and dNdScv [PMID:31130341](../papers/31130341.md)
- Part of the consensus SNV-calling pipeline in the high-grade [UTUC](../cancer_types/UTUC.md) study (37 tumor-normal pairs), used together with [strelka](../methods/strelka.md) and [varscan](../methods/varscan.md); variants annotated by [oncotator](../methods/oncotator.md) [PMID:31278255](../papers/31278255.md)
- One of three core SNV/indel variant callers (Broad) in the PCAWG pan-cancer WGS study (n=2,658 tumors, 38 tumor types); consensus calls with Sanger and DKFZ pipelines achieved 95% sensitivity and 95% precision for SNVs [PMID:32025007](../papers/32025007.md).
- Used (MuTect, as well as Strelka, VarScan2, Platypus, Lancet, Scalpel) for somatic variant calling in WES and MSK-IMPACT data from 44 metaplastic breast cancers ([MBC](../cancer_types/MBC.md)) [PMID:33863915](../papers/33863915.md)
- MuTect2 v4.1.2.0 used to call somatic SNVs in reprocessed WES/WGS data from 88 [CSCC](../cancer_types/CSCC.md) tumors aligned with BWA-MEM to hg19; annotated with Funcotator v4.1.2.0 [PMID:34272401](../papers/34272401.md)
- MuTect used alongside [VarDict](../methods/vardict.md) for SNV/indel calling in cfDNA from 681 plasma samples in the MSK-ACCESS analytical validation and prospective clinical cohort [PMID:34145282](../papers/34145282.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- MuTect used for somatic SNV calling in MSK-IMPACT sequencing of 46 [SCLC](../cancer_types/SCLC.md) PDX/CDX and 26 clinical samples in MSK [SCLC](../cancer_types/SCLC.md) model resource [PMID:35440124](../papers/35440124.md).
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md) for somatic SNV calling from WES of 168 prostate cancer brain metastasis samples (Agilent SureSelectXT V7, Illumina NovaSeq6000, ~258× target coverage) [PMID:35504881](../papers/35504881.md)
- Used in [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) cWGTS pipeline for somatic SNV detection from whole-genome sequencing in 114 pediatric/AYA solid tumor patients (Illumina NovaSeq 6000, PE150, median 95× tumor depth) [PMID:35585047](../papers/35585047.md)
- MuTect2 used for somatic variant calling on b37-aligned whole-exome and whole-genome sequencing data in the GLASS longitudinal diffuse glioma expansion cohort (304 patients, 37 hospitals) [PMID:35649412](../papers/35649412.md)

## Notes

- Requires matched tumor/normal BAM files; not designed for tumor-only mode in its original implementation.
- Sensitivity is maintained down to ~5% variant allele fraction under typical WES coverage (80–100×).
- All candidate variants are typically followed by validation with orthogonal methods (e.g., Sequenom, deep digital sequencing).

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25240281](../papers/25240281.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25589618](../papers/25589618.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26000489](../papers/26000489.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26278805](../papers/26278805.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26855148](../papers/26855148.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26901067](../papers/26901067.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26928463](../papers/26928463.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27161491](../papers/27161491.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27749842](../papers/27749842.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28985567](../papers/28985567.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29301960](../papers/29301960.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29422544](../papers/29422544.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29670109](../papers/29670109.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29657128](../papers/29657128.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29850653](../papers/29850653.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30333627](../papers/30333627.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32025007](../papers/32025007.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33863915](../papers/33863915.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35649412](../papers/35649412.md)

*This page was processed by **entity-page-writer** on **2026-05-21**.*
