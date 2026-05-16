---
name: Endometrial Cancer (MSK, 2018)
studyId: ucec_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 197
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel
  - copy-number
  - msi-scoring
panels:
  - IMPACT341
  - IMPACT410
tags:
  - ucec
  - endometrial-cancer
  - msk
  - prospective-sequencing
  - msi
  - mmr-deficiency
  - actionable-alterations
processed_by: crosslinker
processed_at: 2026-05-16
---

# Endometrial Cancer (MSK, 2018)

## Overview

A prospective tumor/matched-normal sequencing cohort of 197 tumors from 189 patients with advanced endometrial cancer treated at Memorial Sloan Kettering Cancer Center. Sequenced using the MSK-IMPACT panel (341- or 410-gene versions) at average ~735× coverage. The cohort is enriched for high-grade and metastatic disease relative to the [TCGA UCEC](../datasets/ucec_tcga.md) reference cohort, and serves as a benchmark for the clinical utility of prospective molecular profiling in advanced endometrial cancer. Published by Soumerai, Donoghue, Bandlamudi et al. (Hyman lab, MSK) in Clinical Cancer Research 2018.

## Composition

- 189 patients / 197 tumors (including 8 paired primary–metastatic cases).
- Histologic breakdown: endometrioid carcinoma 75/189 (FIGO grades 1–3), serous carcinoma 46/189, carcinosarcoma 35/189, mixed 15/189, clear cell 13/189, undifferentiated/dedifferentiated 4/189, neuroendocrine 1/189 — all under [UCEC](../cancer_types/UCEC.md).
- 95% advanced disease (FIGO III–IV at diagnosis or recurrence); 51% samples from metastatic sites; 39% sequenced after chemotherapy, 11% after hormonal therapy.
- 70 samples on [IMPACT341](../methods/IMPACT341.md); 127 on [IMPACT410](../methods/IMPACT410.md).
- 154/189 retained for copy-number analysis after excluding <20% tumor purity samples.

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) / [IMPACT410](../methods/IMPACT410.md) — targeted DNA sequencing of 341 or 410 genes; matched tumor/normal pairs; ~735× mean coverage.
- [facets](../methods/facets.md) v0.5.6 — allele-specific copy-number calling (cval=100); used for copy-number cluster analysis and WGD detection.
- [msisensor](../methods/msisensor.md) v0.2 — genomic MSI scoring (MSI-H threshold ≥10).
- [mutational-signatures](../methods/mutational-signatures.md) — NMF-based decomposition for hypermutated samples.
- [immunohistochemistry](../methods/immunohistochemistry.md) — MMR IHC ([MLH1](../genes/MLH1.md), [PMS2](../genes/PMS2.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md)) for MSI status confirmation.
- [oncokb-annotation](../methods/oncokb-annotation.md) — actionability annotation (as of 22-Dec-2016).

## Papers using this cohort

- [PMID:30068706](../papers/30068706.md) — Soumerai et al. Clin Cancer Res 2018: "Clinical Utility of Prospective Molecular Characterization in Advanced Endometrial Cancer."

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) mutations in 63% of MSK cohort vs. 36% in [ucec_tcga](../datasets/ucec_tcga.md) (p=4×10⁻⁵); [PTEN](../genes/PTEN.md) alterations more common in TCGA (56% vs. 22%, p=8×10⁻⁹) — difference attributable to histologic enrichment for high-grade/serous disease [PMID:30068706](../papers/30068706.md).
- Hierarchical clustering of FACETS copy-number profiles identified a novel Cluster C (heterozygous losses across the genome, high-grade endometrioid/non-endometrioid) with significantly worse PFS₁ (median 9.6 vs. 17.4 months for Cluster A, p=0.006) [PMID:30068706](../papers/30068706.md).
- Genomic MSI calling (MSIsensor + mutational-signature decomposition) recovered one MMR-D case scored MMR-proficient by IHC, demonstrating added sensitivity of NGS-based MSI assessment [PMID:30068706](../papers/30068706.md).
- 67% of patients (127/189) carried ≥1 potentially actionable alteration by OncoKB; 27% of those enrolled to matched targeted-therapy trials; 47% of matched patients achieved clinical benefit [PMID:30068706](../papers/30068706.md).
- [ERBB2](../genes/ERBB2.md) amplification in 16/189 (enriched in serous, p=0.018); one heavily pretreated serous patient achieved a 14-month ongoing complete response to [ado-trastuzumab-emtansine](../drugs/ado-trastuzumab-emtansine.md) (T-DM1) [PMID:30068706](../papers/30068706.md).
- Three pathogenic germline [BRCA2](../genes/BRCA2.md) mutations (two carcinosarcoma, one serous) and one germline [MLH1](../genes/MLH1.md) Lynch-syndrome splice mutation identified via universal tumor/normal sequencing [PMID:30068706](../papers/30068706.md).
- [ESR1](../genes/ESR1.md) ligand-binding-domain hotspot mutations in 5 endometrioid patients, including 3/5 arising in apparent absence of prior endocrine therapy — first report of de novo [ESR1](../genes/ESR1.md) mutations in endometrial cancer [PMID:30068706](../papers/30068706.md).

## Sources

- cBioPortal study: `ucec_msk_2018`
- Citation: Soumerai et al. Clin Cancer Res 2018; DOI: 10.1158/1078-0432.CCR-18-0412

*This page was processed by **crosslinker** on **2026-05-16**.*
