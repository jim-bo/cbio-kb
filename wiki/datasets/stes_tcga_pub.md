---
name: TCGA Esophageal and Stomach Cancers (STES, Nature 2017)
studyId: stes_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 559
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-sequencing
  - whole-genome-sequencing
  - snp-array
  - rna-seq
  - mirna-seq
  - dna-methylation-array
  - rppa
panels: []
tags:
  - TCGA
  - esophageal-cancer
  - gastric-cancer
  - escc
  - esca
  - stad
  - multi-platform
  - integrated
processed_by: crosslinker
processed_at: 2026-05-14
---

# TCGA Esophageal and Stomach Cancers (STES, Nature 2017)

## Overview

The stes_tcga_pub dataset is the combined esophageal-stomach TCGA publication cohort, produced by the TCGA Research Network through integrated multi-platform molecular profiling of oesophageal carcinomas (n=164: 90 [ESCC](../cancer_types/ESCC.md), 72 EAC, 2 undifferentiated) alongside 359 gastric adenocarcinomas and 36 gastroesophageal-junction ([GEJ](../cancer_types/GEJ.md)) adenocarcinomas. The study incorporated 77 additional STADs not present in the prior [stad_tcga_pub](../datasets/stad_tcga_pub.md) analysis. Published in Nature (2017), the dataset was specifically assembled to compare oesophageal squamous cell carcinoma ([ESCC](../cancer_types/ESCC.md)) with oesophageal adenocarcinoma ([ESCA](../cancer_types/ESCA.md)/EAC) and gastric adenocarcinoma ([STAD](../cancer_types/STAD.md)), demonstrating that EAC is molecularly indistinguishable from chromosomally-unstable gastric cancer.

## Composition

- **164 oesophageal carcinomas:** 90 [ESCC](../cancer_types/ESCC.md), 72 EAC ([ESCA](../cancer_types/ESCA.md); 61 definite + 11 probable), 2 undifferentiated.
- **359 gastric adenocarcinomas** ([STAD](../cancer_types/STAD.md)) as comparator (including 77 STADs not in original [stad_tcga_pub](../datasets/stad_tcga_pub.md)).
- **36 GEJ adenocarcinomas** of indeterminate origin.
- Total: 559 samples across esophagus, GEJ, and stomach.
- Geographic distribution of ESCC: Vietnamese patients (n=41), Eastern European, South American, and US/Canadian patients.
- 322 oesophageal cases submitted to the [BCR](../genes/BCR.md); 185 qualified by pathology/molecular QC; 171 entered genomic analysis after expert re-review.

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Agilent SureSelect Human All Exon V5 (Broad Institute, STAD-labelled) or Nimblegen SeqCap EZ Human Exome Library v3.0 + custom IDT viral probes (Washington University, ESCA-labelled).
- Low-pass (6–8×) [whole-genome sequencing](../methods/whole-genome-seq.md) on 51 oesophageal cancers.
- SNP-array copy-number profiling on [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md).
- DNA methylation on Illumina [HumanMethylation450 (HM450)](../methods/hm450-methylation-array.md).
- [mRNA-seq](../methods/rna-seq.md) and [miRNA-seq](../methods/mirna-seq.md).
- [Reverse-phase protein array](../methods/rppa.md) (RPPA) on 113 tumors.
- Integrative clustering via [iCluster](../methods/icluster.md); significantly mutated genes by [MutSigCV2.0](../methods/mutsig.md); recurrent SCNAs by [GISTIC 2.0](../methods/gistic.md); allelic copy number/purity/ploidy by [ABSOLUTE](../methods/absolute.md); mutation signatures by [Bayesian NMF](../methods/bayesian-nmf.md).

## Papers using this cohort

- [PMID:28052061](../papers/28052061.md) — TCGA Research Network 2017. Comprehensive molecular characterization of 164 oesophageal carcinomas compared to 395 gastroesophageal adenocarcinomas; established molecular distinctness of ESCC vs EAC, three ESCC molecular subtypes, and molecular equivalence of EAC with CIN gastric cancer.

## Notable findings derived from this cohort

- EAC and ESCC are molecularly distinct across all platforms: ESCC resembles squamous carcinomas of head/neck and lung, while EAC is indistinguishable from chromosomally-unstable (CIN) gastric adenocarcinoma [PMID:28052061](../papers/28052061.md).
- Three ESCC molecular subtypes defined: ESCC1 (NRF2-pathway/classical squamous; [NFE2L2](../genes/NFE2L2.md), [KEAP1](../genes/KEAP1.md), [SOX2](../genes/SOX2.md)/[TP63](../genes/TP63.md) amplification); ESCC2 (NOTCH/PI3K/immune-infiltrated; [NOTCH1](../genes/NOTCH1.md), [CDK6](../genes/CDK6.md) amplification); ESCC3 (PI3K-activated/[SMARCA4](../genes/SMARCA4.md)/[KMT2D](../genes/KMT2D.md) mutant, US/Canada-restricted) [PMID:28052061](../papers/28052061.md).
- Significantly mutated genes — ESCC: [TP53](../genes/TP53.md), [NFE2L2](../genes/NFE2L2.md), [KMT2D](../genes/KMT2D.md), [ZNF750](../genes/ZNF750.md), [NOTCH1](../genes/NOTCH1.md), [TGFBR2](../genes/TGFBR2.md). Significantly mutated genes — EAC: [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), [ARID1A](../genes/ARID1A.md), [SMAD4](../genes/SMAD4.md), [ERBB2](../genes/ERBB2.md) [PMID:28052061](../papers/28052061.md).
- [ERBB2](../genes/ERBB2.md) altered in 32% of EACs vs 3% of ESCCs; [CCND1](../genes/CCND1.md) amplified in 57% of ESCC vs 15% of EAC; [CDKN2A](../genes/CDKN2A.md) inactivated in 76% of both histologies [PMID:28052061](../papers/28052061.md).
- No aetiological role for HPV in ESCC; HPV-transcript levels resembled HPV-negative HNSCC [PMID:28052061](../papers/28052061.md).
- APOBEC mutation signatures enriched in ESCC vs EAC (p=5e-5); [NFE2L2](../genes/NFE2L2.md) mutations enriched in Vietnamese ESCC patients (24% vs 6% in others, p=0.017) [PMID:28052061](../papers/28052061.md).
- 71/72 EACs classified as CIN per TCGA gastric subtyping; integrative clustering showed no separation between EAC and CIN gastric tumors — supporting treatment as a single disease entity [PMID:28052061](../papers/28052061.md).

## Sources

- cBioPortal study: stes_tcga_pub
- Published: TCGA Research Network, Nature 2017.

*This page was processed by **crosslinker** on **2026-05-14**.*
