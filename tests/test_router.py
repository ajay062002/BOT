"""Tests for ACE's command routing — run with: python -m pytest or python -m unittest"""

from __future__ import annotations

import unittest

from ace.brain.router import route


class RouterTests(unittest.TestCase):
    def handled_by(self, text: str) -> str:
        return route(text).handled_by

    def test_time(self):
        self.assertEqual(self.handled_by("what time is it"), "tell_time")

    def test_date(self):
        self.assertEqual(self.handled_by("what's the date"), "tell_date")

    def test_greeting(self):
        self.assertEqual(self.handled_by("hello"), "greet")

    def test_help(self):
        result = route("help")
        self.assertEqual(result.handled_by, "show_help")
        self.assertIn("open <app>", result.reply)

    def test_open_folder_beats_open_app(self):
        # "open downloads" must go to the folder skill, not app launching
        self.assertEqual(self.handled_by("open downloads"), "open_folder")

    def test_open_app(self):
        self.assertEqual(self.handled_by("open notepad"), "open_app")

    def test_open_site(self):
        self.assertEqual(self.handled_by("open youtube"), "open_site")

    def test_set_timer_beats_start_app(self):
        # "start timer 5 minutes" must go to the timer, not app launching
        self.assertEqual(self.handled_by("start timer 5 minutes"), "set_timer")
        self.assertEqual(self.handled_by("set timer 10 mins"), "set_timer")

    def test_find_file_beats_web_search(self):
        self.assertEqual(self.handled_by("find file report.pdf"), "find_file")

    def test_web_search(self):
        self.assertEqual(self.handled_by("search best pizza near me"), "web_search")

    def test_note_roundtrip(self):
        self.assertEqual(self.handled_by("note buy milk"), "take_note")
        result = route("show my notes")
        self.assertEqual(result.handled_by, "show_notes")
        self.assertIn("buy milk", result.reply)
        self.assertEqual(self.handled_by("clear my notes"), "clear_notes")

    def test_unknown_without_llm(self):
        result = route("flurble the wobbly grumpus")
        self.assertEqual(result.handled_by, "unknown")

    def test_unknown_falls_back_to_llm(self):
        result = route("what is the capital of France", llm=lambda text: "Paris.")
        self.assertEqual(result.handled_by, "llm")
        self.assertEqual(result.reply, "Paris.")

    def test_empty_input(self):
        self.assertEqual(route("   ").handled_by, "unknown")

    def test_who_are_you(self):
        self.assertEqual(self.handled_by("who are you"), "who_are_you")

    # --- natural speech (phrases that failed in real voice usage) ---

    def test_courtesy_prefix_open_app(self):
        self.assertEqual(self.handled_by("can you open Notepad"), "open_app")
        self.assertEqual(self.handled_by("hey ace, please open notepad"), "open_app")

    def test_courtesy_suffix(self):
        self.assertEqual(self.handled_by("open notepad please"), "open_app")

    def test_keyword_system_info(self):
        self.assertEqual(self.handled_by("give me a bit of a system info"), "system_info")

    def test_keyword_open_screenshot(self):
        self.assertEqual(
            self.handled_by("can you open the screenshot that you've taken"),
            "open_screenshot",
        )

    def test_keyword_time(self):
        self.assertEqual(self.handled_by("could you tell me the time"), "tell_time")

    def test_keyword_does_not_shadow_exact_match(self):
        # "set timer 10 minutes" contains no clash, but "take a screenshot"
        # must still hit the exact skill, not a keyword pass
        self.assertEqual(self.handled_by("take a screenshot"), "screenshot")
        self.assertEqual(self.handled_by("open downloads"), "open_folder")


if __name__ == "__main__":
    unittest.main()
