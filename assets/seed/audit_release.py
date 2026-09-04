#!/usr/bin/env python3
"""Release assertions. Any FAIL → non-zero exit. Read-only. Target-repo copy."""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

from pack_exclude import load_excludes

ROOT = Path(__file__).resolve().parents[2]
FAILURES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    if not ok:
        FAILURES.append(name)


def _load_sets_via_pack():
    """Load excludes the way pack.py does (import path may differ from this sibling)."""
    here = Path(__file__).resolve().parent
    candidates = [
        ROOT / "governance" / "pack" / "pack.py",
        here / "pack.py",
    ]
    for c in candidates:
        if not c.is_file():
            continue
        spec = importlib.util.spec_from_file_location("pack_mod_for_audit", c)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.load_sets(ROOT)
    return None


def excluded(rel: Path, dirs: set, files: set, exts: set) -> bool:
    if set(rel.parts) & dirs:
        return True
    if rel.name in files:
        return True
    if rel.suffix.lower() in exts:
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

    dirs, files, exts, empty_dirs = load_excludes(ROOT)
    check("pack.ini dirs not empty (no silent empty exclude)", not empty_dirs)
    via_pack = _load_sets_via_pack()
    check("pack.py load_sets reachable", via_pack is not None)
    if via_pack is not None:
        check(
            "pack.py and audit load_excludes agree",
            via_pack[:3] == (dirs, files, exts),
        )
    packed = [
        f.relative_to(ROOT)
        for f in ROOT.rglob("*")
        if f.is_file() and not excluded(f.relative_to(ROOT), dirs, files, exts)
    ]
    leaked = [
        p.as_posix()
        for p in packed
        if "governance" in p.parts or p.parts[:1] == (".git",) or p.name == "AGENTS.md"
    ]
    check("pack set has no governance/.git/AGENTS.md", not leaked, ", ".join(leaked[:8]))

    planning = ROOT / "governance" / "planning"
    if planning.is_dir() and version:
        leftover = list(planning.glob(f"upgrade-plan-v{version}.md"))
        check("no AP left for published version", not leftover, str(leftover))

    smoke = ROOT / "tests" / "run_smoke.py"
    if smoke.is_file():
        proc = subprocess.run(
            [sys.executable, str(smoke)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        check("tests/run_smoke.py", proc.returncode == 0, f"exit {proc.returncode}")
        if proc.returncode != 0:
            if proc.stdout:
                print(proc.stdout, end="")
            if proc.stderr:
                print(proc.stderr, end="", file=sys.stderr)

    if FAILURES:
        print(f"\n{len(FAILURES)} failed")
        sys.exit(1)
    print("\nok")


if __name__ == "__main__":
    main()
