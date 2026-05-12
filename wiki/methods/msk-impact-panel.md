---
name: MSK-IMPACT panel (generic)
slug: msk-impact-panel
kind: method
canonical_source: 
unverified: true
tags: [msk-impact, targeted-sequencing, panel]
processed_by: wiki-cli
processed_at: 2026-05-11
---

# MSK-IMPACT panel (generic)

## Overview

Generic slug for MSK-IMPACT, the Memorial Sloan Kettering matched tumor/normal hybridization-capture targeted DNA sequencing assay. Specific cBioPortal panel versions are tracked separately as `[IMPACT341](../methods/IMPACT341.md)`, `[IMPACT410](../methods/IMPACT410.md)`, `[IMPACT468](../methods/IMPACT468.md)`, and `[IMPACT505](../methods/IMPACT505.md)`. Used here when papers refer to MSK-IMPACT without specifying a panel era.

## Used by

- [PMID:36493333](../papers/36493333.md) — used to profile a retrospective MSK cohort of appendiceal adenocarcinoma patients (April 2015–October 2020). Matched tumor/normal hybridization-capture NGS, with oncogenic/actionable variants annotated via [OncoKB](../methods/oncokb.md) and clonality assessed with [FACETS](../methods/facets.md), defined three molecular MAAP subtypes (RAS-mut, GNAS-mut, TP53-mut predominant) associated with [OS](../cancer_types/OS.md), peritoneal tumor burden, and chemotherapy response [PMID:36493333](../papers/36493333.md).
- [PMID:37084736](../papers/37084736.md) — used to profile 2,532 [LUAD](../cancer_types/LUAD.md) specimens from 2,309 MSK patients for the metastatic organotropism study; an additional WES subcohort supported mutational signature analysis. Identified TP53/SMARCA4/CDKN2A inactivation as correlated with site-specific shorter time to metastasis, and showed only ~4% of metastases harbored actionable alterations not present in the matched primary [PMID:37084736](../papers/37084736.md).
- [PMID:37682528](../papers/37682528.md) — used to sequence 1,507 urothelial carcinoma tumors from 1,421 MSK patients ([BLCA](../cancer_types/BLCA.md)/[UTUC](../cancer_types/UTUC.md)), defining the landscape of [FGFR3](../genes/FGFR3.md) alterations across NMIBC, MIBC, [UTUC](../cancer_types/UTUC.md), and metastatic disease, and documenting 26% primary/metastasis [FGFR3](../genes/FGFR3.md) discordance in paired samples [PMID:37682528](../papers/37682528.md).
- [PMID:37910594](../papers/37910594.md) — 468-gene targeted hybrid-capture NGS applied to 73/128 patients with IDH-mutant Grade 2 glioma with tissue available, identifying [TERT](../genes/TERT.md) promoter mutations (100%), [CIC](../genes/CIC.md) (42%) and [FUBP1](../genes/FUBP1.md) (24%) in 1p19q codeleted tumors and [TP53](../genes/TP53.md) (94%) and [ATRX](../genes/ATRX.md) (77%) in 1p19q intact tumors; CDKN2A/B homozygous deletion defined molecular grade-high tumors with ~2x faster tumor volume growth rate [PMID:37910594](../papers/37910594.md).
- [PMID:39506116](../papers/39506116.md) — MSK-IMPACT targeted panel sequencing of 24,950 MSK patients across [NSCLC](../cancer_types/NSCLC.md), [BRCA](../cancer_types/BRCA.md), [COADREAD](../cancer_types/COADREAD.md), [PRAD](../cancer_types/PRAD.md), and [PAAD](../cancer_types/PAAD.md) formed the genomic backbone of the MSK-CHORD clinicogenomic dataset; enabled discovery of [SETD2](../genes/SETD2.md) driver mutations in 3% of [LUAD](../cancer_types/LUAD.md) as a biomarker of longer [OS](../cancer_types/OS.md), lower CNS metastasis, and improved immune checkpoint blockade response [PMID:39506116](../papers/39506116.md).
- [PMID:37477937](../papers/37477937.md) — MSK-IMPACT sequencing contributed to the cohort analysis [PMID:37477937](../papers/37477937.md).
- [PMID:38147626](../papers/38147626.md) — MSK-IMPACT sequencing contributed to the cohort analysis [PMID:38147626](../papers/38147626.md).
- [PMID:38864854](../papers/38864854.md) — MSK-IMPACT sequencing contributed to the cohort analysis [PMID:38864854](../papers/38864854.md).
- [PMID:38995739](../papers/38995739.md) — referenced alongside the heme-focused [MSK-HemePACT](../methods/msk-hemepact.md) panel in the phase I/II [ibrutinib](../drugs/ibrutinib.md) trial in r/r CNS lymphoma; an independent cohort of 177 MSK [PCNSL](../cancer_types/PCNSL.md) patients treated with standard of care was used to show [TBL1XR1](../genes/TBL1XR1.md) status was not prognostic under SOC, supporting its predictive (rather than prognostic) role for [ibrutinib](../drugs/ibrutinib.md) benefit [PMID:38995739](../papers/38995739.md).
- [PMID:39214094](../papers/39214094.md) — applied to 397/1,360 resected [PAAD](../cancer_types/PAAD.md) patients in the MSK `pancreas_msk_2024` cohort with no selection criteria, producing driver-gene and [KRAS](../genes/KRAS.md)-allele calls that underpinned the stage I [KRAS](../genes/KRAS.md)^G12R^ enrichment and allele-specific outcome findings; authors explicitly note that CDKN2A/B deep deletions were under-detected by IMPACT and excluded from their main analyses [PMID:39214094](../papers/39214094.md).
- [PMID:39289779](../papers/39289779.md) — FDA-authorized MSK-IMPACT ([IMPACT468](../methods/IMPACT468.md) n=274, [IMPACT505](../methods/IMPACT505.md) n=733) applied to cfDNA from 1,007 CSF samples from 711 patients with CNS tumors; detected somatic alterations in 53% of samples from patients with documented CNS disease (specificity 100%); ctDNA positivity associated with HR 3.23 for death (p<0.001) [PMID:39289779](../papers/39289779.md).
- [PMID:39746944](../papers/39746944.md) — MSK-IMPACT (including [IMPACT468](../methods/IMPACT468.md)) used as the primary sequencing platform for MiMSI training (n=741) and prospective cohort (n=5,037 and n=45,112); microsatellite loci from 1,755 IMPACT-covered microsatellite sites were used to train the deep MIL classifier; MiMSI reduced the indeterminate MSI call rate from 3.8% to 0.47% across 45,112 samples [PMID:39746944](../papers/39746944.md).
- [PMID:39753968](../papers/39753968.md) — FDA-authorized MSK-IMPACT applied to 2,336 [PAAD](../cancer_types/PAAD.md) patients (median 606× depth); four panel generations ([IMPACT341](../methods/IMPACT341.md) n=17, [IMPACT410](../methods/IMPACT410.md) n=438, [IMPACT468](../methods/IMPACT468.md) n=1,536, [IMPACT505](../methods/IMPACT505.md) n=345); enabled definition of three genomic PDAC subtypes (KRAS-mutant 95%, other-MAPK-mutant 3%, MAPK-WT 2%) and [KRAS](../genes/KRAS.md) mutant-allele dosage prognostic analyses [PMID:39753968](../papers/39753968.md).
- [PMID:40256659](../papers/40256659.md) — MSK-IMPACT applied to matched archival tumor tissue from 107 of 201 mUC patients in the CALGB 90601 trial; 57.1% of DDR alterations concordant between cfDNA and matched tumor; cfDNA numerically detected higher rates of [PIK3CA](../genes/PIK3CA.md), [RB1](../genes/RB1.md), [ERCC2](../genes/ERCC2.md), [BRAF](../genes/BRAF.md), and [KRAS](../genes/KRAS.md) alterations than matched tumor [PMID:40256659](../papers/40256659.md).
- [PMID:37643132](../papers/37643132.md) — MSK-IMPACT (341, 410, or 468 genes, avg 648x coverage) used to sequence 177 [CESC](../cancer_types/CESC.md) patients; actionability annotated via [OncoKB](../methods/oncokb.md) v3.1.4 [PMID:37643132](../papers/37643132.md).
- [PMID:37651310](../papers/37651310.md) — MSK-IMPACT (341–505 gene panel, tumor-normal, FDA-authorized) used to sequence 1,882 endometrial carcinoma patients; genetic ancestry inferred from IMPACT data; copy number analysis performed with [FACETS](../methods/facets.md) [PMID:37651310](../papers/37651310.md).
- [PMID:37699004](../papers/37699004.md) — MSK-IMPACT ([IMPACT505](../methods/IMPACT505.md), up to 505 genes) used to sequence 902/1,123 esophagogastric cancer patients; germline analysis performed with a 76–88-gene MSK-IMPACT panel [PMID:37699004](../papers/37699004.md).
- [PMID:37730754](../papers/37730754.md) — MSK-IMPACT used to sequence MSK cohort (n=20) of relapsed/metastatic rhabdomyosarcoma patients [PMID:37730754](../papers/37730754.md).
- [PMID:38488807](../papers/38488807.md) — MSK-IMPACT (341–505 genes) used to profile 195 STLMS and 238 [ULMS](../cancer_types/ULMS.md) cases; longitudinal subset of 18 STLMS and 15 [ULMS](../cancer_types/ULMS.md) patients had sequential tumors sequenced [PMID:38488807](../papers/38488807.md).
- [PMID:38630790](../papers/38630790.md) — MSK-IMPACT used to profile 290 diffuse pleural mesothelioma ([PLMESO](../cancer_types/PLMESO.md)) patients; 210 (72%) had sufficient tumor purity for [FACETS](../methods/facets.md) LOH analysis [PMID:38630790](../papers/38630790.md).
- [PMID:38653864](../papers/38653864.md) — MSK-IMPACT used for MSI/TMB assessment in 35 patients with dMMR/MSI-H/hypermutated gynecologic cancers on [nivolumab](../drugs/nivolumab.md) phase 2 trial [PMID:38653864](../papers/38653864.md).
- [PMID:38758238](../papers/38758238.md) — MSK-IMPACT used to sequence all pituitary neuroendocrine tumors; retrospective cohort (n=26) also underwent [WES](../methods/whole-exome-seq.md) for [USP8](../genes/USP8.md) mutation detection [PMID:38758238](../papers/38758238.md).
- [PMID:38922339](../papers/38922339.md) — 97,024 samples from 69,337 patients sequenced via MSK-IMPACT, MSK-ACCESS, and MSK-Fusion between January 2014 and November 2022; identified 212 patients with oncogenic [BRAF](../genes/BRAF.md) fusions across 52 histologies [PMID:38922339](../papers/38922339.md).
- [PMID:38949888](../papers/38949888.md) — 3,244 prostate cancer tumors from 2,257 patients sequenced using MSK-IMPACT targeted NGS panel; WES performed on 48 tumor samples via recapture of MSK-IMPACT libraries [PMID:38949888](../papers/38949888.md).
- [PMID:35764743](../papers/35764743.md) — MSK-IMPACT targeted clinical sequencing used to infer HRD status for 130 MSKCC [HGSOC](../cancer_types/HGSOC.md) patients with research consent; variant significance annotated via OncoKB and Hotspot; high-confidence COSMIC SBS3 detected in 48 and low-confidence in 30 patients; HRD status combined with histopathological and radiological features in the multimodal late-fusion prognostic model [PMID:35764743](../papers/35764743.md).
- Used to sequence 103 [GIST](../cancer_types/GIST.md) patients (341, 410, or 505 gene panels) and 499 tumor-normal pairs at MSKCC; ESMO-recommended VAF thresholds (>30% SNVs, >20% indels) correctly distinguished germline from somatic P/LP variants [PMID:36593350](../papers/36593350.md)
- Applied to 1,313 bladder urothelial carcinoma patients at MSK (2014-2021); mean TMB 11.7 in primary vs 11.2 in metastatic tumors (Wilcoxon p=0.1); 23% of actionable mutations ([FGFR3](../genes/FGFR3.md), [PIK3CA](../genes/PIK3CA.md), [TSC1](../genes/TSC1.md), [ERBB2](../genes/ERBB2.md)) discordant between primary-metastasis pairs [PMID:36543146](../papers/36543146.md)
- [IMPACT468](../methods/IMPACT468.md) (468-gene panel) applied to 42 treatment-naive [HGSOC](../cancer_types/HGSOC.md) patients; validation cohort of 1,298 [HGSOC](../cancer_types/HGSOC.md) patients used to confirm clonal 6p HLA LOH frequency (31% in BRCA1-mutant cases) [PMID:36517593](../papers/36517593.md)
- Used alongside Guardant360 CDx and MSK-ACCESS for sequencing KRASG12C-mutant colorectal cancer cell lines, PDX, and tissue samples to characterize acquired resistance mechanisms to combined KRAS/EGFR inhibition [PMID:36355783](../papers/36355783.md)
- Used to profile 244 [GBC](../cancer_types/GBC.md) samples (233 patients) at MSK with 341--505 gene panel versions (median coverage 634X), identifying actionable alterations in 35% of patients [PMID:36228155](../papers/36228155.md)
- Used for genomic profiling in a 247-patient [NSCLC](../cancer_types/NSCLC.md) cohort treated with PD-(L)1 blockade; TMB from MSK-IMPACT achieved AUC = 0.61 alone vs AUC = 0.80 for the full multimodal DyAM model [PMID:36038778](../papers/36038778.md)
- Targeted hybrid-capture sequencing of 279 cancer-associated genes (Illumina HiSeq 2000, mean depth 442×, ≥100× at 97% of targeted exons) used on 12 paired SCCOHT tumor/normal samples, identifying biallelic SMARCA4 inactivating mutations in 100% of cases [PMID:24658004](../papers/24658004.md)
- Capture-based MSK-IMPACT sequencing of 109 high-grade urothelial bladder carcinomas (blca_mskcc_solit_2014) at mean 579x coverage across targeted exons; detected mutations in 240 genes with 23 mutated in ≥5% of cases; PIK3CA mutation associated with improved post-cystectomy recurrence-free survival [PMID:25092538](../papers/25092538.md)

## Notes

- Targeted-panel scope limits subtype calls and mutational-signature resolution; both papers note this limitation, and the [LUAD](../cancer_types/LUAD.md) study partially mitigates it with a WES subcohort [PMID:36493333](../papers/36493333.md) [PMID:37084736](../papers/37084736.md).
- For panel-specific analyses (IMPACT341/410/468/505), see the dedicated canonical-panel pages.

## Sources

- [PMID:36493333](../papers/36493333.md)
- [PMID:37084736](../papers/37084736.md)
- [PMID:37682528](../papers/37682528.md)
- [PMID:37910594](../papers/37910594.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:37477937](../papers/37477937.md)
- [PMID:38147626](../papers/38147626.md)
- [PMID:38864854](../papers/38864854.md)
- [PMID:38995739](../papers/38995739.md)
- [PMID:39214094](../papers/39214094.md)
- [PMID:37643132](../papers/37643132.md)
- [PMID:37651310](../papers/37651310.md)
- [PMID:37699004](../papers/37699004.md)
- [PMID:37730754](../papers/37730754.md)
- [PMID:38488807](../papers/38488807.md)
- [PMID:38630790](../papers/38630790.md)
- [PMID:38653864](../papers/38653864.md)
- [PMID:38758238](../papers/38758238.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:35764743](../papers/35764743.md)
- [PMID:39289779](../papers/39289779.md)
- [PMID:39746944](../papers/39746944.md)
- [PMID:39753968](../papers/39753968.md)
- [PMID:40256659](../papers/40256659.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36593350](../papers/36593350.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36543146](../papers/36543146.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36517593](../papers/36517593.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36355783](../papers/36355783.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36228155](../papers/36228155.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:36038778](../papers/36038778.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:24658004](../papers/24658004.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25092538](../papers/25092538.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
