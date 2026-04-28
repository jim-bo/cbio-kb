"""Shared runner logic — hit /api/chat SSE endpoint, collect structured results."""
from __future__ import annotations

import json
import re
import time

import httpx

_API_BASE = "http://localhost:8080"
# PMIDs can appear as `PMID:39506116`, `PMID 39506116`, or as wiki links
# like `[title](papers/39506116.html)` / `papers/39506116.md`. All three
# forms count as a citation for the purposes of recall.
_PMID_RE = re.compile(r"PMID[:\s]*(\d{7,8})|papers/(\d{7,8})\.(?:html|md)")


def _extract_pmids(text: str) -> list[str]:
    pmids: list[str] = []
    for m in _PMID_RE.finditer(text):
        pmid = m.group(1) or m.group(2)
        if pmid and pmid not in pmids:
            pmids.append(pmid)
    return sorted(pmids)


def run_question(
    question: str,
    mode: str,
    *,
    api_base: str = _API_BASE,
    timeout: float = 180.0,
) -> dict:
    """Send a question to /api/chat in the given mode, return structured result.

    ``timeout`` is the wall-clock deadline for the entire stream. If the
    server keeps trickling bytes past it, we stop reading and flag the
    record with ``timed_out: true``.
    """
    t0 = time.monotonic()
    deadline = t0 + timeout
    answer_parts: list[str] = []
    tool_uses: list[dict] = []
    tool_timeline: list[dict] = []
    retrieval: list[dict] = []
    usage: dict = {}
    retrieved_sources: list[str] = []
    timed_out = False
    tool_limit_reached = False
    llm_calls = None
    error = None

    with httpx.Client(timeout=timeout) as client:
        with client.stream(
            "POST",
            f"{api_base}/api/chat",
            json={"message": question, "mode": mode},
        ) as resp:
            resp.raise_for_status()
            event_type = None
            for line in resp.iter_lines():
                if time.monotonic() > deadline:
                    timed_out = True
                    break
                if line.startswith("event: "):
                    event_type = line[7:]
                elif line.startswith("data: ") and event_type:
                    data = json.loads(line[6:])
                    if event_type == "text":
                        answer_parts.append(data.get("delta", ""))
                    elif event_type == "error":
                        error = data.get("error") or json.dumps(data, ensure_ascii=False)
                    elif event_type == "tool_use":
                        tool_uses.append(data)
                        for p in data.get("result_paths", []):
                            if p not in retrieved_sources:
                                retrieved_sources.append(p)
                        tool_timeline.append({
                            "name": data.get("name"),
                            "args": data.get("args", {}),
                            "t_start": data.get("t_start", 0.0),
                            "t_end": data.get("t_end", 0.0),
                            "chars": data.get("chars", 0),
                            "summary": data.get("summary"),
                        })
                        if data.get("name") == "vector_search" and data.get("results"):
                            retrieval = data["results"]
                    elif event_type == "tool_limit_reached":
                        tool_limit_reached = True
                    elif event_type == "done":
                        for k in ("input_tokens", "output_tokens"):
                            if k in data:
                                usage[k] = data[k]
                        if "llm_calls" in data:
                            llm_calls = data["llm_calls"]
                        if data.get("tool_limit_reached"):
                            tool_limit_reached = True
                    event_type = None

    wall_time = time.monotonic() - t0
    answer = "".join(answer_parts)
    cited_pmids = _extract_pmids(answer)

    result = {
        "mode": mode,
        "question": question,
        "answer": answer,
        "cited_pmids": cited_pmids,
        "retrieved_sources": retrieved_sources,
        "tool_uses": len(tool_uses),
        "tool_timeline": tool_timeline,
        "wall_time_s": round(wall_time, 2),
        **usage,
    }
    if retrieval:
        result["retrieval"] = retrieval
    if llm_calls is not None:
        result["llm_calls"] = llm_calls
    if timed_out:
        result["timed_out"] = True
    if tool_limit_reached:
        result["tool_limit_reached"] = True
    if error:
        result["error"] = error
    return result
