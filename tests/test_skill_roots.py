#!/usr/bin/env python3
"""discover_skill_roots.py: env override, --contains, --check-name, no throw on zero extra roots."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "discover_skill_roots.py"


def _run(args, extra_env=None):
    e = os.environ.copy()
    for k in ("GROK_HOME", "LINGXI_HOME", "CLAUDE_HOME", "CODEX_HOME", "SKILL_DEVKIT_SKILLS_DIRS"):
        e.pop(k, None)
    if extra_env:
        e.update(extra_env)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        env=e,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(proc.stderr or proc.stdout)
    return json.loads(proc.stdout)


class SkillRootsTests(unittest.TestCase):
    def test_env_dirs_and_check_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "skills"
            skill = root / "foo"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: foo\n---\n", encoding="utf-8")
            data = _run(
                ["--check-name", "foo"],
                extra_env={"SKILL_DEVKIT_SKILLS_DIRS": str(root)},
            )
            paths = [r["path"] for r in data["roots"]]
            self.assertTrue(any(Path(p).resolve() == root.resolve() for p in paths))
            self.assertTrue(data["hits"])

    def test_contains_under_env_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "skills"
            ws = root / "bar"
            ws.mkdir(parents=True)
            data = _run(
                ["--contains", str(ws)],
                extra_env={"SKILL_DEVKIT_SKILLS_DIRS": str(root)},
            )
            self.assertTrue(data["workspace_in_install_dir"])

    def test_heuristic_dotdir_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp) / ".grok" / "skills" / "demo"
            ws.mkdir(parents=True)
            data = _run(["--contains", str(ws)], extra_env={"SKILL_DEVKIT_SKILLS_DIRS": ""})
            self.assertTrue(data["workspace_in_install_dir"])

    def test_zero_override_does_not_throw(self):
        data = _run([], extra_env={"SKILL_DEVKIT_SKILLS_DIRS": ""})
        self.assertIn("roots", data)
        self.assertFalse(data["workspace_in_install_dir"])


if __name__ == "__main__":
    unittest.main()
