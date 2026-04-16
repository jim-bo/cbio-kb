---
name: Prostate Cancer (MSK, 2024)
studyId: prostate_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 3244
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [targeted-panel, whole-exome-seq]
panels: []
tags:
  - prostate-cancer
  - prad
  - msk-impact
  - msi
  - tmb
  - immunotherapy
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# Prostate Cancer (MSK, 2024)

## Overview

Large single-center retrospective cohort of 2,257 prostate cancer ([PRAD](../cancer_types/PRAD.md)) patients treated at Memorial Sloan Kettering Cancer Center from April 2015 to February 2021, with 3,244 tumors sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md). Designed to characterize MSI-H/dMMR and TMB-H/MSS prostate cancers and evaluate their response to immune checkpoint blockade. Data deposited in cBioPortal as `prostate_msk_2024`. [PMID:38949888](../papers/38949888.md)

## Composition

- 2,257 patients; 3,244 tumors sequenced with MSK-IMPACT. [PMID:38949888](../papers/38949888.md)
- MSI-H/dMMR: 63 (2.8%); TMB-H/MSS: 33 (1.5%); TMB-L/MSS: 2,161 (95.7%). [PMID:38949888](../papers/38949888.md)
- WES performed on 48 tumor samples (20 MSI-H/dMMR, 28 TMB-H/MSS) via recapture of MSK-IMPACT libraries. [PMID:38949888](../papers/38949888.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted NGS. [PMID:38949888](../papers/38949888.md)
- Whole-exome sequencing ([WES](../methods/whole-exome-seq.md)) on selected samples. [PMID:38949888](../papers/38949888.md)
- [FACETS](../methods/facets.md) (v0.5.6) for copy-number analysis. [PMID:38949888](../papers/38949888.md)
- MSIsensor (v0.5) for MSI status; TMB defined as non-synonymous mutations per megabase in canonical exons. [PMID:38949888](../papers/38949888.md)

## Papers using this cohort

- [PMID:38949888](../papers/38949888.md) — Microsatellite Instability, Tumor Mutational Burden, and Response to Immune Checkpoint Blockade in Patients with Prostate Cancer.

## Notable findings derived from this cohort

- MSI-H/dMMR tumors had significantly higher TMB than TMB-H/MSS (median 41 vs. 15 mut/Mb, P<0.01). Both MSI-H/dMMR (62%) and TMB-H/MSS (59%) tumors more commonly Gleason grade group 5. [PMID:38949888](../papers/38949888.md)
- ICB response in MSI-H/dMMR (n=27): 45% RECIST ORR (including 2 CRs, 7 PRs); 65% PSA50 response. In TMB-H/MSS (n=8): 0% RECIST response; 50% PSA50 response. [PMID:38949888](../papers/38949888.md)
- Median rPFS tended to favor MSI-H/dMMR vs. TMB-H/MSS (38 vs. 7 months, HR 2.13, P=0.14). [PMID:38949888](../papers/38949888.md)
- WES: MSI-H/dMMR tumors had significantly higher neoantigen burden (11.1 vs. 6.8, P=0.011) and indel burden vs. TMB-H/MSS. [PMID:38949888](../papers/38949888.md)

## Sources

- cBioPortal study `prostate_msk_2024` [PMID:38949888](../papers/38949888.md).

*This page was processed by **entity-page-writer** on **2026-04-11**.*
