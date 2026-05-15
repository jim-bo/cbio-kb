---
name: ICGC Cholangiocarcinoma Multi-Omic Cohort 2017 (Jusakul et al.)
studyId: chol_icgc_2017
institution: International Cancer Genome Consortium (ICGC) PedBrain / multi-national (Singapore, Thailand, Romania, Italy, France, South Korea, Brazil, Taiwan, China, Japan)
size: 489
reference_genome: GRCh37/hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - targeted-dna-seq
  - snp-array-cn
  - 450k-methylation-array
  - microarray-gene-expression
panels: []
tags:
  - cholangiocarcinoma
  - multi-omic
  - ICGC
  - integrative-clustering
  - methylation
processed_by: crosslinker
processed_at: 2026-05-15
---

# ICGC Cholangiocarcinoma Multi-Omic Cohort 2017 (Jusakul et al.)

## Overview

The ICGC CCA cohort is the largest integrated multi-omic survey of cholangiocarcinoma to date, assembled by the International Cancer Genome Consortium across 10 countries. Jusakul et al. profiled 489 cholangiocarcinomas from patients spanning fluke-positive (132 *Opisthorchis viverrini*, 1 *Clonorchis sinensis*) and fluke-negative etiologies (including HBV/HCV-positive and PSC-positive subsets). Tumors were collected prior to any systemic therapy and staged using AJCC 7th edition criteria. The primary goal was to identify etiology-driven molecular subtypes by integrating genomic, epigenomic, and transcriptomic data, and to nominate new therapeutic targets based on subtype-specific vulnerabilities [PMID:28667006](../papers/28667006.md).

## Composition

- **Total:** 489 [cholangiocarcinomas](../cancer_types/CHOL.md) from 10 countries; 133 Fluke-Positive (OV/CS), 356 Fluke-Negative; 39 HBV/HCV-positive; 5 PSC-positive; all untreated.
- **Anatomical breakdown:** intrahepatic ([IHCH](../cancer_types/IHCH.md)), perihilar ([PHCH](../cancer_types/PHCH.md)), and distal extrahepatic ([EHCH](../cancer_types/EHCH.md)); survival data available for 459 samples.
- **Platform breakdown:** whole-genome sequencing (WGS) n=71 tumor/normal pairs (avg 64.2× depth, Illumina HiSeq X10/2500/2000); whole-exome sequencing (WES) n=200 (previously published); targeted sequencing of 404 genes n=188 (SureSelect XT2, HiSeq 4000); SNP arrays (HumanOmniExpress) n=175; Illumina 450K methylation BeadChip n=138; HumanHT-12 Expression BeadChip n=118 [PMID:28667006](../papers/28667006.md).
- **Integrative subset:** 94 samples with all four data types used for [iClusterPlus](../methods/icluster.md) clustering; expanded to 121 samples for reanalysis (90% cluster-prediction accuracy).
- **Validation cohort:** newly classified samples plus a published 38-sample US TCGA CCA series for survival reproducibility [PMID:28667006](../papers/28667006.md).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md)
- [whole-exome-seq](../methods/whole-exome-seq.md)
- [targeted-dna-seq](../methods/targeted-dna-seq.md)
- [450k-methylation-array](../methods/450k-methylation-array.md)
- [microarray-gene-expression](../methods/microarray-gene-expression.md)
- [icluster](../methods/icluster.md)
- [mutational-signatures](../methods/mutational-signatures.md)
- [ascat](../methods/ascat.md)
- [crest](../methods/crest.md)
- [mutsig](../methods/mutsig.md)
- [firefly](../methods/firefly.md)
- [estimate](../methods/estimate.md)

## Papers using this cohort

- [PMID:28667006](../papers/28667006.md) — Jusakul et al. 2017; first comprehensive multi-omic landscape of 489 CCAs defining four etiology-driven molecular subtypes.

## Notable findings derived from this cohort

- Four integrative molecular subtypes (Clusters 1–4) defined by [iClusterPlus](../methods/icluster.md): Clusters 1–2 enriched in [TP53](../genes/TP53.md) mutations and [ERBB2](../genes/ERBB2.md) amplifications (Fluke-Positive); Cluster 3 with highest CNA burden and immune-checkpoint upregulation ([PDCD1](../genes/PDCD1.md), [PDCD1LG2](../genes/PDCD1LG2.md)); Cluster 4 with [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md) mutations, [BAP1](../genes/BAP1.md) inactivation, and [FGFR2](../genes/FGFR2.md) rearrangements [PMID:28667006](../papers/28667006.md).
- Four newly nominated CCA driver genes: [RASA1](../genes/RASA1.md) (4.1% inactivating, shRNA knockdown enhances migration/invasion), [STK11](../genes/STK11.md) (5% inactivating), [MAP2K4](../genes/MAP2K4.md) (homozygous deletions + 2.2% mutations), and [SF3B1](../genes/SF3B1.md) (4.6% at codons 625/700) [PMID:28667006](../papers/28667006.md).
- First [FGFR3](../genes/FGFR3.md)-[TACC3](../genes/TACC3.md) fusion reported in CCA; [FGFR2](../genes/FGFR2.md) 3′UTR truncating rearrangements identified as a new mechanism of [FGFR2](../genes/FGFR2.md) upregulation beyond canonical in-frame fusions [PMID:28667006](../papers/28667006.md).
- [ERBB2](../genes/ERBB2.md) amplification enriched in Fluke-Positive CCAs (10.4% vs 2.7%, p<0.01; avg 14 copies, FISH-validated); activating [ERBB2](../genes/ERBB2.md) point mutations in 2% of cases; nominates anti-HER2 therapy in Clusters 1–2 [PMID:28667006](../papers/28667006.md).
- Two distinct DNA-methylation subgroups: Cluster 1 CpG-island hypermethylation ([TET1](../genes/TET1.md) downregulated, [EZH2](../genes/EZH2.md) upregulated) and Cluster 4 CpG-shore hypermethylation (IDH1/2-driven or BAP1-associated) [PMID:28667006](../papers/28667006.md).
- Clusters 3 and 4 carry significantly better overall survival than Clusters 1–2 (log-rank p<0.001), independent of fluke status, anatomy, and stage; reproduced in an independent validation cohort [PMID:28667006](../papers/28667006.md).
- Ten COSMIC mutational signatures detected; APOBEC enriched in Fluke-Positive tumors (p<0.001); Signature 1 (CpG>TpG deamination) elevated in Cluster 1; L1 retrotransposition from [TTC28](../genes/TTC28.md) intron-1 in 28.2% of WGS tumors [PMID:28667006](../papers/28667006.md).
- FIREFLY method applied to 70 WGS samples identified four gene sets enriched for promoter mutations that alter TF binding and produce concordant transcriptional dysregulation, predominantly affecting PRC2/H3K27me3 pathways in Cluster 1 [PMID:28667006](../papers/28667006.md).

## Sources

- Jusakul A, Cutcutache I, Yong CH, et al. Whole-genome and epigenomic landscapes of etiologically distinct subtypes of cholangiocarcinoma. *Cancer Cell.* 2017;32(4):516-527.e8. [PMID:28667006](../papers/28667006.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
