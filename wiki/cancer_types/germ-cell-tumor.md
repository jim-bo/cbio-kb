---
name: Germ Cell Tumor (corpus umbrella)
oncotree_code: germ-cell-tumor
main_type: Germ Cell Tumor
parent:
tags:
  - corpus-umbrella
  - germ-cell
  - cisplatin
  - unverified
unverified: true
canonical_source: corpus
processed_by: orchestrator
processed_at: 2026-09-11
---

# Germ Cell Tumor (germ-cell-tumor)

> **Note:** `germ-cell-tumor` is a corpus umbrella slug, not an OncoTree code. OncoTree has a "Germ Cell Tumor" main type but no code for it; its germ cell codes are split by site. Link here when a paper reports germ cell tumors without a site or histology, and link the specific code when it gives one. The OncoTree code `GCT` is [Granular Cell Tumor](GCT.md), a sellar tumor, not germ cell tumor.

## Overview

Germ cell tumors arise from primordial germ cells, most often in the testis or ovary and less often at midline extragonadal sites (mediastinum, retroperitoneum, brain). OncoTree files them under their site:

| Site | OncoTree code | Children | Wiki page |
| :-- | :-- | :-- | :-- |
| Testis | `NSGCT`, `SEM` | NSGCT: `EMBCA`, `TYST`, `TCCA`, `TT`, `MGCT`, `GCTSTM` | [NSGCT](NSGCT.md), [SEM](SEM.md), [TT](TT.md), [TYST](TYST.md), [MGCT](MGCT.md) |
| Ovary | `OGCT` | `ODYS`, `OYST`, `OEC`, `OIMT`, `OMT`, `OPE`, `OMGCT` | [OGCT](OGCT.md) |
| Extragonadal (mediastinum, retroperitoneum) | `EGCT` | none | none yet |
| Brain | `BGCT` | `GMN`, `BYST`, `BEC`, `BCCA`, `BIMT`, `BMT`, `BMGT`, `BMGCT` | none yet |
| Vulva | `VGCT` | `VDYS`, `VYST`, `VOEC`, `VIMT`, `VMT`, `VPE`, `VMGCT` | none yet |

Two abbreviations collide with OncoTree codes. Papers write "GCT" for germ cell tumor, but OncoTree `GCT` is Granular Cell Tumor. TCGA writes "TGCT" for testicular germ cell tumors, but OncoTree `TGCT` is Tenosynovial Giant Cell Tumor, Diffuse Type; the TCGA cohort is covered on the [TGCT](TGCT.md) corpus page. Some cBioPortal studies also use `GCT` for germ cell tumor samples: [pancan_pdx_uthsa_2023](../datasets/pancan_pdx_uthsa_2023.md) labels 12 samples `GCT` (and 4 `OGCT`). Read that as the study's own label, not the OncoTree meaning. The two MSK germ cell studies code by histology instead: [gct_msk_2016](../datasets/gct_msk_2016.md) uses `NSGCT`/`SEM` and [gct_msk_2020](../datasets/gct_msk_2020.md) uses `NSGCT`, including for mediastinal primaries that OncoTree's site-based tree would place under `EGCT`.

## Cohorts in the corpus

- [gct_msk_2016](../datasets/gct_msk_2016.md) — N=180 men with advanced germ cell tumors receiving first-line cisplatin-based chemotherapy at Memorial Sloan Kettering Cancer Center; 19 tumors by whole-exome sequencing (discovery) + 161 by MSK-IMPACT targeted sequencing (validation); 76 cisplatin-sensitive vs 104 resistant; primary sites 87.2% testis, 12.2% mediastinum, 0.6% retroperitoneum [PMID:27646943](../papers/27646943.md).
- [gct_msk_2020](../datasets/gct_msk_2020.md) — 15 men with primary mediastinal nonseminoma and a concomitant hematologic malignancy; see [NSGCT](NSGCT.md) for the findings [PMID:32897884](../papers/32897884.md).
- [makeanimpact_ccr_2023](../datasets/makeanimpact_ccr_2023.md) — the Make-an-IMPACT outreach program profiled 83 female germ cell tumor patients with MSK-IMPACT (67 ovarian primaries, 16 extragonadal; findings on [OGCT](OGCT.md)) and 54 male germ cell tumor patients, whose tumors the paper does not subtype [PMID:36862133](../papers/36862133.md).
- [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) — 4 germ cell tumors in the MSK whole-genome and transcriptome (cWGTS) cohort of 114 pediatric and rare solid tumor patients; the study codes them `TYST`, `BIMT`, `OMGCT`, and `TT` [PMID:35585047](../papers/35585047.md).
- [pancan_pdx_uthsa_2023](../datasets/pancan_pdx_uthsa_2023.md) — 10 germ cell tumors among 68 pediatric solid tumor PDX models from 65 patients across 16 cancer types [PMID:37990009](../papers/37990009.md).
- [msk_impact_50k_2026](../datasets/msk_impact_50k_2026.md) — germ cell tumors are among the 448 OncoTree histologies in the MSK-50K cohort [PMID:41895280](../papers/41895280.md).
- TCGA testicular germ cell tumors — see [TGCT](TGCT.md).

## Recurrent alterations

- **12p gain** — present in 74% of discovery tumors; the well-characterized germ cell tumor cytogenetic hallmark [PMID:27646943](../papers/27646943.md).
- **[TP53](../genes/TP53.md)** — alterations exclusive to cisplatin-resistant tumors (17/104 [16.3%] resistant vs 0/76 sensitive, P<.001); 72% of primary mediastinal nonseminomas harbored [TP53](../genes/TP53.md) alterations; strongest single-gene biomarker of [cisplatin](../drugs/cisplatin.md) resistance [PMID:27646943](../papers/27646943.md).
- **[MDM2](../genes/MDM2.md)** — amplifications in 7.6% of resistant vs 2.6% sensitive tumors; mutually exclusive with [TP53](../genes/TP53.md) alteration; combined TP53/MDM2 alterations in 24.0% of resistant vs 2.6% sensitive (P<.001) [PMID:27646943](../papers/27646943.md).
- **[MYCN](../genes/MYCN.md)** — amplifications in 5 patients, all [cisplatin](../drugs/cisplatin.md) resistant; transcriptionally targets both [TP53](../genes/TP53.md) and [MDM2](../genes/MDM2.md) [PMID:27646943](../papers/27646943.md).
- **[RAC1](../genes/RAC1.md)** — novel hotspot mutations at codons 12, 34, 61 (G12V/R, P34R, Q61R/K) in 9 patients (5% — highest reported across TCGA cancer types at time of publication); functionally validated to activate [PAK1](../genes/PAK1.md) and MEK1/2 phosphorylation [PMID:27646943](../papers/27646943.md).
- **[KIT](../genes/KIT.md)** — exon 17 hotspot mutations in 19 patients; enriched in [SEM](SEM.md) (29.6% vs 4% in nonseminoma, P<.001) [PMID:27646943](../papers/27646943.md).
- **[KRAS](../genes/KRAS.md)** — 22 patients (G12 dominant); enriched in seminomas overall (20% vs 8.7%, P=.045) [PMID:27646943](../papers/27646943.md).
- **PI3K pathway** — alterations in 13.3% ([PIK3CA](../genes/PIK3CA.md) E542K ×4, [PTEN](../genes/PTEN.md) LOF ×5, [AKT1](../genes/AKT1.md) amplification, [MTOR](../genes/MTOR.md), [TSC1](../genes/TSC1.md), [TSC2](../genes/TSC2.md)) [PMID:27646943](../papers/27646943.md).
- **Low mutation burden** — mean MSK-IMPACT mutation rate of 0.9/Mb, very low compared with other adult solid tumors [PMID:27646943](../papers/27646943.md).
- **[RRAS2](../genes/RRAS2.md)** — 70% of RRAS2 hotspot mutations (104/147) in the MSK-50K cohort were in endometrial and germ cell tumors; in germ cell tumors every oncogenic RRAS2 mutation was at the new G23 or G24 hotspots (n=22), paralogous to RAS G12/G13 [PMID:41895280](../papers/41895280.md).
- **Chromothripsis** — detected in 2 of 4 germ cell tumors in the cWGTS cohort; one immature teratoma patient carried a pathogenic germline [PMS2](../genes/PMS2.md) mutation (c.538-1G>C) [PMID:35585047](../papers/35585047.md).
- **[LRPAP1](../genes/LRPAP1.md)–[PDGFRA](../genes/PDGFRA.md) fusion** — found in one germ cell tumor PDX (and one glioblastoma); the fusion keeps the PDGFRA kinase domain and goes with high PDGFRA expression. Germ cell tumors also had the longest telomeres of the cancer types in that PDX resource [PMID:37990009](../papers/37990009.md).

## Subtypes

- **[NSGCT](NSGCT.md)** — non-seminomatous germ cell tumor; 70% of the gct_msk_2016 cohort (n=126); lower [KIT](../genes/KIT.md) mutation rate (4%) than seminoma; [KRAS](../genes/KRAS.md) mutations in nonseminomas enriched in cisplatin-resistant tumors [PMID:27646943](../papers/27646943.md).
- **[SEM](SEM.md)** — seminoma; 30% of the gct_msk_2016 cohort (n=54); high [KIT](../genes/KIT.md) mutation rate (29.6%); enriched [KRAS](../genes/KRAS.md) [PMID:27646943](../papers/27646943.md).
- **[MGCT](MGCT.md)** — mixed germ cell tumor; 49 resistant samples were mixed tumors containing teratoma [PMID:27646943](../papers/27646943.md).
- **Primary mediastinal nonseminoma** — uniquely poor prognosis; 72% [TP53](../genes/TP53.md) alteration rate vs 2.5% in testicular primaries (P<.001); provides molecular basis for IGCCCG poor-risk designation [PMID:27646943](../papers/27646943.md). OncoTree's site code for mediastinal primaries is `EGCT`; both MSK studies code them `NSGCT`.
- **[OGCT](OGCT.md)** — ovarian and other female germ cell tumors from Make-an-IMPACT, including a near-haploid genomic subtype [PMID:36862133](../papers/36862133.md).

## Therapeutic landscape

- **[Cisplatin](../drugs/cisplatin.md)-based chemotherapy** — BEP ([bleomycin](../drugs/bleomycin.md), [etoposide](../drugs/etoposide.md), cisplatin), EP, TIP, and VIP; standard first-line, with cisplatin resistance the central clinical challenge. TP53/MDM2 alterations independently predict shorter PFS (HR 1.83, P=.016) after adjusting for IGCCCG risk [PMID:27646943](../papers/27646943.md).
- **[Nutlin-3](../drugs/nutlin-3.md) ([MDM2](../genes/MDM2.md) inhibitor)** — showed antiproliferative and apoptotic synergy with [cisplatin](../drugs/cisplatin.md) in [TP53](../genes/TP53.md) wild-type cisplatin-resistant cell lines in vitro; 7 [MDM2](../genes/MDM2.md) inhibitors in clinical trials at time of publication [PMID:27646943](../papers/27646943.md).
- **[Imatinib](../drugs/imatinib.md)/[sunitinib](../drugs/sunitinib.md)** — therapeutic candidates for KIT-mutant germ cell tumors (particularly seminoma) [PMID:27646943](../papers/27646943.md).
- **MEK inhibitors ([trametinib](../drugs/trametinib.md), [selumetinib](../drugs/selumetinib.md), [binimetinib](../drugs/binimetinib.md))** — candidates for KRAS/NRAS/RAC1-altered germ cell tumors [PMID:27646943](../papers/27646943.md).

## Sources

- [PMID:27646943](../papers/27646943.md) — Bagrodia et al. 2016 (JCO). Whole-exome + MSK-IMPACT sequencing of 180 advanced germ cell tumors; TP53/MDM2 alterations exclusive to cisplatin-resistant tumors; novel [RAC1](../genes/RAC1.md) hotspot mutations.
- [PMID:32897884](../papers/32897884.md) — Taylor et al. 2020 (JCI). Primary mediastinal nonseminomas and clonally related hematologic malignancies.
- [PMID:35585047](../papers/35585047.md) — MSK cWGTS of pediatric and rare solid tumors.
- [PMID:36862133](../papers/36862133.md) — Make-an-IMPACT direct-to-patient rare cancer profiling.
- [PMID:37990009](../papers/37990009.md) — Pediatric solid tumor PDX resource.
- [PMID:41895280](../papers/41895280.md) — Bandlamudi et al. MSK-50K driver atlas.

*This page was processed by **orchestrator** on **2026-09-11**.*
