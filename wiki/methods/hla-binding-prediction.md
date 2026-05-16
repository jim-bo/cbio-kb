---
name: HLA-binding prediction (neoantigen prediction)
slug: hla-binding-prediction
kind: method
canonical_source: corpus
unverified: true
tags:
  - neoantigen
  - immunotherapy
  - hla
  - mhc
  - computational-immunology
  - proteomics
processed_by: crosslinker
processed_at: 2026-05-16
---

# HLA-binding prediction (neoantigen prediction)

## Overview

HLA-binding prediction involves computationally scoring candidate peptides (typically 9–11 amino acids in length) for their affinity to patient-specific HLA class I or class II alleles, as a means to prioritize putative neoantigens for immunotherapy applications. Methods such as NetMHCpan, NetMHC, or custom scoring matrices [estimate](../methods/estimate.md) IC50 or percentile rank for each peptide-HLA pair; peptides with IC50 <500 nM (or top 2% rank) are conventionally considered high-affinity binders. In proteogenomics, the peptide database is derived from patient-specific somatic mutations translated into mutant peptides, enabling proteomics-supported neoantigen discovery.

## Used by

- Applied in the CPTAC colon cancer proteogenomic study ([coad_cptac_2019](../datasets/coad_cptac_2019.md)) using a customized proteomics database from 173 proteomics-supported somatic mutations; identified 88 mutant 9–11mer peptides with high predicted HLA-I binding affinity (putative neoantigens) across 38% of tumors; neoantigens were enriched in MSI-H tumors and largely patient-specific, in contrast to three shared cancer/testis antigens ([IGF2BP3](../genes/IGF2BP3.md) in 51%, [SPAG1](../genes/SPAG1.md) in 14%, [ATAD2](../genes/ATAD2.md) in 8% of tumor/NAT pairs) [PMID:31031003](../papers/31031003.md)

## Notes

- Proteomics-supported neoantigen filtering (requiring the mutant peptide to be detected by MS) provides a more stringent prioritization than mRNA-only approaches, as it confirms the neoepitope is actually produced as a protein.
- 78% of CPTAC colon tumors had at least one proteomics-supported neoantigen or cancer/testis antigen, expanding the fraction potentially eligible for personalized immunotherapy.
- Cancer/testis antigens (IGF2BP3, SPAG1, ATAD2) are MSI-status-independent, making them candidates for MSS tumors that lack sufficient neoantigen load for checkpoint blockade.
- Not in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
