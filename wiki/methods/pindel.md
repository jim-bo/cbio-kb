---
name: Pindel
slug: pindel
kind: method
canonical_source: corpus
unverified: true
tags: [indel-calling, structural-variant, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-21
---

# Pindel

## Overview

Pindel is a pattern growth algorithm for detecting break points of large deletions, medium-sized insertions, inversions, tandem duplications, and other structural variants at single-base resolution from paired-end short-read sequencing data. It is particularly sensitive for detecting insertion/deletion events that are difficult to call with standard short-read aligners.

## Used by

- Used in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases, hg19) alongside [crest](../methods/crest.md) and [delly](../methods/delly.md) for somatic SV detection; contributed to identifying structural rearrangements including [BRAF](../genes/BRAF.md) fusions in the MAPK-pathway-driven pilocytic astrocytoma cohort [PMID:23817572](../papers/23817572.md)
- Used for small insertion/deletion detection in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23), complementing MuTect for SNV calling [PMID:24336570](../papers/24336570.md)
- PInDel used for indel detection in the HGSC Mercury pipeline processing whole-exome sequencing data from 160 periampullary tumors; detected [ELF3](../genes/ELF3.md) frameshift/nonsense inactivating mutations [PMID:26804919](../papers/26804919.md)
- Used for indel detection in the plasmacytoid-variant bladder cancer WES discovery cohort; contributed to identifying [CDH1](../genes/CDH1.md) frameshift truncating mutations. [PMID:26901067](../papers/26901067.md)
- Used as one of three somatic variant callers in the MSK-IMPACT pipeline (union of MuTect, Pindel, GATK somatic indel detector) for SNV and indel detection across 10,945 tumors [PMID:28481359](../papers/28481359.md)
- Applied for somatic indel detection in MET500 whole-exome sequencing data (500 metastatic solid tumors, GRCh37/hg19 alignment) as part of the bioinformatics pipeline alongside VarScan2 and ANNOVAR [PMID:28783718](../papers/28783718.md)
- One of seven callers in the TCGA MC3 pipeline; made the most indel calls overall, but >130K calls clustered in two samples indicating sample-specific artifacts; used Pindel-priority merging for complex indels [PMID:29596782](../papers/29596782.md)
- Used for germline indel calling (≥2-of-3 consensus or Pindel-unique ≥30× coverage / ≥20% VAF) and as one of seven somatic MC3 callers for the TCGA PanCancer Atlas 11,000-tumor germline/somatic analysis [PMID:29625049](../papers/29625049.md).
- Pindel used for FLT3-ITD detection from whole-exome sequencing of 622 [AML](../cancer_types/AML.md) specimens in the Beat [AML](../cancer_types/AML.md) study; results supplemented with a dedicated PCR/capillary-electrophoresis assay [PMID:30333627](../papers/30333627.md)
- Used to call somatic indels (Pindel v0.2.5) in reprocessed WES/WGS data from 88 [CSCC](../cancer_types/CSCC.md) tumors alongside MuTect2 for SNV calling [PMID:34272401](../papers/34272401.md)
- Pindel applied for structural variant and large indel detection in MSK-IMPACT sequencing of 46 [SCLC](../cancer_types/SCLC.md) PDX/CDX models [PMID:35440124](../papers/35440124.md).
- Used in [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) cWGTS pipeline for structural variant and indel detection from whole-genome sequencing in 114 pediatric/AYA solid tumor patients [PMID:35585047](../papers/35585047.md)
- Used for InDel calling in the OrigiMed CSYS 450-gene NGS panel pipeline across 10,194 Chinese solid-tumor patients alongside MuTect for SNVs; all variants manually reviewed in IGV [PMID:35871175](../papers/35871175.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Specialized in detecting events that confound standard alignment-based variant callers, including medium-to-large indels.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26901067](../papers/26901067.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28783718](../papers/28783718.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30333627](../papers/30333627.md)

- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35871175](../papers/35871175.md)

*This page was processed by **wiki-cli** on **2026-05-21**.*
