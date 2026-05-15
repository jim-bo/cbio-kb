---
name: METABRIC Targeted Sequencing
slug: metabric-targeted-sequencing
kind: method
canonical_source: corpus
unverified: true
tags: [targeted-sequencing, breast-cancer, panel-sequencing]
processed_by: crosslinker
processed_at: 2026-05-14
---

# METABRIC Targeted Sequencing

## Overview

The METABRIC targeted sequencing panel is a custom 173-gene targeted capture assay designed for the Molecular Taxonomy of Breast Cancer International Consortium (METABRIC). The 173-gene list was assembled from five large breast-cancer sequencing studies published in 2012 plus genes recurrently homozygously deleted in the prior METABRIC copy-number analysis. Sequencing was performed using Illumina Nextera Custom Target Enrichment with paired-end 100 bp reads on a HiSeq 2000 platform, achieving a mean depth ≥112× in 80% of samples (median 152×). The panel covers approximately 1.2 Mbp of the genome.

## Used by

- [Pereira et al. 2016 — METABRIC breast cancer landscape](../papers/27161491.md): Applied to 2,433 primary breast tumours ([BRCA](../cancer_types/BRCA.md)) with 650 matched normals (523 normal-adjacent breast, 127 peripheral blood) and 548 matched tumor/normal pairs; 221 tumors sequenced in replicate for quality control; identified 40 Mut-driver genes across ER+ and ER- disease; revealed IntClust-specific mutation enrichment and [PIK3CA](../genes/PIK3CA.md) prognostic context-dependence [PMID:27161491](../papers/27161491.md).

## Notes

- The panel targets ~1.2 Mbp; genome-wide events outside the 173-gene list are not detectable (a stated limitation of the study).
- 173-gene selection was retrospective (based on 2012 knowledge); more recently nominated drivers are under-represented.
- Mutation calling used panel-of-normals filtering analogous to MuTect; LOH and CCF estimated via ASCAT.
- The large cohort size (n=2,433) compensates for the panel's limited breadth, enabling detection of low-frequency drivers.
- Coverage: ~1.2 Mbp; not genome-wide and not exome-wide.

## Sources

- [PMID:27161491](../papers/27161491.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
