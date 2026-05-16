---
name: iCARE (individualized Coherent Absolute Risk Estimation)
slug: icare
kind: method
canonical_source: corpus
unverified: true
tags:
  - absolute-risk-modeling
  - statistical-framework
  - epidemiology
  - myeloid-neoplasm
processed_by: crosslinker
processed_at: 2026-05-16
---

# iCARE (individualized Coherent Absolute Risk Estimation)

## Overview

iCARE is an R package for building and validating individualized [absolute](../methods/absolute.md) risk models. It combines relative risk estimates (from logistic regression, Cox models, or externally published hazard ratios) with population-level incidence rates and competing-mortality data to compute absolute (cumulative) risk over a specified time horizon. The framework is designed to be modular: users supply their own risk-factor model, the reference incidence rates (e.g., from SEER or NCCN tables), and competing-cause mortality rates, and iCARE integrates them into a coherent absolute-risk [estimate](../methods/estimate.md). It supports continuous and categorical risk factors and can incorporate genetic variants.

## Used by

- Bolton et al. used the iCARE R package to build a synthetic absolute-risk model for therapy-related myeloid neoplasm (tMN) in a hypothetical cohort of U.S. women aged 50–75 with breast cancer, combining clonal hematopoiesis hazard ratios (HR=6.9 for CH VAF >2%), NCCN AML/MDS incidence rates, and SEER competing-mortality data; the model projected that 96% of this population had 10-year absolute tMN risk <1%, but that the top-risk 1% (by CH and blood-count features) faced ≈9% excess absolute tMN risk from adjuvant chemotherapy [PMID:33106634](../papers/33106634.md)

## Notes

- iCARE is a statistical framework, not a sequencing or variant-calling method; output is risk probabilities, not genomic calls.
- The absolute-risk model in [PMID:33106634](../papers/33106634.md) is illustrative/synthetic; it combines externally derived HR estimates with SEER/NCCN rates and assumes a multiplicative risk model.
- The R package is available at: https://github.com/therneau/icare.
- Validation in that study was restricted to breast cancer as a use case; the framework is disease-agnostic.

## Sources

- [PMID:33106634](../papers/33106634.md) — Bolton et al., clonal hematopoiesis in 24,146 cancer patients; iCARE used for absolute tMN risk modeling to illustrate clinical decision context for CH-bearing patients.

*This page was processed by **crosslinker** on **2026-05-16**.*
