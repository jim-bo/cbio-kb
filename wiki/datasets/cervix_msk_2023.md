---
name: Cervical Cancer (MSK, Gynecologic Oncology 2023)
studyId: cervix_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 177
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [targeted-panel]
panels: []
tags: [cervical-cancer, cesc, msk-impact, hpv]
processed_by: crosslinker
processed_at: 2026-04-11
---

# Cervical Cancer (MSK, Gynecologic Oncology 2023)

## Overview

Single-center retrospective cohort of 177 patients with cervical cancer ([CESC](../cancer_types/CESC.md)) sequenced at Memorial Sloan Kettering Cancer Center from February 2014 through May 2019. Profiled with [MSK-IMPACT](../methods/msk-impact-panel.md) to characterize the genomic landscape and identify actionable alterations, with a survival subset (n=97) for [OS](../cancer_types/OS.md) analysis. Compared against [cesc_tcga_pan_can_atlas_2018](../datasets/cesc_tcga_pan_can_atlas_2018.md). [PMID:37643132](../papers/37643132.md)

## Composition

- 177 patients with cervical cancer; histologic subtypes: squamous cell carcinoma (n=69, 39%), usual endocervical adenocarcinoma (n=50, 28%), gastric-type endocervical adenocarcinoma (n=22, 12%), adenosquamous carcinoma (n=21, 12%), and other (n=15, 9%). [PMID:37643132](../papers/37643132.md)
- 60% primary tumors, 40% metastatic sites. [PMID:37643132](../papers/37643132.md)
- 80% of tumors HPV-positive (high-risk). [PMID:37643132](../papers/37643132.md)
- Actionability annotated using [OncoKB](../methods/oncokb.md) version 3.1.4. [PMID:37643132](../papers/37643132.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341-, 410-, or 468-gene panels), average 648x coverage. [PMID:37643132](../papers/37643132.md)

## Papers using this cohort

- [PMID:37643132](../papers/37643132.md) — Assessing the Genomic Landscape of Cervical Cancers: Clinical Opportunities and Therapeutic Targets.

## Notable findings derived from this cohort

- Most frequently altered genes: [PIK3CA](../genes/PIK3CA.md) (25%), [ERBB2](../genes/ERBB2.md) (12%), [KRAS](../genes/KRAS.md) (12%), [KMT2C](../genes/KMT2C.md) (10%), [KMT2D](../genes/KMT2D.md) (9%). [PMID:37643132](../papers/37643132.md)
- [KRAS](../genes/KRAS.md) mutations significantly enriched vs. TCGA (12% vs. 5%, P=0.019). [PMID:37643132](../papers/37643132.md)
- 13% of patients had TMB-high (>10 mut/Mb) tumors; 37% had at least one actionable alteration at OncoKB level 3B. [PMID:37643132](../papers/37643132.md)
- Oncogenic [TP53](../genes/TP53.md) mutations and HPV positivity were mutually exclusive: 3.5% of HPV-positive vs. 53.8% of non-gastric-type HPV-negative cases harbored oncogenic [TP53](../genes/TP53.md) alterations (P=0.00007). [PMID:37643132](../papers/37643132.md)
- Median OS for survival cohort (n=97): 59.2 months (95% CI: 46.7–89.4). [PMID:37643132](../papers/37643132.md)

## Sources

- cBioPortal study `cervix_msk_2023` [PMID:37643132](../papers/37643132.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
