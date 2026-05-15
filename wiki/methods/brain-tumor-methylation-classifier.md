---
name: Brain Tumor DNA-Methylation Classifier
slug: brain-tumor-methylation-classifier
kind: method
canonical_source: corpus
unverified: true
tags: [methylation, classification, brain-tumor, cns]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Brain Tumor DNA-Methylation Classifier

## Overview

The brain tumor DNA-methylation classifier (Capper et al., Nature 2018) is a random forest classifier trained on genome-wide DNA methylation profiles from a large reference cohort of ~100 distinct CNS tumor types and subtypes. It assigns a tumor's methylation profile to a CNS tumor methylation class and returns a calibrated prediction score (0 to 1). The classifier is available at www.molecularneuropathology.org and is considered a standard clinical tool for CNS tumor classification, particularly for histologically ambiguous cases.

## Used by

- Applied to a urinary bladder [EWSR1](../genes/EWSR1.md)::[BEND2](../genes/BEND2.md) fusion sarcoma using Infinium MethylationEPIC v2.0 data; returned a low-confidence prediction score of 0.364 for the MN1-rearranged astroblastoma class — suggesting weak epigenetic similarity to [MN1](../genes/MN1.md)::BEND2-rearranged CNS tumors but below the threshold for reliable classification [PMID:28199314](../papers/28199314.md)

## Notes

- Calibrated scores >0.9 are generally considered reliable for clinical classification.
- Scores between 0.3 and 0.9 (ambiguous range) indicate uncertain class membership and require clinical/histological correlation.
- The classifier includes astroblastoma, MN1-altered and related BEND2-rearranged subclasses that share epigenetic features with some extra-CNS FET-family fusion sarcomas.
- Reference: Capper D et al., Nature 2018; PMID: 29539639.

## Sources

- [PMID:28199314](../papers/28199314.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
