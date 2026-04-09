"""Tests for logs.export content formatting."""
from __future__ import annotations

from cbio_kb.logs.export import _fmt_content


def test_fmt_text_block() -> None:
    out = _fmt_content([{"type": "text", "text": "hello"}])
    assert "hello" in out


def test_fmt_thinking_block() -> None:
    out = _fmt_content([{"type": "thinking", "thinking": "inner"}])
    assert "[thinking]" in out and "inner" in out


def test_fmt_tool_use_and_result() -> None:
    blocks = [
        {"type": "tool_use", "name": "Bash", "input": {"command": "ls"}},
        {"type": "tool_result", "content": "a\nb\n"},
    ]
    out = _fmt_content(blocks)
    assert "tool_use" in out and "Bash" in out
    assert "tool_result" in out and "a\nb" in out


def test_fmt_truncates_long_text() -> None:
    long = "x" * 5000
    out = _fmt_content([{"type": "text", "text": long}], truncate=100)
    assert "[truncated]" in out
    assert len(out) < 300
