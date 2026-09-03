#!/usr/bin/env python3
"""Copy pack-included files into governance/baselines/{VERSION}/.

Refuses to overwrite an existing baseline directory (freeze).
Keep EXCLUDE_* in sync with pack.py.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
EXCLUDE_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}


def excluded(rel: Path) -> bool:
    if set(rel.parts) & EXCLUDE_DIRS:
        return True
    if rel.name in EXCLUDE_FILES:
        return True
    if rel.suffix.lower() in EXCLUDE_EXTS:
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


def main() -> None:
    ver = version()
    dest = ROOT / "governance" / "baselines" / ver
    if dest.exists():
        print(f"ERROR: baseline {ver} already exists (freeze, will not overwrite)", file=sys.stderr)
        sys.exit(1)
    files = [f for f in ROOT.rglob("*") if f.is_file() and not excluded(f.relative_to(ROOT))]
    dest.mkdir(parents=True)
    for f in files:
        rel = f.relative_to(ROOT)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
    print(f"baseline {ver}: {len(files)} files -> {dest}")


if __name__ == "__main__":
    main()
