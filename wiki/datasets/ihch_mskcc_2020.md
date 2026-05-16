---
name: MSK Intrahepatic Cholangiocarcinoma Cohort (MSKCC, Clin Cancer Res 2021)
studyId: ihch_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 573
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - intrahepatic-cholangiocarcinoma
  - lymph-node-metastasis
  - hepatic-arterial-infusion-chemotherapy
  - retrospective-cohort
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# MSK Intrahepatic Cholangiocarcinoma Cohort (MSKCC, Clin Cancer Res 2021)

## Overview

Single-institution retrospective cohort of 573 patients with liver-limited intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)) treated at Memorial Sloan Kettering Cancer Center from 2000–2018. Patients received curative-intent resection (N=237), hepatic arterial infusion chemotherapy (HAIC with floxuridine via hepatic arterial infusion pump; N=196), or systemic chemotherapy alone (SYS; N=140). MSK-IMPACT genomic profiling was performed on 219 patients across three successive panel versions. The study focuses on treatment-related outcomes stratified by lymph-node status and defines a genomic high-risk composite (TP53 mutation, KRAS mutation, or CDKN2A/B deletion) that predicts poor prognosis in node-positive disease. [PMID:33963001](../papers/33963001.md)

## Composition

- 573 patients with liver-limited [IHCH](../cancer_types/IHCH.md), treated 2000–2018 at MSKCC.
- Treatment groups: resection (N=237, 41.4%), HAIC (N=196, 34.2%), SYS (N=140, 24.4%).
- N1 (lymph-node-positive) breakdown: 38/237 resected (16.0%), 56/196 HAIC (28.6%), 57/140 SYS (40.7% by imaging-based criteria).
- Genomic profiling: 219/433 resection+HAIC patients (50.6%) via MSK-IMPACT: [IMPACT341](../methods/IMPACT341.md) (N=26), [IMPACT410](../methods/IMPACT410.md) (N=93), [IMPACT468](../methods/IMPACT468.md) (N=100).
- Sequencing tissue source: primary tumors (91.5%), local recurrence (2.8%), extrahepatic recurrence (1.9%), lymph-node metastases (6.6%). [PMID:33963001](../papers/33963001.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted panel across three successive versions: [IMPACT341](../methods/IMPACT341.md) (N=26), [IMPACT410](../methods/IMPACT410.md) (N=93), [IMPACT468](../methods/IMPACT468.md) (N=100).
- Oncogenic-driver calls based on [OncoKB](../methods/oncokb-annotation.md). [PMID:33963001](../papers/33963001.md)

## Papers using this cohort

- [PMID:33963001](../papers/33963001.md) — Jolissaint et al., *Clin Cancer Res* 2021: For node-negative IHC, resection produced the longest median OS (59.9 months) vs HAIC (24.9 months) vs SYS (13.7 months; p<0.001); for node-positive IHC, resection and HAIC were equivalent (19.7 vs 18.1 months; p=0.560) and both outperformed SYS (11.2 months; p=0.024). A composite genomic "high-risk" set (TP53/KRAS mutation or CDKN2A/B deletion) stratified N1 patients into poor (median OS 12.1 months) vs favorable (30.9 months) prognosis (p=0.002). [PMID:33963001](../papers/33963001.md)

## Notable findings derived from this cohort

- Eleven genes altered in ≥5% of profiled patients; top five: [IDH1](../genes/IDH1.md) (18.7%), [ARID1A](../genes/ARID1A.md) (15.5%), [FGFR2](../genes/FGFR2.md) (15.5%), [TP53](../genes/TP53.md) (14.6%), [BAP1](../genes/BAP1.md) (13.2%). [PMID:33963001](../papers/33963001.md)
- CDKN2A/B deletion independently predicted worse OS in N1 disease: [CDKN2A](../genes/CDKN2A.md) deletion HR 3.3 (95% CI 1.1–9.5, p=0.030); [CDKN2B](../genes/CDKN2B.md) deletion HR 6.0 (95% CI 2.5–14.6, p<0.001); median OS ~7 vs ~27 months for CDKN2A/B-deleted vs wild-type N1 patients. [PMID:33963001](../papers/33963001.md)
- IDH1/2 mutations and FGFR2 fusions had no significant impact on survival in the N1 setting; N1 patients with these alterations should not be excluded from locoregional therapy on this basis alone. [PMID:33963001](../papers/33963001.md)
- 10/49 (20.4%) IDH1/2-mutant patients received ivosidenib or vorasidenib on clinical trial. [PMID:33963001](../papers/33963001.md)

## Sources

- cBioPortal study `ihch_mskcc_2020`.
- Jolissaint JS, et al. *Intrahepatic Cholangiocarcinoma with Lymph Node Metastasis: Treatment-Related Outcomes and the Role of Tumor Genomics in Patient Selection.* Clin Cancer Res. 2021. [PMID:33963001](../papers/33963001.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
