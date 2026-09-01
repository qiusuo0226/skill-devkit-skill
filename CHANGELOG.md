# Changelog

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
