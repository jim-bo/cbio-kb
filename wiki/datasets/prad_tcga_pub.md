---
name: Prostate Adenocarcinoma — TCGA 2015
studyId: prad_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 333
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - affymetrix-snp6
  - hm450-methylation-array
  - rppa
panels: []
tags:
  - prostate-cancer
  - PRAD
  - tcga
  - molecular-taxonomy
  - ets-fusions
  - multi-platform
processed_by: crosslinker
processed_at: 2026-05-14
---

# Prostate Adenocarcinoma — TCGA 2015

## Overview

Integrated multi-platform molecular characterization of 333 primary prostate adenocarcinomas ([PRAD](../cancer_types/PRAD.md)) from radical prostatectomy specimens, assembled by The Cancer Genome Atlas (TCGA) Research Network. The cohort (originally 425 cases, reduced to 333 after pathology and quality-control review) was profiled by whole-exome and whole-genome sequencing, SNP arrays, DNA methylation arrays, mRNA and miRNA sequencing, and reverse-phase protein arrays (RPPA). Reference genome hg19.

## Composition

- **333 primary prostate adenocarcinomas** (radical prostatectomy; final cohort after QC review from 425 initial cases).
- 19 matched non-malignant adjacent prostate samples profiled for methylation and RNA/miRNA expression.
- Cancer type: [PRAD](../cancer_types/PRAD.md) (prostate adenocarcinoma).
- Average follow-up under two years; outcomes analysis was not performed.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) (333 tumor/normal pairs)
- [whole-genome-seq](../methods/whole-genome-seq.md) (low-pass 100 pairs; high-pass 19 pairs)
- [affymetrix-snp6](../methods/affymetrix-snp6.md) (copy-number)
- [hm450-methylation-array](../methods/hm450-methylation-array.md)
- [rna-seq](../methods/rna-seq.md)
- [mirna-seq](../methods/mirna-seq.md) (330 samples)
- [rppa](../methods/rppa.md) (152 samples)
- [icluster](../methods/icluster.md) (integrative clustering)
- [mutsig](../methods/mutsig.md) (MutSigCV; significantly mutated genes)
- [gistic](../methods/gistic.md) (GISTIC 2.0; focal SCNAs)
- [absolute](../methods/absolute.md) (tumor purity estimation)

## Papers using this cohort

- [PMID:26544944](../papers/26544944.md) — The Cancer Genome Atlas Research Network 2015, "The Molecular Taxonomy of Primary Prostate Cancer," *Cell*.

## Notable findings derived from this cohort

- Seven mutually exclusive molecular subtypes capture 74% of primary prostate cancers: ETS-family fusions — [ERG](../genes/ERG.md) 46%, [ETV1](../genes/ETV1.md) 8%, [ETV4](../genes/ETV4.md) 4%, [FLI1](../genes/FLI1.md) 1% — and hotspot mutations in [SPOP](../genes/SPOP.md) 11%, [FOXA1](../genes/FOXA1.md) 3%, [IDH1](../genes/IDH1.md) 1% [PMID:26544944](../papers/26544944.md).
- Median mutational burden 0.94 mutations/Mb (~19 non-synonymous mutations/tumor); 13 significantly mutated genes at q < 0.1, including [SPOP](../genes/SPOP.md), [TP53](../genes/TP53.md), [FOXA1](../genes/FOXA1.md), [PTEN](../genes/PTEN.md), [MED12](../genes/MED12.md), [CDKN1B](../genes/CDKN1B.md), [ATM](../genes/ATM.md) [PMID:26544944](../papers/26544944.md).
- Homozygous [PTEN](../genes/PTEN.md) deletion in 15% — one of the highest rates across TCGA tumor types; [BRCA2](../genes/BRCA2.md) loss almost always co-occurred with [RB1](../genes/RB1.md) loss at 13q [PMID:26544944](../papers/26544944.md).
- DNA repair gene inactivation in 19% of tumors ([BRCA2](../genes/BRCA2.md), [BRCA1](../genes/BRCA1.md), [CDK12](../genes/CDK12.md), [ATM](../genes/ATM.md), [FANCD2](../genes/FANCD2.md), [RAD51C](../genes/RAD51C.md)), with therapeutic relevance for PARP inhibitors such as [olaparib](../drugs/olaparib.md) [PMID:26544944](../papers/26544944.md).
- [IDH1](../genes/IDH1.md) R132 mutations define a CIMP-like epigenetic subgroup with greater genome-wide hypermethylation than IDH1-mutant [GBM](../cancer_types/GBM.md) or [AML](../cancer_types/AML.md), associated with younger age and ETS/SPOP-wild-type status [PMID:26544944](../papers/26544944.md).
- PI3K/MAPK pathway lesions in ~25% of tumors; [AR](../genes/AR.md) splice variants including AR-V7 detectable at low levels in hormone-naive primary tumors [PMID:26544944](../papers/26544944.md).
- [SPOP](../genes/SPOP.md) and [FOXA1](../genes/FOXA1.md) mutations confer highest [AR](../genes/AR.md) transcriptional activity; SPOP-mutant tumors showed distinct co-mutation landscape (HEXA silencing, no ETS fusions) [PMID:26544944](../papers/26544944.md).

## Sources

- [PMID:26544944](../papers/26544944.md)
- TCGA data portal (prad_tcga_pub)

*This page was processed by **crosslinker** on **2026-05-14**.*
