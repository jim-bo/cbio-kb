"""Export a merged, chronological Markdown transcript of a Claude Code session.

Stitches together the main session JSONL plus every sub-agent JSONL under
`<session>/subagents/` into one human-readable log.

Usage:
    uv run cbio-kb logs export --session <uuid> --out logs/foo.md
    uv run cbio-kb logs export --latest --out logs/foo.md
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

PROJECT_DIR = Path.home() / ".claude" / "projects" / "-Users-jlindsay-Code-cbioportal-cbio-vec"


def _latest_session() -> str:
    candidates = [p for p in PROJECT_DIR.glob("*.jsonl")]
    if not candidates:
        raise SystemExit(f"no sessions under {PROJECT_DIR}")
    newest = max(candidates, key=lambda p: p.stat().st_mtime)
    return newest.stem


def _iter_records(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def _fmt_content(content, *, truncate: int = 2000) -> str:
    """Render a message content block (str or list of blocks) as markdown."""
    if isinstance(content, str):
        return content[:truncate] + (" …[truncated]" if len(content) > truncate else "")
    if not isinstance(content, list):
        return repr(content)[:truncate]
    parts = []
    for block in content:
        if not isinstance(block, dict):
            parts.append(str(block))
            continue
        btype = block.get("type")
        if btype == "text":
            txt = block.get("text", "")
            parts.append(txt[:truncate] + (" …[truncated]" if len(txt) > truncate else ""))
        elif btype == "thinking":
            txt = block.get("thinking", "")
            parts.append(f"> **[thinking]** {txt[:truncate]}")
        elif btype == "tool_use":
            name = block.get("name")
            inp = json.dumps(block.get("input", {}), indent=2, default=str)
            if len(inp) > truncate:
                inp = inp[:truncate] + " …[truncated]"
            parts.append(f"**→ tool_use: `{name}`**\n```json\n{inp}\n```")
        elif btype == "tool_result":
            raw = block.get("content", "")
            if isinstance(raw, list):
                raw = "\n".join(
                    b.get("text", "") if isinstance(b, dict) else str(b) for b in raw
                )
            raw = str(raw)
            if len(raw) > truncate:
                raw = raw[:truncate] + f" …[truncated, {len(raw)} chars total]"
            parts.append(f"**← tool_result**\n```\n{raw}\n```")
        else:
            parts.append(f"[{btype}] {json.dumps(block, default=str)[:truncate]}")
    return "\n\n".join(parts)


def _record_events(path: Path, source_label: str):
    """Yield (timestamp, source_label, record) for message-bearing records."""
    for r in _iter_records(path):
        if r.get("type") not in ("user", "assistant"):
            continue
        ts = r.get("timestamp", "")
        yield ts, source_label, r


def export(session_id: str, out_path: Path, *, truncate: int = 2000) -> None:
    main_path = PROJECT_DIR / f"{session_id}.jsonl"
    if not main_path.exists():
        raise SystemExit(f"session not found: {main_path}")

    subagent_dir = PROJECT_DIR / session_id / "subagents"
    events = list(_record_events(main_path, "main"))

    if subagent_dir.exists():
        for sub in sorted(subagent_dir.glob("agent-*.jsonl")):
            label = f"subagent:{sub.stem}"
            events.extend(_record_events(sub, label))

    events.sort(key=lambda e: (e[0] or ""))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as out:
        out.write(f"# Session transcript `{session_id}`\n\n")
        out.write(f"- Main: `{main_path}`\n")
        out.write(f"- Sub-agents: {len(list(subagent_dir.glob('agent-*.jsonl'))) if subagent_dir.exists() else 0}\n")
        out.write(f"- Total message records: {len(events)}\n\n---\n\n")

        last_source = None
        for ts, source, r in events:
            if source != last_source:
                out.write(f"\n## === {source} ===\n\n")
                last_source = source
            msg = r.get("message", {})
            role = msg.get("role", r.get("type", "?")) if isinstance(msg, dict) else "?"
            content = msg.get("content", "") if isinstance(msg, dict) else ""
            out.write(f"### {role} — {ts}\n\n")
            out.write(_fmt_content(content, truncate=truncate))
            out.write("\n\n")

    print(f"wrote {out_path} ({len(events)} records)")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="cbio-kb logs export")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--session", help="session UUID")
    g.add_argument("--latest", action="store_true", help="use most recent session")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--truncate", type=int, default=2000,
                    help="max chars per content block (default 2000)")
    args = ap.parse_args(argv)
    sid = _latest_session() if args.latest else args.session
    export(sid, args.out, truncate=args.truncate)


if __name__ == "__main__":
    main()
