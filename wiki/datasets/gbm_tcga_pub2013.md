---
name: TCGA Glioblastoma 2013 (Publication Freeze)
studyId: gbm_tcga_pub2013
institution: The Cancer Genome Atlas (TCGA) — 17 contributing sites
size: 543
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - rppa
  - hm27-methylation-array
  - hm450-methylation-array
  - illumina-goldengate
panels: []
tags:
  - tcga
  - glioblastoma
  - multi-omics
  - molecular-subtypes
  - g-cimp
  - tert-promoter
  - egfr-rearrangements
processed_by: crosslinker
processed_at: 2026-05-09
---

# TCGA Glioblastoma 2013 (Publication Freeze)

## Overview

Multi-platform genomic, transcriptomic, epigenomic, and proteomic dataset for 543 primary glioblastoma ([GBM](../cancer_types/GBM.md)) patients assembled by The Cancer Genome Atlas (TCGA), with data frozen on 2013-07-15. This 2013 publication freeze substantially expanded the 2008 TCGA GBM study by adding whole-exome sequencing (291 pairs), whole-genome sequencing (42 deep-coverage pairs), RNA-seq (164 transcriptomes), expanded DNA methylation arrays, and reverse-phase protein arrays (214 samples, 171 antibodies). The corresponding cBioPortal study is `gbm_tcga_pub2013`. Primary publication: Brennan et al. *Cell* 2013.

## Composition

- **Cancer type:** [GBM](../cancer_types/GBM.md) — primary glioblastoma multiforme.
- **Samples:** 543 primary GBM patients accrued from 17 TCGA contributing sites, diagnosed 1989–2011.
- **Demographics:** median age 59.6 years; M:F = 1.6 (333:209).
- **Survival:** median [OS](../cancer_types/OS.md) 13.9 months; 2-year survival 22.5%; 5-year 5.3%.
- **Treatment:** 40% (217/543) received concurrent TMZ + radiation; 50.2% of those diagnosed ≥2002.
- **[IDH1](../genes/IDH1.md) mutation frequency:** 6% (28/423 with adequate coverage). [PMID:24120142](../papers/24120142.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 291 tumor/normal pairs; Agilent SureSelect 50 Mb hybrid capture; 138× mean target coverage; Illumina GA2000/HiSeq; 98% SNV validation rate.
- [whole-genome-seq](../methods/whole-genome-seq.md) — 42 deep-coverage tumor/normal pairs; structural variant callers [breakdancer](../methods/breakdancer.md) and [bambam](../methods/bambam.md).
- [rna-seq](../methods/rna-seq.md) — 164 transcriptomes; analyzed with [prada](../methods/prada.md) for fusion detection.
- [rppa](../methods/rppa.md) — 214 samples, 171 antibodies; pathway-level protein and phosphoprotein profiling.
- [hm27-methylation-array](../methods/hm27-methylation-array.md) — 283 samples (91 reanalyzed).
- [hm450-methylation-array](../methods/hm450-methylation-array.md) — 76 samples in publication freeze; 113 in re-analysis.
- [illumina-goldengate](../methods/illumina-goldengate.md) — DNA methylation, 238 samples.
- DNA copy-number arrays (aCGH) — 492 samples; SCNA peaks by [gistic](../methods/gistic.md).
- Significance calling: [mutsig](../methods/mutsig.md) and [invex](../methods/invex.md); mutual exclusivity: [memo](../methods/memo.md).

## Papers using this cohort

- [PMID:24120142](../papers/24120142.md) — Brennan CW et al., "The Somatic Genomic Landscape of Glioblastoma", *Cell* 2013.

## Notable findings derived from this cohort

- 71 significantly mutated genes identified by MutSig + InVEx, including the novel driver [LZTR1](../genes/LZTR1.md) (mutated in 10 samples) and known drivers [EGFR](../genes/EGFR.md), [PTEN](../genes/PTEN.md), [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), [NF1](../genes/NF1.md), [RB1](../genes/RB1.md), [IDH1](../genes/IDH1.md), [PDGFRA](../genes/PDGFRA.md). [PMID:24120142](../papers/24120142.md)
- [EGFR](../genes/EGFR.md) is altered in 57% of GBM; EGFRvIII (exon 2–7 deletion) at ≥10% TAF in 11%; diverse co-existing alteration forms (EGFRvIII, C-terminal deletions, Δ12–13, point mutations) suggest intratumoral heterogeneity will complicate single-agent targeting. [PMID:24120142](../papers/24120142.md)
- [TERT](../genes/TERT.md) promoter mutations (C228T/C250T) detected in 84% of deep-coverage WGS cases; all non-TERT-mutant cases harbored [ATRX](../genes/ATRX.md) mutations, defining a binary telomere-maintenance dichotomy. [PMID:24120142](../papers/24120142.md)
- [MGMT](../genes/MGMT.md) promoter methylation (48.5% of cohort) predicts [temozolomide](../drugs/temozolomide.md) response specifically in the classical transcriptomic subtype (P=0.01) but not in proneural, mesenchymal, or neural subtypes. [PMID:24120142](../papers/24120142.md)
- Proneural-subtype survival advantage is attributable to the G-CIMP+ epigenotype, not the transcriptomic subtype per se; non-G-CIMP proneural tumors behave like other subtypes. [PMID:24120142](../papers/24120142.md)
- RPPA data reveal non-linear genotype-to-signaling relationships: RTK-amplified samples show lower downstream phospho-AKT/S6K/MAPK; PI3K-mutant samples show lower AKT activity than PI3K-WT — complicating pathway-level therapeutic rationale. [PMID:24120142](../papers/24120142.md)

## Sources

- cBioPortal study: `gbm_tcga_pub2013`
- [PMID:24120142](../papers/24120142.md) — primary publication
- Data freeze date: 2013-07-15

*This page was processed by **crosslinker** on **2026-05-09**.*
