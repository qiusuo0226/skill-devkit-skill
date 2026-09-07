# Changelog

## 0.9.0 — 2026-09-07

发版前自动结构校验。对照点 `v0.8.0`。

### Added

- `assets/seed/validate_skill.py`：零依赖；`--skill-root`；查 SKILL.md frontmatter `name`/`description`、`references/` 引用存在、`VERSION` 与 `skill.json.version` 一致
- 目标仓拷贝为 `governance/scripts/validate_skill.py`；`audit_release.py` 先跑它
- `assets/seed/test_validate_skill.py` → 目标仓 `tests/test_validate_skill.py`；本仓 `tests/test_validate_skill.py`
- `dev.ps1 validate` 子命令（audit / release 已串联，不必再手跑一遍）

### Changed

- `references/01-init.md` §5 拷贝表与目录树补校验脚本与测试
- `references/02-adopt.md` 测试补缺列表加上 `test_validate_skill.py`
- README 开篇与能力清单写上结构校验；示例 06 / 08 / 13 发版检查补说明必填项和引用文件

### 测了什么

`python assets/seed/validate_skill.py --skill-root .`；`python tests/run_smoke.py`（含缺 name / 版本不一致 / 断引用反例）；`python assets/seed/pack.py --skill-root . --dry-run`（无 governance/.git/AGENTS.md）。

### 怎么回滚

`git checkout v0.8.0`。本包无 `governance/baselines/`。已用 0.8.x 初始化的目标仓不自动获得校验脚本。

## 0.8.0 — 2026-09-04

技能目录探测可配置；半套初始化/收编可续跑；打包排除收敛为 pack.ini；版权默认读 git user.name；description 触发表收缩；pack/探测可机器冒烟。对照点 `v0.7.0`。

### Added

- `references/03-skill-roots.md` 与 `scripts/discover_skill_roots.py`：环境变量 + 候选回退 + 启发式
- 初始化/收编恢复节；示例 25
- `governance/pack.ini` + `pack_exclude.py`；目标仓 `tests/run_smoke.py`
- `tests/test_pack_exclude.py`、`tests/test_skill_roots.py`、`tests/init-resume.md`

### Changed

- 占用检查、收编安装闸、试用拷贝改走同一探测算法
- 硬闸 1 允许半套续跑；完成态 = 种子痕迹 + 非空版本基线目录（不比对 VERSION）
- 版权默认改为 `git config user.name`；空则不问「仇索」
- `SKILL.md` description 收到高频触发 + 正负路由；全表迁入 `references/04-triggers.md`
- 三脚本改读 pack.ini；空 dirs 回退内置；目标仓 audit 跑冒烟，并断言 pack.py 与 audit 加载结果相等
- snapshot 对空版本目录允许续写

### 测了什么

`python tests/run_smoke.py`；`python assets/seed/pack.py --skill-root . --dry-run`（无 governance/.git/AGENTS.md）。对话表 `tests/init-resume.md`、`adopt.md`、`gap-capture.md`、`upgrade-roles.md`。

### 怎么回滚

`git checkout v0.7.0`。本包无 `governance/baselines/`。已用 0.7.x 初始化的目标仓不自动获得 pack.ini。

## 0.7.0 — 2026-09-03

空仓初始化之外增加收编；目标仓升级支持 A 出方案、B 审核或人直接执行；初始化写入技能缺口捕捉。对照点 `v0.6.4`。

### Added

- 收编：`references/02-adopt.md`；已有 `SKILL.md`、无指纹时只补骨架
- 目标仓 `governance/rules/upgrade-dual-agent.md`：路径 H / 路径 B
- `references/gap-capture.md` 与缺口模板（进目标 zip）；稿在 `outputs/skill-gaps/`（不进 zip）
- 示例 17～24

### Changed

- 三脚本 `EXCLUDE_DIRS` 同步增加 `outputs`
- `skill-governance.md` §13 白名单含 `outputs/`；§2.11 B 节随 AP 删除
- `SKILL.md` 路由与硬闸拆成初始化 / 收编；本包不加缺口路由

## 0.6.4 — 2026-09-03

升级相关示例按「完全不懂」重写：方案固定七章、文件生成在 `governance/planning/upgrade-plan-v版本.md`、审查盯什么、同意执行后会多出哪些记录。初始化示例仍保持白话问答。

### Changed

- `examples/08` 改为完整升级教程（路径、七章、填好的方案、同意后文件表、常见错法）
- `examples/06` `09` `10` `11` `12` `13` `15` 与目录、开口表对齐上述路径和步骤

## 0.6.3 — 2026-09-03

示例补上初始化之后：怎么升级、写规则、先方案后改、改开口说法、发版检查、错别字、回滚、装到助手里试用。对本包说升级会停。

### Added

- `examples/08`～`16`：升级、对本包说升级会停、写规则、直接改仍先出方案、改开口说法、发版检查没过、打错字、回滚、装到助手里试用
- `examples/README.md` 分成「初始化」和「初始化之后」两张表

### Changed

- README 开口表与示例篇数（16 篇）
- 01 / 03 / 06 链到升级和写规则

## 0.6.2 — 2026-09-01

分发包 zip 改用英文名 `{name}-Skill-v{版本}.zip`，不再用中文显示名。

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
