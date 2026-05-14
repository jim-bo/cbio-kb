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
processed_by: crosslinker
processed_at: 2026-05-14
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
- EBV-positive tumors: extreme CIMP, 9p24.1 amplification of JAK2/CD274/PDCD1LG2 (15%), [PIK3CA](../genes/PIK3CA.md) mutations in 80%, supporting PD-L1/L2 immune-checkpoint blockade and [JAK2](../genes/JAK2.md) inhibition [PMID:25079317](../papers/25079317.md)
- MSI tumors: [MLH1](../genes/MLH1.md) promoter hypermethylation drives MSI; 37 significantly mutated genes after indel inclusion; [BRAF](../genes/BRAF.md) V600E absent (unlike MSI colorectal cancer) [PMID:25079317](../papers/25079317.md)
- GS tumors: [RHOA](../genes/RHOA.md) mutations in 15% and CLDN18-ARHGAP26/ARHGAP6 fusions in 15% are mutually exclusive and together affect 30% of GS cases; enriched for diffuse Lauren histology (73%) [PMID:25079317](../papers/25079317.md)
- CIN tumors: [TP53](../genes/TP53.md) mutation in 71%; recurrent focal amplifications of [ERBB2](../genes/ERBB2.md), [KRAS](../genes/KRAS.md), [MYC](../genes/MYC.md), [EGFR](../genes/EGFR.md), [CCNE1](../genes/CCNE1.md), [CDK6](../genes/CDK6.md), [VEGFA](../genes/VEGFA.md) [PMID:25079317](../papers/25079317.md)
- [MET](../genes/MET.md) exon 2 skipping in 30% and exon 18/19 skipping in 17% across the full cohort [PMID:25079317](../papers/25079317.md)
- Used as validation cohort for [BRCA2](../genes/BRCA2.md) mutation-survival analysis in gastric adenocarcinoma; 289 cases with 28 BRCA2-mutant tumors contributed to pooled log-rank P=0.03 survival association, and [ERBB4](../genes/ERBB4.md) kinase-domain mutations (p.V744L, p.774N/G) and [NRG1](../genes/NRG1.md)–ERBB4 mutual exclusivity confirmed in this cohort [PMID:25583476](../papers/25583476.md)

## Sources

- cBioPortal studyId: stad_tcga_pub
- TCGA Data Portal

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
