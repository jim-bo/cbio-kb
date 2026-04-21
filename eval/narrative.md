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

We compare two retrieval strategies over a curated, 56-paper subset of the
cBioPortal cancer-genomics publication corpus. The first (**Agentic**) is
a language-model agent that navigates a hand-compiled wiki of papers,
genes, cancer types, datasets, drugs, and methods via six graph-walk
tools. The second (**RAG**) is standard dense-vector retrieval: chunk
paper markdowns, embed with Vertex AI `gemini-embedding-001`, pull the
top-40 chunks, answer in a single call. Both modes share the answering
model (`claude-haiku-4-5`) and a rubric judge (`claude-opus-4-6`). On a
50-question set split 30/10/10 across train/val/test and four question
categories, the agent wins on every dimension of the held-out test split —
accuracy {stat:ag_test_acc} vs {stat:rg_test_acc}, completeness
{stat:ag_test_comp} vs {stat:rg_test_comp}, citation recall
{stat:ag_test_rec} vs {stat:rg_test_rec} — at roughly 25% more wall time.
Results are consistent across splits, so the win is not train-set
overfitting. We read this as a preliminary step before trying GraphRAG-style
community summarization, adaptive retrieval (Self-RAG / CRAG), and a larger
corpus. The apparatus, data, and source are all reproducible from `eval/`.

## section:intro

Retrieval-augmented generation ({cite:lewis2020rag}) has become the default
recipe for grounding language-model answers in a specific corpus. The
dominant implementation is dense-vector search over fixed-size text chunks
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
vector search is underpowered.

This experiment is a preliminary step in that direction for a
cancer-genomics corpus. We already maintain a hand-compiled wiki of
papers, genes, cancer types, datasets, drugs and methods (56 papers as of
this run, a subset of the cBioPortal publication list), with cross-links
between entity pages and their citing papers. The question we want to
answer is modest: *given that graph, does an agent that walks it beat a
vanilla RAG pipeline over the same papers?* A positive answer makes the
wiki investment defensible and motivates building more structure into it;
a negative one says the structure isn't paying for itself and a plain
embedding pipeline would do. Biomedical-QA evaluation has a long tradition
of treating this setup carefully — factoid, list, yes/no and summary
question types ({cite:krithara2023bioasq}, {cite:jin2019pubmedqa},
{cite:wadden2020scifact}) — which shaped our question set.

We are aware of several gaps before this can serve as a full comparison
to the 2024–2026 GraphRAG / agentic-retrieval literature. Our wiki graph
has no community-detection layer ({cite:edge2024graphrag}), no
pre-computed theme/subgraph summaries, and no adaptive retrieval loop
({cite:asai2023selfrag}, {cite:yan2024crag}). We are under-covering the
full cBioPortal publication set (56 of several hundred), and
question-set coverage of synthesis and list question types is thin. Treat
the numbers here as directional, not absolute.

## section:methods

**Corpus.** 56 papers from the cBioPortal publication list, selected because
they were fully ingested into both our compiled wiki (at
`wiki/papers/{pmid}.md`) and our chunking/embedding pipeline (raw markdown
at `data/raw/papers/{pmid}.md`). Both retrieval modes see exactly this set
— no side channel.

**Question set.** 50 questions authored manually, split 30 / 10 / 10 across
train / val / test, and tagged with one of four categories: *lookup*
(single-paper factoid), *list* (enumerate papers or entities meeting a
criterion), *synthesis* (cross-paper claim), or *definition* (what is X?).
Each question carries one or more gold PMIDs so we can measure citation
recall independently of the judge.

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

**Judge.** `claude-opus-4-6` reads the question, gold notes, and the
agent's final answer, and returns three integer scores on a 1–5 rubric —
*accuracy*, *completeness*, *citation_correctness* — plus a free-text
reason. We separately compute citation recall as the fraction of gold
PMIDs cited in the answer (detected by regex on `PMID:\d+` and
`papers/\d+\.html` link forms). Full rubric and scoring code are in
[eval/judge.py](https://github.com/jim-bo/cbio-kb/blob/main/eval/judge.py)
and [eval/README.md](https://github.com/jim-bo/cbio-kb/blob/main/eval/README.md).

## section:headline_intro

Mean scores on the 30-question train split. Judge scores are on a 1–5
scale; citation recall is the fraction of gold PMIDs appearing in the
answer.

## section:headline_takeaway

*Takeaway — agentic wins on completeness and recall; RAG is 2× cheaper in
tokens and ~2× faster in wall time. Accuracy and citation correctness are
within noise.*

## section:figure1_intro

Each category is a different flavour of question. Categories where
*completeness* (did you enumerate the facts?) carries signal are where
the agent's per-page reading pays off.

## section:figure1_caption

Figure 1. Mean judge score by question category, agentic vs RAG. Each
panel is one metric (accuracy / completeness / citation). Agentic pulls
clearly ahead on completeness for list and synthesis questions.

## section:figure1_takeaway

*Takeaway — lookup and definition are a wash; agentic edges RAG on list
(+0.3 completeness) and especially synthesis (+1.3 completeness), the
categories where full-page reading matters most.*

## section:splits_intro

Three disjoint splits run with identical configuration. Consistency across
the three is evidence the agent's win isn't train-set overfitting (we
tuned nothing between splits).

## section:splits_takeaway

*Takeaway — agentic stays ahead on every metric on every split, with the
test margins matching or exceeding the train margins.*

## section:figure2_intro

Each point is one train-split question plotted at its total judge score
(accuracy + completeness + citation, 3–15) for both modes. Bubble size is
proportional to whichever mode took longer on that question. Points above
the dashed *y = x* line are agent wins; below the line are RAG wins.

*Hover any point in the interactive version for the full question and
both answers.*

## section:figure2_takeaway

*Takeaway — most synthesis points (red) sit above the diagonal, most
definition and high-scoring lookup points pile near (15, 15). Two
agent-losses stand out: LS04 (a list question the agent got lost on) and
S04 (a synthesis question both modes struggled with, but RAG did
better).*

## section:figure3_intro

Cost here is deliberately not budget-matched: each strategy carries its
own shape. The left panel shows input-token cost (log scale) against
total judge score; the right panel shows the same against wall time. A
well-behaved retrieval strategy should have its high-scoring dots
concentrated at the left of each panel.

## section:figure3_caption

Figure 3. Total judge score vs input tokens (log scale, left) and wall
time (right), agentic and RAG overlaid. RAG clusters cheap/fast; agentic
spends more to reach the same score ceiling, but also reaches it on
questions where RAG cannot.

## section:figure3_takeaway

*Takeaway — RAG has a tight, cheap, fast cluster in the 10k-token band;
agentic spreads across 10k–200k tokens. Both modes hit the score ceiling
of 15, but for several mid-scoring synthesis questions only the agent
crosses into the high band.*

## section:guardrails_note

Exceeding either cap is a harness-level failure, not a judge failure; the
record is kept and scored on whatever partial output was emitted before
the cap fired.

## section:discussion_caveats

The held-out test split is the number to quote — the agent beats RAG on
every dimension (accuracy, completeness, citation, citation recall) at
roughly 25% more wall time. The magnitude of the win is largest on
*completeness*, which matches the intuition that graph-walking over whole
pages beats passage-packing when the answer needs to enumerate.
Train/val/test consistency rules out overfitting to a single split.

Several caveats bound how far to push this result. It's a single corpus
(56 papers), a single question set (50 questions), a single judge model,
and no statistical-significance testing on the metric differences. RAG
hyperparameters (chunk size, overlap, top-k, embedding model) were not
swept; we used a sensible-default configuration. The agent benefits from
a wiki that was itself authored by language-model agents from the same
paper corpus, so some of the lift could be attributed to that
pre-processing rather than graph-walk retrieval per se — a dedicated
ablation would be needed to separate the two.

## section:next_steps

**Next steps, in rough priority order:**

1. **GraphRAG-style community summarization** on our wiki's cross-link
   graph ({cite:edge2024graphrag}). We already emit `wiki/graph.json`;
   running Leiden over it and generating theme-level summaries would give
   a third retrieval strategy to compare against — and address our
   current lack of synthesis/theme pages.

2. **Adaptive retrieval** — layering a reflection-token style decision
   ({cite:asai2023selfrag}) or a retrieval evaluator
   ({cite:yan2024crag}) on top of the RAG path so it can fall through to
   graph-walk when the top-k is weak.

3. **Corpus expansion.** We run on 56 of cBioPortal's several hundred
   published studies. Re-evaluating on a 200+ paper corpus would test
   whether the agent scales with depth.

4. **Question-set scale and judges.** A larger, possibly partially
   auto-generated question set; multiple judge models and bootstrap
   confidence intervals on every delta.

5. **Authoring themes and community pages.** A structural gap in the
   current wiki: no pre-written cross-paper synthesis pages. Their
   absence probably hurts both modes, but the agent more (it's the
   natural top-down landing page).
