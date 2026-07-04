"""Open and close applications."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

from ace.skills import skill

IS_WINDOWS = sys.platform == "win32"

# friendly name -> what to actually launch on Windows
APP_ALIASES = {
    "chrome": "chrome",
    "google chrome": "chrome",
    "edge": "msedge",
    "firefox": "firefox",
    "notepad": "notepad",
    "calculator": "calc",
    "calc": "calc",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "explorer": "explorer",
    "file explorer": "explorer",
    "files": "explorer",
    "cmd": "cmd",
    "command prompt": "cmd",
    "terminal": "wt",
    "task manager": "taskmgr",
    "settings": "ms-settings:",
    "vs code": "code",
    "vscode": "code",
    "spotify": "spotify",
    "vlc": "vlc",
    "steam": "steam",
    "discord": "discord",
    "whatsapp": "whatsapp",
}


def _launch(target: str) -> bool:
    if IS_WINDOWS:
        try:
            os.startfile(target)  # handles exes on PATH, URIs like ms-settings:
            return True
        except OSError:
            pass
        # os.startfile needs a path; fall back to `start` which searches PATH
        result = subprocess.run(
            f'start "" "{target}"', shell=True, capture_output=True
        )
        return result.returncode == 0
    if shutil.which(target):
        subprocess.Popen([target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    return False


@skill(
    r"(?:open|launch|start|run) (?P<app>.+?)",
    help="open <app> — launch an application",
    priority=80,  # catch-all: let "open downloads", "start timer" etc. match first
)
def open_app(app: str) -> str:
    name = app.strip().lower()
    target = APP_ALIASES.get(name, name)
    if _launch(target):
        return f"Opening {app.strip()}."
    return (
        f"I couldn't find '{app.strip()}'. If it's installed, try the exact "
        "program name (for example 'open notepad')."
    )


@skill(
    r"(?:close|kill|quit|stop) (?P<app>.+?)",
    help="close <app> — close an application",
    priority=80,
)
def close_app(app: str) -> str:
    name = app.strip().lower()
    target = APP_ALIASES.get(name, name)
    exe = target if target.endswith(".exe") else f"{target}.exe"
    if IS_WINDOWS:
        result = subprocess.run(
            ["taskkill", "/IM", exe, "/F"], capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"Closed {app.strip()}."
        return f"I couldn't find a running app called '{app.strip()}'."
    result = subprocess.run(["pkill", "-f", target], capture_output=True)
    if result.returncode == 0:
        return f"Closed {app.strip()}."
    return f"I couldn't find a running app called '{app.strip()}'."
