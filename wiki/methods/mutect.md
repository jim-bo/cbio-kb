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
processed_by: wiki-cli
processed_at: 2026-05-11
---

# MuTect

## Overview

MuTect is a Bayesian statistical framework for the sensitive and specific detection of somatic single-nucleotide variants (SNVs) in paired tumor/normal sequencing data. Developed at the Broad Institute, it uses a two-sample likelihood model to distinguish somatic mutations from germline variants and sequencing artifacts, with particular attention to low-allele-fraction variants in impure tumor samples. MuTect is widely applied in cancer exome and genome sequencing pipelines, typically paired with Indelocator for indel detection.

## Used by

- Applied alongside Indelocator, dRanger, BreakPointer, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors; detected 356,136 somatic base-pair mutations across the cohort (mean 33 non-silent exonic per primary tumor) [PMID:23622249](../papers/23622249.md)
- Used for somatic SNV calling in 149 esophageal adenocarcinoma WES pairs (and 16 WGS pairs) alongside Indelocator; median 104 non-silent coding mutations per tumor at median genome-wide frequency 9.9/Mb [PMID:23525077](../papers/23525077.md)
- Used alongside SomaticSniper for somatic SNV calling in 60 ACC tumor/normal pairs (55 exome + 5 WGS, Illumina HiSeq 2000); yielded 710 validated nonsynonymous mutations across 643 genes [PMID:23685749](../papers/23685749.md)
- Used to call somatic SNVs from whole-exome data of 45 [BRAF](../genes/BRAF.md) V600 metastatic melanoma FFPE tumors (DeCOG cohort) aligned to hg19 via the Broad Picard/Firehose pipeline [PMID:24265153](../papers/24265153.md).
- Applied for somatic point-mutation calling in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23); mutation validation rate informed by independent re-genotyping [PMID:24336570](../papers/24336570.md)
- Applied for somatic point-mutation calling on the Illumina HiSeq whole-exome arm (13 paired samples) of the rhabdomyosarcoma cohort (147 total tumor/normal pairs); combined with MutSig for significantly mutated gene identification [PMID:24436047](../papers/24436047.md)
- Applied for somatic point-mutation calling on 130 TCGA bladder carcinoma WES tumor/normal pairs; identified mean 302 exonic mutations per sample and APOBEC TpC signature representing 51% of all mutations [PMID:24476821](../papers/24476821.md)
- Used to call SNVs in pre-treatment urothelial carcinoma tumors (n=50), identifying ERCC2 mutations enriched in cisplatin responders. [PMID:25096233](../papers/25096233.md)
- Used to call somatic SNVs in matched primary/metastasis CRC trios (n=69) as part of the MSK-IMPACT analysis pipeline. [PMID:25164765](../papers/25164765.md)

## Notes

- Requires matched tumor/normal BAM files; not designed for tumor-only mode in its original implementation.
- Sensitivity is maintained down to ~5% variant allele fraction under typical WES coverage (80–100×).
- All candidate variants are typically followed by validation with orthogonal methods (e.g., Sequenom, deep digital sequencing).

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
