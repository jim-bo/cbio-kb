---
name: BCGSC Non-Hodgkin Lymphoma Genome and Exome Sequencing
studyId: nhl_bcgsc_2011
institution: BC Cancer Agency Genome Sciences Centre
size: 127
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - MRNA_EXPRESSION
panels: []
tags:
  - non-hodgkin-lymphoma
  - dlbcl
  - follicular-lymphoma
  - histone-modification
  - whole-genome-sequencing
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# BCGSC Non-Hodgkin Lymphoma Genome and Exome Sequencing

## Overview

Whole-genome, whole-exome, and transcriptome sequencing study of 127 B-cell non-Hodgkin lymphoma (NHL) tumor samples plus 10 DLBCL cell lines from the BC Cancer Agency Genome Sciences Centre. The study used a multi-platform design: 14 cases with matched tumor/normal whole-genome or whole-exome sequencing for discovery, and 113 additional cases with RNA-seq. Extensive Sanger and Illumina amplicon validation cohorts were used to confirm mutations in [KMT2D](../genes/KMT2D.md) (89 cases) and [MEF2B](../genes/MEF2B.md) (572 total samples across multiple NHL subtypes). Data are deposited at SRA (SRP001599) and dbGaP (phs000235.v2.p1).

## Composition

- Cancer types: [DLBCLNOS](../cancer_types/DLBCLNOS.md), [FL](../cancer_types/FL.md)
- 127 B-cell NHL tumors + 10 DLBCL cell lines
- 14 cases: matched tumor/normal [whole-genome-seq](../methods/whole-genome-seq.md) or [whole-exome-seq](../methods/whole-exome-seq.md)
- 113 additional cases: [rna-seq](../methods/rna-seq.md)
- KMT2D validation cohort: 89 cases (35 [FL](../cancer_types/FL.md), 37 DLBCL, 17 DLBCL cell lines) via Illumina amplicon resequencing
- MEF2B validation cohort: 261 FL, 259 DLBCL, 17 cell lines, 35 other NHL, 8 centroblasts via [sanger-sequencing](../methods/sanger-sequencing.md)
- Key clinical fields: COO subtype (GCB vs. ABC), histology (DLBCL vs. FL), survival

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — tumor/normal pairs for 14 discovery cases
- [whole-exome-seq](../methods/whole-exome-seq.md) — tumor/normal pairs for 14 discovery cases
- [rna-seq](../methods/rna-seq.md) — 113 additional NHL cases for transcriptome-level mutation calls
- [sanger-sequencing](../methods/sanger-sequencing.md) — MEF2B validation in 572 samples

## Papers using this cohort

- [PMID:21796119](../papers/21796119.md) — Morin et al. 2011, genome/exome sequencing revealing histone-modifier mutations in NHL

## Notable findings derived from this cohort

- [KMT2D](../genes/KMT2D.md) (MLL2) mutated in 89% (31/35) of FL and 32% (12/37) of DLBCL; 91% of mutations were inactivating (frameshift, nonsense, splice-site); bi-allelic inactivation in 8 FL cases [PMID:21796119](../papers/21796119.md)
- [MEF2B](../genes/MEF2B.md) recurrent non-synonymous mutations in 12.7% of DLBCL and 15.3% of FL; 59.4% of variants clustered at four residues (K4, Y69, N81, D83); restricted to GCB subtype [PMID:21796119](../papers/21796119.md)
- [GNA13](../genes/GNA13.md) mutated in 17% of DLBCL, restricted to GCB subtype (P = 2.28e-4); multiple nonsense mutations indicate tumor suppressor role [PMID:21796119](../papers/21796119.md)
- [EZH2](../genes/EZH2.md) Y641 hotspot mutations with allelic imbalance; novel sites A682G and A692V identified [PMID:21796119](../papers/21796119.md)
- 109 genes confirmed somatically mutated in ≥2 NHL cases; 26 genes with significant evidence of positive selection (FDR 0.03) [PMID:21796119](../papers/21796119.md)
- Mutual exclusion between ABC-enriched mutations ([MYD88](../genes/MYD88.md), [CD79B](../genes/CD79B.md)) and GCB-enriched mutations ([EZH2](../genes/EZH2.md), [GNA13](../genes/GNA13.md)) supports distinct molecular pathogenesis of COO subtypes [PMID:21796119](../papers/21796119.md)

## Sources

- [PMID:21796119](../papers/21796119.md) — Morin et al., "Frequent mutation of histone-modifying genes in non-Hodgkin lymphoma," *Nature* 2011
- SRA: SRP001599
- dbGaP: phs000235.v2.p1

*This page was processed by **entity-page-writer** on **2026-05-06**.*
