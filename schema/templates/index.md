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

## News

- **2026-05-12** — Added 5 more 2014 papers spanning sarcoma, uterine, MPNST, cSCC, and non-clear-cell RCC: Institut Curie Ewing sarcoma WGS defining STAG2/TP53 mutations as adverse prognosticators ([PMID 25223734](papers/25223734.md)); JHU/OHSU uterine carcinosarcoma WES showing TP53/PIK3CA/PPP2R1A/FBXW7 EMT-driven landscape ([PMID 25233892](papers/25233892.md)); MSKCC MPNST PRC2 (SUZ12/EED) loss in 70%+ of sporadic and NF1-associated MPNSTs ([PMID 25240281](papers/25240281.md)); MDACC aggressive cSCC WES showing TP53/CDKN2A/NOTCH1/FAT1 driver landscape with limited actionable oncogenes ([PMID 25303977](papers/25303977.md)); Genentech non-clear-cell RCC multi-platform analysis defining PRCC subtypes and TFE3/TFEB translocations in TRCC ([PMID 25401301](papers/25401301.md)). ~104 unique genes touched (~32 new), 5 new datasets, 4 new methods (CREST, GenomeMUSiC, Sequenom genotyping, VarScan), 4 new OncoTree types (MXOV, PRCC, TRCC, ROCY).
- **2026-05-12** — Added 5 more 2014–2015 papers: BLCA ERCC2-mutation as cisplatin-response biomarker in muscle-invasive bladder cancer ([PMID 25096233](papers/25096233.md)); TCGA chromophobe RCC landmark defining KICH genomic profile distinct from clear-cell RCC including mtDNA driver and TERT promoter mutations ([PMID 25155756](papers/25155756.md)); MSKCC colorectal primary-metastasis paired sequencing showing 100% KRAS/NRAS/BRAF concordance with implications for cetuximab/panitumumab biomarker testing ([PMID 25164765](papers/25164765.md)); Ewing sarcoma EWS-FLI1 heMSC cell-of-origin model defining mesenchymal stem-cell origin and DDR vulnerability ([PMID 25186949](papers/25186949.md)); MSKCC prostate cancer organoid biobank with enzalutamide/everolimus/buparlisib drug screening ([PMID 25201530](papers/25201530.md)). ~80 unique genes touched, 5 new datasets, 3 new drugs (aspirin, enzalutamide, buparlisib), 8 new methods (mirna-seq, meerkat, mtdna-long-range-pcr, ChIP-seq, comet assay, teratoma assay, intramuscular xenograft, AmpliSeq Childhood Cancer Panel).
- **2026-05-12** — Added 5 more 2014 landmark papers: gallbladder cancer SEMA7A/YAP-TEAD/EMT stroma-tumor mechanism with verteporfin/c646 inhibitor proof-of-concept ([PMID 24997986](papers/24997986.md)); MSKCC prostate cancer SHQ1 as MYC-cooperating tumor suppressor in the prad_mskcc_2014 aCGH cohort ([PMID 25024180](papers/25024180.md)); TCGA gastric adenocarcinoma 295-tumor multi-platform defining four molecular subtypes (EBV, MSI, GS, CIN) ([PMID 25079317](papers/25079317.md)); TCGA lung adenocarcinoma 230-tumor landmark defining RIT1/MGA as novel drivers and NF1/RIT1 RAS-like subgroup ([PMID 25079552](papers/25079552.md)); MSKCC bladder cancer MSK-IMPACT 109-tumor profiling with chromatin remodeler co-mutation ([PMID 25092538](papers/25092538.md)). ~96 unique genes touched, 5 new datasets (stad_tcga_pub, luad_tcga_pub, prad_mskcc_2014, blca_mskcc_solit_2014), 3 new corpus-grown research-tool drugs (verteporfin, ly294002, c646), 8 new methods (Masson trichrome, tumorsphere, transwell, co-IP, ChIP-qPCR, ELISA, hydrogel stiffness, subcutaneous xenograft).
- **2026-05-11** — Added 5 more papers spanning HCC, gastric, NPC, and thymic genomics: Llovet HCC genomics+therapy review covering molecular subtypes and the sorafenib/lenvatinib/regorafenib/cabozantinib/atezo-bev landscape ([PMID 24798001](papers/24798001.md), flagged content-overlap with [PMID 24735922](papers/24735922.md)); RHOA yeast-complementation functional study of 5 hotspot alleles distinguishing GOF (C16R/A161P) from LOF (R5Q) in DSTAD/AITL/ATLL ([PMID 24816253](papers/24816253.md)); HDGC/diffuse-STAD review on CDH1/CTNNA1 germline and H. pylori/inflammation susceptibility axis ([PMID 24816255](papers/24816255.md)); NPC immunotherapy comprehensive review covering 60+ investigational PD-1/PD-L1/LAG3/TIGIT/agonist agents ([PMID 24952746](papers/24952746.md)); NCI thymic epithelial tumor genomics defining the recurrent GTF2I L404H hotspot ([PMID 24974848](papers/24974848.md)). ~135 unique genes touched, 2 new datasets (lihc_amc_prv, tet_nci_2014), ~64 new corpus-grown drugs (mostly Chinese-trial NPC investigational IO agents), 2 new methods (yeast-complementation-assay, calmorph).
- **2026-05-11** — Added 5 papers spanning renal, ovarian-microbiome, esophageal, and liver genomics: ccRCC multi-region exome study from the TRACERx Renal pilot demonstrating pervasive intratumor heterogeneity and branched evolution ([PMID 24487277](papers/24487277.md)); SMARCA4-deficient SCCO/SMARCB1-loss small-cell cancer of the ovary characterization ([PMID 24658004](papers/24658004.md)); ESCC oral-microbiome meta-analysis linking periodontal pathogens to esophageal carcinoma risk ([PMID 24670651](papers/24670651.md)); UCLA ESCC exome+RNA discovery defining FAT1/FAT2/ZNF750/KMT2D as novel drivers and XPO1/selinexor as actionable ([PMID 24686850](papers/24686850.md)); Llovet et al. HCC genomics+therapy comprehensive review covering TERT/TP53/CTNNB1 driver landscape and sorafenib/cabozantinib/tivantinib/regorafenib axis ([PMID 24735922](papers/24735922.md)). ~115 unique genes touched, 4 datasets, 4 new drugs (selinexor, refametinib, tivantinib, interferon-alpha), 6 new methods (multiregion-exome-seq, phylogenetic-tree-reconstruction, 16s-rrna-seq, etc.). HN1→JPT1 HUGO normalization applied.
- **2026-05-10** — Added 5 more papers spanning brain, head & neck, hematologic, sarcoma, and bladder genomics: UCSF low-grade-glioma paired initial/recurrent WES showing temozolomide-driven hypermutation in 6/10 treated patients progressing to GBM ([PMID 24336570](papers/24336570.md)); sinonasal adenoid cystic carcinoma molecular profiling with canonical and noncanonical MYB/MYBL1::NFIB plus novel ESRRG/DNM3 fusions ([PMID 24418857](papers/24418857.md)); Broad multiple myeloma WES/WGS revealing pervasive subclonal architecture and paradoxical BRAF-WT activation by BRAF inhibitors ([PMID 24434212](papers/24434212.md)); NCI/COG pediatric rhabdomyosarcoma comprehensive genomics defining PAX-fusion genotype as superior to histology with RTK/RAS/PIK3CA altered in 93% ([PMID 24436047](papers/24436047.md)); TCGA muscle-invasive bladder cancer with 32 SMGs, APOBEC-dominant mutagenesis, and 69% therapeutically targetable ([PMID 24476821](papers/24476821.md)). 137 unique genes touched, 4 new datasets, 4 new methods (droplet-digital-pcr, trusight-oncology-500). Brontictuzumab and PLX4720 added as corpus-grown drugs.
- **2026-05-09** — Added 5 more rare-cancer and discovery papers (2013–2014): JHU biliary tract WES (IHCH/GBC, BAP1/ARID1A/PBRM1 chromatin axis) ([PMID 24185509](papers/24185509.md)); Broad melanoma BRAF-inhibitor resistance WES (MAP2K2/MITF as novel resistance) ([PMID 24265153](papers/24265153.md)); JHU pancreatic acinar cell carcinoma + pancreatoblastoma first WES (KRAS-absent, Fanconi/DDR-targetable in >43%) ([PMID 24293293](papers/24293293.md)); Cambridge CIMR landmark CALR discovery in JAK2/MPL-negative MPN ([PMID 24325359](papers/24325359.md)); BC Cancer POG metastatic NEN WGTA (manifest mismatch flagged — actual paper Wee 2025) ([PMID 24326773](papers/24326773.md)). 83 unique genes touched, 5 new datasets, 16 new cancer-type pages spanning MPN-spectrum and neuroendocrine OncoTree codes, 11 new methods (mutational-signatures, viper, strelka, bwa, star, rsem, edger, msi-pcr-pentaplex, qmsp, tsne, consensus-hierarchical-clustering).
- **2026-05-09** — Added 5 more 2013–2014 papers spanning bladder, brain, and lymphoma genomics: MSKCC bladder integrated genomics with MK-2206 sensitivity profiling ([PMID 23897969](papers/23897969.md)); a co-clinical trials review covering KRAS-mutant LUAD selumetinib+docetaxel and PDAC saridegib failures ([PMID 23999436](papers/23999436.md)); TCGA glioblastoma 2013 543-patient multi-platform analysis with TERT/ATRX dichotomy and MGMT subtype-specific methylation ([PMID 24120142](papers/24120142.md)); BGI bladder WGS/WES identifying STAG2 as a novel driver and 32% SCCS-pathway alteration rate ([PMID 24121792](papers/24121792.md)); IDIBAPS mantle cell lymphoma WGS+WES with NOTCH2 as independent prognostic factor ([PMID 24145436](papers/24145436.md)). 102 unique genes touched, 4 new datasets, 9 new methods (RPPA, HM27/HM450 methylation arrays, BreakDancer, BamBam, PRADA, MEMo, INVEX, array-cgh-agilent-1m).
- **2026-05-09** — Added 5 more 2013 papers covering rare-cancer and pediatric genomics: adenoid cystic carcinoma MSKCC WES/WGS ([PMID 23685749](papers/23685749.md)) and Sanger 24-sample cohort with SPEN/FGFR2 mutations ([PMID 23778141](papers/23778141.md)); TCGA clear-cell renal cell carcinoma 446-sample multi-platform characterization ([PMID 23792563](papers/23792563.md)); VHL-loss HIF-isoform-specific scRNA-seq mouse model ([PMID 23797736](papers/23797736.md), manifest mismatch flagged); ICGC PedBrain pilocytic astrocytoma WGS demonstrating 100% MAPK alteration with novel NTRK2 fusions ([PMID 23817572](papers/23817572.md)). 109 unique genes touched (~50 new), 11 new methods (CREST, dRanger-class SV callers, ANNOVAR, Oncotator, Pindel, etc.). Belzutifan added as corpus-grown drug.
- **2026-05-09** — Added 5 landmark 2013 genomics papers spanning five cancer types: esophageal adenocarcinoma WES/WGS revealing the RAC1-GEF (ELMO1/DOCK2) axis ([PMID 23525077](papers/23525077.md)), oral squamous cell carcinoma multi-platform profiling with NOTCH1 as tumor suppressor and 80% targetable rate ([PMID 23619168](papers/23619168.md)), prostate cancer chromoplexy WGS introducing ChainFinder/CLONET ([PMID 23622249](papers/23622249.md)), the TCGA AML 200-case study with mutation-sparse genomes and NPM1+DNMT3A+FLT3 triple-mutant subtype ([PMID 23634996](papers/23634996.md)), and TCGA endometrial carcinoma defining four molecular subgroups (POLE ultramutated, MSI, copy-number low, serous-like) ([PMID 23636398](papers/23636398.md)). 151 unique genes touched (68 new), 5 new datasets, 7 new methods (ABSOLUTE, ChainFinder, CLONET, dRanger, BreakPointer, Indelocator, MuTect).
- **2026-05-06** — Added 5 landmark genomics papers: cBioPortal platform ([PMID 19176454](papers/19176454.md)), MSKCC prostate integrative profiling ([PMID 20579941](papers/20579941.md)), pancreatic neuroendocrine exome sequencing ([PMID 21252315](papers/21252315.md)), TCGA ovarian carcinoma ([PMID 21720365](papers/21720365.md)), and NHL histone-modifier mutations ([PMID 21796119](papers/21796119.md)). 17 new gene pages, 4 cancer types, 4 datasets created.
- **2026-05-06** — Added 12 papers spanning sarcoma genomics ([PMID 20601955](papers/20601955.md)), lung adenocarcinoma somatic mutations ([PMID 18948947](papers/18948947.md)), GIST germline variants ([PMID 36593350](papers/36593350.md)), AURORA metastatic breast cancer multiomics ([PMID 36585450](papers/36585450.md)), myoepithelial carcinoma WGS ([PMID 36577525](papers/36577525.md)), bladder cancer primary-metastasis concordance ([PMID 36543146](papers/36543146.md)), HGSOC TME atlas ([PMID 36517593](papers/36517593.md)), KRASG12C-EGFR resistance in CRC ([PMID 36355783](papers/36355783.md)), FBXO7-CHEK1 synthetic lethality ([PMID 36334560](papers/36334560.md)), metastatic urothelial carcinoma molecular landscape ([PMID 36333289](papers/36333289.md)), gallbladder cancer genomics ([PMID 36228155](papers/36228155.md)), and NSCLC multimodal ICI prediction ([PMID 36038778](papers/36038778.md)). Also shipped `wiki append-citation` CLI for 29% token-efficiency improvement.
- **2026-05-01** — Added 11 papers: the landmark 2008 TCGA glioblastoma interim analysis ([PMID 18772890](papers/18772890.md)) plus 10 from 2024–2025 covering MSK-CHORD multimodal NLP, MiMSI MSI classifier, PDAC MAPK-subtype atlas, HGSOC fallopian-tube precursor spatial atlas, normal-skin melanocyte cell-of-origin atlas, CALGB 90601 mUC cfDNA, and others.

## Browse

| Section | Count | What you'll find |
|---|---|---|
| [Papers](#papers) | ${papers_count} | Per-publication summaries: cohort, methods, findings, citations |
| [Genes](#genes) | ${genes_count} | Alterations, co-occurrence, therapeutic relevance across the corpus |
| [Cancer types](#cancer-types) | ${cancer_types_count} | OncoTree-anchored disease pages linking studies and alterations |
| [Datasets](#datasets) | ${datasets_count} | cBioPortal studies with cohort details and linked publications |
| [Drugs](#drugs) | ${drugs_count} | Targeted therapies, resistance patterns, evidence in the corpus |
| [Methods](#methods) | ${methods_count} | Sequencing assays, gene panels, and analytical pipelines |
| [Themes](#themes) | ${themes_count} | Cross-cutting syntheses (in progress) |

## Papers

${papers_list}

## Genes

${genes_list}

## Cancer types

${cancer_types_list}

## Datasets

${datasets_list}

## Drugs

${drugs_list}

## Methods

${methods_list}

## Themes

${themes_list}

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
