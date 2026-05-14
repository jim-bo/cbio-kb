---
name: University of Cologne Small Cell Lung Cancer 2015
studyId: sclc_ucologne_2015
institution: University of Cologne / German Cancer Research Center
size: 110
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
  - small-cell-lung-cancer
  - sclc
  - whole-genome-sequencing
  - tumor-suppressor
  - neuroendocrine
processed_by: crosslinker
processed_at: 2026-05-14
---

# University of Cologne Small Cell Lung Cancer 2015

## Overview

One hundred ten small cell lung cancer ([SCLC](../cancer_types/SCLC.md)) whole genomes from 152 fresh-frozen clinical specimens collected under IRB approval; 42 were excluded for insufficient DNA quality/quantity. At the time of publication, this was the first comprehensive somatic whole-genome analysis of [SCLC](../cancer_types/SCLC.md) and remains the largest whole-genome SCLC cohort. Most cases were treatment-naive; only 5 were obtained at relapse. Complementary assays included RNA-seq (n=81), Affymetrix SNP 6.0 arrays (n=142), and an independent validation cohort of 112 samples (28 exomes + 84 targeted).

## Composition

- **Cancer type:** [SCLC](../cancer_types/SCLC.md) (Small Cell Lung Cancer); primary lung n=106, metastatic n=4 among the WGS cases; median tumor content 84%.
- **Sample count:** 110 tumor + matched normal WGS pairs passing QC; 152 total specimens collected.
- **Clinical fields:** treatment status (naive vs relapsed), smoking history (median 45 pack-years among smokers; known for 88%), follow-up (median 69 months; 31% alive at last follow-up), pathology by ≥2 independent pathologists with IHC.
- **WGS:** Illumina HiSeq 2000 (TruSeq DNA PCR-free libraries, paired-end 2×100 bp, ≥30× tumor and normal); reference genome NCBI37/hg19; BWA v0.6.1-r104 alignment.
- **Transcriptome:** RNA-seq on 81 specimens (71 overlapping WGS + 10 additional).
- **Copy number:** Affymetrix SNP 6.0 arrays on 142 specimens (103 of WGS + 39 additional).
- **Validation cohort:** 28 fresh-frozen exomes + 9 SCLC cell lines (prior published data) + 75 fresh-frozen/FFPE samples sequenced with a 22-gene custom Agilent SureDesign targeted panel (≥200× coverage).
- **Mouse models:** 8 SCLC tumors from Trp53;Rb1 double-knockout and Trp53;Rb1;Rbl2 triple-knockout mice analyzed by WES (n=6) or WGS (n=2).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — primary cohort, ≥30× coverage.
- [whole-exome-seq](../methods/whole-exome-seq.md) — validation cohort fresh-frozen (28 samples + mouse tumors).
- [rna-seq](../methods/rna-seq.md) — transcriptome sequencing on 81 specimens; neuroendocrine subtype definition.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy number profiling on 142 specimens.
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — 22-gene custom validation panel on FFPE samples.
- [immunohistochemistry](../methods/immunohistochemistry.md) — chromogranin A, synaptophysin, CD56, Ki67; protein-level validation of key drivers.

## Papers using this cohort

- [PMID:26168399](../papers/26168399.md) — George et al. 2015, "Comprehensive genomic profiles of small cell lung cancer," *Nature*.

## Notable findings derived from this cohort

- Bi-allelic inactivation of [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) is obligatory in SCLC: found in 100% and 93% of non-chromothriptic tumors respectively, often through complex genomic rearrangements; mutation burden averages 8.62 nonsynonymous mutations/Mb with a heavy-smoking C>A transversion signature [PMID:26168399](../papers/26168399.md).
- NOTCH-family genes ([NOTCH1](../genes/NOTCH1.md)–4) are recurrently inactivated in 25% of human SCLC; mouse TKO models confirm Notch activation suppresses SCLC initiation and neuroendocrine differentiation and extends survival [PMID:26168399](../papers/26168399.md).
- Recurrent oncogenic [TP73](../genes/TP73.md) rearrangements (introns 1–3 breakpoints) produce dominant-negative N-terminally truncated isoforms (p73Δex2/3) in 7% of cases; total [TP73](../genes/TP73.md) somatic alteration rate 13% [PMID:26168399](../papers/26168399.md).
- Two chromothriptic tumors with wild-type [RB1](../genes/RB1.md) showed [CCND1](../genes/CCND1.md) overexpression as an alternative Rb-pathway inactivation mechanism; SCLC subclonal diversity threefold lower than lung adenocarcinoma (p=0.00023) [PMID:26168399](../papers/26168399.md).

## Sources

- cBioPortal study: `sclc_ucologne_2015`

*This page was processed by **crosslinker** on **2026-05-14**.*
