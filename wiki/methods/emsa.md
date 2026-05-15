---
name: EMSA (Electrophoretic Mobility Shift Assay)
slug: emsa
kind: method
canonical_source: corpus
unverified: true
tags:
  - protein-dna-interaction
  - transcription-factor-binding
  - allele-specific
  - functional-validation
processed_by: crosslinker
processed_at: 2026-05-15
---

# EMSA (Electrophoretic Mobility Shift Assay)

## Overview

Electrophoretic Mobility Shift Assay (EMSA), also known as gel-shift or band-shift assay, is a technique used to detect protein-DNA or protein-RNA interactions. Labeled DNA probes (often radiolabeled or fluorescently labeled) are incubated with protein extract; protein-bound complexes migrate more slowly through a native polyacrylamide gel than unbound probes, appearing as shifted bands. Super-shift EMSA uses antibodies against specific proteins to confirm the identity of a binding protein. In the context of GWAS functional validation, EMSA with allele-specific probes can confirm that a candidate causal SNP alters TF binding affinity.

## Used by

- EMSA and super-shift EMSA performed in 293T and LNCaP cells using rs4519489 A and T allele probes; showed stronger binding of nuclear extract to the A allele (specifically displaced by unlabeled consensus competitor), confirming allele-specific protein binding at the prostate cancer risk locus. Flag-USF1 super-shift EMSA in LNCaP and 22Rv1 cells confirmed [USF1](../genes/USF1.md) as the A-allele-preferring binder [PMID:28927585](../papers/28927585.md)

## Notes

- EMSA validates allele-specific binding inferred by SNPs-seq and is used alongside ChIP-qPCR and proteomics for mechanistic confirmation.
- Super-shift variant confirms TF identity by antibody-induced further shift of the protein-DNA complex.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
