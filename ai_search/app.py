"""FastAPI application with SSE streaming for the wiki chat agent."""
from __future__ import annotations

import asyncio
import json
import uuid
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic_ai import Agent
from pydantic_ai.messages import (
    PartDeltaEvent,
    PartStartEvent,
    TextPart,
    TextPartDelta,
)
from sse_starlette.sse import EventSourceResponse

from .agent import SYSTEM_PROMPT, Deps, ToolEvent, agent
from .memory import KEEP_RECENT_TURNS
from .sessions import get_store

# Force tool registration
from . import tools as _tools  # noqa: F401

_HERE = Path(__file__).resolve().parent

app = FastAPI(title="cbio-kb Chat")
app.mount("/static", StaticFiles(directory=_HERE / "static"), name="static")
templates = Jinja2Templates(directory=_HERE / "templates")

# Session store — in-memory by default, Firestore when SESSION_STORE=firestore
_session_store = get_store()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body["message"]
    session_id = body.get("session_id") or str(uuid.uuid4())
    history = await _session_store.get(session_id) or []

    # Count previous user turns to derive this turn's index. The frontend
    # uses this to decide which older cards to dim as pruned (anything
    # older than KEEP_RECENT_TURNS).
    from .memory import _is_user_turn_start  # noqa: PLC0415
    prior_turns = sum(1 for m in history if _is_user_turn_start(m))
    turn_index = prior_turns  # zero-based: 0 on first turn

    async def event_generator():
        tool_queue: asyncio.Queue[ToolEvent | None] = asyncio.Queue()
        sse_queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()

        deps = Deps(tool_queue=tool_queue)

        async def run_agent():
            try:
                # On the first turn of a session, emit the system prompt as
                # a context block. It stays in the context forever (re-sent
                # with every API request) so we only render it once in the
                # UI and let it persist.
                if turn_index == 0:
                    sys_chars = len(SYSTEM_PROMPT)
                    await sse_queue.put((
                        "context_system",
                        json.dumps({
                            "content": SYSTEM_PROMPT,
                            "chars": sys_chars,
                            "tokens": max(1, sys_chars // 4),
                        }),
                    ))

                # Announce the start of a new turn so the frontend can
                # re-evaluate which prior tool cards are now "pruned".
                await sse_queue.put((
                    "turn_start",
                    json.dumps({
                        "turn_index": turn_index,
                        "keep_recent": KEEP_RECENT_TURNS,
                    }),
                ))

                # Emit the user message as the next context block, tagged
                # with its turn index so the frontend can group & prune.
                await sse_queue.put((
                    "context_user",
                    json.dumps({
                        "content": user_message,
                        "chars": len(user_message),
                        "tokens": max(1, len(user_message) // 4),
                        "turn_index": turn_index,
                    }),
                ))

                async with agent.iter(
                    user_message,
                    deps=deps,
                    message_history=history or None,
                ) as run:
                    async for node in run:
                        if Agent.is_model_request_node(node):
                            async with node.stream(run.ctx) as request_stream:
                                async for event in request_stream:
                                    delta = None
                                    if isinstance(event, PartStartEvent) and isinstance(
                                        event.part, TextPart
                                    ):
                                        delta = event.part.content
                                    elif isinstance(event, PartDeltaEvent) and isinstance(
                                        event.delta, TextPartDelta
                                    ):
                                        delta = event.delta.content_delta
                                    if delta:
                                        await sse_queue.put((
                                            "text",
                                            json.dumps({"delta": delta}),
                                        ))
                # Save updated history
                if run.result is not None:
                    await _session_store.put(
                        session_id, run.result.all_messages()
                    )
            except Exception as e:
                await sse_queue.put(("error", json.dumps({"error": str(e)})))
            finally:
                await tool_queue.put(None)
                await sse_queue.put(("done", json.dumps({"session_id": session_id})))

        async def drain_tools():
            while True:
                event = await tool_queue.get()
                if event is None:
                    break
                await sse_queue.put((
                    "tool_use",
                    json.dumps({
                        "name": event.tool_name,
                        "args": event.args,
                        "preview": event.result_preview,
                        "summary": event.summary,
                        "chars": event.result_chars,
                        "tokens": event.result_tokens,
                        "turn_index": turn_index,
                    }),
                ))

        agent_task = asyncio.create_task(run_agent())
        tool_task = asyncio.create_task(drain_tools())

        while True:
            event_type, data = await sse_queue.get()
            yield {"event": event_type, "data": data}
            if event_type == "done":
                break

        await asyncio.gather(agent_task, tool_task)

    return EventSourceResponse(event_generator())
