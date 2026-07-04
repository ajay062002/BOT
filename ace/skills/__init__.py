"""Skill registry for ACE.

A skill is a function decorated with @skill(pattern, ...). The pattern is a
regular expression matched (case-insensitively) against the user's whole
utterance; named groups become keyword arguments to the function. The
function returns the reply ACE gives the user.

All modules in this package are imported automatically, so adding a new
skill file makes its commands available without touching anything else.
"""

from __future__ import annotations

import importlib
import pkgutil
import re
from dataclasses import dataclass, field
from typing import Callable

SkillFunc = Callable[..., str]


@dataclass
class Skill:
    pattern: re.Pattern
    func: SkillFunc
    help: str
    priority: int = 50
    name: str = field(default="")

    def __post_init__(self):
        if not self.name:
            self.name = self.func.__name__


_REGISTRY: list[Skill] = []


def skill(pattern: str, *, help: str = "", priority: int = 50) -> Callable[[SkillFunc], SkillFunc]:
    """Register a function as an ACE skill.

    `pattern` is anchored on both ends, so write the full command shape.
    Lower `priority` numbers are tried first — give broad, catch-all
    patterns (like "open <anything>") a high number so specific skills win.
    """

    def decorator(func: SkillFunc) -> SkillFunc:
        compiled = re.compile(rf"^\s*(?:{pattern})\s*$", re.IGNORECASE)
        _REGISTRY.append(Skill(pattern=compiled, func=func, help=help, priority=priority))
        return func

    return decorator


def all_skills() -> list[Skill]:
    load_skills()
    return sorted(_REGISTRY, key=lambda s: s.priority)


_loaded = False


def load_skills() -> None:
    """Import every module in ace.skills so their @skill decorators run."""
    global _loaded
    if _loaded:
        return
    _loaded = True
    package = __name__
    for module_info in pkgutil.iter_modules(__path__):
        if not module_info.name.startswith("_"):
            importlib.import_module(f"{package}.{module_info.name}")
