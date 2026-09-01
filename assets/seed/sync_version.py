#!/usr/bin/env python3
"""Sync VERSION file into skill.json and SKILL.md front matter."""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSION_FILE = ROOT / "VERSION"


def main() -> None:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not version:
        raise SystemExit("VERSION is empty")
    today = date.today().isoformat()

    sj_path = ROOT / "skill.json"
    data = json.loads(sj_path.read_text(encoding="utf-8"))
    data["version"] = version
    hist = data.setdefault("versionHistory", [])
    if not any(item.get("version") == version for item in hist):
        hist.insert(0, {"version": version, "date": today})
    sj_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    skill_md = ROOT / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    text = re.sub(r"^(version:\s*)[\d.]+", rf"\g<1>{version}", text, count=1, flags=re.M)
    skill_md.write_text(text, encoding="utf-8")
    print(f"synced {version}")


if __name__ == "__main__":
    main()
