---
name: Sarcoma DNA-Methylation Classifier
slug: sarcoma-methylation-classifier
kind: method
canonical_source: corpus
unverified: true
tags: [methylation, classification, sarcoma]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Sarcoma DNA-Methylation Classifier

## Overview

The sarcoma DNA-methylation classifier (Koelsche et al.) is a machine-learning classifier trained on genome-wide DNA methylation profiles (Infinium EPIC or 450k arrays) from a large reference cohort of sarcoma subtypes. It assigns a tumor's methylation profile to one of several defined sarcoma methylation classes and returns a calibrated prediction score. A high score (typically >0.9) indicates reliable subclass assignment; low scores or "no class match" indicate an epigenetically novel or unclassifiable entity.

## Used by

- Applied to a urinary bladder [EWSR1](../genes/EWSR1.md)::[BEND2](../genes/BEND2.md) fusion sarcoma using Infinium MethylationEPIC v2.0 data (Koelsche et al. v13 classifier); the tumor did not match any sarcoma classifier subclass, indicating a novel or uncharacterized epigenetic entity [PMID:28199314](../papers/28199314.md)

## Notes

- Reference classifier: Koelsche et al., published by the German Cancer Research Center (DKFZ) group.
- Failure to classify (no class match) may indicate a genuinely novel entity, sample quality issues, or admixture with normal tissue.
- Often interpreted alongside the brain-tumor methylation classifier for tumors with ambiguous lineage.

## Sources

- [PMID:28199314](../papers/28199314.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
