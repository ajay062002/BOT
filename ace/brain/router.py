"""Routes user input to the first matching skill, or to the LLM fallback."""

from __future__ import annotations

import re
from dataclasses import dataclass

from ace.skills import all_skills

# Spoken commands come wrapped in politeness — peel it off before matching.
# Applied repeatedly, so "hey ace, can you please open notepad" fully unwraps.
_COURTESY_PREFIXES = (
    "hey", "hi", "ok", "okay", "ace", "please", "kindly",
    "can you", "could you", "would you", "will you",
    "i want you to", "i need you to", "i want to", "i'd like you to", "i'd like to",
)
_COURTESY_SUFFIXES = ("please", "for me", "thanks", "thank you")


def normalize(text: str) -> str:
    cleaned = text.strip().strip(",.!?").strip()
    lowered = cleaned.lower()
    changed = True
    while changed:
        changed = False
        for prefix in _COURTESY_PREFIXES:
            if lowered.startswith((prefix + " ", prefix + ",")) or lowered == prefix:
                cleaned = cleaned[len(prefix):].lstrip(" ,")
                lowered = cleaned.lower()
                changed = True
        for suffix in _COURTESY_SUFFIXES:
            if lowered.endswith(" " + suffix):
                cleaned = cleaned[: -len(suffix)].rstrip(" ,")
                lowered = cleaned.lower()
                changed = True
    return cleaned


@dataclass
class RouteResult:
    reply: str
    handled_by: str  # skill name, "llm", or "unknown"


def _run(sk, **kwargs) -> str:
    try:
        return sk.func(**kwargs)
    except Exception as exc:  # a broken skill shouldn't crash the assistant
        return f"Sorry, that command failed: {exc}"


# Skills at or above this priority are catch-alls ("open <anything>") and
# only get a shot after the looser keyword pass, so "open the screenshot
# you've taken" reaches the screenshot skill instead of app launching.
_CATCHALL_PRIORITY = 70


def route(text: str, *, llm=None) -> RouteResult:
    """Find a skill matching `text` and run it.

    Four passes: exact pattern match for specific skills, a looser keyword
    match (for natural speech like "give me a bit of a system info"),
    exact match for catch-all skills, then the optional LLM fallback.
    """
    cleaned = normalize(text)
    if not cleaned:
        return RouteResult("I didn't catch that. Try 'help' to see what I can do.", "unknown")

    skills = all_skills()

    def try_patterns(candidates) -> RouteResult | None:
        for sk in candidates:
            match = sk.pattern.match(cleaned)
            if match:
                kwargs = {k: v for k, v in match.groupdict().items() if v is not None}
                return RouteResult(_run(sk, **kwargs), sk.name)
        return None

    result = try_patterns(sk for sk in skills if sk.priority < _CATCHALL_PRIORITY)
    if result:
        return result

    # Keyword pass: fire when every word of a keyword tuple appears somewhere
    words = set(re.findall(r"[a-z']+", cleaned.lower()))
    for sk in skills:
        for keyword_set in sk.keywords:
            if all(word in words for word in keyword_set):
                return RouteResult(_run(sk), sk.name)

    result = try_patterns(sk for sk in skills if sk.priority >= _CATCHALL_PRIORITY)
    if result:
        return result

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
