#!/usr/bin/env python3
"""Pack the Skill at --skill-root into {name}-Skill-v{version}.zip.

Zip stem uses skill.json `name` (English slug), not displayName.
Exclude sets: governance/pack.ini via pack_exclude.py.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import zipfile
from pathlib import Path

_FALLBACK_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
_FALLBACK_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
_FALLBACK_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}


def _load_exclude_mod():
    here = Path(__file__).resolve().parent
    candidates = [
        here / "pack_exclude.py",
        here.parents[2] / "governance" / "scripts" / "pack_exclude.py",
    ]
    for c in candidates:
        if c.is_file():
            spec = importlib.util.spec_from_file_location("pack_exclude", c)
            if spec is None or spec.loader is None:
                continue
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    return None


def load_sets(root: Path):
    mod = _load_exclude_mod()
    if mod is None:
        print("WARN: pack_exclude.py missing; using built-in exclude set", file=sys.stderr)
        return _FALLBACK_DIRS, _FALLBACK_FILES, _FALLBACK_EXTS, False
    return mod.load_excludes(root)


def read_version(root: Path) -> str:
    vf = root / "VERSION"
    if vf.is_file():
        v = vf.read_text(encoding="utf-8").strip()
        if v:
            return v
    sj = root / "skill.json"
    if sj.is_file():
        data = json.loads(sj.read_text(encoding="utf-8"))
        if data.get("version"):
            return str(data["version"])
    print("ERROR: no VERSION or skill.json version", file=sys.stderr)
    sys.exit(1)


def read_slug(root: Path) -> str:
    sj = root / "skill.json"
    if not sj.is_file():
        print("ERROR: skill.json missing", file=sys.stderr)
        sys.exit(1)
    data = json.loads(sj.read_text(encoding="utf-8"))
    name = str(data.get("name") or "").strip()
    if not name:
        print("ERROR: skill.json missing 'name'", file=sys.stderr)
        sys.exit(1)
    return name


def excluded(rel: Path, dirs: set, files: set, exts: set) -> bool:
    if set(rel.parts) & dirs:
        return True
    if rel.name in files:
        return True
    if rel.suffix.lower() in exts:
        return True
    return False


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--skill-root", default=".", help="Directory that contains SKILL.md")
    p.add_argument("--output-dir", default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    root = Path(args.skill_root).resolve()
    if not (root / "SKILL.md").is_file():
        print(f"ERROR: SKILL.md not found in {root}", file=sys.stderr)
        sys.exit(1)
    dirs, files, exts, _empty = load_sets(root)
    version = read_version(root)
    slug = read_slug(root)
    out_dir = Path(args.output_dir).resolve() if args.output_dir else root
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{slug}-Skill-v{version}.zip"
    packed = [f for f in root.rglob("*") if f.is_file() and not excluded(f.relative_to(root), dirs, files, exts)]
    print(f"{slug} v{version}: {len(packed)} files -> {zip_path}")
    if args.dry_run:
        for f in packed:
            print(" ", f.relative_to(root).as_posix())
        return
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in packed:
            zf.write(f, f.relative_to(root).as_posix())
    print("ok")


if __name__ == "__main__":
    main()
