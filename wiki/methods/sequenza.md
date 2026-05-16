---
name: Sequenza
slug: sequenza
kind: copy_number_analysis
canonical_source: corpus
unverified: true
tags: []
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Sequenza

## Overview

Sequenza is an R/Bioconductor tool for allele-specific copy-number analysis and loss-of-heterozygosity (LOH) inference from tumor/normal paired sequencing data. It jointly estimates tumor cellularity, ploidy, B-allele frequencies, and segmented copy-number states using depth ratio and B-allele frequency (BAF) information. LOH events are inferred from heterozygous germline SNP positions and are manually curated against depth ratio tracks.

## Used by

- Applied to 15 Korean vulvar SCC paired tumor/normal WES samples to infer LOH events including copy-neutral LOH (4 tumors: 1 HPV(+), 3 HPV(−)); results were manually curated using depth ratio and B-allele frequency in conjunction with [nexus-copy-number](../methods/nexus-copy-number.md) [PMID:29422544](../papers/29422544.md)
- Used for allele-specific copy-number estimation and tumor purity/ploidy inference in the pan-Asia cHCC-ICC WES/WGS study (173 tumor samples); supported identification of focal CNAs including [MYC](../genes/MYC.md) amplification (73%) and [CDKN2A](../genes/CDKN2A.md) deletion (37%) [PMID:31130341](../papers/31130341.md)

## Notes

- Corpus-grown slug; not listed as a `genePanelId` in cBioPortal gene panels or as a `molecularAlterationType` in cBioPortal molecular profiles.
- Operates on paired tumor/normal WES or targeted sequencing data; not suitable for tumor-only workflows.
- Complementary to allele-specific CNA tools such as [facets](../methods/facets.md) and [ascat](../methods/ascat.md).

## Sources

- [PMID:29422544](../papers/29422544.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
