---
name: SigMA (Mutational Signatures)
slug: sigma-mutational-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, hrd, cosmic, targeted-sequencing, genomics]
processed_by: crosslinker
processed_at: 2026-04-16
---

# SigMA (Mutational Signatures)

## Overview

SigMA is a computational tool for detecting mutational signatures — in particular COSMIC SBS3 (associated with homologous recombination deficiency, HRD) — from targeted panel sequencing data such as [MSK-IMPACT](../methods/msk-impact-panel.md). Standard mutational-signature decomposition requires whole-genome or whole-exome sequencing for reliable signal; SigMA adapts this analysis to the reduced mutation counts available from targeted panels by applying likelihood-ratio tests and machine-learning classifiers trained on WGS-calibrated data. The tool reports high-confidence and low-confidence SBS3 calls, with high-confidence calls used as HRD assignment surrogates when WGS is unavailable.

## Used by

- [PMID:35764743](../papers/35764743.md) — SigMA applied to [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing data from 130 MSKCC [HGSOC](../cancer_types/HGSOC.md) patients with research consent to detect COSMIC SBS3 (HRD signature); high-confidence SBS3 in 48 patients, low-confidence in 30; SigMA-derived HRD status combined with [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md)/DDR variant evidence and [CDK12](../genes/CDK12.md)/[CCNE1](../genes/CCNE1.md) subtype rules for final genomic-subtype assignment; genomic HRD status on its own had test concordance c = 0.52 in late-stage HGSOC [PMID:35764743](../papers/35764743.md).

## Notes

- SBS3 in COSMIC corresponds to exposure to defective homologous recombination-based DNA repair; it is elevated in [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md)-mutant tumors but also in a subset of BRCA-wildtype HRD tumors.
- SigMA's panel-adapted calling introduces uncertainty relative to WGS; the authors of the [HGSOC](../cancer_types/HGSOC.md) multimodal study note that patients sequenced only with germline HRD-DDR panels (not [MSK-IMPACT](../methods/msk-impact-panel.md)) had looser HRD assignments.
- The tool is publicly available and was designed specifically for clinical panel data where mutation burden is low.
- SigMA outputs are distinct from the Myriad myChoice HRD genomic instability score (GIS) and BRCA-centered germline tests; all three approaches classify HRD but with different sensitivities and specificities.

## Sources

- [PMID:35764743](../papers/35764743.md)

*This page was processed by **crosslinker** on **2026-04-16**.*
