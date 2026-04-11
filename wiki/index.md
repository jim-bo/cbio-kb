---
title: "cbio-kb"
subtitle: "A living knowledge base of cBioPortal publications"
toc: false
---

**cbio-kb** is a structured, cross-linked reading of the primary literature
behind [cBioPortal](https://www.cbioportal.org/) studies. It follows the
[LLM knowledge base pattern described by Andrej Karpathy](https://x.com/karpathy/status/2039805659525644595)
([idea file gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)):
raw source documents are incrementally compiled by an LLM into a directory of
interlinked Markdown pages, with the LLM maintaining summaries, backlinks,
and indexes as the corpus grows.

Every paper in the corpus is distilled into a standardized page — cohort, methods, key findings,
clinical implications, open questions — and every gene, cancer type, dataset,
drug, and assay mentioned gets its own page that aggregates what the corpus
collectively says about it.

The goal is to make it fast to answer questions like:

- *What has been published about* **[FGFR3](genes/FGFR3.md)** *in* **[urothelial carcinoma](cancer_types/BLCA.md)** *?*
- *Which studies profiled the* **[MSK-IMPACT](datasets/msk_impact_2017.md)** *cohort, and what did they find?*
- *Where has* **[erdafitinib](drugs/erdafitinib.md)** *resistance been characterized?*
- *What methods have been used to detect clonal hematopoiesis in solid-tumor sequencing?*

Every claim on an entity page is traceable back to a specific paper via
`PMID:` citations, and every paper page links out to the entities it touches.
Nothing is invented — unverified terms are flagged rather than canonicalized.

## Browse

| Section | Count | What you'll find |
|---|---|---|
| [Papers](#papers) | 43 | Per-publication summaries: cohort, methods, findings, citations |
| [Genes](#genes) | 253 | Alterations, co-occurrence, therapeutic relevance across the corpus |
| [Cancer types](#cancer-types) | 70 | OncoTree-anchored disease pages linking studies and alterations |
| [Datasets](#datasets) | 50 | cBioPortal studies with cohort details and linked publications |
| [Drugs](#drugs) | 51 | Targeted therapies, resistance patterns, evidence in the corpus |
| [Methods](#methods) | 51 | Sequencing assays, gene panels, and analytical pipelines |
| [Themes](#themes) | 0 | Cross-cutting syntheses (in progress) |

## Papers

- [25730765](papers/25730765.md) — The landscape of somatic mutations in Infant MLL rearranged acute lymphoblastic leukemias
- [27634761](papers/27634761.md) — A platform-independent AI tumor lineage and site (ATLAS) classifier
- [34433969](papers/34433969.md) — A Clinically Applicable Integrative Molecular Classification of Meningiomas
- [35927489](papers/35927489.md) — Molecular map of chronic lymphocytic leukemia and its impact on outcome
- [36357680](papers/36357680.md) — Overall survival with circulating tumor DNA-guided therapy in advanced non-small-cell lung cancer
- [36493333](papers/36493333.md) — Molecular Classification of Appendiceal Adenocarcinoma
- [36723991](papers/36723991.md) — Molecular Evolution of Classic Hodgkin Lymphoma Revealed Through Whole-Genome Sequencing of Hodgkin and Reed Sternberg Cells
- [36862133](papers/36862133.md) — Overcoming barriers to tumor genomic profiling through direct-to-patient outreach
- [37078708](papers/37078708.md) — TP53 mutations identify high-risk events for peripheral T-cell lymphoma treated with CHOP-based chemotherapy
- [37084736](papers/37084736.md) — Genomic Mapping of Metastatic Organotropism in Lung Adenocarcinoma
- [37202560](papers/37202560.md) — An integrated tumor, immune and microbiome atlas of colon cancer
- [37315267](papers/37315267.md) — Extremity Rhabdomyosarcoma: An Integrated Clinicopathologic and Genomic Study to Improve Risk Stratification
- [37350195](papers/37350195.md) — Distinct genomic landscapes in radiation-associated angiosarcoma compared with other radiation-associated sarcoma histologies
- [37406106](papers/37406106.md) — Determinants of Survival with Combined HER2 and PD-1 Blockade in Metastatic Esophagogastric Cancer
- [37477937](papers/37477937.md) — Novel Genomic Risk Stratification Model for Primary Gastrointestinal Stromal Tumors (GIST) in the Adjuvant Therapy Era
- [37591896](papers/37591896.md) — Genomic analysis and clinical correlations of non-small cell lung cancer brain metastasis
- [37643132](papers/37643132.md) — Assessing the Genomic Landscape of Cervical Cancers: Clinical Opportunities and Therapeutic Targets
- [37651310](papers/37651310.md) — Molecular characterization of endometrial carcinomas in Black and White patients reveals disparate drivers with therapeutic implications
- [37682528](papers/37682528.md) — Clinical and Genomic Landscape of FGFR3-Altered Urothelial Carcinoma and Treatment Outcomes with Erdafitinib: A Real-World Experience
- [37699004](papers/37699004.md) — Clinical and molecular characteristics of early-onset vs average-onset esophagogastric cancer
- [37730754](papers/37730754.md) — Sequential genomic analysis using a multisample/multiplatform approach to better define rhabdomyosarcoma progression and relapse
- [37769223](papers/37769223.md) — Targeted Molecular Profiling of Circulating Cell-Free DNA in Patients With Advanced Hepatocellular Carcinoma
- [37910594](papers/37910594.md) — Tumor Volume Growth Rates and Doubling Times during Active Surveillance of IDH-mutant Low-Grade Glioma
- [38117484](papers/38117484.md) — The Epigenetic Evolution of Glioma Is Determined by the IDH1 Mutation Status and Treatment Regimen
- [38147626](papers/38147626.md) — High-risk and silent clonal hematopoietic genotypes in patients with nonhematologic cancer
- [38412093](papers/38412093.md) — The genomic and evolutionary landscapes of anaplastic thyroid carcinoma
- [38488807](papers/38488807.md) — Developing Novel Genomic Risk Stratification Models in Soft Tissue and Uterine Leiomyosarcoma
- [38488813](papers/38488813.md) — Integrative Molecular Analyses of the MD Anderson Prostate Cancer Patient-derived Xenograft (MDA PCa PDX) Series
- [38497151](papers/38497151.md) — Validation of LymphGen classification on a 400-gene clinical next-generation sequencing panel in diffuse large B-cell lymphoma: real-world experience from a cancer center
- [38630790](papers/38630790.md) — Diffuse pleural mesotheliomas with genomic near-haploidization: a newly recognized subset with distinct clinical, histologic, and molecular features
- [38653864](papers/38653864.md) — Nivolumab for mismatch-repair-deficient or hypermutated gynecologic cancers: a phase 2 trial with biomarker analyses
- [38758238](papers/38758238.md) — Genome-wide loss of heterozygosity predicts aggressive, treatment-refractory behavior in pituitary neuroendocrine tumors
- [38864854](papers/38864854.md) — A Novel Approach to Quantify Heterogeneity of Intrahepatic Cholangiocarcinoma: the Hidden-Genome Classifier
- [38895302](papers/38895302.md) — Molecular effects of indoor tanning
- [38922339](papers/38922339.md) — Tumor-agnostic genomic and clinical analysis of BRAF fusions identify actionable targets
- [38949888](papers/38949888.md) — Microsatellite Instability, Tumor Mutational Burden, and Response to Immune Checkpoint Blockade in Patients with Prostate Cancer
- [38995739](papers/38995739.md) — A Phase II study assessing Long-Term Response to Ibrutinib Monotherapy in recurrent or refractory CNS Lymphoma
- [39091884](papers/39091884.md) — Genetic evolution of keratinocytes to cutaneous squamous cell carcinoma
- [39147831](papers/39147831.md) — DNA liquid biopsy-based prediction of cancer-associated venous thromboembolism
- [39214094](papers/39214094.md) — Distinct clinical outcomes and biological features of specific KRAS mutants in human pancreatic cancer
- [39289779](papers/39289779.md) — Real-world experience with circulating tumor DNA in cerebrospinal fluid from patients with central nervous system tumors
- [39386723](papers/39386723.md) — Multimodal Spatial Profiling Reveals Immune Suppression and Microenvironment Remodeling in Fallopian Tube Precursors to High-Grade Serous Ovarian Carcinoma
- [39506116](papers/39506116.md) — Automated real-world data integration improves cancer outcome prediction

## Genes

[ACADL](genes/ACADL.md) · [AGK](genes/AGK.md) · [AKT1](genes/AKT1.md) · [AKT2](genes/AKT2.md) · [ALK](genes/ALK.md) · [APC](genes/APC.md) · [AR](genes/AR.md) · [ARID1A](genes/ARID1A.md) · [ARID2](genes/ARID2.md) · [ASXL1](genes/ASXL1.md) · [ATM](genes/ATM.md) · [ATR](genes/ATR.md) · [ATRX](genes/ATRX.md) · [AURKA](genes/AURKA.md) · [B2M](genes/B2M.md) · [BANF1](genes/BANF1.md) · [BAP1](genes/BAP1.md) · [BCL2](genes/BCL2.md) · [BCL6](genes/BCL6.md) · [BCL7A](genes/BCL7A.md) · [BCOR](genes/BCOR.md) · [BRAF](genes/BRAF.md) · [BRCA1](genes/BRCA1.md) · [BRCA2](genes/BRCA2.md) · [CARD11](genes/CARD11.md) · [CBL](genes/CBL.md) · [CCL5](genes/CCL5.md) · [CCND1](genes/CCND1.md) · [CCND3](genes/CCND3.md) · [CCNE1](genes/CCNE1.md) · [CD274](genes/CD274.md) · [CD79B](genes/CD79B.md) · [CD8A](genes/CD8A.md) · [CD8B](genes/CD8B.md) · [CDH1](genes/CDH1.md) · [CDK12](genes/CDK12.md) · [CDK4](genes/CDK4.md) · [CDK7](genes/CDK7.md) · [CDKN1A](genes/CDKN1A.md) · [CDKN2A](genes/CDKN2A.md) · [CDKN2B](genes/CDKN2B.md) · [CENPF](genes/CENPF.md) · [CGAS](genes/CGAS.md) · [CHD2](genes/CHD2.md) · [CHEK2](genes/CHEK2.md) · [CIC](genes/CIC.md) · [CREBBP](genes/CREBBP.md) · [CRKL](genes/CRKL.md) · [CSF1R](genes/CSF1R.md) · [CTLA4](genes/CTLA4.md) · [CTNNB1](genes/CTNNB1.md) · [CXCL10](genes/CXCL10.md) · [CXCL9](genes/CXCL9.md) · [DAXX](genes/DAXX.md) · [DICER1](genes/DICER1.md) · [DIS3](genes/DIS3.md) · [DMD](genes/DMD.md) · [DNMT3A](genes/DNMT3A.md) · [EGFR](genes/EGFR.md) · [EIF1AX](genes/EIF1AX.md) · [EML4](genes/EML4.md) · [ERBB2](genes/ERBB2.md) · [ERBB3](genes/ERBB3.md) · [ERG](genes/ERG.md) · [ETV1](genes/ETV1.md) · [ETV4](genes/ETV4.md) · [FANCA](genes/FANCA.md) · [FANCF](genes/FANCF.md) · [FAT1](genes/FAT1.md) · [FBXW7](genes/FBXW7.md) · [FGF9](genes/FGF9.md) · [FGFR1](genes/FGFR1.md) · [FGFR2](genes/FGFR2.md) · [FGFR3](genes/FGFR3.md) · [FLT3](genes/FLT3.md) · [FLT4](genes/FLT4.md) · [FOXA1](genes/FOXA1.md) · [FOXM1](genes/FOXM1.md) · [FOXO1](genes/FOXO1.md) · [FOXP3](genes/FOXP3.md) · [FUBP1](genes/FUBP1.md) · [GLI1](genes/GLI1.md) · [GNA13](genes/GNA13.md) · [GNAS](genes/GNAS.md) · [GNLY](genes/GNLY.md) · [GZMA](genes/GZMA.md) · [GZMB](genes/GZMB.md) · [GZMH](genes/GZMH.md) · [H3-3A](genes/H3-3A.md) · [HLA-A](genes/HLA-A.md) · [HLA-B](genes/HLA-B.md) · [HLA-E](genes/HLA-E.md) · [HMCN1](genes/HMCN1.md) · [HOXA7](genes/HOXA7.md) · [HOXD13](genes/HOXD13.md) · [HRAS](genes/HRAS.md) · [HSPG2](genes/HSPG2.md) · [IDH1](genes/IDH1.md) · [IDH2](genes/IDH2.md) · [IDO1](genes/IDO1.md) · [IFITM1](genes/IFITM1.md) · [IFNG](genes/IFNG.md) · [IGF2](genes/IGF2.md) · [IL12B](genes/IL12B.md) · [IL4R](genes/IL4R.md) · [INO80](genes/INO80.md) · [INPPL1](genes/INPPL1.md) · [IRF1](genes/IRF1.md) · [IRF7](genes/IRF7.md) · [IRF9](genes/IRF9.md) · [ISG15](genes/ISG15.md) · [ITPKB](genes/ITPKB.md) · [JAK1](genes/JAK1.md) · [JAK2](genes/JAK2.md) · [KDM6A](genes/KDM6A.md) · [KDR](genes/KDR.md) · [KEAP1](genes/KEAP1.md) · [KIAA1549](genes/KIAA1549.md) · [KIT](genes/KIT.md) · [KLF4](genes/KLF4.md) · [KLRK1](genes/KLRK1.md) · [KMT2A](genes/KMT2A.md) · [KMT2B](genes/KMT2B.md) · [KMT2C](genes/KMT2C.md) · [KMT2D](genes/KMT2D.md) · [KRAS](genes/KRAS.md) · [LRP1](genes/LRP1.md) · [MAP2K1](genes/MAP2K1.md) · [MAP2K2](genes/MAP2K2.md) · [MAPK1](genes/MAPK1.md) · [MAX](genes/MAX.md) · [MCL1](genes/MCL1.md) · [MCM2](genes/MCM2.md) · [MDM2](genes/MDM2.md) · [MED12](genes/MED12.md) · [MEGF8](genes/MEGF8.md) · [MET](genes/MET.md) · [MGA](genes/MGA.md) · [MGMT](genes/MGMT.md) · [MLH1](genes/MLH1.md) · [MSH2](genes/MSH2.md) · [MSH3](genes/MSH3.md) · [MSH6](genes/MSH6.md) · [MSL3](genes/MSL3.md) · [MSMB](genes/MSMB.md) · [MT1E](genes/MT1E.md) · [MT1H](genes/MT1H.md) · [MT2A](genes/MT2A.md) · [MX1](genes/MX1.md) · [MYB](genes/MYB.md) · [MYC](genes/MYC.md) · [MYCN](genes/MYCN.md) · [MYD88](genes/MYD88.md) · [MYOD1](genes/MYOD1.md) · [NCOR2](genes/NCOR2.md) · [NEUROD1](genes/NEUROD1.md) · [NF1](genes/NF1.md) · [NF2](genes/NF2.md) · [NFKB1](genes/NFKB1.md) · [NFKBIE](genes/NFKBIE.md) · [NKX2-1](genes/NKX2-1.md) · [NKX3-1](genes/NKX3-1.md) · [NOTCH1](genes/NOTCH1.md) · [NOTCH2](genes/NOTCH2.md) · [NOTCH3](genes/NOTCH3.md) · [NRAS](genes/NRAS.md) · [NT5C2](genes/NT5C2.md) · [NTRK1](genes/NTRK1.md) · [PAX3](genes/PAX3.md) · [PAX7](genes/PAX7.md) · [PBRM1](genes/PBRM1.md) · [PCNA](genes/PCNA.md) · [PDCD1](genes/PDCD1.md) · [PDGFRA](genes/PDGFRA.md) · [PIK3CA](genes/PIK3CA.md) · [PIK3CD](genes/PIK3CD.md) · [PIK3R1](genes/PIK3R1.md) · [PLCG1](genes/PLCG1.md) · [PMS2](genes/PMS2.md) · [POLD1](genes/POLD1.md) · [POLE](genes/POLE.md) · [POLR2A](genes/POLR2A.md) · [PPP2R1A](genes/PPP2R1A.md) · [PPP6C](genes/PPP6C.md) · [PRF1](genes/PRF1.md) · [PTCH1](genes/PTCH1.md) · [PTEN](genes/PTEN.md) · [PTPN1](genes/PTPN1.md) · [PTPN11](genes/PTPN11.md) · [PTPRB](genes/PTPRB.md) · [PTPRD](genes/PTPRD.md) · [PTPRT](genes/PTPRT.md) · [RAC1](genes/RAC1.md) · [RAD51B](genes/RAD51B.md) · [RAF1](genes/RAF1.md) · [RB1](genes/RB1.md) · [RECQL4](genes/RECQL4.md) · [RET](genes/RET.md) · [RFX7](genes/RFX7.md) · [RHOA](genes/RHOA.md) · [RICTOR](genes/RICTOR.md) · [RNF43](genes/RNF43.md) · [ROS1](genes/ROS1.md) · [RRM1](genes/RRM1.md) · [RSPO4](genes/RSPO4.md) · [RUNX1](genes/RUNX1.md) · [S100B](genes/S100B.md) · [SCGN](genes/SCGN.md) · [SDHA](genes/SDHA.md) · [SDHB](genes/SDHB.md) · [SETD1B](genes/SETD1B.md) · [SETD2](genes/SETD2.md) · [SETDB1](genes/SETDB1.md) · [SF3B1](genes/SF3B1.md) · [SMAD4](genes/SMAD4.md) · [SMARCA2](genes/SMARCA2.md) · [SMARCA4](genes/SMARCA4.md) · [SMARCB1](genes/SMARCB1.md) · [SMO](genes/SMO.md) · [SND1](genes/SND1.md) · [SOCS1](genes/SOCS1.md) · [SPEN](genes/SPEN.md) · [SPOP](genes/SPOP.md) · [STAT1](genes/STAT1.md) · [STAT3](genes/STAT3.md) · [STAT6](genes/STAT6.md) · [STING1](genes/STING1.md) · [STK11](genes/STK11.md) · [SUZ12](genes/SUZ12.md) · [TACC3](genes/TACC3.md) · [TBL1XR1](genes/TBL1XR1.md) · [TBX21](genes/TBX21.md) · [TEK](genes/TEK.md) · [TERT](genes/TERT.md) · [TET1](genes/TET1.md) · [TET2](genes/TET2.md) · [TGFBR2](genes/TGFBR2.md) · [TMPRSS2](genes/TMPRSS2.md) · [TMSB4X](genes/TMSB4X.md) · [TNFAIP3](genes/TNFAIP3.md) · [TP53](genes/TP53.md) · [TP63](genes/TP63.md) · [TRAF3](genes/TRAF3.md) · [TRAF7](genes/TRAF7.md) · [TRIM24](genes/TRIM24.md) · [TSC1](genes/TSC1.md) · [TSC2](genes/TSC2.md) · [USH2A](genes/USH2A.md) · [USP8](genes/USP8.md) · [VGLL3](genes/VGLL3.md) · [XPO1](genes/XPO1.md) · [ZC3H18](genes/ZC3H18.md) · [ZFP36L1](genes/ZFP36L1.md)

## Cancer types

[ACYC](cancer_types/ACYC.md) · [AITL](cancer_types/AITL.md) · [ALCL](cancer_types/ALCL.md) · [ALCLALKN](cancer_types/ALCLALKN.md) · [ALCLALKP](cancer_types/ALCLALKP.md) · [ANGS](cancer_types/ANGS.md) · [APAD](cancer_types/APAD.md) · [ARMS](cancer_types/ARMS.md) · [ASTR](cancer_types/ASTR.md) · [BLCA](cancer_types/BLCA.md) · [BLLKMT2A](cancer_types/BLLKMT2A.md) · [BRCA](cancer_types/BRCA.md) · [CESC](cancer_types/CESC.md) · [CHL](cancer_types/CHL.md) · [CLLSLL](cancer_types/CLLSLL.md) · [COAD](cancer_types/COAD.md) · [COADREAD](cancer_types/COADREAD.md) · [CSCC](cancer_types/CSCC.md) · [CUP](cancer_types/CUP.md) · [DIFG](cancer_types/DIFG.md) · [DLBCLNOS](cancer_types/DLBCLNOS.md) · [EATL](cancer_types/EATL.md) · [ECD](cancer_types/ECD.md) · [EGC](cancer_types/EGC.md) · [EHCH](cancer_types/EHCH.md) · [ERMS](cancer_types/ERMS.md) · [ESCA](cancer_types/ESCA.md) · [GB](cancer_types/GB.md) · [GBC](cancer_types/GBC.md) · [GEJ](cancer_types/GEJ.md) · [GIST](cancer_types/GIST.md) · [HCC](cancer_types/HCC.md) · [HGSOC](cancer_types/HGSOC.md) · [IHCH](cancer_types/IHCH.md) · [LCH](cancer_types/LCH.md) · [LMS](cancer_types/LMS.md) · [LUAD](cancer_types/LUAD.md) · [LUSC](cancer_types/LUSC.md) · [MBL](cancer_types/MBL.md) · [MEITL](cancer_types/MEITL.md) · [MEL](cancer_types/MEL.md) · [MFH](cancer_types/MFH.md) · [MGCT](cancer_types/MGCT.md) · [MNG](cancer_types/MNG.md) · [MPNST](cancer_types/MPNST.md) · [NSCLC](cancer_types/NSCLC.md) · [ODG](cancer_types/ODG.md) · [OGCT](cancer_types/OGCT.md) · [OS](cancer_types/OS.md) · [OVT](cancer_types/OVT.md) · [PAAD](cancer_types/PAAD.md) · [PAST](cancer_types/PAST.md) · [PCNSL](cancer_types/PCNSL.md) · [PLMESO](cancer_types/PLMESO.md) · [PRAD](cancer_types/PRAD.md) · [PRNE](cancer_types/PRNE.md) · [PTAD](cancer_types/PTAD.md) · [PTCL](cancer_types/PTCL.md) · [RMS](cancer_types/RMS.md) · [SCLC](cancer_types/SCLC.md) · [SCRMS](cancer_types/SCRMS.md) · [STAD](cancer_types/STAD.md) · [THAP](cancer_types/THAP.md) · [THPA](cancer_types/THPA.md) · [TLL](cancer_types/TLL.md) · [UCEC](cancer_types/UCEC.md) · [UCS](cancer_types/UCS.md) · [ULMS](cancer_types/ULMS.md) · [USC](cancer_types/USC.md) · [UTUC](cancer_types/UTUC.md)

## Datasets

[all_stjude_2015](datasets/all_stjude_2015.md) · [appendiceal_msk_2022](datasets/appendiceal_msk_2022.md) · [bladder_msk_2023](datasets/bladder_msk_2023.md) · [bm_nsclc_mskcc_2023](datasets/bm_nsclc_mskcc_2023.md) · [braf_msk_archer_2024](datasets/braf_msk_archer_2024.md) · [braf_msk_impact_2024](datasets/braf_msk_impact_2024.md) · [cervix_msk_2023](datasets/cervix_msk_2023.md) · [cesc_tcga_pan_can_atlas_2018](datasets/cesc_tcga_pan_can_atlas_2018.md) · [chl_sccc_2023](datasets/chl_sccc_2023.md) · [cll_broad_2022](datasets/cll_broad_2022.md) · [coad_silu_2022](datasets/coad_silu_2022.md) · [coadread_tcga](datasets/coadread_tcga.md) · [csf_msk_2024](datasets/csf_msk_2024.md) · [difg_glass](datasets/difg_glass.md) · [difg_msk_2023](datasets/difg_msk_2023.md) · [egc_msk_2023](datasets/egc_msk_2023.md) · [egc_trap_ccr_msk_2023](datasets/egc_trap_ccr_msk_2023.md) · [gist_msk_2023](datasets/gist_msk_2023.md) · [hcc_jcopo_msk_2023](datasets/hcc_jcopo_msk_2023.md) · [hcc_msk_2024](datasets/hcc_msk_2024.md) · [lms_msk_2024](datasets/lms_msk_2024.md) · [luad_mskcc_2023_met_organotropism](datasets/luad_mskcc_2023_met_organotropism.md) · [lung_smc_2016](datasets/lung_smc_2016.md) · [makeanimpact_ccr_2023](datasets/makeanimpact_ccr_2023.md) · [mbn_msk_2024](datasets/mbn_msk_2024.md) · [mng_utoronto_2021](datasets/mng_utoronto_2021.md) · [msk_ch_2023](datasets/msk_ch_2023.md) · [msk_chord_2024](datasets/msk_chord_2024.md) · [msk_ctdna_vte_2024](datasets/msk_ctdna_vte_2024.md) · [msk_impact_2017](datasets/msk_impact_2017.md) · [mtnn_msk_2022](datasets/mtnn_msk_2022.md) · [normal_skin_melanocytes_2024](datasets/normal_skin_melanocytes_2024.md) · [nsclc_ctdx_msk_2022](datasets/nsclc_ctdx_msk_2022.md) · [ovary_geomx_gray_foundation_2024](datasets/ovary_geomx_gray_foundation_2024.md) · [paad_icgc](datasets/paad_icgc.md) · [paad_tcga](datasets/paad_tcga.md) · [pancreas_msk_2024](datasets/pancreas_msk_2024.md) · [pcawg](datasets/pcawg.md) · [pcnsl_msk_2024](datasets/pcnsl_msk_2024.md) · [plmeso_msk_2024](datasets/plmeso_msk_2024.md) · [prad_msk_mdanderson_2023](datasets/prad_msk_mdanderson_2023.md) · [prad_su2c_2019](datasets/prad_su2c_2019.md) · [prad_tcga](datasets/prad_tcga.md) · [prostate_msk_2024](datasets/prostate_msk_2024.md) · [ptad_msk_2024](datasets/ptad_msk_2024.md) · [rms_msk_2023](datasets/rms_msk_2023.md) · [sarcoma_msk_2023](datasets/sarcoma_msk_2023.md) · [thyroid_gatci_2024](datasets/thyroid_gatci_2024.md) · [ucec_ancestry_cds_msk_2023](datasets/ucec_ancestry_cds_msk_2023.md) · [ucec_msk_2024](datasets/ucec_msk_2024.md)

## Drugs

[afatinib](drugs/afatinib.md) · [alpelisib](drugs/alpelisib.md) · [bevacizumab](drugs/bevacizumab.md) · [binimetinib](drugs/binimetinib.md) · [brentuximab-vedotin](drugs/brentuximab-vedotin.md) · [capecitabine](drugs/capecitabine.md) · [capmatinib](drugs/capmatinib.md) · [cobimetinib](drugs/cobimetinib.md) · [crizotinib](drugs/crizotinib.md) · [cyclophosphamide](drugs/cyclophosphamide.md) · [dabrafenib](drugs/dabrafenib.md) · [dostarlimab](drugs/dostarlimab.md) · [doxorubicin](drugs/doxorubicin.md) · [durvalumab](drugs/durvalumab.md) · [encorafenib](drugs/encorafenib.md) · [enfortumab-vedotin](drugs/enfortumab-vedotin.md) · [erdafitinib](drugs/erdafitinib.md) · [erlotinib](drugs/erlotinib.md) · [etoposide](drugs/etoposide.md) · [everolimus](drugs/everolimus.md) · [fludarabine](drugs/fludarabine.md) · [fluorouracil](drugs/fluorouracil.md) · [ibrutinib](drugs/ibrutinib.md) · [imatinib](drugs/imatinib.md) · [infigratinib](drugs/infigratinib.md) · [ipilimumab](drugs/ipilimumab.md) · [irinotecan](drugs/irinotecan.md) · [lenalidomide](drugs/lenalidomide.md) · [lenvatinib](drugs/lenvatinib.md) · [leucovorin](drugs/leucovorin.md) · [methotrexate](drugs/methotrexate.md) · [monalizumab](drugs/monalizumab.md) · [neratinib](drugs/neratinib.md) · [nivolumab](drugs/nivolumab.md) · [osimertinib](drugs/osimertinib.md) · [oxaliplatin](drugs/oxaliplatin.md) · [pembrolizumab](drugs/pembrolizumab.md) · [prednisone](drugs/prednisone.md) · [selumetinib](drugs/selumetinib.md) · [sirolimus](drugs/sirolimus.md) · [temozolomide](drugs/temozolomide.md) · [temsirolimus](drugs/temsirolimus.md) · [tirabrutinib](drugs/tirabrutinib.md) · [trametinib](drugs/trametinib.md) · [trastuzumab](drugs/trastuzumab.md) · [trastuzumab-deruxtecan](drugs/trastuzumab-deruxtecan.md) · [vemurafenib](drugs/vemurafenib.md) · [venetoclax](drugs/venetoclax.md) · [vincristine](drugs/vincristine.md) · [vinorelbine](drugs/vinorelbine.md) · [vorinostat](drugs/vorinostat.md)

## Methods

[16s-rrna-seq](methods/16s-rrna-seq.md) · [450k-methylation-array](methods/450k-methylation-array.md) · [89zr-trastuzumab-pet](methods/89zr-trastuzumab-pet.md) · [ACCESS129](methods/ACCESS129.md) · [IMPACT341](methods/IMPACT341.md) · [IMPACT410](methods/IMPACT410.md) · [IMPACT468](methods/IMPACT468.md) · [IMPACT505](methods/IMPACT505.md) · [archer-fusionplex](methods/archer-fusionplex.md) · [bayesian-nmf](methods/bayesian-nmf.md) · [clumps](methods/clumps.md) · [cms-classifier](methods/cms-classifier.md) · [coca](methods/coca.md) · [consensus-tme](methods/consensus-tme.md) · [cosmx-smi](methods/cosmx-smi.md) · [ctdna-dynamics](methods/ctdna-dynamics.md) · [ctdx-lung](methods/ctdx-lung.md) · [cycif](methods/cycif.md) · [epic-methylation-array](methods/epic-methylation-array.md) · [facets](methods/facets.md) · [fish](methods/fish.md) · [geomx-wta](methods/geomx-wta.md) · [icr-signature](methods/icr-signature.md) · [igcaller](methods/igcaller.md) · [immunoediting-quantification](methods/immunoediting-quantification.md) · [joint-longitudinal-survival-model](methods/joint-longitudinal-survival-model.md) · [lc-ms-ms-proteomics](methods/lc-ms-ms-proteomics.md) · [log-linear-mixed-effects-model](methods/log-linear-mixed-effects-model.md) · [lymphgen](methods/lymphgen.md) · [msk-access](methods/msk-access.md) · [msk-fusion](methods/msk-fusion.md) · [msk-hemepact](methods/msk-hemepact.md) · [msk-impact-panel](methods/msk-impact-panel.md) · [multiplexed-immunofluorescence](methods/multiplexed-immunofluorescence.md) · [nlp-prissmm](methods/nlp-prissmm.md) · [oncocast-mpm](methods/oncocast-mpm.md) · [oncokb](methods/oncokb.md) · [phylogicndt](methods/phylogicndt.md) · [random-survival-forest](methods/random-survival-forest.md) · [rna-seq](methods/rna-seq.md) · [rrbs](methods/rrbs.md) · [scrna-seq](methods/scrna-seq.md) · [single-cell-genotyping](methods/single-cell-genotyping.md) · [snrna-seq](methods/snrna-seq.md) · [spatial-transcriptomics](methods/spatial-transcriptomics.md) · [targeted-dna-seq](methods/targeted-dna-seq.md) · [tcr-seq](methods/tcr-seq.md) · [volumetric-mri-segmentation](methods/volumetric-mri-segmentation.md) · [whole-exome-seq](methods/whole-exome-seq.md) · [whole-genome-seq](methods/whole-genome-seq.md) · [xgboost](methods/xgboost.md)

## Themes



---

## How to read a page

- **Paper pages** follow a fixed template — start with *TL;DR*, then *Cohort &
  data*, *Key findings*, *Clinical implications*, and *Limitations & open
  questions*. Every section cites back to the source PMID.
- **Entity pages** (genes, cancer types, drugs, etc.) aggregate everything the
  corpus says about that entity, with every claim tied to the paper it came
  from. If an entity has only one citing paper, the page will be short — that
  is expected.
- **Unverified flags.** When an entity couldn't be validated against OncoTree,
  HUGO, or cBioPortal's study/panel catalogs, its page carries an
  `unverified: true` flag. Treat those pages as provisional.

## About this site

This site is built from a Markdown vault that lives in a git repository. The
content is maintained by a small set of sub-agents (paper compiler, entity
writer, crosslinker, linter) that read raw paper text and write into the
wiki. The rendering, search, and navigation you see here are from
[Quarto](https://quarto.org/). For the full pipeline and engineering details,
see the [project repository](https://github.com/jim-bo/cbio-kb).
