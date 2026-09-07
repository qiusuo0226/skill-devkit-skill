#!/usr/bin/env python3
"""Structural checks for a Skill repo. Stdlib only. Exit 0/1.

Usage:
  python validate_skill.py --skill-root PATH
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REF_RE = re.compile(
    r"references/[A-Za-z0-9][A-Za-z0-9_.-]*(?:/[A-Za-z0-9_.-]+)*\.md"
)


def check(results: list, name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))
    line = f"[{'PASS' if ok else 'FAIL'}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)


def parse_frontmatter(text: str) -> dict[str, str]:
    raw = text.lstrip("\ufeff")
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return {}
    out: dict[str, str] = {}
    key: str | None = None
    folded = False
    acc: list[str] = []

    def flush() -> None:
        nonlocal key, folded, acc
        if key is None:
            return
        if folded:
            out[key] = " ".join(p for p in acc if p).strip()
        key = None
        folded = False
        acc = []

    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            flush()
            key = m.group(1)
            val = m.group(2)
            if val in (">", "|", ">-", "|-"):
                folded = True
                acc = []
            else:
                folded = False
                out[key] = val.strip().strip("'").strip('"')
                key = None
            continue
        if key and folded:
            acc.append(line.strip())
    flush()
    return out


def iter_ref_paths(text: str) -> set[str]:
    return set(REF_RE.findall(text))


def run_checks(root: Path) -> list[tuple[str, bool, str]]:
    results: list[tuple[str, bool, str]] = []
    root = root.resolve()

    skill = root / "SKILL.md"
    check(results, "SKILL.md exists", skill.is_file())
    fm: dict[str, str] = {}
    skill_text = ""
    if skill.is_file():
        skill_text = skill.read_text(encoding="utf-8")
        fm = parse_frontmatter(skill_text)
        check(results, "SKILL.md has YAML frontmatter", bool(fm), "missing --- block" if not fm else "")
        name = (fm.get("name") or "").strip()
        check(results, "frontmatter name non-empty", bool(name), name)
        desc = (fm.get("description") or "").strip()
        check(results, "frontmatter description non-empty", bool(desc))

    vf = root / "VERSION"
    check(results, "VERSION exists", vf.is_file())
    version = vf.read_text(encoding="utf-8").strip() if vf.is_file() else ""
    check(results, "VERSION non-empty", bool(version), version)

    sj_path = root / "skill.json"
    check(results, "skill.json exists", sj_path.is_file())
    if sj_path.is_file():
        try:
            data = json.loads(sj_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            check(results, "skill.json is JSON", False, str(exc))
            data = {}
        else:
            check(results, "skill.json is JSON", True)
        sj_ver = str(data.get("version") or "") if data else ""
        if version:
            check(
                results,
                "skill.json.version == VERSION",
                sj_ver == version,
                f"{sj_ver} vs {version}",
            )

    texts = []
    if skill_text:
        texts.append(skill_text)
    readme = root / "references" / "README.md"
    if readme.is_file():
        texts.append(readme.read_text(encoding="utf-8"))
    refs = set()
    for t in texts:
        refs |= iter_ref_paths(t)
    missing = sorted(r for r in refs if not (root / r).is_file())
    check(
        results,
        "referenced references/ files exist",
        not missing,
        ", ".join(missing[:8]) if missing else f"{len(refs)} ok",
    )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Structural checks for a Skill repo.")
    parser.add_argument("--skill-root", default=".", help="Skill repo root")
    args = parser.parse_args(argv)
    root = Path(args.skill_root)
    if not root.is_dir():
        print(f"[FAIL] skill-root is a directory — {root}", file=sys.stderr)
        return 1
    results = run_checks(root)
    failed = [name for name, ok, _ in results if not ok]
    if failed:
        print(f"\n{len(failed)} failed")
        return 1
    print("\nok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
