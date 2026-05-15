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

- **2026-05-15** — Added 5 papers (PMIDs 26878173, 26901067, 26928463, 26950094, 26977886) — first batch under the new deterministic bracket-normalizer + lint enforcement, and the agents emitted **zero malformed Obsidian-style links** (vs. ~1,200 in the previous batch). MSKCC advanced thyroid (PDTC + ATC, 117 tumors, MSK-IMPACT) — BRAF/RAS dichotomy with stepwise TERT-promoter enrichment ([PMID 26878173](papers/26878173.md)); MSKCC plasmacytoid bladder cancer — CDH1 truncating mutations as pathognomonic marker ([PMID 26901067](papers/26901067.md)); FHCRC mCRPC rapid-autopsy multi-tumor cohort — Fanconi-anemia / ATM-deficient subset as carboplatin-response biomarker ([PMID 26928463](papers/26928463.md)); UNIGE NB-UVB phototherapy NanoSeq — first quantitative duplex-sequencing measurement of in-vivo therapy-induced somatic mutation burden ([PMID 26950094](papers/26950094.md)); BCGSC extra-cranial malignant rhabdoid tumor multi-omic landscape — quiet somatic genome with HOX-cluster super-enhancers as epigenetic dependencies ([PMID 26977886](papers/26977886.md)). 39 new entity pages (25 genes incl. full FA core complex; 5 cancer types THPD/SRCBC/BCC/MRT/MRTL; 5 datasets; 2 drugs; 2 methods nanoseq/polygenic-risk-score). Also: shipped `cbio-kb wiki normalize-brackets` CLI + lint enforcement so dangerous bracket shapes now fail CI before the publish workflow runs.
- **2026-05-14** — Added 5 papers (PMIDs 26804919, 26824661, 26829750, 26855148, 26862087) covering rare-cancer landscapes and a TCGA pan-glioma landmark. BCM periampullary/biliary WES with ELF3 tumor suppressor and WNT-pathway taxonomy ([PMID 26804919](papers/26804919.md)); TCGA pan-glioma integrated multi-platform analysis (1,122 cases, six LGm methylation subtypes superseding prior LGG/GBM analyses) ([PMID 26824661](papers/26824661.md)); two adenoid cystic carcinoma genomic studies revealing MYB enhancer hijacking with JQ1 sensitivity ([PMID 26829750](papers/26829750.md)) and NFIB rearrangements pushing translocation prevalence to 60% ([PMID 26862087](papers/26862087.md)); WCM neuroendocrine prostate cancer multi-omic characterization with 70-gene NEPC classifier ([PMID 26855148](papers/26855148.md)). 42 new entity pages (29 genes, 2 cancer types AMPCA/DA, 5 datasets, 6 methods incl. radia/mutcomfocal/tumor-map/estimate/ingenuity-pathway-analysis/variantdx). Also tightened paper-compiler and crosslinker agent prompts to forbid Obsidian wiki-link syntax (`[[...]]`) after the recent multi-hour pandoc hang.
- **2026-05-14** — Added 30 papers (PMIDs 25409260–26760213) in a six-wave /loop covering 2014–2016 cancer genomics. Landmark immuno-oncology: Snyder CTLA-4 melanoma neoantigen tetrapeptide signature ([PMID 25409260](papers/25409260.md)) and Van Allen ipilimumab melanoma neoantigen+cytolytic axis ([PMID 26359337](papers/26359337.md)); Rizvi/MSKCC TMB→pembrolizumab response in NSCLC ([PMID 25765070](papers/25765070.md)). TCGA multi-platform landmarks: papillary thyroid ([PMID 25417114](papers/25417114.md)), HNSCC ([PMID 25631445](papers/25631445.md)), cutaneous melanoma BRAF/RAS/NF1/Triple-WT subtypes ([PMID 26091043](papers/26091043.md)), lobular breast cancer (ILC) ([PMID 26451490](papers/26451490.md)), prostate 7-subtype integrated analysis ([PMID 26544944](papers/26544944.md)). Other landmark cohorts: BC Cancer breast PDX single-cell clonal dynamics ([PMID 25470049](papers/25470049.md)); Schulze/INSERM HCC WES with AFB1 signatures ([PMID 25822088](papers/25822088.md)); UTSW microdissected PDAC WES ([PMID 25855536](papers/25855536.md)); SU2C-PCF mCRPC prospective WES ([PMID 26000489](papers/26000489.md)); UCologne SCLC universal TP53/RB1 loss ([PMID 26168399](papers/26168399.md)); Landau/Broad CLL 538-tumor WES discovering RPS15 ([PMID 26466571](papers/26466571.md)); SickKids medulloblastoma primary/recurrence pairs ([PMID 26760213](papers/26760213.md)). Rare-cancer / novel-driver discovery: UTUC vs UCB ([PMID 26278805](papers/26278805.md)), desmoplastic melanoma NFKBIE promoter hotspot ([PMID 26343386](papers/26343386.md)), MD Anderson ACC MYBL1-NFIB fusions ([PMID 26631609](papers/26631609.md)), QIMR uveal melanoma PLCB4 p.D630Y ([PMID 26683228](papers/26683228.md)), Mayo PCNSL TOX/PRKCD biallelic loss ([PMID 25991819](papers/25991819.md)), Tianjin gastric NRG1-ERBB4 axis ([PMID 25583476](papers/25583476.md)). Translational reviews: cholangiocarcinoma precision medicine (FGFR2, IDH1) ([PMID 25526346](papers/25526346.md)), gut-liver microbiome/bile-acid in CCA ([PMID 25608663](papers/25608663.md)). Methods firsts: Bu rat somatic-editing ER+ breast cancer model via intraductal AAV/CRISPR ([PMID 26437033](papers/26437033.md)); CLL del(13q)/SF3B1 H3B-8800 splicing-modulator PoC ([PMID 26200345](papers/26200345.md)). Race-specific genomics: Case Western AA colorectal SMGs ([PMID 25583493](papers/25583493.md)); DFCI metastatic cSCC OncoPanel ([PMID 25589618](papers/25589618.md)); MSKCC breast ACC ([PMID 26095796](papers/26095796.md)); Columbia CTCL Sézary/MF WES ([PMID 26551667](papers/26551667.md)); Peifer/UCologne neuroblastoma TERT rearrangements ([PMID 26466568](papers/26466568.md)). ~675 unique gene-page touches, 25 new datasets, 14 new cancer types, ~28 new drugs (incl. gut-microbiome/bile-acid tools, splicing modulator H3B-8800, MDM2 nutlin/AMG-232), ~25 new methods (incl. aav-crispr-somatic-editing, pyclone, titan-cna, paradigm, isopure, oncosign, expands, sleeping-beauty-transposon-screen, shatterseek, dna-methylation-array, whole-genome-bisulfite-seq). Wave commits: e960567, 04ca78a, f82deca, d38f6e4, 5bcc14b, 5361db5.
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
