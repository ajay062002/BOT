"""Optional Claude API fallback for requests no built-in skill matches."""

from __future__ import annotations

from ace import config

SYSTEM_PROMPT = (
    "You are ACE, a friendly personal assistant running on the user's Windows PC. "
    "Answer questions helpfully and concisely (a few sentences at most, since "
    "replies may be spoken aloud). You cannot directly control the PC from this "
    "chat; if the user asks for a PC action you can't do, suggest the closest "
    "built-in ACE command instead."
)


class ClaudeBrain:
    """Wraps the Anthropic SDK with a short rolling conversation memory."""

    def __init__(self, api_key: str):
        import anthropic  # imported lazily so ACE runs without the package

        self._client = anthropic.Anthropic(api_key=api_key)
        self._history: list[dict] = []

    def __call__(self, text: str) -> str:
        self._history.append({"role": "user", "content": text})
        # keep the last 10 exchanges so context stays small and cheap
        self._history = self._history[-20:]
        try:
            response = self._client.messages.create(
                model=config.CLAUDE_MODEL,
                max_tokens=400,
                system=SYSTEM_PROMPT,
                messages=self._history,
            )
        except Exception as exc:
            self._history.pop()
            return f"I couldn't reach the Claude API: {exc}"
        reply = "".join(block.text for block in response.content if block.type == "text")
        self._history.append({"role": "assistant", "content": reply})
        return reply


def make_llm() -> ClaudeBrain | None:
    """Return a Claude fallback if an API key and the SDK are available."""
    api_key = config.get_api_key()
    if not api_key:
        return None
    try:
        return ClaudeBrain(api_key)
    except ImportError:
        return None
