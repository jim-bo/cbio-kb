---
name: StarDist (Nucleus Segmentation)
slug: stardist-nuclei
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, nucleus-segmentation, histopathology, whole-slide-imaging, computational-pathology]
processed_by: crosslinker
processed_at: 2026-04-16
---

# StarDist (Nucleus Segmentation)

## Overview

StarDist is a deep-learning nucleus segmentation method that represents each nucleus as a star-convex polygon defined by radial distances from a central point, enabling accurate delineation of densely packed nuclei in histology images. It was developed for fluorescence and H&E tissue images and is available as a Python library and as a plugin for the QuPath whole-slide image analysis platform. StarDist produces instance segmentation masks (one mask per nucleus) together with confidence scores, enabling downstream measurement of nuclear morphometric features such as area, diameter, eccentricity, and texture.

## Used by

- [PMID:35764743](../papers/35764743.md) — StarDist used in QuPath to segment tumor nuclei from pre-treatment H&E whole-slide images of 444 [HGSOC](../cancer_types/HGSOC.md) patients; nuclei were detected across >1.4 million 128×128 px (64×64 µm) tiles after Macenko stain normalization; 216 histopathological features were computed per tile including nuclear morphometry and tissue-class composition (from a weakly supervised ResNet-18 tissue classifier trained on 60 annotated WSIs); 24 features had significant univariate log(HR) in Cox regression, and 20 described tumor nuclear diameter or size; the final two-feature histopathological submodel used mean tumor nuclear area and stromal major axis length (training c-index 0.56, test c-index 0.54) [PMID:35764743](../papers/35764743.md).

## Notes

- StarDist's star-convex polygon parameterization is particularly suited to round-to-oval nuclei; it may under-segment elongated stromal nuclei or irregular necrotic cells.
- In the [HGSOC](../cancer_types/HGSOC.md) multimodal study, larger tumor nuclei on H&E were associated with shorter overall survival; the authors hypothesize this may reflect whole-genome doubling or cellular fusion events.
- The combination of StarDist segmentation with a tissue-type classifier (trained separately) enables cell-type-specific feature extraction — here, distinguishing tumor, stroma, and other tissue compartments before computing nuclear morphometry per compartment.
- StarDist is open source: https://github.com/stardist/stardist.

## Sources

- [PMID:35764743](../papers/35764743.md)

*This page was processed by **crosslinker** on **2026-04-16**.*
