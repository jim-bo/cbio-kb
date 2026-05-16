---
name: abemaciclib
targets:
  - CDK4
  - CDK6
drug_class: CDK4/6 inhibitor
canonical_source: corpus
unverified: true
tags:
  - targeted_therapy
  - cdk4_6_inhibitor
  - cell_cycle
processed_by: crosslinker
processed_at: 2026-05-16
---

# abemaciclib

## Overview

Abemaciclib (Verzenio) is a selective CDK4/6 inhibitor that blocks [CDK4](../genes/CDK4.md)- and [CDK6](../genes/CDK6.md)-mediated phosphorylation of [RB1](../genes/RB1.md), halting G1-to-S cell cycle progression. It is FDA-approved for HR+/HER2- advanced or metastatic breast cancer in combination with endocrine therapy or as monotherapy. Unlike [palbociclib](../drugs/palbociclib.md) and [ribociclib](../drugs/ribociclib.md), abemaciclib has continuous daily dosing and greater single-agent activity.

## Evidence in the corpus

- In vitro overexpression of candidate resistance drivers ([AKT1](../genes/AKT1.md), [KRAS](../genes/KRAS.md) G12D, [AURKA](../genes/AURKA.md), [CCNE2](../genes/CCNE2.md)) or CRISPR knockout of [RB1](../genes/RB1.md) in T47D and MCF7 HR+/HER2- breast cancer cell lines was sufficient to confer resistance to abemaciclib (and palbociclib), validating each alteration as a functional CDK4/6i resistance mechanism; context-dependence was noted (AURKA overexpression drove resistance in T47D but not MCF7) [PMID:32404308](../papers/32404308.md).

## Resistance mechanisms

- **[RB1](../genes/RB1.md) biallelic loss** — CRISPR knockout in T47D/MCF7 confers abemaciclib resistance; observed in 4/41 (9.8%) resistant biopsies in the Wander et al. HR+/HER2- [MBC](../cancer_types/MBC.md) cohort [PMID:32404308](../papers/32404308.md).
- **[AKT1](../genes/AKT1.md) activation** — lentiviral overexpression (W80R and other activating mutations) confers abemaciclib resistance in T47D [PMID:32404308](../papers/32404308.md).
- **[KRAS](../genes/KRAS.md)/RAS pathway mutations** — KRAS G12D overexpression confers CDK4/6i resistance; KRAS/HRAS/NRAS alterations found in 4/41 (9.8%) resistant biopsies [PMID:32404308](../papers/32404308.md).
- **[AURKA](../genes/AURKA.md) amplification** — overexpression confers abemaciclib resistance in T47D; amplified in 11/41 (26.8%) resistant biopsies, 0/18 sensitive (p=0.0081) [PMID:32404308](../papers/32404308.md).
- **[CCNE2](../genes/CCNE2.md) amplification** — overexpression confers abemaciclib resistance; amplified in 6/41 (14.6%) resistant biopsies; CCNE2-amplified resistant cells are sensitized to the CHK1 inhibitor [prexasertib](../drugs/prexasertib.md) [PMID:32404308](../papers/32404308.md).
- **[ERBB2](../genes/ERBB2.md) alterations** — present in 5/41 (12.2%) resistant biopsies in the Wander et al. cohort [PMID:32404308](../papers/32404308.md).

## Cancer types (linked)

- [BRCA](../cancer_types/BRCA.md) — HR+/HER2- metastatic breast cancer; primary indication for CDK4/6 inhibitor therapy including abemaciclib [PMID:32404308](../papers/32404308.md).

## Sources

- [PMID:32404308](../papers/32404308.md) — Wander et al., whole-exome sequencing of 59 metastatic HR+/HER2- breast cancer biopsies identifying eight categories of CDK4/6 inhibitor resistance mechanisms.

*This page was processed by **crosslinker** on **2026-05-16**.*
