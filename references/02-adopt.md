# 收编已有技能

工作区 = 用户选中的文件夹。本流程把**已经有 `SKILL.md`、但还没有本包这套规范**的仓补上版本 / 基线 / 治理 / 打包，**不改技能怎么干活**。

种子与模板从本包根复制：`assets/seed/`、`assets/templates/`。先定位本包根（含本包 `SKILL.md` 且 `name: skill-devkit`）。种子缺失 → 停止。

写完后本包退场。之后升版本走目标仓 `governance/rules/skill-governance.md`（及 `upgrade-dual-agent.md`）。

## 1. 何时走本文件

见 `SKILL.md` 路由。触发：收编这个 skill / 把现有 skill 纳入基线 / 改造现有 skill / adopt。

对已有技能说「初始化」：走 `01-init.md` §2，**停止并指路收编**，不在 01 里写盘。

## 2. 收编前检查（未通过 = 不写盘）

判定顺序见 `00-core.md`：**先 E，再半套，再下列项。** 恢复节仍执行第 4、5、6、7、8 项；只让第 2、3 项让位于 E/半套。

拒绝并说明原因：

1. 无 `SKILL.md`（空目录应走初始化）
2. 已规范（E）：至少一件种子痕迹，且有非空版本基线目录 → 停止
3. 有 `governance/` 但无种子痕迹（来源不明，不覆盖）。半套（有痕迹、无非空版本基线目录）不落入本条，走恢复节
4. 工作区是本包（根 `SKILL.md` 的 `name: skill-devkit`，或存在 `assets/seed/skill-governance.md`）
5. 工作区位于已探测的助手技能安装根之下（算法见 `references/03-skill-roots.md`；能跑则跑 `scripts/discover_skill_roots.py --contains <工作区>`）。零个根时本条不阻断，但必须警告
6. 业务项目：存在 `ai/.skill-version.json` 或 `ai/todos/`
7. 英文名无法从 `skill.json` / front matter 读出，且用户未提供合法名
8. **版本多源冲突**：根 `VERSION`、`skill.json` 的 `version`、`SKILL.md` front matter 的 `version` 之中，任意两处有值且字符串不一致 → 列出三处，停止。未决禁止猜。

通过后进入提问。已从文件读到的不要再问。半套走恢复节，不重问已写入的字段。

## 3. 版本（只补 `VERSION` 一次）

收编完成后目标仓仍遵守：根目录 `VERSION` 是唯一可读源。

**采用哪个号（读，不写）：** `VERSION` 非空 → 就是它；否则 `skill.json` 的 `version`；否则 front matter 的 `version`；否则 `0.1.0`。

**写盘：**

| 情况 | 动作 |
|---|---|
| 无 `VERSION` | 按采用号写一次 |
| 已有 `VERSION` | 不改内容 |
| 无 `skill.json` | 按现有 `SKILL.md` 生成，`version` = 采用号 |
| 已有 `skill.json` 且 `version` 缺失 | 只补 `version`（及缺失的 `name`）；不改 description |
| 已有 `skill.json` 且 `version` 已有 | 不反向改（能写盘说明已与采用号一致） |

收编不升版本。基线目录名 = 该采用号。

## 4. 先读后补

必须先读、再在确认清单里用白话复述，用户说「按这个写」才写盘：

1. 根 `SKILL.md`（英文名、说明、触发、正文结构）
2. 若有：`skill.json`、`VERSION`、`CHANGELOG.md`、`LICENSE`、`README.md`、`AGENTS.md`
3. 目录：`references/`、`scripts/`、`assets/`、`tests/`、`.git/`
4. 点名不会改的文件：技能正文、已有规则与脚本

复述至少：英文名、干什么、现有规则文件数、将采用的版本号。禁止把本包 `SKILL.md.tmpl` 覆盖目标仓。

提问（一次一项）：

1. 复述英文名 / 用途 / 将采用版本，问是否按这个收编
2. 英文名不合法 → 先改名（规则同初始化）
3. 无 description 或无开口说法 → 补问
4. 无 LICENSE → 版权写谁。先跑 `git config --get user.name`（工作区，失败再全局；失败当空）。非空则默认用该名须点头；空则问「版权写谁？」，不要提示「仇索」
5. 占用检查（同 `01-init.md` §3.1 / `03-skill-roots.md`；仅警告）
6. 确认清单：补版本与打包、不改技能怎么干活、保留哪些文件、采用版本、许可证、git 提交

不问升到几、不问是否安装到助手、不问工作区 schema。版本冲突是硬闸，不在本清单里顺带问。

## 5. 补缺表（无则写入，有则不覆盖）

| 目标 | 收编动作 |
|---|---|
| `SKILL.md` 正文与 front matter | 默认不改。例外：英文名不合法且用户确认改名 → 只改 `name` |
| `SKILL.md` 路由表「技能做不到 / 记成升级需求」行 | **不覆盖**已有路由。无该行则在表末**只追加一行**，指向 `references/gap-capture.md` |
| `references/` 已有文件 | 不覆盖；无该目录或无 README 才补种子 README |
| `references/gap-capture.md` | 无则从 `assets/seed/gap-capture.md` 拷入 |
| `scripts/`、`assets/`、`tests/` 已有文件 | 不覆盖；缺目录才建；缺 `.gitkeep` / `tests/README.md` / `tests/run_smoke.py` / `tests/test_pack_exclude.py` / `tests/test_validate_skill.py` 才补 |
| `assets/templates/skill-gap-demand.md` | 无则从本包 `assets/templates/skill-gap-demand.md` 拷入（先建目录） |
| `LICENSE` / `README.md` | 有则保留；无 README 才按模板写 |
| `.gitignore` | 无则写入种子；有则只追加种子里缺失的行 |
| `AGENTS.md` | 无则写入种子；有且未指向 `skill-governance.md` §14 则文首追加指针，不删原文 |
| `VERSION` | 见 §3 |
| `skill.json` | 见 §3 |
| `CHANGELOG.md` | 无则新建并含当前版本收编段；已有该版本标题 → 不动正文；无该版本标题 → 文首追加收编段 |
| `governance/` | 正常收编：**必须不存在**才整棵创建。恢复（D）：按拷贝表补缺种子，不覆盖已有文件 |
| `governance/rules/upgrade-dual-agent.md` | 随整棵 `governance/` 从种子拷入（`governance/` 本不存在） |
| 出生证明 | `CR-000-adopt.md`；`governance/migrations/upgrade-to-{采用版本}.md`。不写「空架子、无业务能力」。额外根文件列入出生 CR |

漏装 dual-agent / gap-capture / 缺口模板 / 路由追加行 = 收编失败，须补拷后再打基线。

整棵 `governance/` 用本版种子（含 §13 `outputs/`、§2.11 B 随 AP 删、§14 双路径口令）。按 `01-init.md` §5 拷贝表写入所有 `governance/` 目标（含 `pack.ini`、`scripts/pack_exclude.py`）。

占位符与初始化相同：`__NAME__` `__DISPLAY_NAME__` `__DESCRIPTION__` `__COPYRIGHT__` `__YEAR__` `__DATE__`。`__VERSION__` 用采用号。

## 6. 写完后顺序

1. `python governance/scripts/snapshot_baseline.py` → `governance/baselines/{VERSION}/`。目录名 = 根 `VERSION`。已有**非空**该目录则脚本失败，中止，列出已写文件。空版本目录视为未完成，允许写入。
2. `python governance/scripts/audit_release.py`。汇报通过 / 失败。有 `outputs/` 时退出码仍须为 0。
3. `python governance/pack/pack.py --skill-root . --dry-run`。点名没有 `governance/`、`.git/`、`AGENTS.md`、`outputs/`。不超过 20 条预览。不把 zip 落仓。dry-run **不是**打基线。
4. git：已有 `.git` 不 init。提交说明：`{版本} 收编：写入版本控制与基线`。不擅自 push、不默装。

中途失败：列出已写 / 未写。禁止为过检查而改用户技能正文。禁止改用户已有正文与已有规则。允许按拷贝表补缺种子并续跑收尾。真要放弃：回退该次 commit 或删掉未提交的 `governance/`。

## 7. 结束语（白话）

> 收编好了。英文名 / 中文名 / 版本（沿用）。技能怎么干活没改。已经能按规范升版本、打安装包。做不到的可以先记成升级需求。本包用完了。以后改这个技能，把工作区留在这个文件夹直接说就行。

## 8. 失败

检查未过 → 不写盘。用户拒绝默认项 → 按改后的写。写盘失败 → 已写列出。中途取消 → 已写留下并列出，不擅自删。

## 9. 中断恢复

不新增问项。确认清单前禁止写盘。仍执行 §2 第 4、5、6、7、8 项。

| 阶段 | 磁盘 | 怎么继续 |
|---|---|---|
| 问答中 / 清单未确认 | 无 `governance/` 半套 | 同对话已答不重问。新对话重问未确认项 |
| 写盘中（D） | 用户 `SKILL.md` + 种子痕迹 + 无非空版本基线目录 | 不改正文。按 §5 拷贝表补缺（含 tests 冒烟与结构校验测试），再从失败的 snapshot / audit / dry-run / git 继续 |
| 已规范（E） | 痕迹 + 非空基线 | 停止 |

对用户说话：已经读到的 / 已经写入的 / 下一步。用户再说「收编这个 skill」「接着写」「继续」即可进入本节。

