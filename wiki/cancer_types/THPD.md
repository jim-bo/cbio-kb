---
name: Poorly Differentiated Thyroid Cancer
oncotree_code: THPD
main_type: Thyroid Cancer
parent: THYROID
tags:
  - thyroid
  - poorly-differentiated
  - advanced-thyroid
processed_by: crosslinker
processed_at: 2026-05-14
---

# Poorly Differentiated Thyroid Cancer (THPD)

## Overview

Poorly differentiated thyroid carcinoma (PDTC) is an intermediate-grade follicular-cell-derived thyroid malignancy that sits between well-differentiated (papillary, follicular) and anaplastic thyroid cancers in the OncoTree hierarchy (parent: THYROID). It is defined histologically by two competing diagnostic criteria: the Turin proposal (solid/nested/insular growth + absent papillary nuclear features + mitoses ≥3/10 HPF or necrosis) and the MSKCC criteria (≥5 mitoses/10 HPF and/or necrosis with follicular differentiation, irrespective of growth pattern). These criteria select biologically distinct sub-populations — Turin enriches for RAS-driven tumors with distant-metastasis tropism, while MSKCC enriches for BRAF-driven tumors with locoregional-nodal tropism.

## Cohorts in the corpus

- [thyroid_mskcc_2016](../datasets/thyroid_mskcc_2016.md): 84 PDTC tumors (plus 33 ATC) profiled by MSK-IMPACT 341-gene panel; 80 FFPE + 37 frozen; paired normal available for 78 PDTC [PMID:26878173](../papers/26878173.md)

## Recurrent alterations

- [BRAF](../genes/BRAF.md) V600E in 33% of PDTC; BRAF-mutant PDTCs are smaller, more often nodal-metastatic, and classified predominantly by MSKCC criteria [PMID:26878173](../papers/26878173.md)
- [NRAS](../genes/NRAS.md)/[HRAS](../genes/HRAS.md)/[KRAS](../genes/KRAS.md) collectively in 28% of PDTC; mutually exclusive with [BRAF](../genes/BRAF.md) and gene fusions; RAS-mutant PDTCs meet Turin criteria and tend toward distant metastasis [PMID:26878173](../papers/26878173.md)
- [TERT](../genes/TERT.md) promoter mutations (C228T or C250T) in 40% of PDTC, stepwise enriched from 9% in PTC; clonal in PDTC vs subclonal in PTC; co-occurs with BRAF/RAS (OR 3.4, P=0.004); TERT-mutant PDTCs develop more distant metastases (56% vs 20%, P=0.01) [PMID:26878173](../papers/26878173.md)
- [EIF1AX](../genes/EIF1AX.md) mutated in 11% of PDTC via N-terminal hotspot or thyroid-specific p.A113splice site; near-perfect co-occurrence with RAS (OR 58.3, P<0.001); associated with shorter survival (logrank P=0.048) [PMID:26878173](../papers/26878173.md)
- [TP53](../genes/TP53.md) mutated in only 8% of PDTC (vs 73% in ATC; P<1×10⁻⁴) — a key feature distinguishing PDTC from anaplastic thyroid cancer [PMID:26878173](../papers/26878173.md)
- PI3K/AKT/mTOR pathway ([PIK3CA](../genes/PIK3CA.md), [PTEN](../genes/PTEN.md), [MTOR](../genes/MTOR.md), etc.) disrupted in 11% of PDTC [PMID:26878173](../papers/26878173.md)
- SWI/SNF complex alterations in 6% of PDTC; histone-methyltransferase mutations in 7% [PMID:26878173](../papers/26878173.md)
- Gene fusions in 14% of PDTC (RET/PTC, [PAX8](../genes/PAX8.md)-[PPARG](../genes/PPARG.md), [ALK](../genes/ALK.md) rearrangements); absent in ATC; mutually exclusive with BRAF/RAS [PMID:26878173](../papers/26878173.md)
- Median mutation burden 2 mutations (across 341 genes) vs 6 in ATC and 1 in PTC; higher burden correlates with older age, larger tumor, distant metastasis, and worse survival [PMID:26878173](../papers/26878173.md)

## Subtypes

- **Turin-PDTC**: predominantly RAS-mutant, distant-metastasis tropism, larger tumors [PMID:26878173](../papers/26878173.md)
- **MSKCC-PDTC**: predominantly BRAF-mutant, locoregional-nodal tropism, smaller tumors, female-enriched (P=0.005) [PMID:26878173](../papers/26878173.md)
- **[TERT](../genes/TERT.md)+BRAF/RAS double-mutant**: extreme-risk sub-group with high rate of distant metastasis and shorter survival [PMID:26878173](../papers/26878173.md)

## Therapeutic landscape

- BRAF-V600E prevalence (33%) supports consideration of BRAF-inhibitor strategies [PMID:26878173](../papers/26878173.md)
- PI3K/AKT/mTOR pathway alterations (11%) suggest potential for pathway inhibitors [PMID:26878173](../papers/26878173.md)
- No drugs were administered or tracked in the MSKCC sequencing study; all therapeutic implications are inferred [PMID:26878173](../papers/26878173.md)

## Sources

- [PMID:26878173](../papers/26878173.md) — Landa et al., MSKCC MSK-IMPACT sequencing of 84 PDTC and 33 ATC

*This page was processed by **crosslinker** on **2026-05-14**.*
