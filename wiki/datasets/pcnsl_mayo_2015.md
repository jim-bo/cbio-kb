---
name: "PCNSL Mayo Clinic 2015 (Chapuy et al.)"
studyId: pcnsl_mayo_2015
institution: "Mayo Clinic / University of Virginia"
size: 19
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - array-cgh-agilent-1m
panels: []
tags:
  - primary-central-nervous-system-lymphoma
  - diffuse-large-b-cell-lymphoma
  - nf-kb-pathway
  - myd88
  - copy-number
processed_by: crosslinker
processed_at: 2026-05-14
---

# PCNSL Mayo Clinic 2015 (Chapuy et al.)

## Overview

Comprehensive genomic characterization of 19 immunocompetent primary central nervous system lymphoma ([PCNSL](../cancer_types/PCNSL.md)) cases from the Mayo Clinic Tumor Registry and the University of Virginia. Published 2015 (PMID:25991819). The study combined array-CGH, whole-exome sequencing, mate-pair sequencing, targeted sequencing, Sanger validation, and FISH to define the genomic landscape of [PCNSL](../cancer_types/PCNSL.md) versus systemic DLBCL. aCGH microarray data deposited in GEO under accession GSE28952.

## Composition

- **N = 19** immunocompetent [PCNSL](../cancer_types/PCNSL.md) patients (HIV−, EBV−), newly diagnosed, disease confined to the CNS.
- **Cancer type:** [PCNSL](../cancer_types/PCNSL.md); comparisons made throughout to systemic [DLBCLNOS](../cancer_types/DLBCLNOS.md).
- **Tissue source:** frozen tissue (7 cases) or FFPE (12 cases); 3 frozen samples required whole-genome amplification due to low yield.
- **Matched normal:** 9 of 19 biopsies provided tumor-free tissue for matched-normal validation sequencing.

## Assays / panels (linked)

- [array-cgh-agilent-1m](../methods/array-cgh-agilent-1m.md) — 18 cases; Human Genome 244A + Sureprint G3 (Agilent); CNA calling via Nexus RANK segmentation; CNVs filtered using TCAG database plus 10 in-house HapMap controls.
- [whole-exome-seq](../methods/whole-exome-seq.md) — 10 cases; SureSelect 50 Mb capture; 100 bp paired-end on HiSeq2000; mean 65.6M mapped reads, median 80% of exome at ≥30× coverage. SNVs called with SomaticSniper; indels with [gatk-somatic-indel-detector](../methods/gatk-somatic-indel-detector.md); annotated by snpEFF/PolyPhen-2 via TREAT workflow.
- [mate-pair-seq](../methods/mate-pair-seq.md) — structural rearrangement detection.
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — Ion Torrent PGM for [MYD88](../genes/MYD88.md) coding regions (~2,005× average depth); Sanger sequencing for CARD11/CD79B/PRKCD/TNFAIP3 variants.
- [fish](../methods/fish.md) — interphase FISH for IGH-BCL6, [PRKCD](../genes/PRKCD.md), and [TOX](../genes/TOX.md) rearrangements.

## Papers using this cohort

- [PMID:25991819](../papers/25991819.md) — Genome-wide analysis uncovers novel recurrent alterations in primary central nervous system lymphoma; primary discovery study for this cohort.

## Notable findings derived from this cohort

- BCR/TLR/NF-κB pathway altered in >90% of [PCNSL](../cancer_types/PCNSL.md) when integrating mutation and CNA data. [PMID:25991819](../papers/25991819.md)
- [MYD88](../genes/MYD88.md) activating mutations in 79% of cases (predominantly L265P) — ~2× the prevalence in nodal ABC-DLBCL — making MYD88-dependent signaling a particularly attractive [PCNSL](../cancer_types/PCNSL.md) target. [PMID:25991819](../papers/25991819.md)
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) 9p21.3 deletion in 83% of cases (homozygous in 55%), making it the most common CNA in the cohort. [PMID:25991819](../papers/25991819.md)
- PCNSL-specific biallelic inactivation of [PRKCD](../genes/PRKCD.md) (splice-donor mutations + missense) and homozygous deletion of [TOX](../genes/TOX.md) (8q12) — neither event reported recurrently in systemic DLBCL. [PMID:25991819](../papers/25991819.md)
- [PRDM1](../genes/PRDM1.md) 6q21 deletion (55% of cases) associated with shorter overall survival (log-rank P=0.001) in univariate analysis. [PMID:25991819](../papers/25991819.md)

## Sources

- cBioPortal study: `pcnsl_mayo_2015`
- GEO: GSE28952 (aCGH microarray data)

*This page was processed by **crosslinker** on **2026-05-14**.*
