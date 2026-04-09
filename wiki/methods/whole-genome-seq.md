---
name: Whole-genome sequencing (WGS)
slug: whole-genome-seq
kind: method
unverified: true
tags: [sequencing, wgs]
processed_by: crosslinker
processed_at: 2026-04-08
---

# Whole-genome sequencing (WGS)

## Overview

Unbiased short-read sequencing of the entire tumor (and matched normal) genome, used in the corpus for structural variant detection, mutational signature analysis at non-coding sites, evolutionary timing, and microbiome read mining.

## Used by

- [PMID:35927489](../papers/35927489.md) — 177 WGS samples in the CLL-map cohort; identified 681 SV breakpoints in 141 patients (~4.8/patient), [BCL2](../genes/BCL2.md) translocations predominantly in M-CLL via aberrant V(D)J, and a recurrent 37-Mb chr14 deletion disrupting [ZFP36L1](../genes/ZFP36L1.md) (and [DICER1](../genes/DICER1.md), [TRAF3](../genes/TRAF3.md)) in U-CLL via class-switch recombination. Supported mutational signature analysis (canonical AID SBS84 enriched in U-CLL clustered mutations; non-canonical AID SBS85 enriched in M-CLL, p=1.6×10^-9; plus SBS18) [PMID:35927489](../papers/35927489.md).
- [PMID:36723991](../papers/36723991.md) — WGS on FACS-purified Hodgkin and Reed Sternberg cells from 25 cHL patients with matched intratumoral T cells as germline; established the first comprehensive WGS landscape of cHL, with median post-artifact-removal mutational burden of 5,279 SBS+indels per genome (range 1,880–18,883), prevalent APOBEC mutagenesis (SBS2/SBS13), AID off-target activity, chromothripsis, and timing of WGD as a late event [PMID:36723991](../papers/36723991.md).
- [PMID:37202560](../papers/37202560.md) — tumor WGS in the AC-ICAM colon cancer atlas, used for microbiome read mining alongside 16S rRNA sequencing [PMID:37202560](../papers/37202560.md).

## Notes

- Small WGS cohorts in some corpus papers (e.g., n=25 in cHL, 177 in CLL) are repeatedly cited as a limitation for SV and rare-variant inference [PMID:35927489](../papers/35927489.md) [PMID:36723991](../papers/36723991.md).
- HRS-cell WGS in cHL required whole-genome amplification, introducing palindromic SBS artifacts that had to be computationally removed [PMID:36723991](../papers/36723991.md).

## Sources

- [PMID:35927489](../papers/35927489.md)
- [PMID:36723991](../papers/36723991.md)
- [PMID:37202560](../papers/37202560.md)

*This page was processed by **crosslinker** on **2026-04-08**.*
