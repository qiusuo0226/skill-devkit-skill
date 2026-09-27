#!/usr/bin/env python3
"""Single-point mutation self-test for the release checkers.

Builds a known-good repo in a temp dir using the *target-repo layout*
(governance/pack/pack.py + governance/scripts/*), then applies one mutation per
case and asserts that exactly the named rule reports FAIL (plus only the
cascade rules the case declares). A coverage guard fails when a checker rule
has no mutation case, so a new rule without a test turns the smoke red.

Covered: governance/scripts/validate_skill.py, governance/scripts/audit_release.py,
governance/pack/pack.py + pack_exclude.py (pack.ini dirs / files / exts).
Stdlib only. Picked up by tests/run_smoke.py.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LINE_RE = re.compile(r"^\[(PASS|FAIL)\] (.+?)(?: — .*)?$")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

DEFAULT_INI = (
    "[exclude]\n"
    "dirs = .git, governance, tests, outputs, __pycache__, .idea, .vscode, .qoder\n"
    "files = .gitignore, .DS_Store, Thumbs.db, AGENTS.md\n"
    "exts = .pyc, .pyo, .zip, .tar, .gz\n"
)
TRIGGERS = "演示一下、试试 demo、关于我，你知道什么"
FIXED_FINDER = 'here.parent / "scripts" / "pack_exclude.py"'
BUGGY_FINDER = 'here.parents[2] / "governance" / "scripts" / "pack_exclude.py"'


def _source(name: str) -> Path:
    """Checker source in this repo: skill-devkit seed layout or target layout."""
    seed = REPO / "assets" / "seed" / name
    if seed.is_file():
        return seed
    target = REPO / "governance" / ("pack" if name == "pack.py" else "scripts") / name
    if target.is_file():
        return target
    raise FileNotFoundError(name)


def build_fixture(root: Path) -> None:
    (root / "governance" / "pack").mkdir(parents=True)
    (root / "governance" / "scripts").mkdir(parents=True)
    (root / "governance" / "planning").mkdir(parents=True)
    (root / "governance" / "baselines" / "0.2.0").mkdir(parents=True)
    (root / "governance" / "baselines" / "0.2.0" / "SKILL.md").write_text("frozen\n", encoding="utf-8")
    shutil.copy2(_source("pack.py"), root / "governance" / "pack" / "pack.py")
    for n in ("pack_exclude.py", "audit_release.py", "validate_skill.py"):
        shutil.copy2(_source(n), root / "governance" / "scripts" / n)
    (root / "governance" / "pack.ini").write_text(DEFAULT_INI, encoding="utf-8")
    (root / "references").mkdir()
    (root / "references" / "a.md").write_text("# a\n", encoding="utf-8")
    (root / "SKILL.md").write_text(
        "---\nname: demo\ndescription: >\n  演示技能。触发：演示一下、试试 demo、\n  关于我，你知道什么。\n---\n"
        "# Demo\n\n细则见 references/a.md\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text(
        f"# Demo\n\n触发：`演示一下`、`试试 demo`、`关于我，你知道什么`。\n", encoding="utf-8"
    )
    (root / "VERSION").write_text("0.2.0\n", encoding="utf-8")
    (root / "skill.json").write_text(
        json.dumps(
            {
                "name": "demo",
                "version": "0.2.0",
                "description": f"演示技能。触发：{TRIGGERS}。",
                "versionHistory": [{"version": "0.2.0"}, {"version": "0.1.0"}],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (root / "CHANGELOG.md").write_text("# Changelog\n\n## 0.2.0\n\n改了。\n\n## 0.1.0\n\n初始化。\n", encoding="utf-8")
    (root / "LICENSE").write_text("MIT\n", encoding="utf-8")
    (root / "tests").mkdir()
    # Plain script, not unittest: no recursion back into this file. Prints non-GBK text on purpose.
    (root / "tests" / "run_smoke.py").write_text(
        "import sys\nsys.stdout.write('smoke \\u2713 \\u2014 \\U0001F642 中文\\n')\nsys.exit(0)\n",
        encoding="utf-8",
    )


def _rw(root: Path, rel: str, old: str, new: str) -> None:
    p = root / rel
    text = p.read_text(encoding="utf-8")
    assert old in text, f"{rel}: {old!r} not found"
    p.write_text(text.replace(old, new), encoding="utf-8")


def _rm(root: Path, rel: str) -> None:
    p = root / rel
    shutil.rmtree(p) if p.is_dir() else p.unlink()


def _put(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def _norm(name: str) -> str:
    return re.sub(r"^baseline .* exists$", "baseline {version} exists", name)


def run_checker(root: Path, checker: str):
    if checker == "validate":
        cmd = [sys.executable, str(root / "governance" / "scripts" / "validate_skill.py"), "--skill-root", str(root)]
    else:
        cmd = [sys.executable, str(root / "governance" / "scripts" / "audit_release.py")]
    proc = subprocess.run(
        cmd, cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV
    )
    rules = {}
    for line in proc.stdout.splitlines():
        m = LINE_RE.match(line)  # column 0 only; audit indents the nested validate output
        if m:
            rules[_norm(m.group(2))] = m.group(1)
    return proc, rules


def pack_listing(root: Path):
    proc = subprocess.run(
        [sys.executable, str(root / "governance" / "pack" / "pack.py"), "--skill-root", str(root), "--dry-run"],
        cwd=str(root), capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV,
    )
    files = {l.strip() for l in proc.stdout.splitlines()[1:] if l.startswith("  ")}
    return proc, files


TRIG = "trigger phrases consistent"
PREV = "no previous version in distribution set"
V_OK = "validate_skill.py"

# (checker, rule, case id, mutation, allowed cascade)
CASES = [
    # validate_skill.py
    ("validate", "SKILL.md exists", "rm SKILL.md", lambda r: _rm(r, "SKILL.md"), {TRIG}),
    ("validate", "SKILL.md has YAML frontmatter", "strip front matter",
     lambda r: _put(r, "SKILL.md", "# Demo\n\n细则见 references/a.md\n"),
     {"frontmatter name non-empty", "frontmatter description non-empty", TRIG}),
    ("validate", "frontmatter name non-empty", "blank name", lambda r: _rw(r, "SKILL.md", "name: demo", "name:"), set()),
    ("validate", "frontmatter description non-empty", "blank description",
     lambda r: _put(r, "SKILL.md", "---\nname: demo\ndescription:\n---\n# Demo\n\n细则见 references/a.md\n"), {TRIG}),
    ("validate", "VERSION exists", "rm VERSION", lambda r: _rm(r, "VERSION"), {"VERSION non-empty"}),
    ("validate", "VERSION non-empty", "empty VERSION", lambda r: _put(r, "VERSION", "\n"), set()),
    ("validate", "skill.json exists", "rm skill.json", lambda r: _rm(r, "skill.json"), {TRIG}),
    ("validate", "skill.json is JSON", "broken JSON", lambda r: _put(r, "skill.json", "{bad"),
     {"skill.json.version == VERSION", TRIG}),
    ("validate", "skill.json.version == VERSION", "version drift",
     lambda r: _rw(r, "skill.json", '"version": "0.2.0",\n  "description"', '"version": "0.9.9",\n  "description"'), set()),
    ("validate", "referenced references/ files exist", "rm references/a.md", lambda r: _rm(r, "references/a.md"), set()),
    ("validate", TRIG, "README drops one phrase", lambda r: _rw(r, "README.md", "、`试试 demo`", ""), set()),
    ("validate", TRIG, "skill.json lacks 触发", lambda r: _rw(r, "skill.json", f"触发：{TRIGGERS}。", ""), set()),
    ("validate", PREV, "README keeps previous version", lambda r: _put(r, "README.md",
     "# Demo\n\n触发：`演示一下`、`试试 demo`、`关于我，你知道什么`。\n\n当前 0.1.0\n"), set()),
    ("validate", PREV, "old zip name left", lambda r: _put(r, "references/a.md", "# a\n安装 demo-Skill-v0.1.0.zip\n"), set()),
    # audit_release.py
    ("audit", "VERSION exists", "rm VERSION", lambda r: _rm(r, "VERSION"),
     {"VERSION non-empty", "skill.json.version == VERSION", V_OK, "baseline {version} exists"}),
    ("audit", "VERSION non-empty", "empty VERSION", lambda r: _put(r, "VERSION", "\n"),
     {"skill.json.version == VERSION", V_OK, "baseline {version} exists"}),
    ("audit", "skill.json exists", "rm skill.json", lambda r: _rm(r, "skill.json"), {V_OK}),
    ("audit", "skill.json.version == VERSION", "version drift",
     lambda r: _rw(r, "skill.json", '"version": "0.2.0",\n  "description"', '"version": "0.9.9",\n  "description"'), {V_OK}),
    ("audit", "skill.json has name", "drop name", lambda r: _rw(r, "skill.json", '"name": "demo",', ""), set()),
    ("audit", "CHANGELOG.md exists", "rm CHANGELOG", lambda r: _rm(r, "CHANGELOG.md"), set()),
    ("audit", "CHANGELOG has this version heading", "drop heading",
     lambda r: _rw(r, "CHANGELOG.md", "## 0.2.0\n", "改动：\n"), set()),
    ("audit", "SKILL.md exists", "rm SKILL.md", lambda r: _rm(r, "SKILL.md"), {V_OK}),
    ("audit", "LICENSE exists", "rm LICENSE", lambda r: _rm(r, "LICENSE"), set()),
    ("audit", "validate_skill.py present", "rm validator", lambda r: _rm(r, "governance/scripts/validate_skill.py"), set()),
    ("audit", V_OK, "validator-only defect", lambda r: _rm(r, "references/a.md"), set()),
    ("audit", "baseline {version} exists", "rm baseline", lambda r: _rm(r, "governance/baselines/0.2.0"), set()),
    ("audit", "pack.ini dirs not empty (no silent empty exclude)", "empty dirs",
     lambda r: _rw(r, "governance/pack.ini", "dirs = .git, governance, tests, outputs, __pycache__, .idea, .vscode, .qoder", "dirs ="), set()),
    ("audit", "pack.py load_sets reachable", "rm pack.py", lambda r: _rm(r, "governance/pack/pack.py"), set()),
    ("audit", "pack.py found pack_exclude.py (no builtin fallback)", "legacy parents[2] path bug, default ini",
     lambda r: _rw(r, "governance/pack/pack.py", FIXED_FINDER, BUGGY_FINDER), set()),
    ("audit", "pack.py found pack_exclude.py (no builtin fallback)", "legacy parents[2] path bug, edited ini",
     lambda r: (_rw(r, "governance/pack/pack.py", FIXED_FINDER, BUGGY_FINDER),
                _rw(r, "governance/pack.ini", ".qoder\n", ".qoder, extra_dir\n")),
     {"pack.py and audit load_excludes agree"}),
    ("audit", "pack.py and audit load_excludes agree", "pack.py drops a dir",
     lambda r: _rw(r, "governance/pack/pack.py", "    return mod.load_excludes(root)",
                   "    d, f, e, x = mod.load_excludes(root)\n    return set(d) - {'tests'}, f, e, x"), set()),
    ("audit", "pack set has no governance/.git/AGENTS.md", "ini stops excluding governance",
     lambda r: _rw(r, "governance/pack.ini", "dirs = .git, governance,", "dirs = .git,"), set()),
    ("audit", "no AP left for published version", "AP left behind",
     lambda r: _put(r, "governance/planning/upgrade-plan-v0.2.0.md", "# AP\n"), set()),
    ("audit", "tests/run_smoke.py", "smoke fails", lambda r: _put(r, "tests/run_smoke.py", "import sys\nsys.exit(1)\n"), set()),
]

# pack.ini is honored by governance/pack/pack.py in the target layout
PACK_CASES = [
    ("dirs", lambda r: _rw(r, "governance/pack.ini", ".qoder\n", ".qoder, extra_dir\n"), "extra_dir/x.md"),
    ("files", lambda r: _rw(r, "governance/pack.ini", "AGENTS.md\n", "AGENTS.md, NOTES.txt\n"), "NOTES.txt"),
    ("exts", lambda r: _rw(r, "governance/pack.ini", ".gz\n", ".gz, .bak\n"), "old.bak"),
]


class CheckerMutationTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "demo"
        self.root.mkdir()
        build_fixture(self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def test_good_fixture_passes_and_every_rule_has_a_case(self):
        for checker in ("validate", "audit"):
            proc, rules = run_checker(self.root, checker)
            failed = sorted(n for n, s in rules.items() if s == "FAIL")
            self.assertEqual(proc.returncode, 0, f"{checker} on good fixture: {failed}\n{proc.stdout}\n{proc.stderr}")
            self.assertNotIn("Traceback", proc.stderr)
            self.assertNotIn("WARN", proc.stderr, f"{checker}: {proc.stderr}")
            covered = {rule for c, rule, *_ in CASES if c == checker}
            self.assertEqual(set(rules) - covered, set(), f"{checker} rules without a mutation case")
            self.assertEqual(covered - set(rules), set(), f"{checker} cases for rules that no longer exist")

    def test_each_mutation_is_caught_by_its_rule(self):
        for checker, rule, case_id, mutate, cascade in CASES:
            with self.subTest(checker=checker, case=case_id):
                with tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp) / "demo"
                    root.mkdir()
                    build_fixture(root)
                    mutate(root)
                    proc, rules = run_checker(root, checker)
                failed = {n for n, s in rules.items() if s == "FAIL"}
                self.assertNotEqual(proc.returncode, 0, f"{case_id}: exit 0\n{proc.stdout}")
                self.assertIn(rule, failed, f"{case_id}: {rule!r} not FAIL; failed={sorted(failed)}")
                self.assertLessEqual(failed - {rule}, cascade, f"{case_id}: unexpected FAIL")

    def test_pack_ini_honored_in_target_layout(self):
        _put(self.root, "extra_dir/x.md", "x\n")
        _put(self.root, "NOTES.txt", "n\n")
        _put(self.root, "old.bak", "b\n")
        proc, files = pack_listing(self.root)
        self.assertTrue({"extra_dir/x.md", "NOTES.txt", "old.bak"} <= files, files)
        for key, mutate, path in PACK_CASES:
            with self.subTest(key=key):
                mutate(self.root)
                proc, files = pack_listing(self.root)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertNotIn("WARN", proc.stderr)
                self.assertNotIn(path, files, f"pack.ini {key} ignored")
                self.assertNotIn("governance/pack.ini", files)

    def test_pack_path_bug_is_caught(self):
        """The legacy parents[2] bug: pack.ini edits silently ignored in the target layout."""
        _put(self.root, "extra_dir/x.md", "x\n")
        PACK_CASES[0][1](self.root)
        _rw(self.root, "governance/pack/pack.py", FIXED_FINDER, BUGGY_FINDER)
        proc, files = pack_listing(self.root)
        self.assertIn("WARN: pack_exclude.py missing", proc.stderr)
        self.assertIn("extra_dir/x.md", files)

    def test_audit_survives_non_gbk_child_output(self):
        proc, rules = run_checker(self.root, "audit")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertNotIn("UnicodeDecodeError", proc.stderr)
        self.assertEqual(rules.get("tests/run_smoke.py"), "PASS")


if __name__ == "__main__":
    unittest.main()
