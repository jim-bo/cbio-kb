---
name: Diffuse Glioma
oncotree_code: DIFG
main_type: Glioma
parent: GLIOMA
tags: [glioma, cns]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Diffuse Glioma (DIFG)

## Overview

OncoTree parent for adult diffuse gliomas, including IDH-mutant astrocytoma ([ASTR](ASTR.md)) and oligodendroglioma ([ODG](ODG.md)).

## Cohorts in the corpus

- [difg_msk_2023](../datasets/difg_msk_2023.md) — 128 adult patients at MSKCC with WHO 2016 Grade 2 IDH-mutant astrocytoma or oligodendroglioma on active surveillance; 73/128 profiled by MSK-IMPACT [PMID:37910594](../papers/37910594.md).
- [csf_msk_2024](../datasets/csf_msk_2024.md) — Gliomas were the third most common tumor type in the MSK CSF ctDNA cohort (n=148 patients), including diffuse gliomas profiled by MSK-IMPACT on CSF samples [PMID:39289779](../papers/39289779.md).
- Bakas 2017 published expert MRI segmentations and radiomic features for the TCGA-LGG collection (IDH-mutant lower-grade gliomas, a subset of diffuse gliomas), providing multiparametric MRI with manually delineated tumor sub-region labels and extracted radiomic features alongside the TCGA-GBM dataset [PMID:28872634](../papers/28872634.md).

## Recurrent alterations

- [IDH1](../genes/IDH1.md)/IDH2 mutation required for cohort inclusion; verified by IHC (93.8%) and/or NGS (57%) [PMID:37910594](../papers/37910594.md).
- [CDKN2A](../genes/CDKN2A.md)/B homozygous deletion defines "molecular grade-high" IDH-mt glioma (WHO 2021 Grade 4 astrocytoma) and drove ~2× faster tumor-volume growth rate (19.17% vs 9.54% per 6 months) [PMID:37910594](../papers/37910594.md).
- Focal amplifications of [MYCN](../genes/MYCN.md), [CDK4](../genes/CDK4.md), [PDGFRA](../genes/PDGFRA.md) defined "molecular grade-intermediate" in 1p19q intact tumors [PMID:37910594](../papers/37910594.md).
- [IDH1](../genes/IDH1.md) p.R132H detected in CSF ctDNA from IDH-mutant gliomas [PMID:39289779](../papers/39289779.md).
- [H3-3A](../genes/H3-3A.md) p.K28M histone mutation supporting diagnosis of diffuse midline glioma detected in CSF ctDNA [PMID:39289779](../papers/39289779.md).
- [BRAF](../genes/BRAF.md)::[KIAA1549](../genes/KIAA1549.md) fusions detected in CSF ctDNA from gliomas [PMID:39289779](../papers/39289779.md).
- Temozolomide mutational signatures identified in CSF ctDNA from glioma samples among high-TMB cases [PMID:39289779](../papers/39289779.md).
- Exome sequencing of 23 paired initial/recurrent grade II diffuse gliomas showed pervasive early clonal branching; [IDH1](../genes/IDH1.md) R132H was the only mutation shared in every patient pair, confirming it as the initiating event in low-grade gliomagenesis [PMID:24336570](../papers/24336570.md).
- TCGA pan-glioma study (n=1,122 grade II-IV diffuse gliomas) identified 75 significantly mutated genes including novel drivers SETD2, ARID2, DNMT3A, KRAS, NRAS; six methylation subclusters (LGm1–6) provide an independent prognostic classification on top of age and grade [PMID:26824661](../papers/26824661.md)
- PIPseq cohort included diffuse intrinsic pontine glioma cases; H3-3A (H3F3A) K27M mutation identified as HDAC-inhibitor target; paired with FGFR1 N577K in one patient [PMID:28007021](../papers/28007021.md)
- Included in pan-cancer pathway analysis of 9,125 TCGA tumors; IDH-mutant LGG/DIFG shows 82% RTK-RAS alteration rate in IDHwt subtype; IDH+PI3K inhibitor combination actionable in 14% of IDH-mutant LGG [PMID:29625050](../papers/29625050.md)
- DIFG (glioma) was the clearest exception to the pan-cancer TMB–OS benefit: high TMB was not associated with improved overall survival in glioma patients treated with ICI, possibly due to temozolomide-induced subclonal mutations or CNS-specific immune biology. [PMID:30643254](../papers/30643254.md)
- In 85 adult DIFG patients profiled by MSK-IMPACT CSF liquid biopsy, ctDNA was detected in 42/85 (49.4%) CSFs; positivity carried HR 4.16 (95% CI 2.15–8.05, p=2.43×10⁻⁵) for death and was concordant with truncal IDH1/TP53/ATRX/TERT/1p19q alterations in 100% of non-hypermutated cases. [PMID:30675060](../papers/30675060.md)
- MSK prospective glioma cohort (923 patients / 1,004 tumors); 13% germline pathogenic-variant rate (DNA-repair-enriched); CDKN2A/B cell-cycle alterations are IDH-independent drivers of malignant progression (HR=2.6 at recurrence); alkylator-induced hypermutation more common in IDH-mutant (29% vs 12%, P=0.004) and MGMT-methylated (30% vs 10%, P=0.006) tumors [PMID:31263031](../papers/31263031.md).
- DIFG/DMG PDX models in the PPTC cohort included histone H3-wild-type DIPG (n=2); both DIPG models expressed H3.3 at high levels (FPKM >50) but lacked canonical H3.1/H3.3 mutations [PMID:31693904](../papers/31693904.md).
- GLASS Consortium analyzed 222 adult diffuse glioma patients (IDHmut-codel n=25, IDHmut-noncodel n=63, IDHwt n=134) with paired initial/recurrence sequencing; driver genes (IDH1, TP53, ATRX, TERT promoter, chr7 gain/10 loss, EGFR amplification) were almost universally retained at recurrence; subclonal selection at recurrence was prognostic (Cox HR=1.53, 95% CI 1.00–2.41, P=0.048) [PMID:31748746](../papers/31748746.md)

## Subtypes

- 1p19q codeleted oligodendroglioma (n=69, 53.9%) and 1p19q intact astrocytoma (n=59, 46.1%) [PMID:37910594](../papers/37910594.md).
- Molecular grade-high (CDKN2A/B homozygous deletion, n=4) behaves aggressively on imaging even during watch-and-wait [PMID:37910594](../papers/37910594.md).

## Therapeutic landscape

- Tumor volume growth rate (TVGR) on volumetric MRI proposed as an earlier surrogate endpoint for active-surveillance trials of IDH-targeted therapies [PMID:37910594](../papers/37910594.md).
- Standard treatment ([temozolomide](../drugs/temozolomide.md) and/or radiotherapy) in IDH-mutant gliomas delays progression (PFI 40.5 vs 27 months, P=0.009) but is associated with epigenetic evolution toward an aggressive IDH-wildtype-like phenotype at recurrence; survival from second surgery is markedly worse in previously treated patients (log-rank P=0.0001) [PMID:38117484](../papers/38117484.md).
- [HOXD13](../genes/HOXD13.md) identified as master regulator of IDH-mutant astrocytoma progression; CRISPR knockout decreased cell proliferation [PMID:38117484](../papers/38117484.md).

## Sources

- [PMID:37910594](../papers/37910594.md)
- [PMID:38117484](../papers/38117484.md)
- [PMID:39289779](../papers/39289779.md)
- [PMID:28872634](../papers/28872634.md)
- [PMID:24336570](../papers/24336570.md)
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
- [PMID:28007021](../papers/28007021.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

- [PMID:30675060](../papers/30675060.md)
- [PMID:31263031](../papers/31263031.md) — Jonsson et al. MSK glioma prospective cohort (Clinical Cancer Research 2019).

*This page was processed by **entity-page-writer** on **2026-05-16**.*

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31748746](../papers/31748746.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
