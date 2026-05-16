---
name: Cone-Beam CT Image-Guided Radiotherapy (CBCT-IGRT)
slug: cone-beam-ct-igrt
kind: method
canonical_source: corpus
unverified: true
tags: [radiation-therapy, image-guidance, igrt, pancreatic-cancer, sbrt]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Cone-Beam CT Image-Guided Radiotherapy (CBCT-IGRT)

## Overview

Cone-beam CT image-guided radiotherapy (CBCT-IGRT) acquires a volumetric CT image immediately before or during each radiation treatment fraction using a kV or MV X-ray source mounted on the treatment gantry. The resulting image is registered to the planning CT to verify and correct patient and tumour positioning before beam delivery. In pancreatic SBRT, CBCT-IGRT enables daily verification of fiducial marker position and soft-tissue tumour location, supporting the tight PTV margins required for high-dose hypofractionated treatment.

## Used by

- CBCT-IGRT is described as a standard image-guidance component of the linac-based SBRT technical workflow reviewed in nine prospective trials of locally advanced pancreatic cancer; enables daily positional correction with fiducial markers to maintain tight PTV margins (2–5 mm) and protect adjacent OARs (duodenum, stomach, small bowel). [PMID:27826200](../papers/27826200.md)
- An alternating random forest (ARF) with auto-context model trained on 12 brain and 14 pelvis radiotherapy patients corrects CBCT images to planning-CT quality (brain MAE 12.81 ± 2.04 HU, pelvis MAE 19.94 ± 5.44 HU), enabling dosimetrically accurate CBCT-guided adaptive radiotherapy [PMID:30471129](../papers/30471129.md)

## Notes

- Typical workflow: acquire CBCT immediately before each SBRT fraction, register to planning CT using bony anatomy and/or implanted fiducials, apply couch corrections, then deliver treatment.
- Paired with 4D-CT simulation and endoscopic fiducial placement for comprehensive motion management in pancreatic SBRT.
- CBCT soft-tissue contrast is lower than diagnostic CT; fiducial markers are used as surrogate landmarks for the tumour centre.
- On-board imaging dose contribution (1–3 cGy per CBCT) is negligible relative to SBRT prescription doses (33 Gy / 5 fx).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:30471129](../papers/30471129.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
