---
name: DLBCL Duke 2017 (Reddy et al.)
studyId: dlbcl_duke_2017
institution: Duke University / Broad Institute
size: 1001
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - fish
  - immunohistochemistry
  - sanger-sequencing
panels: []
tags:
  - dlbcl
  - large-b-cell-lymphoma
  - crispr-screen
  - cell-of-origin
  - prognostic-model
  - rituximab
processed_by: crosslinker
processed_at: 2026-05-15
---

# DLBCL Duke 2017 (Reddy et al.)

## Overview

Reddy et al. performed integrative whole-exome and transcriptome sequencing of 1001 newly-diagnosed [DLBCL](../cancer_types/DLBCLNOS.md) patients (502 with paired germline DNA) treated uniformly with rituximab-containing regimens. The study defined a comprehensive landscape of 150 recurrently mutated driver genes, characterized functional dependencies via a genome-wide CRISPR screen across six lymphoma cell lines, and built a multivariate prognostic model combining genetic alterations with cell-of-origin and MYC/BCL2 expression. Published in *Cell* (2017).

## Composition

- **1001 de novo DLBCL tumors** with whole-exome sequencing; 400 paired tumor-normal pairs from this study plus 102 previously published pairs for a total 502-pair primary discovery set.
- All cases treated with a [rituximab](../drugs/rituximab.md)-containing standard regimen (de facto R-CHOP); complete clinical annotation including IPI, response, overall survival, gender, age, stage, performance status, and extranodal sites.
- RNA-seq performed on 775 cases; 625 used in core integrative analysis.
- Cell-of-origin assignment via RNA-seq classifier: 313 ABC, 331 GCB, remainder unclassified.
- Cancer type: [DLBCL NOS](../cancer_types/DLBCLNOS.md).
- CRISPR screen: GeCKO v2 genome-wide library (~120,000 sgRNAs, 19,050 protein-coding genes) across six cell lines — three ABC DLBCL (LY3, TMD8, HBL1), two GCB DLBCL (SUDHL4, Pfeiffer), one Burkitt-like (BJAB).

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Agilent All Exon V5, ~75X coverage on Illumina HiSeq 2500
- [RNA-seq](../methods/rna-seq.md) — transcriptome profiling for cell-of-origin and expression analysis
- [MuTect](../methods/mutect.md) v1.1.4 — somatic variant calling
- [BWA](../methods/bwa.md) mem — alignment to hg19
- [EXCAVATOR](../methods/excavator-cnv.md) — copy-number variant calling
- [ANNOVAR](../methods/annovar.md) — variant annotation
- [FISH](../methods/fish.md) — MYC/BCL2 translocation detection
- [IHC](../methods/immunohistochemistry.md) — [IRF4](../genes/IRF4.md), [BCL6](../genes/BCL6.md), CD10 (Hans algorithm cell-of-origin)
- [Sanger sequencing](../methods/sanger-sequencing.md) — variant validation (1130 events, 61 genes, 90% concordance)

## Papers using this cohort

- [PMID:28985567](../papers/28985567.md) — Reddy et al., *Cell* (2017): Genetic and Functional Drivers of Diffuse Large B Cell Lymphoma.

## Notable findings derived from this cohort

- **150 recurrent driver genes** identified in DLBCL (mean 7.75 mutations per case); 27 newly implicated in DLBCL including [SPEN](../genes/SPEN.md), [KLHL14](../genes/KLHL14.md), and [MGA](../genes/MGA.md). [PMID:28985567](../papers/28985567.md)
- **20 driver genes differentially mutated** between ABC and GCB subtypes: [EZH2](../genes/EZH2.md), [SGK1](../genes/SGK1.md), [GNA13](../genes/GNA13.md), [SOCS1](../genes/SOCS1.md), [STAT6](../genes/STAT6.md), [TNFRSF14](../genes/TNFRSF14.md) enriched in GCB; [ETV6](../genes/ETV6.md), [MYD88](../genes/MYD88.md), [PIM1](../genes/PIM1.md), [TBL1XR1](../genes/TBL1XR1.md) enriched in ABC. [PMID:28985567](../papers/28985567.md)
- CRISPR screen identified **1956 essential genes** across at least one cell line; ABC-selective dependencies include [CARD11](../genes/CARD11.md), [MYD88](../genes/MYD88.md), [IKBKB](../genes/IKBKB.md), [IRF4](../genes/IRF4.md); GCB-selective include [XPO1](../genes/XPO1.md), [ZBTB7A](../genes/ZBTB7A.md), [TGFBR2](../genes/TGFBR2.md), [PTPN6](../genes/PTPN6.md). [PMID:28985567](../papers/28985567.md)
- **36% of DLBCL patients** harbor genetic alterations in 9 CRISPR-validated essential driver genes that are direct drug targets. [PMID:28985567](../papers/28985567.md)
- A **3-tier genomic risk classifier** integrating 150 driver genes with cell-of-origin, [MYC](../genes/MYC.md), and [BCL2](../genes/BCL2.md) expression outperforms IPI, cell-of-origin, and MYC/BCL2 dual-expressor models; validated on an independent 20% test set (p=8×10⁻⁵) and 5-fold cross-validation. [PMID:28985567](../papers/28985567.md)
- Mutations associated with poorer [OS](../cancer_types/OS.md) across all DLBCL: [MYC](../genes/MYC.md), [CD79B](../genes/CD79B.md), [ZFAT](../genes/ZFAT.md). Favorable: [NF1](../genes/NF1.md), [SGK1](../genes/SGK1.md). [PMID:28985567](../papers/28985567.md)
- Within GCB DLBCL: [EZH2](../genes/EZH2.md) mutations associated with better survival; within ABC DLBCL: [KLHL14](../genes/KLHL14.md), [BTG1](../genes/BTG1.md), [PAX5](../genes/PAX5.md), [CDKN2A](../genes/CDKN2A.md) alterations associated with poorer survival. [PMID:28985567](../papers/28985567.md)

## Sources

- cBioPortal study ID: dlbcl_duke_2017
- Interactive web tool: dlbcl.davelab.org

*This page was processed by **crosslinker** on **2026-05-15**.*
