---
name: Chronic Lymphocytic Leukemia (Broad, Nature 2015)
studyId: cll_broad_2015
institution: Broad Institute / Dana-Farber Cancer Institute / University of Ulm (CLL8 trial consortium)
size: 538
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels: []
tags:
  - cll
  - chronic-lymphocytic-leukemia
  - whole-exome-seq
  - clinical-trial
  - clonal-evolution
  - chemoimmunotherapy
processed_by: crosslinker
processed_at: 2026-05-14
---

# Chronic Lymphocytic Leukemia (Broad, Nature 2015)

## Overview

The cll_broad_2015 dataset comprises whole-exome sequencing of 538 chronic lymphocytic leukemia (CLL) samples with matched germline DNA, published by Landau et al. in Nature (2015). The cohort combines the phase III CLL8 trial prospective sub-cohort (n=278 pre-treatment samples, median >6 years follow-up, randomized between FC and FCR), two prior non-overlapping CLL WES cohorts (n=260), and matched relapse exomes from 59 CLL8 subjects. Mean exome read depth was 95.0× (tumor) / 95.7× (normal). CLL8 WES data are deposited in dbGaP (phs000922.v1.p1).

## Composition

- 538 [CLLSLL](../cancer_types/CLLSLL.md) whole-exomes with matched germline DNA.
- Prospective sub-cohort: 278 pre-treatment samples from the CLL8 phase III trial (FC vs FCR randomization).
- Longitudinal sub-cohort: 59 matched pre-treatment/relapse pairs from CLL8 subjects.
- Matched RNA-seq in 156 cases for orthogonal validation.
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [mutsig](../methods/mutsig.md) (MutSig2CV for driver discovery)
- [absolute](../methods/absolute.md) (clonality and CCF estimation)

## Papers using this cohort

- [PMID:26466571](../papers/26466571.md) — Landau et al. 2015, Nature — "Mutations driving CLL and their evolution in progression and relapse."

## Notable findings derived from this cohort

- 44 recurrently mutated CLL driver genes identified (18 previously reported + 26 novel, including [RPS15](../genes/RPS15.md) and [IKZF3](../genes/IKZF3.md)); 91.1% of CLLs carry at least one driver event [PMID:26466571](../papers/26466571.md).
- In the CLL8 prospective sub-cohort, mutated [TP53](../genes/TP53.md), [SF3B1](../genes/SF3B1.md), and the novel driver [RPS15](../genes/RPS15.md) each independently predicted shorter progression-free survival (PFS); any pre-treatment subclonal driver predicted shorter PFS (HR 1.6, 95% CI 1.2–2.2, P=0.004) [PMID:26466571](../papers/26466571.md).
- Non-canonical [BRAF](../genes/BRAF.md) mutations in CLL cluster in the kinase activation segment rather than at V600E, implying distinct mechanism and reduced sensitivity to V600E-selective inhibitors [PMID:26466571](../papers/26466571.md).
- Large clonal shifts observed in 57/59 (97%) paired pre-treatment/relapse exomes; eventual relapse clone detectable pre-treatment in 30% of cases by WES, rising further with targeted deep sequencing [PMID:26466571](../papers/26466571.md).
- sCNVs are the earliest driver events; del(13q) and tri(12) are mutually exclusive entry points converging on del(11q); copy loss precedes sSNV/sINDEL hits in biallelic [ATM](../genes/ATM.md) and [BIRC3](../genes/BIRC3.md) inactivation [PMID:26466571](../papers/26466571.md).

## Sources

- Landau DA et al. "Mutations driving CLL and their evolution in progression and relapse." Nature. 2015;526(7574):525-530. [PMID:26466571](../papers/26466571.md). DOI: 10.1038/nature15395.

*This page was processed by **crosslinker** on **2026-05-14**.*
