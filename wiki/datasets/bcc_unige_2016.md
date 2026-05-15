---
name: NB-UVB Phototherapy Mutation Burden Cohort (Fowler et al. 2025)
studyId: bcc_unige_2016
institution: University of Southampton / NHS dermatology centre (UK)
size: 16
reference_genome: hg38
canonical_source: corpus
unverified: true
assays:
  - nanoseq
  - whole-genome-seq
panels: []
tags:
  - psoriasis
  - NB-UVB
  - phototherapy
  - mutation-burden
  - mutational-signatures
  - SBS7
  - skin-cancer-surveillance
  - keratinocyte-cancer
  - UV-mutagenesis
  - EGA
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# NB-UVB Phototherapy Mutation Burden Cohort (Fowler et al. 2025)

## Overview

Cohort of 16 patients with psoriasis recruited at a single UK dermatology centre providing paired pre- and post-treatment skin biopsies to quantify somatic mutation burden induced by a single course of narrowband ultraviolet B (NB-UVB) phototherapy. Profiled by NanoSeq (nanorate duplex sequencing) on epidermal DNA microdissected from 6-mm punch biopsies of buttock (infrequently sun-exposed) and dorsal forearm (frequently sun-exposed) skin.

**Note:** This dataset is registered under the studyId `bcc_unige_2016` in the wiki ontology but is **not hosted on cBioPortal**. Sequencing data are deposited at the European Genome-Phenome Archive (EGA): whole-genome data under EGAD0000101525 and NanoSeq data under EGAD00001015249; HaCaT keratinocyte ancillary data at ENA accession ERP156525. [PMID:26950094](../papers/26950094.md)

## Composition

- 21 patients with psoriasis recruited; 16 provided paired pre/post NB-UVB biopsies (6 women, 10 men; median age 33, range 20–73).
- UK census ethnicity: 13 White British, 1 White Irish, 1 Asian Indian, 1 Asian other.
- 6-mm punch biopsies from buttock (infrequently sun-exposed, n=14 paired) and dorsal forearm (frequently sun-exposed, n=10 paired); venous blood used as germline reference.
- NB-UVB delivered at 311 nm; 14–35 exposures (median 28); total course dose 84–756 SED (median 219); MED 1.7–5.1 SED (median 2.9).
- Epidermal DNA isolated by microdissection; ~one-third of the genome covered per NanoSeq library — sufficient for mutation-burden / signature analysis but not for driver-gene calling.
- Ancillary in vitro: HaCaT keratinocytes treated with 8-methoxypsoralen ([methoxsalen](../drugs/methoxsalen.md)) plus UVA, then re-sequenced with NanoSeq to validate a PUVA-associated signature. [PMID:26950094](../papers/26950094.md)

## Assays / panels (linked)

- [nanoseq](../methods/nanoseq.md) — duplex sequencing with error rate <5 per billion bp; ~one-third-genome coverage per sample (paired pre/post NB-UVB biopsies).
- [whole-genome-seq](../methods/whole-genome-seq.md) — whole-genome NanoSeq libraries (EGA EGAD0000101525).

## Papers using this cohort

- [PMID:26950094](../papers/26950094.md) — Fowler et al., *Br J Dermatol* 2025: primary study quantifying NB-UVB-induced mutation burden in normal skin and modelling skin-cancer surveillance thresholds.

## Notable findings derived from this cohort

- Single NB-UVB course raised median mutation burden in buttock skin from 0.52 to 1.09 substitutions/Mb (P < 0.001) and in forearm skin from 3.13 to 3.77 substitutions/Mb (P = 0.01) [PMID:26950094](../papers/26950094.md).
- Dose-normalised burden (Δ-mutation burden/dose): median 0.0021 substitutions/Mb/SED (buttock) and 0.0034 (forearm); UVR-associated COSMIC signatures SBS7a/SBS7b appeared in all post-NB-UVB samples [PMID:26950094](../papers/26950094.md).
- Prior phototherapy elevated baseline mutation burden (P = 0.01), indicating induced mutations persist across decades [PMID:26950094](../papers/26950094.md).
- Asian patients had lower Δ-mutation burden/dose (median 0.0003 substitutions/Mb/SED), correlated with polygenic tan-propensity scores [PMID:26950094](../papers/26950094.md).
- Surveillance modelling (for MED = 2 SED): cancer surveillance should begin after 422 (cautious), 165 (typical), or 58 (enthusiastic sun-exposure) NB-UVB exposures — far below the current BAD/BPG 500-exposure guideline threshold [PMID:26950094](../papers/26950094.md).

## Sources

- **Not on cBioPortal.** Data deposited at:
  - EGA (whole-genome): EGAD0000101525
  - EGA (NanoSeq): EGAD00001015249
  - ENA (HaCaT ancillary data): ERP156525
- [PMID:26950094](../papers/26950094.md) — Fowler JC et al., "Mutation burden of narrowband ultraviolet B phototherapy (NB-UVB) in human skin: relevance to NB-UVB lifetime exposures and skin cancer surveillance." *Br J Dermatol* 2025.

*This page was processed by **entity-page-writer** on **2026-05-15**.*
