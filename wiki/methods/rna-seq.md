---
name: RNA sequencing
slug: rna-seq
kind: method
canonical_source: 
unverified: true
tags: [transcriptomics, sequencing]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# RNA sequencing

## Overview

Bulk RNA sequencing of tumor (and where available matched normal) tissue for gene expression quantification, fusion detection, and downstream signature/classifier analysis.

## Used by

- [PMID:35927489](../papers/35927489.md) — RNA-seq on n=712 CLL samples (603 treatment-naive used for clustering); unsupervised clustering identified 8 robust expression clusters that are independent prognostic factors beyond IGHV/epitype [PMID:35927489](../papers/35927489.md).
- [PMID:36862133](../papers/36862133.md) — select targeted RNA sequencing alongside MSK-IMPACT in the Make-an-IMPACT program; detected actionable fusions including a PRDX1-NTRK1 fusion in histiocytosis only via targeted RNA-seq, plus MS4A6A-BRAF, DOCK8-BRAF, HLA-A-BRAF, and TFG-ALK [PMID:36862133](../papers/36862133.md).
- [PMID:37202560](../papers/37202560.md) — bulk RNA-seq on 348 AC-ICAM colon cancer tumor/normal pairs; underpins the ICR signature, ConsensusTME deconvolution, and CMS classification used for prognostic analysis [PMID:37202560](../papers/37202560.md).
- [PMID:27634761](../papers/27634761.md) — RNA-seq (platform-independent, multiple normalization schemes including RSEM, FPKM, RPKM, TPM) used as the sole molecular feature (~500 features for site of origin, ~200 for lineage) in the ATLAS tumor classification model; trained on 8,249 TCGA/CCLE samples and validated on 10,376 samples [PMID:27634761](../papers/27634761.md).
- [PMID:34433969](../papers/34433969.md) — mRNA-seq on 121 fresh-frozen meningiomas from the University Health Network Brain Tumor BioBank; integrated with WES, EPIC methylation array, and snRNA-seq to define four stable molecular groups [PMID:34433969](../papers/34433969.md).
- [PMID:38117484](../papers/38117484.md) — RNA-seq on 54 glioma patients in the GLASS International consortium; paired with 450K/EPIC methylation arrays and WES/WGS; identified [HOXD13](../genes/HOXD13.md) as master regulator of IDH-mutant astrocytoma progression [PMID:38117484](../papers/38117484.md).
- [PMID:38412093](../papers/38412093.md) — RNA-seq on 24 primary anaplastic thyroid carcinomas and 13 cell lines, integrated with TCGA PTC data [PMID:38412093](../papers/38412093.md).
- [PMID:38488813](../papers/38488813.md) — RNA-seq on 44 prostate cancer PDX models; paired with WGS (30X) and targeted sequencing for integrative multi-platform analysis; confirmed ETS fusion-driven expression changes [PMID:38488813](../papers/38488813.md).
- [PMID:38895302](../papers/38895302.md) — RNA-seq paired with WES using G&T-seq protocol on single-cell clones from normal skin melanocytes; supported mutation calling via RNA evidence and phasing [PMID:38895302](../papers/38895302.md).
- [PMID:30325352](../papers/30325352.md) — Illumina HiSeq 2500 RNA-seq (TruSeq Total Stranded RNA + Ribo-Zero) on 130 of 211 [NSCLC](../cancer_types/NSCLC.md) subjects; reads aligned to hg19 with STAR v2.3, quantified with Cufflinks v2.0.2 in FPKM; RIN <2.5 excluded; part of the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) public radiogenomic resource [PMID:30325352](../papers/30325352.md).
- [PMID:39214094](../papers/39214094.md) — bulk RNA-seq on 100 upfront resected [PAAD](../cancer_types/PAAD.md) tumors (63 [KRAS](../genes/KRAS.md)^G12D^, 37 [KRAS](../genes/KRAS.md)^G12R^) from the Canadian COMPASS trial (NCT02750657) plus consortium-resected patients; aligned to GRCh38 via STAR; revealed [KRAS](../genes/KRAS.md)^G12D^ enrichment for EMT, mTORC1, and E2F/G2M Hallmarks versus [KRAS](../genes/KRAS.md)^G12R^ enrichment for NF-κB/TNFα signaling [PMID:39214094](../papers/39214094.md).
- [PMID:39305899](../papers/39305899.md) — bulk RNA-seq (KAPA Hyper Prep, NovaSeq6000, STAR, GRCh38.108) on sarcoma specimens from the UCLA biobank (194 total, subset sequenced); deposited on Synapse (PDTOSarcoma); used alongside WGS and targeted DNA panel sequencing to characterize 24 bone and soft-tissue sarcoma subtypes [PMID:39305899](../papers/39305899.md).
- [PMID:39753968](../papers/39753968.md) — bulk RNA-seq applied to 11 MAPK-WT [PAAD](../cancer_types/PAAD.md) tumors for fusion discovery (FusionCatcher v1.20 + Arriba v2.1.0); also used for the COMPASS trial transcriptomics arm referenced within the study; identified activating [BRAF](../genes/BRAF.md) and [NRG1](../genes/NRG1.md) fusions in 2/11 MAPK-WT tumors [PMID:39753968](../papers/39753968.md).
- rRNA-depletion RNA-seq applied to breast cancer primaries and metastases (AURORA cohort); expression subtype switching detected in 13/39 (33%) of paired cases; basal-like was the most stable subtype (15/16 concordant) [PMID:36585450](../papers/36585450.md)
- Performed on one sample per MEC patient for fusion validation; confirmed [EWSR1](../genes/EWSR1.md)::[KLF15](../genes/KLF15.md) fusion (Patient 2) and novel [ASCC2](../genes/ASCC2.md)::[GGNBP2](../genes/GGNBP2.md) fusion (Patient 1) [PMID:36577525](../papers/36577525.md)
- Total RNA-seq (Illumina TruSeq RiboZero Gold on HiSeq 4000) performed on 176 of 218 metastatic UC patients in UC-GENOME; enabled molecular subtyping and immune cell deconvolution (CIBERSORTx) [PMID:36333289](../papers/36333289.md)
- Used to sequence transcriptomes of 113 additional NHL cases (DLBCL and [FL](../cancer_types/FL.md)) in the BCGSC study; provided mutation calls and expression data complementing WGS/WES in 14 matched pairs [PMID:21796119](../papers/21796119.md)
- Bulk RNA-seq used across [SCLC](../cancer_types/SCLC.md) and [LUAD](../cancer_types/LUAD.md) cell lines (CCLE/DepMap) to characterize [ARID1A](../genes/ARID1A.md) expression levels and correlate with JQ1 sensitivity; [SCLC](../cancer_types/SCLC.md) lines showed markedly higher [ARID1A](../genes/ARID1A.md) expression than [LUAD](../cancer_types/LUAD.md) lines (p < 0.0001) [PMID:22037554](../papers/22037554.md)
- Bulk RNA-seq used across 14 ccRCC cohorts (n=3,621) to define HiTME molecular subtypes and train ICI/TKI response prediction models; WU-RCC independent validation cohort included 157 samples with bulk RNA-seq [PMID:22138691](../papers/22138691.md)
- Used alongside WES in breast cancer to detect splice-site consequences of [SF3B1](../genes/SF3B1.md) mutations and quantify allele-specific expression [PMID:22158541](../papers/22158541.md)
- RNA-seq applied alongside WGS in BCCRC breast tumor cohort to characterize transcriptomic landscape [PMID:22495314](../papers/22495314.md)
- RNA-seq used in [HCC](../cancer_types/HCC.md) studies to characterize hepatocellular carcinoma transcriptome alongside WGS [PMID:22634756](../papers/22634756.md)
- Strand-specific high-coverage RNA sequencing performed on 28 pediatric medulloblastoma cases (ICGC); identified first medulloblastoma fusion transcripts (DNAJB6-SHH, LCLAT1-ERBB4); only 48% of non-synonymous DNA mutations detectable at RNA level [PMID:22832583](../papers/22832583.md)
- Applied to Genentech colorectal cohort to detect RSPO2/RSPO3 fusion transcripts and characterise expression profiles [PMID:22895193](../papers/22895193.md)
- Used in CLCGP [SCLC](../cancer_types/SCLC.md) study (29 tumors) to complement WES/WGS and characterise transcriptome of TP53/RB1-deficient tumors [PMID:22941188](../papers/22941188.md)
- Applied in JHU [SCLC](../cancer_types/SCLC.md) study (36 tumors) to validate [SOX2](../genes/SOX2.md) and [MYCL](../genes/MYCL.md) amplification at the transcriptional level [PMID:22941189](../papers/22941189.md)
- Used in TCGA [LUSC](../cancer_types/LUSC.md) study (178 tumors) for expression profiling alongside WES to characterise the CDKN2A/TP53/KEAP1/NFE2L2 mutational landscape [PMID:22960745](../papers/22960745.md)
- RNA-seq profiling of 510 breast tumors enabled mRNA subtype classification and identified outlier expression events in known cancer genes [PMID:23000897](../papers/23000897.md)
- RNA-seq used in neuroblastoma study to detect gene fusions and outlier expression; confirmed [ALK](../genes/ALK.md) overexpression in cases lacking [ALK](../genes/ALK.md) point mutations [PMID:23334666](../papers/23334666.md)
- RNA-seq performed on 20 prostate tumors with matched benign prostate tissue (16 matched cases) as part of the WGS chromoplexy characterization study [PMID:23622249](../papers/23622249.md)
- RNA-seq performed on 179 of 200 [AML](../cancer_types/AML.md) samples in TCGA [AML](../cancer_types/AML.md) analysis; used for de novo assembly identifying 118 fusions in 80 samples and NMF consensus clustering yielding 7 expression groups [PMID:23634996](../papers/23634996.md)
- RNA-seq applied to 333 endometrial carcinoma tumors; combined with microRNA-seq, RPPA, and DNA-methylation for iCluster and consensus clustering defining four molecular subtypes [PMID:23636398](../papers/23636398.md)
- Used in TCGA [CCRCC](../cancer_types/CCRCC.md) study for transcriptome profiling; multi-platform integration with WES, copy-number arrays, methylation, miRNA-seq, and RPPA identified four mRNA expression subtypes (m1-m4) with distinct genomic correlates and survival differences [PMID:23792563](../papers/23792563.md)
- Applied in 73/96 pediatric pilocytic astrocytoma cases (ICGC cohort) for matched RNA sequencing alongside WGS; used for fusion discovery via TopHat-Fusion and deFuse, identifying novel [NTRK2](../genes/NTRK2.md) fusions ([QKI](../genes/QKI.md):[NTRK2](../genes/NTRK2.md), [NACC2](../genes/NACC2.md):[NTRK2](../genes/NTRK2.md)) and novel [BRAF](../genes/BRAF.md) fusion partners [PMID:23817572](../papers/23817572.md)
- Applied to 164 [GBM](../cancer_types/GBM.md) transcriptomes; analyzed with PRADA to detect fusion transcripts (228 total in 106/164 samples) including recurrent EGFR-SEPT14, FGFR3-TACC3, and [PDGFRA](../genes/PDGFRA.md) intragenic splice variants [PMID:24120142](../papers/24120142.md)
- Applied to 42 TCC bladder tumors with 16 matched normal bladder tissues; detected FGFR3-TACC3 in-frame fusion in 2/42 (5%) cases with outlier [TACC3](../genes/TACC3.md) expression [PMID:24121792](../papers/24121792.md)
- Performed alongside whole-genome sequencing (STAR hg38 alignment + RSEM quantification) for 28 metastatic NENs in the BC Cancer POG program; expression data drove 6 of 10 clinical benefit outcomes through independent transcriptome-based therapy recommendations [PMID:24326773](../papers/24326773.md).
- Used to validate aberrant splicing in grade II glioma, including confirmation of [RB1](../genes/RB1.md) c.2520+1G>A splice-site mutation-driven premature termination and loss of growth-suppression domain in a TMZ-treated hypermutated recurrence [PMID:24336570](../papers/24336570.md)
- PolyA RNA-seq on Illumina HiSeq2000 (100 bp PE) applied to 80 rhabdomyosarcoma tumors; mapped with TopHat2; fusions called via [tophat-fusion](../methods/tophat-fusion.md) and deFuse; showed 58% of DNA-level somatic mutations had RNA expression evidence; identified cryptic PAX rearrangements including PAX3-INO80D [PMID:24436047](../papers/24436047.md)
- Applied to all 131 TCGA bladder carcinoma tumors (n=129 for mRNA clustering); miRNA-seq also performed; identified 4 mRNA expression clusters including papillary-like (cluster I, enriched for [FGFR3](../genes/FGFR3.md) mutations) and basal/squamous-like (cluster III, expressing KRT14/KRT5/EGFR); viral integration transcripts detected in 5/122 [PMID:24476821](../papers/24476821.md)
- Performed on 4 of the 20 Discovery Cohort [ESCC](../cancer_types/ESCC.md) tumors to support transcriptomic analysis of mutated genes (e.g., [APOBEC3B](../genes/APOBEC3B.md) expression, [XPO1](../genes/XPO1.md) mRNA levels) [PMID:24686850](../papers/24686850.md)
- Applied to 196 [HCC](../cancer_types/HCC.md) patients as part of the TCGA integrated molecular characterisation (DNA copy number, methylation, mRNA, miRNA, RPPA) [PMID:24798001](../papers/24798001.md)
- Transcriptome RNA-seq performed on 25 thymic epithelial tumors (Illumina Genome Analyzer II / HiSeq2000) using TopHat + Cufflinks; identified [BCL2](../genes/BCL2.md) focal amplification correlated with increased [BCL2](../genes/BCL2.md) mRNA; both [GTF2I](../genes/GTF2I.md) alleles expressed (mean mutant allele fraction 47%) [PMID:24974848](../papers/24974848.md)
- Used for bulk RNA-seq of primary human gallbladder fibroblasts (GFs) cultured on 0.5 vs 16 kPa silicon hydrogels (NCBI SRA PRJNA1182410), identifying [SEMA7A](../genes/SEMA7A.md) as the most strongly upregulated semaphorin under stiff matrix conditions in [GBC](../cancer_types/GBC.md) stroma [PMID:24997986](../papers/24997986.md)
- Six-platform TCGA profiling of 295 gastric adenocarcinomas ([stad_tcga_pub](../datasets/stad_tcga_pub.md)) included mRNA-seq (RNA-seq) to define transcriptional subtypes and pathway activity across EBV, MSI, GS, and CIN molecular subgroups [PMID:25079317](../papers/25079317.md)
- Multi-platform TCGA profiling of 230 lung adenocarcinomas ([luad_tcga_pub](../datasets/luad_tcga_pub.md)) included mRNA sequencing to identify transcriptional subtypes (TRU, PI, PP) and [MET](../genes/MET.md) exon 14 skipping events [PMID:25079552](../papers/25079552.md)
- Used in TCGA ChRCC project (66 tumors) to profile gene expression, identify distal-nephron cell-of-origin signatures, characterize mtDNA-mutant transcriptomes, and assess [TERT](../genes/TERT.md) expression levels. [PMID:25155756](../papers/25155756.md)
- Used on Illumina HiSeq 2500 (GEO GSE272957) to profile transcriptomes of EWS::FLI1-transduced heMSCs vs controls, identifying 3,836 DEGs and Ewing sarcoma gene-expression signatures. [PMID:25186949](../papers/25186949.md)
- Used on Illumina HiSeq to profile seven prostate cancer organoid lines; identified TMPRSS2-ERG fusion status, [SPINK1](../genes/SPINK1.md) overexpression, and confirmed gene-expression concordance between organoids and parental tumor tissue. [PMID:25201530](../papers/25201530.md)
- Used in [MPNST](../cancer_types/MPNST.md) discovery cohort (15 tumors, 51 bp PE, Illumina HiSeq-2500, hg19, STAR v2.3); RNA-seq was essential to detect [SUZ12](../genes/SUZ12.md) structural rearrangements missed by WES, and revealed 455/479 differentially expressed genes upregulated in PRC2-loss tumors [PMID:25240281](../papers/25240281.md)
- Applied to 159 nccRCC tumors (TruSeq, HiSeq 2000, ~68M PE reads/sample); enabled a 5-gene classifier (ASB1, GLYAT, PDZK1IP1, PLCG2, SDCBP2) achieving 95.3% subtype accuracy and detection of novel ACTG1-MITF and CLTC-TFEB fusions [PMID:25401301](../papers/25401301.md)
- Used in TCGA papillary thyroid carcinoma ([THPA](../cancer_types/THPA.md)) multiplatform study to derive BRAFV600E-RAS Score (BRS) from a 71-gene expression signature and Thyroid Differentiation Score (TDS) from 16 metabolism genes, enabling molecular reclassification of 496 PTCs [PMID:25417114](../papers/25417114.md)
- Applied to 279 [HNSC](../cancer_types/HNSC.md) tumors for HPV status determination (E6/E7 read mapping; threshold >1,000 reads) and expression subtype classification (atypical/mesenchymal/basal/classical), as well as structural variant detection including [MET](../genes/MET.md) exon-14 skipping [PMID:25631445](../papers/25631445.md)
- Paired-end RNA-seq (Illumina HiSeq 2500, 2×100 nt, ~50M paired reads) performed on 150 mCRPC biopsies alongside WES, enabling fusion detection via Tophat-Fusion and FPKM quantification by Cufflinks. [PMID:26000489](../papers/26000489.md)
- mRNA sequencing (Illumina TruSeq, HiSeq 2000) on 331 melanoma samples enabled identification of three transcriptomic subclasses (Immune, Keratin, MITF-low) and 224 candidate fusion drivers. [PMID:26091043](../papers/26091043.md)
- RNA-seq used for transcriptome profiling in breast cancer genomic analysis [PMID:26168399](../papers/26168399.md)
- RNA-seq used for transcriptome profiling as part of multi-omic characterization of ovarian cancer [PMID:26200345](../papers/26200345.md)
- Used in 40-42 of 110 metastatic melanoma pretreatment tumors ([skcm_dfci_2015](../datasets/skcm_dfci_2015.md)) to measure cytolytic activity ([GZMA](../genes/GZMA.md)+[PRF1](../genes/PRF1.md) geometric mean) and immune checkpoint expression ([CTLA4](../genes/CTLA4.md), [PDCD1LG2](../genes/PDCD1LG2.md)); each independently associated with [ipilimumab](../drugs/ipilimumab.md) clinical benefit [PMID:26359337](../papers/26359337.md)
- Performed on 35 AAV-CRISPR-edited rat mammary tumors across six genotype groups; ANOVA (FDR<1%) identified 1,579 differentially expressed genes; intrinsic subtype assignment classified most tumors as Luminal A or B; GSEA of fulvestrant-responsive DEGs showed significant concordance with human patient neoadjuvant endocrine therapy datasets [PMID:26437033](../papers/26437033.md)
- Used in the TCGA breast ILC/IDC multi-platform study (n=817) for mRNA expression profiling; enabled definition of three [ILC](../cancer_types/ILC.md) transcriptional subtypes (reactive-like, immune-related, proliferative) and orthogonal validation of mutation calls (78.1% of CLL gene mutations detected at sites with >90% detection power) [PMID:26451490](../papers/26451490.md)
- Performed on neuroblastoma tumors (Illumina HiSeq 2000) alongside custom 4x44K Agilent oligonucleotide microarrays; quantified [TERT](../genes/TERT.md) expression showing 92-fold higher levels in TERT-rearranged vs low-risk tumors and higher than MYCN-amplified tumors (P=0.028) [PMID:26466568](../papers/26466568.md)
- Used in 156 of 538 CLL whole-exome samples for orthogonal validation; 78.1% of CLL gene mutations detected in matched RNA-seq at sites with >90% detection power; MGA-mutant CLLs showed downregulation of MYC-suppressed B-cell gene sets [PMID:26466571](../papers/26466571.md)
- Profiled mRNA expression in 333 primary prostate adenocarcinomas (TCGA) as part of multi-platform characterization; 19 matched non-malignant adjacent samples profiled for methylation and RNA/miRNA expression [PMID:26544944](../papers/26544944.md).
- TruSeq Stranded Total RNA, 100 bp paired-end, ≥50 M reads applied to 30 periampullary tumors (28 AMPAC + 2 DUOAC) to characterize WNT-pathway transcriptional dysregulation [PMID:26804919](../papers/26804919.md)
- Applied to 1,045 diffuse gliomas in the TCGA pan-glioma study; TERT mRNA quantified as a 91% sensitive / 95% specific surrogate for TERTp mutation status; also used for LGr1–4 expression cluster derivation [PMID:26824661](../papers/26824661.md)
- Used alongside WGS and ChIP-seq in adenoid cystic carcinoma (ACC) primagrafts and primary tumors to characterize MYB-driven transcriptional programs and the BRD4 super-enhancer landscape [PMID:26829750](../papers/26829750.md)
- TruSeq, HiSeq 2500, 2×75 bp paired-end applied to 49 metastatic CRPC specimens (Adeno + NE) to identify the 70-gene NEPC classifier and characterize EZH2/PRC2 target dysregulation [PMID:26855148](../papers/26855148.md)
- Illumina HiSeq 2000, ≥50M paired 100×100 bp reads applied to 17 adenoid cystic carcinoma (ACC) tumors; NFIB overexpression confirmed independent of fusion status (p=0.002 vs normal tissue); quantification by RSEM [PMID:26862087](../papers/26862087.md)
- Applied to 40 MRT cases plus 3 hESC lines (with 4 fetal cerebellum normals); NMF on top-25% most-variable protein-coding genes identified 2 mRNA sub-groups recapitulating the AT/RT vs RTK distinction, with organ site associated with sub-group 1 (all 6 extra-renal cases; Fisher p=0.04). [PMID:26977886](../papers/26977886.md)
- Performed on 28-tumor subset of anti-PD-1-treated metastatic melanomas to identify the IPRES transcriptional resistance program via GSVA/GSEA enrichment analysis [PMID:26997480](../papers/26997480.md)
- Performed on 495 lung ADC and 476 lung SqCC samples; used for fusion calling via PRADA and for mutational-signature transcriptional cross-validation in the NSCLC landscape study [PMID:27158780](../papers/27158780.md)
- Applied on 7 uRCC tumours (4 NF2-loss, 3 NF2-WT) using Illumina HiSeq 2500, with STAR alignment, to evaluate YAP/TAZ transcriptional signatures via GSEA. [PMID:27713405](../papers/27713405.md)
- Transcriptome sequencing (RNA-seq) on N=54 cases used to characterize the DUX4/ERG B-ALL subtype; identified ERGalt from a novel non-canonical first exon and distinguished this subtype from other B-ALL classes. [PMID:27776115](../papers/27776115.md)
- Used as tumor transcriptome profiling (TruSeq Stranded Total RNA LT) in the PIPseq program; RNA-seq independently contributed ~40% of clinically impactful findings including fusion detection, BCR-ABL1-like signature identification, and expression-based subtyping across 65 pediatric patients [PMID:28007021](../papers/28007021.md).
- Used for mRNA profiling of 164 oesophageal carcinomas and 359 gastric adenocarcinomas in the TCGA esophageal/stomach study; mRNA-seq confirmed no HPV transcripts in ESCC and provided expression data for iCluster integrative subtyping [PMID:28052061](../papers/28052061.md).
- Applied to 173 PCPG tumors in the TCGA PCPG study; mRNA-seq revealed four molecular subtypes (kinase signaling, pseudohypoxia, Wnt-altered, cortical admixture) and confirmed CSDE1 splice-site mutation effects via intron retention and exon skipping [PMID:28162975](../papers/28162975.md).
- Used RNA-seq to profile transcriptional changes in tumor models [PMID:28196596](../papers/28196596.md)
- Employed RNA-seq for transcriptome profiling in sarcoma tumor samples [PMID:28199314](../papers/28199314.md)
- Used RNA-seq for transcriptome profiling and fusion detection in cancer specimens [PMID:28373299](../papers/28373299.md)
- Poly(A)+ transcriptomes generated for 164 medulloblastoma cases; recurrent fusions targeting GLI2, PTEN, and PVT1 identified by integrating SV breakpoints with RNA-seq data [PMID:28726821](../papers/28726821.md)
- Poly(A)+ and exome-capture transcriptomes generated for 868 libraries from 496 MET500 metastatic tumors (40–50M paired reads on Illumina HiSeq 2000/2500); enabled fusion calling (CODAC), immune deconvolution, and MImmScore derivation [PMID:28783718](../papers/28783718.md)
- Applied to NOL10-knockdown LNCaP cells to identify 71 downregulated cell-cycle genes (DLGAP5, MCM4, KIF20B, DIAPH3, SUV39H1, CENPE, GINS2, HMGB3, CDC6); also used for GSEA and eQTL/sQTL analyses across CPGEA and TCGA PRAD cohorts [PMID:28927585](../papers/28927585.md)
- Performed on 775 DLBCL cases (625 used in core analysis) for cell-of-origin assignment (ABC vs GCB) and integrated prognostic modeling [PMID:28985567](../papers/28985567.md)
- Performed on 408/412 BLCA tumors enabling five mRNA expression subtype classification (luminal-papillary, luminal-infiltrated, luminal, basal-squamous, neuronal) with subtype-associated survival p=4×10⁻⁴ [PMID:28988769](../papers/28988769.md)
- Performed on 45 baseline and 26 paired pre/on-therapy melanoma biopsies (STAR-aligned, hg19); 189 pre-therapy DEGs distinguished CR/PR from PD and 475 on-therapy DEGs captured pharmacodynamic immune response to nivolumab [PMID:29033130](../papers/29033130.md)
- Performed on 206 TCGA sarcomas; revealed that UPS and MFS are transcriptomically indistinguishable and identified miR-181b-5p as an independent recurrence-free survival predictor in LMS (HR=7.4, p=9×10⁻⁶) [PMID:29100075](../papers/29100075.md)
- Performed on 18 PBRM1-LOF vs. 14 PBRM1-intact pre-treatment [CCRCC](../cancer_types/CCRCC.md) tumors; GSEA confirmed up-regulation of hypoxia and IL6/JAK-STAT3 gene sets in PBRM1-deficient tumors [PMID:29301960](../papers/29301960.md)
- RNA-seq fusion calling across 9,624 TCGA tumor samples and 713 normal samples (33 cancer types) using STAR-Fusion, EricScript, and BREAKFAST pipelines; GRCh38 reference; yielded 25,664 filtered fusions [PMID:29617662](../papers/29617662.md)
- HiSeq 2500 PE100 RNA-seq performed on AALE chr_3p-deleted cells; processed via STAR + RSEM + edgeR for differential expression analysis [PMID:29622463](../papers/29622463.md)

## Notes

- In the CLL-map study, RNA-seq is one arm of an integrated WES/WGS + RNA-seq + methylation analysis used to derive an integrated outcome model [PMID:35927489](../papers/35927489.md).
- In the AC-ICAM atlas, RNA-seq drives both immune signature scoring and downstream microbiome integration [PMID:37202560](../papers/37202560.md).
- In the [NSCLC](../cancer_types/NSCLC.md) radiogenomics dataset, RNA-seq (n=130) complements CT/PET-CT imaging and SNaPshot mutational testing for EGFR/KRAS/ALK, with 17 subjects having both RNA-seq and microarray expression data [PMID:30325352](../papers/30325352.md).

## Sources

- [PMID:35927489](../papers/35927489.md)
- [PMID:36862133](../papers/36862133.md)
- [PMID:37202560](../papers/37202560.md)
- [PMID:27634761](../papers/27634761.md)
- [PMID:34433969](../papers/34433969.md)
- [PMID:38117484](../papers/38117484.md)
- [PMID:38412093](../papers/38412093.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:38895302](../papers/38895302.md)
- [PMID:30325352](../papers/30325352.md)
- [PMID:39214094](../papers/39214094.md)
- [PMID:39305899](../papers/39305899.md)
- [PMID:39753968](../papers/39753968.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36585450](../papers/36585450.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36333289](../papers/36333289.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:21796119](../papers/21796119.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22037554](../papers/22037554.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22138691](../papers/22138691.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22158541](../papers/22158541.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22495314](../papers/22495314.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22634756](../papers/22634756.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22832583](../papers/22832583.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22895193](../papers/22895193.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22941188](../papers/22941188.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22941189](../papers/22941189.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23000897](../papers/23000897.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23622249](../papers/23622249.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23634996](../papers/23634996.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23636398](../papers/23636398.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23792563](../papers/23792563.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23817572](../papers/23817572.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24120142](../papers/24120142.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24121792](../papers/24121792.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24326773](../papers/24326773.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24686850](../papers/24686850.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24798001](../papers/24798001.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24974848](../papers/24974848.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24997986](../papers/24997986.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25155756](../papers/25155756.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25186949](../papers/25186949.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25201530](../papers/25201530.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25240281](../papers/25240281.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25631445](../papers/25631445.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26000489](../papers/26000489.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26168399](../papers/26168399.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26200345](../papers/26200345.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26359337](../papers/26359337.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26466568](../papers/26466568.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26466571](../papers/26466571.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26829750](../papers/26829750.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26855148](../papers/26855148.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26862087](../papers/26862087.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26977886](../papers/26977886.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26997480](../papers/26997480.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27776115](../papers/27776115.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28007021](../papers/28007021.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28162975](../papers/28162975.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28196596](../papers/28196596.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28199314](../papers/28199314.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28726821](../papers/28726821.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28783718](../papers/28783718.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28985567](../papers/28985567.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29301960](../papers/29301960.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
