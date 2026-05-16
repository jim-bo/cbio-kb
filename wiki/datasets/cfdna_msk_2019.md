---
name: MSK cfDNA WBC-Paired Clonal Hematopoiesis Study (2019)
studyId: cfdna_msk_2019
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 124
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - liquid-biopsy
  - targeted-seq
  - whole-blood-seq
panels:
  - grail_cfdna_508
  - msk-impact-panel
tags:
  - cfDNA
  - liquid-biopsy
  - clonal-hematopoiesis
  - breast-cancer
  - lung-cancer
  - prostate-cancer
  - metastatic
  - WBC-paired
  - tumor-mutation-burden
  - MSI
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK cfDNA WBC-Paired Clonal Hematopoiesis Study (2019)

## Overview

This prospective cohort from Memorial Sloan Kettering Cancer Center profiles plasma cell-free DNA (cfDNA) alongside matched white-blood-cell (WBC) DNA from patients with metastatic breast cancer ([MBC](../cancer_types/MBC.md)), non-small cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)), and castration-resistant prostate cancer (CRPC), plus non-cancer controls. The study demonstrates that joint cfDNA + WBC sequencing is necessary to discriminate clonal hematopoiesis (CH) events from true tumor-derived mutations. Enrollment ran from September 24, 2015 through August 1, 2016 under MSKCC protocol 12-245 (NCT01775072). Tumor biopsies from the same patients were sequenced by the FDA-authorized MSK-IMPACT panel, enabling direct concordance analysis between tissue and liquid biopsy.

## Composition

- **Evaluable cancer patients:** 124 (of 161 enrolled): 39 MBC, 41 NSCLC, 44 CRPC
- **Non-cancer controls:** 47 (from San Diego Blood Bank; 50 enrolled, 3 excluded)
- **Cancer types:** metastatic breast ([BRCA](../cancer_types/BRCA.md)), NSCLC ([NSCLC](../cancer_types/NSCLC.md)), castration-resistant prostate ([PRAD](../cancer_types/PRAD.md))
- **Matched tumor biopsies:** all 124 cancer patients had [MSK-IMPACT](../methods/msk-impact-panel.md) tissue sequencing (mean >900X, 410 genes)
- **Stage:** all cancer patients had metastatic / advanced disease

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 410-gene FDA-authorized CLIA panel on matched tumor biopsies (mean >900X coverage)
- [grail_cfdna_508](../methods/grail_cfdna_508.md) — GRAIL targeted DNA assay: 508 genes, ~2 Mb, UMIs, >60,000X raw depth / ~4,400X median collapsed; error rate 1×10⁻⁵ to 3×10⁻⁵; 95% LoD ~0.36% VAF at 30 ng input
- [MSIsensor](../methods/msisensor.md) — depth-adjusted MSI calling on cfDNA
- [droplet-digital-pcr](../methods/droplet-digital-pcr.md) — orthogonal validation of selected VUSo

## Papers using this cohort

- [PMID:31768066](../papers/31768066.md) — Razavi et al. 2019, high-intensity cfDNA sequencing with matched WBC reveals pervasive clonal hematopoiesis in cancer patients

## Notable findings derived from this cohort

- At least one tumor-derived mutation was detected de novo in cfDNA in 104/124 patients (84%, 95% CI 76–90%); per-cancer rates: MBC 95%, NSCLC 76%, CRPC 82%. [PMID:31768066](../papers/31768066.md)
- 81.6% of cfDNA somatic mutations in controls and 53.2% in cancer patients were clonal hematopoiesis events identifiable only with matched WBC sequencing; 89.5% of cancer patients and 83% of controls had evidence of CH in cfDNA. [PMID:31768066](../papers/31768066.md)
- [PPM1D](../genes/PPM1D.md) truncating C-terminal mutations were significantly enriched in cancer patients vs controls (age-adjusted p=0.0115) and in chemotherapy/radiation-exposed patients (p=0.0008), establishing a therapy-related CH signal. [PMID:31768066](../papers/31768066.md)
- MSI-H was detected from cfDNA alone in one CRPC patient using MSIsensor; that patient received anti-PD-L1 therapy and showed rapid, sustained tumor regression by RECIST v1.1 and PSA. [PMID:31768066](../papers/31768066.md)
- cfDNA CNV detection of actionable amplifications ([ERBB2](../genes/ERBB2.md), [MET](../genes/MET.md)) was reliable only when ctDNA fraction ≥10%. [PMID:31768066](../papers/31768066.md)

## Sources

- cBioPortal study: `cfdna_msk_2019`
- ClinicalTrials.gov: NCT01775072
- Primary publication: [PMID:31768066](../papers/31768066.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
