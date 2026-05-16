---
name: MSK Melanoma BRAF-WT MAPK MSK-IMPACT 2020
studyId: mel_mskimpact_2020
institution: Memorial Sloan Kettering Cancer Center
size: 696
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - melanoma
  - MAPK
  - immunotherapy
  - targeted-sequencing
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Melanoma BRAF-WT MAPK MSK-IMPACT 2020

## Overview

Retrospective cohort of 696 patients with cutaneous melanoma (556, 80%) or melanoma of unknown primary (140, 20%) prospectively sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) at Memorial Sloan Kettering Cancer Center and Lehigh Valley Health Network between January 2014 and April 2019. The study characterized oncogenic RTK-RAS-MAPK pathway alterations across 28 pathway genes, built a 9-group MAPK driver classifier, and linked driver group to time-to-treatment-failure (TTF) on frontline PD-1 monotherapy and combination [nivolumab](../drugs/nivolumab.md)+[ipilimumab](../drugs/ipilimumab.md). Data are available at cBioPortal (`http://cbioportal.org/study?id=mel_mskimpact_2020`).

## Composition

- **Cancer types:** [Cutaneous Melanoma (SKCM)](../cancer_types/SKCM.md), melanoma of unknown primary ([CUP](../cancer_types/CUP.md))
- **N = 696** patients; 792 tumors analyzed, 756 (95.4%) sequenced successfully
- **Treatment cohorts:** 181 patients on frontline PD-1 monotherapy ([pembrolizumab](../drugs/pembrolizumab.md) or [nivolumab](../drugs/nivolumab.md)); 141 on nivolumab + [ipilimumab](../drugs/ipilimumab.md)
- **Assay versions:** [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md); median sequencing depth 709×; exclusion threshold <20% tumor purity or <50× depth
- **Clonality:** [FACETS](../methods/facets.md) applied to 428 samples with adequate quality
- **Oncogenicity:** restricted to variants annotated oncogenic by [OncoKB](../methods/oncokb-annotation.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — hybridization-capture NGS
- [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)
- [FACETS](../methods/facets.md) — allele-specific copy-number and clonality
- [OncoKB](../methods/oncokb-annotation.md) — oncogenicity annotation
- [Kaplan-Meier](../methods/kaplan-meier.md) / [Cox proportional hazards](../methods/cox-proportional-hazards.md) — survival statistics

## Papers using this cohort

- [PMID:33509808](../papers/33509808.md) — MSK melanoma MAPK driver landscape and immunotherapy outcomes

## Notable findings derived from this cohort

- 670/696 tumors (96%) harbored an oncogenic RTK-RAS-MAPK pathway alteration in ≥1 of 28 pathway genes; 33% had ≥2 concurrent drivers. [PMID:33509808](../papers/33509808.md)
- Driver frequencies: [BRAF](../genes/BRAF.md) V600E/K/R 31%, [NRAS](../genes/NRAS.md) Q61 29%, [NF1](../genes/NF1.md) loss-of-function 23%, [MAP2K1](../genes/MAP2K1.md)/[MAP2K2](../genes/MAP2K2.md) 7%, [KIT](../genes/KIT.md) 4%; overall median TMB 16.3 mut/Mb ([NF1](../genes/NF1.md) highest at 43 mut/Mb). [PMID:33509808](../papers/33509808.md)
- TTF on PD-1 monotherapy (N=181) varied sharply by MAPK driver group: [NRAS](../genes/NRAS.md) Q61 4.2 months, [BRAF](../genes/BRAF.md) V600 7.5 months, NF1 22 months, Other not reached (log-rank p<0.0001); no driver-group effect on nivolumab+ipilimumab. [PMID:33509808](../papers/33509808.md)
- TMB was an independent predictor of TTF (HR 0.43 per 10-fold increase, 95% CI 0.29–0.62, p<0.0001) and [OS](../cancer_types/OS.md) on both PD-1 monotherapy and combination immunotherapy. [PMID:33509808](../papers/33509808.md)
- Among 172 BRAF V600 wild-type patients progressing on checkpoint blockade, 27 received genomically matched targeted therapy; 8/27 (30%) had ≥6-month benefit, including durable complete responses to [crizotinib](../drugs/crizotinib.md) ([ROS1](../genes/ROS1.md) fusion), [larotrectinib](../drugs/larotrectinib.md) ([NTRK1](../genes/NTRK1.md) fusion), [trametinib](../drugs/trametinib.md) (BRAF K601E + [MAP2K1](../genes/MAP2K1.md) E203K), and [PLX8394](../drugs/plx8394.md) (BRAF-AGK fusion). [PMID:33509808](../papers/33509808.md)

## Sources

- cBioPortal study: `mel_mskimpact_2020`
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
