#!/usr/bin/env python3
"""validate_skill.py: this repo PASS; tempfile missing name / version / ref; trigger + previous-version positives.

Single-point negatives for every rule live in test_checker_mutations.py.
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def _load_mod():
    here = Path(__file__).resolve()
    repo = here.parents[1]
    candidates = [
        repo / "assets" / "seed" / "validate_skill.py",
        repo / "governance" / "scripts" / "validate_skill.py",
    ]
    for c in candidates:
        if c.is_file():
            spec = importlib.util.spec_from_file_location("validate_skill", c)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    raise FileNotFoundError("validate_skill.py not found")


def _write_skill(root: Path, *, name="demo", description="hello", body="", version="0.1.0", sj_ver="0.1.0"):
    fm = ["---"]
    if name is not None:
        fm.append(f"name: {name}")
    if description is not None:
        fm.append(f"description: {description}")
    fm.append("---")
    fm.append("")
    fm.append(body or "# Demo\n")
    (root / "SKILL.md").write_text("\n".join(fm), encoding="utf-8")
    (root / "VERSION").write_text(version + "\n", encoding="utf-8")
    (root / "skill.json").write_text(
        json.dumps({"name": name or "demo", "version": sj_ver}),
        encoding="utf-8",
    )


class ValidateSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_mod()
        cls.repo = Path(__file__).resolve().parents[1]

    def _failed_names(self, root: Path) -> set[str]:
        return {name for name, ok, _ in self.mod.run_checks(root) if not ok}

    def test_this_repo_passes(self):
        results = self.mod.run_checks(self.repo)
        failed = [(n, d) for n, ok, d in results if not ok]
        self.assertEqual(failed, [], f"this repo should PASS: {failed}")
        self.assertEqual(self.mod.main(["--skill-root", str(self.repo)]), 0)

    def test_missing_name_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root, name=None, body="# Demo\n")
            failed = self._failed_names(root)
            code = self.mod.main(["--skill-root", str(root)])
        self.assertTrue(any("name" in n for n in failed), failed)
        self.assertNotEqual(code, 0)

    def test_version_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root, version="0.1.0", sj_ver="0.2.0")
            failed = self._failed_names(root)
        self.assertIn("skill.json.version == VERSION", failed)

    def test_missing_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root, body="# Demo\nSee references/missing.md\n")
            failed = self._failed_names(root)
        self.assertIn("referenced references/ files exist", failed)

    def test_present_reference_passes_that_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "references").mkdir()
            (root / "references" / "a.md").write_text("# a\n", encoding="utf-8")
            _write_skill(root, body="# Demo\nSee references/a.md\n")
            failed = self._failed_names(root)
        self.assertNotIn("referenced references/ files exist", failed)

    def test_trigger_forms_pass(self):
        """Folded YAML, a phrase containing '，', README 同义口令 with backticks."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text(
                "---\nname: demo\ndescription: >\n  演示。触发：我是……、关于我，你知道什么、\n"
                "  生成 画像。其它说明。\n---\n# Demo\n",
                encoding="utf-8",
            )
            (root / "VERSION").write_text("0.1.0\n", encoding="utf-8")
            (root / "skill.json").write_text(
                json.dumps(
                    {"name": "demo", "version": "0.1.0",
                     "description": "演示。触发：我是……、关于我，你知道什么、 生成 画像。其它说明。"},
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (root / "README.md").write_text(
                "# Demo\n\n同义口令：`我是……`、`关于我，你知道什么`、`生成 画像`。\n", encoding="utf-8"
            )
            failed = self._failed_names(root)
        self.assertNotIn("trigger phrases consistent", failed)

    def test_no_trigger_anywhere_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root)
            (root / "README.md").write_text("# Demo\n", encoding="utf-8")
            failed = self._failed_names(root)
        self.assertNotIn("trigger phrases consistent", failed)

    def test_previous_version_only_in_history_schema_and_changelog_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root, version="0.2.0", sj_ver="0.2.0")
            data = json.loads((root / "skill.json").read_text(encoding="utf-8"))
            data["versionHistory"] = [{"version": "0.2.0"}, {"version": "0.1.0"}]
            data["schemaVersion"] = "0.1.0"
            (root / "skill.json").write_text(json.dumps(data), encoding="utf-8")
            (root / "CHANGELOG.md").write_text("# Changelog\n\n## 0.2.0\n\n## 0.1.0\n\n对照 0.1.0\n", encoding="utf-8")
            (root / "README.md").write_text("# Demo 0.2.0，不是 0.1.00 也不是 10.1.0\n", encoding="utf-8")
            failed = self._failed_names(root)
        self.assertNotIn("no previous version in distribution set", failed)

    def test_single_changelog_heading_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_skill(root)
            (root / "CHANGELOG.md").write_text("# Changelog\n\n## 0.1.0\n", encoding="utf-8")
            failed = self._failed_names(root)
        self.assertNotIn("no previous version in distribution set", failed)


if __name__ == "__main__":
    unittest.main()
