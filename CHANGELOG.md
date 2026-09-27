# Changelog

## 0.11.1 — 2026-09-27

本包说明与触发词改成中文作者会说的话。对照点 `v0.11.0`。用户对比 Qoder 市场技能后认为本包唤不起。人直接同意（未经 B）。

### Changed

- `SKILL.md` description：先英文后中文；写明什么时候用（空文件夹新建、接管还没管起来的技能）；去掉「Use once, then this kit exits」「本包退场」，改为「之后按仓里写好的规则升级」；负路由句保留。725 字符
- 触发 19 → 20 条，`SKILL.md`、README、`skill.json` 三处同集。新增：新建一个技能、帮我做个skill、建个skill仓库、把这个技能管起来、接管这个技能。去掉：新建技能（由「新建一个技能」替代）、收编skill（与「收编这个skill」重复）、scaffold skill（术语）、/skill-devkit init（与 /skill-devkit 重复）。去掉的仍在 `references/04-triggers.md`
- `metadata.short-description` 去掉「用完即走」
- `SKILL.md` 开篇两句、README 开篇粗体句、英文副标题、「写完本包就退场」一句：改为准确描述「建好之后不再经过本包，升级走那个仓自己的文件」
- 路由表：初始化行补「帮我做个 skill / 建个 skill 仓库」，收编行补「接管这个技能 / 把这个技能管起来」；`references/04-triggers.md`、`references/02-adopt.md` 同步
- `skill.json` description 换成新中文句 + 新触发
- 示例 17 照着说补「把这个技能管起来。」；`tests/adopt.md` 加 P4、N8
- 0.11.0 效果核对结论行补进 `RR-20260927-0.11.0.md`，核对单删除

### 测了什么

`python assets/seed/validate_skill.py --skill-root .`（12 条全 PASS，触发 20 条同集，0.11.0 零命中）；`python tests/run_smoke.py`（23 tests）；`python assets/seed/pack.py --skill-root . --dry-run`（83 files）。YAML 用 PyYAML 解析通过。对话未跑 LLM。

### 怎么回滚

`git checkout v0.11.0`。无需迁移工作区。

## 0.11.0 — 2026-09-27

发版把关从「条数够」改成「每版同题可比、规则自己被测过」，并修掉目标仓 `pack.ini` 被悄悄忽略。对照点 `v0.10.1`。来自需求稿 SG-20260927-001～004、006～008（005 不做）。人直接同意（未经 B）。

### Fixed

- 种子 `pack.py`：在目标仓 `governance/pack/` 里找不到 `governance/scripts/pack_exclude.py`（旧路径 `here.parents[2]` 指到仓的上一级），`pack.ini` 改动被忽略、退回内置名单。改为 `here.parent / "scripts" / "pack_exclude.py"`。本包自己用同目录布局，不受影响
- 种子 `audit_release.py`：新规则「pack.py found pack_exclude.py (no builtin fallback)」；默认 `pack.ini` 时原「agree」检查会把上面的错遮住
- 种子 `audit_release.py` 两处子进程与本包 `tests/test_skill_roots.py`：`encoding="utf-8", errors="replace"`，子进程 `PYTHONIOENCODING=utf-8`（中文 Windows cp936 解码）。audit 转印的 validate 输出改为缩进两格

### Added

- `validate_skill.py` 新规则「trigger phrases consistent」：`SKILL.md` description、README（「触发：」或「同义口令：」）、`skill.json` description 三处触发集合相同；只按「、」切分；三处都没有算通过
- `validate_skill.py` 新规则「no previous version in distribution set」：上一版号取 `CHANGELOG.md` 第一个不等于当前 `VERSION` 的标题；按 `pack.ini` 取分发集；不扫 `CHANGELOG.md` 与 `skill.json` 的 `versionHistory`、`schemaVersion`
- `assets/seed/test_checker_mutations.py` → 目标仓 `tests/test_checker_mutations.py`（本包 `tests/` 同内容）：按目标仓布局搭合格样仓，validate 12 条规则 14 例、audit 19 条规则 20 例单点变异，各由对应规则抓到；覆盖守卫；pack.ini dirs / files / exts 生效；旧路径缺陷专门用例；非 GBK 子进程输出
- RR 模板「固定四问」表（装得上 / 唤得起 / 答得对 / 说得清）+「上一版结果」；固定输入在 `tests/README.md`
- 方案模板与 A / B 规则：可信度标签 已验证 / 推断 / 参考；推断只进 AP-5「推断待验证」；B 只凭推断不能判阻塞
- `tests/upgrade-roles.md` U6、N15、N16

### Changed

- 种子 `skill-governance.md` §2 第 6 步：固定四问 + 正 / 反 / 旧；§3 可信度标签
- 种子 `upgrade-dual-agent.md` §2 第 5 步、§4 #3 与说明
- `release-checklist.md` 两项；种子 `tests-README.md` 固定四问占位；`test_pack_exclude.py` 加目标仓布局用例；`test_validate_skill.py` 加四条正例
- `references/01-init.md` §5 拷贝表与目录树、`references/02-adopt.md` 补缺清单加 `test_checker_mutations.py`
- 本包 README「同义口令」行改为与 `SKILL.md` 相同的「触发：」行；能力表回归报告、结构校验两行
- 本包 `skill.json` description 末尾补同一段触发（核心契约，只加不删）
- 示例 12：改开口说法要同时改 README 触发行与 `skill.json` description

### 测了什么

`python assets/seed/validate_skill.py --skill-root .`（12 条全 PASS）；`python tests/run_smoke.py`（23 tests，原 13 条 + 新 10 条）；`python assets/seed/pack.py --skill-root . --dry-run`（83 files，无 governance/.git/AGENTS.md）。反例：把 `pack.py` 改回旧路径、给 validate 加一条没配用例的假规则、让两条新规则恒真、换回 0.10.1 的 audit，冒烟都变红。按 §5 拷贝表模拟全新初始化并跑 `audit_release.py` 全 PASS。Linux 与用户 Windows（Python 3.13，cp936）两边都跑。本包根不跑 `audit_release.py`，不打基线。

### 怎么回滚

`git checkout v0.10.1`。本包无 `governance/baselines/`。已建好的目标仓不自动更新；personal-graph 需手工修 `governance/pack/pack.py`，见 `upgrade-to-0.11.0.md`。

## 0.10.1 — 2026-09-26

核对升级效果的三处句子补齐。对照点 `v0.10.0`。来自 0.10.0 效果核对的三条方案外。B1、B2 均为通过-待修订，已并入方案 1.2 后执行。

### Changed

- 种子 `AGENTS.md` 入口加上活动名「核对升级效果」，仍只指向 §14，不另列口令
- `references/00-core.md` 确认工作区表末行补上「检查升级效果 / 检查开发仓实际升级效果 / 升级做完了核对一下」，看见仍停止、不写盘。该行与 `SKILL.md` 路由行的其余差异不动
- 写盘边界嵌入角色表、效果核对节开头、效果核对节末行、§14，四处同一句：不改技能正文，不改方案正文，不建 CR；写盘只允许核对单本身；方案已删则把文首结论一行补进该版已有回归报告后删核对单。除此以外改文件算失败。原有「不是 B 审核」「不顺手清残留」「只按模板回复」以及节末针对禁止标题和未满足的「都算失败」保留。第 6 步两种时机不改
- `tests/upgrade-roles.md` N12：改残留注释或技能正文仍失败；写核对单或补已有回归报告的结论行不算这条失败

### 测了什么

`python assets/seed/validate_skill.py --skill-root .`；`python tests/run_smoke.py`；`python assets/seed/pack.py --skill-root . --dry-run`（无 governance/.git/AGENTS.md）。对话表实读，未跑对话。本包根不跑 `audit_release.py`，不打基线。

### 怎么回滚

`git checkout v0.10.0`。本包无 `governance/baselines/`。已建好的目标仓不自动更新。新初始化会带上新种子。新收编仅当 `AGENTS.md` 缺失或未指向 §14 时写出新入口句。

## 0.10.0 — 2026-09-25

升级做完后的效果核对固定成三栏编号清单。对照点 `v0.9.0`。

### Added

- `assets/templates/upgrade-effect.md`：空核对单。满足 / 未满足 / 方案外；一条方案行一个编号
- 初始化拷贝到目标仓 `governance/templates/upgrade-effect.md`
- `assets/seed/upgrade-dual-agent.md` 效果核对节：口令、对照顺序、回复只贴核对单、不改文件
- 示例 26

### Changed

- 目标仓 `skill-governance.md` §14 增加核对口令；§2 第 11 步删掉发版前已写出的核对单，结论行写入 RR
- 发版后才写出的核对单：当次把结论行补进该版 RR 后删除
- 本包 `SKILL.md` 路由：对本包说核对口令则停止，换到目标仓
- 索引：README、示例目录、种子 `planning/` 与 `governance/` 说明、`tests/upgrade-roles.md`（U4、U5、N11–N14）

### 测了什么

`python assets/seed/validate_skill.py --skill-root .`；`python tests/run_smoke.py`；`python assets/seed/pack.py --skill-root . --dry-run`（无 governance/.git/AGENTS.md）。对话表 `tests/upgrade-roles.md` 已写入，未跑对话。

### 怎么回滚

`git checkout v0.9.0`。本包无 `governance/baselines/`。已用 0.9.x 及更早初始化的目标仓不自动获得核对单。

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
