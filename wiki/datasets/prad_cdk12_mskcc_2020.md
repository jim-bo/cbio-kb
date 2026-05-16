---
name: MSK CDK12-Mutant Prostate Cancer Pan-Cancer (Nguyen et al. 2020)
studyId: prad_cdk12_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 1875
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - prostate-cancer
  - CDK12
  - pan-cancer
  - MSK-IMPACT
  - tandem-duplicator
  - prognostic
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK CDK12-Mutant Prostate Cancer Pan-Cancer (Nguyen et al. 2020)

## Overview

Retrospective single-institution pan-cancer cohort of 26,743 MSK-IMPACT-sequenced tumors across 25 solid tumor types profiled between July 2014 and April 12, 2019. The prostate cancer subcohort (n=1,875) is released on cBioPortal as prad_cdk12_mskcc_2020 and provides the primary dataset for characterizing [CDK12](../genes/CDK12.md) alterations in prostate cancer. Cases with MSI sensor score >10 or TMB ≥20 mut/Mb were excluded to limit passenger [CDK12](../genes/CDK12.md) alterations. Clinical outcomes were evaluable for 1,465 prostate cancer patients. [PMID:32317181](../papers/32317181.md)

## Composition

- Prostate cancer subcohort: 1,875 patients; 100 with CDK12 alterations (CDK12-altered), 1,365 CDK12-WT (clinical outcomes evaluable subset: 1,465 total).
- Ovarian cancer subcohort: 1,034 patients; 43 with CDK12 alterations (for cross-cancer comparison).
- Full pan-cancer cohort: 26,743 patients across 25 solid tumor types.
- Cancer type: [prostate adenocarcinoma](../cancer_types/PRAD.md) (primary released cohort).
- CDK12-altered patients: higher rates of de-novo metastatic disease (40% vs. 26%), higher median PSA at diagnosis (14.8 vs. 9.0 ng/mL), higher Gleason ≥8 (80% vs. 57%). [PMID:32317181](../papers/32317181.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — three panel versions: [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md); all included CDK12.
- [FACETS](../methods/facets.md) for allele-specific copy number, zygosity, and clonality.
- [MutSigCV](../methods/mutsigcv.md) v1.4 for significantly mutated gene identification.
- [OncoKB](../methods/oncokb.md) (Aug 28, 2019) for oncogenic annotation. [PMID:32317181](../papers/32317181.md)

## Papers using this cohort

- [PMID:32317181](../papers/32317181.md) — Nguyen et al., pan-cancer characterization of CDK12 alterations; CDK12-biallelic prostate cancer defined as a distinct subtype with tandem-duplicator phenotype, CCND1/MCL1/MYC enrichment, TP53/ERG depletion, shorter [OS](../cancer_types/OS.md), and faster progression to castration resistance.

## Notable findings derived from this cohort

- [CDK12](../genes/CDK12.md) alterations in 404/26,743 (1.5%) pan-cancer; highest in prostate 100/1,875 (5.3%) and ovarian 43/1,034 (4.2%); MutSigCV: CDK12 significantly recurrently mutated only in prostate (FDR <0.001) and ovarian (FDR 0.056). [PMID:32317181](../papers/32317181.md)
- CDK12-biallelic inactivation in 73% (61/84) of CDK12-altered prostate cases; biallelic mechanism predominantly concurrent CDK12 mutations (75%); clonality 91% in prostate vs. 71% for other mutations (p<0.001). [PMID:32317181](../papers/32317181.md)
- CDK12-Bi prostate cancer showed higher fraction of genome gain, more copy-number breakpoints, and smaller median copy-number-altered segment size — consistent with a tandem duplicator phenotype; 13% of evaluated genome differentially altered vs. CDK12-WT. [PMID:32317181](../papers/32317181.md)
- CDK12-Bi enriched for [CCND1](../genes/CCND1.md), [MCL1](../genes/MCL1.md), [MYC](../genes/MYC.md) amplifications and [FANCA](../genes/FANCA.md) loss; depleted for [TP53](../genes/TP53.md) mutations and [TMPRSS2](../genes/TMPRSS2.md)–[ERG](../genes/ERG.md) fusions (all FDR <0.05). [PMID:32317181](../papers/32317181.md)
- CDK12-altered patients: shorter median OS from metastatic diagnosis (64.4 vs. 74.9 months; aHR 1.80, 95% CI 1.12–2.89; p=0.024) and shorter time to castration resistance (median 10.8 vs. 13.1 months; aHR 1.49, 95% CI 1.09–2.03; p=0.017). [PMID:32317181](../papers/32317181.md)
- No significant difference in time on first-line [abiraterone](../drugs/abiraterone.md) or [enzalutamide](../drugs/enzalutamide.md) between CDK12-altered and CDK12-WT patients (median 9.7 vs. 8.7 months; aHR 1.08; p=0.8). [PMID:32317181](../papers/32317181.md)

## Sources

- [PMID:32317181](../papers/32317181.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
