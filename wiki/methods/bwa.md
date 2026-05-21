---
name: BWA (Burrows-Wheeler Aligner)
slug: bwa
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, short-read, dna-seq, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-21
---

# BWA (Burrows-Wheeler Aligner)

## Overview

BWA (Burrows-Wheeler Aligner) is a short-read alignment tool for mapping sequencing reads to a reference genome using the Burrows-Wheeler transform. It includes three algorithms: BWA-backtrack (for reads ≤100 bp), BWA-SW (for longer reads with local alignment), and BWA-MEM (the current standard, suitable for 70 bp – 1 Mb reads). BWA-MEM is the most widely used for WGS and WES alignment in cancer genomics pipelines and is distributed with the Broad GATK best-practices workflow.

## Used by

- Used to align paired tumor/normal WGS reads to hg19 for 28 metastatic neuroendocrine neoplasms in the BC Cancer POG program; downstream SNV/indel calling performed by Strelka, SV calling by ABySS/Trans-ABySS [PMID:40328872](../papers/40328872.md).
- Used for read alignment in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23) [PMID:24336570](../papers/24336570.md)
- BWA used to align paired-end 100-bp reads from low-pass whole-genome sequencing (1-3x) of four FFPE prostate needle biopsies to hg19 as a proof-of-principle for CNA burden measurement in diagnostic biopsies [PMID:25024180](../papers/25024180.md)
- Used for sequence alignment in the MSK-IMPACT pipeline for 69 matched CRC primary/metastasis trios. [PMID:25164765](../papers/25164765.md)
- Used for read alignment to GRCh37-lite in Ewing sarcoma WGS study (112 tumors with matched germline) [PMID:25223734](../papers/25223734.md)
- Used for WES read alignment to GRCh37/hg19 in nccRCC study (167 primary tumors, 140 tumor-normal pairs) [PMID:25401301](../papers/25401301.md)
- Used for read alignment in WES pipeline processing 29 AA CRC tumor/normal discovery exomes in the MSS African American CRC landscape study [PMID:25583493](../papers/25583493.md)
- BWA used to align reads to UCSC hg19 in 109 microdissected PDA WES samples prior to MuTect/VarScan variant calling. [PMID:25855536](../papers/25855536.md)
- BWA used together with Picard and Firehose at the Broad Institute to align reads from 320 melanoma WES and WGS samples to the reference genome. [PMID:26091043](../papers/26091043.md)
- BWA used for read alignment in whole-exome sequencing of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- BWA used for read alignment in targeted panel sequencing (MSK-IMPACT) of pancreatic cancer [PMID:26278805](../papers/26278805.md)
- BWA used for read alignment in whole-exome and whole-genome sequencing of colorectal cancer [PMID:26343386](../papers/26343386.md)
- Used to align paired-end whole-exome sequencing reads (BWA v0.5.9) to hg19 in a 42-patient CTCL study defining the mutational landscape of Sézary syndrome and mycosis fungoides [PMID:26551667](../papers/26551667.md).
- Used for alignment in whole-genome sequencing of 28 uveal melanoma samples with GRCh37 reference, followed by GATK indel realignment and base quality recalibration; enabled discovery of the recurrent [PLCB4](../genes/PLCB4.md) p.D630Y hotspot [PMID:26683228](../papers/26683228.md).
- Used for alignment of whole-genome sequencing reads to GRCh37-lite in 46 matched diagnostic/recurrence medulloblastoma samples; enabled characterization of massive genetic divergence between primary and recurrent tumours [PMID:26760213](../papers/26760213.md).
- BWA used for read alignment in the HGSC Mercury pipeline processing whole-exome sequencing data from 160 periampullary tumors on HiSeq 2000; followed by GATK recalibration and Atlas/PInDel variant calling [PMID:26804919](../papers/26804919.md)
- bwa v0.7.1 used for alignment of WES reads from 141 tumors of 56 men with metastatic CRPC ([prad_fhcrc](../datasets/prad_fhcrc.md)), followed by GATK indel realignment and MuTect somatic mutation calling. [PMID:26928463](../papers/26928463.md)
- BWA-MEM used for read realignment in 619 CRC FFPE tumor/normal WES pairs prior to SNV/indel calling with MuTect and Indelocator/Strelka [PMID:27149842](../papers/27149842.md)
- Used for read alignment in the [NSCLC](../cancer_types/NSCLC.md) pan-lung WES study covering 1,144 tumor/normal pairs (660 ADC + 484 SqCC) [PMID:27158780](../papers/27158780.md)
- BWA-MEM used to align tumour and matched-normal reads to hg19 for MSK-IMPACT sequencing in 62 uRCC tumours; average coverage 348x tumour / 280x normal. [PMID:27713405](../papers/27713405.md)
- BWA-MEM used for read alignment of 216 metastatic breast cancer whole-exome sequencing samples before GATK base recalibration and MuTect/Scalpel mutation calling [PMID:28027327](../papers/28027327.md).
- Used for read alignment in the TCGA esophageal/stomach multi-platform study across 164 oesophageal carcinomas and 359 gastric adenocarcinomas [PMID:28052061](../papers/28052061.md).
- Used BWA for short-read alignment to the reference genome in WGS/WES pipelines [PMID:28373299](../papers/28373299.md)
- BWA MEM used for alignment to hg19 in the MSK-IMPACT bioinformatics pipeline, followed by ABRA realignment and GATK base-quality recalibration [PMID:28481359](../papers/28481359.md)
- Used for alignment of whole-genome sequencing reads (Illumina HiSeq X10/2500/2000) in the ICGC cholangiocarcinoma study (n=71 WGS tumor/normal pairs) [PMID:28667006](../papers/28667006.md)
- BWA mem alignment to hg19 applied in the DLBCL whole-exome sequencing pipeline for 1001 tumors [PMID:28985567](../papers/28985567.md)
- BWA v0.7.15 used to align WES reads to hg19 for 15 Korean vulvar SCC tumor/normal pairs; followed by Picard v2.7.1 and Samtools v1.3.1 de-duplication and GATK v3.6 local realignment/BQSR [PMID:29422544](../papers/29422544.md)
- Used (v0.5.9) to align paired tumor/normal germline data from dbGaP to GRCh37-lite for the TCGA PanCancer Atlas germline and somatic driver analysis of 11,000 tumors across 33 cancer types [PMID:29625049](../papers/29625049.md).
- WES reads from 304 DLBCLs aligned to GRCh37 using BWA via Broad's Picard/Firehose pipeline; median tumor coverage 87.6× [PMID:29713087](../papers/29713087.md)
- Reads aligned with BWA as part of the WGS processing pipeline for the MSK pediatric cancer cohort [PMID:29670109](../papers/29670109.md)
- Reads from 11,139 tumor-normal whole-exome pairs aligned to hg38 (or hg19 for DLBCL) using BWA-MEM in the pan-cancer MSI MANTIS analysis [PMID:29850653](../papers/29850653.md)
- Used for small RNA-seq read alignment to miRBase (BWA mapping) and for MSK-IMPACT DNA read alignment to hg19/b37 in the HCA/HCC miRNA pilot study [PMID:30052636](../papers/30052636.md)
- BWA MEM used to align whole-exome sequencing reads from 622 [AML](../cancer_types/AML.md) tumor specimens in the Beat [AML](../cancer_types/AML.md) study ([aml_ohsu_2018](../datasets/aml_ohsu_2018.md)) [PMID:30333627](../papers/30333627.md)
- Used to map WES reads to hg19 (~100x tumor / ~60x normal coverage) for 58 matched tumor-blood pairs in the [GBM](../cancer_types/GBM.md) anti-PD-1 immunotherapy cohort ([gbm_columbia_2019](../datasets/gbm_columbia_2019.md)) [PMID:30742119](../papers/30742119.md)
- Used for read alignment in the pan-Asia cHCC-ICC integrative genomic study (WES: 173 tumors / 121 cases at mean 108×; WGS: 41 tumors / 37 cases; RNA-seq: 97 tumors / 77 cases) [PMID:31130341](../papers/31130341.md)
- Used to align reads to GRCh37 (BWA v0.7.15) for whole-exome sequencing of 27 metaplastic breast cancers ([MBC](../cancer_types/MBC.md)) at MSKCC [PMID:33863915](../papers/33863915.md)
- Used to align reads to hg19 (BWA-MEM v0.7.13) for reprocessing of WES/WGS data from 88 cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) samples spanning 10 published studies [PMID:34272401](../papers/34272401.md)
- Used for cfDNA alignment (BWA-MEM, GRCh37) in the MSK-ACCESS analytical validation and clinical deployment pipeline for 681 plasma samples from 617 patients [PMID:34145282](../papers/34145282.md)
- Used for GRCh37 alignment of whole-exome sequencing data from 168 prostate cancer brain metastasis samples ([prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md)) at median 258× target coverage [PMID:35504881](../papers/35504881.md)
- BWA-MEM used for b37 alignment of whole-exome and whole-genome sequencing data in the GLASS longitudinal diffuse glioma cohort (304 patients, 37 hospitals) [PMID:35649412](../papers/35649412.md)
- Used as BWA-MEM for alignment of whole-genome sequencing data (mean tumor coverage 94.56x) from 25 metastatic cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) lymph node specimens to GRCh38 [PMID:35982973](../papers/35982973.md)

## Notes

- BWA-MEM is the recommended algorithm for reads ≥70 bp; BWA-backtrack was standard for early Illumina CASAVA-era data.
- PCR duplicate marking (e.g., Picard MarkDuplicates, samblaster) is typically applied after BWA alignment.
- Output is SAM/BAM format; coordinate-sorted and indexed BAMs are required for most downstream tools.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26278805](../papers/26278805.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26551667](../papers/26551667.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26928463](../papers/26928463.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28985567](../papers/28985567.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29422544](../papers/29422544.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29670109](../papers/29670109.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29850653](../papers/29850653.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30052636](../papers/30052636.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30333627](../papers/30333627.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33863915](../papers/33863915.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35649412](../papers/35649412.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
