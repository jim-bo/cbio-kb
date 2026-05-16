---
name: Therapy-Related Myeloid Neoplasms
oncotree_code: TMN
main_type: Leukemia
parent: AML
tags:
  - therapy-related
  - myeloid
  - clonal-hematopoiesis
  - TP53
processed_by: crosslinker
processed_at: 2026-05-16
---

# Therapy-Related Myeloid Neoplasms (TMN)

## Overview

Therapy-Related Myeloid Neoplasms (TMN) are [AML](../cancer_types/AML.md), [MDS](../cancer_types/MDS.md), or myelodysplastic/myeloproliferative neoplasms that arise as late complications of cytotoxic chemotherapy or radiation therapy. In OncoTree, TMN sits under AML (level 4, parent: AML), tissue: Myeloid. The corpus documents how clonal hematopoiesis (CH) — particularly CH in DNA-damage-response (DDR) genes — acts as a precursor to TMN following cancer therapy, with CH VAF >2% conferring HR=6.9 for subsequent TMN in a pooled cohort of 9,437 therapy-exposed cancer patients.

## Cohorts in the corpus

- [msk_ch_2020](../datasets/msk_ch_2020.md) — 24,146 solid-tumor cancer patients with paired tumor+blood MSK-IMPACT sequencing; 35 paired CH→TMN samples (median interval 24 months); pooled TMN risk cohort of 9,437 therapy-exposed patients with 75 TMN events. [PMID:33106634](../papers/33106634.md)

## Recurrent alterations

- In 19/32 (59%) paired CH→TMN cases, ≥1 leukemia-defining mutation was detectable at the pre-TMN CH timepoint; 13/32 (41%) harbored two or more TMN-defining mutations at CH stage. [PMID:33106634](../papers/33106634.md)
- TP53-mutant TMN: 14/35 (40%) of TMN cases carried [TP53](../genes/TP53.md); 10/14 detectable at the CH stage; 12/13 evaluable TP53-mutant TMN cases co-occurred with complex karyotype or isolated aneuploidy at transformation. [PMID:33106634](../papers/33106634.md)
- Late-progression drivers acquired between CH and TMN diagnosis: [FLT3](../genes/FLT3.md), [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md) (chromosomal aneuploidies in 91% of transformations). [PMID:33106634](../papers/33106634.md)
- Strongest gene-specific TMN predictors: TP53, [SRSF2](../genes/SRSF2.md), [U2AF1](../genes/U2AF1.md), [SF3B1](../genes/SF3B1.md) (spliceosome); CH VAF >2% HR=6.9 (p<10⁻⁶) rising with clone size and mutation number. [PMID:33106634](../papers/33106634.md)

## Subtypes

- **DDR-driven TMN** — TP53, [PPM1D](../genes/PPM1D.md), [CHEK2](../genes/CHEK2.md) CH mutations selectively expanded by platinum, topoisomerase II inhibitors, and external-beam radiation; represent the dominant therapy-selected CH pathway to TMN. [PMID:33106634](../papers/33106634.md)
- **Spliceosome-driven TMN** — SRSF2, SF3B1, U2AF1 CH mutations strongly age-associated; not enriched by therapy but among the strongest TMN risk predictors in pooled analysis. [PMID:33106634](../papers/33106634.md)

## Therapeutic landscape

- Pre-treatment CH screening (MSK-IMPACT-style panel) is proposed as a risk-stratification tool; patients with high-risk CH (DDR genes, high VAF, multiple mutations) may benefit from altered chemotherapy selection to minimize TMN risk. [PMID:33106634](../papers/33106634.md)
- Carboplatin, topoisomerase II inhibitors, and external-beam radiation drive the strongest DDR clonal selection; avoiding or substituting these agents may reduce TMN risk when clinically interchangeable alternatives exist. [PMID:33106634](../papers/33106634.md)

## Sources

- [PMID:33106634](../papers/33106634.md) — Bolton et al., clonal hematopoiesis and therapy-related myeloid neoplasm risk in 24,146 cancer patients (MSK-IMPACT CH cohort).

*This page was processed by **crosslinker** on **2026-05-16**.*
