---
name: vcf2maf
slug: vcf2maf
kind: method
canonical_source: corpus
unverified: true
tags: [annotation, format-conversion, pipeline]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# vcf2maf

## Overview

vcf2maf is a Perl/Python tool that converts VCF (Variant Call Format) files to the Mutation Annotation Format (MAF) used by TCGA and cBioPortal, while simultaneously annotating variants with functional consequences via VEP (Variant Effect Predictor). It handles multi-allelic sites, applies common-population-variant filters (e.g., based on ExAC/gnomAD allele counts), and produces the standardized MAF columns required for downstream analyses.

## Used by

- Used in the TCGA MC3 pipeline (v1.6.11) to convert ensemble VCFs to MAF format and apply the "Common in ExAC" filter (AC > 16 unless ClinVar-pathogenic); the AC = 16 threshold was anchored to [SF3B1](../genes/SF3B1.md) K700E as the highest ExAC count observed for a known clonal-hematopoiesis somatic event [PMID:29596782](../papers/29596782.md)
- vcf2maf used to convert VCF variant calls to MAF format for AML whole-exome sequencing data in the Beat AML study (aml_ohsu_2018) [PMID:30333627](../papers/30333627.md)
- Used for re-annotation of external reference cohorts (AACR GENIE, TCGA, Foundation Medicine) with VEP v88 in the 923-patient MSK glioma study ([glioma_mskcc_2019](../datasets/glioma_mskcc_2019.md)) [PMID:31263031](../papers/31263031.md)

## Notes

- vcf2maf v1.6.11 was the version used in MC3; later versions may behave differently for edge cases.
- The ExAC/gnomAD allele count threshold used by vcf2maf is a critical parameter that affects which variants are labeled as germline.
- Produces standardized MAF columns compatible with cBioPortal import and downstream tools such as MutSig2CV.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:30333627](../papers/30333627.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31263031](../papers/31263031.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
