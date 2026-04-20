"""Opus-based rubric judge for RAG-vs-agentic evaluation.

Scores each (question, answer) pair on three dimensions (1-5):
  - accuracy:              factual correctness relative to gold notes
  - completeness:          coverage of gold PMIDs and entities
  - citation_correctness:  cited PMIDs match gold, no hallucinated citations
"""
from __future__ import annotations

import json
import re

import anthropic
from dotenv import load_dotenv

load_dotenv()

_JUDGE_MODEL = "claude-opus-4-6"

_RUBRIC = """\
You are a strict scientific evaluator. Score the ANSWER to the QUESTION
on three dimensions, each 1-5.

## Scoring rubric

### accuracy (factual correctness)
5 = all facts correct and precise
4 = minor imprecision but no wrong facts
3 = mostly correct, one notable error
2 = multiple errors or misleading claims
1 = fundamentally wrong

### completeness (coverage)
5 = covers all gold PMIDs/entities, nothing missing
4 = covers most, one minor gap
3 = covers roughly half
2 = significant gaps
1 = barely addresses the question

### citation_correctness (source attribution)
5 = all cited PMIDs are in the gold set, no extras
4 = one extra or missing citation
3 = several extra or missing citations
2 = mostly wrong citations
1 = no citations or all hallucinated

## Inputs

QUESTION: {question}

GOLD NOTES: {notes}

GOLD PMIDs: {gold_pmids}

GOLD ENTITIES: {gold_entities}

ANSWER TO EVALUATE:
{answer}

CITED PMIDs IN ANSWER: {cited_pmids}

## Output format

Return ONLY a JSON object, no markdown fencing:
{{"accuracy": <int>, "completeness": <int>, "citation_correctness": <int>, "reasoning": "<1-2 sentences>"}}
"""

_JSON_RE = re.compile(r"\{[^{}]*\}", re.DOTALL)


def judge(question_entry: dict, run_result: dict) -> dict:
    """Score a single run result against its gold labels. Returns scores dict."""
    prompt = _RUBRIC.format(
        question=question_entry["question"],
        notes=question_entry.get("notes", "N/A"),
        gold_pmids=", ".join(str(p) for p in question_entry.get("gold_pmids", [])),
        gold_entities=", ".join(question_entry.get("gold_entities", [])),
        answer=run_result["answer"],
        cited_pmids=", ".join(run_result.get("cited_pmids", [])),
    )

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=_JUDGE_MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()

    m = _JSON_RE.search(text)
    if not m:
        return {"accuracy": 0, "completeness": 0, "citation_correctness": 0, "reasoning": f"parse error: {text[:200]}"}

    scores = json.loads(m.group())
    for k in ("accuracy", "completeness", "citation_correctness"):
        scores.setdefault(k, 0)
    return scores
