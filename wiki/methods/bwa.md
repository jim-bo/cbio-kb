---
name: BWA (Burrows-Wheeler Aligner)
slug: bwa
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, short-read, dna-seq, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-14
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

## Notes

- BWA-MEM is the recommended algorithm for reads ≥70 bp; BWA-backtrack was standard for early Illumina CASAVA-era data.
- PCR duplicate marking (e.g., Picard MarkDuplicates, samblaster) is typically applied after BWA alignment.
- Output is SAM/BAM format; coordinate-sorted and indexed BAMs are required for most downstream tools.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
