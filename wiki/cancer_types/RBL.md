---
name: Retinoblastoma
oncotree_code: RBL
main_type: Retinoblastoma
parent: EYE
tags: []
canonical_source: oncotree
unverified: false
processed_by: crosslinker
processed_at: 2026-05-16
---

# Retinoblastoma (RBL)

## Overview

Retinoblastoma (OncoTree: RBL) is a pediatric intraocular malignancy arising from retinal precursor cells, classified under the Eye Tumor main type with parent node EYE. The canonical oncogenic event is biallelic inactivation of [RB1](../genes/RB1.md); approximately 1% of cases are instead driven by [MYCN](../genes/MYCN.md) amplification without [RB1](../genes/RB1.md) loss. In heritable disease, a germline RB1 pathogenic variant is followed by somatic loss of the remaining allele; non-heritable unilateral tumors acquire both hits somatically. Modern treatment using ophthalmic artery chemosurgery (intra-arterial chemotherapy) has reduced enucleation rates below 10%, which removes most tumor tissue from molecular workups — motivating plasma cfDNA approaches for somatic mutation detection.

## Cohorts in the corpus

- [rbl_cfdna_msk_2020](../datasets/rbl_cfdna_msk_2020.md) — 10 pediatric patients with advanced intraocular unilateral retinoblastoma at MSKCC; matched tumor (MSK-IMPACT) and plasma cfDNA (custom RB1 hybrid-capture panel, ~1530× coverage); 3/10 patients developed metastatic disease on follow-up [PMID:32633890](../papers/32633890.md).

## Recurrent alterations

- [RB1](../genes/RB1.md) — biallelic loss-of-function is the canonical driver; 13 somatic RB1 variants were identified across 10 tumors by MSK-IMPACT, spanning nonsense (R579*, R320*, R255*, R445*, E315*, R556*, Q736*), frameshift (N623Qfs*15, D338Vfs*11), in-frame deletion (N480del), and splice variants; tumor-guided cfDNA genotyping detected 10/13 of these mutations in plasma (median VAF 4.9%, range 0.7%–12.6%) [PMID:32633890](../papers/32633890.md).
- [MYCN](../genes/MYCN.md) — amplification without RB1 loss drives ~1% of retinoblastomas; not assayed in the [rbl_cfdna_msk_2020](../datasets/rbl_cfdna_msk_2020.md) cohort but flagged as a future extension target via cfDNA copy-number analysis [PMID:32633890](../papers/32633890.md).

## Subtypes

- **Heritable (bilateral/familial)** — germline RB1 pathogenic variant; bilateral presentation more common; requires cascade genetic testing for family members.
- **Non-heritable (unilateral)** — both somatic RB1 hits; somatic cfDNA detection (absent from matched buffy coat) can confirm non-heritable status without biopsy, lifting screening obligations for siblings/offspring.
- **MYCN-amplified, RB1-wildtype** — rare (~1%); distinct molecular subtype not addressable by RB1-targeted cfDNA panels in current form.

## Therapeutic landscape

- **Ophthalmic artery chemosurgery** (intra-arterial [carboplatin](../drugs/carboplatin.md), [melphalan](../drugs/melphalan.md), [topotecan](../drugs/topotecan.md)) is the dominant eye-sparing modality; has reduced enucleation rates to <10% [PMID:32633890](../papers/32633890.md).
- **Systemic chemotherapy** (carboplatin + [etoposide](../drugs/etoposide.md) + [vincristine](../drugs/vincristine.md)) for high-risk or extraocular disease; systemic therapy prior to cfDNA collection suppressed detectable circulating tumor DNA in at least one patient [PMID:32633890](../papers/32633890.md).
- **Somatic RB1 cfDNA testing** before systemic treatment offers a non-invasive route to confirm non-heritable status, with clinical utility in avoiding unnecessary lifelong secondary-cancer surveillance for the patient and genetic counseling for the family [PMID:32633890](../papers/32633890.md).

## Sources

- [PMID:32633890](../papers/32633890.md) — Kothari et al. plasma cfDNA RB1 detection in retinoblastoma.

*This page was processed by **crosslinker** on **2026-05-16**.*
