---
name: Low-Grade Serous Ovarian Cancer (MSK, Clin Cancer Res 2022)
studyId: lgsoc_mapk_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 119
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [msk-impact]
panels: [IMPACT341, IMPACT410, IMPACT468, IMPACT505]
tags: [lgsoc, ovarian-cancer, mapk, msk-impact, germline]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Low-Grade Serous Ovarian Cancer (MSK, Clin Cancer Res 2022)

## Overview

MSK-IMPACT targeted sequencing cohort of 119 patients with centrally pathology-reviewed low-grade serous ovarian carcinoma (LGSC), including primary peritoneal LGSC and serous borderline tumors with invasive implants, treated at MSK between April 2015 and February 2021. Drawn from 2,063 epithelial ovarian carcinomas sequenced on MSK-IMPACT. Designed to characterize the MAPK pathway alteration landscape and its association with overall survival and platinum sensitivity in LGSC. [PMID:35443055](../papers/35443055.md)

## Composition

- **n=119** patients with centrally reviewed LGSC; cancer type: [LGSOC](../cancer_types/LGSOC.md).
- Tumor samples: primary (n=81) and recurrent (n=38); matched normal blood for all.
- 92% FIGO stage III/IV advanced disease; median age 48 years (range 20–79); median [OS](../cancer_types/OS.md) follow-up 62.7 months.
- Germline testing in 79/119 (66%) patients via custom 76–90 gene panels at MSK plus outside labs.
- 16 patients (13%) self-identified as Ashkenazi Jewish; MSIsensor score median 0.12 (all evaluable cases MSS). [PMID:35443055](../papers/35443055.md)

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md): four successive versions — [IMPACT341](../methods/IMPACT341.md) (n=8), [IMPACT410](../methods/IMPACT410.md) (n=23), [IMPACT468](../methods/IMPACT468.md) (n=83), [IMPACT505](../methods/IMPACT505.md) (n=5); median sequencing depth 588× (range 94–1,231×).
- Germline: custom cancer-predisposition gene panels (76–90 genes) at MSK and outside laboratories.
- LOH inferred via [FACETS](../methods/facets.md). [PMID:35443055](../papers/35443055.md)

## Papers using this cohort

- [PMID:35443055](../papers/35443055.md) — Manning-Geist et al., *Clin Cancer Res* 2022: somatic and germline landscape of MAPK alterations in 119 LGSCs; primary discovery study for this dataset.

## Notable findings derived from this cohort

- MAPK pathway alteration in 71/119 (60%) of LGSCs: [KRAS](../genes/KRAS.md) 33%, [NRAS](../genes/NRAS.md) 11%, [BRAF](../genes/BRAF.md) 11%, [EIF1AX](../genes/EIF1AX.md) 10%, [CDKN2A](../genes/CDKN2A.md) homozygous deletion 8%; [ERBB2](../genes/ERBB2.md) alterations in 5 cases. [PMID:35443055](../papers/35443055.md)
- MAPK pathway alteration is an independent favorable prognostic factor for OS in LGSC on multivariate analysis (HR 2.5 [1.2–5.2] for absence vs presence, p=0.019); platinum sensitivity also independently favorable (HR 0.4, p=0.005). [PMID:35443055](../papers/35443055.md)
- Median OS: 339 months (MAPK-altered) vs 125 months (MAPK-wildtype); 234 months (platinum-sensitive) vs 45 months (platinum-resistant). [PMID:35443055](../papers/35443055.md)
- No pathogenic germline [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md) mutations in any of 79 tested patients — sharply distinguishing LGSC from HGSC despite 13% Ashkenazi Jewish representation in the cohort. [PMID:35443055](../papers/35443055.md)
- 18% of LGSCs (n=21) lacked detectable driver alterations despite adequate tumor purity; sequential re-sequencing in 8 patients showed 2/5 initially driver-negative tumors acquired MAPK alterations at recurrence. [PMID:35443055](../papers/35443055.md)
- Low tumor mutational burden: median 1.8 mutations/Mb; all 102 evaluable cases microsatellite stable. [PMID:35443055](../papers/35443055.md)

## Sources

- cBioPortal study `lgsoc_mapk_msk_2022`; reference genome hg19. [PMID:35443055](../papers/35443055.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
