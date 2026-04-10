"""History processor for the wiki chat agent.

Memory policy
-------------
The agent already has strong navigation tools (``read_page``, ``search``,
``follow_links``…) so it can always re-fetch a page it has seen before.
That means old tool results are *pure cost* — they bloat the prompt, slow
the request, and contribute nothing the agent can't recover cheaply.

This processor keeps conversational context intact while stripping bulky,
stale tool payloads:

1. **Last N user turns** are preserved verbatim — full tool results included,
   so the model can reason over what it just fetched.
2. **Older turns** keep their text (user prompts, assistant replies) and
   the tool-call *signatures* (so the model still knows what it has looked
   at), but tool-return *payloads* are replaced with a short stub.
3. Nothing is dropped entirely — the turn structure is preserved so
   PydanticAI's message pairing stays valid.

No rolling summary, no persistence. If the conversation outgrows the
window, raise ``KEEP_RECENT_TURNS`` or add a summarizer later.
"""
from __future__ import annotations

from dataclasses import replace

from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ToolReturnPart,
    UserPromptPart,
)

KEEP_RECENT_TURNS = 3
TOOL_RESULT_STUB = (
    "[previously retrieved — re-run the tool if you need this again]"
)


def _is_user_turn_start(msg: ModelMessage) -> bool:
    """A user turn begins with a ModelRequest containing a UserPromptPart."""
    if not isinstance(msg, ModelRequest):
        return False
    return any(isinstance(p, UserPromptPart) for p in msg.parts)


def _strip_tool_results(msg: ModelMessage) -> ModelMessage:
    """Replace any ToolReturnPart content with the stub."""
    if not isinstance(msg, ModelRequest):
        return msg
    new_parts = []
    changed = False
    for part in msg.parts:
        if isinstance(part, ToolReturnPart):
            new_parts.append(replace(part, content=TOOL_RESULT_STUB))
            changed = True
        else:
            new_parts.append(part)
    if not changed:
        return msg
    return replace(msg, parts=new_parts)


def prune_history(messages: list[ModelMessage]) -> list[ModelMessage]:
    """Strip tool results from all turns older than the most recent KEEP_RECENT_TURNS.

    This is the ``history_processors`` hook — PydanticAI calls it before
    every model request.
    """
    turn_starts = [i for i, m in enumerate(messages) if _is_user_turn_start(m)]
    if len(turn_starts) <= KEEP_RECENT_TURNS:
        return messages

    cutoff = turn_starts[-KEEP_RECENT_TURNS]
    return [
        _strip_tool_results(m) if i < cutoff else m
        for i, m in enumerate(messages)
    ]
