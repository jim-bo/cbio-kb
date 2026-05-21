---
name: PD-L1 IHC 22C3 pharmDx
slug: pd-l1-ihc-22c3
kind: method
canonical_source: corpus
unverified: true
tags: [immunohistochemistry, biomarker, PD-L1, companion-diagnostic]
processed_by: wiki-cli
processed_at: 2026-05-21
---

# PD-L1 IHC 22C3 pharmDx

## Overview

PD-L1 IHC 22C3 pharmDx (Agilent/Dako) is an FDA-approved companion diagnostic [immunohistochemistry](../methods/immunohistochemistry.md) assay using the 22C3 monoclonal antibody to detect PD-L1 protein expression in formalin-fixed paraffin-embedded tumor tissue. Results are reported as a Combined Positive Score (CPS) — the number of PD-L1-staining cells (tumor cells, lymphocytes, macrophages) divided by the total number of viable tumor cells, multiplied by 100. CPS thresholds (e.g., ≥1, ≥10, ≥20) are used as biomarkers for anti-PD-1/PD-L1 therapy eligibility across multiple indications including HNSCC, gastric/GEJ, cervical, urothelial, and other cancers.

## Used by

- [PMID:38780927](../papers/38780927.md) — central PD-L1 IHC 22C3 pharmDx performed on tumor tissue from 51 evaluable patients with recurrent/second primary HNSCC enrolled on NCT03521570; CPS <20 vs. ≥20 showed no significant correlation with 1-year PFS (68.8% vs. 59.2%, P = .86) or [OS](../cancer_types/OS.md) (94.4% vs. 84.3%, P = .74), in contrast to its predictive utility in recurrent/metastatic HNSCC with single-agent PD-1 inhibition [PMID:38780927](../papers/38780927.md).
- PD-L1 IHC 22C3 TPS slides digitized and used as a texture-feature input to the DyAM multimodal model; PD-L1 TPS alone achieved AUC = 0.73, while IHC-G (automated texture) achieved AUC = 0.62 in the pathology validation cohort (n=52) [PMID:36038778](../papers/36038778.md)
- PD-L1 expression measured by IHC using clone 22C3 (Merck) on 30/34 [NSCLC](../cancer_types/NSCLC.md) patients treated with [pembrolizumab](../drugs/pembrolizumab.md); among PD-L1–expressing tumors with high mutation burden (>200 nonsynonymous mutations), DCB was 91% (10/11), demonstrating mutation burden and PD-L1 IHC capture complementary biomarker information [PMID:25765070](../papers/25765070.md)
- Referenced as the regulatory companion diagnostic comparator; the OrigiMed cohort used clone 28-8 (not 22C3) for PD-L1 IHC (TPS ≥1% threshold); combined IO biomarker positivity (MSI-H OR TMB-H OR PD-L1+) was 30.3% across 2,723 evaluable Chinese solid-tumor patients [PMID:35871175](../papers/35871175.md)

## Notes

- PD-L1 CPS by 22C3 did not stratify benefit in the reirradiation + [nivolumab](../drugs/nivolumab.md) context, suggesting that the predictive value of this biomarker may be attenuated when PD-1 blockade is combined with reirradiation in previously irradiated fields [PMID:38780927](../papers/38780927.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:38780927](../papers/38780927.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36038778](../papers/36038778.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25765070](../papers/25765070.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:35871175](../papers/35871175.md)

*This page was processed by **wiki-cli** on **2026-05-21**.*
