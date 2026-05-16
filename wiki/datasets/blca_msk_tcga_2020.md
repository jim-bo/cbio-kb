---
name: MSK + TCGA Bladder Cancer (ERCC2/Cisplatin) Cohort (2020)
studyId: blca_msk_tcga_2020
institution: Memorial Sloan Kettering Cancer Center / TCGA
size: 479
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-dna-seq
panels:
  - IMPACT300
  - IMPACT341
  - IMPACT410
tags:
  - bladder-cancer
  - BLCA
  - cisplatin
  - neoadjuvant-chemotherapy
  - ERCC2
  - primary-vs-secondary-MIBC
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# MSK + TCGA Bladder Cancer (ERCC2/Cisplatin) Cohort (2020)

## Overview

This combined MSK + TCGA cohort was assembled to investigate genomic differences between "primary" and "secondary" muscle-invasive bladder cancer (MIBC) and their association with differential response to cisplatin-based neoadjuvant chemotherapy (NAC). Primary MIBC is defined as de novo MIBC; secondary MIBC arises after prior non–muscle-invasive bladder cancer (NMIBC) treatment. The combined dataset includes a retrospective discovery cohort (TCGA WES + MSK WES/targeted capture) and a prospective validation cohort sequenced by MSK-IMPACT. Data are publicly available at cBioPortal (cbioportal.mskcc.org). [PMID:30290956](../papers/30290956.md)

## Composition

- **Clinical cohort:** 288 MSKCC patients with cT2–4aN0M0 [BLCA](../cancer_types/BLCA.md) treated with cisplatin-based NAC followed by radical cystectomy (May 2001 – July 2015); 245 primary MIBC (85%), 43 secondary MIBC (15%). [PMID:30290956](../papers/30290956.md)
- **Retrospective discovery genomic cohort:** 385 muscle-invasive (≥T2), chemotherapy-naïve pretreatment specimens (330 primary, 55 secondary) from 981 NGS-sequenced tumors — 412 by whole-exome sequencing (TCGA urothelial) plus 569 sequenced at MSKCC by WES or targeted exon capture. [PMID:30290956](../papers/30290956.md)
- **Prospective validation genomic cohort:** 94 consecutive chemotherapy-naïve MIBC tumors (70 primary, 24 secondary), sequenced prospectively 2014–2015 under MSKCC IRB #12–245 / NCT01775072. [PMID:30290956](../papers/30290956.md)
- **Combined genomic cohort total:** ~479 sequenced tumors (400 primary + 79 secondary MIBC, pooling discovery and validation). [PMID:30290956](../papers/30290956.md)
- **Reference genome:** GRCh37

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — TCGA and MSKCC components of the discovery cohort
- [msk-impact-panel](../methods/msk-impact-panel.md) — prospective validation cohort; three panel versions covering 300, 341, or 410 cancer-associated genes
- [IMPACT300](../methods/IMPACT300.md), [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md)

## Papers using this cohort

- [PMID:30290956](../papers/30290956.md) — Pietzak et al. 2019, "Genomic Differences Between 'Primary' and 'Secondary' Muscle-invasive Bladder Cancer as a Basis for Disparate Outcomes to Cisplatin-based Neoadjuvant Chemotherapy," *European Urology*

## Notable findings derived from this cohort

- **Lower pathologic response in secondary MIBC:** 26% (11/43) vs. 45% (110/245) with NAC (univariable p=0.02; multivariable OR=0.4, 95% CI 0.18–0.84, p=0.02). [PMID:30290956](../papers/30290956.md)
- **NAC detrimental in secondary MIBC:** cancer-specific survival was significantly worse with NAC versus cystectomy alone in secondary MIBC (p=0.002), while NAC improved recurrence-free survival in primary MIBC (p=0.042). [PMID:30290956](../papers/30290956.md)
- **[ERCC2](../genes/ERCC2.md) missense mutations enriched in primary MIBC:** discovery cohort 10.9% (36/330) primary vs. 1.8% (1/55) secondary (p=0.044); validation cohort 15.7% (12/70) primary vs. 0% (0/24) secondary (p=0.033); combined 12% (48/400) primary vs. 1.3% (1/79) secondary (unadjusted p=0.004). [PMID:30290956](../papers/30290956.md)
- **ERCC2-mutant tumors have higher TMB:** WES 14.7 vs. 5.5 mutations/Mb; targeted capture 25.0 vs. 8.5 mutations/Mb (both p<0.001). [PMID:30290956](../papers/30290956.md)
- **Secondary MIBC enriched for [FGFR3](../genes/FGFR3.md) (18%) and [ERBB2](../genes/ERBB2.md) (15%) alterations**, and RTK/MAPK pathway alterations in 42% of secondary MIBC. [PMID:30290956](../papers/30290956.md)
- **[STAG2](../genes/STAG2.md) and [TSC1](../genes/TSC1.md)** inactivating alterations were enriched in secondary MIBC (17% vs. 7.8% and 14% vs. 5.5%, respectively; univariable only, did not survive FDR correction). [PMID:30290956](../papers/30290956.md)

## Sources

- cBioPortal study ID: `blca_msk_tcga_2020`
- Available at cbioportal.mskcc.org
- NCT01775072 (MSKCC IRB #12–245)
- [PMID:30290956](../papers/30290956.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
