"""Answer-shape experiment against the local LibreChat stack (deploy/librechat-local/).

Condition A is the committed ai_search/mcp_instructions.md; condition B is the
working-tree version. For each condition: install that file in the cbio-kb-mcp
container, restart it and LibreChat, then run each question REPS times through
LibreChat's chat API, one at a time, timing every SSE event. Appends one JSON
line per run to <out dir>/results.jsonl; score it with analyze.py.

Chats run as the stack's first registered user, with a token signed by the
stack's own JWT_SECRET, and are marked temporary so they stay out of the sidebar.
Results for 2026-09-18 are in notes/GROUNDING.md.

usage: uv run --extra chat python eval/chat_experiment/run_experiment.py <out dir>
"""
import json
import re
import subprocess
import sys
import time
import uuid
from pathlib import Path

import httpx

SP = Path(sys.argv[1])
SP.mkdir(parents=True, exist_ok=True)
REPO = Path(__file__).resolve().parents[2]
COMPOSE = ["docker", "compose", "-f", str(REPO / "deploy/librechat-local/compose.yml")]
REPS = 2
QUESTIONS = {
    "casual": "oi what papers you have",
    "lookup": "What did the paper behind msk_impact_50k_2026 find about RRAS2?",
    "open_ras": "Tell me what you know about RAS and its relationship to late stage lung cancer",
    "open_stk11": "What does the literature say about STK11 and immunotherapy response in lung cancer?",
}
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")


def sh(*args, **kw):
    return subprocess.run(args, check=True, capture_output=True, text=True, **kw).stdout


def install(condition: str) -> str:
    src = SP / f"instructions_{condition}.md"
    if condition == "A":
        src.write_text(sh("git", "-C", str(REPO), "show", "HEAD:ai_search/mcp_instructions.md"))
    else:
        src.write_text((REPO / "ai_search/mcp_instructions.md").read_text())
    sh(*COMPOSE, "cp", str(src), "cbio-kb-mcp:/app/ai_search/mcp_instructions.md")
    since = time.time()
    sh(*COMPOSE, "restart", "cbio-kb-mcp")
    while "retrieval indexes warm" not in sh(*COMPOSE, "logs", "cbio-kb-mcp", "--since", str(int(since) - 5)):
        time.sleep(2)
    since = time.time()
    sh(*COMPOSE, "restart", "librechat")
    while True:
        logs = sh(*COMPOSE, "logs", "librechat", "--since", str(int(since) - 5))
        m = re.search(r"cbioportal-literature\] Server Instructions: configured \((\d+) chars\)", logs)
        if m and "Server listening" in logs:
            return f"{m.group(1)} chars loaded (file {len(src.read_text())} chars)"
        time.sleep(2)


def token() -> str:
    """A short-lived LibreChat JWT for the stack's first user (no password involved)."""
    return sh(*COMPOSE, "exec", "-T", "librechat", "node", "-e",
              "const {MongoClient}=require('/app/node_modules/mongodb');"
              "const jwt=require('/app/node_modules/jsonwebtoken');"
              "(async()=>{const c=await MongoClient.connect(process.env.MONGO_URI);"
              "const u=await c.db().collection('users').findOne({},{sort:{_id:1}});"
              "console.log(jwt.sign({id:String(u._id),username:u.username,provider:u.provider,"
              "email:u.email},process.env.JWT_SECRET,{expiresIn:'3h'}));await c.close();})()").strip()


def run(question: str, tok: str) -> dict:
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json", "User-Agent": UA}
    body = {"text": question, "sender": "User", "isCreatedByUser": True,
            "parentMessageId": "00000000-0000-0000-0000-000000000000",
            "conversationId": str(uuid.uuid4()), "messageId": str(uuid.uuid4()), "error": False,
            "generation": "", "responseMessageId": None, "overrideParentMessageId": None,
            "endpoint": "anthropic", "model": "claude-sonnet-4-6", "spec": "cbio-kb-local",
            "modelLabel": "cBioPortal Literature", "maxContextTokens": 200000, "promptCache": True,
            "isContinued": False, "isTemporary": True,
            "ephemeralAgent": {"mcp": ["cbioportal-literature"], "execute_code": False,
                               "web_search": False, "file_search": False}}
    ev: list[tuple[float, str, dict]] = []
    final = None
    t0 = time.perf_counter()
    with httpx.Client(base_url="http://localhost:3080", headers=headers, timeout=900) as c:
        sid = c.post("/api/agents/chat/anthropic", json=body).json()["streamId"]
        with c.stream("GET", f"/api/agents/chat/stream/{sid}") as s:
            for line in s.iter_lines():
                if not line.startswith("data:"):
                    continue
                t = time.perf_counter() - t0
                try:
                    d = json.loads(line[5:])
                except json.JSONDecodeError:
                    continue
                if d.get("final"):
                    final = d
                    ev.append((t, "final", {}))
                    break
                ev.append((t, d.get("event", "?"), d.get("data") or {}))
    return summarize(ev, final)


def summarize(ev, final) -> dict:
    first = lambda names: next((t for t, n, _ in ev if n in names), None)
    tools, tool_rounds, done = [], [], []
    tin = tout = cache = llm_calls = 0
    for t, n, d in ev:
        if n == "on_run_step" and d.get("type") == "tool_calls":
            names = [tc.get("name", "").split("_mcp_")[0] for tc in d["stepDetails"]["tool_calls"]]
            tools += names
            tool_rounds.append(t)
        elif n == "on_run_step_completed":
            done.append(t)
        elif n == "on_token_usage":
            llm_calls += 1
            tin += d.get("input_tokens", 0)
            tout += d.get("output_tokens", 0)
            cache += (d.get("input_token_details") or {}).get("cache_read", 0)
    last_done = max(done) if done else 0.0
    answer_start = next((t for t, n, _ in ev if n == "on_message_delta" and t > last_done), None)
    text = ""
    if final and final.get("responseMessage"):
        text = "".join(p.get("text", "") for p in final["responseMessage"].get("content") or []
                       if p.get("type") == "text")
    errors = [p for p in ((final or {}).get("responseMessage") or {}).get("content") or []
              if p.get("type") == "error"]
    return {"first_visible_s": first({"on_reasoning_delta", "on_message_delta"}),
            "first_text_s": first({"on_message_delta"}), "answer_start_s": answer_start,
            "total_s": ev[-1][0] if ev else None, "tool_calls": tools, "tool_steps": len(tool_rounds),
            "llm_calls": llm_calls, "input_tokens": tin, "output_tokens": tout, "cache_read_tokens": cache,
            "answer": text, "errors": len(errors)}


def main() -> None:
    out = SP / "results.jsonl"
    for condition in ("A", "B"):
        loaded = install(condition)
        print(f"[{time.strftime('%H:%M:%S')}] condition {condition}: {loaded}", flush=True)
        tok = token()
        for rep in range(1, REPS + 1):
            for qid, q in QUESTIONS.items():
                r = run(q, tok)
                r.update(condition=condition, question=qid, rep=rep)
                with out.open("a") as fh:
                    fh.write(json.dumps(r) + "\n")
                fmt = lambda v: "-" if v is None else f"{v:.0f}s"
                print(f"[{time.strftime('%H:%M:%S')}] {condition} {qid} rep{rep}: "
                      f"answer starts {fmt(r['answer_start_s'])}, total {fmt(r['total_s'])}, "
                      f"{len(r['tool_calls'])} tools, {len(r['answer'])} chars, errors {r['errors']}", flush=True)


if __name__ == "__main__":
    main()
