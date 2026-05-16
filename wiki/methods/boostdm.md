---
name: BoostDM
slug: boostdm
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [driver-classification, machine-learning, cancer-genomics]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# BoostDM

## Overview

BoostDM is a machine-learning model for classifying individual somatic mutations as driver or passenger events within specific cancer types and genes. It integrates features such as mutational signature exposure, 3D protein structure, functional impact scores, and population genetics signals to produce per-mutation driver probabilities.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to classify individual somatic mutations as driver events in the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)

## Notes

- Developed by the Hartwig Medical Foundation / IRB Barcelona group (Alexandrov/Lopez-Bigas labs).
- Provides cancer-type-specific driver probability scores, distinguishing it from pan-cancer classifiers.
- Used alongside IntOGen for driver discovery in the Sherlock-Lung study.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
