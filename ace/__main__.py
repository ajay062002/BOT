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
    parser.add_argument(
        "--voices",
        action="store_true",
        help="list installed text-to-speech voices and exit",
    )
    parser.add_argument(
        "--tts-voice",
        default="",
        metavar="NAME",
        help="speak with this voice (e.g. zira, david); see --voices for options",
    )
    args = parser.parse_args()

    if args.voices:
        from ace.io_channels.voice_io import print_voices

        print_voices()
        return

    run(voice=args.voice, wake_word=not args.no_wake, tts_voice=args.tts_voice)


if __name__ == "__main__":
    main()
