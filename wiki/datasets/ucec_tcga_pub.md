---
name: Endometrial Carcinoma — TCGA (2013)
studyId: ucec_tcga_pub
institution: The Cancer Genome Atlas
size: 373
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - 450k-methylation-array
  - affymetrix-snp6
panels: []
tags:
  - UCEC
  - uterine endometrial carcinoma
  - endometrial cancer
  - USC
  - TCGA
processed_by: crosslinker
processed_at: 2026-05-09
---

# Endometrial Carcinoma — TCGA (2013)

## Overview

The Cancer Genome Atlas integrated genomic, transcriptomic, and proteomic characterization of 373 endometrial carcinomas (307 endometrioid, 53 serous, 13 mixed histology), published in Nature 2013. The study proposed a four-category molecular classification that refines histology-based subtyping and may guide post-surgical adjuvant therapy decisions. [PMID:23636398](../papers/23636398.md)

## Composition

- 373 endometrial carcinomas with matched germline DNA: 307 endometrioid, 53 serous, and 13 mixed-histology cases; median follow-up 32 months (range 1–195 months); 21% recurred and 11% died at time of analysis. [PMID:23636398](../papers/23636398.md)
- Cancer types: [UCEC](../cancer_types/UCEC.md) (uterine endometrioid carcinoma), [UEC](../cancer_types/UEC.md), and [USC](../cancer_types/USC.md) (uterine serous carcinoma). [PMID:23636398](../papers/23636398.md)
- Whole-exome sequencing performed on 248 tumor/normal pairs (≥20× depth); low-pass paired-end whole-genome sequencing on 106–107 tumors (mean depth 6×); MSI testing on all samples using seven repeat loci. [PMID:23636398](../papers/23636398.md)

## Assays / panels (linked)

- [affymetrix-snp6](../methods/affymetrix-snp6.md) — SCNAs on 363 samples with [gistic](../methods/gistic.md) recurrent-event calling. [PMID:23636398](../papers/23636398.md)
- [whole-exome-seq](../methods/whole-exome-seq.md) — 248 tumor/normal pairs at ≥20× depth. [PMID:23636398](../papers/23636398.md)
- [rna-seq](../methods/rna-seq.md) — mRNA on 333 tumors; microRNA on 367; RPPA protein expression on 293. [PMID:23636398](../papers/23636398.md)
- [450k-methylation-array](../methods/450k-methylation-array.md) — Illumina Infinium 450K on all 373 tumors. [PMID:23636398](../papers/23636398.md)
- Integrated analyses: MEMo (mutual exclusivity), iCluster, PARADIGM pathway clustering, SuperCluster consensus algorithm. [PMID:23636398](../papers/23636398.md)

## Papers using this cohort

- [PMID:23636398](../papers/23636398.md) — The Cancer Genome Atlas Research Network, "Integrated genomic characterization of endometrial carcinoma," *Nature* 2013.

## Notable findings derived from this cohort

- Four integrated molecular subgroups: [POLE](../genes/POLE.md) ultramutated (n=17, ~7%; 232×10⁻⁶ mut/Mb), MSI hypermutated (n=65; 18×10⁻⁶ mut/Mb), copy-number low endometrioid (n=90; 2.9×10⁻⁶ mut/Mb), and copy-number high serous-like (n=60; 2.3×10⁻⁶ mut/Mb). [PMID:23636398](../papers/23636398.md)
- [POLE](../genes/POLE.md) exonuclease-domain hotspots Pro286Arg and Val411Leu define the ultramutated subgroup (100% mutated, Q=4.2×10⁻²³) and are associated with significantly better progression-free survival (log-rank P=0.02). [PMID:23636398](../papers/23636398.md)
- Copy-number high (serous-like) tumors share molecular features with high-grade serous ovarian carcinoma and basal-like breast carcinoma: [TP53](../genes/TP53.md) mutations (~90–91%), extensive SCNAs, focal amplifications of [MYC](../genes/MYC.md), [ERBB2](../genes/ERBB2.md), [CCNE1](../genes/CCNE1.md), [FGFR3](../genes/FGFR3.md), and [SOX17](../genes/SOX17.md), and significantly worse progression-free survival (log-rank P=0.003). [PMID:23636398](../papers/23636398.md)
- 93% of endometrioid tumors harbored PI(3)K/AKT pathway alterations; [PTEN](../genes/PTEN.md) mutated in 84% of MSS endometrioid and 94% of POLE-ultramutated; [CTNNB1](../genes/CTNNB1.md) mutated in 52% of copy-number-low MSS endometrioid. [PMID:23636398](../papers/23636398.md)
- Novel recurrently mutated gene [ARID5B](../genes/ARID5B.md) (SWI/SNF-related ARID-family chromatin remodeller) identified: 23.1% MSI vs. 5.6% MSS endometrioid vs. 0% serous. [RPL22](../genes/RPL22.md) frameshift indels almost exclusively in the MSI group (36.9%). [PMID:23636398](../papers/23636398.md)
- MEMo identified a mutually exclusive WNT-axis module of [CTNNB1](../genes/CTNNB1.md), [KRAS](../genes/KRAS.md), and [SOX17](../genes/SOX17.md) in copy-number-low tumors; novel recurrent SOX17 mutations at Ala96Gly and Ser403Ile (8% in this subgroup). [PMID:23636398](../papers/23636398.md)
- Low-pass WGS on 106 tumors found recurrent translocations involving BCL family members ([BCL2](../genes/BCL2.md), [BCL7A](../genes/BCL7A.md), [BCL9](../genes/BCL9.md), [BCL2L11](../genes/BCL2L11.md)) in 5/106 cases, all predicted in-frame. [PMID:23636398](../papers/23636398.md)

## Sources

- DOI: 10.1038/nature12113

*This page was processed by **crosslinker** on **2026-05-09**.*
