<!--
Editable prose for wiki/experiments/rag-vs-agentic.qmd.

Rules:
  - Sections are delimited by a top-level heading of the form:
        ## section:<id>
    The builder splits on those lines; the body is everything up to
    the next ## section or EOF. Ids are referenced by name in
    eval/build_report.py, so don't rename them without updating the
    corresponding lookup.
  - Inline citations use {cite:KEY} where KEY is a bibliography key
    from eval/bibliography.yaml. Expands to a markdown link like
    [Edge 2024](https://arxiv.org/abs/2404.16130).
  - Inline numbers that depend on the current eval run use
    {stat:<name>} placeholders — see the _compute_stats() table in
    build_report.py for the full set of names. These are for numbers
    that should stay live when new runs land; use plain text for
    numbers that are commentary ("roughly 25% more wall time").

Tables, figures, bibliography list, and the appendix are rendered by
Python from the JSONL records — those are NOT in this file.
-->

## section:abstract

We compare three retrieval strategies over the full 377-paper cBioPortal
cancer-genomics publication corpus. **Agentic** is a language-model agent
that navigates a hand-compiled wiki of papers, genes, cancer types,
datasets, drugs, and methods via six graph-walk tools. **RAG** is standard
dense-vector retrieval: chunk paper markdowns, embed with Vertex AI
`gemini-embedding-001`, pull the top-40 chunks, answer in a single call.
**Hybrid** fuses three retrieval legs — dense vectors, BM25, and a one-hop
walk over the wiki cross-link graph — reranks with a cross-encoder, then
answers in a single call. All three share the answering model
(`claude-haiku-4-5`) and a rubric judge (`claude-opus-4-6`), and crucially
all three search the *same* 377-paper corpus, so the comparison isolates
retrieval strategy from corpus size. On an 80-question set split 48/16/16
across train/val/test and four categories, **no strategy dominates**: on the
held-out test split accuracy is a near-wash (agentic {stat:ag_test_acc},
RAG {stat:rg_test_acc}, hybrid {stat:hy_test_acc}), while the agent leads
completeness ({stat:ag_test_comp} vs {stat:rg_test_comp} / {stat:hy_test_comp})
and citation recall ({stat:ag_test_rec} vs {stat:rg_test_rec} /
{stat:hy_test_rec}) — a lead concentrated in the enumeration-heavy *list* and
*synthesis* categories, bought with substantially more tokens and wall time.
RAG matches the agent on accuracy and edges it on citation correctness at a
small fraction of the cost; hybrid is the cheapest and fastest but trails on
quality. We read this as evidence that graph-walk retrieval earns its cost
only on multi-document questions, and that for single-fact retrieval a
conventional embedding pipeline is competitive. The apparatus, data, and
source are all reproducible from `eval/`.

## section:intro

Retrieval-augmented generation ({cite:lewis2020rag}) has become the default
recipe for grounding language-model answers in a knowledge base. The
classic implementation is vector search over fixed-size text chunks
({cite:karpukhin2020dpr}, {cite:khattab2022colbertv2}), evaluated on
heterogeneous retrieval benchmarks ({cite:thakur2021beir},
{cite:muennighoff2022mteb}) and generation-quality rubrics
({cite:es2023ragas}). In parallel, two threads have emerged that treat
retrieval as a *behaviour* rather than a single lookup: graph-augmented
retrieval ({cite:edge2024graphrag}, {cite:jimenez2024hipporag},
{cite:guo2024lightrag}, {cite:gao2024structrag}) builds an explicit
structure over the corpus and walks it; agentic retrieval
({cite:yao2023react}, {cite:nakano2022webgpt}, {cite:asai2023selfrag},
{cite:yan2024crag}, {cite:singh2025agenticrag}) lets a language-model
agent decide what to read next based on what it just saw. Both converge
on the same observation: for questions that span documents, flat top-k
vector search is **not the best fit**.

This study evaluates that proposition for a cancer-genomics knowledge base
that powers a conversational question-answering interface. We maintain a
hand-compiled wiki of papers, genes, cancer types, datasets, drugs, and
methods (377 papers in this study, a subset of the cBioPortal publication
list together with related work), cross-linked between entity pages and their
citing papers. The central question is whether, given that graph, an agent
that walks it outperforms a conventional dense-RAG pipeline — or a hybrid that
augments dense retrieval with BM25 and a one-hop graph expansion — over the
same papers. A positive result would justify investing in richer structure in
the knowledge base; a negative one would indicate that the structure does not
earn its keep and that a plain embedding pipeline suffices. Following the
tradition of biomedical question-answering evaluation, we use a language model
to author a question set spanning four categories — *lookup* (single-paper
factoid), *list*, *synthesis*, and *definition* ({cite:krithara2023bioasq},
{cite:jin2019pubmedqa}, {cite:wadden2020scifact}).

Several aspects of the setup are deliberately simple. The wiki graph has no
community-detection layer ({cite:edge2024graphrag}), no pre-computed theme or
subgraph summaries, and no adaptive retrieval loop ({cite:asai2023selfrag},
{cite:yan2024crag}); the choice of what to abstract from each paper, and what
to treat as an entity, has not been systematically optimized. Because the
question set is language-model-authored with limited manual review, the
absolute scores should be read as indicative rather than definitive, and the
relative comparison across modes is the object of interest.

## section:methods

**Corpus.** 377 papers from the cBioPortal publication list, selected because
they were fully ingested into both the compiled wiki (at
`wiki/papers/{pmid}.md`) and the chunking/embedding pipeline (raw markdown
at `data/raw/papers/{pmid}.md`). All three retrieval modes index exactly this
set, with no side channel. Sharing a single corpus across modes is a
deliberate control: it ensures the measured differences reflect retrieval
strategy rather than differences in corpus coverage.

**Question set.** 80 questions authored by an LLM, split 48 / 16 / 16 across
train / val / test, and tagged with one of four categories: *lookup*
(single-paper factoid, 27), *list* (enumerate papers or entities meeting a
criterion, 10), *synthesis* (cross-paper claim, 25), or *definition* (what is
X?, 18). Each question carries one or more gold PMIDs so we can measure
citation recall independently of the judge; *list*-question gold is the
comprehensive expected set over the full 377-paper corpus.

**Agentic mode.** A PydanticAI agent using `claude-haiku-4-5` with six
graph-walk tools: `read_page`, `read_section`, `follow_links`,
`find_references`, `get_page_metadata`, `list_pages`. The system prompt
instructs the agent to start from `index.md` and traverse by title match →
entity pivot → follow links. A hard cap of 20 tool calls per query and a
180-second wall-clock deadline are enforced at the server and runner
layers respectively.

**RAG mode.** Paper markdowns are chunked (~900 chars with 120 overlap),
embedded with Vertex AI `gemini-embedding-001` (3072-dim), and stored in a
FAISS `IndexFlatIP` for cosine similarity. At query time we embed the
question, pull the top-40 passages (budgeted to ~60k characters of
context), and issue a single `claude-haiku-4-5` call with the stitched
passages plus the question.

**Hybrid mode.** Three retrieval legs run over the same index and are fused:
(1) *dense* — the RAG vector leg above; (2) *BM25* — a `rank_bm25.BM25Okapi`
lexical index built from the same chunk `meta.jsonl`; (3) *graph 1-hop* —
entity anchors extracted from the question expand over `wiki/graph.json`
cross-edges to citing papers. Candidates are reranked by a cross-encoder
before being packed into a single `claude-haiku-4-5` call. Hybrid is meant
to combine RAG's lexical/semantic recall with a thin slice of the agent's
graph awareness, without the agent's multi-call traversal cost.

**Judge.** `claude-opus-4-6` reads the question, gold notes, and the
agent's final answer, and returns three integer scores on a 1–5 rubric —
*accuracy*, *completeness*, *citation_correctness* — plus a free-text
reason. We separately compute citation recall as the fraction of gold
PMIDs cited in the answer (detected by regex on `PMID:\d+` and
`papers/\d+\.html` link forms). Full rubric and scoring code are in
[eval/judge.py](https://github.com/jim-bo/cbio-kb/blob/main/eval/judge.py)
and [eval/README.md](https://github.com/jim-bo/cbio-kb/blob/main/eval/README.md).

## section:headline_intro

Mean scores on the 48-question train split, all three modes. Judge scores
are on a 1–5 scale; citation recall is the fraction of gold PMIDs appearing
in the answer.

## section:headline_takeaway

*Takeaway — no clean winner. On train, RAG actually leads accuracy, citation
correctness, and citation recall; agentic's only lead is completeness. Hybrid
is by far the cheapest (≈3k input tokens vs RAG's ≈12k and agentic's ≈280k)
and fastest, but trails on every quality metric. The agent's cost — roughly
20–80× the tokens and ~3× the wall time — buys completeness, not accuracy.*

## section:figure1_intro

Each category is a different flavour of question. Categories where
*completeness* (did you enumerate the facts?) carries signal are where
the agent's per-page reading pays off — and the only place it clearly leads.

## section:figure1_caption

Figure 1. Mean judge score by question category and mode (agentic / hybrid /
RAG). Each panel is one metric (accuracy / completeness / citation). The
agent pulls ahead only on *completeness* for list and synthesis; elsewhere
RAG is even or better.

## section:figure1_takeaway

*Takeaway — the agent's advantage is narrow and category-specific: it leads
completeness on list (≈3.0 vs RAG 2.3) and synthesis (≈3.2 vs 2.6), the
enumeration-heavy categories where full-page reading matters. On lookup and
definition RAG matches or beats it, and on list/synthesis accuracy the agent
actually trails RAG. Hybrid is the weakest on the multi-document categories —
its one-hop graph leg does not recover the agent's completeness edge.*

## section:splits_intro

Three disjoint splits run with identical configuration. We tuned nothing
between splits, so consistency across the three says which differences are
real signal rather than one split's noise.

## section:splits_takeaway

*Takeaway — the one finding that holds on every split is the agent's
**completeness** lead. Accuracy is a wash that slightly favours RAG (RAG leads
on train and val, dead-even on test), citation correctness favours RAG, and
citation recall is mixed (RAG on train and val, agent on test). No single mode
is ahead on every metric on any split.*

## section:figure2_intro

Each point is one train-split question plotted at its total judge score
(accuracy + completeness + citation, 3–15) for the agentic vs RAG head-to-head
(hybrid is shown in Figures 1 and 3, not this pairwise view). Bubble size is
proportional to whichever mode took longer on that question. Points above the
dashed *y = x* line are agent wins; below are RAG wins.

*Hover any point in the interactive version for the full question and
both answers.*

## section:figure2_takeaway

*Takeaway — synthesis questions cluster above the diagonal (the agent's
home turf: S08, S02, S06 are its biggest wins), while lookup and definition
points pile near (15, 15) where both modes ace them. The agent's worst loss
is L16 — a single-fact prostate-actionability lookup it got badly wrong while
RAG nailed it — alongside synthesis cases S17 and S20 where RAG's packed
passages beat the graph walk.*

## section:figure3_intro

Cost here is deliberately not budget-matched: each strategy carries its
own shape. The left panel shows input-token cost (log scale) against
total judge score; the right panel shows the same against wall time. A
well-behaved retrieval strategy should have its high-scoring dots
concentrated at the left of each panel.

## section:figure3_caption

Figure 3. Total judge score vs input tokens (log scale, left) and wall
time (right), all three modes overlaid. Hybrid and RAG cluster cheap and
fast; agentic spends one-to-two orders of magnitude more to reach a
comparable score band.

## section:figure3_takeaway

*Takeaway — hybrid (≈3k tokens) and RAG (≈12k) form a tight, cheap, fast
cluster; agentic fans out to ≈280k tokens and ~3× the wall time. All three
reach the high score band on easy lookup/definition questions, so that spend
only pays off on the multi-document questions where the agent's completeness
edge lives.*

## section:guardrails_note

Exceeding either cap is a harness-level failure, not a judge failure; the
record is kept and scored on whatever partial output was emitted before
the cap fired.

## section:discussion_caveats

The held-out test split is the headline result. **Accuracy is a near-wash**
across all three modes — a single-paper factoid is roughly as answerable from
packed passages as from a graph walk. Where the agent separates is
*completeness* and *citation recall*, and only in the **enumeration-heavy
categories** (*list*, *synthesis*): reading whole pages beats passage-packing
when the answer must enumerate a set. That lead is bought with roughly an
order of magnitude more input tokens and approximately twice the wall time,
and **RAG matches the agent on accuracy while edging it on citation
correctness** at a small fraction of the cost. **Hybrid** is the cheapest and
fastest mode but trails on quality on this question set; its one-hop graph leg
does not recover the agent's completeness edge. The conclusion is therefore
one of *no free lunch*: the agent is preferable when completeness or recall on
multi-document questions justifies the cost, and dense RAG when
accuracy-per-unit-cost is the priority.

Because all three modes index the same 377 papers, these differences are
attributable to retrieval strategy rather than corpus coverage; the comparison
is controlled in that respect.

Several caveats bound how far to push the result. It rests on a single corpus
(377 papers), a single 80-question set, a single judge model, and no
statistical-significance testing on the metric differences. The RAG and hybrid
hyperparameters (chunk size, overlap, top-k, BM25 weighting, reranker, and
embedding model) were not swept; sensible defaults were used throughout. The
agent also benefits from a wiki that was itself authored by language models
from the same paper corpus, so part of its completeness advantage may derive
from that pre-processing rather than from graph-walk retrieval per se;
separating the two would require a dedicated ablation.

## section:next_steps

**Next steps, in rough priority order:**

1. **GraphRAG-style community summarization** on our wiki's cross-link
   graph ({cite:edge2024graphrag}). The hybrid mode already uses a thin
   one-hop graph leg; running Leiden over `wiki/graph.json` and generating
   theme-level community summaries would give the graph signal real
   synthesis depth — and address our current lack of theme pages, which the
   synthesis-category numbers suggest is where retrieval is weakest.

2. **Adaptive retrieval** — layering a reflection-token style decision
   ({cite:asai2023selfrag}) or a retrieval evaluator
   ({cite:yan2024crag}) on top of the RAG/hybrid path so it can fall through to
   graph-walk only when the top-k is weak — buying the agent's completeness
   edge without paying its token cost on every query.

3. **Corpus expansion.** This study covers 377 of cBioPortal's published
   studies. Extending to the remaining several hundred would test whether the
   category-specific agentic advantage holds, grows, or washes out with corpus
   depth.

4. **Question-set scale and judges.** A larger, possibly partially
   auto-generated question set; multiple judge models and bootstrap
   confidence intervals on every delta.

5. **Authoring themes and community pages.** A structural gap in the
   current wiki: no pre-written cross-paper synthesis pages. Their
   absence probably hurts both modes, but the agent more (it's the
   natural top-down landing page).
