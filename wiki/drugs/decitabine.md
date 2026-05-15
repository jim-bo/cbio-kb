---
name: decitabine
targets:
  - DNMT1
  - DNMT3A
  - DNMT3B
drug_class: hypomethylating agent (DNA methyltransferase inhibitor)
canonical_source: corpus
unverified: true
tags:
  - chemotherapy
  - hypomethylating-agent
  - aml
  - mds
  - epigenetic-therapy
processed_by: crosslinker
processed_at: 2026-05-14
---

# decitabine

## Overview

Decitabine (5-aza-2'-deoxycytidine) is a cytosine nucleoside analog that is incorporated into DNA and irreversibly inhibits DNA methyltransferases (DNMT1, [DNMT3A](../genes/DNMT3A.md), DNMT3B), leading to global DNA hypomethylation and reactivation of silenced tumor suppressor genes. It is approved for [MDS](../cancer_types/MDS.md) and used off-label in [AML](../cancer_types/AML.md), particularly in older or unfit patients and those with [TP53](../genes/TP53.md) mutations. The 10-day dosing schedule (20 mg/m²/day × 10 days per 28-day cycle) is more intensive than the standard 5-day schedule and was developed specifically to maximize epigenetic reprogramming.

## Evidence in the corpus

- In a single-arm prospective trial at Washington University in St. Louis (NCT01687400, N=116 total; discovery cohort n=84, extension cohort n=32), 10-day decitabine (20 mg/m²/day) achieved bone-marrow blast clearance in 53/116 (46%) of [AML](../cancer_types/AML.md) and [MDS](../cancer_types/MDS.md) patients overall: 15 (13%) CR, 24 (21%) CRi, 14 (12%) mCR; cBioPortal study [mnm_washu_2016](../datasets/mnm_washu_2016.md) [PMID:27959731](../papers/27959731.md)
- **[TP53](../genes/TP53.md) mutations are a positive predictor of decitabine response**: 21/21 (100%) [TP53](../genes/TP53.md)-mutant patients achieved blast clearance vs 32/78 (41%) wild-type-TP53 patients (P<0.001); in the discovery cohort alone, 7/7 vs 15/32 (47%), P=0.02 [PMID:27959731](../papers/27959731.md)
- **Unfavorable-risk cytogenetics also predicted response**: 29/43 (67%) with unfavorable karyotypes had blast clearance vs 24/71 (34%) intermediate/favorable-risk (P<0.001); 20/21 TP53-mutant patients had unfavorable karyotype [PMID:27959731](../papers/27959731.md)
- **Survival is not worsened by TP53 or unfavorable cytogenetics on this regimen**: median [OS](../cancer_types/OS.md) 12.7 months (TP53-mutant) vs 15.4 months (wild-type-TP53), P=0.79; compared to only 4–6 months on conventional [cytarabine](../drugs/cytarabine.md)-based induction in TP53-mutant [AML](../cancer_types/AML.md) [PMID:27959731](../papers/27959731.md)
- **Mutation clearance is universal but incomplete**: only [TP53](../genes/TP53.md) and [SF3B1](../genes/SF3B1.md) mutations consistently dropped to VAF <5%; founding-clone VAF at maximum clearance ranged from 0.06% to 18.43% across the 20 best responders; all evaluable relapses arose from preexisting resistant subclones [PMID:27959731](../papers/27959731.md)
- **Pharmacology and methylation are not predictive**: steady-state plasma decitabine on day 4 of cycle 1 did not correlate with response; reduction in CpG methylcytosine from day 0 to day 10 was similar between responders and non-responders (P=0.19 by ANOVA) [PMID:27959731](../papers/27959731.md)
- **Allogeneic SCT had the largest survival effect**: Cox stepwise regression — SCT vs no SCT, P<0.001; benefit not adversely affected by [TP53](../genes/TP53.md) status; decitabine proposed as bridge to transplant in TP53-mutant ultra-high-risk AML/MDS [PMID:27959731](../papers/27959731.md)
- Combined with [panobinostat](../drugs/panobinostat.md) (10 mg three times weekly) in 3 patients in the 5-day decitabine extension cohort at WashU [PMID:27959731](../papers/27959731.md)

## Resistance mechanisms

- All evaluable relapses in the WashU trial arose from preexisting subclones that were already detectable before therapy; primary resistance was observed in 9/39 exome-sequenced patients who had resistant founding or subclonal architecture pre-treatment [PMID:27959731](../papers/27959731.md)
- Mutation clearance was never complete in any tested patient; remissions are short-lived (typically <1 year); decitabine alone is not curative [PMID:27959731](../papers/27959731.md)

## Cancer types (linked)

- [AML](../cancer_types/AML.md) — primary indication; TP53-mutant AML has 100% response rate to 10-day decitabine; survival comparable to TP53-wild-type despite higher response.
- [MDS](../cancer_types/MDS.md) — transfusion-dependent [MDS](../cancer_types/MDS.md) included in WashU trial; TP53 mutation trended toward decreased survival in MDS subset (P=0.08, underpowered).

## Sources

- [PMID:27959731](../papers/27959731.md) — Welch et al. 2016, *NEJM*. WashU single-arm prospective trial of 10-day decitabine in AML/MDS (N=116); TP53 mutation as positive predictor of response; incomplete mutation clearance; SCT as dominant survival predictor.

*This page was processed by **crosslinker** on **2026-05-14**.*
