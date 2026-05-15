---
name: Acral Melanoma
oncotree_code: ACRM
main_type: Melanoma
parent: MEL
tags:
  - melanoma
  - acral
  - skin-cancer
  - structural-variation
  - tert
processed_by: crosslinker
processed_at: 2026-05-14
---

# Acral Melanoma (ACRM)

## Overview

Acral melanoma (acral lentiginous melanoma, ALM) is a rare melanoma subtype arising on sun-shielded acral surfaces (palms, soles, nail beds). Unlike cutaneous melanoma ([SKCM](../cancer_types/SKCM.md)), it occurs predominantly in non-White populations and shows a worse prognosis. Genomically, it is dominated by structural variation (SVs) rather than UV-derived single-nucleotide variants, with a low UV mutational signature, low SNV burden (median 42 coding mutations per tumor), high SV burden (median 31 somatic breakpoints), and under-representation of canonical BRAF/NRAS/NF1 drivers. It occupies OncoTree position ACRM under [MEL](../cancer_types/MEL.md) (Melanoma), skin tissue.

## Cohorts in the corpus

- **[mel_tsam_liang_2017](../datasets/mel_tsam_liang_2017.md)** — 38 ALM tumors from 34 patients at Vanderbilt University and MSKCC; whole-exome sequencing (33 patients), long-insert whole-genome sequencing (31 patients), RNA-seq (33 patients), Sanger [TERT](../genes/TERT.md) promoter sequencing (28 patients); raw data deposited in dbGaP `phs001036.v1.p1` [PMID:28373299](../papers/28373299.md).

## Recurrent alterations

- [TERT](../genes/TERT.md) — aberrations in 41% (14/34) of patients, encompassing consensus CNV gains at the TERT-CLPTM1L locus (Chr 5p), promoter mutations in 4/28 (Chr5:1,295,113:G>A), one exonic missense (F919L), intronic SNV, and SV breakpoints in 4 patients; all patients with somatic TERT events expressed TERT; Telomerase Inhibitor IX produced ≥75% loss of viability in two primary ALM lines in vitro [PMID:28373299](../papers/28373299.md).
- [PAK1](../genes/PAK1.md) — focal copy gains in 5/34 (15%) patients, exclusively in BRAF/NRAS wild-type tumors (1 NF1-subtype, 4 triple-wild-type); validated by qPCR in 4/5; elevated [PAK1](../genes/PAK1.md) expression in 2/5; proposed as an alternative MAPK-pathway dysregulation route in triple-wild-type ALM [PMID:28373299](../papers/28373299.md).
- [BRAF](../genes/BRAF.md) — mutated in 6/34 (18%) patients: V600E (4 patients, 12%), V600K+R462K (1), G466E (1); mutually exclusive of [NRAS](../genes/NRAS.md); UV signature present in 2 BRAF-mutant tumors [PMID:28373299](../papers/28373299.md).
- [NRAS](../genes/NRAS.md) — 4 patients: Q61K (3, 9%), A59G (1); mutually exclusive of [BRAF](../genes/BRAF.md) [PMID:28373299](../papers/28373299.md).
- [NF1](../genes/NF1.md) — homozygous loss in 9% (3 patients); LOH plus E2578* nonsense in a fourth patient; combined prevalence 12% [PMID:28373299](../papers/28373299.md).
- [CDKN2A](../genes/CDKN2A.md) — recurrent deletion (Chr 9), statistically significant in both primary and metastatic subsets [PMID:28373299](../papers/28373299.md).
- [CDK4](../genes/CDK4.md) — recurrent copy gain (Chr 12), significant in metastases [PMID:28373299](../papers/28373299.md).
- [CLPTM1L](../genes/CLPTM1L.md) — frequent SV breakpoints in 15% of patients and consensus copy gain on Chr 5p adjacent to TERT [PMID:28373299](../papers/28373299.md).
- [ADCY2](../genes/ADCY2.md) — most-rearranged gene in the cohort: 32 breakpoints across 7 samples (21% of patients); partners include [CLPTM1L](../genes/CLPTM1L.md), TERT, [HECTD4](../genes/HECTD4.md), [UBE2QL1](../genes/UBE2QL1.md) [PMID:28373299](../papers/28373299.md).
- [MDM2](../genes/MDM2.md) — copy gain in metastases only; [MDM2](../genes/MDM2.md):GNS and MDM2:CCT2 RNA fusions detected [PMID:28373299](../papers/28373299.md).
- [KIT](../genes/KIT.md) — single L576P mutation (1 patient) [PMID:28373299](../papers/28373299.md).

## Subtypes

- **BRAF/NRAS-mutant ALM** (~29% combined): lower UV signature in most; 2 BRAF-mutant cases showed UV signature.
- **NF1-subtype ALM** (~12%): homozygous [NF1](../genes/NF1.md) loss or biallelic inactivation.
- **Triple-wild-type ALM** (BRAF/NRAS/NF1-wild-type, ~59%): enriched for PAK1 copy gains (all 5 PAK1-gain patients were triple-wild-type or NF1-subtype) and structural variation [PMID:28373299](../papers/28373299.md).

## Therapeutic landscape

- **[Telomerase Inhibitor IX](../drugs/telomerase-inhibitor-ix.md)** — in vitro, 2.5 µM for 72 h reduced viability ≥75% in two primary ALM cell lines (TERT CNV gain and TERT promoter mutation) versus ~12% in normal melanocytes; authors propose TERT inhibition as a therapeutic strategy given limited targeted options in ALM [PMID:28373299](../papers/28373299.md).
- **[Ipilimumab](../drugs/ipilimumab.md) / [Pembrolizumab](../drugs/pembrolizumab.md)** — immune checkpoint blockade administered to 22/34 patients; three complete responders had paradoxically low mutation (<75) and neo-antigen (<60) burdens, distinct from the pattern in cutaneous melanoma; response mechanism unclear [PMID:28373299](../papers/28373299.md).
- **MAPK-directed therapy** — [BRAF](../genes/BRAF.md)/[NRAS](../genes/NRAS.md) drivers actionable in ~29%; PAK1 copy gains (15%) nominated as an alternative MAPK target in triple-wild-type ALM [PMID:28373299](../papers/28373299.md).

## Sources

- [PMID:28373299](../papers/28373299.md) — Liang et al. 2017; integrated WES/LIWGS/RNA-seq of 38 ALM tumors; first comprehensive genomic landscape of ACRM.

*This page was processed by **crosslinker** on **2026-05-14**.*
