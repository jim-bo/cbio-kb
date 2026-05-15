---
name: BWA (Burrows-Wheeler Aligner)
slug: bwa
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, short-read, dna-seq, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# BWA (Burrows-Wheeler Aligner)

## Overview

BWA (Burrows-Wheeler Aligner) is a short-read alignment tool for mapping sequencing reads to a reference genome using the Burrows-Wheeler transform. It includes three algorithms: BWA-backtrack (for reads ≤100 bp), BWA-SW (for longer reads with local alignment), and BWA-MEM (the current standard, suitable for 70 bp – 1 Mb reads). BWA-MEM is the most widely used for WGS and WES alignment in cancer genomics pipelines and is distributed with the Broad GATK best-practices workflow.

## Used by

- Used to align paired tumor/normal WGS reads to hg19 for 28 metastatic neuroendocrine neoplasms in the BC Cancer POG program; downstream SNV/indel calling performed by Strelka, SV calling by ABySS/Trans-ABySS [PMID:24326773](../papers/24326773.md).
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
- bwa v0.7.1 used for alignment of WES reads from 141 tumors of 56 men with metastatic CRPC (prad_fhcrc), followed by GATK indel realignment and MuTect somatic mutation calling. [PMID:26928463](../papers/26928463.md)
- BWA-MEM used for read realignment in 619 CRC FFPE tumor/normal WES pairs prior to SNV/indel calling with MuTect and Indelocator/Strelka [PMID:27149842](../papers/27149842.md)
- Used for read alignment in the NSCLC pan-lung WES study covering 1,144 tumor/normal pairs (660 ADC + 484 SqCC) [PMID:27158780](../papers/27158780.md)
- BWA-MEM used to align tumour and matched-normal reads to hg19 for MSK-IMPACT sequencing in 62 uRCC tumours; average coverage 348x tumour / 280x normal. [PMID:27713405](../papers/27713405.md)
- BWA-MEM used for read alignment of 216 metastatic breast cancer whole-exome sequencing samples before GATK base recalibration and MuTect/Scalpel mutation calling [PMID:28027327](../papers/28027327.md).
- Used for read alignment in the TCGA esophageal/stomach multi-platform study across 164 oesophageal carcinomas and 359 gastric adenocarcinomas [PMID:28052061](../papers/28052061.md).

## Notes

- BWA-MEM is the recommended algorithm for reads ≥70 bp; BWA-backtrack was standard for early Illumina CASAVA-era data.
- PCR duplicate marking (e.g., Picard MarkDuplicates, samblaster) is typically applied after BWA alignment.
- Output is SAM/BAM format; coordinate-sorted and indexed BAMs are required for most downstream tools.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26278805](../papers/26278805.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26551667](../papers/26551667.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26928463](../papers/26928463.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
