#!/usr/bin/env python3
"""Pack the Skill at --skill-root into {name}-Skill-v{version}.zip.

Zip stem uses skill.json `name` (English slug), not displayName.
Excludes: .git, governance, tests, outputs, __pycache__, zip artifacts.
Keep EXCLUDE_* in sync with snapshot_baseline.py and audit_release.py.
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

EXCLUDE_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
EXCLUDE_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
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
    slug = read_slug(root)
    out_dir = Path(args.output_dir).resolve() if args.output_dir else root
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{slug}-Skill-v{version}.zip"
    files = [f for f in root.rglob("*") if f.is_file() and not excluded(f.relative_to(root))]
    print(f"{slug} v{version}: {len(files)} files -> {zip_path}")
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
