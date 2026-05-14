---
name: Ampullary Carcinoma
oncotree_code: AMPCA
main_type: Ampullary Cancer
parent: AMPULLA_OF_VATER
tags:
  - periampullary
  - ampullary
  - gi
processed_by: crosslinker
processed_at: 2026-05-14
---

# Ampullary Carcinoma (AMPCA)

## Overview

Ampullary carcinoma arises at the ampulla of Vater, where the common bile duct and pancreatic duct join the duodenum. In the OncoTree hierarchy it sits under the Ampulla of Vater tissue node (parent: AMPULLA_OF_VATER). Clinically it is grouped with distal bile-duct (extrahepatic) cholangiocarcinoma and duodenal adenocarcinoma as the three periampullary cancers, all resected by pancreatoduodenectomy (Whipple procedure). Histologically, two IHC subtypes are recognised — pancreatobiliary (CK7+/CK20-) and intestinal (CK7-/CK20+) — but molecular profiling shows these subtypes do not cleanly segregate the driver mutation landscape.

## Cohorts in the corpus

- [ampca_bcm_2016](../datasets/ampca_bcm_2016.md) — 98 ampullary adenocarcinomas from the Australian Pancreatic Cancer Genome Initiative (APGI), Baylor College of Medicine, MD Anderson, and TU Dresden, all from patients who underwent curative-intent pancreatoduodenectomy; whole-exome sequencing + SNP-array CNAs + RNA-seq (28/98 subset); reference genome GRCh37 [PMID:26804919](../papers/26804919.md).

## Recurrent alterations

- WNT pathway mutated in 49% of AMPCA tumors (significantly lower than 72% in DUOAC and higher than 30% in CAC; ChiSq p < 0.05); intestinal-subtype AMPCA is 67% WNT-altered vs. 30% in pancreatobiliary tumors [PMID:26804919](../papers/26804919.md).
- [ELF3](../genes/ELF3.md) inactivating frameshift/nonsense mutations in 10.6% of periampullary tumors overall; predominantly AMPCA-enriched; mutation rate ~3× higher than in any other cancer in cBioPortal at the time; [ELF3](../genes/ELF3.md) loss-of-function co-occurs with WNT-pathway mutations in 71% of cases (Chi-square p = 0.02); proposed early driver (found in a duodenal adenoma with intraepithelial neoplasia) [PMID:26804919](../papers/26804919.md).
- [SMAD4](../genes/SMAD4.md) — most commonly mutated TGF-β-pathway gene in AMPCA and [EHCH](../cancer_types/EHCH.md) (sites anatomically closest to the pancreas) [PMID:26804919](../papers/26804919.md).
- [ARID1A](../genes/ARID1A.md), [ARID2](../genes/ARID2.md) — most frequent SWI/SNF chromatin-remodeling alterations; equally distributed across all three periampullary tumor types [PMID:26804919](../papers/26804919.md).
- [KDM4C](../genes/KDM4C.md) — statistically significant focal chromosome-9 deletion removing the promoter and 5′ end, reducing [KDM4C](../genes/KDM4C.md) expression and the upstream [UHRF2](../genes/UHRF2.md); significant specifically in AMPCA [PMID:26804919](../papers/26804919.md).
- [PMS2](../genes/PMS2.md) — germline Lynch-syndrome gene mutated in ~50% of MSI-positive periampullary patients, disproportionately high vs. <5% in general Lynch-syndrome populations [PMID:26804919](../papers/26804919.md).
- MSI present in 12 patients overall (AMPCA 3%); all 6 MSI-AMPAC patients were alive 2–8 years post-diagnosis (p = 0.04); MSI confers dramatically elevated mutation rates (68/Mb in AMPAC MSI vs. 3.8/Mb MSS) [PMID:26804919](../papers/26804919.md).
- RTK/RAS/PI3K pathway activated in 84–94% across all periampullary sites (including [KRAS](../genes/KRAS.md), [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md)) [PMID:26804919](../papers/26804919.md).

## Subtypes

- **Pancreatobiliary subtype** (IHC CK7+/CK20-): 51% of AMPCA in the APGI/BCM cohort; associated with pancreatobiliary morphology but IHC-based and molecular-based subtype assignment agreed only 53–77% of the time [PMID:26804919](../papers/26804919.md).
- **Intestinal subtype** (IHC CK7-/CK20+): 34% of AMPCA; enriched for WNT-pathway alterations (67% vs. 30% in pancreatobiliary); associated with better prognosis in some series.
- **MSI-high subset**: 3% of AMPCA; dramatically elevated mutation burden; all 6 MSI patients in this cohort survived 2–8 years post-surgery [PMID:26804919](../papers/26804919.md).

## Therapeutic landscape

- **WNT pathway inhibitors**: With ~49% of AMPCA WNT-mutated, the authors propose AMPCA, [DA](../cancer_types/DA.md), and [EHCH](../cancer_types/EHCH.md) should be classified as a single "WNT+/–" entity for therapeutic stratification; small-molecule β-catenin inhibitors were in clinical trials at the time of publication [PMID:26804919](../papers/26804919.md).
- **MSI as a prognostic biomarker**: MSI strongly predicts favorable outcome; situates AMPCA alongside CRC in candidate MSI-directed immunotherapy contexts [PMID:26804919](../papers/26804919.md).
- **[PMS2](../genes/PMS2.md) germline screening**: May be disproportionately valuable in periampullary tumors vs. general Lynch-syndrome populations [PMID:26804919](../papers/26804919.md).

## Sources

- [PMID:26804919](../papers/26804919.md) — Gingras et al. (2016), whole-exome sequencing of 160 periampullary tumors.

*This page was processed by **crosslinker** on **2026-05-14**.*
