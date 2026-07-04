"""Routes user input to the first matching skill, or to the LLM fallback."""

from __future__ import annotations

from dataclasses import dataclass

from ace.skills import Skill, all_skills


@dataclass
class RouteResult:
    reply: str
    handled_by: str  # skill name, "llm", or "unknown"


def route(text: str, *, llm=None) -> RouteResult:
    """Find a skill whose pattern matches `text` and run it.

    `llm` is an optional callable(text) -> str used when nothing matches.
    """
    cleaned = text.strip()
    if not cleaned:
        return RouteResult("I didn't catch that. Try 'help' to see what I can do.", "unknown")

    for sk in all_skills():
        match = sk.pattern.match(cleaned)
        if match:
            kwargs = {k: v for k, v in match.groupdict().items() if v is not None}
            try:
                reply = sk.func(**kwargs)
            except Exception as exc:  # a broken skill shouldn't crash the assistant
                reply = f"Sorry, that command failed: {exc}"
            return RouteResult(reply, sk.name)

    if llm is not None:
        reply = llm(cleaned)
        if reply:
            return RouteResult(reply, "llm")

    return RouteResult(
        "I don't know how to do that yet. Say 'help' for my built-in commands, "
        "or set up a Claude API key so I can handle free-form requests (see README).",
        "unknown",
    )


def help_text() -> str:
    lines = ["Here's what I can do:"]
    for sk in sorted(all_skills(), key=lambda s: s.help):
        if sk.help:
            lines.append(f"  • {sk.help}")
    lines.append("  • exit / quit — close ACE")
    return "\n".join(lines)
