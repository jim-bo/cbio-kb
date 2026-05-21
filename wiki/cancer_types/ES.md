---
name: Ewing Sarcoma
oncotree_code: ES
main_type: Bone Cancer
parent: BONE
tags:
  - sarcoma
  - bone-cancer
  - pediatric
processed_by: crosslinker
processed_at: 2026-05-21
---

# Ewing Sarcoma (ES)

## Overview

Ewing sarcoma is an aggressive small-round-cell sarcoma of bone and soft tissue, typically driven by `EWSR1::FLI1` (or related ETS-family) gene fusions. Most cases occur in children and young adults.

## Cohorts in the corpus

- [sarcoma_ucla_2024](../datasets/sarcoma_ucla_2024.md) — UCLA pediatric/adult sarcoma patient-derived tumor organoid (PDTO) biobank includes Ewing sarcoma specimens for organoid drug screening. [PMID:39305899](../papers/39305899.md)

## Recurrent alterations

- ES is characterized by recurrent EWSR1-rearrangements (canonical `EWSR1::FLI1` t(11;22)); secondary alterations involve [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), and [STAG2](../genes/STAG2.md).
- CCLE pharmacogenomic profiling included Ewing sarcoma cell lines among 947 lines tested across 24 drugs, enabling genotype-response correlation analyses [PMID:22460905](../papers/22460905.md)
- EWS::[FLI1](../genes/FLI1.md) expression in human embryonic mesenchymal stem cells (heMSCs) alone is sufficient to impose an ES-like transcriptome, directly upregulate [BRCA1](../genes/BRCA1.md) while impairing ATM/ATR-mediated DNA damage response, and generate metastatic Ewing-like tumors in NOD/SCID mice (40% penetrance), supporting heMSCs as the cell of origin. [PMID:25186949](../papers/25186949.md)
- WGS of 112 Ewing sarcoma tumors (extended to 299 patients) identified [STAG2](../genes/STAG2.md) (17%), [CDKN2A](../genes/CDKN2A.md) deletion (12%), [TP53](../genes/TP53.md) (7%), and epigenetic regulators EZH2/BCOR/ZMYM3 (2.7% each) as recurrently mutated; [STAG2](../genes/STAG2.md)+[TP53](../genes/TP53.md) co-mutation defined a high-risk subtype with markedly inferior survival [PMID:25223734](../papers/25223734.md)
- One odontogenic tumor harboring an EWSR1-FLI1 fusion in the MSK-IMPACT cohort (Morris et al.) was reclassified from 'ameloblastic carcinoma' to Ewing sarcoma with epithelial differentiation, illustrating that EWSR1-FLI1 fusions can occur in unusual anatomic sites and require histologic re-evaluation [PMID:27442865](../papers/27442865.md).
- PIPseq cohort identified EWSR1-FLI1 fusion as diagnostic in two Ewing sarcoma patients; one patient additionally showed low PAX8/FHIT/CASP10/CHD2 expression and high CHD11/FUS/MTA1 expression as a poor-prognosis transcriptomic signature; [APC](../genes/APC.md) V1822D VOUS also returned in one ES patient [PMID:28007021](../papers/28007021.md)
- [EWSR1](../genes/EWSR1.md)::[BEND2](../genes/BEND2.md) in-frame fusion sarcoma of the bladder initially diagnosed as extraskeletal Ewing sarcoma based on [CD99](../genes/CD99.md) positivity and [EWSR1](../genes/EWSR1.md) FISH; RNA-seq identified [BEND2](../genes/BEND2.md) (not an ETS family gene) as partner — reclassifying to EWSR1-non-ETS undifferentiated sarcoma per WHO 2020 [PMID:28199314](../papers/28199314.md)
- In the MSK-IMPACT pan-cancer cohort, EWSR1-FLI1 was detected in 25 Ewing sarcoma (ES) cases — the 4th most common rearrangement overall (after TMPRSS2-ERG n=151, EGFRvIII n=65, EML4-ALK n=38); ES was included among 62 principal tumor types in [msk_impact_2017](../datasets/msk_impact_2017.md). [PMID:28481359](../papers/28481359.md)
- ES (Ewing sarcoma) was used as a 3D model test bed; A673 spheroids in anchored-droplet microfluidic chips yielded IC50 measurements for [cisplatin](../drugs/cisplatin.md) + [etoposide](../drugs/etoposide.md) combinations consistent with 96-well plates, and synergy was greater when [etoposide](../drugs/etoposide.md) preceded [cisplatin](../drugs/cisplatin.md). [PMID:30643250](../papers/30643250.md)
- Ewing sarcoma PDX models in PPTC cohort: EWSR1-FLI1 fusion in all RNA-seq-profiled models; [TP53](../genes/TP53.md) mutations in 7/10 (70%); homozygous CDKN2A/B loss in 60% (mutually exclusive with [STAG2](../genes/STAG2.md) mutations 20%); CHLA-258 additionally harbored FLI1-RP11-9L18.2 [PMID:31693904](../papers/31693904.md).
- Ewing sarcoma (ES) was enrolled in the MAPPYACTS trial (sarcomas 37% of 787 patients); [EWSR1](../genes/EWSR1.md) fusions were covered in the sarcoma oncomap; 17% ORR with matched therapy (38% for ready-for-routine-use alterations) [PMID:35292802](../papers/35292802.md)
- Included in the MSK cWGTS pediatric/rare solid tumor cohort (n=114 patients, [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)); whole-genome + transcriptome sequencing added oncogenic findings beyond MSK-IMPACT in 54% of patients [PMID:35585047](../papers/35585047.md)
- In a 7,494-sarcoma cohort, Ewing sarcoma was among the translocation-associated histologies; EWSR1-FLI1 fusions were characteristic; [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), and STAG2 alterations carry prognostic weight [PMID:35705558](../papers/35705558.md).
- In the 2,138-sarcoma MSK-IMPACT cohort (n=99 ES), 10% harbored STAG2 mutations co-occurring with TP53 alterations; [DSRCT](../cancer_types/DSRCT.md) and ES had the lowest intra-subtype genomic entropy [PMID:35705560](../papers/35705560.md).

## Subtypes

- Conventional Ewing sarcoma ([EWSR1](../genes/EWSR1.md)::[FLI1](../genes/FLI1.md) / EWSR1::[ERG](../genes/ERG.md) fusions) is the dominant subtype; CIC-rearranged and BCOR-rearranged round-cell sarcomas are histologic mimics with distinct molecular drivers and are tracked separately under the round-cell-sarcoma family.

## Therapeutic landscape

- Backbone chemotherapy regimens combine [vincristine](../drugs/vincristine.md), [doxorubicin](../drugs/doxorubicin.md), [cyclophosphamide](../drugs/cyclophosphamide.md), [ifosfamide](../drugs/ifosfamide.md) (where present), and [etoposide](../drugs/etoposide.md) (VDC/IE). [PMID:39305899](../papers/39305899.md) tested PDTO sensitivity to multi-kinase inhibitors and DNA-damage agents.

## Sources

- [PMID:39305899](../papers/39305899.md) — UCLA sarcoma PDTO biobank with pharmacotyping across sarcoma subtypes including ES.

---

*Page last touched by entity-page-writer on 2026-05-01.*

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25186949](../papers/25186949.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27442865](../papers/27442865.md) — Morris et al. 2017 (JAMA Oncol). EWSR1-FLI1 fusion reclassified an odontogenic 'ameloblastic carcinoma' as Ewing sarcoma with epithelial differentiation.

- [PMID:28007021](../papers/28007021.md)
- [PMID:28199314](../papers/28199314.md) — Halava et al. 2025; EWSR1::[BEND2](../genes/BEND2.md) bladder sarcoma initially classified as extraskeletal ES; EWSR1-non-ETS reclassification by RNA-seq.

- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30643250](../papers/30643250.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705558](../papers/35705558.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
