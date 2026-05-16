---
name: Germ Cell Tumors and Associated Hematologic Malignancies (MSK, JCI 2020)
studyId: gct_msk_2020
institution: Memorial Sloan Kettering Cancer Center
size: 15
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-exome-seq
panels:
  - msk-impact-panel
tags:
  - gct
  - hematologic-malignancy
  - mediastinal
  - clonal-evolution
processed_by: crosslinker
processed_at: 2026-05-16
---

# Germ Cell Tumors and Associated Hematologic Malignancies (MSK, JCI 2020)

## Overview

This cohort comprises 15 male patients (ages 18–33, median 25) with concurrent primary mediastinal (PM) nonseminomatous germ cell tumors ([NSGCT](../cancer_types/NSGCT.md)) and hematologic malignancies, identified at MSKCC over a 21-year period (1998–2019). MSK-IMPACT sequencing was performed on 11 patients with available tissue; whole-exome sequencing (WES) on a 5-patient subset using fingernail DNA as matched normal controls. IMPACT mutation calls are deposited on cBioPortal as this study. The dataset underpins the discovery that mediastinal GCTs and their associated hematologic malignancies derive from a common somatic ancestral precursor — not from therapy-induced clonal expansion.

## Composition

- 15 patients with PM NSGCT + concurrent hematologic malignancy; all male, ages 18–33 (median 25).
- [GCT](../cancer_types/GCT.md) histology: teratoma component 73% (predominant 60%); yolk sac tumor 53%.
- Hematologic malignancies: [AML](../cancer_types/AML.md) 53% (nearly half M7/AMKL), [MDS](../cancer_types/MDS.md), [CMML](../cancer_types/CMML.md), histiocytic sarcoma; one-third developed multiple temporally distinct subtypes.
- 2/15 patients had clinically diagnosed Klinefelter syndrome.
- Sequencing: MSK-IMPACT on 11 patients; WES on 5-patient subset.
- Allele-specific copy number and clonality by FACETS v0.5.6; oncogenic-alteration annotation via OncoKB.
- WES data deposited at dbGaP `phs2231.V1`.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341–468 gene panel)
- [Whole-exome sequencing](../methods/whole-exome-seq.md) (fingernail DNA as matched normal)
- [FACETS](../methods/facets.md) v0.5.6 for allele-specific copy number
- [OncoKB](../methods/oncokb-annotation.md) for oncogenic-alteration annotation
- [Phylogenetic tree reconstruction](../methods/phylogenetic-tree-reconstruction.md)

## Papers using this cohort

- [PMID:32897884](../papers/32897884.md) — Taylor et al. 2020, JCI: "Germ cell tumors and associated hematologic malignancies evolve from a common shared precursor"

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) mutations were shared between the GCT and the blood cancer in 91% (10/11) of paired patients, versus 61% in mediastinal GCTs without hematologic malignancy and only 9% in de novo AML; isochromosome 12p was present in both malignancy types but absent from de novo AML — [PMID:32897884](../papers/32897884.md)
- Shared ancestral precursor confirmed by WES in all 5 patients; branching clonal evolution produced each malignancy independently via distinct secondary events — [PMID:32897884](../papers/32897884.md)
- Absence of canonical myeloid drivers ([FLT3](../genes/FLT3.md), [DNMT3A](../genes/DNMT3A.md), [TET2](../genes/TET2.md), [NPM1](../genes/NPM1.md)) in all hematologic malignancies distinguishes these from de novo myeloid neoplasms — [PMID:32897884](../papers/32897884.md)
- Median overall survival was 6.3 months (95% CI 4.6–25.2 months); only 1 patient alive at analysis — [PMID:32897884](../papers/32897884.md)
- Autologous stem cell transplant products from 5 high-risk PM GCT patients showed no clonal hematopoiesis by sequencing, even for one patient who later developed a clonally related MDS — [PMID:32897884](../papers/32897884.md)

## Sources

- [PMID:32897884](../papers/32897884.md)
- cBioPortal study: `gct_msk_2020`
- dbGaP: `phs2231.V1`

*This page was processed by **crosslinker** on **2026-05-16**.*
