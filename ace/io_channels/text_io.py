"""Plain console input/output."""

from __future__ import annotations


class TextIO:
    def listen(self) -> str:
        try:
            return input("You > ")
        except (EOFError, KeyboardInterrupt):
            return "exit"

    def say(self, message: str) -> None:
        print(f"ACE: {message}")
