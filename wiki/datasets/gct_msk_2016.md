---
name: Germ Cell Tumors (MSK, J Clin Oncol 2016)
studyId: gct_msk_2016
institution: Memorial Sloan Kettering Cancer Center
size: 180
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-dna-seq
panels:
  - IMPACT410
tags:
  - germ-cell-tumor
  - cisplatin-resistance
  - testicular-cancer
  - mediastinal-primary
  - TP53-pathway
  - MDM2-amplification
  - RAC1
  - actionable-alterations
processed_by: crosslinker
processed_at: 2026-05-14
---

# Germ Cell Tumors (MSK, J Clin Oncol 2016)

## Overview

Bagrodia et al. performed whole-exome sequencing on a discovery cohort of 19 advanced germ cell tumors (GCTs) and validated findings with MSK-IMPACT targeted sequencing on 161 additional prospective patients at Memorial Sloan Kettering Cancer Center (combined N=180). The cohort was heavily enriched for the cisplatin-resistant phenotype to identify genomic determinants of resistance. All mutational and clinical data are publicly available on cBioPortal.

## Composition

- **N = 180 men** with advanced germ cell tumor receiving first-line cisplatin-based chemotherapy at MSK.
- **Discovery cohort:** 19 tumors profiled by whole-exome sequencing (10 cisplatin-resistant, 9 cisplatin-sensitive); mean coverage 116× (range 93–134×).
- **Validation cohort:** 161 prospective patients profiled by MSK-IMPACT ([IMPACT410](../methods/IMPACT410.md)) targeted exon-capture (>300 cancer-related genes; 500–1,000× depth).
- **Histology:** 70% [NSGCT](../cancer_types/NSGCT.md) (n=126), 30% [SEM](../cancer_types/SEM.md) (n=54).
- **Primary site:** 87.2% testis ([TT](../cancer_types/TT.md)), 12.2% mediastinum, 0.6% retroperitoneum.
- **Cisplatin sensitivity:** 76 sensitive vs 104 resistant.
- **IGCCCG risk:** good 51.1%, intermediate 15.6%, poor 32.8%.
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — discovery cohort (19 tumors); mean coverage 116×.
- [IMPACT410](../methods/IMPACT410.md) — MSK-IMPACT targeted NGS of >300 cancer-related genes; 500–1,000× depth; validation cohort (161 patients).

## Papers using this cohort

- [PMID:27646943](../papers/27646943.md) — Bagrodia et al., "Genetic Determinants of Cisplatin Resistance in Patients With Advanced Germ Cell Tumors," *Journal of Clinical Oncology* 2016. (Defining study for this cohort.)

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) alterations found **exclusively** in cisplatin-resistant tumors (17/104 [16.3%] vs 0/76 sensitive; P<.001); combined [TP53](../genes/TP53.md)/[MDM2](../genes/MDM2.md) pathway alterations present in 24.0% vs 2.6% (P<.001) of resistant vs sensitive tumors. [PMID:27646943](../papers/27646943.md)
- [TP53](../genes/TP53.md)/[MDM2](../genes/MDM2.md) alteration independently predicted shorter progression-free survival (HR 1.83; 95% CI 1.12–2.98; P=.016) after adjusting for IGCCCG risk model. [PMID:27646943](../papers/27646943.md)
- 72% of primary mediastinal nonseminomas harbored [TP53](../genes/TP53.md) alterations (13/18), providing the first genetic basis for the dismal prognosis of this subgroup. [PMID:27646943](../papers/27646943.md)
- Novel [RAC1](../genes/RAC1.md) hotspot mutations (G12V, G12R, P34R, Q61R, Q61K) identified in 9 patients (5% incidence — highest reported across cancer types in TCGA at publication); functionally validated to activate [PAK1](../genes/PAK1.md) and MEK1/2 phosphorylation. [PMID:27646943](../papers/27646943.md)
- Actionable alterations detected in 55% of cisplatin-resistant GCTs, including [KIT](../genes/KIT.md) mutations (enriched in [SEM](../cancer_types/SEM.md), 29.6%), [KRAS](../genes/KRAS.md) mutations (15%), PI3K pathway alterations (13.3%), and [MDM2](../genes/MDM2.md) amplifications (7.6%). [PMID:27646943](../papers/27646943.md)
- Mean MSK-IMPACT mutation rate of 0.9/Mb confirms that GCTs are among the least mutationally burdened adult solid tumors; 12p gain present in 74% of discovery tumors, consistent with the well-characterized [GCT](../cancer_types/GCT.md) cytogenetic signature. [PMID:27646943](../papers/27646943.md)

## Sources

- cBioPortal study ID: `gct_msk_2016`
- DOI: 10.1200/JCO.2016.68.7798
- Reference genome: hg19

*This page was processed by **crosslinker** on **2026-05-14**.*
