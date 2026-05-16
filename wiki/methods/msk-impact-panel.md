---
name: MSK-IMPACT panel (generic)
slug: msk-impact-panel
kind: method
canonical_source: 
unverified: true
tags: [msk-impact, targeted-sequencing, panel]
processed_by: wiki-cli
processed_at: 2026-05-16
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
- Targeted hybrid-capture sequencing of 279 cancer-associated genes (Illumina HiSeq 2000, mean depth 442×, ≥100× at 97% of targeted exons) used on 12 paired SCCOHT tumor/normal samples, identifying biallelic [SMARCA4](../genes/SMARCA4.md) inactivating mutations in 100% of cases [PMID:24658004](../papers/24658004.md)
- Capture-based MSK-IMPACT sequencing of 109 high-grade urothelial bladder carcinomas ([blca_mskcc_solit_2014](../datasets/blca_mskcc_solit_2014.md)) at mean 579x coverage across targeted exons; detected mutations in 240 genes with 23 mutated in ≥5% of cases; [PIK3CA](../genes/PIK3CA.md) mutation associated with improved post-cystectomy recurrence-free survival [PMID:25092538](../papers/25092538.md)
- Custom 230-gene targeted capture panel (mean coverage 692×) applied to 69 matched CRC primary/metastasis trios; demonstrated 100% concordance of KRAS/NRAS/BRAF and 93% overall concordance for recurrent driver mutations. [PMID:25164765](../papers/25164765.md)
- Used in [MPNST](../cancer_types/MPNST.md) validation cohort (37 FFPE MPNSTs and 7 neurofibromas from 32 [NF1](../genes/NF1.md) patients); targeted hybrid-capture panel including [NF1](../genes/NF1.md), [SUZ12](../genes/SUZ12.md), [EED](../genes/EED.md), [CDKN2A](../genes/CDKN2A.md), [TP53](../genes/TP53.md) confirmed PRC2 alterations in 70–90% of MPNSTs [PMID:25240281](../papers/25240281.md)
- MSK-IMPACT targeted sequencing panel applied to >650 pancreatic ductal adenocarcinoma samples to profile somatic mutations and copy-number alterations [PMID:26278805](../papers/26278805.md)
- Used as the 341-gene IMPACT341 targeted-capture NGS panel (mean depth 584x tumor / 236x normal; 739x for ATCs) to sequence 117 advanced thyroid tumors (84 PDTC, 33 ATC) at MSKCC; detected TP53, TERT, SWI/SNF, and HMT mutations at 2-3x higher frequency than WES due to deep coverage. [PMID:26878173](../papers/26878173.md)
- Used as the CLIA-certified MSK-IMPACT 341-gene panel to profile 6 plasmacytoid-variant bladder tumors in a prospective clinical cohort at MSKCC; identified CDH1 truncating mutations in all 6 plasmacytoid cases and 0/56 urothelial NOS cases. [PMID:26901067](../papers/26901067.md)
- MSK-IMPACT 410-gene panel (IMPACT410) applied to 151 advanced head and neck tumors at MSK; CLIA-approved, median coverage 600x; guided therapy in 21/151 (14%) patients and 13/53 (25%) HNSC cases [PMID:27442865](../papers/27442865.md)
- MSK-IMPACT 410-gene targeted exon-capture assay (>300 cancer genes, 500–1000x depth) used to validate in 161 prospective GCT patients the TP53/MDM2 alteration findings discovered by WES in the 19-patient discovery cohort [PMID:27646943](../papers/27646943.md)
- Used for targeted DNA sequencing (230-gene panel, avg 348x tumour / 280x normal coverage) to characterize 62 high-grade unclassified renal cell carcinoma (uRCC) tumours at MSKCC; variant calling via MuTect and GATK Somatic Indel Detector on hg19-aligned reads. [PMID:27713405](../papers/27713405.md)
- MSK-IMPACT panel sequencing (341 and 410-gene versions) applied to 10,945 tumors across 62 cancer types for clinical actionability [PMID:28336552](../papers/28336552.md)
- MSK-IMPACT hybridization-capture Illumina HiSeq 2500 platform with full exon coverage of 410 cancer-related genes used to characterize 19 anaplastic oligodendroglioma tumors in the odg_msk_2017 cohort [PMID:28472509](../papers/28472509.md)
- Prospective CLIA-certified hybrid-capture sequencing of 10,945 advanced/metastatic tumors from 10,336 patients across 62 tumor types; catalogued 78,066 non-synonymous mutations, 22,989 CNAs, and 1,875 rearrangements [PMID:28481359](../papers/28481359.md)
- Sequenced 105 NMIBC tumors and 40 MIBC comparators with matched germline DNA; ARID1A mutation was the only gene significantly associated with BCG recurrence (HR=3.14, p=0.002) [PMID:28583311](../papers/28583311.md)
- Hybridization-capture targeted DNA panel covering >300 cancer-related genes (SNVs, indels, somatic CNAs, structural rearrangements) applied to 504 tumors from 451 prostate cancer patients spanning locoregional to mCRPC; matched normal blood used for germline filtering; 68% sequencing success rate [PMID:28825054](../papers/28825054.md)
- CLIA-certified hybrid-capture targeted NGS assay applied to 295 metastatic esophagogastric adenocarcinoma (EGC) patients at MSKCC; mean coverage 744X; detected mutations, copy-number alterations, and select rearrangements [PMID:29122777](../papers/29122777.md)
- MSK-IMPACT prospectively sequenced 1,134 [COADREAD](../cancer_types/COADREAD.md) tumors (panels [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)) with 98.6% MMR-IHC/MSIsensor concordance; characterized recurrently mutated genes, APC intronic variants, and CTNNB1 exon-3 deletions in MSS and MSI-H CRC [PMID:29316426](../papers/29316426.md)
- Central sequencing of 91 archival FFPE tumors and 15 plasma cfDNA samples from the SUMMIT neratinib basket trial using [IMPACT341](../methods/IMPACT341.md) (n=18) or [IMPACT410](../methods/IMPACT410.md) (n=88) at mean 738× coverage; concordance with local testing 95% [PMID:29420467](../papers/29420467.md)
- MC3 capture-kit mask excluded 170 CDS-altering calls in MSK-IMPACT's 410-gene panel that fall outside the Broad capture BED, including TERT promoter hits, CIC truncations, and CRLF2 splice alterations [PMID:29596782](../papers/29596782.md)
- 706 advanced prostate cancers from MSK-IMPACT (msk_impact_2017) used as validation cohort for the prad_p1000 WES SMG analysis [PMID:29610475](../papers/29610475.md)
- MSK-IMPACT 468-gene panel (IMPACT468) applied at ~500-fold coverage to 22 patient-derived bladder cancer organoid lines and matched parental tumors; enables subclonal variant detection and includes TERT promoter capture [PMID:29625057](../papers/29625057.md).
- Used to sequence 195 cholangiocarcinoma patients in the chol_msk_2018 cohort; 20 patients sequenced with 341-gene panel (IMPACT341) and 175 with 410-gene panel (IMPACT410); median coverage 759×; 47.6% of patients had actionable alterations at OncoKB level 3B or higher [PMID:29848569](../papers/29848569.md)
- Panel used to identify HLA-restricted neoantigens and tumor mutational burden in the MSK IMPACT sequencing cohort [PMID:29657128](../papers/29657128.md)
- Prospective MSK-IMPACT sequencing (341- or 410-gene versions) of 197 tumors from 189 advanced endometrial cancer patients; 67% carried ≥1 actionable alteration; panel enabled simultaneous MSI scoring, copy-number profiling, and germline assessment [PMID:30068706](../papers/30068706.md)
- Hybrid-capture targeted sequencing assay (341/410/468 gene panels; mean coverage 771×) used to sequence 1,918 breast tumors prospectively at MSKCC [PMID:30205045](../papers/30205045.md)
- Targeted exon capture assay spanning 300/341/410 cancer-associated genes used for prospective validation of 94 MIBC tumors; ERCC2-missense enrichment confirmed [PMID:30290956](../papers/30290956.md)
- Hybridization-capture targeted NGS (341/410/468 genes, mean coverage 690×) used to profile 127 advanced HCC patients; OncoKB and MSIsensor applied post-sequencing [PMID:30373752](../papers/30373752.md)
- Targeted DNA-sequencing assay (341–410 genes) applied to 81 GBCA tumors from three international centers [PMID:30427539](../papers/30427539.md)
- MSK-IMPACT targeted NGS (341-, 410-, or 468-gene versions) used to compute TMB (non-synonymous somatic mutations/exonic Mb) in 1,662 ICI-treated and 5,371 non-ICI-treated advanced cancer patients; TMB-high (top 20% per histology) associated with OS HR 0.52 across all histologies [PMID:30643254](../papers/30643254.md)
- MSK-IMPACT 410-gene panel (+ 46 introns from 17 rearranged genes) used to sequence CSF cell-free DNA and matched tumor tissue from 85 glioma patients; ctDNA detected in 42/85 (49.4%) CSFs with median TMB 4.90 mut/Mb, closely matching tissue biopsies (4.46/Mb) [PMID:30675060](../papers/30675060.md)
- Applied as matched tumor-normal hybridization-capture NGS platform to sequence 96 samples from 80 metastatic panNET patients at MSK; somatic alterations detected in 95% of patients [PMID:30687805](../papers/30687805.md)
- Used alongside MSK-HemePACT and whole-exome sequencing for genomic profiling of histiocytic neoplasm patients in the cobimetinib phase 2 trial (n=18); MAPK-pathway mutations identified in 83% of patients [PMID:30867592](../papers/30867592.md)
- Used for prospective paired tumor-normal sequencing of 837 of 1,004 adult glioma tumors (923 patients) at MSKCC, July 2013–July 2017; detected SNVs, indels, CNVs, and fusions across cancer-associated coding exons in the [glioma_mskcc_2019](../datasets/glioma_mskcc_2019.md) cohort [PMID:31263031](../papers/31263031.md)

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

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36593350](../papers/36593350.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36543146](../papers/36543146.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36517593](../papers/36517593.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36355783](../papers/36355783.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36228155](../papers/36228155.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36038778](../papers/36038778.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24658004](../papers/24658004.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25092538](../papers/25092538.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25240281](../papers/25240281.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26278805](../papers/26278805.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26878173](../papers/26878173.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26901067](../papers/26901067.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27646943](../papers/27646943.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28336552](../papers/28336552.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28472509](../papers/28472509.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28583311](../papers/28583311.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625057](../papers/29625057.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29657128](../papers/29657128.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30205045](../papers/30205045.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30290956](../papers/30290956.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30675060](../papers/30675060.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30687805](../papers/30687805.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30867592](../papers/30867592.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31263031](../papers/31263031.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
