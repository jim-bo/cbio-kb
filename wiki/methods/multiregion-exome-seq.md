---
name: Multiregion exome sequencing (M-seq)
slug: multiregion-exome-seq
kind: method
canonical_source: corpus
unverified: true
tags: [sequencing, wes, intratumor-heterogeneity]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Multiregion exome sequencing (M-seq)

## Overview

A whole-exome sequencing design in which multiple spatially distinct regions are sampled from the same tumor to characterize intratumor heterogeneity (ITH) and reconstruct evolutionary trajectories. Each region is sequenced independently and mutation calls are integrated across regions to distinguish truncal (ubiquitous) from branch (subclonal) alterations.

## Used by

- Applied to 10 ccRCC primary tumors (79 total tumor samples, 8–12 macrodissected regions per case) using Agilent SureSelect Human All Exon V4 on Illumina HiSeq (median ≥70× depth); 92.5% of candidate mutations validated by ultra-deep amplicon sequencing (>400×) on Ion Torrent PGM [PMID:24487277](../papers/24487277.md).
- Used in the TRACERx [NSCLC](../cancer_types/NSCLC.md) study to profile 327 spatially separated primary tumor regions and 4 metastatic biopsies for ctDNA panel design and phylogenetic tracking of disease evolution [PMID:28445469](../papers/28445469.md)
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md): multi-region sampling with 168 tumor regions (105 PCBM + 63 matched primaries) sequenced across 51 patients via Agilent SureSelectXT V7 WES to characterize clonal evolution and spatial heterogeneity [PMID:35504881](../papers/35504881.md)

## Notes

- Enables separation of truncal (founding) from branch (subclonal) driver events; single-biopsy designs systematically underestimate driver prevalence per case.
- Saturation of ITH detection requires many regions; 7/10 ccRCC tumors showed no saturation with up to 12 regions sampled [PMID:24487277](../papers/24487277.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28445469](../papers/28445469.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
