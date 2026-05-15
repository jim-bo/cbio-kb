---
name: CRISPR Base Editing
slug: crispr-base-editing
kind: method
canonical_source: corpus
unverified: true
tags:
  - crispr
  - base-editing
  - allele-specific
  - functional-validation
  - prostate-cancer
processed_by: crosslinker
processed_at: 2026-05-15
---

# CRISPR Base Editing

## Overview

CRISPR base editing uses engineered fusions of a partially disabled Cas9 (nickase or dead Cas9) with a deaminase enzyme to install point mutations at a target genomic locus without introducing double-strand DNA breaks. Cytosine base editors (CBEs) convert C to T (or G to A on the opposite strand) within a defined editing window, while adenine base editors (ABEs) convert A to G. This enables allelic conversion at SNPs of interest — including disease-associated risk variants — to directly test the causal effect of a specific nucleotide change on gene expression or cellular phenotype.

## Used by

- CBE (cytosine base editor) used to convert rs4519489 T→A in PC3 cells (T/T→A/T), increasing [NOL10](../genes/NOL10.md) expression (P=9.06×10⁻³); an AYBE editor used in DU145 cells to perform reverse A→T conversion (A/A→T/T), reducing NOL10 expression. Together these reciprocal edits established causal allele-specific regulation of NOL10 by the rs4519489 variant [PMID:28927585](../papers/28927585.md)

## Notes

- Base editing is complementary to CRISPRi: CRISPRi perturbs enhancer activity transiently without sequence change; base editing permanently converts the allele to assess the direct effect of the SNP.
- The AYBE editor is a custom adenine base editor variant used for A→T conversion.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
