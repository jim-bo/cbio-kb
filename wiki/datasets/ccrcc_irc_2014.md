---
name: Clear Cell Renal Cell Carcinoma Multiregion Sequencing (IRC 2014)
studyId: ccrcc_irc_2014
institution: Institute of Cancer Research / University College London / The Royal Marsden
size: 79
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - renal-cell-carcinoma
  - intratumor-heterogeneity
  - multiregion-sequencing
  - branched-evolution
  - whole-exome-seq
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Clear Cell Renal Cell Carcinoma Multiregion Sequencing (IRC 2014)

## Overview

Multiregion exome sequencing (M-seq) cohort of 10 stage T2–T4 clear cell renal cell carcinoma (ccRCC) nephrectomies generating 79 tumor samples. Developed through the London Renal Cancer Consortium tissue protocol and the E-PREDICT translational trial (EUDRACT 2009-013381-54). Sequenced on Illumina HiSeq using Agilent SureSelect Human All Exon V4 (median ≥70× depth); 92.5% of candidate mutations validated by AmpliSeq ultra-deep amplicon sequencing (>400×) on Ion Torrent PGM. Raw exome data deposited at EGA (EGAS00001000667); gene-expression microarray at GEO (GSE53000).

## Composition

- 10 ccRCC primary tumors ([CCRCC](../cancer_types/CCRCC.md)), stages T2 (n=2), T3 (n=7), T4 (n=1).
- 79 tumor samples total: 8–20 macrodissected regions per nephrectomy, 8–12 retained for sequencing per case.
- Additional metastatic samples for 4 cases (perinephric, chest-wall, lymph-node, renal-vein tumor thrombus).
- Treatment context: 6 cases received preoperative [everolimus](../drugs/everolimus.md); 1 case received [sunitinib](../drugs/sunitinib.md); 3 cases treatment-naive.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — Agilent SureSelect V4 on Illumina HiSeq
- [Multiregion exome sequencing (M-seq)](../methods/multiregion-exome-seq.md)
- [Phylogenetic tree reconstruction](../methods/phylogenetic-tree-reconstruction.md) — maximum parsimony from regional mutation calls

## Papers using this cohort

- [PMID:24487277](../papers/24487277.md) — Gerlinger et al. (2014): multiregion sequencing defining genomic architecture and ITH in ccRCC.

## Notable findings derived from this cohort

- 73–75% of driver aberrations (36/49 driver mutations; 57/76 driver SCNAs) were subclonal in all 10 ccRCCs; [VHL](../genes/VHL.md) inactivation and chromosome 3p loss were the only truncal events in every tumor [PMID:24487277](../papers/24487277.md).
- [PBRM1](../genes/PBRM1.md) mutations were truncal in only 3 of 6 mutated tumors, qualifying it as a "facultative" trunk driver [PMID:24487277](../papers/24487277.md).
- Parallel evolution documented for [PIK3CA](../genes/PIK3CA.md), [SETD2](../genes/SETD2.md), [BAP1](../genes/BAP1.md), and the SWI/SNF complex across multiple tumors [PMID:24487277](../papers/24487277.md).
- Single-biopsy approaches underestimate driver-mutation prevalence: [TP53](../genes/TP53.md) detected in 6% of individual biopsies vs 40% of cases; PI3K–mTOR pathway mutations in 28% vs 60% of cases [PMID:24487277](../papers/24487277.md).
- C>T transitions at CpG sites increased significantly on branch versus trunk mutations (q = 0.007), indicating shifting mutational processes during ccRCC evolution [PMID:24487277](../papers/24487277.md).

## Sources

- [PMID:24487277](../papers/24487277.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
