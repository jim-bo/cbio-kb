---
name: IMmotion150 Gene-Expression Signatures (Angio, Teff, Myeloid Inflammation)
slug: immotion150-gene-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [gene-expression-signature, angiogenesis, t-effector-signature, myeloid-inflammation, tumor-immune-microenvironment, renal-cell-carcinoma]
processed_by: crosslinker
processed_at: 2026-09-11
---

# IMmotion150 Gene-Expression Signatures (Angio, Teff, Myeloid Inflammation)

## Overview

A set of three median-dichotomized, RNA-seq-derived gene-expression signatures defined in the IMmotion150 phase 2 trial of [atezolizumab](../drugs/atezolizumab.md) +/- [bevacizumab](../drugs/bevacizumab.md) versus [sunitinib](../drugs/sunitinib.md) in treatment-naive metastatic renal cell carcinoma: **Angio** ([VEGFA](../genes/VEGFA.md), [KDR](../genes/KDR.md), [ESM1](../genes/ESM1.md), [PECAM1](../genes/PECAM1.md), [ANGPTL4](../genes/ANGPTL4.md), [CD34](../genes/CD34.md)), **Teff/T-effector** ([CD8A](../genes/CD8A.md), [EOMES](../genes/EOMES.md), [PRF1](../genes/PRF1.md), [IFNG](../genes/IFNG.md), [CD274](../genes/CD274.md)) and **myeloid inflammation** ([IL6](../genes/IL6.md), [CXCL1](../genes/CXCL1.md), [CXCL2](../genes/CXCL2.md), [CXCL3](../genes/CXCL3.md), [CXCL8](../genes/CXCL8.md), [PTGS2](../genes/PTGS2.md)).

## Used by

- Defined and used to stratify 263 IMmotion150 tumors by RNA-seq: AngioHigh tumors tracked CD31 IHC vascular density and predicted sunitinib benefit (ORR 46% AngioHigh vs 9% AngioLow; PFS HR 0.31 within the sunitinib arm); TeffHigh tumors tracked CD8/PD-L1 IHC and predicted atezolizumab + bevacizumab benefit over sunitinib (HR 0.55) and over atezolizumab monotherapy in TeffHighMyeloidHigh tumors (HR 0.25 for the combination vs atezolizumab alone) [PMID:29867230](../papers/29867230.md).

## Notes

- Signatures were split at the cohort median with no prespecified threshold; TMB and neoantigen burden did not correlate with the Teff score in this cohort.
- Reused as a comparator in a later 14-cohort ccRCC meta-analysis (IMmotion150 n=163) for TKI-response prediction [PMID:40834854](../papers/40834854.md).

## Sources

- [PMID:29867230](../papers/29867230.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
