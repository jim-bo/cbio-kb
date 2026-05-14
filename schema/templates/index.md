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

- **2026-05-14** — Added 5 papers (PMIDs 25409260, 25417114, 25470049, 25526346, 25583476). Landmark immuno-oncology: Snyder et al. CTLA-4 melanoma neoantigen tetrapeptide signature ([PMID 25409260](papers/25409260.md)). TCGA papillary thyroid integrated genomics with BRAFV600E/RAS dichotomy and BRS / TDS classifiers ([PMID 25417114](papers/25417114.md)). BC Cancer breast PDX single-cell clonal-dynamics WGS ([PMID 25470049](papers/25470049.md)). Cholangiocarcinoma precision-medicine review covering FGFR2 inhibitors (pemigatinib/infigratinib/futibatinib) and IDH1 (ivosidenib) ([PMID 25526346](papers/25526346.md)). Tianjin gastric adenocarcinoma WES+WGS with HiC/LoC clonal subtypes and NRG1-ERBB4 axis ([PMID 25583476](papers/25583476.md)). 78 unique genes touched, 4 new datasets (skcm_mskcc_2014, thca_tcga_pub, brca_bccrc_xenograft_2014, egc_tmucih_2015), 1 new cancer type (CHOL), 3 new drugs (pemigatinib, futibatinib, ivosidenib), 2 new methods (pyclone, titan-cna).
- **2026-05-12** — Added 25 papers (PMIDs 24487277–25401301) in a five-wave batch covering 2014 cancer genomics. Landmarks: TCGA STAD ([PMID 25079317](papers/25079317.md)), TCGA LUAD ([PMID 25079552](papers/25079552.md)), TCGA KICH ([PMID 25155756](papers/25155756.md)). Reviews: Llovet HCC genomics+therapy ([PMID 24735922](papers/24735922.md), [PMID 24798001](papers/24798001.md)), NPC immunotherapy ([PMID 24952746](papers/24952746.md)), HDGC/STAD susceptibility ([PMID 24816255](papers/24816255.md)). Rare-cancer discovery: Ewing WGS ([PMID 25223734](papers/25223734.md)) and EWS-FLI1 heMSC origin ([PMID 25186949](papers/25186949.md)), uterine carcinosarcoma ([PMID 25233892](papers/25233892.md)), MPNST PRC2 loss ([PMID 25240281](papers/25240281.md)), cSCC ([PMID 25303977](papers/25303977.md)), non-clear-cell RCC ([PMID 25401301](papers/25401301.md)), thymic epithelial tumors / GTF2I L404H ([PMID 24974848](papers/24974848.md)), SMARCA4-deficient SCCO ([PMID 24658004](papers/24658004.md)), gallbladder SEMA7A/YAP-TEAD ([PMID 24997986](papers/24997986.md)), RHOA yeast-complementation functional dissection ([PMID 24816253](papers/24816253.md)). Translational: BLCA ERCC2-cisplatin biomarker ([PMID 25096233](papers/25096233.md)), CRC primary-met concordance for anti-EGFR ([PMID 25164765](papers/25164765.md)), MSKCC PRAD organoid drug screen ([PMID 25201530](papers/25201530.md)), MSKCC BLCA MSK-IMPACT ([PMID 25092538](papers/25092538.md)), MSKCC PRAD SHQ1 ([PMID 25024180](papers/25024180.md)), ccRCC TRACERx multi-region ([PMID 24487277](papers/24487277.md)), ESCC genomics ([PMID 24686850](papers/24686850.md)), ESCC microbiome ([PMID 24670651](papers/24670651.md)). ~400 gene-page touches, ~20 new datasets, ~80 new drugs (mostly Chinese-trial NPC investigational IO agents and HCC TKIs), ~30 new methods. HN1→JPT1 HUGO normalization applied.
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
