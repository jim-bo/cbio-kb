---
name: PyClone
slug: pyclone
kind: method
canonical_source: corpus
unverified: true
tags: [clonal-inference, bayesian, mutation-clustering]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# PyClone

## Overview

PyClone is a Bayesian statistical method for inferring the clonal population structure of tumours from deep sequencing data. It clusters somatic single-nucleotide variants (SNVs) into groups that share the same cellular prevalence (cancer cell fraction), using a Dirichlet process mixture model. The resulting mutation clusters correspond to distinct clonal genotypes, enabling phylogenetic inference and tracking of clonal dynamics across samples or time-points.

## Used by

- Applied in a breast cancer patient-derived xenograft (PDX) clonal-dynamics study to cluster somatic SNVs into clonal populations; single-cell DNA sequencing of 210 nuclei from SA494 and SA501 PDX lines validated that PyClone clusters correspond to real clonal genotypes, and replicate transplants produced concordant clonal expansion patterns (median Pearson r 0.91–0.94) [PMID:25470049](../papers/25470049.md)
- Used alongside EXPANDS for clonal-prevalence inference in medulloblastoma WGS data; supported detection that on average only 11.8% of somatic SNVs/indels were shared between matched diagnostic and recurrent tumors [PMID:26760213](../papers/26760213.md).
- Modified PyClone used in TRACERx to cluster somatic variants into subclonal populations from multi-region exome sequencing data, enabling ctDNA panel design and phylogenetic tree construction [PMID:28445469](../papers/28445469.md)
- PyClone v0.13.0 used to estimate cancer cell fraction of somatic variants in 68 paired melanoma WES biopsies; enabled characterization of clonal vs subclonal mutation dynamics on nivolumab [PMID:29033130](../papers/29033130.md)
- Applied for bulk CCF inference in mixed-type cHCC-ICC cases (133 cases); PyClone bulk CCF results were validated against single-nucleus sequencing (SNS) on one case (Mix_19, 74 tumor nuclei + 11 normal nuclei) — recapitulating one founding clone and two subclones consistent with PyClone output [PMID:31130341](../papers/31130341.md)

## Notes

- Uses copy-number and tumour purity estimates as inputs alongside variant allele frequencies to compute cancer cell fractions.
- Suitable for multi-region and longitudinal sampling designs where the same clones appear across multiple sequencing runs.
- Results are often paired with TITAN (for CNA-based clonal inference) or phylogenetic tree methods to cross-validate clonal structure.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-14**.*
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28445469](../papers/28445469.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
