---
name: Targeted Deep Amplicon Sequencing
slug: targeted-deep-amplicon-seq
kind: method
canonical_source: corpus
unverified: true
tags:
  - sequencing
  - subclonal-detection
  - ultra-deep
  - validation
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Targeted Deep Amplicon Sequencing

## Overview

Targeted deep amplicon sequencing applies PCR amplification followed by massively parallel sequencing to quantify variant allele frequencies at a predefined set of loci with very high depth (typically hundreds to tens of thousands of reads per site). This approach is used for sensitive detection and tracking of subclonal mutations across tumor samples, including longitudinal studies comparing primary and recurrent tumors, and enables quantification of rare tumor subpopulations that would be missed by standard WGS or WES.

## Used by

- Ultra-deep targeted resequencing of 192 patient-specific SNVs across 20 medulloblastoma patients at diagnosis and recurrence; confirmed expansion of clones initially present at <5% in 16/20 patients, with sensitivity demonstrated down to 2/10,000 reads [PMID:26760213](../papers/26760213.md).
- Used as an 8-sample addendum with a 71-gene targeted exome panel to supplement whole-exome sequencing of periampullary tumors in the Australian Pancreatic Cancer Genome Initiative cohort [PMID:26804919](../papers/26804919.md)
- Bespoke patient-specific multiplex-PCR NGS panels targeting clonal and subclonal SNVs identified by multi-region exome sequencing, sequenced at ~40,000x depth, used in TRACERx for ctDNA monitoring with ≥2-SNV positivity threshold [PMID:28445469](../papers/28445469.md)
- Custom 165-amplicon Ion AmpliSeq panel at mean coverage ×5,406 used for multiregion sequencing of one heavily sampled salivary ACC across 6 primary subregions and 8 lung metastases, revealing 36 unique mutations with 70% of metastatic mutations present in only 1–3 primary subregions [PMID:31483290](../papers/31483290.md).

## Notes

- Sensitivity can reach 0.01–0.001% variant allele frequency depending on depth and error-correction methods.
- Requires prior knowledge of target loci (e.g., from WGS/WES discovery), making it suitable for validation and longitudinal monitoring rather than de novo discovery.
- Patient-specific SNV panels (as in [PMID:26760213](../papers/26760213.md)) provide individualized coverage of subclonal architecture.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-14**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28445469](../papers/28445469.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
