---
name: SigMA (Mutational Signatures)
slug: sigma-mutational-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, hrd, cosmic, targeted-sequencing, genomics]
processed_by: crosslinker
processed_at: 2026-04-30
---

# SigMA (Mutational Signatures)

## Overview

SigMA is a computational tool for detecting mutational signatures — in particular COSMIC SBS3 (associated with homologous recombination deficiency, HRD) — from targeted panel sequencing data such as [MSK-IMPACT](../methods/msk-impact-panel.md). Standard mutational-signature decomposition requires whole-genome or whole-exome sequencing for reliable signal; SigMA adapts this analysis to the reduced mutation counts available from targeted panels by applying likelihood-ratio tests and machine-learning classifiers trained on WGS-calibrated data. The tool reports high-confidence and low-confidence SBS3 calls, with high-confidence calls used as HRD assignment surrogates when WGS is unavailable.

## Used by

- [PMID:35764743](../papers/35764743.md) — SigMA applied to [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing data from 130 MSKCC [HGSOC](../cancer_types/HGSOC.md) patients with research consent to detect COSMIC SBS3 (HRD signature); high-confidence SBS3 in 48 patients, low-confidence in 30; SigMA-derived HRD status combined with [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md)/DDR variant evidence and [CDK12](../genes/CDK12.md)/[CCNE1](../genes/CCNE1.md) subtype rules for final genomic-subtype assignment; genomic HRD status on its own had test concordance c = 0.52 in late-stage [HGSOC](../cancer_types/HGSOC.md) [PMID:35764743](../papers/35764743.md).
- [PMID:39746944](../papers/39746944.md) — mutational signature analysis (COSMIC v3.4, SigProfilerAssignment v0.1.8) applied to the MiMSI prospective cohort (n=5,037); MMR-D samples showed median MMR-signature contribution of 0.62 vs 0.036 in MMR-P; MSH6-loss tumors had the lowest MMR-signature contribution (median 0.42) and MLH1-loss the highest (median 0.67) among the four MMR proteins [PMID:39746944](../papers/39746944.md).
- [PMID:39975212](../papers/39975212.md) — mutational signature decomposition (SigProfilerAssignment v0.1.8 against COSMIC v3.4) applied to 297 clonally expanded single melanocytes; UV-attributable SBS7 (sum of SBS7a–d) dominated HighMut cells while clock-like SBS1/SBS5 dominated LowMut cells; signature fractions were compared by Wilcoxon rank-sum (p<0.0001) [PMID:39975212](../papers/39975212.md).

## Notes

- SBS3 in COSMIC corresponds to exposure to defective homologous recombination-based DNA repair; it is elevated in [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md)-mutant tumors but also in a subset of BRCA-wildtype HRD tumors.
- SigMA's panel-adapted calling introduces uncertainty relative to WGS; the authors of the [HGSOC](../cancer_types/HGSOC.md) multimodal study note that patients sequenced only with germline HRD-DDR panels (not [MSK-IMPACT](../methods/msk-impact-panel.md)) had looser HRD assignments.
- The tool is publicly available and was designed specifically for clinical panel data where mutation burden is low.
- SigMA outputs are distinct from the Myriad myChoice HRD genomic instability score (GIS) and BRCA-centered germline tests; all three approaches classify HRD but with different sensitivities and specificities.

## Sources

- [PMID:35764743](../papers/35764743.md)
- [PMID:39746944](../papers/39746944.md)
- [PMID:39975212](../papers/39975212.md)

*This page was processed by **crosslinker** on **2026-04-30**.*
