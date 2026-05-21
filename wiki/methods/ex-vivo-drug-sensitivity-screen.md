---
name: Ex vivo drug sensitivity screen
slug: ex-vivo-drug-sensitivity-screen
kind: method
canonical_source: corpus
unverified: true
tags:
  - functional-assay
  - drug-screen
  - ex-vivo
  - pharmacogenomics
processed_by: crosslinker
processed_at: 2026-05-21
---

# Ex vivo drug sensitivity screen

## Overview

An ex vivo drug sensitivity screen tests primary patient tumor or bone marrow cells against a panel of small-molecule inhibitors shortly after specimen collection, before cells are substantially altered by in vitro culture. Drug response is typically summarized as area under the dose-response curve (AUC) per drug per specimen. This approach enables pharmacogenomic integration with matched genomic and transcriptomic profiles from the same patient sample, facilitating identification of mutation-specific or expression-signature-driven drug sensitivities. Results are functional and patient-specific but do not directly predict clinical response, as ex vivo conditions differ from the in vivo tumor microenvironment.

## Used by

- The Beat [AML](../cancer_types/AML.md) platform screened 409 of 672 primary [AML](../cancer_types/AML.md) specimens (363 patients) within 24 hours of sample isolation against a panel of 122 small-molecule inhibitors; AUC was computed per drug. Integration with matched whole-exome sequencing and RNA-seq data identified single-gene and combinatorial mutation-specific sensitivities (e.g. FLT3-ITD + [NPM1](../genes/NPM1.md) → ibrutinib/entospletinib; [BCOR](../genes/BCOR.md) + [RUNX1](../genes/RUNX1.md) → JAK inhibitors); 64/122 drugs were significantly more sensitive in de novo vs transformed AML cases (FDR<0.1) [PMID:30333627](../papers/30333627.md).
- Ex vivo chemosensitivity screening of 65 rectal cancer tumoroids against 5-FU, FOLFOX, and ionizing radiation; ex vivo AUC correlated with patient PFS (Spearman r=0.86, p=0.024); radiation resistance ex vivo tracked with clinical non-response; tumoroids derived from as little as 2.8 mm biopsy [PMID:31591597](../papers/31591597.md).
- Applied to 942 AML specimens (Beat AML Waves 1–4) with probit dose-response curve fitting; identified 65 additional mutation–drug associations in the expanded cohort vs Waves 1+2 alone (27% increase in power); drug-family analysis across 25 drug families showed cell-state-biased response patterns [PMID:35868306](../papers/35868306.md)

## Notes

- Specimens must be processed within 24 hours of isolation to preserve primary cell viability; this limits feasibility to centers with rapid processing infrastructure.
- Ex vivo AUC does not map directly to clinical response; combinatorial sensitivities identified in the Beat AML study require clinical validation.
- Ibrutinib in particular has known broad off-target effects in continuous ex vivo culture, warranting cautious interpretation of single-drug response signals.
- The Beat AML Vizome browser (www.vizome.org) and dbGaP phs001657 provide public access to drug-sensitivity and genomic data from this assay.

## Sources

- [PMID:30333627](../papers/30333627.md) — Tyner et al. 2018, Beat AML multi-omics drug-sensitivity profiling ([aml_ohsu_2018](../datasets/aml_ohsu_2018.md)).

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31591597](../papers/31591597.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35868306](../papers/35868306.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
