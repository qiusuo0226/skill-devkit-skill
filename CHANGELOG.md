# Changelog

## 0.6.1 — 2026-09-01

示例改成给使用者看的对话：怎么开口、问什么、怎么回。不再把内部文件名和术语写进示例。

### Changed

- `examples/` 七篇用白话重写并按用途改名
- 初始化对用户说话与示例对齐，不念 governance / CR / AP

## 0.6.0 — 2026-09-01

简介改成能力清单。向导增加触发词工坊、英文名占用检查、出生证明；结束时审计 + 打包 dry-run 绿灯。

### Changed

- `SKILL.md` / README 主句改为覆盖：版本控制、冻结基线、升级记录、变更门禁、触发词、一键打包、发布审计

### Added

- 触发说法单独一问，写入 `description`
- 英文名对照 `~/.grok/skills` 与 bundled
- `CR-000-init`、`upgrade-to-0.1.0.md` 出生证明
- 初始化结束 `pack.py --dry-run`（不把 zip 留仓）
- 示例 07：英文名占用

## 0.5.0 — 2026-09-01

对外叙事改成「一次对话，空仓变成能自己发版的 Skill；用完即走」。初始化确认清单宣读能力；结束时跑发布审计；目标仓增加 `governance/dev.ps1`。

### Changed

- `SKILL.md` / README / `skill.json` 简介：不再用「改 Skill、写方案、发版」的常驻工具箱口吻
- README 增加与普通 SKILL.md 脚手架的对照表

### Added

- 目标仓 `governance/dev.ps1`（sync / snapshot / audit / pack / release）
- 初始化写完后跑 `audit_release.py` 并汇报

## 0.4.0 — 2026-09-01

只允许空文件夹或空 git 仓初始化（用一次）。目标仓写入完整治理：版本控制、基线、升级记录、打包、审计，以及本地提示词。README 增加功能清单。

### Changed

- 非空目录改为直接停止，不再问「能不能在这里初始化」
- 初始化结束时打 `0.1.0` 基线；后续流程指向目标仓 `governance/rules/skill-governance.md`

### Added

- 目标仓种子：治理提示词、`AGENTS.md`、基线快照脚本、发布审计、IA / upgrade-to 模板、`tests/`
- README「初始化后，开发仓自带这些能力」清单

## 0.3.0 — 2026-09-01

本包只负责初始化。目标仓的 `governance/` 即完整版本控制，之后不必再调用本包。补对话示例与 README。

### Changed

- `SKILL.md` 去掉 Agent A/B、写 AP、发版等升级路由；已有 `SKILL.md` 时拒绝再初始化，不改走升级
- 初始化结束语与目标仓 README：升版本、打包用仓内 `governance/`，不再指向 skill-devkit

### Added

- `examples/`：空文件夹、一句话带齐、拒绝重复初始化、非空目录、名称不合法、初始化之后打包

## 0.2.0 — 2026-09-01

初始化开发仓：空文件夹可触发；问答后写入 git 与 `governance/` 版本控制目录（含打包）。

### Added

- `references/01-init.md` 初始化流程
- `assets/seed/`、`assets/templates/` 目标仓种子与模板
- `SKILL.md` 广触发与空目录路由（无 `SKILL.md` 不再一律停止）

## 0.1.0 — 2026-09-01

独立开发仓骨架。与 ChronoPM 分仓。本版仅入口、版本触点与核心门禁。

### Added

- `SKILL.md` 路由与硬闸
- `references/00-core.md`
- `governance/planning/`（方案草稿位）
- MIT 许可证
