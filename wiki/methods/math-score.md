---
name: MATH Score (Mutant-Allele Tumor Heterogeneity)
slug: math-score
kind: method
canonical_source: corpus
unverified: true
tags: [intra-tumor-heterogeneity, clonality, biomarker]
processed_by: crosslinker
processed_at: 2026-05-14
---

# MATH Score (Mutant-Allele Tumor Heterogeneity)

## Overview

The MATH (Mutant-Allele Tumor Heterogeneity) score is a simple quantitative measure of intra-tumor genetic heterogeneity derived from somatic mutation variant allele frequencies (VAFs). Specifically, MATH is defined as 100 × (MAD of VAFs) / (median of VAFs), where MAD is the median [absolute](../methods/absolute.md) deviation. A higher MATH score reflects greater dispersion of VAFs and thus greater intra-tumor heterogeneity. The metric requires at least 5 mutations per sample and is applied after tumor-purity correction. MATH was introduced by Mroz and Rocco.

## Used by

- [Pereira et al. 2016 — METABRIC breast cancer landscape](../papers/27161491.md): MATH scores computed per the Mroz and Rocco method for 2,433 primary breast tumours in the METABRIC cohort (173-gene targeted panel); ER+ tumours had lower median MATH (0.29) than ER- (0.41); higher MATH was associated with worse breast-cancer-specific survival in ER+ disease (P=0.003) but not ER-; IntClust10 had the highest MATH (median 0.47); IntClust2 (CCND1/PAK1 11q13–14 co-amplification) paradoxically showed low MATH (median 0.25) despite poor outcome, suggesting a single early clonal amplification event dominates that subtype [PMID:27161491](../papers/27161491.md).

## Notes

- MATH requires ≥5 mutations per sample; tumours with very few somatic mutations are excluded, limiting applicability to mutation-quiet subtypes.
- MATH is a bulk measure — it does not reconstruct clonal architecture; high MATH may reflect many subclones or a single large-VAF subclone.
- The paradoxical finding in IntClust2 (low MATH + poor outcome) illustrates that heterogeneity-based biomarkers must be interpreted in the context of CNA-defined molecular subtypes.
- MATH is correlated with overall mutational burden but is conceptually distinct; it measures the spread of VAFs rather than the total mutation count.
- Samples must have purity-corrected VAFs to avoid confounding by normal-cell contamination.

## Sources

- Mroz EA, Rocco JW (2013) MATH, a novel measure of intratumor genetic heterogeneity, is high in poor-outcome classes of head and neck squamous cell carcinoma. *Oral Oncology* 49:211–215.
- [PMID:27161491](../papers/27161491.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
