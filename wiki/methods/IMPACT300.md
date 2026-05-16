---
name: MSK-IMPACT 300 (IMPACT300)
slug: IMPACT300
kind: gene-panel
canonical_source: cbioportal
unverified: false
tags:
  - panel
  - msk-impact
  - targeted-sequencing
processed_by: crosslinker
processed_at: 2026-05-16
genePanelId: IMPACT300
---

# MSK-IMPACT 300 (IMPACT300)

## Overview

MSK-IMPACT 300 is the first-generation 300-gene targeted hybrid-capture sequencing panel developed at Memorial Sloan Kettering Cancer Center (MSKCC). It profiles cancer-associated genes for somatic mutations, copy-number alterations, and [select](../methods/select.md) structural variants in paired tumor/normal specimens. Panel ID `IMPACT300` is registered in cBioPortal's gene-panel ontology. It was superseded by the 341-gene ([IMPACT341](IMPACT341.md)), 410-gene ([IMPACT410](IMPACT410.md)), and 468-gene ([IMPACT468](IMPACT468.md)) versions as the prospective MSK genotyping program expanded.

## Used by

- [MSK-IMPACT panel (generic)](msk-impact-panel.md) — generic slug covering all MSK-IMPACT panel generations.
- Applied across three panel generations (IMPACT300/341/410) in a prospective validation cohort of 94 chemotherapy-naïve MIBC tumors (2014–2015); [FANCC](../genes/FANCC.md) data were missing for 6 patients sequenced on the 300-gene panel due to limited gene coverage [PMID:30290956](../papers/30290956.md).

## Notes

- 300 cancer-associated genes captured by targeted exon capture and sequenced on Illumina platforms in a CLIA-certified laboratory (MSKCC IRB #12-245 / NCT01775072).
- Smaller gene set than successor panels; FANCC not included, limiting DDR gene coverage relative to IMPACT341/410.
- Mutation burden is normalized by panel size for inter-panel comparisons.

## Sources

- [PMID:30290956](../papers/30290956.md) — Pietzak et al. 2019, primary/secondary MIBC and cisplatin-based NAC outcomes.

*This page was processed by **crosslinker** on **2026-05-16**.*
