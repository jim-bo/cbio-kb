---
name: TCGA Stomach Adenocarcinoma (STAD)
studyId: stad_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 295
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - METHYLATION
  - PROTEIN_LEVEL
panels: []
tags:
  - gastric-cancer
  - stomach-adenocarcinoma
  - stad
  - tcga
  - multi-platform
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# TCGA Stomach Adenocarcinoma (STAD)

## Overview

Multi-platform molecular characterization of 295 primary, treatment-naive gastric adenocarcinomas performed by The Cancer Genome Atlas (TCGA) Research Network. The study defines four molecular subtypes — EBV-positive, microsatellite instable (MSI), genomically stable (GS), and chromosomally instable (CIN) — providing a taxonomy for biomarker-stratified clinical trials in gastric cancer.

## Composition

- Cancer type: gastric/stomach adenocarcinoma ([STAD](../cancer_types/STAD.md))
- 295 treatment-naive patients (surgery); 77% profiled on all six molecular platforms
- Non-malignant gastric tissue controls: methylation n=27, expression n=29
- 107 tumor/germline pairs with low-pass whole-genome sequencing (<6×)
- Subtype distribution: EBV 9%, MSI 22%, GS 20%, CIN 50%

## Assays / panels (linked)

- [affymetrix-snp6](../methods/affymetrix-snp6.md): somatic copy-number
- [whole-exome-seq](../methods/whole-exome-seq.md): somatic mutations
- [hm450-methylation-array](../methods/hm450-methylation-array.md): DNA methylation
- [rna-seq](../methods/rna-seq.md): mRNA expression
- miRNA-seq
- [rppa](../methods/rppa.md): reverse-phase protein arrays
- [whole-genome-seq](../methods/whole-genome-seq.md): low-pass (<6×) on 107 pairs

## Papers using this cohort

- [PMID:25079317](../papers/25079317.md) — TCGA Research Network 2014, comprehensive molecular characterization of gastric adenocarcinoma

## Notable findings derived from this cohort

- Four-subtype classification: EBV-positive (9%), MSI (22%), GS (20%), CIN (50%); each subtype defined by a distinct molecular signature and therapeutic vulnerability profile [PMID:25079317](../papers/25079317.md)
- EBV-positive tumors: extreme CIMP, 9p24.1 amplification of JAK2/CD274/PDCD1LG2 (15%), PIK3CA mutations in 80%, supporting PD-L1/L2 immune-checkpoint blockade and JAK2 inhibition [PMID:25079317](../papers/25079317.md)
- MSI tumors: MLH1 promoter hypermethylation drives MSI; 37 significantly mutated genes after indel inclusion; BRAF V600E absent (unlike MSI colorectal cancer) [PMID:25079317](../papers/25079317.md)
- GS tumors: RHOA mutations in 15% and CLDN18-ARHGAP26/ARHGAP6 fusions in 15% are mutually exclusive and together affect 30% of GS cases; enriched for diffuse Lauren histology (73%) [PMID:25079317](../papers/25079317.md)
- CIN tumors: TP53 mutation in 71%; recurrent focal amplifications of ERBB2, KRAS, MYC, EGFR, CCNE1, CDK6, VEGFA [PMID:25079317](../papers/25079317.md)
- MET exon 2 skipping in 30% and exon 18/19 skipping in 17% across the full cohort [PMID:25079317](../papers/25079317.md)

## Sources

- cBioPortal studyId: stad_tcga_pub
- TCGA Data Portal

*This page was processed by **entity-page-writer** on **2026-05-11**.*
