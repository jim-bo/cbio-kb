---
name: Pindel
slug: pindel
kind: method
canonical_source: corpus
unverified: true
tags: [indel-calling, structural-variant, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Pindel

## Overview

Pindel is a pattern growth algorithm for detecting break points of large deletions, medium-sized insertions, inversions, tandem duplications, and other structural variants at single-base resolution from paired-end short-read sequencing data. It is particularly sensitive for detecting insertion/deletion events that are difficult to call with standard short-read aligners.

## Used by

- Used in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases, hg19) alongside [crest](../methods/crest.md) and [delly](../methods/delly.md) for somatic SV detection; contributed to identifying structural rearrangements including [BRAF](../genes/BRAF.md) fusions in the MAPK-pathway-driven pilocytic astrocytoma cohort [PMID:23817572](../papers/23817572.md)
- Used for small insertion/deletion detection in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23), complementing MuTect for SNV calling [PMID:24336570](../papers/24336570.md)
- PInDel used for indel detection in the HGSC Mercury pipeline processing whole-exome sequencing data from 160 periampullary tumors; detected ELF3 frameshift/nonsense inactivating mutations [PMID:26804919](../papers/26804919.md)
- Used for indel detection in the plasmacytoid-variant bladder cancer WES discovery cohort; contributed to identifying CDH1 frameshift truncating mutations. [PMID:26901067](../papers/26901067.md)
- Used as one of three somatic variant callers in the MSK-IMPACT pipeline (union of MuTect, Pindel, GATK somatic indel detector) for SNV and indel detection across 10,945 tumors [PMID:28481359](../papers/28481359.md)
- Applied for somatic indel detection in MET500 whole-exome sequencing data (500 metastatic solid tumors, GRCh37/hg19 alignment) as part of the bioinformatics pipeline alongside VarScan2 and ANNOVAR [PMID:28783718](../papers/28783718.md)
- One of seven callers in the TCGA MC3 pipeline; made the most indel calls overall, but >130K calls clustered in two samples indicating sample-specific artifacts; used Pindel-priority merging for complex indels [PMID:29596782](../papers/29596782.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Specialized in detecting events that confound standard alignment-based variant callers, including medium-to-large indels.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26901067](../papers/26901067.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:28783718](../papers/28783718.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
