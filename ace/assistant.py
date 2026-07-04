"""ACE's main loop: listen → route → respond."""

from __future__ import annotations

from ace import __version__, config
from ace.brain.llm import make_llm
from ace.brain.router import route

EXIT_WORDS = {"exit", "quit", "bye", "goodbye", "stop listening", "shut up"}

BANNER = rf"""
    ___   _____________
   /   | / ____/ ____/    ACE v{__version__}
  / /| |/ /   / __/       Your personal PC assistant
 / ___ / /___/ /___       Type 'help' to see what I can do.
/_/  |_\____/_____/       Type 'exit' to quit.
"""


def run(voice: bool = False, wake_word: bool = True) -> None:
    config.ensure_data_dir()
    print(BANNER)

    if voice:
        try:
            from ace.io_channels.voice_io import VoiceIO

            io = VoiceIO(require_wake_word=wake_word)
        except ImportError:
            print(
                "Voice mode needs extra packages:\n"
                "  pip install SpeechRecognition pyttsx3 pyaudio\n"
                "Starting in text mode instead.\n"
            )
            from ace.io_channels.text_io import TextIO

            io = TextIO()
        except OSError as exc:
            print(f"I couldn't open a microphone ({exc}). Starting in text mode.\n")
            from ace.io_channels.text_io import TextIO

            io = TextIO()
    else:
        from ace.io_channels.text_io import TextIO

        io = TextIO()

    llm = make_llm()
    if llm is None:
        print("(No Claude API key found — running with built-in commands only. See README to enable.)\n")
    else:
        print("(Claude API connected — ask me anything.)\n")

    io.say("Hello! I'm ACE. How can I help?")

    try:
        while True:
            text = io.listen()
            if not text.strip():
                continue
            if text.strip().lower() in EXIT_WORDS:
                io.say("Goodbye!")
                break
            result = route(text, llm=llm)
            io.say(result.reply)
    except KeyboardInterrupt:
        print()
        io.say("Goodbye!")
