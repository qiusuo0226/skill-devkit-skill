# tests/

本包回归用例。发布前至少各 1 条：正向、反向、旧能力未破坏。发版时在 RR 里引用。

| 文件 | 覆盖 |
|---|---|
| `adopt.md` | 收编正/反/旧；半套续跑 |
| `upgrade-roles.md` | A/B 路径与硬闸 |
| `gap-capture.md` | 缺口落盘、不改正文；X1 pack.ini |
| `init-resume.md` | 半套续跑、已规范仍停、空基线目录 |
| `run_smoke.py` | 可执行冒烟入口 |
| `test_pack_exclude.py` | 排除加载器 |
| `test_validate_skill.py` | 结构校验（frontmatter / 版本 / 引用） |
| `test_skill_roots.py` | 技能目录探测（本包） |
