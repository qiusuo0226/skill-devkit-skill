# tests/

本包回归用例。每版先答固定四问（见下），再加正向、反向、旧能力未破坏各至少 1 条。发版时在 RR 里引用。

## 固定四问

每版 RR 同题同输入，对照上一版 RR。0.11.0 起。

| 问题 | 固定输入 |
|---|---|
| 装得上 | `python assets/seed/pack.py --skill-root . --dry-run`：文件数；无 `governance/`、`.git/`、根上 `AGENTS.md` |
| 唤得起 | 实读 `SKILL.md` description 触发段；`validate_skill.py` 的「trigger phrases consistent」与 README、`skill.json` 三处一致 |
| 答得对 | `tests/upgrade-roles.md` R4：空仓初始化仍 7 问（实读）；`python tests/run_smoke.py` 退出 0 |
| 说得清 | `python assets/seed/validate_skill.py --skill-root .` 全 PASS；README 开口表与 `examples/README.md` 目录实读 |

| 文件 | 覆盖 |
|---|---|
| `adopt.md` | 收编正/反/旧；半套续跑 |
| `upgrade-roles.md` | A/B 路径、效果核对与硬闸 |
| `gap-capture.md` | 缺口落盘、不改正文；X1 pack.ini |
| `init-resume.md` | 半套续跑、已规范仍停、空基线目录 |
| `run_smoke.py` | 可执行冒烟入口 |
| `test_pack_exclude.py` | 排除加载器 |
| `test_validate_skill.py` | 结构校验（frontmatter / 版本 / 引用 / 触发词三处 / 上一版号） |
| `test_checker_mutations.py` | 检查器单点变异 + 覆盖守卫；目标仓布局的 pack.ini 生效 |
| `test_skill_roots.py` | 技能目录探测（本包） |
