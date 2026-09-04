# tests/

本 Skill 的回归用例。发布前至少各 1 条：正向、反向、旧能力未破坏。

初始化时带一份 pack 冒烟脚本（`run_smoke.py`）。用例用 Markdown 或脚本均可，发版时在 RR 里引用。目标仓 `audit_release.py` 若发现 `tests/run_smoke.py` 会跑它。
