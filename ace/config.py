"""Configuration and shared paths for ACE.

User data lives under ~/.ace (notes, config). The optional Claude API key is
read from the ANTHROPIC_API_KEY environment variable or from
~/.ace/config.ini ([ace] api_key = ...).
"""

from __future__ import annotations

import configparser
import os
from pathlib import Path

ASSISTANT_NAME = "ACE"
WAKE_WORD = "ace"

DATA_DIR = Path.home() / ".ace"
CONFIG_FILE = DATA_DIR / "config.ini"
NOTES_FILE = DATA_DIR / "notes.txt"
REMINDERS_FILE = DATA_DIR / "reminders.txt"

CLAUDE_MODEL = "claude-opus-4-8"


def ensure_data_dir() -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def _read_config() -> configparser.ConfigParser:
    parser = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        parser.read(CONFIG_FILE)
    return parser


def get_api_key() -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    parser = _read_config()
    key = parser.get("ace", "api_key", fallback="").strip()
    return key or None


def screenshots_dir() -> Path:
    pictures = Path.home() / "Pictures"
    target = (pictures if pictures.exists() else ensure_data_dir()) / "ACE Screenshots"
    target.mkdir(parents=True, exist_ok=True)
    return target
