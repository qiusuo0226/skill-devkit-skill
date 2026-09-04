#!/usr/bin/env python3
"""Discover assistant skill roots. JSON on stdout. See references/03-skill-roots.md."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

HOME_VARS = ("GROK_HOME", "LINGXI_HOME", "CLAUDE_HOME", "CODEX_HOME")
FALLBACK_REL = (
    Path(".grok") / "skills",
    Path(".grok") / "bundled" / "skills",
    Path(".claude") / "skills",
    Path(".codex") / "skills",
    Path(".cursor") / "skills",
    Path(".lingma") / "skills",
    Path(".lingxi") / "skills",
    Path(".lingxi") / "bundled" / "skills",
    Path(".qoder") / "skills",
    Path(".agents") / "skills",
)
NAME_RE = re.compile(r"(?m)^name:\s*[\"']?([A-Za-z0-9][A-Za-z0-9-]{0,62})[\"']?\s*$")


def _add(roots: list[dict], path: Path, source: str) -> None:
    try:
        resolved = path.resolve()
    except OSError:
        return
    if not resolved.is_dir():
        return
    key = str(resolved)
    if any(r["path"] == key for r in roots):
        return
    roots.append({"path": key, "source": source, "exists": True})


def discover_roots() -> list[dict]:
    roots: list[dict] = []
    raw = os.environ.get("SKILL_DEVKIT_SKILLS_DIRS", "").strip()
    if raw:
        for part in raw.split(";"):
            part = part.strip().strip('"')
            if part:
                _add(roots, Path(part), "env:SKILL_DEVKIT_SKILLS_DIRS")
    for var in HOME_VARS:
        val = os.environ.get(var, "").strip()
        if not val:
            continue
        home = Path(val)
        _add(roots, home / "skills", f"env:{var}")
        _add(roots, home / "bundled" / "skills", f"env:{var}")
    home = Path.home()
    for rel in FALLBACK_REL:
        _add(roots, home / rel, "fallback")
    return roots


def heuristic_skills_dir(path: Path) -> Path | None:
    try:
        parts = list(path.resolve().parts)
    except OSError:
        return None
    if len(parts) < 3:
        return None
    if parts[-2] == "skills" and parts[-3] == "bundled":
        return path.resolve().parent
    if parts[-2] == "skills" and parts[-3].startswith("."):
        return path.resolve().parent
    return None


def in_install_dir(workspace: Path, roots: list[dict]) -> bool:
    try:
        ws = workspace.resolve()
    except OSError:
        return False
    for r in roots:
        try:
            ws.relative_to(Path(r["path"]))
            return True
        except ValueError:
            continue
    return heuristic_skills_dir(ws) is not None


def read_name(skill_md: Path) -> str:
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return ""
    m = NAME_RE.search(text)
    return m.group(1) if m else ""


def check_name(slug: str, roots: list[dict]) -> list[dict]:
    hits = []
    for r in roots:
        root = Path(r["path"])
        try:
            entries = list(root.iterdir())
        except OSError:
            continue
        for child in entries:
            if child.name == slug:
                hits.append({"path": str(child), "how": "dirname", "root": r["path"]})
            skill = child / "SKILL.md" if child.is_dir() else None
            if skill and skill.is_file():
                name = read_name(skill)
                if name == slug:
                    hits.append({"path": str(skill), "how": "frontmatter", "root": r["path"]})
    return hits


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--contains", default=None, help="Workspace absolute path (adopt gate)")
    p.add_argument("--check-name", default=None, help="Skill slug (occupancy)")
    args = p.parse_args()
    roots = discover_roots()
    extra_root = None
    ws_in = False
    if args.contains:
        ws = Path(args.contains)
        heur = heuristic_skills_dir(ws)
        if heur is not None:
            _add(roots, heur, "heuristic")
            extra_root = str(heur.resolve()) if heur.is_dir() else None
        ws_in = in_install_dir(ws, roots)
    payload = {
        "roots": roots,
        "workspace_in_install_dir": ws_in,
    }
    if extra_root:
        payload["heuristic_root"] = extra_root
    if args.check_name:
        payload["hits"] = check_name(args.check_name.strip(), roots)
    json.dump(payload, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
