---
name: WCM Soft Tissue Myoepithelial Carcinoma WGS Study (2022)
studyId: stmyec_wcm_2022
institution: Weill Cornell Medicine
size: 2
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - myoepithelial-carcinoma
  - soft-tissue-sarcoma
  - structural-variants
  - chromoplexy
  - gene-fusions
  - rare-tumors
  - low-tmb
processed_by: crosslinker
processed_at: 2026-05-05
---

# WCM Soft Tissue Myoepithelial Carcinoma WGS Study (2022)

## Overview

Institutional case series from Weill Cornell Medicine providing the first whole-genome sequencing (WGS) characterization of soft tissue myoepithelial carcinomas (MECs). Two male patients (ages 27 and 37) contributed 12 total tumor samples (primary plus metastatic/recurrent) profiled by WES (mean coverage 98.5x) and WGS (22–29x tumor coverage). RNA-seq was performed on one sample per patient for fusion validation. The dataset is deposited to cBioPortal as `stmyec_wcm_2022`.

## Composition

- 2 patients with soft tissue [MYEC](../cancer_types/MYEC.md); 12 total tumor samples.
- WES (mean 98.5x coverage) on all 12 samples; WGS on primary tumor from each patient (Patient 1: 29x tumor/25x normal; Patient 2: 22x tumor/15x normal).
- RNA-seq on one sample per patient for fusion gene validation.
- Key clinical fields: age at diagnosis, sex, primary vs metastatic/recurrent sample designation, [SMARCB1](../genes/SMARCB1.md) and [SMARCA2](../genes/SMARCA2.md) IHC status.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — all 12 samples, mean 98.5x coverage
- [whole-genome-seq](../methods/whole-genome-seq.md) — primary tumor from each patient, 22–29x
- [rna-seq](../methods/rna-seq.md) — one sample per patient for fusion validation
- FISH — confirmatory [EWSR1](../genes/EWSR1.md) rearrangement testing

## Papers using this cohort

- [PMID:36577525](../papers/36577525.md) — Cyrta et al., *Cold Spring Harbor Molecular Case Studies* 2022. Whole-genome characterization of myoepithelial carcinomas of the soft tissue.

## Notable findings derived from this cohort

- Both MECs displayed very low tumor mutation burden (mean 1.35 mutations/Mb, range 0.43–2.98), consistent with fusion-driven oncogenesis and absence of targetable point mutations by WES [PMID:36577525](../papers/36577525.md).
- Patient 1 harbored a novel [ASCC2](../genes/ASCC2.md)::[GGNBP2](../genes/GGNBP2.md) in-frame fusion, homozygous [SMARCB1](../genes/SMARCB1.md) deletion, and biallelic [NF1](../genes/NF1.md) loss, all arising from a single >30-way biallelic chromoplexy event involving chromosomes 17, 19, and 22 — detectable only by WGS [PMID:36577525](../papers/36577525.md).
- Patient 2 harbored an [EWSR1](../genes/EWSR1.md)::[KLF15](../genes/KLF15.md) rearrangement and high-level (>10 copy) [ELK4](../genes/ELK4.md) amplification via double minute, also identified by WGS [PMID:36577525](../papers/36577525.md).
- COSMIC Signature 3 (HR-deficiency-associated) contributed 36.8% and 17.4% of SNVs in MEC1 and MEC2 respectively, despite no detectable somatic HR pathway alterations [PMID:36577525](../papers/36577525.md).

## Sources

- cBioPortal study: `stmyec_wcm_2022`
- Associated publication: [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
