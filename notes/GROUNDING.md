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
| 3 | Re-chunk the passage index with anchors | To do |
| 4 | Links that land on the quoted sentence | To do |
| 5 | Grounding score in the eval | To do |
| 6 | Sentence-level provenance in the wiki | Later |

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
`index build-papers`).
- Split on paragraphs within sections and overlap by whole sentences.
- Record `section`, `paragraph`, and `char_start`/`char_end` into the raw file.
- Drop reference lists and PMC manuscript boilerplate.
- Passages then get anchors like `PMID:18948947 §Results ¶12`, and
  `get_passage` can take the anchor.
- Changing chunking means a full rebuild. Re-run the retrieval eval to check
  recall didn't regress (`eval/`, as in the embedding bake-off).

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
