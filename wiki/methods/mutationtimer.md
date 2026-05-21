---
name: MutationTimeR
slug: mutationtimer
kind: method
canonical_source: corpus
unverified: true
tags: [clonal-timing, copy-number, wgs, somatic-evolution]
processed_by: entity-page-writer
processed_at: 2026-05-21
---

# MutationTimeR

## Overview

MutationTimeR (also written MutationTimer) is a probabilistic computational tool for inferring the relative timing of somatic mutations with respect to copy-number alteration (CNA) events in tumor genomes. It uses allele-specific copy-number states (from tools such as FACETS, ASCAT, or PURPLE) to classify somatic SNVs as either "clonal early" (occurring before CNA gains, therefore present on all copies) or "clonal late / subclonal" (occurring after CNA gains, present on a subset of copies). MutationTimeR thereby reconstructs the temporal ordering of oncogenic events — amplifications, deletions, and point mutations — during tumor evolution, enabling researchers to determine whether a given structural event (e.g., chromothripsis-derived ecDNA amplification) was an early founding event or a late subclonal acquisition.

## Used by

- Applied in WGS analysis of atypical small cell lung carcinoma (aSCLC; n = 11 WGS cases) at MSKCC; MutationTimeR placed all chromothripsis-associated oncogene amplifications (including [CCND1](../genes/CCND1.md) ecDNA and [CCND2](../genes/CCND2.md)/[CDK4](../genes/CDK4.md)/[MDM2](../genes/MDM2.md) co-amplifications on chromosomes 11 and 12) as clonally early events in tumorigenesis. Multi-sample analysis across 14 patients confirmed conservation of chromothriptic chromosomes and amplifications from primary to metastatic specimens. [PMID:39185963](../papers/39185963.md)

## Notes

- MutationTimeR was developed by Gerstung et al. (PCAWG Consortium) and is distributed as an R package.
- It requires phased or allele-specific copy-number calls as input; accuracy depends on tumor purity and sequencing depth. In the aSCLC study, WGS was performed at ~100× tumor / ~80× normal coverage on NovaSeq 6000 with FACETS for CN calling.
- Not present in `schema/ontology/gene_panels.json`; no gene-panel ID. Corpus-grown slug. See `schema/ontology/_observed.md`.
- Complementary to [ShatterSeek](../methods/shatterseek.md) (chromothripsis detection from SVs): ShatterSeek identifies which chromosomes underwent chromothripsis; MutationTimeR determines when those events occurred relative to point mutations.

## Sources

- [PMID:39185963](../papers/39185963.md)

*This page was processed by **entity-page-writer** on **2026-05-21**.*
