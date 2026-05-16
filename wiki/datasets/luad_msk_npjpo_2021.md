---
name: MSK Lung Adenocarcinoma (NPJ Precis Oncol 2021)
studyId: luad_msk_npjpo_2021
institution: Memorial Sloan Kettering Cancer Center
size: 426
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - MSK-IMPACT341
  - MSK-IMPACT410
  - MSK-IMPACT468
tags:
  - lung
  - LUAD
  - lymph-node
  - staging
  - MSK-IMPACT
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Lung Adenocarcinoma (NPJ Precis Oncol 2021)

## Overview

Single-institution retrospective cohort of 426 treatment-naive patients with clinical N2-negative (cN0 or cN1) stage I/II lung adenocarcinoma ([LUAD](../cancer_types/LUAD.md)) who underwent complete anatomic resection with lymph node (LN) dissection at Memorial Sloan Kettering Cancer Center between 2010 and 2018. Tumors were profiled with [MSK-IMPACT](../methods/msk-impact-panel.md) to characterize genomic features associated with occult pathologic LN metastasis. The study was published in NPJ Precision Oncology 2021 and is available on cBioPortal as `luad_msk_npjpo_2021`. [PMID:34290393](../papers/34290393.md)

## Composition

- 426 [LUAD](../cancer_types/LUAD.md) patients; 60% male, 74% ever-smokers.
- Clinical stage: 78% stage I (n=334), 22% stage II (n=92); 85% cN0, 15% cN1.
- Pathologic outcomes: pN0 80% (n=341), pN1 11% (n=48), pN2 9% (n=37); pN1 and pN2 grouped as pN-positive for analyses.
- Sequencing performed across MSK-IMPACT 341-, 410-, and 468-gene panels (0.98, 1.06, 1.22 Mb coding regions). Copy number and WGD called from FACETS; focal CNAs from GISTIC 2.0; mutational signatures computed against COSMIC SBS for samples with ≥13.8 Mut/Mb. [PMID:34290393](../papers/34290393.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341-, 410-, and 468-gene panels) — tumor/matched-normal NGS; mutations, small indels, copy-number alterations, MSI, TMB.
- [FACETS](../methods/facets.md) — allele-specific copy number and WGD estimation.
- [GISTIC 2.0](../methods/gistic.md) — focal copy number alteration calling.

## Papers using this cohort

- [PMID:34290393](../papers/34290393.md) — Multivariable logistic regression combining preoperative clinical features and tumor genomic alterations ([SMARCA4](../genes/SMARCA4.md), [SMAD4](../genes/SMAD4.md)) to predict pathologic LN metastasis in clinical N2-negative stage I/II LUAD. [PMID:34290393](../papers/34290393.md)

## Notable findings derived from this cohort

- False-negative rate for preoperative clinical LN staging was high: 15% of cN0 patients (54/362) had occult pathologic LN metastasis at surgery; 48% (31/64) of cN1 patients confirmed pN+. [PMID:34290393](../papers/34290393.md)
- [SMARCA4](../genes/SMARCA4.md) alteration (8% vs 1.8%, p=0.006) and [SMAD4](../genes/SMAD4.md) alteration (7% vs 1.5%, p=0.011) were significantly more frequent in pN-positive tumors and both retained independence in the final multivariable model ([SMARCA4](../genes/SMARCA4.md) OR 3.67, p=0.046; [SMAD4](../genes/SMAD4.md) OR 5.01, p=0.02). [PMID:34290393](../papers/34290393.md)
- [STK11](../genes/STK11.md) was enriched in pN-positive tumors (22% vs 12%, p=0.024) but did not retain significance in the final multivariable model. [PMID:34290393](../papers/34290393.md)
- Fraction of genome altered ([FGA](../genes/FGA.md)) was higher in pN-positive tumors (median 0.343 vs 0.269, p=0.037); whole-genome doubling was more frequent in pN+ (22% vs 13%, p=0.028). [PMID:34290393](../papers/34290393.md)
- APOBEC signatures (SBS2 and SBS13) were enriched in pN-positive tumors (SBS2: 27.3% vs 12.8%, p=0.03; SBS13: 31.8% vs 14.9%, p=0.02). [PMID:34290393](../papers/34290393.md)
- TMB did not differ between pN groups (median 4.9 vs 6.1 Mut/Mb, p=0.058). [PMID:34290393](../papers/34290393.md)

## Sources

- cBioPortal study: `luad_msk_npjpo_2021` (canonical, verified).
- Primary publication: [PMID:34290393](../papers/34290393.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
