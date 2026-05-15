---
name: Indelocator
slug: indelocator
kind: method
canonical_source: corpus
unverified: false
tags:
  - indel-calling
  - somatic-mutation
  - whole-exome-seq
  - whole-genome-seq
processed_by: wiki-cli
processed_at: 2026-05-14
---

# Indelocator

## Overview

Indelocator is a somatic indel (insertion/deletion) caller developed at the Broad Institute. It detects small insertions and deletions in tumor/normal paired sequencing data by comparing read alignments and applying statistical filters to identify somatic events. Indelocator is commonly run in tandem with MuTect (which handles SNVs) to provide a complete somatic small-variant callset for cancer genome studies.

## Used by

- Applied alongside MuTect, dRanger, BreakPointer, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors; total cohort had 356,136 somatic base-pair mutations with an average of 33 non-silent exonic mutations per primary tumor [PMID:23622249](../papers/23622249.md)
- Used for indel calling in 149 esophageal adenocarcinoma WGS/WES pairs alongside MuTect; median 104 non-silent coding mutations per tumor [PMID:23525077](../papers/23525077.md)
- Used to call somatic indels from whole-exome data of 45 [BRAF](../genes/BRAF.md) V600 metastatic melanoma FFPE tumors (DeCOG cohort) as part of the Broad Picard/Firehose pipeline alongside MuTect for SNVs [PMID:24265153](../papers/24265153.md).
- Used to call somatic indels in 50 muscle-invasive urothelial carcinoma tumors as part of the cisplatin-response WES study. [PMID:25096233](../papers/25096233.md)
- One of four mutation callers (MuTect, Indelocator, VarScan, RADIA) used in ≥2-caller consensus strategy for somatic indel detection in 820 TCGA diffuse glioma exomes [PMID:26824661](../papers/26824661.md)
- Used alongside Strelka for indel calling in 619 CRC FFPE tumor/normal WES pairs; concordant calls from both tools were retained to reduce false positives [PMID:27149842](../papers/27149842.md)
- Used alongside MuTect for indel calling in 1,144 NSCLC (660 lung ADC + 484 lung SqCC) tumor/normal exome pairs [PMID:27158780](../papers/27158780.md)

## Notes

- Designed for paired tumor/normal analysis; not intended for tumor-only calling.
- Typically used in conjunction with MuTect for comprehensive somatic SNV+indel discovery.
- Outputs feed into significance callers (e.g., MutSig) and manual validation workflows.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
