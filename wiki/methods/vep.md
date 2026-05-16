---
name: VEP (Variant Effect Predictor)
slug: vep
kind: method
canonical_source: corpus
unverified: true
tags: [annotation, variant-effect, functional-annotation]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# VEP (Variant Effect Predictor)

## Overview

VEP (Variant Effect Predictor), developed by Ensembl, annotates genetic variants with their predicted functional consequences (e.g., synonymous, missense, stop-gain, splice-site) using transcript databases and external tools (SIFT, PolyPhen-2, etc.). In the TCGA MC3 pipeline, VEP is invoked as part of the [vcf2maf](../methods/vcf2maf.md) annotation step to assign functional consequence to each variant.

## Used by

- Invoked as part of the vcf2maf annotation step in the TCGA MC3 pipeline for functional consequence annotation of ~22.5M somatic variants across 10,510 TCGA tumor/normal pairs [PMID:29596782](../papers/29596782.md)
- VEP v83 used to annotate somatic variants from whole-exome sequencing of 622 AML specimens in the Beat AML study [PMID:30333627](../papers/30333627.md)

## Notes

- VEP is the standard annotation engine used by vcf2maf; the version used affects HGVS notation and consequence predictions.
- Annotation accuracy depends on the transcript build and version of VEP used; MC3 used vcf2maf v1.6.11.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:30333627](../papers/30333627.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
