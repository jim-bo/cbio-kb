---
name: "Broad/DeCOG BRAF-Inhibitor Resistance in Metastatic Melanoma WES 2012"
studyId: skcm_broad_brafresist_2012
institution: "Broad Institute / Dermatologic Cooperative Oncology Group of Germany (DeCOG)"
size: 45
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - melanoma
  - BRAFV600
  - RAF-inhibitor
  - resistance
  - MAPK-pathway
  - PI3K-pathway
processed_by: crosslinker
processed_at: 2026-05-09
---

# Broad/DeCOG BRAF-Inhibitor Resistance in Metastatic Melanoma WES 2012

## Overview

The skcm_broad_brafresist_2012 cohort was assembled by Van Allen, Wagle, Schadendorf and colleagues through a collaboration between the Broad Institute and the Dermatologic Cooperative Oncology Group of Germany (DeCOG). The dataset comprises whole-exome sequencing of FFPE tumors from [BRAF](../genes/BRAF.md) V600 metastatic cutaneous melanoma patients treated with single-agent RAF inhibitors ([vemurafenib](../drugs/vemurafenib.md) or [dabrafenib](../drugs/dabrafenib.md)), with matched pre-treatment and post-resistance biopsies available for the majority of patients. It was a landmark study characterizing the genetic landscape of clinical RAF-inhibitor resistance, revealing a "long tail" of MAPK-pathway alterations beyond the canonical resistance mechanisms.

## Composition

- **Total samples:** 45 patients (BRAF V600 metastatic [SKCM](../cancer_types/SKCM.md))
- **Early resistance:** 14/45 (31%) — progression in <12 weeks
- **Acquired resistance:** 31/45 (69%)
- **Matched pre-/post-resistance pairs:** 32/45 patients; remainder contributed either pre-treatment or resistance biopsy only
- **Treatment:** single-agent [vemurafenib](../drugs/vemurafenib.md) or [dabrafenib](../drugs/dabrafenib.md)
- Reference genome: hg19

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Illumina HiSeq on FFPE-derived DNA; mean coverage 200× (tumor), 92× (germline)
- Somatic SNV calling: [MuTect](../methods/mutect.md); indels: [Indelocator](../methods/indelocator.md); annotation: [Oncotator](../methods/oncotator.md); Broad Picard/Firehose pipeline

## Papers using this cohort

- [PMID:24265153](../papers/24265153.md) — Van Allen et al., Cancer Discovery 2014: genetic landscape of clinical resistance to RAF inhibition

## Notable findings derived from this cohort

- Genetic alterations in known or putative RAF-inhibitor resistance genes observed in 23/45 (51%) patients [PMID:24265153](../papers/24265153.md)
- MAPK-pathway resistance mechanisms ([NRAS](../genes/NRAS.md), [BRAF](../genes/BRAF.md) amplification, [MAP2K1](../genes/MAP2K1.md), [MAP2K2](../genes/MAP2K2.md), [MITF](../genes/MITF.md), [NF1](../genes/NF1.md)) accounted for 44.4% (20/45) of the cohort [PMID:24265153](../papers/24265153.md)
- [MAP2K2](../genes/MAP2K2.md) (MEK2) mutations and [MITF](../genes/MITF.md) amplification identified as novel resistance mechanisms with experimental validation [PMID:24265153](../papers/24265153.md)
- Three tumors carried multiple co-occurring resistance mechanisms within the same biopsy [PMID:24265153](../papers/24265153.md)
- [BRAF](../genes/BRAF.md) V600 mutations confirmed in 100% of pre-treatment biopsies; 44/45 at codon V600 plus one in-frame deletion (Val600_Lys601delinsGlu) predicted to phenocopy V600E [PMID:24265153](../papers/24265153.md)

## Sources

- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
