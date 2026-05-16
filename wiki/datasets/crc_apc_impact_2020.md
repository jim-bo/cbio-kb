---
name: MSK CRC APC Mutation Cohort (MSK-IMPACT, 2020)
studyId: crc_apc_impact_2020
institution: Memorial Sloan Kettering Cancer Center
size: 430
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - colorectal-cancer
  - metastatic
  - microsatellite-stable
  - wnt-pathway
  - apc-mutation-site
  - retrospective
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK CRC APC Mutation Cohort (MSK-IMPACT, 2020)

## Overview

The crc_apc_impact_2020 cohort comprises 430 patients with microsatellite-stable (MSS) unresectable metastatic colorectal cancer ([COADREAD](../cancer_types/COADREAD.md)) treated at Memorial Sloan Kettering Cancer Center with first-line chemotherapy between 2014 and 2017, whose tumors were genomically profiled by the [MSK-IMPACT panel](../methods/msk-impact-panel.md). The study was designed to evaluate whether specific [APC](../genes/APC.md) mutation location (N-terminal vs. C-terminal relative to amino acid 1400) or DNA damage response (DDR) alterations were prognostic in this setting. [PMID:32730818](../papers/32730818.md)

## Composition

- **n = 430** patients with MSS unresectable metastatic CRC; includes both [COAD](../cancer_types/COAD.md) and [READ](../cancer_types/READ.md) primaries.
- Treated with first-line chemotherapy at MSK between 2014 and 2017.
- Tumor profiling by [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing; allele-specific copy number by [FACETS](../methods/facets.md); large state transitions (LST) for HRD assessment.
- Survival analysis from first-line treatment start using [Kaplan-Meier](../methods/kaplan-meier.md) and [Cox proportional hazards](../methods/cox-proportional-hazards.md) regression. [PMID:32730818](../papers/32730818.md)

## Assays / panels (linked)

- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — targeted NGS for somatic variant calling.
- [FACETS](../methods/facets.md) — allele-specific copy-number analysis; LST computation.

## Papers using this cohort

- [PMID:32730818](../papers/32730818.md) — Mondaca et al. (2020): [APC](../genes/APC.md) mutation site (N-terminal vs. C-terminal at aa 1400) is prognostic in MSS metastatic CRC; N-terminal APC mutations associate with longer [OS](../cancer_types/OS.md) and PFS; DDR alterations are not prognostic.

## Notable findings derived from this cohort

- [APC](../genes/APC.md) truncating mutation was independently associated with longer PFS (HR 0.68, p<0.001) and OS (HR 0.56, p<0.001) versus tumors with no Wnt pathway alteration; the effect was driven by N-terminal (≤aa 1400) vs. C-terminal (>aa 1400) position. [PMID:32730818](../papers/32730818.md)
- C-terminal [APC](../genes/APC.md) mutations co-occurred more frequently with [KRAS](../genes/KRAS.md) (72% vs. 46%), [BRAF](../genes/BRAF.md) (13% vs. 2%), [PIK3CA](../genes/PIK3CA.md) (28% vs. 11%), and [PTEN](../genes/PTEN.md) (12% vs. 3%) alterations (all p<0.01). [PMID:32730818](../papers/32730818.md)
- [CTNNB1](../genes/CTNNB1.md) and [RNF43](../genes/RNF43.md) alterations co-occurred with RAS pathway alterations in 63% and 71% of cases, respectively, and identified poor-prognosis mCRC. [PMID:32730818](../papers/32730818.md)
- DDR pathway alterations were not associated with survival or with response to [oxaliplatin](../drugs/oxaliplatin.md)-containing chemotherapy (HR 1.1, 95% CI 0.7–1.6, p=0.74); no patient had an LST score >15 (the proposed HRD cutoff). [PMID:32730818](../papers/32730818.md)

## Sources

- cBioPortal study `crc_apc_impact_2020`.
- Mondaca et al. (2020) *Gastroenterology* [PMID:32730818](../papers/32730818.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
