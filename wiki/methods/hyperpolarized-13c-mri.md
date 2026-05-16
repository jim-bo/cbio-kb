---
name: Hyperpolarized 13C MRI
slug: hyperpolarized-13c-mri
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, mri, metabolic-imaging, prostate-cancer]
processed_by: crosslinker
processed_at: 2026-05-16
---

# Hyperpolarized 13C MRI

## Overview

Hyperpolarized [1-13C] pyruvate MRI (HP-MRI) is a metabolic imaging technique that uses dissolution dynamic nuclear polarization (dDNP) to transiently increase the MRI signal of carbon-13-labeled substrates by >10,000-fold. When [1-13C] pyruvate is injected intravenously, its real-time conversion to [1-13C] lactate is measured in vivo by 13C spectroscopic imaging, providing a non-invasive readout of glycolytic flux (Warburg effect). The maximum lactate-to-pyruvate ratio (Lac_max) serves as the primary biomarker output. Imaging requires a specialized dual-tuned 1H/13C radiofrequency coil and a clinical scanner capable of 13C detection.

## Used by

- 3T wide-bore GE MR750w scanner with dual-tuned 1H/13C endorectal coil; 17 hyperpolarized [1-13C] pyruvate injections across 12 prostate cancer patients pre-radical prostatectomy; Lac_max was significantly higher in tumor vs. normal prostate (p=0.0001 for Gleason 3, p<0.0001 for Gleason ≥4) and correlated with MCT1 ([SLC16A1](../genes/SLC16A1.md)) IHC expression; test/re-test stable within 1 hr (p=0.2) [PMID:31564440](../papers/31564440.md).

## Notes

- Corpus-grown slug; no matching `genePanelId` in cBioPortal ontology.
- Clinical trial: NCT02421380 (MSK IRB#14-205); performed May 2015–July 2018.
- Pyruvate preparation: 14.2 M [1-13C] pyruvate with 15 mM trityl radical, dissolved, neutralized with Tris/NaOH, terminally sterilized; dose 0.43 mL/kg of 250 mM IV.
- Temporal resolution 4.9 s per EPSI frame; spatial resolution 1×1×1.5-cm³ voxels — partial-volume contamination limits intratumoral heterogeneity analysis.
- Lac_max correlates poorly with PSA (R²=0.26) and prostate/tumor volume (<0.20) — the metabolic signal is distinct from bulk-disease markers.
- Bicarbonate signal (reflecting oxidative flux via pyruvate dehydrogenase) detected in only 1/12 patients at this field strength.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
