---
name: NetMHC 4.0
slug: netmhc4
kind: method
canonical_source: corpus
unverified: true
tags: [neoantigen, hla, immunotherapy, prediction]
processed_by: crosslinker
processed_at: 2026-05-15
---

# NetMHC 4.0

## Overview

NetMHC 4.0 is a computational tool for predicting peptide binding affinity to MHC class I molecules (HLA alleles) using artificial neural networks trained on experimentally measured binding data. It is widely used for neoantigen prediction: candidate peptides (e.g., from somatic mutations or fusion junctions) are scored for binding to the patient's HLA type, and those predicted to bind strongly are nominated as potential neoantigens for T-cell recognition.

## Used by

- Used for HLA-typed neoantigen prediction from fusion-junction peptides across 9,624 TCGA tumor samples; mean 1.5 predicted neoantigens per fusion (range 0.33 in [KICH](../cancer_types/KICH.md) to 2.88 in [THYM](../cancer_types/THYM.md)); frameshift fusions yielded more epitopes than inframe fusions (mean 2.2 vs. 1.0); results described as "exploratory and speculative" [PMID:29617662](../papers/29617662.md)

## Notes

- Neoantigen predictions are theoretical; experimental validation (MHC binding assays, T-cell response assays) is required to confirm immunogenicity.
- Frameshift fusions generate longer novel peptide sequences and thus more neoantigen candidates than inframe fusions, though the former may be subject to nonsense-mediated decay.
- HLA typing is required as input; TCGA HLA types were available for the cohort.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
