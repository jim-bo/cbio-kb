---
name: Acral Melanoma TSAM Cohort (Liang 2017)
studyId: mel_tsam_liang_2017
institution: Vanderbilt University / Memorial Sloan Kettering Cancer Center
size: 34
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - STRUCTURAL_VARIANT
panels: []
tags:
  - acral-melanoma
  - melanoma
  - acrm
  - whole-exome-sequencing
  - whole-genome-sequencing
  - structural-variation
  - tert
  - pak1
processed_by: crosslinker
processed_at: 2026-05-14
---

# Acral Melanoma TSAM Cohort (Liang 2017)

## Overview

Integrated whole-exome sequencing, long-insert whole-genome sequencing (LIWG), and RNA-seq analysis of 38 acral lentiginous melanoma (ALM) tumors from 34 patients enrolled at Vanderbilt University and Memorial Sloan-Kettering Cancer Center. This rare sun-shielded melanoma subtype was characterized by a low UV-signature SNV burden and high structural variant (SV) burden. Key findings include frequent [TERT](../genes/TERT.md) aberrations (41%) and [PAK1](../genes/PAK1.md) copy gains (15%) in BRAF/NRAS wild-type tumors. Raw sequencing deposited in dbGaP under accession `phs001036.v1.p1`.

## Composition

- **38 ALM tumors from 34 patients** — 3 patients contributed multiple tumors (patient 25: two metastases; patient 29: primary + two metastases; patient 34: primary + metastasis). Median tumor cellularity 50%.
- **Tumor types:** primary acral lentiginous melanomas and paired metastases; subsite includes plantar foot, fingers, palms.
- **Comparator:** TCGA cutaneous melanoma ([SKCM](../cancer_types/SKCM.md)) cohort used for landscape comparison.
- **Cancer types:** [ACRM](../cancer_types/ACRM.md).

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — 33 paired tumor/constitutional; 1 tumor-only. Somatic SNV calling required 2-of-3 callers (Seurat Q>30, [MuTect](../methods/mutect.md), [Strelka](../methods/strelka.md)).
- [Whole-genome sequencing](../methods/whole-genome-seq.md) — long-insert (~900 bp) LIWG for structural variant and CNV detection in 31 patients.
- [RNA-seq](../methods/rna-seq.md) — 33 patients; fusions detected with [TopHat-Fusion](../methods/tophat-fusion.md); differential expression via [Cufflinks/Cuffdiff](../methods/tophat-cufflinks.md) and DESeq2.
- [Sanger sequencing](../methods/sanger-sequencing.md) — [TERT](../genes/TERT.md) promoter interrogation in 28 patients (poorly covered by exome baits).
- Alignment: [BWA](../methods/bwa.md) (DNA), [STAR](../methods/star.md) (RNA).

## Papers using this cohort

- [PMID:28373299](../papers/28373299.md) — Liang et al. 2017, *Nature Genetics*: integrated multi-omic characterization of acral lentiginous melanoma; frequent TERT aberrations and [PAK1](../genes/PAK1.md) copy gains define this rare subtype.

## Notable findings derived from this cohort

- Low SNV burden (median 42 somatic coding mutations per tumor) but high structural variant burden (median 31 somatic breakpoints per patient across 74% of patients); UV mutational signature largely absent (C>T at dipyrimidines only 39.4%) [PMID:28373299](../papers/28373299.md).
- Only 29% of patients carried canonical BRAF/NRAS driver mutations, far below the rate in cutaneous melanoma; [NF1](../genes/NF1.md) loss in 12% [PMID:28373299](../papers/28373299.md).
- [TERT](../genes/TERT.md) aberrations (copy gains, promoter mutations, translocations, missense, or germline events) in 41% (14/34) of patients; Telomerase Inhibitor IX produced ≥75% loss of viability in two primary ALM cell lines carrying TERT alterations but not in normal melanocytes [PMID:28373299](../papers/28373299.md).
- [PAK1](../genes/PAK1.md) focal copy gains in 15% (5/34) of patients, all BRAF/NRAS wild-type; validated by real-time PCR in 4/5, supporting PAK1 as an alternative MAPK-pathway dysregulation route in triple-wild-type ALM [PMID:28373299](../papers/28373299.md).
- MAPK/PI3K pathway altered in 66% of patients; cell-cycle ([CDK4](../genes/CDK4.md)/[CDKN2A](../genes/CDKN2A.md)) in 51%; telomere maintenance ([TERT](../genes/TERT.md)) in 37%; apoptosis/senescence ([MDM2](../genes/MDM2.md)/[TP53](../genes/TP53.md)) in 17% [PMID:28373299](../papers/28373299.md).
- Among 22 patients receiving immune checkpoint blockade, three complete responders had low mutation (<75) and neo-antigen (<60) burdens — opposite of the cutaneous melanoma pattern [PMID:28373299](../papers/28373299.md).
- Most-rearranged genes: [ADCY2](../genes/ADCY2.md) (21% of patients) and [CLPTM1L](../genes/CLPTM1L.md) (15%); all ADCY2/CLPTM1L rearrangements occurred in [BRAF](../genes/BRAF.md) wild-type tumors [PMID:28373299](../papers/28373299.md).

## Sources

- dbGaP accession: phs001036.v1.p1
- cBioPortal studyId: mel_tsam_liang_2017
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
