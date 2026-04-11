"""Session storage for chat history.

The session store is an async key/value interface that the chat endpoint
uses to persist per-session PydanticAI ``ModelMessage`` history. A thin
protocol lets us swap between a local in-memory dict (dev) and Firestore
(Cloud Run deployment) without touching the rest of the app.

Backend selection
-----------------
The ``SESSION_STORE`` environment variable picks the implementation:

- unset / ``"memory"`` → :class:`InMemorySessionStore` (default)
- ``"firestore"`` → :class:`FirestoreSessionStore` (requires the
  ``cloud`` optional-deps group — ``pip install cbio-kb[cloud]``)

Firestore auth uses Application Default Credentials. On Cloud Run the
service account is picked up automatically; locally you can
``gcloud auth application-default login`` if you ever need to exercise
this path.

Firestore TTL
-------------
Each doc carries a ``ttl`` timestamp field 24 hours in the future. Enable
the TTL policy once per collection via gcloud so stale sessions self-
delete::

    gcloud firestore fields ttls update ttl \\
        --collection-group=sessions --enable-ttl
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Protocol, runtime_checkable

from pydantic_ai.messages import ModelMessage, ModelMessagesTypeAdapter

SESSION_TTL = timedelta(hours=24)
DEFAULT_COLLECTION = "sessions"


@runtime_checkable
class SessionStore(Protocol):
    """Minimal async CRUD surface for chat sessions."""

    async def get(self, session_id: str) -> list[ModelMessage] | None: ...
    async def put(
        self, session_id: str, messages: list[ModelMessage]
    ) -> None: ...
    async def delete(self, session_id: str) -> None: ...


class InMemorySessionStore:
    """Process-local dict store — fine for dev, lost on restart.

    Not shared across workers, not shared across Cloud Run instances.
    Use :class:`FirestoreSessionStore` for anything that needs to
    survive scale-to-zero.
    """

    def __init__(self) -> None:
        self._data: dict[str, list[ModelMessage]] = {}

    async def get(self, session_id: str) -> list[ModelMessage] | None:
        return self._data.get(session_id)

    async def put(
        self, session_id: str, messages: list[ModelMessage]
    ) -> None:
        self._data[session_id] = list(messages)

    async def delete(self, session_id: str) -> None:
        self._data.pop(session_id, None)


class FirestoreSessionStore:
    """Firestore-backed store. Documents live under a single collection.

    The message history is serialized to JSON via PydanticAI's
    ``ModelMessagesTypeAdapter`` so the underlying shape stays portable
    (no pickling of arbitrary Python objects).
    """

    def __init__(self, collection: str = DEFAULT_COLLECTION) -> None:
        # Imported lazily so the module works without the `cloud` extra
        # installed when running with the in-memory backend.
        from google.cloud.firestore import AsyncClient  # type: ignore

        self._client = AsyncClient()
        self._collection = collection

    def _doc(self, session_id: str):
        return self._client.collection(self._collection).document(session_id)

    async def get(self, session_id: str) -> list[ModelMessage] | None:
        snap = await self._doc(session_id).get()
        if not snap.exists:
            return None
        raw = snap.get("messages")
        if not raw:
            return None
        return list(ModelMessagesTypeAdapter.validate_json(raw))

    async def put(
        self, session_id: str, messages: list[ModelMessage]
    ) -> None:
        now = datetime.now(timezone.utc)
        payload = {
            "messages": ModelMessagesTypeAdapter.dump_json(messages).decode(),
            "updated_at": now,
            "ttl": now + SESSION_TTL,
        }
        await self._doc(session_id).set(payload)

    async def delete(self, session_id: str) -> None:
        await self._doc(session_id).delete()


def get_store() -> SessionStore:
    """Return the session store selected by the ``SESSION_STORE`` env var."""
    backend = os.environ.get("SESSION_STORE", "memory").strip().lower()
    if backend == "firestore":
        return FirestoreSessionStore()
    return InMemorySessionStore()
