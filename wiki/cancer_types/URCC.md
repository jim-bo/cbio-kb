---
name: Unclassified Renal Cell Carcinoma
oncotree_code: URCC
main_type: Renal Cell Carcinoma
parent: NCCRCC
tags:
  - kidney
  - renal
  - unclassified
  - nf2
  - mtorc1
  - fh-deficient
  - hippo-yap
processed_by: crosslinker
processed_at: 2026-05-14
---

# Unclassified Renal Cell Carcinoma (URCC)

## Overview

Unclassified renal cell carcinoma (URCC) is an OncoTree child of [Renal Non-Clear Cell Carcinoma (NCCRCC)](NCCRCC.md) and represents high-grade primary renal tumors that cannot be assigned to any established [RCC](../cancer_types/RCC.md) subtype after rigorous pathologic review. URCC comprises approximately 4–5% of all [RCC](RCC.md). It lacks a standard of care and is molecularly heterogeneous. A landmark MSKCC molecular characterization study of 62 high-grade primary uRCCs using MSK-IMPACT, RNA-seq, OncoScan SNP arrays, FISH, and IHC defined four molecularly distinct subsets covering ~76% of cases: [NF2](../genes/NF2.md) loss (26%), mTORC1-hyperactive (21%), FH-deficient (6%), and [ALK](../genes/ALK.md) translocation (2%), with a chromatin/DNA-damage regulator group (21%) [PMID:27713405](../papers/27713405.md).

## Cohorts in the corpus

- [urcc_mskcc_2016](../datasets/urcc_mskcc_2016.md) — 62 high-grade primary uRCC tumors from MSKCC, re-reviewed by three genitourinary pathologists; all profiled with the 230-gene MSK-IMPACT panel (avg 348x coverage), with RNA-seq (n=7), OncoScan SNP arrays (n=15/16 NF2-loss cases), FISH, and IHC [PMID:27713405](../papers/27713405.md).

## Recurrent alterations

- [NF2](../genes/NF2.md) — mutated in 18% (11/62); biallelic inactivation by mutation plus 22q12 LOH in 13/16 (81%) of the NF2-loss subset; drives Hippo–YAP pathway dysregulation with nuclear YAP/TAZ accumulation; shYAP1 knockdown reverses proliferation phenotype in NF2-loss nccRCC lines (ACHN, LB996-RCC) [PMID:27713405](../papers/27713405.md).
- [SETD2](../genes/SETD2.md) — 18% overall, but 44% within the NF2-loss subset (Fisher P=0.004); complete loss of H3K36me3 mark co-occurs with mutation [PMID:27713405](../papers/27713405.md).
- [BAP1](../genes/BAP1.md) — 13% [PMID:27713405](../papers/27713405.md).
- [KMT2C](../genes/KMT2C.md), [KMT2D](../genes/KMT2D.md), [KMT2A](../genes/KMT2A.md) — chromatin modulators recurrently mutated (~16% combined across KMT2 family) [PMID:27713405](../papers/27713405.md).
- [MTOR](../genes/MTOR.md) — 8% missense; recurrent L2427R (3 cases) functionally activating in 293T co-transfection assays; defines the mTORC1-hyperactive subset together with [TSC1](../genes/TSC1.md), [TSC2](../genes/TSC2.md), and [PTEN](../genes/PTEN.md) [PMID:27713405](../papers/27713405.md).
- [TSC1](../genes/TSC1.md), [TSC2](../genes/TSC2.md), [PTEN](../genes/PTEN.md) — together with [MTOR](../genes/MTOR.md) define the mTORC1-hyperactive subset (n=13, 21%); mutually exclusive across the 16-case set; 7 TSC1/TSC2-mutated tumors show maximal p-4EBP1 (H-score=300) [PMID:27713405](../papers/27713405.md).
- [FH](../genes/FH.md) — defines the FH-deficient subset (n=4, 6%); three confirmed HLRCC cases with germline [FH](../genes/FH.md) mutations; one somatic homozygous FH deletion (T41) represents a novel non-germline mechanism [PMID:27713405](../papers/27713405.md).
- [ALK](../genes/ALK.md) and [TPM3](../genes/TPM3.md) — [TPM3](../genes/TPM3.md)–ALK fusion in T12 (2%); confirmed by ALK break-apart FISH; second adult RCC case with this fusion [PMID:27713405](../papers/27713405.md).
- [VHL](../genes/VHL.md) — only 1/62 mutations (T08); absence of [VHL](../genes/VHL.md) alteration despite frequent 3p loss distinguishes uRCC from [CCRCC](CCRCC.md) [PMID:27713405](../papers/27713405.md).
- [YAP1](../genes/YAP1.md) and [WWTR1](../genes/WWTR1.md) (TAZ) — not mutated but nuclear accumulation marks the NF2-loss subset [PMID:27713405](../papers/27713405.md).
- [TP53](../genes/TP53.md), [CHEK2](../genes/CHEK2.md), [BRCA2](../genes/BRCA2.md) — DNA-damage-response mutations in 5 of the chromatin/DNA-damage group cases [PMID:27713405](../papers/27713405.md).
- [MET](../genes/MET.md) H1094Y and [BRAF](../genes/BRAF.md) Y472C — pathogenic mutations in single cases (T62, T69) suggesting candidate therapeutic targets [PMID:27713405](../papers/27713405.md).

## Subtypes

- **NF2-loss (26%, n=16):** Defined by NF2 mutation and/or 22q12 loss; biallelic inactivation in 81%; Hippo–YAP dysregulation confirmed by RNA-seq GSEA; co-occurrence with [SETD2](../genes/SETD2.md) mutation (44%) causes H3K36me3 loss. Associated with worst cancer-specific and progression-free survival [PMID:27713405](../papers/27713405.md).
- **mTORC1-hyperactive (21%, n=13):** Mutually exclusive MTOR/TSC1/TSC2/PTEN mutations in 16 cases; 13/16 confirmed by p-S6 and p-4EBP1 IHC. Comparatively better clinical course; biologically similar to mTOR-altered [CCRCC](CCRCC.md) where mTOR inhibitors have shown benefit [PMID:27713405](../papers/27713405.md).
- **FH-deficient (6%, n=4):** FH IHC-negative and 2SC-positive; three HLRCC cases plus one case with somatic homozygous FH deletion. Associated with worst survival [PMID:27713405](../papers/27713405.md).
- **ALK-translocation (2%, n=1):** TPM3–ALK fusion; confirms uRCC as an emerging RCC entity with ALK rearrangement [PMID:27713405](../papers/27713405.md).
- **Chromatin/DNA-damage regulator (21%, n=13):** Eight cases with SETD2, [BAP1](../genes/BAP1.md), KMT2A/C/D, [PBRM1](../genes/PBRM1.md) mutations; 5 with [TP53](../genes/TP53.md), [CHEK2](../genes/CHEK2.md), [BRCA2](../genes/BRCA2.md) mutations; intermediate outcome [PMID:27713405](../papers/27713405.md).
- **Other (24%, n=15):** No recurrent molecular feature identified [PMID:27713405](../papers/27713405.md).

## Therapeutic landscape

- mTORC1-hyperactive uRCC (21%): biological rationale for mTOR inhibitor use (MTOR/TSC1/TSC2/PTEN alterations analogous to ccRCC long-term mTOR-inhibitor responders) [PMID:27713405](../papers/27713405.md).
- NF2-loss uRCC: candidate for YAP-pathway inhibitors (e.g., [verteporfin](../drugs/verteporfin.md)); concurrent SETD2 mutation with H3K36me3 loss supports WEE1-inhibitor synthetic-lethality hypothesis [PMID:27713405](../papers/27713405.md).
- FH-deficient cases: genetic counselling for HLRCC recommended [PMID:27713405](../papers/27713405.md).
- ALK-translocation case (TPM3–ALK): candidate for ALK inhibition [PMID:27713405](../papers/27713405.md).

## Sources

- [PMID:27713405](../papers/27713405.md) — Chen et al., first in-depth molecular characterization of 62 MSKCC high-grade uRCCs via MSK-IMPACT; defines four molecularly distinct subsets.

*This page was processed by **crosslinker** on **2026-05-14**.*
