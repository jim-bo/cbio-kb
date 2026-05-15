---
name: Malignant Rhabdoid Tumor BCGSC 2016 (Chun et al.)
studyId: mrt_bcgsc_2016
institution: BC Cancer Genome Sciences Centre / Children's Oncology Group
size: 40
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-genome-bisulfite-seq
  - rna-seq
  - mirna-seq
  - chip-seq
panels: []
tags:
  - rhabdoid-tumor
  - pediatric
  - mrt
  - smarcb1
  - epigenomics
  - super-enhancers
  - HOX-clusters
  - methylation
  - TARGET
  - COG
  - dbGaP
processed_by: crosslinker
processed_at: 2026-05-14
---

# Malignant Rhabdoid Tumor BCGSC 2016 (Chun et al.)

## Overview

Integrative multi-omic reference landscape of 40 extra-cranial malignant rhabdoid tumors ([MRT](../cancer_types/MRT.md)) — primarily pediatric kidney and soft-tissue cases — banked through the National Wilms Tumor Study Group 5 / Children's Oncology Group (COG) AREN03B2 protocols and analyzed at the BC Cancer Genome Sciences Centre. The cohort combines whole-genome sequencing, whole-genome bisulfite sequencing (WGBS), RNA-Seq, miRNA-Seq, and H3K27me3/H3K27ac ChIP-Seq to characterize the molecular sub-groups and epigenetic architecture of MRT despite the near-uniform [SMARCB1](../genes/SMARCB1.md) driver. Sequencing reads and analyzed files deposited at NCBI dbGaP (phs000470) and the TARGET data portal. [PMID:26977886](../papers/26977886.md)

## Composition

- **40 tumor/normal pairs** (WGS; median tumor content 88.0% by APOLLOH).
- **66 primary MRTs** profiled by miRNA-Seq (58 kidney, 7 soft tissue, 2 liver).
- 40 matched normals: 16 adjacent kidney tissue, 24 peripheral blood.
- Cancer types: rhabdoid tumor of the kidney ([MRT](../cancer_types/MRT.md)) and extra-renal/liver MRT ([MRTL](../cancer_types/MRTL.md)).
- Age range: predominantly <2 years (pediatric); one sub-group enriched for patients >1 year.
- Multiple supplemental assays: 40 MRT + 3 MRT cell lines + 3 hESC lines + 4 NPCs (WGBS); 35 primary MRTs + cell lines + normals (H3K27me3 ChIP-Seq); 10 MRT + comparators (H3K27ac ChIP-Seq). [PMID:26977886](../papers/26977886.md)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 40 tumor/normal pairs; somatic SNV/indel and structural variant calling.
- [whole-genome-bisulfite-seq](../methods/whole-genome-bisulfite-seq.md) — WGBS on 40 MRT + 3 MRT cell lines + 3 hESC + 4 NPCs; promoter CpG-island methylation clustering.
- [rna-seq](../methods/rna-seq.md) — 40 MRT + 3 hESC + 4 fetal cerebellum normals; mRNA sub-group discovery.
- [mirna-seq](../methods/mirna-seq.md) — 66 primary MRTs; clustering against TCGA and normal references (11,819 cases, 37 cancer types, 27 normal tissues).
- [chip-seq](../methods/chip-seq.md) — H3K27me3 (35 MRT + 3 cell lines + 2 hESC + 2 fetal brain + 2 [NPC](../cancer_types/NPC.md)); H3K27ac (10 MRT + 3 cell lines + 3 hESC + 1 fetal brain).

## Papers using this cohort

- [PMID:26977886](../papers/26977886.md) — Chun et al., *Nat Genet* 2016: primary discovery study; integrative epigenomic and multi-omic reference for extra-cranial MRT.

## Notable findings derived from this cohort

- [SMARCB1](../genes/SMARCB1.md) biallelic inactivation in 39/40 cases; the single SMARCB1-intact case carried somatic LOH plus a germline one-base [SMARCA4](../genes/SMARCA4.md) deletion; median 612.5 somatic SNVs per case (0.231 mutations/Mb), confirming quiet genomes outside the SWI/SNF driver [PMID:26977886](../papers/26977886.md).
- [DSCAM](../genes/DSCAM.md) was the only recurrent non-SMARCB1 non-synonymous target (2/40 cases; flagged as possibly passenger) [PMID:26977886](../papers/26977886.md).
- Chromosome 22 dominated structural variation: 9/15 recurrent CNA loci and 22/26 verified gene fusions involve chr22; 7 fusions arise as direct consequences of SMARCB1 deletion, with [SPECC1L](../genes/SPECC1L.md) as the most common fusion partner [PMID:26977886](../papers/26977886.md).
- miRNA clustering against TCGA/normals split 66 MRTs into a large group clustering with normal cerebellum and TCGA pheochromocytoma/paraganglioma and a smaller group (n=9) clustering with synovial sarcomas, linking MRT to neural-crest lineages [PMID:26977886](../papers/26977886.md).
- mRNA NMF sub-group 1 (enriched for extra-renal tumors) is more AT/RT-like; sub-group 2 is more RTK-like (one-sided Fisher p = 1.193e-13 vs Grupenmacher 2013 markers) [PMID:26977886](../papers/26977886.md).
- Two methylation sub-groups: sub-group A (higher CGI methylation) enriched for patients >1 year; MRT-specific super-enhancers cover HOXA, HOXB, HOXC, HISTH1/HISTH2 clusters and the [HOTAIR](../genes/HOTAIR.md) lncRNA; 158 promoters show loss of H3K27me3 enriched for homeobox/HOX terms (FDR 4.17e-44) [PMID:26977886](../papers/26977886.md).

## Sources

- NCBI dbGaP: phs000470
- TARGET data portal: additional analyzed matrices
- [PMID:26977886](../papers/26977886.md) — Chun HE et al., "Genome-wide profiles of extra-cranial malignant rhabdoid tumors reveal heterogeneity and dysregulated developmental pathways." *Nat Genet* 2016.

*This page was processed by **crosslinker** on **2026-05-14**.*
