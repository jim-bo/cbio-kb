---
name: Wearable sensor monitoring
slug: wearable-sensor-monitoring
kind: method
canonical_source: corpus
unverified: true
tags: [wearables, digital-health, continuous-monitoring, multi-omics, longitudinal]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Wearable sensor monitoring

## Overview

Wearable sensor monitoring refers to the continuous or near-continuous collection of physiological and behavioral data via body-worn electronic devices (e.g., smartwatches, fitness trackers, continuous glucose monitors, ECG patches). Measured parameters commonly include heart rate, heart rate variability, blood oxygen saturation (SpO2), skin temperature, electrodermal activity, accelerometry (physical activity/sleep), and, increasingly, continuous interstitial glucose. In research settings, wearable data is integrated with molecular omics layers (genomics, transcriptomics, proteomics, [metabolomics](../methods/metabolomics.md)) to capture real-time environmental and behavioral exposures that explain variance in molecular phenotypes not attributable to static genetic factors.

## Used by

- Reviewed as one of the core data modalities in multi-omics integration for precision health alongside WGS, WES, RNA-seq, proteomics, DNA methylation, metabolomics, and [lipidomics](../methods/lipidomics.md); Babu and Snyder (2023) propose that by 2030 multi-omics will be routinely combined with real-time wearable monitoring and microbiome analysis for management of chronic disease, including cancer. [PMID:37119971](../papers/37119971.md)
- The iPOP longitudinal study used wearable data integrated with molecular omics across 20 time points to characterize transitions from healthy to insulin-resistant states — demonstrating the feasibility of wearable-plus-omics integration in clinical research. [PMID:37119971](../papers/37119971.md)

## Notes

- In oncology, wearable monitoring is primarily investigational: applications include tracking treatment toxicity, fatigue, and activity decline during chemotherapy or immunotherapy, and post-treatment surveillance.
- No gene-panel ID. Corpus-grown slug. See `schema/ontology/_observed.md`.
- Data governance challenges (privacy, consent, HIPAA/GDPR compliance) are explicitly flagged in the Babu & Snyder review as barriers to clinical integration of continuous wearable streams with molecular data.

## Sources

- [PMID:37119971](../papers/37119971.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
