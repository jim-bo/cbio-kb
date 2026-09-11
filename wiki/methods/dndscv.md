---
name: dNdScv
slug: dndscv
kind: method
canonical_source: corpus
unverified: true
tags:
  - selection-inference
  - somatic-mutation
  - driver-discovery
  - bioinformatics
processed_by: wiki-cli
processed_at: 2026-09-10
---

# dNdScv

## Overview

dNdScv (dN/dS in cancer using a Poisson framework with covariate correction) is an R package for inferring positive and negative selection acting on somatic point mutations across cancer genes. It models the expected number of synonymous and nonsynonymous mutations under neutrality — controlling for gene-specific mutation rates, trinucleotide context, and gene length — and then computes gene-level dN/dS ratios. Genes with dN/dS significantly above 1 are inferred to be under positive selection (i.e., candidate drivers). The method was designed to reduce false positives relative to earlier recurrence-based approaches by explicitly modeling mutational heterogeneity.

## Used by

- Bolton et al. applied dNdScv to clonal hematopoiesis (CH) mutations from 24,146 cancer patients (MSK-IMPACT), restricting the analysis to the IMPACT-410/468 sub-cohorts with q < 0.1 and ≥25 variants per gene, to identify genes under positive selection in hematopoietic stem and progenitor cells across diverse cancer and therapy contexts [PMID:33106634](../papers/33106634.md)
- Applied as one of four statistical cancer-gene discovery tools in a [CSCC](../cancer_types/CSCC.md) ([CSCC](../cancer_types/CSCC.md)) meta-analysis of 88 WES/WGS tumors; dN/dS compares observed nonsynonymous-to-synonymous mutation ratios against neutral-evolution expectations to detect positive selection; collectively the four tools nominated 12 cancer genes, 7 called by ≥2 tools [PMID:34272401](../papers/34272401.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Part of three-tool consensus driver-calling pipeline applied to 25 metastatic [CSCC](../cancer_types/CSCC.md) WGS samples; called [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), and [C9](../genes/C9.md) as significant coding drivers (p<0.005) — all three corroborated by all tools [PMID:35982973](../papers/35982973.md)
- One of five driver-discovery tools (with MutSig2CV, OncodriveCLUST, OncodriveFM, e-Driver) run on nonhypermutated colorectal tumors to nominate 46 high-confidence significantly mutated genes [PMID:35487942](../papers/35487942.md)
- One of four tools (with MutSig2CV, HOTMAPS, OncodriveFML) used to call significantly mutated genes, requiring agreement from at least 2 of the 4 [PMID:36201743](../papers/36201743.md)
- Used with OncodriveFML and Cancer Genome Interpreter to identify driver genes in SDHB-mutant pheochromocytoma/paraganglioma genomes [PMID:40097403](../papers/40097403.md)

## Notes

- Input: somatic SNV calls from a targeted or whole-exome/genome panel, plus a reference of expected mutation rates (typically trinucleotide frequencies).
- Output: per-gene dN/dS ratios, p-values, and q-values for positive and negative selection.
- Analysis in [PMID:33106634](../papers/33106634.md) was restricted to genes with ≥25 variants and FDR q < 0.1, requiring large cohort sizes.
- Original method publication: Martincorena et al. (2017), Cell 171:1029–1041.

## Sources

- [PMID:33106634](../papers/33106634.md) — Bolton et al., clonal hematopoiesis in 24,146 cancer patients; dNdScv used to map positive selection in CH across cancer types and treatment exposures.

- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35487942](../papers/35487942.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
- [PMID:36201743](../papers/36201743.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
- [PMID:40097403](../papers/40097403.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
