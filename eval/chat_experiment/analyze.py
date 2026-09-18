"""Score run_experiment.py's results.jsonl: timing, answer size, quotes
(re-verified against the paper each quote links to), lines with uncited
numbers, and follow-up offers. Writes scored.json next to the input.

usage: PYTHONPATH=. uv run --extra chat --extra mcp python eval/chat_experiment/analyze.py <out dir>/results.jsonl
"""
import json
import re
import statistics as st
import sys
from pathlib import Path

import ai_search.mcp as m

rows = [json.loads(l) for l in Path(sys.argv[1]).read_text().splitlines() if l.strip()]
papers = m.catalog().papers
pmc2pmid = {p.pmcid: p.pmid for p in papers.values() if p.pmcid}
NUM = re.compile(r"\d+(?:\.\d+)?\s?%|[Pp]\s?[<=]\s?\d|\bHR\s?[=:]?\s?\d|\bn\s?=\s?\d")
CITE = re.compile(r"PMID|pubmed\.ncbi|pmc\.ncbi")
FOLLOW = re.compile(r"(?i)(want me to|would you like|i can (also )?\w+|happy to|let me know|"
                    r"go deeper|dig (deeper|into)|follow[- ]up|explore further|\?\s*$)")


def quotes(answer: str) -> tuple[int, int]:
    n = ok = 0
    for mq in re.finditer(r"[\"“]([^\"”\n]{20,700})[\"”]", answer):
        q = mq.group(1)
        link = re.fullmatch(r"\[(.+)\]\((https?://[^)]+)\)[.,;]?", q)
        text, url = (link.group(1), link.group(2)) if link else (q, None)
        after = answer[mq.end():mq.end() + 400]
        pmid = None
        u = url or (re.search(r"https://pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)", after) or [None])[0]
        if u and (pc := re.search(r"PMC\d+", u)):
            pmid = pmc2pmid.get(pc.group(0))
        if pmid is None and (pm := re.search(r"(?:PMID[:\s]*|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,9})", after)):
            pmid = pm.group(1)
        if pmid is None:
            continue  # a term in quote marks, not a cited quotation
        n += 1
        ok += bool(m.verify_quote(pmid, text).get("verified"))
    return n, ok


for r in rows:
    a = r["answer"]
    r["words"] = len(a.split())
    r["quotes"], r["quotes_ok"] = quotes(a)
    r["sentence_links"] = len(re.findall(r"pmc\.ncbi\.nlm\.nih\.gov/articles/PMC\d+/#:~:text=", a))
    lines = [l for l in a.splitlines() if NUM.search(l)]
    r["uncited_number_lines"] = sum(1 for l in lines if not CITE.search(l))
    r["follow_up"] = bool(FOLLOW.search(a[-700:]))
    r["clarified_only"] = not r["tool_calls"] and a.rstrip().endswith("?")

f = lambda xs: "-" if not xs else (f"{xs[0]:.0f}" if len(xs) == 1 else f"{st.mean(xs):.0f} ({'/'.join(f'{x:.0f}' for x in xs)})")
print("| Question | Cond | Answer starts, s | Total, s | Tool calls | Model calls | Output tokens | Words | Quotes (verify) | Uncited number lines | Follow-up offer | Errors |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
for q in dict.fromkeys(r["question"] for r in rows):
    for c in ("A", "B"):
        g = [r for r in rows if r["question"] == q and r["condition"] == c]
        if not g:
            continue
        col = lambda k: [r[k] for r in g if r[k] is not None]
        print(f"| {q} | {c} | {f(col('answer_start_s'))} | {f(col('total_s'))} | "
              f"{f([len(r['tool_calls']) for r in g])} | {f(col('llm_calls'))} | {f(col('output_tokens'))} | "
              f"{f(col('words'))} | {sum(r['quotes'] for r in g)} ({sum(r['quotes_ok'] for r in g)}) | "
              f"{sum(r['uncited_number_lines'] for r in g)} | {sum(r['follow_up'] for r in g)}/{len(g)} | "
              f"{sum(r['errors'] for r in g)} |")
print()
for c in ("A", "B"):
    g = [r for r in rows if r["condition"] == c]
    if g:
        print(f"{c}: median answer start {st.median(r['answer_start_s'] for r in g if r['answer_start_s']):.0f}s, "
              f"median total {st.median(r['total_s'] for r in g):.0f}s, median words {st.median(r['words'] for r in g):.0f}, "
              f"quotes {sum(r['quotes'] for r in g)} ({sum(r['quotes_ok'] for r in g)} verify), "
              f"follow-up offers {sum(r['follow_up'] for r in g)}/{len(g)}, "
              f"input tokens {sum(r['input_tokens'] for r in g):,}, output tokens {sum(r['output_tokens'] for r in g):,}")
json.dump(rows, open(Path(sys.argv[1]).with_name("scored.json"), "w"), indent=1)
