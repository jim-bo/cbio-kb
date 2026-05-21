---
name: Nearest Template Prediction (NTP)
slug: nearest-template-prediction
kind: method
canonical_source: corpus
unverified: true
tags: [classification, transcriptomics, subtype-assignment]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Nearest Template Prediction (NTP)

## Overview

Nearest Template Prediction (NTP) is a gene-expression-based classification algorithm that assigns samples to predefined molecular subtypes by computing the distance (typically Pearson correlation or cosine similarity) between each sample's expression profile and template centroids representing each subtype. It is robust to batch effects and does not require retraining, making it well-suited for applying subtypes derived from one cohort to external datasets.

## Used by

- Used in [prad_organoids_msk_2022](../datasets/prad_organoids_msk_2022.md) to assign 366 CRPC patients (266 SU2C + 100 WCM) from bulk RNA-seq to one of four CRPC subtypes (CRPC-AR, CRPC-NE, CRPC-WNT, CRPC-SCL) defined by ATAC-seq in organoid models; NTP and SVM classifiers agreed on 92% (WCM) and 85% (SU2C) of samples [PMID:35617398](../papers/35617398.md)

## Notes

- NTP is particularly useful for projecting experimentally derived molecular subtypes onto independent clinical cohorts with bulk RNA-seq data.
- Agreement with orthogonal classifiers (e.g., SVM) strengthens confidence in subtype assignments.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
