---
name: "SKCM TCGA 2015 (TCGA Melanoma Working Group)"
studyId: skcm_tcga_pub_2015
institution: "TCGA Research Network (Broad Institute + 14 tissue source sites)"
size: 333
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-sequencing
  - rna-seq
  - mirna-seq
  - 450k-methylation-array
  - affymetrix-snp6
  - rppa
panels: []
tags:
  - skin-cutaneous-melanoma
  - tcga
  - uv-signature
  - braf
  - nras
  - nf1
  - tumor-microenvironment
  - immunotherapy-biomarker
processed_by: crosslinker
processed_at: 2026-05-14
---

# SKCM TCGA 2015 (TCGA Melanoma Working Group)

## Overview

Comprehensive multi-platform genomic characterization of 333 cutaneous melanomas (67 primary, 266 metastatic) from 331 adult patients across 14 tissue source sites, published by the TCGA Network in *Cell* 2015 (PMID:26091043). The study applied six molecular platforms to a core set of 199 samples and whole-exome sequencing to 320 samples. Cutaneous melanoma carries the highest mutation burden of any TCGA tumor type (mean 16.8 mutations/Mb), driven primarily by UV-signature C>T substitutions. Raw data available at GDAC Firehose `stddata__2013_11_14` and the TCGA [SKCM](../cancer_types/SKCM.md) Data Portal.

## Composition

- **N = 333** cutaneous melanoma samples from 331 adult patients; 67 (20%) primary, 266 (80%) metastatic.
- **Metastasis sites:** 160 regional lymph nodes, 52 regional skin/soft tissue, 35 distant.
- **Cancer type:** [SKCM](../cancer_types/SKCM.md).
- **Median primary thickness:** 2.7 mm (mean 4.9 mm).
- Complete six-platform data available for 199 samples; WES for 320 samples (318 with paired germline).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 320 samples; Agilent SureSelect Human All Exon v2.0 44 Mb; Illumina HiSeq 2×76 bp paired-end; ~87× mean exon coverage. Reads aligned with [bwa](../methods/bwa.md)/Picard/Firehose.
- [whole-genome-sequencing](../methods/whole-genome-sequencing.md) — deep WGS on 38 samples; low-pass WGS on 119 samples.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — DNA copy-number profiling on 333 samples; purity/ploidy via [absolute](../methods/absolute.md).
- [rna-seq](../methods/rna-seq.md) — mRNA sequencing on 331 samples (Illumina mRNA TruSeq, HiSeq 2000).
- [mirna-seq](../methods/mirna-seq.md) — microRNA sequencing on 323 samples.
- [450k-methylation-array](../methods/450k-methylation-array.md) — DNA methylation profiling on 333 samples (Illumina 450K).
- [rppa](../methods/rppa.md) — reverse-phase protein array (181 cancer-related proteins/phosphoproteins) on 202 samples.
- [sanger-sequencing](../methods/sanger-sequencing.md) — [TERT](../genes/TERT.md) promoter C228T/C250T PCR-Sanger sequencing in 115 samples.
- [mutsig](../methods/mutsig.md) — significantly mutated gene discovery (Q < 0.1).
- [icluster](../methods/icluster.md) — multi-platform integrative subtype discovery.
- [shatterseek](../methods/shatterseek.md) — complex structural rearrangement detection.

## Papers using this cohort

- [PMID:26091043](../papers/26091043.md) — TCGA Network, *Cell* 2015: genomic classification of cutaneous melanoma; primary discovery study for this cohort.

## Notable findings derived from this cohort

- Four genomic subtypes defined by dominant driver: [BRAF](../genes/BRAF.md) (52%), RAS (28%, predominantly [NRAS](../genes/NRAS.md)), [NF1](../genes/NF1.md) (14%), and Triple-WT (no hot-spot BRAF/RAS/NF1); all three named subtypes show UV-signature prevalence >90% while Triple-WT is only 30% UV-signature. [PMID:26091043](../papers/26091043.md)
- Mean mutation burden 16.8 mut/Mb — highest of any TCGA tumor type at the time; 76–84% of samples carry a UV mutational signature. [PMID:26091043](../papers/26091043.md)
- Three transcriptomic subclasses with prognostic significance: Immune (51%, favorable outcome), Keratin (31%, worst outcome), MITF-low (18%); high lymphocyte score + Immune subclass + high [LCK](../genes/LCK.md) expression form a tri-feature prognostic model (log-rank P=8.0e–6) in regional metastases. [PMID:26091043](../papers/26091043.md)
- [TERT](../genes/TERT.md) promoter C228T enriched in [BRAF](../genes/BRAF.md) (75%), RAS (72%), [NF1](../genes/NF1.md) (83%) subtypes but depleted in Triple-WT (6.7%), which activates [TERT](../genes/TERT.md) via amplification or structural rearrangement instead. [PMID:26091043](../papers/26091043.md)
- [KIT](../genes/KIT.md) mutations and 4q12 focal amplifications ([KIT](../genes/KIT.md)/[PDGFRA](../genes/PDGFRA.md)/[KDR](../genes/KDR.md)) enriched in Triple-WT subtype; [CD274](../genes/CD274.md) (PD-L1) focal amplifications in [BRAF](../genes/BRAF.md) subtype — each subtype presents distinct therapeutic opportunities. [PMID:26091043](../papers/26091043.md)
- 224 candidate fusion drivers identified; Triple-WT enriched for complex structural rearrangements (ShatterSeek p=0.00098) and driver fusions involving [AKT3](../genes/AKT3.md), [RAF1](../genes/RAF1.md), [MITF](../genes/MITF.md), and [HMGA2](../genes/HMGA2.md). [PMID:26091043](../papers/26091043.md)

## Sources

- cBioPortal study: `skcm_tcga_pub_2015`
- GDAC Firehose: `stddata__2013_11_14`
- TCGA [SKCM](../cancer_types/SKCM.md) Data Portal

*This page was processed by **crosslinker** on **2026-05-14**.*
