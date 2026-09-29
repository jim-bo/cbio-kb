# Grounding: answers that cite what the papers actually say

Captured 2026-09-18 after checking one LibreChat answer against the papers
it cited. The answer came from Claude Sonnet 4.6 using the MCP server
(`deploy/librechat-local/`) for "Tell me what you know about RAS and its
relationship to late stage lung cancer". This note is about the answers
clients build from the KB. `FACT_VERIFICATION.md` is about checking the wiki
itself against cBioPortal's API, and items 5 and 6 below overlap its Phase B.

## What the audit found

The five claims in the answer's first section, each traced to the tool
results the model saw and to the cited paper's full text in
`data/raw/papers/{pmid}.md`:

| Claim in the answer | What the paper says | Verdict |
|---|---|---|
| KRAS in ~27–32% of LUAD | "KRAS (32%, n =74)" in PMID:25079552 (TCGA 2014); "KRAS (27%)" in PMID:22980975 (Imielinski 2012) | Supported, but mislabeled "TCGA Pan-Cancer Atlas" |
| KRAS essentially absent in LUSC | "Only one sample had a KRAS codon 61 mutation" (PMID:22960745) | Fair paraphrase; a quote would be exact |
| KRAS linked to smoking, P=0.021 | "KRAS mutations correlate with smoker status (P=0.021)" (PMID:18948947) | Verbatim. The same paper uses P=0.021 for another test too |
| KRAS/EGFR mutually exclusive, P<1e-7 | "negative correlation of mutations in EGFR and KRAS ... (P < 1 × 10-07)" (PMID:18948947) | Correct but uncited in the answer |
| RTK/RAS/RAF altered in "62–85% across large cohorts" | Both cited papers report 76%. 62% is TCGA's figure before its extended analysis ("from 62% to 76%"); 85% is 193 of 227 expert-reviewed tumours in PMID:27158780 | Misleading composite. 62% was in no tool result, so it came from the model's memory |

Four of five hold up. The real problem is that the reader can't tell a quote
from a paraphrase, or either from the model's memory, and nothing stopped the
model from building a range no paper states.

## Why

- **Paraphrase of a paraphrase.** Most numbers reached the model through
  `get_entity` (the KRAS wiki page, 21k characters, written by an LLM), not
  through paper text.
- **Passages can't be addressed.** `data/paper_index/meta.jsonl` stores only
  `pmid`, `chunk_id` and `text`: no section, paragraph or offsets.
  `_chunk_sentences` (`src/cbio_kb/index/papers.py`) overlaps chunks by the
  last 120 characters of the previous one, so passages start mid-word.
  Reference lists and PMC manuscript headers are indexed: 3 of the 22 passages
  in the audit were bibliography, and the only "62" in any tool result was a
  journal volume number.
- **No citation contract.** `ai_search/mcp_instructions.md` asks for PMIDs
  but says nothing about quotes vs paraphrase, where numbers may come from, or
  merging figures from different papers.

## Plan

| # | Change | Status |
|---|---|---|
| 1 | Citation contract in the server instructions | Done 2026-09-18 |
| 2 | `get_passage` and `verify_quote` tools | Done 2026-09-18 |
| 3 | Re-chunk the passage index with anchors | Done 2026-09-29 (results below) |
| 4 | Links that land on the quoted sentence | To do |
| 5 | Grounding score in the eval | To do |
| 6 | Sentence-level provenance in the wiki | Later |
| 7 | Answer-first shape in the instructions | Done 2026-09-18 (tested below) |
| 8 | Quote-ready sentences in search results | To do (with 3); needed, see experiment |
| 9 | Native `search_result` citations and post-stream checks in `/ask` | To do |
| 10 | Evidence panel as an MCP App, with cBioPortal | Later |

Items 7–10 come from the research on responsive grounded chat below.

**1. Citation contract** (`ai_search/mcp_instructions.md`). These
instructions reach every client, cBioPortal's agent included.
- Quotation marks only around exact paper text, checked with `verify_quote`.
- Every number (%, p-value, HR, n) comes from a passage, not a wiki summary or
  memory.
- Report figures from different papers separately; don't combine them into
  ranges.
- Name sources by the title and year the tools return.
- Tool results label their provenance: wiki pages as LLM summaries (not
  quotable), passages as verbatim paper text.

**2. `get_passage` and `verify_quote`** (`ai_search/mcp.py`). This is the same
pattern `dsbook-kb` uses.
- `get_passage(pmid, chunk_id)` returns the exact passage with its neighbours
  for context.
- `verify_quote(pmid, text)` string-matches against
  `data/raw/papers/{pmid}.md` after normalising whitespace, line-break
  hyphenation, Unicode minus and superscripts (`10-07` vs `10⁻⁷`). It needs
  no model. It returns the matching passage, or the closest candidates when
  there is no exact match.

**3. Re-chunk with anchors** (`src/cbio_kb/index/papers.py`, then a full
`index build-papers`). Now the most urgent item: see "Source text quality"
under the experiment below.
- Split on paragraphs within sections and overlap by whole sentences.
- Record `section`, `paragraph`, and `char_start`/`char_end` into the raw file.
- Drop reference lists and PMC manuscript boilerplate.
- Passages then get anchors like `PMID:18948947 §Results ¶12`, and
  `get_passage` can take the anchor.
- Changing chunking means a full rebuild. Re-run the retrieval eval to check
  recall didn't regress (`eval/`, as in the embedding bake-off).

*Done 2026-09-29.* What changed from the plan above:
- **Text source first.** 390 of 407 raw papers were PDF extractions with no
  headings and almost no paragraph breaks, so anchors needed a different
  source. `cbio-kb ingest bioc --replace` re-fetched PMC's BioC full text for
  every paper with a PMCID and moved the old files to
  `data/raw/papers_pre_bioc/` (all of `data/raw/papers` is also in
  `data/raw/papers-snapshot-2026-09-29.tar.gz`). 360 papers are BioC now; 47
  keep PDF or web text because NCBI has no BioC for them. BioC records without
  a PMID are accepted only when their DOI matches.
- **Anchors use the most specific heading** (`cbio_kb.index.passages`): the
  subsection if there is one, else the section, because BioC's section types
  put older Nature papers' results under "Introduction" or "Methods". The
  audit's KRAS figures now cite as `PMID:25079552 §Candidate driver genes ¶1`
  and `PMID:18948947 §Mutations correlated with clinical features ¶2`.
  Passages never cross a heading, and a recurring heading continues its
  paragraph numbering.
- **Offsets are into the paper's clean text** (kept paragraphs joined by blank
  lines), not the raw file: every passage's `text` is exactly
  `clean[char_start:char_end]`, so the MCP server rebuilds the text from
  `meta.jsonl` alone. Reference lists, author/funding/conflict statements,
  supplementary-file stubs, manuscript boilerplate and tab-separated data
  tables over 5,000 characters are dropped; a "sentence" spaCy can't split is
  cut at word boundaries, so no passage exceeds 900 characters.
- **Server.** Search results, `verify_quote` and `_closest` return `anchor`;
  `get_passage` takes `anchor` as well as `chunk_id`. Old-format indexes still
  load, but an older server reading the new index would repeat overlapping
  sentences, so deploy the code before the index.

Retrieval eval (`eval/embed_bakeoff.py`, Snowflake, 80 labeled questions,
same day, same corpus):

| Index | Passages | dense R@8 | dense R@40 | dense MRR | hybrid R@8 | BM25 + graph R@8 |
|---|---|---|---|---|---|---|
| Before (character overlap) | 41,155 | 0.733 | 0.823 | 0.775 | 0.704 | 0.708 |
| Anchored | 31,441 | 0.704 | 0.838 | 0.822 | 0.724 | 0.689 |

Hybrid, the server's default, gains 0.02; dense MRR gains 0.05; dense R@8
drops 0.03. Part of that drop is recall the old index shouldn't have had: for
the questions that got worse, 7 of the 32 gold hits in the old top 8 were
reference-list passages (all three for S02) and one was a grant
acknowledgement, none of them quotable. The previous index is kept in
`data/paper_index_pre_anchor/`.

Known limits: the 47 non-BioC papers still rely on layout heuristics, and a
structured abstract's "Conclusions" heading can label the body that follows
(PMID 38780927, which is also garbled). BioC text also fixed most garbled
papers: 17 still flag as garbled, down from 109, all among those 47.

**4. Deep links.** Every paper has a PMCID in its frontmatter, so a citation
can be a text-fragment link that opens PMC with the sentence highlighted:
`https://pmc.ncbi.nlm.nih.gov/articles/PMC2694412/#:~:text=KRAS%20mutations%20correlate%20with%20smoker%20status`.
It's best-effort: PMC's wording can differ slightly from our extraction, in
which case the link opens the paper without a highlight. The server should
build these links in tool output, not leave it to the model.

**5. Grounding score** (`eval/`). For each answer, extract claims containing
numbers and check each against the retrieved passages: share verbatim-supported,
share uncited, share not found in anything retrieved. Run it over
`eval/questions/v1.yaml` so each change above shows up as a number. The paused
claims extractor and `scripts/verify_paper.py` are a head start.

**6. Sentence-level provenance in the wiki.** The paper compiler and entity
page writer attach a passage anchor to each bullet, so even summary claims
point at a sentence. That's a tier-3 reprocess of every paper, so it's only
worth doing once 1–5 have shown the anchors hold up.

## Research: responsive grounded chat

Collected 2026-09-18, after verified quotes made the RAS answer take 111 s (6
model rounds, 16 tool calls, 9.7k characters). Our tools took a few seconds of
that; the model's sequential rounds and the length of the answer took the rest.

**What others converge on**

- *Answer first, short, then offer follow-ups.* Users treat AI chat like a
  search bar, skim, and want the essential answer first with follow-ups for the
  rest; ask clarifying questions only when ambiguity would give a wrong answer
  ([NN/g][nng]). OpenAI's Model Spec says to make a reasonable assumption, state
  it and answer ([Model Spec][spec]); unsatisfying conversations have more
  clarifying back-and-forth ([arXiv 2407.13166][clarify]).
- *Retrieve once, then write.* Perplexity assembles sources and citation markers
  into the prompt before generating, then streams ([ZipTie][pplx]). Multi-step
  agentic retrieval costs 16–22× the inference time of single-step retrieval,
  about 90% of it in the model's own thought and query generation
  ([LatentRAG][latent]).
- *Cite fewer things, better.* In deep-research agents, citation accuracy fell
  ~42% as tool calls grew from 2 to 150 while link validity stayed above 92%;
  selective citation beat exhaustive citation ([arXiv 2605.06635][cited]).
- *Stream now, verify after.* Gemini's double-check highlights sentences green
  or orange after the answer ([Gemini help][gemini]). For high-stakes domains, a
  NeurIPS 2025 comparison recommends retrieval-centric, post-hoc citation
  ([arXiv 2509.21557][gcite]). Anthropic's guide suggests drafting, then finding
  a supporting quote per claim and retracting claims without one
  ([Anthropic][halluc]).
- *Don't bury readers in provenance.* A full claim-by-claim evidence view
  lowered researchers' trust but didn't change what they did; checking every
  claim was too costly ([PaperTrail, CHI 2026][papertrail]).

**Tooling**

- *Anthropic `search_result` blocks* ([docs][searchres]). A tool returns sources
  as `search_result` blocks and Claude's citations carry `cited_text`, copied
  from the cited block by the API rather than written by the model, and not
  counted as output tokens. The citable unit is one text block, so passages
  would be split into sentences. Available on the Claude API, Bedrock and
  Google Cloud. MCP has no such content type, and clients drop these blocks
  (Anthropic's Agent SDK did until [#574][sdk574]), so today it fits `/ask`,
  where we make the API call, not LibreChat.
- *MCP Apps / mcp-ui* ([MCP Apps][apps], [mcp-ui][mcpui]). A server can render
  an evidence panel (quotes, verification badges, PMC links) in the chat while
  the prose stays short. Upstream LibreChat supports MCP Apps behind
  `mcpSettings.apps: true` ([#13831][lc13831]); cBioPortal's
  `v0.8.7-custom-v1` has only the legacy mcp-ui renderer, though their
  `v0.8.7-mcp-ui-meta` tag suggests they're exploring it.
- *Paraphrase support checks* (SemanticCite, groundedness evaluators;
  [overview][attr]) judge whether a paraphrase is backed by its source. They
  belong in item 5's eval rather than the live chat; `verify_quote` already
  covers verbatim quotes deterministically.

[nng]: https://www.nngroup.com/articles/less-chat-more-answer/
[spec]: https://model-spec.openai.com/2026-08-18.html
[clarify]: https://arxiv.org/html/2407.13166v1
[pplx]: https://ziptie.dev/blog/how-perplexity-ai-answers-work/
[latent]: https://arxiv.org/html/2605.06285v1
[cited]: https://arxiv.org/html/2605.06635v1
[gemini]: https://support.google.com/gemini/answer/14143489
[gcite]: https://arxiv.org/abs/2509.21557
[halluc]: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
[papertrail]: https://arxiv.org/abs/2602.21045
[searchres]: https://platform.claude.com/docs/en/build-with-claude/search-results
[sdk574]: https://github.com/anthropics/claude-agent-sdk-python/issues/574
[apps]: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
[mcpui]: https://github.com/MCP-UI-Org/mcp-ui
[lc13831]: https://github.com/danny-avila/LibreChat/pull/13831
[attr]: https://futureagi.com/blog/evaluating-llm-citation-attribution-2026/

## Experiment: answer-first instructions (item 7)

2026-09-18, local LibreChat, Claude Sonnet 4.6. Condition A is the committed
instructions; B adds an "Answer shape" section: lead with a 2–3 sentence
answer and at most five key findings, then offer follow-ups; don't open with a
clarifying question; gather evidence in parallel and verify quotes in one
batch. Four questions, two runs each, one at a time, timed from LibreChat's
event stream. Harness: `eval/chat_experiment/`. "Answer starts" is the first
answer text after the last tool call; n = 2 per cell, so treat small gaps as
noise.

| Question | Cond | Answer starts, s | Total, s | Tool calls | Model calls | Words | Quotes (verify) | Follow-up offer |
|---|---|---|---|---|---|---|---|---|
| Casual ("oi what papers you have") | A | 4 | 10 | 1 | 2 | 186 | 0 | 1/2 |
| | B | 4 | 9 | 1 | 2 | 134 | 0 | 2/2 |
| Lookup (RRAS2 in msk_impact_50k_2026) | A | 29 | 47 | 10 | 4 | 487 | 9 (7) | 0/2 |
| | B | 28 | 41 | 8 | 4 | 318 | 6 (5) | 2/2 |
| Open: RAS in late-stage lung cancer | A | 90 | 145 | 22 | 9 | 1,118 | 15 (13) | 0/2 |
| | B | 38 | 64 | 11 | 5 | 556 | 9 (9) | 2/2 |
| Open: STK11 and immunotherapy | A | 98 | 133 | 24 | 10 | 1,099 | 10 (9) | 0/2 |
| | B | 81 | 102 | 20 | 9 | 596 | 12 (6) | 2/2 |

Across all runs, B halved median time to the answer (52 → 28 s) and median
total time (88 → 49 s), halved answer length (791 → 404 words), used 37% fewer
input and output tokens, and offered follow-ups every time (1/8 → 8/8). The
casual and lookup questions barely changed; the open-ended ones gained most.
STK11 stayed slow in B (81 s to the answer, 9 model calls) because the question
spans many papers: evidence gathering, not writing, is its bottleneck.

Quotes verified at a similar rate (A 29/34, B 20/27; B's drop is one run). Of
the failures:

- **Source text quality.** 83 of 407 papers have badly garbled text in the
  passage index (over 50 run-together words per 1,000, e.g.
  `HighTMBcorrelateswithefficacyofPD`; 26 more moderately), from PDF
  extraction of multi-column layouts. No quote from them can verify, and BM25
  can't match run-together words either. 157 papers have reference numbers
  glued to words (`hotspot24`), which breaks exact quotes that drop them.
  Re-extracting these (PMC BioC XML: `cbio-kb ingest bioc`) belongs in item 3.
- **Unverified quotes kept anyway.** Claude sometimes kept a quotation after
  `verify_quote` rejected it (the STK11 sentence from PMID 29657128 in three
  answers; four rejected quotes in one B run), or quoted without checking.
  Instructions don't enforce this reliably; quotes need to come from the tools
  (item 8) or be checked after writing where the UI allows it (item 9).

**Follow-up fix (same day).** Search results, `get_passage` and
`verify_quote` now mark the 109 garbled papers with `text_quality: garbled`
(10+ run-together words per 1,000) and say to paraphrase them; `verify_quote`
ignores reference numbers glued to lowercase words ("hotspot24") while gene
symbols keep their digits. Rescoring the 16 answers, verified quotes went from
29/34 to 31/34 (A) and 20/27 to 21/27 (B), with no previously verified quote
lost. One rerun of the STK11 question paraphrased the garbled paper with its
PMID instead of quoting it; both of its quotes verified (answer at 55 s, 12
tool calls; n = 1). The remaining failures are real misquotes, which item 8
addresses.

## Baseline to beat

The audit above, repeated on the same question after each step: 5 claims with
numbers; 3 supported and cited, 1 correct but uncited, 1 misleading composite
using a number from outside the retrieved text; 0 marked as quotes.

## Results after steps 1 and 2

Same question, same model (Claude Sonnet 4.6), through LibreChat
(`deploy/librechat-local/`):

| Run | Tool calls | Quotes | Quotes that verify | Sentence links | Number lines without a citation |
|---|---|---|---|---|---|
| Baseline | 9 (no paper-text reads) | 0 | n/a | 0 | several; one invented range |
| Tools added; instructions not delivered (see below) | 8 | 0 | n/a | 0 | 4 |
| Instructions delivered, quotes allowed | 8 | 0 | n/a | 0 | 0; one population error (MSK-CHORD's 24,950 patients called LUAD) |
| Instructions ask for quotes | 16 (6 `verify_quote`) | 6 | 6/6 | 5 | 2 |

Claude links the quoted words themselves to PMC (`"[quote](pmc_link)"`), and
the linked sentences appear verbatim on PMC's pages. What's left is background
from memory: the therapy section still gave an uncited, misstated G12C figure.
Step 5's grounding score should count these.

**LibreChat drops server instructions for servers with per-user headers.** Its
startup inspection skips any server whose config has `{{LIBRECHAT_USER_*}}`
placeholders, so it never fetches the instructions and injects the literal
`true`. The local stack now gives cbio-kb no such headers (it doesn't use
them). The `deploy/cbioagent/` patches keep the headers and don't set
`serverInstructions`, so cBioPortal's agent never sees these instructions; it
gets only the tool descriptions, which now carry the short form of the rules.
Dropping the headers and setting `serverInstructions: true` there is a decision
for cBioPortal, since it adds ~4.6k characters to their agent's prompt.
