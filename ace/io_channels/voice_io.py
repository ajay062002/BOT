"""Microphone input and spoken output.

Speech-to-text uses the SpeechRecognition package (Google's free web
recognizer, needs internet). Text-to-speech uses pyttsx3, which is fully
offline (SAPI5 voices on Windows).

If the microphone can't be heard for a while, listen() returns "" and the
main loop simply tries again. Press Ctrl+C to quit.
"""

from __future__ import annotations

from ace.config import WAKE_WORD


class VoiceIO:
    def __init__(self, *, require_wake_word: bool = True):
        import pyttsx3
        import speech_recognition as sr

        self._sr = sr
        self._recognizer = sr.Recognizer()
        self._recognizer.dynamic_energy_threshold = True
        self._mic = sr.Microphone()
        self._tts = pyttsx3.init()
        self._tts.setProperty("rate", 180)
        self.require_wake_word = require_wake_word

        print("Calibrating microphone for background noise — one second...")
        with self._mic as source:
            self._recognizer.adjust_for_ambient_noise(source, duration=0.8)

    def listen(self) -> str:
        if self.require_wake_word:
            prompt = f"🎤 Listening — say '{WAKE_WORD}' then your command (Ctrl+C to quit)"
        else:
            prompt = "🎤 Listening... (Ctrl+C to quit)"
        print(prompt)
        try:
            with self._mic as source:
                audio = self._recognizer.listen(source, timeout=6, phrase_time_limit=12)
        except self._sr.WaitTimeoutError:
            return ""
        except KeyboardInterrupt:
            return "exit"
        try:
            text = self._recognizer.recognize_google(audio)
        except self._sr.UnknownValueError:
            return ""
        except self._sr.RequestError:
            self.say("I can't reach the speech service — is the internet up?")
            return ""
        except KeyboardInterrupt:
            return "exit"

        print(f"You (heard) > {text}")
        if self.require_wake_word:
            lowered = text.lower().strip()
            if not lowered.startswith(WAKE_WORD):
                print(f"   (didn't start with '{WAKE_WORD}' — ignored. Say e.g. '{WAKE_WORD}, what time is it')")
                return ""
            text = text[len(WAKE_WORD):].lstrip(" ,.!")
            if not text:
                self.say("Yes? Say the wake word and your command together, like 'ace open notepad'.")
                return ""
        return text

    def say(self, message: str) -> None:
        print(f"ACE: {message}")
        # speak only the first few lines; long lists are better read than heard
        spoken = " ".join(message.splitlines()[:4])
        try:
            self._tts.say(spoken)
            self._tts.runAndWait()
        except Exception:
            pass  # never let TTS glitches kill the assistant
