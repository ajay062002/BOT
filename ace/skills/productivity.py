"""Productivity: notes, timers, clipboard."""

from __future__ import annotations

import re
import threading
from datetime import datetime

from ace import config
from ace.skills import skill


@skill(
    r"(?:note|take (?:a )?note|remember)(?: that)?[:,]? (?P<text>.+)",
    help="note <anything> — save a note",
    priority=20,
)
def take_note(text: str) -> str:
    config.ensure_data_dir()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(config.NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {text.strip()}\n")
    return "Noted."


@skill(
    r"(?:show|read|list)(?: my)? notes",
    help="show my notes — read saved notes",
    priority=20,
    keywords=[("show", "notes"), ("read", "notes"), ("what", "notes")],
)
def show_notes() -> str:
    if not config.NOTES_FILE.exists():
        return "You don't have any notes yet. Say 'note <something>' to add one."
    content = config.NOTES_FILE.read_text(encoding="utf-8").strip()
    return content if content else "Your notes file is empty."


@skill(
    r"(?:clear|delete)(?: my| all)? notes",
    help="clear my notes — delete all saved notes",
    priority=20,
)
def clear_notes() -> str:
    if config.NOTES_FILE.exists():
        config.NOTES_FILE.unlink()
    return "All notes cleared."


def _parse_duration(amount: str, unit: str) -> int:
    value = int(amount)
    unit = unit.lower()
    if unit.startswith("h"):
        return value * 3600
    if unit.startswith("m"):
        return value * 60
    return value


@skill(
    r"(?:set (?:a )?|start (?:a )?)?timer(?: for)? (?P<amount>\d+) ?(?P<unit>hours?|hrs?|minutes?|mins?|seconds?|secs?)",
    help="set timer 10 minutes — countdown with an alert",
    priority=20,
)
def set_timer(amount: str, unit: str) -> str:
    seconds = _parse_duration(amount, unit)

    def ring():
        message = f"⏰ Time's up! Your {amount} {unit} timer just finished."
        print(f"\nACE: {message}\nYou > ", end="", flush=True)
        try:  # audible beep on Windows
            import winsound

            for _ in range(3):
                winsound.Beep(1000, 400)
        except Exception:
            print("\a", end="", flush=True)

    timer = threading.Timer(seconds, ring)
    timer.daemon = True
    timer.start()
    return f"Timer set for {amount} {unit}. I'll let you know."


@skill(
    r"(?:copy|clipboard) (?P<text>.+)",
    help="copy <text> — put text on the clipboard",
    priority=40,
)
def copy_to_clipboard(text: str) -> str:
    try:
        import pyperclip

        pyperclip.copy(text)
        return "Copied to your clipboard."
    except Exception:
        return "Clipboard needs the pyperclip package: pip install pyperclip"


@skill(
    r"(?:paste|what(?:'s| is) (?:on|in) (?:my |the )?clipboard)",
    help="what's on my clipboard — read the clipboard",
    priority=20,
)
def read_clipboard() -> str:
    try:
        import pyperclip

        content = pyperclip.paste()
        return f"Clipboard: {content}" if content.strip() else "Your clipboard is empty."
    except Exception:
        return "Clipboard needs the pyperclip package: pip install pyperclip"
