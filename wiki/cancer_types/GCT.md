---
name: Germ Cell Tumor
oncotree_code: GCT
main_type: Germ Cell Tumor
parent: TESTIS
tags: [germ-cell, cisplatin, rare-cancers]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Germ Cell Tumor (GCT)

## Overview

Germ Cell Tumor is an umbrella OncoTree designation for testicular and extragonadal germ cell tumors. Note: in the OncoTree hierarchy, GCT canonically maps to "Granular Cell Tumor" in the Sellar Tumor branch; within the cBioPortal study [gct_msk_2016](../datasets/gct_msk_2016.md) the code is used specifically for testicular and mediastinal germ cell tumors. The corpus usage refers to [NSGCT](../cancer_types/NSGCT.md) (non-seminomatous GCT) and [SEM](../cancer_types/SEM.md) (seminoma) as the principal histologic subtypes, with primary sites including testis ([TT](../cancer_types/TT.md)), mediastinum, and retroperitoneum.

## Cohorts in the corpus

- [gct_msk_2016](../datasets/gct_msk_2016.md) — N=180 men with advanced GCT receiving first-line cisplatin-based chemotherapy at Memorial Sloan Kettering Cancer Center; 19 tumors by whole-exome sequencing (discovery) + 161 by MSK-IMPACT targeted sequencing (validation); 76 cisplatin-sensitive vs 104 resistant [PMID:27646943](../papers/27646943.md).

## Recurrent alterations

- **12p gain** — present in 74% of discovery tumors; the well-characterized GCT cytogenetic hallmark [PMID:27646943](../papers/27646943.md).
- **[TP53](../genes/TP53.md)** — alterations exclusive to cisplatin-resistant tumors (17/104 [16.3%] resistant vs 0/76 sensitive, P<.001); 72% of primary mediastinal nonseminomas harbored [TP53](../genes/TP53.md) alterations; strongest single-gene biomarker of [cisplatin](../drugs/cisplatin.md) resistance [PMID:27646943](../papers/27646943.md).
- **[MDM2](../genes/MDM2.md)** — amplifications in 7.6% of resistant vs 2.6% sensitive tumors; mutually exclusive with [TP53](../genes/TP53.md) alteration; combined TP53/MDM2 alterations in 24.0% of resistant vs 2.6% sensitive (P<.001) [PMID:27646943](../papers/27646943.md).
- **[MYCN](../genes/MYCN.md)** — amplifications in 5 patients, all [cisplatin](../drugs/cisplatin.md) resistant; transcriptionally targets both TP53 and [MDM2](../genes/MDM2.md) [PMID:27646943](../papers/27646943.md).
- **[RAC1](../genes/RAC1.md)** — novel hotspot mutations at codons 12, 34, 61 (G12V/R, P34R, Q61R/K) in 9 patients (5% — highest reported across TCGA cancer types at time of publication); functionally validated to activate [PAK1](../genes/PAK1.md) and MEK1/2 phosphorylation [PMID:27646943](../papers/27646943.md).
- **[KIT](../genes/KIT.md)** — exon 17 hotspot mutations in 19 patients; enriched in [SEM](../cancer_types/SEM.md) (29.6% vs 4% in nonseminoma, P<.001) [PMID:27646943](../papers/27646943.md).
- **[KRAS](../genes/KRAS.md)** — 22 patients (G12 dominant); enriched in seminomas overall (20% vs 8.7%, P=.045) [PMID:27646943](../papers/27646943.md).
- **PI3K pathway** — alterations in 13.3% ([PIK3CA](../genes/PIK3CA.md) E542K ×4, [PTEN](../genes/PTEN.md) LOF ×5, [AKT1](../genes/AKT1.md) amplification, [MTOR](../genes/MTOR.md), [TSC1](../genes/TSC1.md), [TSC2](../genes/TSC2.md)) [PMID:27646943](../papers/27646943.md).
- **Mean MSK-IMPACT mutation rate of 0.9/Mb** — very low compared with other adult solid tumors [PMID:27646943](../papers/27646943.md).
- Included in the MSK cWGTS pediatric/rare solid tumor cohort (n=114 patients, [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)); whole-genome + transcriptome sequencing added oncogenic findings beyond MSK-IMPACT in 54% of patients [PMID:35585047](../papers/35585047.md)

## Subtypes

- **[NSGCT](../cancer_types/NSGCT.md)** — non-seminomatous GCT; 70% of the cohort (n=126); lower [KIT](../genes/KIT.md) mutation rate (4%) than seminoma; [KRAS](../genes/KRAS.md) mutations in nonseminomas enriched in cisplatin-resistant tumors [PMID:27646943](../papers/27646943.md).
- **[SEM](../cancer_types/SEM.md)** — seminoma; 30% of cohort (n=54); high [KIT](../genes/KIT.md) mutation rate (29.6%); enriched [KRAS](../genes/KRAS.md) [PMID:27646943](../papers/27646943.md).
- **[MGCT](../cancer_types/MGCT.md)** — mixed GCT (teratoma-containing); 49 resistant samples [PMID:27646943](../papers/27646943.md).
- **Primary mediastinal nonseminoma** — uniquely poor prognosis; 72% TP53 alteration rate vs 2.5% in testicular primaries (P<.001); provides molecular basis for IGCCCG poor-risk designation [PMID:27646943](../papers/27646943.md).

## Therapeutic landscape

- **[Cisplatin](../drugs/cisplatin.md)-based chemotherapy** ([BEP](../drugs/bleomycin.md)/[EP](../drugs/etoposide.md)/TIP/VIP) — standard first-line; cisplatin resistance is the central clinical challenge; TP53/MDM2 alterations independently predict shorter PFS (HR 1.83, P=.016) after adjusting for IGCCCG risk [PMID:27646943](../papers/27646943.md).
- **[Nutlin-3](../drugs/nutlin-3.md) ([MDM2](../genes/MDM2.md) inhibitor)** — showed antiproliferative and apoptotic synergy with cisplatin in TP53 wild-type cisplatin-resistant cell lines in vitro; 7 MDM2 inhibitors in clinical trials at time of publication [PMID:27646943](../papers/27646943.md).
- **[Imatinib](../drugs/imatinib.md)/[sunitinib](../drugs/sunitinib.md)** — therapeutic candidates for KIT-mutant GCT (particularly seminoma) [PMID:27646943](../papers/27646943.md).
- **MEK inhibitors ([trametinib](../drugs/trametinib.md), [selumetinib](../drugs/selumetinib.md), [binimetinib](../drugs/binimetinib.md))** — candidates for KRAS/NRAS/RAC1-altered GCT [PMID:27646943](../papers/27646943.md).

## Sources

- [PMID:27646943](../papers/27646943.md) — Bagrodia et al. 2016 (JCO). Whole-exome + MSK-IMPACT sequencing of 180 advanced GCT; TP53/MDM2 alterations exclusive to cisplatin-resistant tumors; novel [RAC1](../genes/RAC1.md) hotspot mutations.

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
