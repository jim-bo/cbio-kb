---
name: ASCAT
slug: ascat
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number-analysis, allele-specific, tumor-purity, ploidy]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# ASCAT

## Overview

ASCAT (Allele-Specific Copy number Analysis of Tumors) is a computational method for deriving tumor-specific allele-specific copy-number profiles from SNP array or sequencing data. It models the total and allele-specific copy-number signal jointly with tumor purity (cellularity) and ploidy, producing locus-by-locus integer copy-number calls per allele. ASCAT explicitly accounts for the mixture of tumor and normal cells in a sample, enabling accurate estimation of loss of heterozygosity (LOH) and clonal copy-number changes.

## Used by

- [Pereira et al. 2016 — METABRIC breast cancer landscape](../papers/27161491.md): Used to call LOH in 2,433 primary breast tumours from the METABRIC cohort; cancer-cell-fraction (CCF) estimates for clonality analysis relied on ASCAT purity/ploidy calls; the authors explicitly note that subclonal architecture is only approximated rather than directly reconstructed from ASCAT output [PMID:27161491](../papers/27161491.md).
- Used in TRACERx to derive copy number, purity, and ploidy from multi-region exome sequencing data of 327 primary NSCLC tumor regions [PMID:28445469](../papers/28445469.md)

## Notes

- ASCAT is designed for matched tumor/normal pairs; accuracy depends on normal-sample purity for reference allele frequency estimation.
- CCF estimates downstream of ASCAT are approximate — ASCAT provides purity/ploidy for CCF normalization but does not directly reconstruct subclonal trees.
- ASCAT was originally developed for SNP-array data (Affymetrix SNP 6.0, Illumina Omni) and later extended to sequencing (ASCAT-seq, ASCAT-WGS).
- Published by Van Loo et al. (2010, PNAS); widely applied across TCGA and PCAWG pan-cancer studies.

## Sources

- Van Loo P et al. (2010) Allele-specific copy number analysis of tumors. *Proceedings of the National Academy of Sciences* 107:16910–16915.
- [PMID:27161491](../papers/27161491.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28445469](../papers/28445469.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
