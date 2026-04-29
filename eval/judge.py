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


def _citation_score(gold_pmids: list, cited_pmids: list) -> int:
    """Deterministic 1-5 score for citation overlap.

    The judge model is unreliable for this — gold and cited PMIDs are
    both already structured data, so compute the score from them
    directly to keep the metric reproducible.
    """
    gold = {str(p) for p in (gold_pmids or [])}
    cited = {str(p) for p in (cited_pmids or [])}
    if not gold:
        return 5 if not cited else 3
    if not cited:
        return 1
    if cited == gold:
        return 5
    if cited.isdisjoint(gold):
        return 1
    diff = len(cited ^ gold)
    if diff == 1:
        return 4
    if diff <= 3:
        return 3
    return 2


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

    deterministic_citation = _citation_score(
        question_entry.get("gold_pmids", []),
        run_result.get("cited_pmids", []),
    )

    try:
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model=_JUDGE_MODEL,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()
    except Exception as exc:
        return {
            "accuracy": 0,
            "completeness": 0,
            "citation_correctness": deterministic_citation,
            "reasoning": f"judge error: {type(exc).__name__}: {exc}",
        }

    m = _JSON_RE.search(text)
    if not m:
        return {
            "accuracy": 0,
            "completeness": 0,
            "citation_correctness": deterministic_citation,
            "reasoning": f"parse error: {text[:200]}",
        }

    try:
        scores = json.loads(m.group())
    except json.JSONDecodeError as exc:
        return {
            "accuracy": 0,
            "completeness": 0,
            "citation_correctness": deterministic_citation,
            "reasoning": f"parse error: {exc}",
        }

    for k in ("accuracy", "completeness", "citation_correctness"):
        scores.setdefault(k, 0)
    # Override the model's citation_correctness with the deterministic
    # score — keeps the aggregate citation metric reproducible.
    scores["citation_correctness"] = deterministic_citation
    return scores
