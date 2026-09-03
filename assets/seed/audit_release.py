#!/usr/bin/env python3
"""Release assertions. Any FAIL → non-zero exit. Read-only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
EXCLUDE_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}
FAILURES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    if not ok:
        FAILURES.append(name)


def excluded(rel: Path) -> bool:
    if set(rel.parts) & EXCLUDE_DIRS:
        return True
    if rel.name in EXCLUDE_FILES:
        return True
    if rel.suffix.lower() in EXCLUDE_EXTS:
        return True
    return False


def main() -> None:
    vf = ROOT / "VERSION"
    check("VERSION exists", vf.is_file())
    version = vf.read_text(encoding="utf-8").strip() if vf.is_file() else ""
    check("VERSION non-empty", bool(version), version)

    sj_path = ROOT / "skill.json"
    check("skill.json exists", sj_path.is_file())
    sj_ver = ""
    if sj_path.is_file():
        data = json.loads(sj_path.read_text(encoding="utf-8"))
        sj_ver = str(data.get("version") or "")
        check("skill.json.version == VERSION", sj_ver == version, f"{sj_ver} vs {version}")
        check("skill.json has name", bool(data.get("name")))

    cl = ROOT / "CHANGELOG.md"
    check("CHANGELOG.md exists", cl.is_file())
    if cl.is_file() and version:
        text = cl.read_text(encoding="utf-8")
        check(
            "CHANGELOG has this version heading",
            bool(re.search(rf"^## {re.escape(version)}\b", text, re.M)),
            version,
        )

    check("SKILL.md exists", (ROOT / "SKILL.md").is_file())
    check("LICENSE exists", (ROOT / "LICENSE").is_file())

    base = ROOT / "governance" / "baselines" / version
    check(f"baseline {version} exists", base.is_dir(), str(base))

    packed = [f.relative_to(ROOT) for f in ROOT.rglob("*") if f.is_file() and not excluded(f.relative_to(ROOT))]
    leaked = [p.as_posix() for p in packed if "governance" in p.parts or p.parts[:1] == (".git",) or p.name == "AGENTS.md"]
    check("pack set has no governance/.git/AGENTS.md", not leaked, ", ".join(leaked[:8]))

    planning = ROOT / "governance" / "planning"
    if planning.is_dir() and version:
        leftover = list(planning.glob(f"upgrade-plan-v{version}.md"))
        check("no AP left for published version", not leftover, str(leftover))

    if FAILURES:
        print(f"\n{len(FAILURES)} failed")
        sys.exit(1)
    print("\nok")


if __name__ == "__main__":
    main()
