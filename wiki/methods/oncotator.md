---
name: Oncotator
slug: oncotator
kind: method
canonical_source: corpus
unverified: true
tags: [variant-annotation, bioinformatics, cancer-genomics]
processed_by: crosslinker
processed_at: 2026-05-09
---

# Oncotator

## Overview

Oncotator is a cancer-focused variant annotation tool developed at the Broad Institute. It annotates somatic mutations with information from multiple cancer-specific databases including COSMIC, OncoKB, and UniProt, providing protein change information, functional impact predictions, and known oncogenicity classifications specifically tailored to somatic variant interpretation.

## Used by

- Applied alongside [annovar](../methods/annovar.md) for somatic variant annotation in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases); annotated SNVs and indels discovered by genome-wide sequencing in the pediatric brain tumor cohort [PMID:23817572](../papers/23817572.md)
- Used to annotate somatic variants from whole-exome sequencing of 45 [BRAF](../genes/BRAF.md) V600 metastatic melanoma tumors (DeCOG cohort) aligned to hg19 via the Broad Picard/Firehose pipeline [PMID:24265153](../papers/24265153.md).

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Now largely superseded by Funcotator in GATK4 workflows, but widely used in early TCGA-era analyses.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
