---
name: Multistate Markov model (non-homogeneous semi-Markov)
slug: multistate-markov-model
kind: method
canonical_source: corpus
unverified: true
tags:
  - statistics
  - survival-analysis
  - multistate
  - competing-risks
  - longitudinal
processed_by: crosslinker
processed_at: 2026-05-16
---

# Multistate Markov model (non-homogeneous semi-Markov)

## Overview

A multistate Markov model is a statistical framework that tracks individuals through a series of clinical states (e.g., disease-free, loco-regional recurrence, distant recurrence, cancer death, non-cancer death) over time. In a non-homogeneous semi-Markov extension, transition intensities are time-varying (non-homogeneous) and the sojourn-time distribution in each state depends on time spent there (semi-Markov), enabling modeling of complex disease trajectories with competing risks. This approach correctly handles non-cancer death as a competing event rather than a censored observation, avoiding overestimation of disease-specific death rates in older patient populations.

## Used by

- Applied to 3,240 breast cancer patients (15,394 state transitions from 3,147 patients; median 9.77-year follow-up) from five UK/Canada tumor banks in the METABRIC-anchored analysis, with molecular data on 1,980 patients ([brca_metabric](../datasets/brca_metabric.md)); the model tracked five states (loco-regional recurrence, distant recurrence, cancer death, non-cancer death, alive without recurrence) and showed that treating non-cancer deaths as censored overestimates disease-specific death by 9 percentage points at 20 years in ER+ patients (0.46 vs 0.37) [PMID:30867590](../papers/30867590.md)

## Notes

- Applied in combination with IntClust and PAM50 molecular subtype assignments to model subtype-specific recurrence trajectories across 20 years of follow-up.
- The model enabled identification of differential metastatic timing and site patterns across breast cancer subtypes (e.g., ER+ patients more often presented first metastasis in bone; ER- patients had more visceral relapse and faster sequential relapses).
- A patient-level recurrence predictor derived from this model is hosted at https://caldaslab.cruk.cam.ac.uk/brcarepred.
- Not in cBioPortal gene-panels or molecular-profiles ontologies; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
