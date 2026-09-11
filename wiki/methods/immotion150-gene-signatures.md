---
name: IMmotion150 Gene-Expression Signatures (Angio, Teff, Myeloid Inflammation)
slug: immotion150-gene-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [gene-expression-signature, angiogenesis, t-effector-signature, myeloid-inflammation, tumor-immune-microenvironment, renal-cell-carcinoma]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# IMmotion150 Gene-Expression Signatures (Angio, Teff, Myeloid Inflammation)

## Overview

A set of three median-dichotomized, RNA-seq-derived gene-expression signatures defined in the IMmotion150 phase 2 trial of atezolizumab +/- bevacizumab versus sunitinib in treatment-naive metastatic renal cell carcinoma: **Angio** (VEGFA, KDR, ESM1, PECAM1, ANGPTL4, CD34), **Teff/T-effector** (CD8A, EOMES, PRF1, IFNG, CD274) and **myeloid inflammation** (IL6, CXCL1, CXCL2, CXCL3, CXCL8, PTGS2).

## Used by

- Defined and used to stratify 263 IMmotion150 tumors by RNA-seq: AngioHigh tumors tracked CD31 IHC vascular density and predicted sunitinib benefit (ORR 46% AngioHigh vs 9% AngioLow; PFS HR 0.31 within the sunitinib arm); TeffHigh tumors tracked CD8/PD-L1 IHC and predicted atezolizumab + bevacizumab benefit over sunitinib (HR 0.55) and over atezolizumab monotherapy in TeffHighMyeloidHigh tumors (HR 0.25 for the combination vs atezolizumab alone) [PMID:29867230](../papers/29867230.md).

## Notes

- Signatures were split at the cohort median with no prespecified threshold; TMB and neoantigen burden did not correlate with the Teff score in this cohort.
- Reused as a comparator in a later 14-cohort ccRCC meta-analysis (IMmotion150 n=163) for TKI-response prediction [PMID:40834854](../papers/40834854.md).

## Sources

- [PMID:29867230](../papers/29867230.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
