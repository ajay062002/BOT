"""Find files and open common folders."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from ace.skills import skill

SEARCH_ROOTS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path.home() / "Pictures",
    Path.home(),
]

FOLDERS = {
    "desktop": Path.home() / "Desktop",
    "documents": Path.home() / "Documents",
    "downloads": Path.home() / "Downloads",
    "pictures": Path.home() / "Pictures",
    "music": Path.home() / "Music",
    "videos": Path.home() / "Videos",
    "home": Path.home(),
}

MAX_RESULTS = 8
MAX_SCANNED_DIRS = 4000  # keep searches snappy on big drives


def _open_path(path: Path) -> None:
    if sys.platform == "win32":
        os.startfile(str(path))
    else:
        subprocess.Popen(["xdg-open", str(path)])


def _search(name: str) -> list[Path]:
    needle = name.lower()
    hits: list[Path] = []
    seen: set[Path] = set()
    scanned = 0
    for root in SEARCH_ROOTS:
        if not root.is_dir() or root in seen:
            continue
        seen.add(root)
        for dirpath, dirnames, filenames in os.walk(root):
            # skip hidden and system-ish directories
            dirnames[:] = [d for d in dirnames if not d.startswith((".", "$"))]
            scanned += 1
            if scanned > MAX_SCANNED_DIRS:
                return hits
            for fname in filenames:
                if needle in fname.lower():
                    hits.append(Path(dirpath) / fname)
                    if len(hits) >= MAX_RESULTS:
                        return hits
    return hits


@skill(
    r"(?:find|search(?: for)?|locate) (?:file|files) (?P<name>.+)",
    help="find file <name> — search your folders for a file",
    priority=30,
)
def find_file(name: str) -> str:
    hits = _search(name.strip())
    if not hits:
        return f"I couldn't find any file matching '{name.strip()}' in your main folders."
    lines = [f"Found {len(hits)} match(es):"]
    lines += [f"  {p}" for p in hits]
    if len(hits) == 1:
        _open_path(hits[0].parent)
        lines.append("I opened its folder for you.")
    return "\n".join(lines)


@skill(
    r"(?:open|show)(?: my)? (?P<folder>desktop|documents|downloads|pictures|music|videos|home)(?: folder)?",
    help="open downloads / documents / desktop ... — open a common folder",
    priority=30,
)
def open_folder(folder: str) -> str:
    path = FOLDERS[folder.lower()]
    if not path.exists():
        return f"Your {folder} folder doesn't exist at {path}."
    _open_path(path)
    return f"Opening your {folder} folder."
