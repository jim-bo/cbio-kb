---
name: CPTAC Colon Adenocarcinoma Proteogenomics (coad_cptac_2019)
studyId: coad_cptac_2019
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC); multi-institutional
size: 110
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
  - mirna-seq
  - label-free-proteomics
  - tmt-proteomics
  - tmt-phosphoproteomics
  - copy-number-array
panels: []
tags:
  - colon adenocarcinoma
  - COAD
  - CPTAC
  - proteogenomics
  - phosphoproteomics
  - MSI
  - CMS subtypes
processed_by: crosslinker
processed_at: 2026-05-16
---

# CPTAC Colon Adenocarcinoma Proteogenomics (coad_cptac_2019)

## Overview

The first proteogenomic study of a prospectively collected human colon cancer cohort, produced by the Clinical Proteomic Tumor Analysis Consortium (CPTAC-2). 110 newly diagnosed, untreated colon adenocarcinoma patients (rectal tumors excluded) underwent primary surgery and contributed paired tumor and normal-adjacent tissue (NAT) profiled by whole-exome sequencing, copy-number inference, RNA-Seq, miRNA-Seq, label-free shotgun proteomics, and TMT-based global and phosphoproteomics. Raw genomics deposited in SRA BioProject PRJNA514017; raw proteomics in CPTAC Data Portal S045; processed matrices available at LinkedOmics (http://linkedomics.org/cptac-colon/).

## Composition

- **110 patients**: 65 female, 45 male; mean age 65 (range 40–93); newly diagnosed, untreated; colon-only (rectal excluded).
- **Cancer type:** [COAD](../cancer_types/COAD.md) — colon adenocarcinoma only.
- **MSI status:** 24 MSI-H tumors / 82 MSS tumors (bimodal MS-INDEL distribution; PCR-based MSI testing on 85 samples — 100% concordance with WXS-based calls).
- **Platforms per omics:**
  - 106 tumor/normal-blood pairs by whole-exome sequencing (Illumina Nextera Rapid Capture Exome, HiSeq4000, ≥150× target coverage).
  - 105 tumor/normal pairs for copy-number inference ([CopywriteR](../methods/copywriter.md) + [GISTIC2](../methods/gistic2.md)).
  - 106 tumors with [RNA-Seq](../methods/rna-seq.md) and miRNA-Seq.
  - 100 tumors with label-free shotgun proteomics; 96 tumor/NAT pairs by [TMT global proteomics](../methods/tmt-proteomics.md) and [TMT phosphoproteomics](../methods/tmt-phosphoproteomics.md).
  - [Selected Reaction Monitoring (SRM)](../methods/selected-reaction-monitoring.md) for targeted validation.
- **Cross-cohort validation:** average mRNA profiles correlated with TCGA colorectal cohort at Pearson r=0.92; average label-free protein at r=0.96.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — Illumina Nextera Rapid Capture Exome; ≥150× target coverage.
- [RNA-Seq](../methods/rna-seq.md) — tumor transcriptomes; miRNA-Seq also performed.
- [TMT global proteomics](../methods/tmt-proteomics.md) — tandem-mass-tag quantitative proteomics on 96 tumor/NAT pairs.
- [TMT phosphoproteomics](../methods/tmt-phosphoproteomics.md) — phosphosite quantification on 96 tumor/NAT pairs.
- [CMS classifier](../methods/cms-classifier.md) — applied to assign consensus molecular subtypes (CMS1–4).

## Papers using this cohort

- [PMID:31031003](../papers/31031003.md) — Vasaikar et al. 2019, *Cell*: CPTAC-2 proteogenomic characterization of colon cancer; first proteogenomic colon cohort integrating WXS, RNA-seq, and multi-level proteomics.

## Notable findings derived from this cohort

- WXS identified 64,010 somatic SNVs, 7,691 somatic INDELs, and 6,186 somatic microsatellite INDELs across 106 tumors; the MS-INDEL distribution was bimodal, partitioning the cohort into 24 MSI-H and 82 MSS tumors. [PMID:31031003](../papers/31031003.md)
- Proteogenomic integration reclassified [SOX9](../genes/SOX9.md) as oncogenic: protein is significantly overexpressed in tumors vs matched NATs (p=1.02×10⁻¹⁰) despite frequent truncating mutations, because truncations cluster upstream of the K398 ubiquitin-degradation site, stabilizing the protein. [PMID:31031003](../papers/31031003.md)
- [RB1](../genes/RB1.md) is recurrently amplified; Rb protein is overexpressed (p=2.10×10⁻¹⁵) and hyperphosphorylated at E2F-regulating sites (T373/S807/S811/T826; average 1.84-fold higher in tumors vs NATs, p<2.2×10⁻¹⁶); [CDK2](../genes/CDK2.md) activity is the strongest predictor of phospho-Rb change (r=0.47, p=1.8×10⁻⁶), nominating [CDK2](../genes/CDK2.md) inhibition as a therapeutic target, particularly for CIN-subtype tumors. [PMID:31031003](../papers/31031003.md)
- Four new significantly mutated genes in hypermutated samples — [CASP5](../genes/CASP5.md), [RNF43](../genes/RNF43.md), [LTN1](../genes/LTN1.md), [BMPR2](../genes/BMPR2.md) (each in >50% of hypermutated tumors) — not previously reported by TCGA [COAD](../cancer_types/COAD.md). [PMID:31031003](../papers/31031003.md)
- Proteomics-supported proteogenomic search recovered 88 putative HLA-I binding neoantigens across 38% of tumors; three recurrent cancer/testis antigens ([IGF2BP3](../genes/IGF2BP3.md) 51%, [SPAG1](../genes/SPAG1.md) 14%, [ATAD2](../genes/ATAD2.md) 8%) were MSI-status-independent — candidates for shared tumor-antigen vaccines in MSS patients. [PMID:31031003](../papers/31031003.md)
- MSI-H tumors universally upregulated glycolytic enzymes at the protein level (Warburg effect); glycolytic enzyme abundance negatively correlated with [CD8A](../genes/CD8A.md) infiltration (Spearman ρ=−0.61, p=0.02), absent in other subtypes — supporting glycolysis inhibition to overcome checkpoint-blockade resistance in MSI-H CRC. [PMID:31031003](../papers/31031003.md)
- Network integration of CMS subtypes, proteomic subtypes, and MSI status yielded three unified molecular subtypes (UMS): MSI, CIN, and Mesenchymal; CDK inhibition predicted most effective in CIN (highest [RB1](../genes/RB1.md) copy number and Rb phosphorylation). [PMID:31031003](../papers/31031003.md)
- 31 proteins increased >2-fold in tumors vs NATs (cancer-associated proteins); 8 elevated in >95% of pairs: [DDX21](../genes/DDX21.md), [S100A11](../genes/S100A11.md), [S100P](../genes/S100P.md), [PLOD2](../genes/PLOD2.md), [SERPINH1](../genes/SERPINH1.md), [GPRC5A](../genes/GPRC5A.md) and others; only 7 are in the Cancer Gene Census. [PMID:31031003](../papers/31031003.md)

## Sources

- cBioPortal study: `coad_cptac_2019` — https://www.cbioportal.org/study/summary?id=coad_cptac_2019
- SRA BioProject: PRJNA514017 (genomics); CPTAC Data Portal: S045 (proteomics)
- LinkedOmics: http://linkedomics.org/cptac-colon/
- [PMID:31031003](../papers/31031003.md) — Vasaikar et al. 2019, *Cell*, DOI 10.1016/j.cell.2019.03.030

*This page was processed by **crosslinker** on **2026-05-16**.*
