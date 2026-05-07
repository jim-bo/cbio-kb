---
name: Neuroblastoma (AMC, 2012)
studyId: nbl_amc_2012
institution: Academic Medical Center Amsterdam
size: 3
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [PROTEOMICS]
panels: []
tags: [neuroblastoma, proteomics, LC-MS-MS, EV]
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Neuroblastoma (AMC, 2012)

## Overview

This dataset from the Academic Medical Center Amsterdam encompasses proteomic profiling of neuroblastoma cell lines using label-free LC-MS/MS. The study focused on characterizing extracellular vesicle (EV) proteomes from neuroblastoma cell lines with differing [MYCN](../genes/MYCN.md) amplification status and transcriptional programs (adrenergic vs. mesenchymal), using a metabolic labelling strategy (ManNAz/click chemistry) to selectively isolate tumor-derived EVs from native serum.

## Composition

- Three neuroblastoma cell lines: SH-EP2 (mesenchymal, MYCN-non-amplified), SH-SY5Y (adrenergic, MYCN-non-amplified), and Kelly (adrenergic, MYCN-amplified).
- Survival validation using three publicly available transcriptomic datasets: Kocak (GSE45547; n = 476), Versteeg (GSE16476; n = 88), and NREC (GSE85047; n = 220).
- DepMap CRISPR dependency screens across >1100 cancer cell lines (37 neuroblastoma lines) used for [GJC1](../genes/GJC1.md) dependency analysis.
- Cancer type: [NBL](../cancer_types/NBL.md).

## Assays / panels (linked)

- [LC-MS/MS proteomics](../methods/lc-ms-ms-proteomics.md): Label-free quantitative proteomic profiling of tumor-derived extracellular vesicles.
- ManNAz metabolic labelling + copper-catalysed click chemistry for selective tumor EV isolation from native serum.

## Papers using this cohort

- [PMID:22367537](../papers/22367537.md) — Primary proteomic study identifying GJC1 as a neuroblastoma EV surface marker.

## Notable findings derived from this cohort

- GJC1 (connexin 45) identified as a pan-neuroblastoma EV surface marker through LC-MS/MS; high expression correlated with poor overall survival in three independent transcriptomic datasets [PMID:22367537](../papers/22367537.md).
- ManNAz labelling selectively isolated tumor-derived EVs from native serum without altering EV composition (94.2% protein overlap, Pearson r = 0.998) [PMID:22367537](../papers/22367537.md).
- GJC1 was not detected in EVs from healthy adult donor plasma, suggesting tumor specificity for liquid biopsy applications [PMID:22367537](../papers/22367537.md).

## Sources

- [PMID:22367537](../papers/22367537.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
