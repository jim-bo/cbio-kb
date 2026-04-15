---
name: Colon Cancer (Sidra-LUMC AC-ICAM, Nat Med 2023)
studyId: coad_silu_2022
institution: 
size: 
reference_genome: GRCh37
canonical_source: 
unverified: 
assays: []
panels: []
tags: []
processed_by: crosslinker
processed_at: 2026-04-08
description: Whole exome and transcriptome sequencing of 348 Colon Cancers and their matched normals from Sidra-LUMC AC-ICAM.
cancerTypeId: coad
pmid: 37202560
allSampleCount: 1
---

# Colon Cancer (Sidra-LUMC AC-ICAM, Nat Med 2023)

## Overview

AC-ICAM (Sidra-LUMC Atlas and Compass of Immune-Cancer-Microbiome interactions) is a multi-omics resource of 348 treatment-naive primary colon cancers profiled with [RNA-seq](../methods/rna-seq.md), WES, [TCR-seq](../methods/tcr-seq.md), 16S rRNA-seq, and tumor WGS on paired tumor/normal colon tissue [PMID:37202560](../papers/37202560.md).

## Composition

- 348 treatment-naive patients with primary [colon adenocarcinoma](../cancer_types/COAD.md); fresh-frozen tumor and matched healthy colon tissue; median follow-up 4.6 years [PMID:37202560](../papers/37202560.md).
- Additional ICAM42 subset (n=42) profiled with 16S rRNA sequencing [PMID:37202560](../papers/37202560.md).

## Assays / panels (linked)

- [RNA-seq](../methods/rna-seq.md), [whole-exome sequencing](../methods/whole-exome-seq.md), [deep TCRβ sequencing](../methods/tcr-seq.md), [16S rRNA gene sequencing](../methods/16s-rrna-seq.md), and tumor [whole-genome sequencing](../methods/whole-genome-seq.md) [PMID:37202560](../papers/37202560.md).

## Papers using this cohort

- [PMID:37202560](../papers/37202560.md) — Roelands et al., integrated tumor, immune and microbiome atlas of colon cancer. TCGA-COAD was used as a comparator due to limited survival follow-up and tumor-purity selection constraints [PMID:37202560](../papers/37202560.md).

## Notable findings derived from this cohort

- Consensus clustering on the 20-gene [ICR signature](../methods/icr-signature.md) segregated AC-ICAM into ICR-high/medium/low subtypes; ICR-high vs ICR-low HR 0.54 (95% CI 0.34–0.86, P=0.0095) [PMID:37202560](../papers/37202560.md).
- ICR outperformed [CMS](../methods/cms-classifier.md) and MSI classifications for prognosis and retained prognostic value within CMS4/mesenchymal tumors [PMID:37202560](../papers/37202560.md).
- Quantifying [genetic immunoediting](../methods/immunoediting-quantification.md) further refined ICR's prognostic value, and a *Ruminococcus bromii*-driven microbiome signature combined with ICR (mICRoScore) identified a subgroup with excellent survival [PMID:37202560](../papers/37202560.md).

## Sources

- cBioPortal study `coad_silu_2022` [PMID:37202560](../papers/37202560.md).

*This page was processed by **crosslinker** on **2026-04-08**.*
