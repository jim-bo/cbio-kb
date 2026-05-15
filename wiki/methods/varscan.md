---
name: VarScan
slug: varscan
kind: method
canonical_source: corpus
unverified: true
tags:
  - variant-calling
  - somatic
  - bioinformatics
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# VarScan

## Overview

VarScan is a platform-independent variant detection tool for next-generation sequencing data. It uses a heuristic/statistic approach to call somatic mutations (SNVs and indels) and copy-number alterations in paired tumor-normal samples.

## Used by

- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) [PMID:25240281](../papers/25240281.md)
- Used alongside MuTect for somatic variant calling in 78 gastric adenocarcinoma WES samples; joint calling identified a high-clonality (HiC) subtype with distinct C>G mutational enrichment (25% vs. 9% in low-clonality; P=0.002) [PMID:25583476](../papers/25583476.md)
- Used for somatic variant calling in the AA CRC WES pipeline alongside MuTect, contributing to the mutational landscape analysis of 103 African American MSS colorectal cancers [PMID:25583493](../papers/25583493.md)
- VarScan used for INDEL calling in 109 microdissected PDA WES samples (≥8 reference reads, ≥3 variant reads); indels manually inspected in IGV before inclusion. [PMID:25855536](../papers/25855536.md)
- VarScan used for somatic variant calling in whole-exome sequencing of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- Used for indel calling in whole-genome sequencing of 46 matched primary/recurrent medulloblastoma samples alongside Strelka and MutationSeq; supported characterization of massively increased mutational burden (~5-fold) at recurrence [PMID:26760213](../papers/26760213.md).
- One of four mutation callers (MuTect, Indelocator, VarScan, RADIA) used in ≥2-caller consensus strategy for somatic variant detection in 820 TCGA diffuse glioma exomes [PMID:26824661](../papers/26824661.md)
- Used (as VarScan2) together with Sequenza to generate intersected copy-number profiles from anti-PD-1-treated melanoma WES data [PMID:26997480](../papers/26997480.md)
- VarScan2 v2.3.2 used for somatic SNV calling in MET500 whole-exome sequencing data (500 metastatic solid tumors, mean 180× tumor / 120× normal coverage, aligned to GRCh37/hg19 via Novoalign) [PMID:28783718](../papers/28783718.md)
- VarScan 2.3.7 applied as one of four somatic callers in intersection-based SNV detection for 68 paired melanoma WES biopsies in the CA209-038 nivolumab trial [PMID:29033130](../papers/29033130.md)

## Notes

- Commonly paired with MuTect and Strelka in multi-caller somatic variant detection pipelines.
- Corpus-derived slug; not in cBioPortal gene panel ontology.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26997480](../papers/26997480.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28783718](../papers/28783718.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
