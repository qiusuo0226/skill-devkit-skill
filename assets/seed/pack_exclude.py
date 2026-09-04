#!/usr/bin/env python3
"""Load pack exclude sets from governance/pack.ini. Fallback = 0.7.0 builtins."""
from __future__ import annotations

import configparser
import sys
from pathlib import Path

BUILTIN_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
BUILTIN_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
BUILTIN_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}


def _split(raw: str) -> set[str]:
    return {p.strip() for p in raw.split(",") if p.strip()}


def load_excludes(root: Path) -> tuple[set[str], set[str], set[str], bool]:
    """Return (dirs, files, exts, empty_dirs_in_ini). dirs is never empty."""
    ini = Path(root) / "governance" / "pack.ini"
    if not ini.is_file():
        print("WARN: pack.ini missing; using built-in exclude set", file=sys.stderr)
        return set(BUILTIN_DIRS), set(BUILTIN_FILES), set(BUILTIN_EXTS), False
    parser = configparser.ConfigParser()
    try:
        parser.read(ini, encoding="utf-8")
        section = parser["exclude"]
        dirs = _split(section.get("dirs", ""))
        files = _split(section.get("files", ""))
        exts = _split(section.get("exts", ""))
    except (OSError, KeyError, configparser.Error) as exc:
        print(f"WARN: pack.ini unreadable ({exc}); using built-in exclude set", file=sys.stderr)
        return set(BUILTIN_DIRS), set(BUILTIN_FILES), set(BUILTIN_EXTS), False
    empty_dirs = not dirs
    if empty_dirs:
        print("WARN: pack.ini dirs empty; using built-in exclude set", file=sys.stderr)
        dirs = set(BUILTIN_DIRS)
    if not files:
        files = set(BUILTIN_FILES)
    if not exts:
        exts = set(BUILTIN_EXTS)
    return dirs, files, exts, empty_dirs
