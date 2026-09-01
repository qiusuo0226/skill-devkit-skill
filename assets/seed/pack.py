#!/usr/bin/env python3
"""Pack the Skill at --skill-root into {Brand}-Skill-v{version}.zip.

Excludes: .git, governance, tests, __pycache__, zip artifacts.
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

EXCLUDE_DIRS = {".git", "governance", "tests", "__pycache__", ".idea", ".vscode", ".qoder"}
EXCLUDE_FILES = {".gitignore", ".DS_Store", "Thumbs.db"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}


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


def read_brand(root: Path) -> str:
    sj = root / "skill.json"
    if not sj.is_file():
        print("ERROR: skill.json missing", file=sys.stderr)
        sys.exit(1)
    data = json.loads(sj.read_text(encoding="utf-8"))
    display = data.get("displayName") or data.get("name")
    if not display:
        print("ERROR: skill.json missing displayName/name", file=sys.stderr)
        sys.exit(1)
    brand = re.split(r"[—\(]", display)[0].strip()
    return brand or str(display).strip()


def excluded(rel: Path) -> bool:
    parts = set(rel.parts)
    if parts & EXCLUDE_DIRS:
        return True
    if rel.name in EXCLUDE_FILES:
        return True
    if rel.suffix.lower() in EXCLUDE_EXTS:
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
    version = read_version(root)
    brand = read_brand(root)
    out_dir = Path(args.output_dir).resolve() if args.output_dir else root
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{brand}-Skill-v{version}.zip"
    files = [f for f in root.rglob("*") if f.is_file() and not excluded(f.relative_to(root))]
    print(f"{brand} v{version}: {len(files)} files -> {zip_path}")
    if args.dry_run:
        for f in files:
            print(" ", f.relative_to(root).as_posix())
        return
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, f.relative_to(root).as_posix())
    print("ok")


if __name__ == "__main__":
    main()
