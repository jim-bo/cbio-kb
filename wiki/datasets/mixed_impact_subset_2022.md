---
name: Pan-Cancer MSK-IMPACT MET Validation Cohort (MSK 2022)
studyId: mixed_impact_subset_2022
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 69
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - MET
  - copy-number
  - FISH
  - pan-cancer
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Pan-Cancer MSK-IMPACT MET Validation Cohort (MSK 2022)

## Overview

A FISH-validation cohort used to calibrate a purity/ploidy-aware caller for *MET* copy-number alterations from [MSK-IMPACT](../methods/msk-impact-panel.md) hybrid-capture sequencing, drawn from a landscape screen of 66,285 tumor samples (50,748 patients) at Memorial Sloan Kettering. Name, institution, size (69) and reference genome (hg19) are taken from the cBioPortal study record in `schema/ontology/studies.json`; cBioPortal's 69-sample count is close to but does not exactly match the 70-case FISH validation cohort described in the paper text [PMID:36044468](../papers/36044468.md).

## Composition

- 70 cases with material for MET FISH: 48 with NGS-detected MET copy-number gains at various levels and 22 without MET alterations, spanning 16 primary cancer types (59% lung, incl. [NSCLC](../cancer_types/NSCLC.md)/[SCLC](../cancer_types/SCLC.md); 13% gastrointestinal; 7% [RCC](../cancer_types/RCC.md); 7% glioblastoma ([GB](../cancer_types/GB.md))) [PMID:36044468](../papers/36044468.md).
- Drawn from a broader landscape re-analysis of 408 MET-gained/amplified tumors identified among 50,748 MSK-IMPACT-sequenced patients [PMID:36044468](../papers/36044468.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture panel ([IMPACT341](../methods/IMPACT341.md)–[IMPACT505](../methods/IMPACT505.md)), tumor plus matched blood normal [PMID:36044468](../papers/36044468.md).
- Copy number called with GC-normalized read-depth fold-change and with [FACETS](../methods/facets.md) (allele-specific, purity/ploidy-adjusted); validated against MET [FISH](../methods/fish.md) [PMID:36044468](../papers/36044468.md).

## Papers using this cohort

- [PMID:36044468](../papers/36044468.md) — MSK study, source publication: validates a FACETS-based, focality-aware MET copy-number caller against FISH and applies it across >50,000 sequenced solid tumors.

## Notable findings derived from this cohort

- The standard read-depth fold-change caller agreed with FISH in only 81% of cases; adding FACETS allele-specific copy number plus a focality rule (amplified segment <25 Mb) raised agreement to 91% concordance, 97% sensitivity, 89% specificity, with a recommended minimum 20% tumor content [PMID:36044468](../papers/36044468.md).
- Among 45 patients treated with MET inhibitors, objective responses occurred at all amplification levels, and were highest (67%) with concurrent MET exon 14 alterations, arguing against restricting MET-targeted trials to high-level amplification only [PMID:36044468](../papers/36044468.md).

## Sources

- cBioPortal study record: `mixed_impact_subset_2022` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:36044468](../papers/36044468.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
