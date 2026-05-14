---
name: Case Comprehensive Cancer Center CRC — African American Cohort (2015)
studyId: coad_caseccc_2015
institution: Case Medical Center / Case Comprehensive Cancer Center, northeastern Ohio
size: 103 AA CRC cases (29 discovery WES + 74 validation targeted) + 129 Caucasian CRC comparators
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-dna-seq
  - sanger-sequencing
panels: []
tags:
  - colorectal-cancer
  - african-american
  - health-disparities
  - microsatellite-stable
  - driver-genes
  - ethnicity-associated-mutations
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# Case Comprehensive Cancer Center CRC — African American Cohort (2015)

## Overview

A single-institution cohort from Case Medical Center (northeastern Ohio) designed to characterize the somatic mutational landscape of microsatellite-stable (MSS) colorectal cancers in African American (AA) patients — the largest such cohort at the time of publication. All tumors were fresh-frozen, pathologist-confirmed ≥50% tumor cellularity, and MSS by five-marker panel (BAT26/BAT40/D2S123/D5S346/D17S250). The study was published in 2015 by Guda et al. in *PNAS*.

## Composition

- **Discovery set:** 29 informative MSS late-stage AA CRC tumor/normal pairs sequenced by whole-exome sequencing; one hypermutator excluded from the original 30 cases.
- **Validation set:** 74 informative MSS AA CRC cases (predominantly early-stage) sequenced with a custom Agilent SureSelectXT bait library against 78 candidate genes; three hypermutators excluded from the original 77.
- **Comparator:** 129 predominantly late-stage MSS Caucasian CRCs from the same institution, resequenced for the 20 significantly mutated AA genes.
- Cancer type: [COAD](../cancer_types/COAD.md).
- Samples drawn exclusively from fresh-frozen archive in northeastern Ohio.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 29 discovery AA CRC paired tumor/normal exomes.
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — custom Agilent SureSelectXT bait library (78 candidate genes) for 74 AA CRC validation cases; used for 129 Caucasian comparators (20-gene panel).
- [sanger-sequencing](../methods/sanger-sequencing.md) — orthogonal confirmation of candidate somatic variants.

## Papers using this cohort

- [PMID:25583493](../papers/25583493.md) — Guda et al. (2015). Whole-exome and targeted sequencing of 103 AA and 129 Caucasian MSS CRCs; nominated 20 significantly mutated genes with a 15-gene subset preferentially targeted in AA patients.

## Notable findings derived from this cohort

- A 15-gene subset of the 20 newly identified significantly mutated genes is preferentially targeted in AA CRCs (~twofold more mutations per tumor than Caucasian CRCs; P = 1.8 × 10⁻⁸), accounting for 41% of AA cases vs 15% of Caucasian cases. [PMID:25583493](../papers/25583493.md)
- [EPHA6](../genes/EPHA6.md) mutations identified in 5.83% of AA CRCs (6/103) vs 0% of Caucasian CRCs (P = 0.007), proposed as an AA-specific CRC driver. [PMID:25583493](../papers/25583493.md)
- [FLCN](../genes/FLCN.md) mutations (two frameshifts, one nonsense) exclusive to AA cases (3/103 vs 0/129; P = 0.086), consistent with loss-of-function and proposed as an AA-specific driver. [PMID:25583493](../papers/25583493.md)
- Classic CRC drivers ([APC](../genes/APC.md), [TP53](../genes/TP53.md), [KRAS](../genes/KRAS.md), [PIK3CA](../genes/PIK3CA.md), [SMAD4](../genes/SMAD4.md), [BRAF](../genes/BRAF.md), [FBXW7](../genes/FBXW7.md)) did not differ overall between AA and Caucasian CRCs; however, [KRAS](../genes/KRAS.md) and [FBXW7](../genes/FBXW7.md) individually showed significantly higher mutation rates in AA cases. [PMID:25583493](../papers/25583493.md)

## Sources

- [PMID:25583493](../papers/25583493.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
