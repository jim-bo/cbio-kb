---
name: "BC Cancer Personalized OncoGenomics (POG) Program — Metastatic NEN Cohort 2025"
studyId: pog570_bcgsc_2020
institution: "BC Cancer / BC Genome Sciences Centre (BCGSC)"
size: 28
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - neuroendocrine-neoplasms
  - metastatic
  - whole-genome-transcriptome-analysis
  - personalized-oncogenomics
  - mutational-signatures
  - clinical-actionability
processed_by: entity-page-writer
processed_at: 2026-05-09
---

# BC Cancer Personalized OncoGenomics (POG) Program — Metastatic NEN Cohort 2025

> **Manifest mismatch note:** PMID 40328872 was originally logged against the dataset identifier `pog570_bcgsc_2020` (cBioPortal studyId). The raw paper text (Wee et al., Scientific Reports 2025; DOI 10.1038/s41598-025-00549-7) describes the BC Cancer Personalized OncoGenomics (POG) program cohort of 28 metastatic neuroendocrine neoplasms profiled by whole-genome and transcriptome analysis — this is distinct from any `panet_shanghai_2013` dataset. The content below reflects the actual paper. If this studyId was incorrectly resolved from the manifest, verify against the cBioPortal study registry and update the `studyId` frontmatter field accordingly.

## Overview

The pog570_bcgsc_2020 dataset represents the BC Cancer Personalized OncoGenomics (POG) program cohort of metastatic neuroendocrine neoplasms (NENs). Wee, Yang, Schaeffer, Loree, Gorski and colleagues performed paired whole-genome and transcriptome analysis (WGTA) on 28 metastatic NEN patients enrolled in the POG program between 2014 and April 2021, spanning eight distinct primary anatomical sites. The study is the largest WGTA series focused on metastatic NENs, confirming known driver genes in the metastatic context, identifying transcriptomic subgroups with clinical relevance, and demonstrating that WGTA-informed therapeutic recommendations conferred clinical benefit in 10 of 15 treated patients.

## Composition

- **N = 28** metastatic NEN patients (POG program, BC Cancer; referral window 2014 – April 2021)
- Inclusion criteria: available WGS + WTS data, sequencing-estimated tumour content ≥30%, NEN diagnosis or neuroendocrine components
- Primary anatomical sites:
  - Pancreas ([PANET](../cancer_types/PANET.md)/[PANEC](../cancer_types/PANEC.md), n=10)
  - Lung ([LNET](../cancer_types/LNET.md)/[LUNE](../cancer_types/LUNE.md), n=7)
  - Thyroid (medullary, [MTNN](../cancer_types/MTNN.md), n=3)
  - Small intestine ([SBWDNET](../cancer_types/SBWDNET.md))
  - Hepatobiliary, neck, unknown primary ([NETNOS](../cancer_types/NETNOS.md))
  - Ovary (mixed MiNEN: [MNET](../cancer_types/MNET.md)/[HGONEC](../cancer_types/HGONEC.md), n=1)
- 60% male; median age 53 (range 24–75); 26/28 specimens biopsied from metastases; 71% (20/28) biopsied from liver
- Data deposited in EGA under study EGAS00001001159
- Reference genome: hg19 (WGS alignment); hg38 (RNA-seq via STAR)

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md): paired tumor/normal Illumina; [BWA](../methods/bwa.md) alignment to hg19; [Strelka](../methods/strelka.md) for SNVs/indels; CNAseq for somatic CNAs; APOLLOH for LOH; ABySS/Trans-ABySS for SVs
- [RNA-seq](../methods/rna-seq.md): [STAR](../methods/star.md) alignment to hg38; [RSEM](../methods/rsem.md) for quantification; [edgeR](../methods/edger.md) for differential expression
- [MSIsensor](../methods/msisensor.md): microsatellite instability scoring
- [Mutational signatures](../methods/mutational-signatures.md): COSMIC v3 decomposition
- [ConsensusClusterPlus](../methods/consensus-hierarchical-clustering.md): transcriptome clustering (Spearman distance, k=3)
- [t-SNE](../methods/tsne.md): dimensionality reduction and visualization
- [VIPER](../methods/viper.md): master-regulator inference

## Papers using this cohort

- [PMID:40328872](../papers/40328872.md) — Wee et al., Scientific Reports 2025: WGTA landscape and clinical actionability of metastatic NENs in the POG program

## Notable findings derived from this cohort

- Actionable alterations identified in 24/28 patients; 10/15 treated patients experienced clinical benefit from WGTA-informed therapy [PMID:40328872](../papers/40328872.md)
- Median TMB = 2.19 mut/Mb (range 0.89–16.40); two cases had TMB >10 — consistent with prior NEN reports of 1.09–5.45 mut/Mb [PMID:40328872](../papers/40328872.md)
- [MEN1](../genes/MEN1.md), [DAXX](../genes/DAXX.md), [ATRX](../genes/ATRX.md), [RB1](../genes/RB1.md), [TP53](../genes/TP53.md) recurrently altered in pancreatic and pulmonary NENs; activating [RET](../genes/RET.md) mutations in all three medullary thyroid carcinomas [PMID:40328872](../papers/40328872.md)
- Large-scale LOH was [MEN1](../genes/MEN1.md)-mutant and pancreatic-NEN-specific — not observed in MEN1-mutant pulmonary NENs [PMID:40328872](../papers/40328872.md)
- Unsupervised transcriptome clustering (k=3) produced three groups: Cluster A (MEN1/DAXX/ATRX-enriched, mostly PanNETs and small-intestinal NETs), Cluster B (high-grade, MYC-driven), Cluster C (PulNETs and MTCs) [PMID:40328872](../papers/40328872.md)
- 82% (23/28) of POG NENs clustered with external NEN datasets and away from TCGA primary tumour types using a 1,553-gene discriminator panel [PMID:40328872](../papers/40328872.md)
- Biallelic MSH6/MLH1 loss in PN4 produced 18% unstable microsatellites but MSIsensor predicted MSI-low — illustrating limitations of MSI tools in non-colorectal NENs [PMID:40328872](../papers/40328872.md)
- Six patients with clinical benefit received therapies driven by transcriptome expression data alone, supporting value of WGTA beyond somatic mutation profiling [PMID:40328872](../papers/40328872.md)

## Sources

- [PMID:40328872](../papers/40328872.md)

*This page was processed by **entity-page-writer** on **2026-05-09**.*
