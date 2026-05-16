---
name: GRAIL 508-gene cfDNA panel
slug: grail_cfdna_508
kind: method
canonical_source: cbioportal
unverified: false
tags: [liquid-biopsy, cfdna, ctdna, targeted-sequencing, clonal-hematopoiesis]
processed_by: crosslinker
processed_at: 2026-05-16
---

# GRAIL 508-gene cfDNA panel

## Overview

High-intensity targeted sequencing assay developed by GRAIL covering 508 cancer-relevant genes spanning ~2 Mb of the genome. Applied simultaneously to plasma cell-free DNA (cfDNA) and matched white-blood-cell (WBC) buffy-coat DNA. Uses unique molecular identifiers (UMIs) to achieve an error rate of 1×10⁻⁵ to 3×10⁻⁵ with >60,000X raw sequencing depth (~4,400X median collapsed target depth). 95% limit of detection approximately 0.36% VAF at 30 ng cfDNA input. Designed to detect tumor-derived mutations (ctDNA), clonal hematopoiesis (CH) variants, copy-number variations, mutational signatures, and MSI status from a single blood draw.

## Used by

- Prospective cfDNA profiling of 124 patients with metastatic breast cancer ([MBC](../cancer_types/MBC.md)), [NSCLC](../cancer_types/NSCLC.md), or castration-resistant prostate cancer (CRPC) plus 47 non-cancer controls at MSKCC; matched WBC sequencing revealed that 53.2% of cancer-patient cfDNA somatic variants and 81.6% of control variants were attributable to clonal hematopoiesis — demonstrating the requirement for paired WBC subtraction. De novo detection of at least one tumor-derived mutation was achieved in 84% (104/124) of cancer patients [PMID:31768066](../papers/31768066.md).

## Notes

- Requires matched WBC gDNA sequencing alongside cfDNA; without WBC subtraction, canonical CH genes (especially [TP53](../genes/TP53.md), [DNMT3A](../genes/DNMT3A.md), [TET2](../genes/TET2.md), [PPM1D](../genes/PPM1D.md)) are systematically mis-called as tumor-derived variants.
- CNV detection from cfDNA is reliable only when ctDNA fraction ≥10%; actionable amplifications (e.g., [ERBB2](../genes/ERBB2.md), [MET](../genes/MET.md)) at lower fractions require orthogonal tissue confirmation.
- MSI detection is supported via a depth-adjusted [MSIsensor](../methods/msisensor.md) implementation; one CRPC patient identified as MSI-H from cfDNA responded to anti-PD-L1 therapy.
- Canonical genePanelId in cBioPortal: `grail_cfdna_508`.
- Dataset deposited as [cfdna_msk_2019](../datasets/cfdna_msk_2019.md).

## Sources

- [PMID:31768066](../papers/31768066.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
