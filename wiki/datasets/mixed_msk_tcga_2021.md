---
name: RAD51B Associated Mixed Cancers (MSK, NPJ Breast Cancer 2021)
studyId: mixed_msk_tcga_2021
institution: Memorial Sloan Kettering Cancer Center; The Cancer Genome Atlas (TCGA)
size: 18087
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - TARGETED_SEQUENCING
  - WHOLE_EXOME_SEQUENCING
panels:
  - msk-impact-panel
tags:
  - breast cancer
  - ovarian cancer
  - germline
  - RAD51B
  - homologous recombination deficiency
  - MSK-IMPACT
  - TCGA
  - hereditary cancer
processed_by: crosslinker
processed_at: 2026-05-16
---

# RAD51B Associated Mixed Cancers (MSK, NPJ Breast Cancer 2021)

## Overview

mixed_msk_tcga_2021 is a mixed-cancer cohort assembled from the MSK-IMPACT clinical sequencing programme (18,087 cancer patients with paired tumor/germline data; 2,265 breast and 1,157 ovarian cases) and supplementary TCGA cases, used to characterise the cancer-predisposition risk conferred by germline loss-of-function variants in [RAD51B](../genes/RAD51B.md). The primary analysis focused on 3,422 consecutive breast or ovarian cancer patients who consented to germline sequencing, benchmarked against gnomAD non-cancer controls (n = 138,632). Reference genome: hg19.

## Composition

- Cancer types: mixed — predominantly [BRCA](../cancer_types/BRCA.md) (2,265) and [OVARY](../cancer_types/OVARY.md) (1,157) within the primary breast/ovarian sub-cohort
- 18,087 total cancer patients in the broader MSK discovery arm; 3,422 in the germline-consented breast/ovarian sub-cohort
- 6 additional cases from TCGA (validation)
- Germline sequencing via [MSK-IMPACT](../methods/msk-impact-panel.md); whole-exome sequencing for 5 biallelic cases used in HRD/signature analysis
- Copy-number and LOH calls: [FACETS](../methods/facets.md); mutational signatures: [SigMA](../methods/sigma-mutational-signatures.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — primary targeted-panel NGS with tumor/normal (germline) pairs
- Whole-exome sequencing ([whole-exome-seq](../methods/whole-exome-seq.md)) — restricted to 5 biallelic RAD51B cases for HRD characterisation

## Papers using this cohort

- [PMID:34635660](../papers/34635660.md) — Setton et al., NPJ Breast Cancer 2021: Germline RAD51B variants confer susceptibility to breast and ovarian cancers deficient in homologous recombination

## Notable findings derived from this cohort

- Among 3,422 breast/ovarian cancer patients with germline consent, 9 (0.26%) carried RAD51B LOF germline variants vs 0.10% in gnomAD controls (OR 2.69, 95% CI 1.4–5.3, p = 0.004); 6/18 LOF carriers showed tumour LOH vs 6/59 VUS carriers (p = 0.02), consistent with biallelic selection [PMID:34635660](../papers/34635660.md)
- Biallelic RAD51B inactivation (germline LOF + LOH) was associated with dominant Signature 3 and LST ≥ 15 (HRD) in all 5 cases with WES data, at an intermediate level between [WT](../cancer_types/WT.md) and biallelic BRCA1/BRCA2 loss [PMID:34635660](../papers/34635660.md)

## Sources

- cBioPortal study: `https://www.cbioportal.org/study/summary?id=mixed_msk_tcga_2021`
- Citation: Setton et al., NPJ Breast Cancer 2021, [PMID:34635660](../papers/34635660.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
