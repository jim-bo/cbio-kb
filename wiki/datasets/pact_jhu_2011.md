---
name: Pancreatic Cystic Tumors (JHU, 2011)
studyId: pact_jhu_2011
institution: Johns Hopkins University
size: 32
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [MUTATION_EXTENDED]
panels: []
tags: [pancreas, cystic-neoplasm, WES]
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Pancreatic Cystic Tumors (JHU, 2011)

## Overview

This cohort was assembled at Johns Hopkins University and comprises 32 surgically resected neoplastic pancreatic cysts (8 serous cystadenomas, 8 intraductal papillary mucinous neoplasms, 8 mucinous cystic neoplasms, and 8 solid pseudopapillary neoplasms) with matched normal tissue from the same patients. The study was designed to define the genomic landscapes of all four major pancreatic cystic neoplasm subtypes simultaneously by [whole-exome sequencing](../methods/whole-exome-seq.md).

## Composition

- 32 microdissected cyst samples (>33% neoplastic cellularity required) with matched germline DNA.
- Cancer types: [IPMN](../cancer_types/IPMN.md), [MCN](../cancer_types/MCN.md), [SPN](../cancer_types/SPN.md), and serous cystadenoma (SCA; no OncoTree code); progression target [PAAD](../cancer_types/PAAD.md).
- An additional 18 SCA cyst fluids and 28 [IPMN](../cancer_types/IPMN.md) + 3 [MCN](../cancer_types/MCN.md) cyst fluids were screened for selected mutations.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Agilent 50-Mb SureSelect capture on Illumina GAIIx/HiSeq; mean unique coverage ~120-fold (+/- 40) across 64 libraries.
- Customized [VHL](../genes/VHL.md) capture chip for validation of SCA cyst fluids.
- Ligation-based mutation confirmation assays for selected variants.

## Papers using this cohort

- [PMID:22158988](../papers/22158988.md) — Primary WES study defining the somatic mutation landscape of all four cyst types.

## Notable findings derived from this cohort

- A five-gene panel (VHL, [RNF43](../genes/RNF43.md), [CTNNB1](../genes/CTNNB1.md), [GNAS](../genes/GNAS.md), [KRAS](../genes/KRAS.md)) distinguishes all four cyst types in cyst fluid with complete molecular specificity, enabling non-surgical diagnostic classification [PMID:22158988](../papers/22158988.md).
- RNF43 established as a novel tumor suppressor recurrently inactivated in IPMN (6/8) and MCN (3/8); probability of being a passenger < 10^-12 [PMID:22158988](../papers/22158988.md).
- SPNs had only 2.9 +/- 2.1 nonsynonymous mutations per tumor with universal CTNNB1 mutations, the fewest somatic alterations of any tumor type profiled by WES at the time [PMID:22158988](../papers/22158988.md).

## Sources

- [PMID:22158988](../papers/22158988.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
