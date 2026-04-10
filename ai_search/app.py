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

from .agent import Deps, ToolEvent, agent

# Force tool registration
from . import tools as _tools  # noqa: F401

_HERE = Path(__file__).resolve().parent

app = FastAPI(title="cbio-kb Chat")
app.mount("/static", StaticFiles(directory=_HERE / "static"), name="static")
templates = Jinja2Templates(directory=_HERE / "templates")

# In-memory conversation history keyed by session id
_sessions: dict[str, list] = {}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body["message"]
    session_id = body.get("session_id") or str(uuid.uuid4())
    history = _sessions.get(session_id, [])

    async def event_generator():
        tool_queue: asyncio.Queue[ToolEvent | None] = asyncio.Queue()
        sse_queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()

        deps = Deps(tool_queue=tool_queue)

        async def run_agent():
            try:
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
                    _sessions[session_id] = run.result.all_messages()
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
