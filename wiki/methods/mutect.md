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
processed_by: crosslinker
processed_at: 2026-05-14
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
- Used to call SNVs in pre-treatment urothelial carcinoma tumors (n=50), identifying [ERCC2](../genes/ERCC2.md) mutations enriched in [cisplatin](../drugs/cisplatin.md) responders. [PMID:25096233](../papers/25096233.md)
- Used to call somatic SNVs in matched primary/metastasis CRC trios (n=69) as part of the MSK-IMPACT analysis pipeline. [PMID:25164765](../papers/25164765.md)
- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) alongside other callers [PMID:25240281](../papers/25240281.md)
- Used alongside VarScan 2.2.5 for somatic variant calling in 78 gastric adenocarcinoma WES samples; identified 13,866 total somatic mutations including 8,558 missense and 576 nonsense variants [PMID:25583476](../papers/25583476.md)
- Used for somatic SNV and indel calling in the AA CRC WES pipeline (29 discovery tumor/normal pairs), contributing to identification of 20 significantly mutated genes in African American MSS CRC [PMID:25583493](../papers/25583493.md)
- Used for somatic SNV and indel calling (with OxoG artifact filtering) on 29 lymph-node metastases from cSCC patients sequenced with [DFCI-ONCOPANEL-1](../methods/DFCI-ONCOPANEL-1.md) (mean tumor coverage 82×); identified high UV mutation burden (~33 mut/Mb) and recurrent oncogenic alterations [PMID:25589618](../papers/25589618.md)

## Notes

- Requires matched tumor/normal BAM files; not designed for tumor-only mode in its original implementation.
- Sensitivity is maintained down to ~5% variant allele fraction under typical WES coverage (80–100×).
- All candidate variants are typically followed by validation with orthogonal methods (e.g., Sequenom, deep digital sequencing).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23685749](../papers/23685749.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25240281](../papers/25240281.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25589618](../papers/25589618.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
