---
name: TCGA Lung Adenocarcinoma (LUAD)
studyId: luad_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 230
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
  - lung-adenocarcinoma
  - luad
  - tcga
  - multi-platform
  - non-small-cell-lung-cancer
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# TCGA Lung Adenocarcinoma (LUAD)

## Overview

Multi-platform molecular characterization of 230 resected, treatment-naive lung adenocarcinomas by The Cancer Genome Atlas (TCGA) Research Network, combined with 182 previously published cases (n=412 for driver discovery). The study identified 18 significantly mutated genes, nominated novel drivers including RIT1 and MGA, and defined three transcriptional subtypes (TRU, PI, PP). The fraction of LUAD cases with a defined RTK/RAS/RAF activating event was raised from 62% to 76%.

## Composition

- Cancer type: lung adenocarcinoma ([LUAD](../cancer_types/LUAD.md))
- 230 primary, treatment-naive resected tumors with matched normal tissue; 81% former/current smokers
- Median follow-up 19 months; 163 alive at last follow-up
- Statistical pool for driver discovery: n=412 (TCGA n=230 + prior published n=182)
- Low-pass WGS on n=93 tumor/germline pairs (average 36 gene–gene/inter-gene rearrangements; chromothripsis 6%)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): tumor mean coverage 97.6×, germline 95.8×
- [whole-genome-seq](../methods/whole-genome-seq.md): low-pass on n=93
- [rna-seq](../methods/rna-seq.md): mRNA expression
- miRNA-seq
- [hm450-methylation-array](../methods/hm450-methylation-array.md): DNA methylation
- [affymetrix-snp6](../methods/affymetrix-snp6.md): somatic copy-number
- [rppa](../methods/rppa.md): reverse-phase protein arrays (n=181)

## Papers using this cohort

- [PMID:25079552](../papers/25079552.md) — TCGA Research Network 2014, comprehensive molecular profiling of lung adenocarcinoma

## Notable findings derived from this cohort

- Mean somatic mutation rate 8.87 mutations/Mb (median 5.78); 18 significantly mutated genes identified by MutSig2CV across n=412 tumors [PMID:25079552](../papers/25079552.md)
- RIT1 activating mutations (2%, Q79-residue cluster) and NF1 loss-of-function mutations (11%) nominated as novel RTK/RAS/RAF drivers; with focal MET and ERBB2 amplifications, 76% of LUAD now carry a defined RTK/RAS/RAF event (up from 62%) [PMID:25079552](../papers/25079552.md)
- MGA loss-of-function mutations (8%) are mutually exclusive with focal MYC amplification (P=0.04), revealing a novel MYC-pathway activation mechanism [PMID:25079552](../papers/25079552.md)
- MET exon 14 skipping in 4% (10/230); U2AF1 S34F mutations drive 129 alternative splicing events including CTNNB1 [PMID:25079552](../papers/25079552.md)
- Three transcriptional subtypes defined: TRU (terminal respiratory unit, EGFR/fusion-enriched, favorable prognosis), PI (proximal-inflammatory, NF1+TP53), PP (proximal-proliferative, KRAS+STK11) [PMID:25079552](../papers/25079552.md)
- CIMP-H methylation cluster shows hypermethylation of WNT pathway genes and CDKN2A; MYC overexpression associated with CIMP-H (P=0.003) [PMID:25079552](../papers/25079552.md)

## Sources

- cBioPortal studyId: luad_tcga_pub
- TCGA Data Portal

*This page was processed by **entity-page-writer** on **2026-05-11**.*
