#!/usr/bin/env python3
"""Structural checks for a Skill repo. Stdlib only. Exit 0/1.

Usage:
  python validate_skill.py --skill-root PATH

Rules (names are a contract; tests/test_checker_mutations.py keys on them):
  frontmatter / VERSION / skill.json / references
  trigger phrases consistent: SKILL.md description, README, skill.json description
  no previous version in distribution set
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import re
import sys
from contextlib import redirect_stderr
from pathlib import Path

_FALLBACK_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}
_FALLBACK_FILES = {".gitignore", ".DS_Store", "Thumbs.db", "AGENTS.md"}
_FALLBACK_EXTS = {".pyc", ".pyo", ".zip", ".tar", ".gz"}

TRIGGER_RE = re.compile(r"触发[：:]")
README_TRIGGER_RE = re.compile(r"(?:触发|同义口令)[：:]")
HEADING_RE = re.compile(r"^## (\d+\.\d+\.\d+)\b", re.M)

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


def _trigger_segment(text: str, pattern: re.Pattern = TRIGGER_RE) -> set[str] | None:
    """Phrases after 触发： up to the first 。 (or blank line). Split on 、 only."""
    m = pattern.search(text or "")
    if not m:
        return None
    seg = text[m.end():]
    for stop in ("。", "\n\n"):
        i = seg.find(stop)
        if i >= 0:
            seg = seg[:i]
    out = set()
    for part in seg.split("、"):
        item = re.sub(r"[`「」“”\"']", "", part)
        item = re.sub(r"\s+", " ", item).strip().strip("；;，,.")
        if item:
            out.add(item)
    return out


def _readme_triggers(text: str) -> set[str] | None:
    got = _trigger_segment(text, TRIGGER_RE)
    if got is None:
        got = _trigger_segment(text, README_TRIGGER_RE)
    return got


def _load_excludes(root: Path):
    here = Path(__file__).resolve().parent
    for cand in (here / "pack_exclude.py", here.parent / "scripts" / "pack_exclude.py"):
        if not cand.is_file():
            continue
        spec = importlib.util.spec_from_file_location("pack_exclude_for_validate", cand)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        with redirect_stderr(io.StringIO()):
            dirs, files, exts, _empty = mod.load_excludes(root)
        return dirs, files, exts
    return set(_FALLBACK_DIRS), set(_FALLBACK_FILES), set(_FALLBACK_EXTS)


def _excluded(rel: Path, dirs, files, exts) -> bool:
    return bool(set(rel.parts) & dirs) or rel.name in files or rel.suffix.lower() in exts


def previous_version(root: Path, version: str) -> str:
    """First CHANGELOG heading that is not the current VERSION ('' if none)."""
    cl = root / "CHANGELOG.md"
    if not cl.is_file():
        return ""
    for v in HEADING_RE.findall(cl.read_text(encoding="utf-8")):
        if v != version:
            return v
    return ""


def stale_version_hits(root: Path, prev: str, slug: str) -> list[str]:
    pat = re.compile(rf"(?<![\d.]){re.escape(prev)}(?!\.?\d)")
    zip_name = f"{slug}-Skill-v{prev}.zip" if slug else None
    dirs, files, exts = _load_excludes(root)
    hits = []
    for f in sorted(root.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(root)
        if _excluded(rel, dirs, files, exts) or rel.as_posix() == "CHANGELOG.md":
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if rel.as_posix() == "skill.json":
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                continue
            data.pop("versionHistory", None)
            data.pop("schemaVersion", None)  # schema, not the skill version
            text = json.dumps(data, ensure_ascii=False)
        for n, line in enumerate(text.splitlines(), 1):
            if pat.search(line) or (zip_name and zip_name in line):
                hits.append(f"{rel.as_posix()}:{n}")
    return hits


def run_checks(root: Path) -> list[tuple[str, bool, str]]:
    results: list[tuple[str, bool, str]] = []
    root = root.resolve()

    skill = root / "SKILL.md"
    check(results, "SKILL.md exists", skill.is_file())
    fm: dict[str, str] = {}
    skill_text = ""
    desc = ""
    if skill.is_file():
        skill_text = skill.read_text(encoding="utf-8")
        fm = parse_frontmatter(skill_text)
        check(results, "SKILL.md has YAML frontmatter", bool(fm), "missing --- block" if not fm else "")
        name = (fm.get("name") or "").strip()
        check(results, "frontmatter name non-empty", bool(name), name)
        desc = (fm.get("description") or "").strip()
        check(results, "frontmatter description non-empty", bool(desc))

    sj_desc = ""
    sj_name = ""
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
        sj_desc = str(data.get("description") or "") if data else ""
        sj_name = str(data.get("name") or "") if data else ""
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

    readme_path = root / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    sources = {
        "SKILL.md": _trigger_segment(desc),
        "README.md": _readme_triggers(readme_text),
        "skill.json": _trigger_segment(sj_desc),
    }
    present = {k: v for k, v in sources.items() if v is not None}
    if not present:
        check(results, "trigger phrases consistent", True, "no 触发 segment anywhere")
    else:
        missing_src = [k for k, v in sources.items() if v is None]
        base = sources["SKILL.md"] if sources["SKILL.md"] is not None else next(iter(present.values()))
        diffs = []
        for k, v in present.items():
            if v != base:
                extra = sorted(v - base)
                lack = sorted(base - v)
                diffs.append(f"{k} +{extra[:3]} -{lack[:3]}")
        detail = "; ".join(([f"missing in {', '.join(missing_src)}"] if missing_src else []) + diffs)
        check(
            results,
            "trigger phrases consistent",
            not missing_src and not diffs,
            detail or f"{len(base)} phrases",
        )

    prev = previous_version(root, version) if version else ""
    if not prev:
        check(results, "no previous version in distribution set", True, "no previous version")
    else:
        hits = stale_version_hits(root, prev, sj_name)
        check(
            results,
            "no previous version in distribution set",
            not hits,
            f"{prev}: " + ", ".join(hits[:8]) if hits else f"{prev}: 0 hits",
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
