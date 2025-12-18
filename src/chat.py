from typing import List, Optional
from . import helper

# Simple chat wrapper that uses documents loaded by helper.load_data
# Preserves logic: document loading, filtering and splitting remain in `helper`.


class ChatManager:
    def __init__(self):
        self.documents: List = []

    def load_documents(self, path: str) -> int:
        """Load documents from `path` using the helper module. Returns number of chunks/docs loaded."""
        docs = helper.load_data(path)
        self.documents = docs
        return len(docs)

    def chat(self, message: str) -> str:
        """Very small placeholder chat logic that connects frontend to backend.

        This function intentionally doesn't change core document-processing logic.
        Replace or extend this method to integrate an LLM chain or retriever later.
        """
        # Minimal behavior: echo and indicate documents loaded
        if not self.documents:
            return f"Echo: {message} (no documents loaded)"
        # return message + short info about first doc source if available
        src = getattr(self.documents[0], "metadata", {}).get("source", "unknown")
        return f"Echo: {message} (using docs, first source: {src})"


_default_manager: Optional[ChatManager] = None


def get_manager() -> ChatManager:
    global _default_manager
    if _default_manager is None:
        _default_manager = ChatManager()
    return _default_manager
import os
from typing import Optional

try:
    import openai
except Exception:
    openai = None


def _openai_reply(message: str, model: str = "gpt-3.5-turbo") -> Optional[str]:
    key = os.getenv("OPENAI_API_KEY")
    if not key or openai is None:
        return None
    try:
        openai.api_key = key
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful, careful medical assistant. Provide general information and encourage seeking professional care when appropriate. Do not give definitive diagnoses."},
                {"role": "user", "content": message},
            ],
            max_tokens=300,
            temperature=0.2,
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        return None


def get_response(message: str) -> str:
    """Return a reply. Uses OpenAI if configured, otherwise falls back to simple heuristics.

    Keep this function small so it can be replaced with retrieval/LLM logic later.
    """
    if not message or message.strip() == "":
        return "Hello — I'm your medical assistant. How can I help you today?"

    # Try OpenAI if available
    reply = _openai_reply(message)
    if reply:
        return reply

    # If OpenAI isn't configured or the call failed, return a clear message.
    return "OpenAI not configured or failed to produce a reply. Set OPENAI_API_KEY to enable LLM responses."
