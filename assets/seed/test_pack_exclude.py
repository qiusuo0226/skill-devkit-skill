#!/usr/bin/env python3
"""pack_exclude loader: never empty dirs; empty ini dirs fallback + flag."""
from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

BUILTIN_DIRS = {".git", "governance", "tests", "outputs", "__pycache__", ".idea", ".vscode", ".qoder"}


def _load_mod():
    here = Path(__file__).resolve()
    repo = here.parents[1]
    candidates = [
        repo / "assets" / "seed" / "pack_exclude.py",
        repo / "governance" / "scripts" / "pack_exclude.py",
    ]
    for c in candidates:
        if c.is_file():
            spec = importlib.util.spec_from_file_location("pack_exclude", c)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    raise FileNotFoundError("pack_exclude.py not found")


class PackExcludeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_mod()

    def _load_expect_warn(self, root):
        buf = io.StringIO()
        with redirect_stderr(buf):
            result = self.mod.load_excludes(root)
        err = buf.getvalue()
        self.assertIn("WARN", err, "expected WARN on constructed missing/empty pack.ini")
        return result

    def test_missing_ini_uses_builtin_expected_warn(self):
        with tempfile.TemporaryDirectory() as tmp:
            dirs, files, exts, empty = self._load_expect_warn(Path(tmp))
        self.assertEqual(dirs, BUILTIN_DIRS)
        self.assertFalse(empty)
        self.assertTrue(dirs)

    def test_empty_dirs_in_ini_fallback_and_flag_expected_warn(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "governance").mkdir()
            (root / "governance" / "pack.ini").write_text(
                "[exclude]\ndirs =\nfiles = .gitignore\nexts = .pyc\n",
                encoding="utf-8",
            )
            dirs, files, exts, empty = self._load_expect_warn(root)
        self.assertTrue(empty)
        self.assertEqual(dirs, BUILTIN_DIRS)
        self.assertIn(".gitignore", files)
        self.assertIn(".pyc", exts)

    def test_pack_py_agrees_with_loader(self):
        repo = Path(__file__).resolve().parents[1]
        pack_py = repo / "assets" / "seed" / "pack.py"
        if not pack_py.is_file():
            pack_py = repo / "governance" / "pack" / "pack.py"
        self.assertTrue(pack_py.is_file(), "pack.py not found")
        spec = importlib.util.spec_from_file_location("pack_mod", pack_py)
        pack_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pack_mod)
        via_loader = self.mod.load_excludes(repo)
        via_pack = pack_mod.load_sets(repo)
        self.assertEqual(via_loader[:3], via_pack[:3])

    def test_ini_dirs_honored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "governance").mkdir()
            (root / "governance" / "pack.ini").write_text(
                "[exclude]\ndirs = .git, governance, tests, outputs, __pycache__, .idea, .vscode, .qoder, extra_dir\n"
                "files = .gitignore, .DS_Store, Thumbs.db, AGENTS.md\n"
                "exts = .pyc, .pyo, .zip, .tar, .gz\n",
                encoding="utf-8",
            )
            dirs, _files, _exts, empty = self.mod.load_excludes(root)
        self.assertFalse(empty)
        self.assertIn("extra_dir", dirs)
        self.assertIn("governance", dirs)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False).result.wasSuccessful() else 1)
