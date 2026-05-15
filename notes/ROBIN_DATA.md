# ROBIN Batch: Public Methods & Datasets

This document tracks public code repositories, software methods, and datasets identified within the ROBIN citation batch.

## Summary Table

| PMID | Primary Focus | Code / Methods | Datasets / Repositories |
| :--- | :--- | :--- | :--- |
| **34493726** | Neuroblastoma scRNA-seq | `ws6/deindexer`, `jkrijthe/Rtsne`, `broadinstitute/inferCNV` | Synapse (syn22302605), TARGET-NBL (phs000467), SEQC-NB498 (GSE49710) |
| **27389358** | Neuroimaging Reproducibility | `poldrack/myconnectome-vm`, `incf/bids-validator` | FigShare, Dryad, DataVerse, OSF, FCP/INDI |
| **37119971** | Multi-Omics Profiling | `mikelove/awesome-multi-omics` | TCGA, CPTAC, GDC, Synapse |
| **26978244** | FAIR Guiding Principles | — | Zenodo, DataHub, DANS, EUDat, BioSharing |
| **29902176** | Cloud Computing | Cloud-native pipelines (AWS/NIH S3) | PCAWG (Pan-Cancer Analysis of Whole Genomes) |
| **33305538** | Medical Image Synthesis | CycleGAN, U-net, ResNet | Clinical trial synthetic CT datasets |
| **27806376** | Oligodendroglioma scRNA-seq | — | Gene Expression Omnibus (GEO) |

## Radiotherapy Coverage

This section details the availability of radiotherapy (RT) treatment data within the major Robin batch cohorts.

### SEQC-NB498 (`nb_seqc_utah_2015`)
*   **RT Data Availability:** **None (Explicit).** The public metadata (GSE49710) does not include radiation fields, doses, or timing.
*   **Proxy Information:** The "High Risk" and "Unfavorable Class" labels serve as proxies for intensive multimodal therapy, which traditionally includes RT for neuroblastoma patients, but no specific RT analysis can be performed.

### TARGET-NBL (`nbl_target`)
*   **RT Data Availability:** **Partial / Controlled.** 
    *   **Open Access:** cBioPortal and GDC clinical files often list `Radiation Therapy` as a Yes/No flag, but many cases are marked as "Not Reported."
    *   **Controlled Access:** Granular RT details (dosage, type, site) are potentially available in the `radiation.xml` or `treatment` tables via dbGaP ([phs000467](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000467)).
*   **Standard of Care:** Most patients in this cohort were treated under COG protocols (e.g., A3973) where RT is a mandatory component of the high-risk regimen.

### Study-Specific Discovery Data (PMID 34493726)
*   **RT Data Availability:** **Limited.** The primary focus was on untreated primary tumors and normal tissue to identify cell-of-origin. While risk groups are defined (which dictate RT protocols), individual treatment records for the 11 tumors are not summarized in the main text.

---

## cBioPortal Data Gaps

This section identifies data types present in the original publications/repositories but missing from the corresponding cBioPortal studies.

### SEQC-NB498 (`nb_seqc_utah_2015`)
*   **Resolution Gap:** cBioPortal provides **gene-level** expression (Z-scores/RSEM). The original paper ([PMID 26112715](https://pubmed.ncbi.nlm.nih.gov/26112715/)) analyzes data at the **transcript** and **exon junction** levels.
*   **Platform Gap:** cBioPortal primarily hosts the RNA-Seq consensus. The original study includes a direct comparison with **Agilent Microarray** data (GSE49710), which is not fully integrated for cross-query in the portal.
*   **Modeling Labels:** Specific "Class Labels" used for the SEQC predictive models (training vs. validation partitions) are typically not included as searchable clinical attributes.

### TARGET-NBL (`nbl_target`)
*   **Granularity Gap:** cBioPortal provides **discrete** CNA calls (GISTIC -2 to 2). The original study ([PMID 23770567](https://pubmed.ncbi.nlm.nih.gov/23770567/)) and dbGaP ([phs000467](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000467)) contain **continuous** log2 ratios and raw segmentation data.
*   **Variant Gap:** cBioPortal focuses on a **curated somatic MAF**. The original repository includes raw VCFs with multiple callers (MuTect, Strelka) and germline variant data (controlled access).
*   **Structural Variants:** While some fusions are present, the full range of SV calls (BND, DEL, DUP, INV) from WGS is not fully represented in the portal's interface.
*   **Clinical Depth:** Hundreds of granular clinical variables (chemotherapy cycles, detailed pathology) available in dbGaP are reduced to a core subset in cBioPortal.

### Study-Specific Discovery Data (PMID 34493726)
*   **Single-Cell Gap:** The **snRNA-seq** (human) and **scRNA-seq** (mouse) discovery data that form the core of this paper are **not** in cBioPortal. Only the bulk validation cohorts (SEQC/TARGET) are represented.
*   **Imaging Gap:** **RNAscope ISH** spatial validation images are only available in the publication figures/supplement, not in any genomic portal.
*   **Model Weights:** inferCNV weights and cell-type signature latent spaces are not hosted.

---

## Detailed Dataset Catalog

### SEQC-NB498 (Neuroblastoma)
*   **Name:** SEQC-NB498
*   **Institution:** Sequencing Quality Control (SEQC) Consortium (FDA)
*   **Size:** 498 primary tumors
*   **Assays:** mRNA-seq (Illumina HiSeq 2000), Gene Expression Microarray (Agilent 44k)
*   **Clinical Data:** OS, EFS, MYCN status, INSS stage, age at diagnosis.
*   **Sources:**
    *   GEO: [GSE49711](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE49711) (Series), [GSE62564](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62564) (RNA-Seq), [GSE49710](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE49710) (Microarray)
    *   cBioPortal: `nb_seqc_utah_2015`
*   **Key Findings:** Used as a benchmark for RNA-Seq clinical prediction; identified prognostic signatures and confirmed cell-type specific outcome correlations.

### TARGET-NBL (Neuroblastoma)
*   **Name:** TARGET-NBL
*   **Institution:** NCI / TARGET Initiative
*   **Size:** ~1,132 samples (~214 fully characterized cases)
*   **Assays:** mRNA-seq, WES, WGS, SNP-array, DNA-methylation-array
*   **Clinical Data:** INSS stage, COG risk group, MYCN status, outcomes.
*   **Sources:**
    *   dbGaP: [phs000467](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000467)
    *   GDC: [Project TARGET-NBL](https://portal.gdc.cancer.gov/projects/TARGET-NBL)
    *   cBioPortal: `nbl_target`
*   **Key Findings:** Characterized the mutational landscape of high-risk neuroblastoma (*ALK*, *MYCN*, *ATRX*).

### Synapse: human_NB (Karolinska)
*   **Name:** Synapse: human_NB
*   **Institution:** Karolinska Institutet (Bedoya-Reina et al.)
*   **Size:** 11 NB tumors, 3 normal human adrenal glands, 5 mouse adrenal glands
*   **Assays:** snRNA-seq, scRNA-seq (Smart-Seq2 / Nuc-Seq)
*   **Sources:**
    *   Synapse: [syn22302605](https://www.synapse.org/#!Synapse:syn22302605)
    *   Sub-accessions (NB samples): `syn22307346` (K87), `syn22306928` (K6), `syn22306349` (K55), `syn22305928` (K47), `syn22305408` (K40), `syn22304935` (K3), `syn22304482` (K2), `syn22304038` (K14), `syn22303649` (K10), `syn22303256` (23), `syn22302820` (19).
*   **Key Findings:** Identified TRKB+ cholinergic progenitor in human postnatal adrenal gland as potential cell-of-origin for high-risk neuroblastoma.

---

## Detailed Review by Paper

### [PMID 34493726](https://pubmed.ncbi.nlm.nih.gov/34493726/)
*Single-nuclei transcriptomes from human adrenal gland reveal distinct cellular identities of low and high-risk neuroblastoma tumors* (2021)
*   **Methods:**
    *   `deindexer`: [github.com/ws6/deindexer](https://github.com/ws6/deindexer) (Demultiplexing)
    *   `Rtsne`: [github.com/jkrijthe/Rtsne](https://github.com/jkrijthe/Rtsne) (t-SNE implementation)
    *   `inferCNV`: [github.com/broadinstitute/inferCNV](https://github.com/broadinstitute/inferCNV) (CNV analysis)
*   **Datasets:**
    *   **Synapse:** Accession `syn22303649` (K10) and project `syn22302605`.
    *   **dbGap:** Study Accession `phs000218.v16.p6` (via TARGET-NBL `phs000467`).
    *   **GEO:** SEQC publicly available data (GSE49710).

### [PMID 27389358](https://pubmed.ncbi.nlm.nih.gov/27389358/)
*A Practical Guide for Improving Transparency and Reproducibility in Neuroimaging Research* (2016)
*   **Methods:**
    *   `myconnectome-vm`: [github.com/poldrack/myconnectome-vm](https://github.com/poldrack/myconnectome-vm) (Virtual Machine for analysis)
    *   `bids-validator`: [incf.github.io/bids-validator](http://incf.github.io/bids-validator) (BIDS standard compliance)
*   **Datasets:**
    *   **Repositories mentioned:** FigShare, Dryad, DataVerse, Open Science Framework (OSF).
    *   **FCP/INDI:** [Functional Connectome Project/International Neuroimaging Data-Sharing Initiative](http://fcon_1000.projects.nitrc.org/).

### [PMID 37119971](https://pubmed.ncbi.nlm.nih.gov/37119971/)
*Multi-Omics Profiling for Health* (2023)
*   **Methods:**
    *   `awesome-multi-omics`: [github.com/mikelove/awesome-multi-omics](https://github.com/mikelove/awesome-multi-omics) (Curation of multi-omics tools)
*   **Datasets:**
    *   **Consortia:** TCGA ([portal.gdc.cancer.gov](https://portal.gdc.cancer.gov)), CPTAC ([cptac-data-portal.georgetown.edu](https://cptac-data-portal.georgetown.edu)), Synapse.

### [PMID 26978244](https://pubmed.ncbi.nlm.nih.gov/26978244/)
*The FAIR Guiding Principles for scientific data management and stewardship* (2016)
*   **Methods:**
    *   `DataFairPort`: [github.com/WilkinsonLab/DataFairPort](https://github.com/WilkinsonLab/DataFairPort) (Perl libraries, doi:10.5281/zenodo.33584)
*   **Datasets:**
    *   **General Repositories:** Zenodo, DataHub, FigShare, Dryad, Mendeley Data, DANS, EUDat.
    *   **Registry:** BioSharing ([biosharing.org](https://biosharing.org)).

### [PMID 29902176](https://pubmed.ncbi.nlm.nih.gov/29902176/)
*Cloud computing applications for biomedical science: A perspective* (2018)
*   **Methods:**
    *   Cloud-native tools like `CloudMan` and `CloudBioLinux`.
*   **Datasets:**
    *   **PCAWG:** Pan-Cancer Analysis of Whole Genomes.
    *   **Cloud Storage:** NIH datasets on AWS S3.

### [PMID 33305538](https://pubmed.ncbi.nlm.nih.gov/33305538/)
*A review on medical imaging synthesis using deep learning and its clinical applications* (2021)
*   **Methods:**
    *   Extensive review of GAN (CycleGAN), U-net, and ResNet architectures for medical imaging.
*   **Datasets:**
    *   Mentions numerous datasets for MR-to-CT and CT-to-PET synthesis (many are study-specific or linked to radiotherapy planning cohorts).

### [PMID 27806376](https://pubmed.ncbi.nlm.nih.gov/27806376/)
*Single-cell RNA-seq supports a developmental hierarchy in human oligodendroglioma* (2016)
*   **Datasets:**
    *   **GEO:** Data available through the Gene Expression Omnibus.
