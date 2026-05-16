---
name: UCSF Cutaneous Squamous Cell Carcinoma Meta-Analysis Cohort (UCSF, npj Genomic Med 2021)
studyId: cscc_ucsf_2021
institution: University of California, San Francisco
size: 88
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
panels: []
tags:
  - cscc
  - cutaneous-squamous-cell-carcinoma
  - meta-analysis
  - uv-mutagenesis
  - driver-discovery
  - immunosuppression
  - rdeb
  - xeroderma-pigmentosum
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# UCSF Cutaneous Squamous Cell Carcinoma Meta-Analysis Cohort (UCSF, npj Genomic Med 2021)

## Overview

Reanalyzed whole-exome / whole-genome sequencing dataset aggregated from 10 prior published studies of cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) with publicly available raw sequencing data. Chang and Shain at UCSF uniformly reprocessed 105 tumors using a harmonized bioinformatic pipeline (BWA-MEM v0.7.13, MuTect2 v4.1.2.0, Pindel v0.2.5, CNVkit); 17 were excluded after QC for low neoplastic cell content, low reference coverage, sample mismatch, or tumor contamination, leaving 88 tumors for downstream driver-discovery analyses. The reanalyzed somatic mutation calls were deposited in cBioPortal as `cscc_ucsf_2021`. Reference genome: hg19. [PMID:34272401](../papers/34272401.md)

## Composition

- 88 CSCC tumors retained after QC (from 105 aggregated across 10 source studies: Durinck 2011, Wang 2011, South 2014, Zheng 2014, Cammareri 2016, Chitsazzadeh 2016, Yilmaz 2017, Cho 2018, Inman 2018, Ji 2020).
- Cancer type: cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)).
- Five clinical/etiologic subtypes by mutational-signature analysis: xeroderma pigmentosum (XP), sporadic, immunosuppressed without azathioprine, immunosuppressed on azathioprine, and recessive dystrophic epidermolysis bullosa (RDEB).
- Tumor cellularity range: 12%–99%; mean sequencing coverage: 12.4×–498×; mean callable footprint 91.2% of target bases (range 52.3%–~100%). [PMID:34272401](../papers/34272401.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) and whole-genome sequencing sourced from 10 prior publications; uniformly reprocessed with a harmonized pipeline.
- Alignment: [BWA-MEM](../methods/bwa.md) v0.7.13; deduplication with [GATK](../methods/gatk.md) v4.1.2.0 and Picard v4.1.2.0.
- SNV calling: [MuTect2](../methods/mutect.md) v4.1.2.0 annotated with Funcotator v4.1.2.0.
- Indel calling: [Pindel](../methods/pindel.md) v0.2.5.
- CNA calling: [CNVkit](../methods/cnvkit.md) in reference mode with per-study panels of normals.
- Driver discovery: [MutSig](../methods/mutsig.md), [LOFsigrank](../methods/lofsigrank.md), [dN/dS](../methods/dndscv.md), [OncodriveFML](../methods/oncodrivefml.md); cross-referenced with [cancerhotspots.org](../methods/cancer-hotspots.md) and focal-CNA analysis.
- Per-sample callable footprint quantified with [Footprints](../methods/footprints.md) software. [PMID:34272401](../papers/34272401.md)

## Papers using this cohort

- [PMID:34272401](../papers/34272401.md) — Chang and Shain, *npj Genomic Medicine* 2021: Meta-analysis nominating 30 driver genes in CSCC across NOTCH (79.5%), p53 (71.1%), cell-cycle (38.6%), SWI/SNF (38.6%), Hippo (37.3%), stress-response (32.5%), and MAPK/PI3K (31.3%) pathways; four newly nominated genes mutated in >10% of tumors: EP300, PBRM1, USP28, and CHUK. [PMID:34272401](../papers/34272401.md)

## Notable findings derived from this cohort

- 30 cancer driver genes nominated in CSCC; defining features: NOTCH-pathway loss-of-function in 79.5% of tumors ([NOTCH1](../genes/NOTCH1.md) 55.4%, [NOTCH2](../genes/NOTCH2.md) 36.1%); p53-pathway in 71.1% ([TP53](../genes/TP53.md) 66.3%). [PMID:34272401](../papers/34272401.md)
- Four genes mutated in >10% of tumors not previously implicated in CSCC by other studies: [EP300](../genes/EP300.md) (21.7%), [PBRM1](../genes/PBRM1.md) (12%), [USP28](../genes/USP28.md) (12%), [CHUK](../genes/CHUK.md) (10.8%). [PMID:34272401](../papers/34272401.md)
- [CASP8](../genes/CASP8.md) mutations (22.9%) significantly enriched in RDEB-CSCC (recessive dystrophic epidermolysis bullosa), consistent with a role in inflammatory-cytokine-induced apoptosis in chronically blistered skin. [PMID:34272401](../papers/34272401.md)
- [CDKN2A](../genes/CDKN2A.md) (34.9%), including focal homozygous deletions; [FAT1](../genes/FAT1.md) (30.1%); [ARID2](../genes/ARID2.md) (27.7%); [HRAS](../genes/HRAS.md) (9.6%) with canonical Q61 and G12/G13 hotspots. [PMID:34272401](../papers/34272401.md)
- XP tumors had high TMB with high C>T at CC dipyrimidines but lacked canonical signature 7; azathioprine-treated immunosuppressed tumors carried high COSMIC signature 32 burdens. [PMID:34272401](../papers/34272401.md)
- Authors note the dataset does not yet reach driver-discovery saturation; cancer genes mutated in <15% of tumors cannot be reliably detected in this cohort size. [PMID:34272401](../papers/34272401.md)

## Sources

- cBioPortal study `cscc_ucsf_2021`.
- Chang D, Shain AH. *The landscape of driver mutations in cutaneous squamous cell carcinoma.* npj Genomic Medicine. 2021. [PMID:34272401](../papers/34272401.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
