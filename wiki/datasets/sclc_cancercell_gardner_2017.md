---
name: SCLC PDX Chemoresistance Cohort (Gardner 2017)
studyId: sclc_cancercell_gardner_2017
institution: Memorial Sloan Kettering Cancer Center / Johns Hopkins University
size: 10
reference_genome: GRCh38
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - MRNA_EXPRESSION
  - METHYLATION
panels: []
tags:
  - small-cell-lung-cancer
  - sclc
  - pdx
  - chemoresistance
  - ezh2
  - slfn11
  - epigenetics
processed_by: crosslinker
processed_at: 2026-05-14
---

# SCLC PDX Chemoresistance Cohort (Gardner 2017)

## Overview

10 paired patient-derived xenograft (PDX) models of small cell lung cancer ([SCLC](../cancer_types/SCLC.md)) from Memorial Sloan Kettering Cancer Center and Johns Hopkins University. Each model was serially treated in vivo with cisplatin/etoposide to derive matched chemonaive and chemoresistant tumors. The cohort was used to characterize transcriptomic and epigenetic mechanisms of acquired chemoresistance, focusing on [SLFN11](../genes/SLFN11.md) silencing via [EZH2](../genes/EZH2.md)-mediated H3K27me3 deposition. Raw data deposited in dbGaP under accession `phs001249.v1.p1`.

## Composition

- **10 paired [SCLC](../cancer_types/SCLC.md) PDX models** — chemonaive vs. acquired-chemoresistant; majority derived from chemonaive patients. Two models (MSK-LX40 and MSK-LX95) had matched normal DNA. Named models include JHU-LX102, SCRX-Lu149, JHU-LX44 (chemorefractory at baseline), and others.
- **Murine SCLC models** — Rb1/Trp53-null (DKO) and Rb1/Rbl2/Trp53-null (TKO) cell lines; chemonaive allograft TKO-A and its chemoresistant derivative TKO-AR.
- **SCLC cell lines** — NCI-H82, NCI-H446, NCI-H526 used for mechanistic experiments.
- **Clinical TMAs** — untreated SCLC (Vanderbilt Medical Center) and previously-treated SCLC (Case Western Reserve University) for [SLFN11](../genes/SLFN11.md) IHC validation.
- **Cancer types:** [SCLC](../cancer_types/SCLC.md).

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — paired chemonaive/resistant models; reads aligned to a custom human/mouse hybrid reference (GRCh38 + GRCm38.p3).
- [RNA-seq](../methods/rna-seq.md) — paired chemonaive/resistant models.
- [ChIP-seq](../methods/chip-seq.md) — [EZH2](../genes/EZH2.md), H3K27me3, and H3K27Ac in SCRX-Lu149 chemoresistant tumors.
- [ChIP-qPCR](../methods/chip-qpcr.md) — SLFN11 gene-body H3K27me3 quantification.
- [Immunohistochemistry](../methods/immunohistochemistry.md) — SLFN11 IHC H-score on clinical TMAs.

## Papers using this cohort

- [PMID:28196596](../papers/28196596.md) — Gardner et al. 2017, *Cancer Cell*: EZH2-mediated SLFN11 silencing drives acquired chemoresistance in SCLC PDX models; EZH2 inhibition (EPZ011989) restores chemosensitivity and synergizes with [irinotecan](../drugs/irinotecan.md) in vivo.

## Notable findings derived from this cohort

- Whole-exome sequencing of 10 paired SCLC PDX models revealed no recurrent acquired somatic mutations driving chemoresistance; resistant models retained parental [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) driver alterations [PMID:28196596](../papers/28196596.md).
- RNA-seq identified two mutually exclusive transcriptional resistance programs across 7/10 chemoresistant models: [SLFN11](../genes/SLFN11.md) downregulation (4/10 models) and [TWIST1](../genes/TWIST1.md) upregulation with cancer-testis antigen induction (3/10 models) [PMID:28196596](../papers/28196596.md).
- ChIP-seq in SCRX-Lu149 demonstrated that [EZH2](../genes/EZH2.md) and H3K27me3 spread across the SLFN11 gene body in chemoresistant tumors, with concurrent loss of H3K27Ac at the TSS; EPZ011989 (EZH2 inhibitor) reversed this epigenetic silencing and re-expressed SLFN11 [PMID:28196596](../papers/28196596.md).
- [TWIST1](../genes/TWIST1.md) induction accompanied EMT-like changes (E-cadherin loss) but functional experiments showed it is a biomarker rather than direct driver of acquired resistance [PMID:28196596](../papers/28196596.md).
- EPZ011989 combined with cisplatin/etoposide or irinotecan demonstrated potent combinatorial in vivo activity in SLFN11-high PDX models; single-agent EPZ had modest efficacy [PMID:28196596](../papers/28196596.md).

## Sources

- dbGaP accession: phs001249.v1.p1
- cBioPortal studyId: sclc_cancercell_gardner_2017
- [PMID:28196596](../papers/28196596.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
