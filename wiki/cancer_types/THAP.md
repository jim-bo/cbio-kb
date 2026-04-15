---
name: Anaplastic Thyroid Cancer
oncotree_code: THAP
main_type: Thyroid Cancer
parent: THYROID
tags: []
processed_by: crosslinker
processed_at: 2026-04-11
---

# Anaplastic Thyroid Cancer (THAP)

## Overview

Anaplastic thyroid carcinoma (ATC/THAP) is the most aggressive thyroid malignancy, with a median survival of 3--6 months and near-universal lethality. On OncoTree it is a child of THYROID. ATC typically arises from dedifferentiation of a pre-existing differentiated thyroid cancer (DTC), particularly papillary thyroid carcinoma ([THPA](../cancer_types/THPA.md)). It is characterized by a high mutation burden compared to PTC but fewer mutations than most other adult cancers.

## Cohorts in the corpus

- 213 ATC regions from 179 primary ATCs, plus 34 co-occurring DTC components; 115 papillary thyroid cancer regions; 13 ATC cell lines; from 292 patients across 15 institutions (GATCI consortium). WES (n=132), WGS (n=9), SNP arrays (n=110), RNA-seq (n=24). Dataset: [thyroid_gatci_2024](../datasets/thyroid_gatci_2024.md). [PMID:38412093](../papers/38412093.md)

## Recurrent alterations

- [TP53](../genes/TP53.md) — mutations in 36.8% of ATCs vs. 0.9% of PTCs; frequency increases progressively from PTC to co-DTC (21.4%) to ATC; associated with elevated [TP53](../genes/TP53.md) mRNA abundance (P=0.0067). [PMID:38412093](../papers/38412093.md)
- [BRAF](../genes/BRAF.md) — V600E in 21.3% of ATCs vs. 50.9% of PTCs; clonal/early subclonal timing; mutually exclusive with RAS; co-occurs with [PIK3CA](../genes/PIK3CA.md) mutations (FDR=0.034). [PMID:38412093](../papers/38412093.md)
- [NRAS](../genes/NRAS.md) — recurrently mutated in ATC (top 5 by FDR); mutually exclusive with [BRAF](../genes/BRAF.md) V600E. [PMID:38412093](../papers/38412093.md)
- [PIK3CA](../genes/PIK3CA.md) — co-occurs with BRAF V600E (FDR=0.034); preferentially mutated in ATCs and co-DTCs. [PMID:38412093](../papers/38412093.md)
- [CDKN2A](../genes/CDKN2A.md) — deleted in 42% of ATCs; recurrent in co-DTCs, rare in PTCs (~5%). [PMID:38412093](../papers/38412093.md)
- [BRCA2](../genes/BRCA2.md) — deleted in 33.6% of ATCs; deletion associated with better survival (HR=0.48, P=0.005). [PMID:38412093](../papers/38412093.md)
- [TERT](../genes/TERT.md) — promoter mutations correlated with TP53 mutations (FDR<0.01). [PMID:38412093](../papers/38412093.md)
- [ATM](../genes/ATM.md), [BRCA1](../genes/BRCA1.md) — recurrent somatic and germline alterations at both SNV and CNA level. [PMID:38412093](../papers/38412093.md)
- [RB1](../genes/RB1.md) — recurrent deletions in ATCs. [PMID:38412093](../papers/38412093.md)
- [USH2A](../genes/USH2A.md) — recurrently mutated (top 5 by FDR). [PMID:38412093](../papers/38412093.md)
- Mutational burden: 3.8 +/- 1.2 SNVs/Mb and 120 +/- 44 CNAs per tumor; 42 recurrently mutated genes by SeqSig (FDR<0.05). [PMID:38412093](../papers/38412093.md)

## Subtypes

- Five CNA subtypes (A-E) by consensus clustering, with characteristic genomic and clinical features: subtype A enriched for older patients with better survival; subtype D enriched for male patients with metastatic disease. [PMID:38412093](../papers/38412093.md)
- Multi-region WGS (9 patients) confirmed that ATC and co-occurring DTC share a common clonal origin, with the common ancestor harboring ~95% of CNAs but only 19.1% of SNVs. [PMID:38412093](../papers/38412093.md)
- Patients with lower mutation rate (>10 SNVs/Mb) had significantly better survival (HR=0.51, P=0.002). [PMID:38412093](../papers/38412093.md)

## Therapeutic landscape

- BRAF V600E-targeted therapy ([dabrafenib](../drugs/dabrafenib.md) + [trametinib](../drugs/trametinib.md)) FDA-approved for BRAF V600E-mutant ATC; present study mostly pre-approval, limiting survival analysis. [PMID:38412093](../papers/38412093.md)
- Recurrent [BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), and [ATM](../genes/ATM.md) alterations rationalize investigation of PARP inhibitors in ATC. [PMID:38412093](../papers/38412093.md)
- Surgery (FDR=0.0089) and radiotherapy (FDR=1.7e-5) associated with improved [OS](../cancer_types/OS.md). [PMID:38412093](../papers/38412093.md)
- Germline variants in cancer predisposition genes: [RECQL4](../genes/RECQL4.md) (5%), BRCA2 (n=3), [FANCF](../genes/FANCF.md) (n=3). [PMID:38412093](../papers/38412093.md)

## Sources

- [PMID:38412093](../papers/38412093.md) — The genomic and evolutionary landscapes of anaplastic thyroid carcinoma (Cell Reports, 2024)

*This page was processed by **crosslinker** on **2026-04-11**.*
