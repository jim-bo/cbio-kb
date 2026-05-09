---
name: "Cambridge CIMR Myeloproliferative Neoplasms WES 2013"
studyId: mpn_cimr_2013
institution: "Cambridge Institute for Medical Research (CIMR) / Wellcome Sanger Institute"
size: 151
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - sanger-sequencing
panels: []
tags:
  - myeloproliferative-neoplasms
  - calr
  - jak2-negative
  - driver-mutation
  - clonal-hematopoiesis
  - exome-sequencing
processed_by: crosslinker
processed_at: 2026-05-09
---

# Cambridge CIMR Myeloproliferative Neoplasms WES 2013

## Overview

The mpn_cimr_2013 cohort was assembled by Nangalia, Massie, Green and colleagues at the Cambridge Institute for Medical Research (CIMR) and the Wellcome Sanger Institute to characterize the mutational landscape of myeloproliferative neoplasms (MPNs) and discover drivers in the JAK2/MPL-negative subset. The study led to the landmark discovery of somatic calreticulin ([CALR](../genes/CALR.md)) exon-9 indels as a novel, recurrent [MPN](../cancer_types/MPN.md) driver mutation — the first report of CALR as a cancer gene — present in 70–84% of JAK2/MPL-negative essential thrombocythemia and myelofibrosis patients.

## Composition

- **Discovery cohort:** 151 MPN patients passing bioinformatic QC (out of 168 sequenced):
  - 48 polycythemia vera ([PV](../cancer_types/PV.md))
  - 62 essential thrombocythemia ([ET](../cancer_types/ET.md))
  - 39 myelofibrosis ([MF](../cancer_types/MF.md))
  - 2 unclassifiable [MPN](../cancer_types/MPN.md)
- **Follow-up screening:** 1,345 additional hematologic cancers + 52 controls (Sanger sequencing); plus WES/WGS data for 502 solid tumors, 498 controls, 1,015 cancer cell lines
- **Tumor DNA source:** blood granulocytes; constitutional DNA from cultured T cells (n=34), isolated T cells (n=42), or buccal swabs (n=75)
- Average exome coverage: 141×
- Reference genome: hg19

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): matched tumor/germline pairs; average coverage 141×; orthogonal target-capture resequencing for validation
- [Sanger sequencing](../methods/sanger-sequencing.md): CALR exon 9 follow-up screening in 1,345 hematologic cancers; also used for genotyping ~300 individual hematopoietic colonies across 5 patients for clonal phylogeny analysis

## Papers using this cohort

- [PMID:24325359](../papers/24325359.md) — Nangalia et al., NEJM 2013: discovery of somatic CALR mutations as the dominant driver in JAK2/MPL-negative MPNs

## Notable findings derived from this cohort

- 1,498 validated somatic mutations across 150 samples (range 1–32); median mutations per patient: 6.5 ([PV](../cancer_types/PV.md) and [ET](../cancer_types/ET.md)), 13.0 ([MF](../cancer_types/MF.md); ANOVA P=0.008) [PMID:24325359](../papers/24325359.md)
- [JAK2](../genes/JAK2.md) V617F detected in 48/48 (100%) PV, 35/62 (56%) ET, and 27/39 (69%) MF [PMID:24325359](../papers/24325359.md)
- [CALR](../genes/CALR.md) exon-9 indels discovered in 26/151 (17%) of the exome cohort — exclusively in JAK2/MPL-negative patients (26/31, 84%); 148 CALR mutations identified across the full cohort representing 19 distinct variants, all producing a +1 bp frameshift; two dominant variants: L367fs*46 (45%) and K385fs*47 (41%) [PMID:24325359](../papers/24325359.md)
- Mutual exclusivity of [JAK2](../genes/JAK2.md), [MPL](../genes/MPL.md), and CALR mutations in 97% of patients (q<0.01) [PMID:24325359](../papers/24325359.md)
- CALR mutations present in 70% of JAK2/MPL-negative MPN at follow-up; 8% of [MDS](../cancer_types/MDS.md); absent in all 502 solid tumors, 1,015 cell lines, and 550 controls [PMID:24325359](../papers/24325359.md)
- CALR-mutant ET associated with higher platelet counts, lower hemoglobin, and higher ET-to-MF transformation rate vs JAK2-mutant ET [PMID:24325359](../papers/24325359.md)
- Clonal phylogeny in hematopoietic colonies placed CALR mutation at the earliest phylogenetic node in all 5 patients analyzed — consistent with an initiating driver event [PMID:24325359](../papers/24325359.md)

## Sources

- [PMID:24325359](../papers/24325359.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
