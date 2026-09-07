# upgrade-to-0.9.0

| 字段 | 值 |
|---|---|
| 目标版本 | 0.9.0 |
| 上一版本 | 0.8.0 |
| CR | CR-20260907-001 |
| 日期 | 2026-09-07 |
| git | tag `v0.9.0`（对照 `v0.8.0`） |

## 这版改了什么

- **结构校验**：`validate_skill.py` 查 `SKILL.md` frontmatter `name`/`description`、正文与 `references/README.md` 里的 `references/*.md` 是否存在、`VERSION` 是否等于 `skill.json.version`。
- **目标仓**：初始化/收编写入 `governance/scripts/validate_skill.py` 与 `tests/test_validate_skill.py`。`audit_release.py` 先跑校验再跑原基线/打包断言。`dev.ps1 validate` 可单跑。
- **本包**：`python assets/seed/validate_skill.py --skill-root .`。仍不跑 seed `audit_release.py`（无 `governance/baselines/`）。

## 使用者要做什么

- [x] 无需迁移工作区
- [ ] 要用新校验：用新 zip / 新目录替换已安装的本包
- [ ] 已用 0.8.x 初始化过的仓**不会**自动长出校验脚本；要此能力请手拷本版种子，勿对本包说升级（已规范仓会停）
- [ ] 新初始化 / 新收编的仓自带上述能力

## 不兼容说明

无。目标仓 `audit_release.py` 在 0.9.0 种子下会多一轮结构校验；缺 name/description 或断引用时发版会 FAIL（以前不会拦）。

## 回滚

`git checkout v0.8.0`。本包对照物是 git tag，不是 `governance/baselines/`。不要在半套 0.9.0 上打补丁。
