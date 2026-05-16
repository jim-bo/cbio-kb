---
name: PKU Pan-Asia cHCC-ICC Multi-Omic Cohort (2019)
studyId: hccihch_pku_2019
institution: Peking University (PKU), multi-center (8 hospitals, China/Singapore/Japan)
size: 133
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - single-nucleus-seq
panels: []
tags:
  - liver-cancer
  - HCC
  - cholangiocarcinoma
  - cHCC-ICC
  - HBV
  - pan-Asia
  - multi-omic
  - integrative
processed_by: crosslinker
processed_at: 2026-05-16
---

# PKU Pan-Asia cHCC-ICC Multi-Omic Cohort (2019)

## Overview

Xue et al. (*Hepatology* 2019, [PMID:31130341](../papers/31130341.md)) performed a pan-Asia multi-center integrative genomic and transcriptomic study of 133 combined hepatocellular and intrahepatic cholangiocarcinoma (cHCC-ICC) cases — a rare primary liver cancer showing both hepatocellular and biliary differentiation. The dataset is deposited as `hccihch_pku_2019` on cBioPortal. Patients were enrolled across 8 hospitals in China, Singapore, and Japan; 75% were HBV-positive. Reference cohorts used for comparison include [lihc_tcga_pan_can_atlas_2018](../datasets/lihc_tcga_pan_can_atlas_2018.md) (TCGA-HCC), [lihc_riken](../datasets/lihc_riken.md) (RIKEN-HCC), and [chol_icgc_2017](../datasets/chol_icgc_2017.md) (ICGC-ICC).

## Composition

- **133 cHCC-ICC cases** from 8 pan-Asia centers; Allen-Lisa subtypes: 6 separate (Sep), 56 combined (Com), 59 mixed (Mix).
- Etiology: 100 HBV+, 7 HCV+, 1 double-positive, 25 double-negative.
- WES: 173 tumor samples / 121 cases (mean 108x tumor / 101x normal depth).
- WGS: 41 tumor samples / 37 cases.
- RNA-seq: 97 tumor samples / 77 cases.
- Single-nucleus sequencing (SNS): 1 mixed-type case (74 tumor + 11 normal nuclei).
- IHC validation: Nestin on 128 cHCC-ICC, 99 [HCC](../cancer_types/HCC.md), and 86 ICC cases.
- Laser capture microdissection used to separate HCC and ICC components in 3 separate-type and 41 combined-type cases.
- Cancer type: [MIXED](../cancer_types/MIXED.md) (cHCC-ICC); reference arms span [HCC](../cancer_types/HCC.md) and [IHCH](../cancer_types/IHCH.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 173 tumor samples
- [whole-genome-seq](../methods/whole-genome-seq.md) — 41 tumor samples
- [rna-seq](../methods/rna-seq.md) — 97 tumor samples
- [single-cell-dna-seq](../methods/single-cell-dna-seq.md) — 1 mixed-type case (74 tumor nuclei)
- [immunohistochemistry](../methods/immunohistochemistry.md) — Nestin IHC on 313 liver cancer specimens
- [sigprofiler](../methods/sigprofiler.md) — mutational signature analysis
- [pyclone](../methods/pyclone.md) — clonal phylogenetic reconstruction

## Papers using this cohort

- [PMID:31130341](../papers/31130341.md) — Xue et al. 2019, *Hepatology*: defining publication for this dataset.

## Notable findings derived from this cohort

- Significantly mutated genes (dNdScv q < 0.1): [TP53](../genes/TP53.md) (49.2%), [AXIN1](../genes/AXIN1.md), [RB1](../genes/RB1.md), [PTEN](../genes/PTEN.md), [ARID2](../genes/ARID2.md), and [BRD7](../genes/BRD7.md); [TP53](../genes/TP53.md) rate significantly higher than TCGA-HCC (31%, p<0.001) or ICGC-ICC (22%, p<0.0001) [PMID:31130341](../papers/31130341.md).
- [TERT](../genes/TERT.md) promoter C228T mutation in 22.9% of cases; HBV integrations recurrently targeted TERT and [KMT2B](../genes/KMT2B.md); AFB1 mutational signature (COSMIC 24) in 38.8% with TP53 R249S hotspot confined to HBV+ patients [PMID:31130341](../papers/31130341.md).
- Combined-type cHCC-ICC is molecularly ICC-like (enriched in transcriptomic cluster P1, biliary markers); mixed-type is HCC-like (Hoshida-S2, enriched in P2, high AFP); both subtypes show significantly poorer prognosis than P3/P4 HCC clusters [PMID:31130341](../papers/31130341.md).
- Nestin ([NES](../genes/NES.md)) IHC-positive in 81.3% of cHCC-ICC vs HCC/ICC controls (p<0.001); Nestin-positive patients had median [OS](../cancer_types/OS.md) 18.7 months vs 46.6 months for Nestin-negative across all primary liver cancers (p<0.0001, log-rank) [PMID:31130341](../papers/31130341.md).
- Paradoxically low [CTNNB1](../genes/CTNNB1.md) (6%) and zero [KRAS](../genes/KRAS.md) mutation frequencies distinguish cHCC-ICC from both HCC and ICC reference cohorts; separate-type and combined-type tumors show monoclonal origin with branched evolution [PMID:31130341](../papers/31130341.md).

## Sources

- cBioPortal study: `hccihch_pku_2019`
- Xue et al. *Hepatology* 2019. [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
