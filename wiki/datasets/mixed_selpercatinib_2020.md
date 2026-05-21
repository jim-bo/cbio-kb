---
name: "RET-Altered Cancers — Selpercatinib (LIBRETTO-001, MSK 2020)"
studyId: mixed_selpercatinib_2020
institution: Memorial Sloan Kettering Cancer Center
size: 72
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-exome-seq
  - msk-access
panels:
  - IMPACT468
tags:
  - ret-fusion
  - ret-mutation
  - selpercatinib
  - acquired-resistance
  - cfDNA
  - lung-adenocarcinoma
  - medullary-thyroid-carcinoma
  - polyclonal-resistance
processed_by: crosslinker
processed_at: 2026-05-21
---

# RET-Altered Cancers — Selpercatinib (LIBRETTO-001, MSK 2020)

## Overview

`mixed_selpercatinib_2020` is a Memorial Sloan Kettering correlative-genomics dataset from 72 patients with [RET](../genes/RET.md) fusion- or mutation-positive lung and thyroid cancers enrolled on the registrational phase 1/2 LIBRETTO-001 trial (NCT03157128) and treated with the selective [RET](../genes/RET.md) inhibitor [selpercatinib](../drugs/selpercatinib.md). Multi-platform profiling included tissue [MSK-IMPACT](../methods/msk-impact-panel.md), whole-exome sequencing, and longitudinal plasma cfDNA via [MSK-ACCESS](../methods/msk-access.md). Data freeze: December 2019.

## Composition

- **n = 72** patients (70 included in correlative analyses); enrollment May 2017 – December 2019.
- **Cancer types:** [LUAD](../cancer_types/LUAD.md) (81% of fusion-positive cases), papillary thyroid carcinoma ([THPA](../cancer_types/THPA.md), 12%), medullary thyroid carcinoma ([THME](../cancer_types/THME.md)) (all RET-mutant cases), plus rare histologies ([LCNEC](../cancer_types/LCNEC.md), [LUAS](../cancer_types/LUAS.md), [HGNEC](../cancer_types/HGNEC.md), poorly differentiated thyroid).
- **[RET](../genes/RET.md) alteration types:** activating fusions (KIF5B-RET most common; also CCDC6-RET, NCOA4-RET, TAF3-RET, ERC1-RET, RBPMS-RET, CLIP1-RET) and kinase-domain mutations (germline and somatic, including M918T).
- **Prior therapy:** 19/72 received [selpercatinib](../drugs/selpercatinib.md) as first-line; 53 previously treated; 29/53 (55%) had prior multikinase inhibitor ([vandetanib](../drugs/vandetanib.md), [cabozantinib](../drugs/cabozantinib.md), RXDX-105).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — tumor tissue targeted sequencing up to 468 genes (n=51 pre-treatment + 9 post-progression matched pairs).
- [Whole-exome sequencing](../methods/whole-exome-seq.md) — on 44 pre-treatment tumors.
- [MSK-ACCESS](../methods/msk-access.md) — pre-treatment plasma cfDNA profiling (n=68); longitudinal cfDNA in 23 patients (18 sequenced post-progression).

## Papers using this cohort

- [PMID:35304457](../papers/35304457.md) — Rosen et al., *Cancer Discovery* 2022: Correlative genomics study of [selpercatinib](../drugs/selpercatinib.md) response and resistance; acquired resistance identified in 11/18 (61%) evaluable progressing patients via on-target RET solvent-front mutations or off-target MAPK bypass (KRAS/NRAS/BRAF/MET/FGFR1). [PMID:35304457](../papers/35304457.md)

## Notable findings derived from this cohort

- Selpercatinib ORR was 67% in RET fusion-positive and 58% in RET-mutant cancers (RECIST 1.1 per investigator); 82% of responders ongoing at 1 year; prior multikinase inhibitor exposure did not alter outcomes (HR=1.2, P=0.6) [PMID:35304457](../papers/35304457.md).
- Concurrent [TP53](../genes/TP53.md) mutations (n=8, all in fusion-positive cases) were associated with shorter median PFS (HR=3.5, 95% CI 1.3–9.7, P=0.016) [PMID:35304457](../papers/35304457.md).
- Pre-treatment plasma [MSK-ACCESS](../methods/msk-access.md) detected the qualifying RET alteration in 95% of RET-mutant cases and 74% of fusion-positive cases; low cfDNA shedders had superior PFS (HR=3.7, 95% CI 1.1–12.4, P=0.013) [PMID:35304457](../papers/35304457.md).
- Acquired resistance was identified in 11/18 evaluable progressors (61%): on-target via secondary RET solvent-front mutations (G810C/G810S, compound cis mutants) or off-target via [KRAS](../genes/KRAS.md)/[NRAS](../genes/NRAS.md)/[BRAF](../genes/BRAF.md) activating mutations or [MET](../genes/MET.md)/[FGFR1](../genes/FGFR1.md) amplifications; polyclonal resistance (co-occurring on-target + off-target) was common [PMID:35304457](../papers/35304457.md).
- Pre-existing PI3K pathway alterations (PTEN/PIK3CA mutations) did not preclude clinical benefit (CBR 91%) [PMID:35304457](../papers/35304457.md).

## Sources

- cBioPortal study `mixed_selpercatinib_2020`.
- LIBRETTO-001 clinical trial NCT03157128.
- Rosen EY, et al. *RET Inhibition in Novel RET-Rearranged Cancers outside the Lung and Thyroid.* Cancer Discov. 2022. [PMID:35304457](../papers/35304457.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
