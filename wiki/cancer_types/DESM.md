---
name: Desmoplastic Melanoma
oncotree_code: DESM
main_type: Melanoma
parent: MEL
tags:
  - melanoma
  - skin
  - uv-signature
  - high-tmb
  - nfkbie
processed_by: crosslinker
processed_at: 2026-05-14
---

# Desmoplastic Melanoma (DESM)

## Overview

Desmoplastic melanoma (DESM) is a rare, deeply invasive cutaneous melanoma variant characterized by prominent stromal desmoplasia and spindled neoplastic melanocytes. It sits at OncoTree level 3 under [MEL](../cancer_types/MEL.md) (Melanoma), tissue: Skin. Desmoplastic melanoma is genetically distinct from common-type cutaneous melanoma: it carries an exceptionally high mutation burden (median 62 mutations/Mb) driven by a UV-radiation C>T mutational signature, yet is conspicuously devoid of canonical [BRAF](../genes/BRAF.md) V600E and [NRAS](../genes/NRAS.md) Q61K/R drivers. MAPK/PI3K pathway activation is instead achieved through a diverse, non-mutually-exclusive set of alterations in [NF1](../genes/NF1.md), [CBL](../genes/CBL.md), [ERBB2](../genes/ERBB2.md), [MAP2K1](../genes/MAP2K1.md), [MAP3K1](../genes/MAP3K1.md), [EGFR](../genes/EGFR.md), and others, affecting 73% of tumors. The high TMB positions DESM as a strong candidate for immune checkpoint blockade.

## Cohorts in the corpus

- [desm_broad_2015](../datasets/desm_broad_2015.md) — 62 desmoplastic melanomas: 20 fresh-frozen (discovery; 10 MSKCC, 10 Melanoma Institute Australia) with whole-genome + exome sequencing (13× and 89×), and 42 FFPE tumors (validation; UCSF) with targeted sequencing of 293 genes at 216× [PMID:26343386](../papers/26343386.md).

## Recurrent alterations

- [TERT](../genes/TERT.md) — promoter mutations in 85% (17/20) of evaluable samples; overall [TERT](../genes/TERT.md) activation (promoter + amplification) in 90% of tumors [PMID:26343386](../papers/26343386.md).
- [NFKBIE](../genes/NFKBIE.md) — novel recurrent promoter hotspot mutations in 14.5% of tumors (15/62); evidence for biallelic selection; not found in COSMIC or TCGA across any cancer type; proposed gain-of-function suppressing NFκB signaling [PMID:26343386](../papers/26343386.md).
- [CDKN2A](../genes/CDKN2A.md) — focal deletions in 11/62 cases; LOF mutations; p16 loss confirmed by IHC [PMID:26343386](../papers/26343386.md).
- [BRAF](../genes/BRAF.md) — V600E **absent**; kinase-impaired G466E/G469E/D594N substitutions in 3 tumors (paradoxically activate MAPK via CRAF) [PMID:26343386](../papers/26343386.md).
- [NRAS](../genes/NRAS.md) — canonical Q61K/R **absent**; atypical Q61H in 1 tumor [PMID:26343386](../papers/26343386.md).
- [NF1](../genes/NF1.md) — LOF mutations and focal deletions in 4 cases [PMID:26343386](../papers/26343386.md).
- [CBL](../genes/CBL.md) — frequent truncating/damaging missense mutations with no synonymous mutations; supports tumor-suppressor role [PMID:26343386](../papers/26343386.md).
- [ERBB2](../genes/ERBB2.md) — recurrent S310F hotspot in 4/62 tumors [PMID:26343386](../papers/26343386.md).
- [EGFR](../genes/EGFR.md) — focal amplifications in 3 tumors; IHC-confirmed overexpression [PMID:26343386](../papers/26343386.md).
- [MAP2K1](../genes/MAP2K1.md) — P124S/L hotspot in 2 tumors [PMID:26343386](../papers/26343386.md).
- [MAP3K1](../genes/MAP3K1.md) — focal amplifications in 3 tumors; novel finding in melanoma [PMID:26343386](../papers/26343386.md).
- [PTPN11](../genes/PTPN11.md) — E76A/K hotspot in 2 tumors [PMID:26343386](../papers/26343386.md).
- [MET](../genes/MET.md) — focal amplifications in 2 tumors; IHC-confirmed [PMID:26343386](../papers/26343386.md).
- [RAC1](../genes/RAC1.md) — P29S hotspot in 2 tumors [PMID:26343386](../papers/26343386.md).
- [TP53](../genes/TP53.md) — top LOF-burden candidate; IHC-confirmed protein-level alteration [PMID:26343386](../papers/26343386.md).
- [FBXW7](../genes/FBXW7.md) — truncating/WD-domain damaging mutations in 11% of tumors [PMID:26343386](../papers/26343386.md).
- [ARID2](../genes/ARID2.md), [ARID1A](../genes/ARID1A.md) — inactivating SWI/SNF mutations; [ARID1A](../genes/ARID1A.md) IHC-confirmed [PMID:26343386](../papers/26343386.md).
- [RB1](../genes/RB1.md) — LOF mutations; IHC-confirmed protein loss [PMID:26343386](../papers/26343386.md).
- Extreme mutation burden (median 62 mutations/Mb) with dominant UV-radiation C>T signature (88% of mutations); older patients (>55 years) had significantly more mutations (p=2×10⁻³) [PMID:26343386](../papers/26343386.md).

## Subtypes

- Pure and mixed desmoplastic subtypes are genetically similar based on the discovery/validation cohort analysis [PMID:26343386](../papers/26343386.md).
- Tumors from sun-shielded sites had the lowest mutation burdens; one such tumor carried a germline [CDKN2A](../genes/CDKN2A.md) mutation [PMID:26343386](../papers/26343386.md).

## Therapeutic landscape

- BRAF V600-directed inhibitors ([vemurafenib](../drugs/vemurafenib.md), [dabrafenib](../drugs/dabrafenib.md) + [trametinib](../drugs/trametinib.md)) are **not** appropriate for desmoplastic melanoma due to absence of BRAF V600E and NRAS Q61K/R [PMID:26343386](../papers/26343386.md).
- Targetable RTK/MAPK alterations identified in 73% of tumors; small-molecule inhibitors against [MET](../genes/MET.md), EGFR, ERBB2, [IDH1](../genes/IDH1.md), MAP2K1, [PIK3CA](../genes/PIK3CA.md), and [CDK4](../genes/CDK4.md) products represent potential therapeutic avenues [PMID:26343386](../papers/26343386.md).
- Exceptionally high TMB (median 62 mutations/Mb) positions DESM as a strong candidate for immune checkpoint inhibitor therapy [PMID:26343386](../papers/26343386.md).

## Sources

- [PMID:26343386](../papers/26343386.md) — Shain et al. (2015). Whole-genome, exome, and targeted sequencing of 62 desmoplastic melanomas; identified extreme mutation burden, UV signature, absence of BRAF V600E/NRAS canonical drivers, novel [NFKBIE](../genes/NFKBIE.md) promoter hotspot, and diverse MAPK/PI3K activating alterations.

*This page was processed by **crosslinker** on **2026-05-14**.*
