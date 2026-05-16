---
name: Ewing Sarcoma
oncotree_code: ES
main_type: Bone Cancer
parent: BONE
tags:
  - sarcoma
  - bone-cancer
  - pediatric
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Ewing Sarcoma (ES)

## Overview

Ewing sarcoma is an aggressive small-round-cell sarcoma of bone and soft tissue, typically driven by `EWSR1::FLI1` (or related ETS-family) gene fusions. Most cases occur in children and young adults.

## Cohorts in the corpus

- [sarcoma_ucla_2024](../datasets/sarcoma_ucla_2024.md) — UCLA pediatric/adult sarcoma patient-derived tumor organoid (PDTO) biobank includes Ewing sarcoma specimens for organoid drug screening. [PMID:39305899](../papers/39305899.md)

## Recurrent alterations

- ES is characterized by recurrent EWSR1-rearrangements (canonical `EWSR1::FLI1` t(11;22)); secondary alterations involve [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), and STAG2.
- CCLE pharmacogenomic profiling included Ewing sarcoma cell lines among 947 lines tested across 24 drugs, enabling genotype-response correlation analyses [PMID:22460905](../papers/22460905.md)
- EWS::FLI1 expression in human embryonic mesenchymal stem cells (heMSCs) alone is sufficient to impose an ES-like transcriptome, directly upregulate [BRCA1](../genes/BRCA1.md) while impairing ATM/ATR-mediated DNA damage response, and generate metastatic Ewing-like tumors in NOD/SCID mice (40% penetrance), supporting heMSCs as the cell of origin. [PMID:25186949](../papers/25186949.md)
- WGS of 112 Ewing sarcoma tumors (extended to 299 patients) identified STAG2 (17%), CDKN2A deletion (12%), TP53 (7%), and epigenetic regulators EZH2/BCOR/ZMYM3 (2.7% each) as recurrently mutated; STAG2+TP53 co-mutation defined a high-risk subtype with markedly inferior survival [PMID:25223734](../papers/25223734.md)
- One odontogenic tumor harboring an EWSR1-FLI1 fusion in the MSK-IMPACT cohort (Morris et al.) was reclassified from 'ameloblastic carcinoma' to Ewing sarcoma with epithelial differentiation, illustrating that EWSR1-FLI1 fusions can occur in unusual anatomic sites and require histologic re-evaluation [PMID:27442865](../papers/27442865.md).
- PIPseq cohort identified EWSR1-FLI1 fusion as diagnostic in two Ewing sarcoma patients; one patient additionally showed low PAX8/FHIT/CASP10/CHD2 expression and high CHD11/FUS/MTA1 expression as a poor-prognosis transcriptomic signature; APC V1822D VOUS also returned in one ES patient [PMID:28007021](../papers/28007021.md)
- EWSR1::BEND2 in-frame fusion sarcoma of the bladder initially diagnosed as extraskeletal Ewing sarcoma based on CD99 positivity and EWSR1 FISH; RNA-seq identified BEND2 (not an ETS family gene) as partner — reclassifying to EWSR1-non-ETS undifferentiated sarcoma per WHO 2020 [PMID:28199314](../papers/28199314.md)
- In the MSK-IMPACT pan-cancer cohort, EWSR1-FLI1 was detected in 25 Ewing sarcoma (ES) cases — the 4th most common rearrangement overall (after TMPRSS2-ERG n=151, EGFRvIII n=65, EML4-ALK n=38); ES was included among 62 principal tumor types in msk_impact_2017. [PMID:28481359](../papers/28481359.md)
- ES (Ewing sarcoma) was used as a 3D model test bed; A673 spheroids in anchored-droplet microfluidic chips yielded IC50 measurements for cisplatin + etoposide combinations consistent with 96-well plates, and synergy was greater when etoposide preceded cisplatin. [PMID:30643250](../papers/30643250.md)
- Ewing sarcoma PDX models in PPTC cohort: EWSR1-FLI1 fusion in all RNA-seq-profiled models; TP53 mutations in 7/10 (70%); homozygous CDKN2A/B loss in 60% (mutually exclusive with STAG2 mutations 20%); CHLA-258 additionally harbored FLI1-RP11-9L18.2 [PMID:31693904](../papers/31693904.md).

## Subtypes

- Conventional Ewing sarcoma (EWSR1::FLI1 / EWSR1::[ERG](../genes/ERG.md) fusions) is the dominant subtype; CIC-rearranged and BCOR-rearranged round-cell sarcomas are histologic mimics with distinct molecular drivers and are tracked separately under the round-cell-sarcoma family.

## Therapeutic landscape

- Backbone chemotherapy regimens combine [vincristine](../drugs/vincristine.md), [doxorubicin](../drugs/doxorubicin.md), [cyclophosphamide](../drugs/cyclophosphamide.md), ifosfamide (where present), and [etoposide](../drugs/etoposide.md) (VDC/IE). [PMID:39305899](../papers/39305899.md) tested PDTO sensitivity to multi-kinase inhibitors and DNA-damage agents.

## Sources

- [PMID:39305899](../papers/39305899.md) — UCLA sarcoma PDTO biobank with pharmacotyping across sarcoma subtypes including ES.

---

*Page last touched by entity-page-writer on 2026-05-01.*

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:25186949](../papers/25186949.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **wiki-cli** on **2026-05-12**.*
- [PMID:27442865](../papers/27442865.md) — Morris et al. 2017 (JAMA Oncol). EWSR1-FLI1 fusion reclassified an odontogenic 'ameloblastic carcinoma' as Ewing sarcoma with epithelial differentiation.

- [PMID:28007021](../papers/28007021.md)
- [PMID:28199314](../papers/28199314.md) — Halava et al. 2025; EWSR1::BEND2 bladder sarcoma initially classified as extraskeletal ES; EWSR1-non-ETS reclassification by RNA-seq.

- [PMID:28481359](../papers/28481359.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:30643250](../papers/30643250.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
