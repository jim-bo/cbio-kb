---
name: Bladder Urothelial Carcinoma — Weill Cornell (2016)
studyId: blca_cornell_2016
institution: Weill Cornell Medicine
size: 72
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-panel-seq
panels:
  - exact-1
  - n250-targeted-panel
tags:
  - blca
  - urothelial-carcinoma
  - chemotherapy-evolution
  - clonal-dynamics
  - apobec-mutagenesis
  - l1cam
  - platinum-resistance
processed_by: crosslinker
processed_at: 2026-05-14
---

# Bladder Urothelial Carcinoma — Weill Cornell (2016)

## Overview

A prospective longitudinal cohort of 72 urothelial carcinoma (UC) tumors from 32 patients collected at Weill Cornell Medicine, designed to capture matched pre- and post-chemotherapy samples from advanced-stage disease. The cohort enriches for chemotherapy-treated metastatic UC; 16 patients contributed matched primary/advanced sets and 2 underwent rapid autopsy. Data were generated to interrogate how platinum-based chemotherapy reshapes UC clonal architecture. BAMs are deposited in dbGaP phs001087.v1.p1. [PMID:27749842](../papers/27749842.md)

## Composition

- **72 tumors from 32 patients**; 88% (28/32) with metastatic disease at enrollment. [PMID:27749842](../papers/27749842.md)
- **16 matched primary + advanced/post-chemotherapy sets**; 2 rapid autopsies (WCM117 with 12 samples across 8 anatomical sites; WCM259). [PMID:27749842](../papers/27749842.md)
- Cancer type: bladder urothelial carcinoma ([BLCA](../cancer_types/BLCA.md)).
- Comparator cohort: [TCGA bladder cohort (blca_tcga_pub)](../datasets/blca_tcga_pub.md) used for mutation-frequency benchmarking. [PMID:27749842](../papers/27749842.md)
- Drugs administered: [cisplatin](../drugs/cisplatin.md) and [gemcitabine](../drugs/gemcitabine.md) (neoadjuvant/first-line); [docetaxel](../drugs/docetaxel.md) + [ramucirumab](../drugs/ramucirumab.md) at later progression in case WCM117. [PMID:27749842](../papers/27749842.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) via the CLIA-grade [EXaCT-1](../methods/exact-1.md) assay (Agilent HaloPlex Exome, 21,522 genes, mean 85× coverage). [PMID:27749842](../papers/27749842.md)
- Orthogonal [N250 targeted panel](../methods/n250-targeted-panel.md) (250 cancer genes, SeqCap EZ Choice, mean 400× coverage; Pearson r=0.93 with WES VAFs, P<10⁻¹⁷¹). [PMID:27749842](../papers/27749842.md)
- [CLONET](../methods/clonet.md) for tumor purity/ploidy and clonality estimation; [MuTect](../methods/mutect.md) and SNVseeqer for SNV calling; [Oncotator](../methods/oncotator.md) for annotation; [GSEA](../methods/gsea.md) over REACTOME pathways; [mutational signature](../methods/mutational-signatures.md) decomposition vs Sanger COSMIC; phylogeny via parsimony Ratchet; [FISH](../methods/fish.md) for copy-number validation. [PMID:27749842](../papers/27749842.md)
- 53/72 samples passed CLONET QC; 44 (25 patients) had reliable purity/ploidy estimates for clonality analysis. [PMID:27749842](../papers/27749842.md)

## Papers using this cohort

- [PMID:27749842](../papers/27749842.md) — Faltas et al., *Nat Genet* 2016: Clonal evolution of chemotherapy-resistant urothelial carcinoma; whole-exome sequencing of 72 matched pre/post-chemotherapy tumors from 32 patients.

## Notable findings derived from this cohort

- **Only ~28% of mutations shared** between matched pre- and post-chemotherapy samples on average (range 0.2%–76.4%); even canonical UC drivers ([PIK3CA](../genes/PIK3CA.md), [KMT2D](../genes/KMT2D.md), [ATM](../genes/ATM.md), [TP53](../genes/TP53.md)) were inconsistently shared, implying that pre-treatment biopsy is insufficient to define actionable targets in chemotherapy-resistant disease. [PMID:27749842](../papers/27749842.md)
- **Early branching evolution**: phylogenetic analysis placed the primary tumor as a branch (not trunk) of every patient's tree, indicating multiple lineages diverged from an ancestral clone in parallel before diagnosis. [PMID:27749842](../papers/27749842.md)
- **Post-chemotherapy clonal enrichment**: post-chemotherapy samples showed significantly increased clonal mutations (P=0.0134, Fisher's exact); GSEA identified [L1CAM](../genes/L1CAM.md) signaling (OR=1.9, FDR=0.12) and integrin signaling (OR=2.8, FDR=0.02) as enriched — 83% and 90% missense, respectively, suggesting gain-of-function. [PMID:27749842](../papers/27749842.md)
- **ATM/RB/FANCC signature depleted by chemotherapy**: present in 73.3% of pre-chemotherapy vs 37.9% of post-chemotherapy tumors (P=0.05), suggesting selective elimination of [ATM](../genes/ATM.md)/[RB1](../genes/RB1.md)/[FANCC](../genes/FANCC.md)-altered clones. [PMID:27749842](../papers/27749842.md)
- **[APOBEC3A](../genes/APOBEC3A.md) dominates post-chemotherapy mutagenesis**: significant enrichment of [APOBEC3A](../genes/APOBEC3A.md) YTCA-context mutations (P=1×10⁻⁵) and [APOBEC3B](../genes/APOBEC3B.md) RTCA-context mutations (P=0.0395) post-chemotherapy; APOBEC3G mutagenesis decreased. [PMID:27749842](../papers/27749842.md)
- **WCM117 rapid autopsy (12 samples):** [CDKN2A](../genes/CDKN2A.md) deletion progressed from sub-clonal heterozygous in the primary to clonal homozygous in distant metastases; [TSPAN8](../genes/TSPAN8.md) mutation acquired at the primary-to-metastasis transition node. [PMID:27749842](../papers/27749842.md)
- **Copy-number landscape more stable than SNV landscape**: hierarchical CN clustering yields two stable clusters — Cluster A (9p21 [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md)/[MTAP](../genes/MTAP.md) deletions in a euploid background) and Cluster B (1q21.1 [SETDB1](../genes/SETDB1.md)/[MLLT11](../genes/MLLT11.md) amplifications, 6p22.3 [E2F3](../genes/E2F3.md) amplifications; enriched for [TP53](../genes/TP53.md) mutations). [PMID:27749842](../papers/27749842.md)

## Sources

- dbGaP accession: phs001087.v1.p1
- cBioPortal study ID: blca_cornell_2016
- Faltas et al., *Nat Genet* 2016 — DOI: 10.1038/ng.3682

*This page was processed by **crosslinker** on **2026-05-14**.*
