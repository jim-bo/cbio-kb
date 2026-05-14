---
name: Melanoma (MSK, NEJM 2014)
studyId: skcm_mskcc_2014
institution: Memorial Sloan Kettering Cancer Center / Broad Institute
size: 64
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
panels: []
tags:
  - melanoma
  - skcm
  - immunotherapy
  - checkpoint-blockade
  - whole-exome-seq
  - ctla4-blockade
  - neoantigens
  - tumor-mutational-burden
processed_by: crosslinker
processed_at: 2026-05-14
---

# Melanoma (MSK, NEJM 2014)

## Overview

Whole-exome sequencing cohort of 64 patients with metastatic cutaneous melanoma ([SKCM](../cancer_types/SKCM.md)) treated with anti-CTLA-4 checkpoint blockade ([ipilimumab](../drugs/ipilimumab.md) or [tremelimumab](../drugs/tremelimumab.md)) at Memorial Sloan Kettering Cancer Center. Generated to investigate the genomic basis of response to CTLA-4 blockade, with a focus on tumor mutational load and neoantigen signatures as predictors of long-term clinical benefit. Sequencing was performed at MSKCC Genomics Core and the Broad Institute.

## Composition

- **Cancer type:** Cutaneous melanoma ([SKCM](../cancer_types/SKCM.md)), metastatic
- **Sample count:** 64 patients; 128 exomes (tumor + matched blood/normal)
- **Cohort structure:** Discovery set (25 patients: 11 long-term benefit, 14 minimal/no benefit); validation set (39 patients: 25 long-term benefit, 14 minimal/no benefit)
- **Treatment:** 59 patients received [ipilimumab](../drugs/ipilimumab.md); 5 received [tremelimumab](../drugs/tremelimumab.md)
- **Clinical outcome definition:** Long-term benefit = radiographic freedom from disease or stable/decreased disease >6 months; minimal/no benefit = ≤6 months or progression on every CT
- **Reference genome:** hg19

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): SureSelect Human All Exon 50-Mb capture (Agilent) → Illumina HiSeq 2000; mean tumor coverage 103×; >99% of target bases ≥10×

## Papers using this cohort

- [PMID:25409260](../papers/25409260.md) — Snyder et al., *New England Journal of Medicine* 2014. "Genetic Basis for Clinical Response to CTLA-4 Blockade in Melanoma."

## Notable findings derived from this cohort

- High tumor mutational load (nonsynonymous exome mutations) was significantly associated with long-term clinical benefit from anti-CTLA-4 therapy in both discovery (P=0.01, Mann–Whitney) and validation (P=0.009, Mann–Whitney) cohorts; survival advantage for >100 nonsynonymous mutations was significant in the discovery set (P=0.04, log-rank) [PMID:25409260](../papers/25409260.md).
- A set of 101 shared tetrapeptide neoepitopes (identified by HLA-restricted MHC class I binding ≤500 nM using the NAseek algorithm) was exclusive to long-term benefiters in the discovery set and reproduced in the independent validation set; patients carrying the neoantigen signature had markedly longer overall survival (P<0.001 log-rank in both sets) [PMID:25409260](../papers/25409260.md).
- High mutation load alone did not guarantee response — several patients with >1,000 nonsynonymous mutations showed minimal/no benefit — indicating that neoantigen quality (pathogen-homologous tetrapeptides) provides additive predictive value beyond raw TMB [PMID:25409260](../papers/25409260.md).
- Two patient-specific neoantigens — TESPFEQHI (from [FAM3C](../genes/FAM3C.md) c.A577G, HLA-B4402 binder) and GLEREGFTF (from [CSMD1](../genes/CSMD1.md) c.G10337A) — elicited polyfunctional IFN-γ+/TNF-α+ CD8+ T-cell responses ex vivo, providing experimental validation of the neoantigen-driven immune response model [PMID:25409260](../papers/25409260.md).

## Sources

- cBioPortal study: `skcm_mskcc_2014`
- EGA/dbGaP: available via cbioportal.org
- Citation: Snyder et al. NEJM 2014 [PMID:25409260](../papers/25409260.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
