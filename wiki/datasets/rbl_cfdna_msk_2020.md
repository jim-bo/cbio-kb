---
name: MSK Retinoblastoma cfDNA RB1 Capture Cohort
studyId: rbl_cfdna_msk_2020
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 10
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - rb1-cfdna-custom-capture-panel
panels:
  - msk-impact-panel
tags:
  - retinoblastoma
  - cfDNA
  - liquid-biopsy
  - pediatric
  - RB1
  - noninvasive-profiling
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Retinoblastoma cfDNA RB1 Capture Cohort

## Overview

The rbl_cfdna_msk_2020 cohort establishes proof-of-concept for plasma cell-free DNA (cfDNA) profiling of somatic [RB1](../genes/RB1.md) mutations in pediatric retinoblastoma — a cancer type where intraocular biopsy is contraindicated (tumor-seeding risk) and declining enucleation rates have removed tumor tissue from most molecular workups. Ten patients with advanced intraocular unilateral retinoblastoma undergoing primary enucleation at MSKCC were profiled with [MSK-IMPACT](../methods/msk-impact-panel.md) on tumor and a custom hybrid-capture panel tiling all 27 [RB1](../genes/RB1.md) exons on matched plasma. Tumor-guided cfDNA genotyping recovered 10/13 somatic RB1 mutations in 8/10 patients, with the highest cfDNA VAFs observed in the two patients who subsequently developed metastatic disease. [PMID:32633890](../papers/32633890.md)

## Composition

- **10 pediatric patients** with advanced intraocular *unilateral* [retinoblastoma](../cancer_types/RBL.md); all undergoing primary enucleation at MSKCC.
- Median age at diagnosis: 30.8 months (range 0.67–50.2 months).
- 9/10 treatment-naive at plasma collection; 1 patient (P19) had received 1 cycle of systemic carboplatin/etoposide/vincristine prior to presentation.
- 3/10 developed metastatic disease on follow-up; this elevated rate reflects selection for advanced disease in the enucleation cohort. [PMID:32633890](../papers/32633890.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — FDA-cleared targeted panel (>400 genes including all RB1 coding exons) applied to enucleated tumor. [PMID:32633890](../papers/32633890.md)
- [rb1-cfdna-custom-capture-panel](../methods/rb1-cfdna-custom-capture-panel.md) — custom hybrid-capture panel tiling all 27 exons of RB1 plus heterozygous-SNP regions; Illumina HiSeq 2×100 bp paired-end; average unique coverage ~1530×; cfDNA input 5.5–27.4 ng (mean 17.3 ng). [PMID:32633890](../papers/32633890.md)
- Variant callers: tumor-guided genotyping via [Waltz 2.0](../methods/waltz.md); tumor-blind de novo calling via [VarDict](../methods/vardict.md) with IGV v2.3.36 manual review. [PMID:32633890](../papers/32633890.md)

## Papers using this cohort

- [PMID:32633890](../papers/32633890.md) — Kothari et al. (2020), *Cancer Medicine*: Cell-free DNA profiling in retinoblastoma patients with advanced intraocular disease.

## Notable findings derived from this cohort

- Tumor-guided cfDNA genotyping detected **10/13** expected somatic [RB1](../genes/RB1.md) mutations in **8/10** patients; median cfDNA VAF 4.9% (range 0.7%–12.6%); technical replicates showed Pearson r²=0.993. [PMID:32633890](../papers/32633890.md)
- Tumor-blind de novo calling (VarDict + custom filters) recovered **7/13** expected RB1 mutations in **6/10** patients without prior tumor sequencing. [PMID:32633890](../papers/32633890.md)
- Highest cfDNA VAFs (12.6% and 8.1%) were observed in the two patients who developed metastatic disease, suggesting cfDNA VAF may track disease burden. [PMID:32633890](../papers/32633890.md)
- Systemic chemotherapy suppressed circulating tumor cfDNA: the one pre-treated patient (P19) showed no cfDNA signal despite 1596× coverage; diagnostic cfDNA collection must precede systemic therapy. [PMID:32633890](../papers/32633890.md)
- Demonstrating a somatic RB1 cfDNA mutation absent from matched buffy coat is sufficient to confirm non-heritable disease, enabling elimination of serial eye exams and secondary-cancer screening for siblings/offspring. [PMID:32633890](../papers/32633890.md)

## Sources

- cBioPortal study: `rbl_cfdna_msk_2020`
- DOI: [10.1002/cam4.3144](https://doi.org/10.1002/cam4.3144)

*This page was processed by **crosslinker** on **2026-05-16**.*
