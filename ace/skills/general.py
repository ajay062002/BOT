"""Small talk, time and date, and help."""

from __future__ import annotations

import random
from datetime import datetime

from ace.skills import skill


@skill(r"(?:hi|hello|hey|yo)(?: ace)?", help="hello — say hi", priority=10)
def greet() -> str:
    return random.choice(
        [
            "Hey! What can I do for you?",
            "Hello! Ready when you are.",
            "Hi there! Ask me anything — try 'help' to see my tricks.",
        ]
    )


@skill(
    r"(?:what(?:'s| is) the time|what time is it|time)",
    help="what time is it — current time",
    priority=10,
    keywords=[("what", "time"), ("tell", "time"), ("current", "time")],
)
def tell_time() -> str:
    return datetime.now().strftime("It's %I:%M %p.")


@skill(
    r"(?:what(?:'s| is) (?:the |today'?s )?date|date today|today)",
    help="what's the date — today's date",
    priority=10,
    keywords=[("what", "date"), ("today's", "date"), ("todays", "date")],
)
def tell_date() -> str:
    return datetime.now().strftime("Today is %A, %B %d, %Y.")


@skill(r"(?:who are you|introduce yourself|what are you)", help="who are you — meet ACE", priority=10)
def who_are_you() -> str:
    return (
        "I'm ACE, your personal PC assistant. I can open apps, find files, "
        "control volume, take screenshots, search the web, keep notes, set "
        "timers, and more. Say 'help' for the full list."
    )


@skill(
    r"(?:help|what can you do|commands|abilities)",
    help="",
    priority=10,
    keywords=[("help",), ("what", "can", "you", "do")],
)
def show_help() -> str:
    from ace.brain.router import help_text

    return help_text()


@skill(r"(?:thanks|thank you|thx)(?: ace)?", help="", priority=10)
def thanks() -> str:
    return random.choice(["Anytime!", "You're welcome!", "Happy to help!"])
