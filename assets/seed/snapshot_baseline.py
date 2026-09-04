#!/usr/bin/env python3
"""Copy pack-included files into governance/baselines/{VERSION}/.

Refuses to overwrite a non-empty baseline directory (freeze).
Empty version dir (interrupted first snapshot) may be filled.
Exclude sets: governance/pack.ini via pack_exclude.py (sibling).
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from pack_exclude import load_excludes

ROOT = Path(__file__).resolve().parents[2]


def excluded(rel: Path, dirs: set, files: set, exts: set) -> bool:
    if set(rel.parts) & dirs:
        return True
    if rel.name in files:
        return True
    if rel.suffix.lower() in exts:
        return True
    return False


def version() -> str:
    vf = ROOT / "VERSION"
    if vf.is_file():
        v = vf.read_text(encoding="utf-8").strip()
        if v:
            return v
    sj = ROOT / "skill.json"
    if sj.is_file():
        data = json.loads(sj.read_text(encoding="utf-8"))
        if data.get("version"):
            return str(data["version"])
    print("ERROR: no VERSION", file=sys.stderr)
    sys.exit(1)


def _has_files(path: Path) -> bool:
    return path.is_dir() and any(f.is_file() for f in path.rglob("*"))


def main() -> None:
    ver = version()
    dest = ROOT / "governance" / "baselines" / ver
    if dest.exists() and _has_files(dest):
        print(f"ERROR: baseline {ver} already exists (freeze, will not overwrite)", file=sys.stderr)
        sys.exit(1)
    dirs, files, exts, _empty = load_excludes(ROOT)
    packed = [f for f in ROOT.rglob("*") if f.is_file() and not excluded(f.relative_to(ROOT), dirs, files, exts)]
    dest.mkdir(parents=True, exist_ok=True)
    for f in packed:
        rel = f.relative_to(ROOT)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
    print(f"baseline {ver}: {len(packed)} files -> {dest}")


if __name__ == "__main__":
    main()
