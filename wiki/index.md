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
| [Papers](#papers) | 21 | Per-publication summaries: cohort, methods, findings, citations |
| [Genes](#genes) | 143 | Alterations, co-occurrence, therapeutic relevance across the corpus |
| [Cancer types](#cancer-types) | 47 | OncoTree-anchored disease pages linking studies and alterations |
| [Datasets](#datasets) | 24 | cBioPortal studies with cohort details and linked publications |
| [Drugs](#drugs) | 37 | Targeted therapies, resistance patterns, evidence in the corpus |
| [Methods](#methods) | 33 | Sequencing assays, gene panels, and analytical pipelines |
| [Themes](#themes) | 0 | Cross-cutting syntheses (in progress) |

## Papers

- [25730765](papers/25730765.md) — The landscape of somatic mutations in Infant MLL rearranged acute lymphoblastic leukemias
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
- [37477937](papers/37477937.md) — Novel Genomic Risk Stratification Model for Primary Gastrointestinal Stromal Tumors (GIST) in the Adjuvant Therapy Era
- [37591896](papers/37591896.md) — Genomic analysis and clinical correlations of non-small cell lung cancer brain metastasis
- [37682528](papers/37682528.md) — Clinical and Genomic Landscape of FGFR3-Altered Urothelial Carcinoma and Treatment Outcomes with Erdafitinib: A Real-World Experience
- [37910594](papers/37910594.md) — Tumor Volume Growth Rates and Doubling Times during Active Surveillance of IDH-mutant Low-Grade Glioma
- [38147626](papers/38147626.md) — High-risk and silent clonal hematopoietic genotypes in patients with nonhematologic cancer
- [38864854](papers/38864854.md) — A Novel Approach to Quantify Heterogeneity of Intrahepatic Cholangiocarcinoma: the Hidden-Genome Classifier
- [38995739](papers/38995739.md) — A Phase II study assessing Long-Term Response to Ibrutinib Monotherapy in recurrent or refractory CNS Lymphoma
- [39214094](papers/39214094.md) — Distinct clinical outcomes and biological features of specific KRAS mutants in human pancreatic cancer
- [39289779](papers/39289779.md) — Real-world experience with circulating tumor DNA in cerebrospinal fluid from patients with central nervous system tumors
- [39506116](papers/39506116.md) — Automated real-world data integration improves cancer outcome prediction

## Genes

[AKT1](genes/AKT1.md) · [ALK](genes/ALK.md) · [ARID1A](genes/ARID1A.md) · [ASXL1](genes/ASXL1.md) · [ATM](genes/ATM.md) · [ATRX](genes/ATRX.md) · [B2M](genes/B2M.md) · [BCL2](genes/BCL2.md) · [BCL7A](genes/BCL7A.md) · [BRAF](genes/BRAF.md) · [CARD11](genes/CARD11.md) · [CCL5](genes/CCL5.md) · [CD274](genes/CD274.md) · [CD79B](genes/CD79B.md) · [CD8A](genes/CD8A.md) · [CD8B](genes/CD8B.md) · [CDK4](genes/CDK4.md) · [CDKN1A](genes/CDKN1A.md) · [CDKN2A](genes/CDKN2A.md) · [CDKN2B](genes/CDKN2B.md) · [CIC](genes/CIC.md) · [CREBBP](genes/CREBBP.md) · [CRKL](genes/CRKL.md) · [CSF1R](genes/CSF1R.md) · [CTLA4](genes/CTLA4.md) · [CXCL10](genes/CXCL10.md) · [CXCL9](genes/CXCL9.md) · [DICER1](genes/DICER1.md) · [DIS3](genes/DIS3.md) · [DNMT3A](genes/DNMT3A.md) · [EGFR](genes/EGFR.md) · [EML4](genes/EML4.md) · [ERBB2](genes/ERBB2.md) · [FAT1](genes/FAT1.md) · [FGFR1](genes/FGFR1.md) · [FGFR2](genes/FGFR2.md) · [FGFR3](genes/FGFR3.md) · [FLT3](genes/FLT3.md) · [FLT4](genes/FLT4.md) · [FOXA1](genes/FOXA1.md) · [FOXO1](genes/FOXO1.md) · [FOXP3](genes/FOXP3.md) · [FUBP1](genes/FUBP1.md) · [GNA13](genes/GNA13.md) · [GNAS](genes/GNAS.md) · [GNLY](genes/GNLY.md) · [GZMA](genes/GZMA.md) · [GZMB](genes/GZMB.md) · [GZMH](genes/GZMH.md) · [H3-3A](genes/H3-3A.md) · [HLA-B](genes/HLA-B.md) · [HRAS](genes/HRAS.md) · [IDH1](genes/IDH1.md) · [IDH2](genes/IDH2.md) · [IDO1](genes/IDO1.md) · [IFNG](genes/IFNG.md) · [IL12B](genes/IL12B.md) · [IL4R](genes/IL4R.md) · [INO80](genes/INO80.md) · [IRF1](genes/IRF1.md) · [ITPKB](genes/ITPKB.md) · [JAK2](genes/JAK2.md) · [KDM6A](genes/KDM6A.md) · [KDR](genes/KDR.md) · [KEAP1](genes/KEAP1.md) · [KIAA1549](genes/KIAA1549.md) · [KIT](genes/KIT.md) · [KMT2A](genes/KMT2A.md) · [KMT2C](genes/KMT2C.md) · [KMT2D](genes/KMT2D.md) · [KRAS](genes/KRAS.md) · [MAP2K1](genes/MAP2K1.md) · [MAP2K2](genes/MAP2K2.md) · [MAX](genes/MAX.md) · [MDM2](genes/MDM2.md) · [MED12](genes/MED12.md) · [MET](genes/MET.md) · [MGA](genes/MGA.md) · [MSL3](genes/MSL3.md) · [MYC](genes/MYC.md) · [MYCN](genes/MYCN.md) · [MYD88](genes/MYD88.md) · [MYOD1](genes/MYOD1.md) · [NF1](genes/NF1.md) · [NFKB1](genes/NFKB1.md) · [NFKBIE](genes/NFKBIE.md) · [NKX2-1](genes/NKX2-1.md) · [NKX3-1](genes/NKX3-1.md) · [NOTCH1](genes/NOTCH1.md) · [NOTCH3](genes/NOTCH3.md) · [NRAS](genes/NRAS.md) · [NT5C2](genes/NT5C2.md) · [NTRK1](genes/NTRK1.md) · [PAX3](genes/PAX3.md) · [PAX7](genes/PAX7.md) · [PDCD1](genes/PDCD1.md) · [PDGFRA](genes/PDGFRA.md) · [PIK3CA](genes/PIK3CA.md) · [PIK3R1](genes/PIK3R1.md) · [PLCG1](genes/PLCG1.md) · [PRF1](genes/PRF1.md) · [PTEN](genes/PTEN.md) · [PTPN1](genes/PTPN1.md) · [PTPN11](genes/PTPN11.md) · [PTPRB](genes/PTPRB.md) · [PTPRD](genes/PTPRD.md) · [PTPRT](genes/PTPRT.md) · [RB1](genes/RB1.md) · [RET](genes/RET.md) · [RFX7](genes/RFX7.md) · [RHOA](genes/RHOA.md) · [RICTOR](genes/RICTOR.md) · [ROS1](genes/ROS1.md) · [RRM1](genes/RRM1.md) · [RUNX1](genes/RUNX1.md) · [SDHA](genes/SDHA.md) · [SDHB](genes/SDHB.md) · [SETD2](genes/SETD2.md) · [SF3B1](genes/SF3B1.md) · [SMAD4](genes/SMAD4.md) · [SMARCA4](genes/SMARCA4.md) · [SOCS1](genes/SOCS1.md) · [STAT1](genes/STAT1.md) · [STAT3](genes/STAT3.md) · [STAT6](genes/STAT6.md) · [STK11](genes/STK11.md) · [SUZ12](genes/SUZ12.md) · [TACC3](genes/TACC3.md) · [TBL1XR1](genes/TBL1XR1.md) · [TBX21](genes/TBX21.md) · [TEK](genes/TEK.md) · [TERT](genes/TERT.md) · [TET2](genes/TET2.md) · [TMSB4X](genes/TMSB4X.md) · [TNFAIP3](genes/TNFAIP3.md) · [TP53](genes/TP53.md) · [TP63](genes/TP63.md) · [TRAF3](genes/TRAF3.md) · [TSC1](genes/TSC1.md) · [USP8](genes/USP8.md) · [XPO1](genes/XPO1.md) · [ZC3H18](genes/ZC3H18.md) · [ZFP36L1](genes/ZFP36L1.md)

## Cancer types

[ACYC](cancer_types/ACYC.md) · [AITL](cancer_types/AITL.md) · [ALCL](cancer_types/ALCL.md) · [ALCLALKN](cancer_types/ALCLALKN.md) · [ALCLALKP](cancer_types/ALCLALKP.md) · [ANGS](cancer_types/ANGS.md) · [APAD](cancer_types/APAD.md) · [ARMS](cancer_types/ARMS.md) · [AST](cancer_types/AST.md) · [BLCA](cancer_types/BLCA.md) · [BLLKMT2A](cancer_types/BLLKMT2A.md) · [BRCA](cancer_types/BRCA.md) · [CHL](cancer_types/CHL.md) · [CLLSLL](cancer_types/CLLSLL.md) · [COAD](cancer_types/COAD.md) · [COADREAD](cancer_types/COADREAD.md) · [DIFG](cancer_types/DIFG.md) · [DLBCLNOS](cancer_types/DLBCLNOS.md) · [EATL](cancer_types/EATL.md) · [ECD](cancer_types/ECD.md) · [EHCH](cancer_types/EHCH.md) · [ERMS](cancer_types/ERMS.md) · [GBC](cancer_types/GBC.md) · [GIST](cancer_types/GIST.md) · [HCC](cancer_types/HCC.md) · [IHCH](cancer_types/IHCH.md) · [LCH](cancer_types/LCH.md) · [LUAD](cancer_types/LUAD.md) · [LUSC](cancer_types/LUSC.md) · [MBL](cancer_types/MBL.md) · [MEITL](cancer_types/MEITL.md) · [MEL](cancer_types/MEL.md) · [MFH](cancer_types/MFH.md) · [MGCT](cancer_types/MGCT.md) · [MPNST](cancer_types/MPNST.md) · [NSCLC](cancer_types/NSCLC.md) · [ODG](cancer_types/ODG.md) · [OGCT](cancer_types/OGCT.md) · [OS](cancer_types/OS.md) · [PAAD](cancer_types/PAAD.md) · [PCNSL](cancer_types/PCNSL.md) · [PRAD](cancer_types/PRAD.md) · [PTCL](cancer_types/PTCL.md) · [RMS](cancer_types/RMS.md) · [SCRMS](cancer_types/SCRMS.md) · [TLL](cancer_types/TLL.md) · [UTUC](cancer_types/UTUC.md)

## Datasets

[all_stjude_2015](datasets/all_stjude_2015.md) · [appendiceal_msk_2022](datasets/appendiceal_msk_2022.md) · [bladder_msk_2023](datasets/bladder_msk_2023.md) · [bm_nsclc_mskcc_2023](datasets/bm_nsclc_mskcc_2023.md) · [chl_sccc_2023](datasets/chl_sccc_2023.md) · [cll_broad_2022](datasets/cll_broad_2022.md) · [coad_silu_2022](datasets/coad_silu_2022.md) · [coadread_tcga](datasets/coadread_tcga.md) · [csf_msk_2024](datasets/csf_msk_2024.md) · [difg_msk_2023](datasets/difg_msk_2023.md) · [gist_msk_2023](datasets/gist_msk_2023.md) · [hcc_msk_2024](datasets/hcc_msk_2024.md) · [luad_mskcc_2023_met_organotropism](datasets/luad_mskcc_2023_met_organotropism.md) · [makeanimpact_ccr_2023](datasets/makeanimpact_ccr_2023.md) · [msk_ch_2023](datasets/msk_ch_2023.md) · [msk_chord_2024](datasets/msk_chord_2024.md) · [msk_impact_2017](datasets/msk_impact_2017.md) · [mtnn_msk_2022](datasets/mtnn_msk_2022.md) · [nsclc_ctdx_msk_2022](datasets/nsclc_ctdx_msk_2022.md) · [pancreas_msk_2024](datasets/pancreas_msk_2024.md) · [pcawg](datasets/pcawg.md) · [pcnsl_msk_2024](datasets/pcnsl_msk_2024.md) · [rms_msk_2023](datasets/rms_msk_2023.md) · [sarcoma_msk_2023](datasets/sarcoma_msk_2023.md)

## Drugs

[alpelisib](drugs/alpelisib.md) · [bevacizumab](drugs/bevacizumab.md) · [brentuximab-vedotin](drugs/brentuximab-vedotin.md) · [capecitabine](drugs/capecitabine.md) · [capmatinib](drugs/capmatinib.md) · [cobimetinib](drugs/cobimetinib.md) · [crizotinib](drugs/crizotinib.md) · [cyclophosphamide](drugs/cyclophosphamide.md) · [dabrafenib](drugs/dabrafenib.md) · [doxorubicin](drugs/doxorubicin.md) · [enfortumab-vedotin](drugs/enfortumab-vedotin.md) · [erdafitinib](drugs/erdafitinib.md) · [erlotinib](drugs/erlotinib.md) · [etoposide](drugs/etoposide.md) · [fludarabine](drugs/fludarabine.md) · [fluorouracil](drugs/fluorouracil.md) · [ibrutinib](drugs/ibrutinib.md) · [imatinib](drugs/imatinib.md) · [infigratinib](drugs/infigratinib.md) · [irinotecan](drugs/irinotecan.md) · [lenalidomide](drugs/lenalidomide.md) · [leucovorin](drugs/leucovorin.md) · [methotrexate](drugs/methotrexate.md) · [osimertinib](drugs/osimertinib.md) · [oxaliplatin](drugs/oxaliplatin.md) · [pembrolizumab](drugs/pembrolizumab.md) · [prednisone](drugs/prednisone.md) · [sirolimus](drugs/sirolimus.md) · [temozolomide](drugs/temozolomide.md) · [temsirolimus](drugs/temsirolimus.md) · [tirabrutinib](drugs/tirabrutinib.md) · [trametinib](drugs/trametinib.md) · [trastuzumab](drugs/trastuzumab.md) · [vemurafenib](drugs/vemurafenib.md) · [venetoclax](drugs/venetoclax.md) · [vincristine](drugs/vincristine.md) · [vinorelbine](drugs/vinorelbine.md)

## Methods

[16s-rrna-seq](methods/16s-rrna-seq.md) · [450k-methylation-array](methods/450k-methylation-array.md) · [ACCESS129](methods/ACCESS129.md) · [IMPACT341](methods/IMPACT341.md) · [IMPACT410](methods/IMPACT410.md) · [IMPACT468](methods/IMPACT468.md) · [IMPACT505](methods/IMPACT505.md) · [archer-fusionplex](methods/archer-fusionplex.md) · [bayesian-nmf](methods/bayesian-nmf.md) · [clumps](methods/clumps.md) · [cms-classifier](methods/cms-classifier.md) · [consensus-tme](methods/consensus-tme.md) · [cosmx-smi](methods/cosmx-smi.md) · [ctdx-lung](methods/ctdx-lung.md) · [facets](methods/facets.md) · [fish](methods/fish.md) · [icr-signature](methods/icr-signature.md) · [igcaller](methods/igcaller.md) · [immunoediting-quantification](methods/immunoediting-quantification.md) · [joint-longitudinal-survival-model](methods/joint-longitudinal-survival-model.md) · [log-linear-mixed-effects-model](methods/log-linear-mixed-effects-model.md) · [msk-hemepact](methods/msk-hemepact.md) · [msk-impact-panel](methods/msk-impact-panel.md) · [nlp-prissmm](methods/nlp-prissmm.md) · [oncokb](methods/oncokb.md) · [phylogicndt](methods/phylogicndt.md) · [rna-seq](methods/rna-seq.md) · [rrbs](methods/rrbs.md) · [targeted-dna-seq](methods/targeted-dna-seq.md) · [tcr-seq](methods/tcr-seq.md) · [volumetric-mri-segmentation](methods/volumetric-mri-segmentation.md) · [whole-exome-seq](methods/whole-exome-seq.md) · [whole-genome-seq](methods/whole-genome-seq.md)

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
