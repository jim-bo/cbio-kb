---
studyId: cll_broad_2022
name: "Chronic Lymphocytic Leukemia (Broad, Nature Genetics 2022)"
description: "Whole genome and whole exome sequencing of 1,154 samples from 1,148 patients with Chronic Lymphocytic Leukemia and monoclonal B cell lymphocytosis and their matched normals."
cancerTypeId: cllsll
pmid: "35927489"
allSampleCount: 1
processed_by: crosslinker
processed_at: 2026-04-08
---

# Chronic Lymphocytic Leukemia (Broad, Nature Genetics 2022)

## Overview

Largest integrated CLL cohort to date, combining WES/WGS, [RNA-seq](../methods/rna-seq.md), and DNA methylation data from 1,148 patients to build a "CLL map" of drivers, subtypes, and prognostic features [PMID:35927489](../papers/35927489.md).

## Composition

- 1,148 patients (1,095 [CLLSLL](../cancer_types/CLLSLL.md), 54 [MBL](../cancer_types/MBL.md)); WES/WGS n=1,074 (984 WES, 177 WGS), [RNA-seq](../methods/rna-seq.md) n=712 (603 treatment-naive used for clustering), DNA methylation n=999 (450k array n=490, [RRBS](../methods/rrbs.md) n=509) [PMID:35927489](../papers/35927489.md).
- Contexts: active surveillance (n=680), post-treatment (n=52), clinical trial enrollment (n=416; 371 treatment-naive, 45 relapsed/refractory) [PMID:35927489](../papers/35927489.md).

## Assays / panels (linked)

- [Whole-exome](../methods/whole-exome-seq.md) and [whole-genome sequencing](../methods/whole-genome-seq.md), [RNA-seq](../methods/rna-seq.md), [RRBS](../methods/rrbs.md), [450k methylation array](../methods/450k-methylation-array.md); SV calls via [IgCaller](../methods/igcaller.md); 3-D mutation clustering via [CLUMPS](../methods/clumps.md); timing via [PhylogicNDT](../methods/phylogicndt.md) [PMID:35927489](../papers/35927489.md).

## Papers using this cohort

- [PMID:35927489](../papers/35927489.md) — Knisbacher et al., Molecular map of CLL and its impact on outcome.

## Notable findings derived from this cohort

- 202 candidate genetic drivers nominated (109 novel); top drivers [SF3B1](../genes/SF3B1.md) 17.5%, [NOTCH1](../genes/NOTCH1.md) 12.3%, [ATM](../genes/ATM.md) 11.2%, [TP53](../genes/TP53.md) 9.1%; 24.2% of patients carried at least one novel driver mutation [PMID:35927489](../papers/35927489.md).
- U-CLL harbors substantially more significant drivers than M-CLL (54 vs 25; ratio 2.16, Binomial p=0.0015); fraction of patients with no identifiable driver dropped to 3.8% (from 8.9% in prior work), concentrated in M-CLL [PMID:35927489](../papers/35927489.md).
- 8 robust [RNA-seq](../methods/rna-seq.md) expression clusters in treatment-naive patients serve as independent prognostic factors beyond IGHV/epitype; integrated genetic+epigenetic+transcriptomic outcome model built [PMID:35927489](../papers/35927489.md).
- In contemporary ibrutinib/venetoclax era, [TP53](../genes/TP53.md) mutation in the absence of 17p deletion was not associated with adverse outcomes in U-CLL [PMID:35927489](../papers/35927489.md).

## Sources

- cBioPortal study `cll_broad_2022` [PMID:35927489](../papers/35927489.md).

*This page was processed by **crosslinker** on **2026-04-08**.*
