"""Entry point: python -m ace [--voice]"""

from __future__ import annotations

import argparse

from ace.assistant import run


def main() -> None:
    parser = argparse.ArgumentParser(prog="ace", description="ACE — your personal PC assistant")
    parser.add_argument("--voice", action="store_true", help="listen on the microphone and speak replies")
    parser.add_argument(
        "--no-wake",
        action="store_true",
        help="voice mode responds to everything, without needing the 'ace' wake word",
    )
    args = parser.parse_args()
    run(voice=args.voice, wake_word=not args.no_wake)


if __name__ == "__main__":
    main()
