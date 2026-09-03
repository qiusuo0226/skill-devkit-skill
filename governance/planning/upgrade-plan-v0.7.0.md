---
AP Version: 1.5
Status: pending_review
Target Version: 0.7.0
---

# 升级方案审查文档

Skill：skill-devkit  
相对 1.4：吸收 B2「通过-待修订」三条非阻塞建议，写入执行清单，**无需再审**。不改已有 `## B2 审核结果`。

| B2 建议 | 1.5 怎么写死 |
|---|---|
| 01-init §4 树与 §5 复制表同步补缺口模板 | §4 目录树写出 `assets/templates/skill-gap-demand.md`、`references/gap-capture.md`、`governance/rules/upgrade-dual-agent.md`；§5 复制表与树同一套。**不预写** `outputs/` |
| 02-adopt 补缺表不能只看 1.1 | 3.13 + AP-4：`02-adopt.md` 补缺表**显式**含 dual-agent、gap-capture、缺口模板、SKILL.md 路由追加行 |
| 执行 X2 时有 `outputs/` 审计仍通过 | X2 验收写死：`audit_release.py` 退出码 0；基线与 dry-run 路径均不含 `outputs/` |

相对 1.3：吸收 B1 P1～P3（见 1.4 钉死表，口径不变）。

钉死（1.4 保留）：

| B1 | 1.4 怎么改 |
|---|---|
| P1 三脚本 EXCLUDE 必须同步加 `outputs` | AP-4 同时改 `pack.py`、`snapshot_baseline.py`、`audit_release.py`；三套 `EXCLUDE_*` 保持同一内容；回归加「三者一致」 |
| P2 `outputs/` 对根白名单的身份 | `skill-governance.md` **§13 白名单加入 `outputs/`**，注明：运行时生成物目录，懒建；其下稿件不须每次进 AP-4；禁止把缺口稿散落在根上 |
| P3 B 节随 AP 删除 | §2 第 11 步补一句：B 审核节在该 AP 文末，随文件删除；已固化到 CR / CHANGELOG / 基线 / upgrade-to，不另存 B 副本 |
| §14 vs AGENTS 别两边都缺 | **权威口令只写在 skill-governance §14**（点名两份规则）。AGENTS.md **只引用 §14**，不另编一套 |
| examples/README mermaid | 第二图改为：先出方案 → 可直接执行或另开对话 B 审 → 人同意 |
| 本包 SKILL.md 缺口路由 | **不加**本包缺口路由（本包不是记缺口引擎）。用法句含 24。目标仓只改 `SKILL.md.tmpl` |

本周期三个可验证目标（用户要求同周期交付）：

1. **收编**：无规范的已有技能仓，一次补上与空仓初始化同一套结构，正文保留。
2. **升级双路径**：A 出方案；B 审核 **或** 人直接执行。协议在目标仓 `governance/`，不进分发包。参考 ChronoPM 16 号**能力**，不拷全文。
3. **技能缺口 / 升级需求文档**：初始化（及收编）时写入捕捉规则与模板。用技能的人说「做不到 / 记成升级需求」就落下一份需求稿，供以后 A 写 AP 用。参考 ChronoPM `skill-gap-skill` 的**能力**，不拷 `ai/`、REQ、P-OUTPUT。

相对 1.2：新增目标 3。相对 1.3：B1 P1～P3 与文档指针。收编钉死点与双路径口径保留。

## AP-1. 变更概述

### 目标 1 · 收编（1.1 已审，口径不变）

空仓初始化之外增加「收编已有技能」。有 `SKILL.md`、无本包指纹时：先读后补，不改正文。指纹 = `governance/rules/skill-governance.md`。本包用完即走。

### 目标 2 · 升级双路径（本版新加）

现状：目标仓只有「写七章 AP → 人同意执行」。没有 A/B；示例也不教审核。ChronoPM 开发仓则强制 A 出方案、B 独立审、人中转；人也必须最终点头。

本版让**凡经本包初始化或收编的仓**都带上精简双路径：

| 路径 | 谁开口 | 做什么 | 何时才能改技能正文 |
|---|---|---|---|
| **H · 人直接执行** | 「同意执行」「执行升级」 | 跳过 B | 人这四个字之后 |
| **B · 审核后再执行** | 「你是 Agent B，审核 upgrade-plan-vX.md」 | B 只在 AP **文末追加** `## B1 审核结果`，不改 A 正文 | 仍须人再说「同意执行」 |

A 只出方案、不执行。B 只审核、不执行。人始终有最终执行权：即使 B 不是「通过-可执行」，人仍可同意执行，CR 须写明「人覆盖 B」。

本包（skill-devkit）自己仍然**不是**升级引擎：对着本包说「你是 Agent A / 写 AP / 升级」继续停止，指到那个技能文件夹。A/B 只在目标仓的 `governance/rules/` 里生效。

### 目标 3 · 技能缺口文档（本版新加）

ChronoPM：技能做不到时**先写后告知**，产出 `需求-{短标题}.md`，不是项目需求，同痛点原位更新，不写完整 AP。改 Skill 仍走 A/B。

本包初始化写出的仓同样带上这套（精简、与业务项目解绑）：

- 触发：「这是 skill 的问题」「记成升级需求」「当前技能做不到……」
- 先写后告知，不问「要不要记」
- 文件在**当前工作区** `outputs/skill-gaps/`（不用 ChronoPM 的 `ai/outputs/`）
- 同指纹原位更新；已并入某版则标废弃
- **禁止**把缺口文当成 AP；**禁止**因此改 `SKILL.md`
- 以后升级时 A **可读**这些文件当需求输入

规则与模板进**目标仓分发包**（用的人要能记缺口）。A/B 协议仍只在 `governance/`，不进包。

### 文档

08 双路径总教程；21/22/23 人执行 / B 审核 / 同对话转 B；**24 记升级需求**。README / 开口表同步。

## AP-2. 影响点详细分析

| 影响项 | 当前状态 | 变更后状态 | 影响描述 | 影响程度 | 是否可逆 |
|---|---|---|---|---|---|
| 本包身份 | 只初始化空仓 | 空仓初始化 **或** 收编；升级仍不接管 | 见 1.1 | 高 | 回退 0.6.4 |
| 收编 | 无 | 见 1.1 全文 | 不变 | 高 | 是 |
| 目标仓升级角色 | 单助手：七章 → 同意执行 | **A 出方案**；**B 审核（可选）**；**人执行（必经）** | 种子新协议文件 + 改 `skill-governance.md` / `AGENTS.md` / AP 模板文末 | 高（目标仓契约） | 是 |
| 人跳过 B | 本来就是人直接同意 | 保留并写明为正式路径 H | 不得改成「必须先 B」 | 高 | 是 |
| B 落盘 | 无 | 只追加 `## B{N} 审核结果`；禁止改 A 正文与其他 B 节 | 与 ChronoPM 同机制、章节更短 | 中 | 是 |
| 同对话 A→B | 无限制 | **拒绝**。须新对话或人明确把 AP 路径交给 B | 防 A 审自己 | 中 | 是 |
| 工作区确认 | 无 | A 写 AP 前必须展示路径 / `VERSION` / git 并等人确认 | 防读错目录；比 ChronoPM 瘦：一张表即可 | 中 | 是 |
| 本包路由 | 「Agent A / 写 AP」→ 停 | 仍停，结束语改为：到技能文件夹走 A/B 或人执行 | 本包不加载双角色协议 | 中 | 是 |
| 分发包 | governance 已排除 | 协议在 `governance/rules/`，**不进**目标仓 zip（与 ChronoPM 16 号相同） | 终端用户不可见 | 低 | 是 |
| 示例 / README | 08 只教人同意 | 08 双路径总教程 + 21/22/23；README 开口表 | 使用者可见 | 中 | 是 |
| 空仓初始化问答 | 不念 A/B | 结束语加一句：以后改技能先出方案，你可直接同意，也可另开对话让 B 审 | 不把 ChronoPM 术语塞进初始化问答 | 低 | 是 |
| ChronoPM 16 号全文 | 不在本包 | **不拷贝**进种子 | 避免把项目管理升级协议灌进每个小技能 | 高（否决项） | — |
| 技能缺口捕捉 | 无 | 初始化写入 `references/gap-capture.md` + 模板；`SKILL.md` 增路由行 | 用的人可记升级需求；开发者 A 读这些稿 | 中 | 是 |
| 缺口落盘位置 | — | 工作区 `outputs/skill-gaps/` | **三脚本** `EXCLUDE_DIRS` 同步加 `outputs`（pack / snapshot_baseline / audit_release）。§13 白名单收 `outputs/` 为运行时生成物目录，不是「未登记的非法根文件」 | 中 | 是 |
| 缺口 vs AP | 无区分 | 缺口 ≠ 方案。记缺口不改技能；升级仍走 A 七章 | 防把需求稿直接当执行依据 | 高 | 是 |
| ChronoPM gap 全文 / `ai/` | 不在本包 | **不拷** P-OUTPUT、REQ、pm-decisions、schema 字段 | 通用技能没有项目 ai 目录 | 高（否决项） | — |

收编相关行（指纹、补缺、VERSION 只写一次、冲突硬闸、snapshot_baseline、dry-run≠基线、半套 governance）同 1.1，不重复展开。

## AP-3. 变更策略与设计思路

### 3.0 本包执行前固化

同 1.1：`VERSION=0.6.4`，commit `2e9db76`。落盘前 `git tag v0.6.4`（已有则跳过），不擅自 push。回滚：该 tag。

### 3.1～3.8 收编

同 1.1（两条流程不合并、先读后补、VERSION 只写一次、冲突硬闸、`snapshot_baseline.py` 目录名=采用版本、失败不留半套 `governance/`）。不改口径。

### 3.9 目标仓升级双路径（参考 ChronoPM，不拷全文）

**从 ChronoPM 16 号抽取、必须有的能力：**

1. 升级先写 AP，未确认不改 `SKILL.md` / `references/` / `skill.json`。
2. 角色分离：A 设计，B 独立审，人裁决执行。
3. B 只改自己的节，不改 A 正文。
4. 同一对话已以 A 出过方案，禁止直接转 B。
5. 缺规定节 = 本轮失败。
6. 写方案前确认工作区路径与版本。
7. 用户不必报目标版本；A 读 `VERSION` 拟定。
8. **人可以直接执行**（ChronoPM 里人仍是最终闸；本包把「跳过 B」写成一等路径，因大量小技能没有第二名审核员）。

**明确不拷：** 需求辩论 21 节骨架、#1.6 粘贴中转点强制、schema 锁步、四套输出骨架（修订/执行步进/终稿）、缺口技能、禁止用户提供外置提示词那套 ChronoPM 探测路径。

#### 3.9.1 文件落点（目标仓）

| 文件 | 作用 |
|---|---|
| `governance/rules/skill-governance.md` | 总流程：写 AP → **路径 H 或路径 B** → 人同意 → CR 起 |
| `governance/rules/upgrade-dual-agent.md` | **新种子**。A/B 命中时整份加载。分发包不含 |
| `governance/templates/upgrade-plan.md` | 七章不变；文末加 B 占位说明：审核只追加、禁止改上方 |
| `AGENTS.md` | 改本仓 / 写方案 / 你是 A 或 B 时读上述两份规则 |

本包 `assets/seed/` 与 `01-init.md` **§5 复制表**增加 `upgrade-dual-agent.md` → 目标 `governance/rules/upgrade-dual-agent.md`。**§4 目录树同步列出该文件**（不得只改复制表不改树）。收编补缺见 3.13。

#### 3.9.2 Agent A（出方案，不执行）

触发（目标仓内，白话或口令均可）：「升级这个 skill」「写一份升级方案」「你是 Agent A」「先出方案再改」。

A 必须：

1. **工作区确认**：展示根路径、`VERSION`、git HEAD（无 git 则写无）。等人回复确认后再扫描写盘。路径不对则重定位。
2. 扫描 `SKILL.md`、`references/`、`VERSION`、`skill.json`、现有 `governance/planning/`。
3. 把方案写到唯一文件 `governance/planning/upgrade-plan-v{拟定版本}.md`。七章缺一 = 失败，不得请人同意。
4. 文首可加短前置（工作区快照、需求照抄、已扫文件），**不得替代七章**。
5. 写完停止，同时给出两条路，禁止自己改技能正文：

> 方案在 `governance/planning/upgrade-plan-vX.md`。  
> - 直接做：回复「同意执行」或「执行升级」。  
> - 先审核：新开对话（或换一个助手）说「你是 Agent B，审核 governance/planning/upgrade-plan-vX.md」。

#### 3.9.3 路径 H · 人直接执行

人说「同意执行」「执行升级」「按这个执行」（同意该 AP）。  
**不要求**已有 B 节。进入 `skill-governance.md` §2 从建 CR 起。CR 写：`执行授权: 人直接同意（未经 B）`。

#### 3.9.4 路径 B · 审核后再等人

触发：「你是 Agent B / B1 / B2」「审核这份升级方案」「审核 upgrade-plan-vX.md」。

B 必须：

1. 先核对工作区与 A 快照是否同一仓、同一 `VERSION`/git；不一致则停止，不写审核节。
2. **独立实读** AP-4 列出的文件，禁止只读 AP。
3. **只在该 AP 文末追加** `## B{N} 审核结果`（未编号默认 B1）。禁止改 A 正文、禁止改其他 B 节、禁止删节。
4. 不得执行、不得建 CR、不得改 `SKILL.md`。
5. 审核节缺下列任一小节 = 失败：

| 小节 | 内容 |
|---|---|
| #0 | 工作空间核对（路径、VERSION、git、是否与 A 一致、人是否确认过） |
| #1 | 实读文件清单 |
| #2 | 七章是否齐全；AP-4 与实仓是否对得上 |
| #3 | 阻塞问题（无则写「无」） |
| #4 | 四档结语之一：通过-可执行 / 通过-待修订 / 修订-需再审 / 重做-需再审 |

四档含义与 ChronoPM 相同：可执行；仅非阻塞建议；有阻塞须再审；方向错须重做。

B 写完后告诉人：若结语是「通过-可执行」或「通过-待修订」，回复「同意执行」才会改技能；若是后两档，应让 A 修订后再审——**除非人明确覆盖**。

#### 3.9.5 人覆盖 B

B 已写「修订-需再审」或「重做-需再审」，人仍说「同意执行」：执行，CR 写 `执行授权: 人覆盖 B（B 结语=…）`。A/B 不得拦人。

#### 3.9.6 硬闸

1. 同一对话已经以 A 身份出过该 AP → 本对话禁止转 B。请人新开对话把路径交给 B。
2. 没有 AP 文件 → B 停止，请先让 A 写。
3. A 在人同意前改技能正文 = 失败。
4. B 改了 A 正文 = 失败，须从 git 恢复 AP 后重审。
5. 对着 skill-devkit 本包说 A/B = 停止（现路由保留，结束语指向目标仓协议文件）。

#### 3.9.7 与「必须先出 AP-1～AP-4」的对齐

`skill-governance.md` §1 现写「必须先写出 AP-1～AP-4」。改为：**七章都要有**才可请人同意（与 §3「缺一不可」一致）。路径 H 与路径 B 都看这份文件。

#### 3.9.8 发版后删 AP 与 B 节（B1 P3）

`skill-governance.md` §2 第 11 步现为「删除该版本 AP（已固化到 CR / CHANGELOG / 基线 / upgrade-to）」。改为明确：

> 删除该版本 AP（含文末 B 审核节；内容已固化到 CR / CHANGELOG / 基线 / upgrade-to，**不另存** B 副本）

`audit_release.py`「已发布版本不得残留 AP」语义不变：B 节随该文件消失是预期，不是丢失审核记录。

#### 3.9.9 口令只在一处写全（B1：别两边都缺）

- **权威**：`skill-governance.md` §14 改成两行：先方案；写 AP / 你是 A 或 B 时**同时读** `skill-governance.md` 与 `upgrade-dual-agent.md`；人「同意执行」或「执行升级」才改技能。
- **AGENTS.md**：只写「遵守 `governance/rules/skill-governance.md` §14」，不重复编一套触发词。
- `rules-README.md`：表里列出 `upgrade-dual-agent.md`（索引，不是第二套口令）。

### 3.10 示例与 README（本周期必须同步）

不是事后补文档。执行 AP-4 时与种子、规则同一轮改。

| 文档 | 改什么 |
|---|---|
| `examples/08` | 总教程：A 写到哪、七章、**两条路**、B 节长什么样、人覆盖 |
| `examples/21` | 新：A 出方案后人口头「执行升级」（路径 H 全过程） |
| `examples/22` | 新：另开对话 B 审核，追加 B1 节，人再同意 |
| `examples/23` | 新：同一对话从 A 转 B 会停 |
| `examples/10` `11` | 点明：写规则/直接改仍是 A 出七章；之后可 H 或 B |
| `examples/09` | 对本包说 A/B 同样停 |
| `examples/README.md` | 表增加 21～24；08 说明改为双路径；**第二张 mermaid 改为：先出方案 → 可直接执行或另开对话 B 审 → 人同意** |
| `README.md` | 开口表增加 A/B/执行升级、记成升级需求；能力表增加双路径与缺口文档 |
| `examples/24` | 新：技能做不到 → 缺口稿路径、不问要不要记 |
| `references/01-init.md` §7 结束语 | 白话加：以后改技能先出方案；可直接同意或让 B 审；做不到可先记升级需求 |
| 本包 `SKILL.md` | 「用法见 examples/」含 08、21～**24**；Agent A 行仍停。**不加**「技能做不到 → gap-capture」路由（那是目标仓 tmpl 的行；本包不是记缺口引擎） |

初始化 01～07 对话仍少念术语；升级示例必须把路径和角色讲清楚（延续 0.6.4 对 08 的要求）。

### 3.11 被否决的替代（本目标）

| 方案 | 否决原因 |
|---|---|
| 把 ChronoPM `16-upgrade-dual-agent.md` 原文拷进每个仓 | 绑定项目管理、21 节过重，小技能用不了 |
| 强制必须先 B 才能执行 | 用户明确要求人可直接执行 |
| 取消人直接执行，只留 B | 同上 |
| 本包常驻当 A/B 引擎 | 与「用完即走」冲突；协议在目标仓 |
| 允许同对话 A 转 B | A 审自己，审核作废 |
| B 可以改 AP 正文「顺手修好」 | 与 ChronoPM 铁律相反，责任分不清 |

收编否决表见 1.1 §3.8，仍有效。

### 3.12 技能缺口 / 升级需求文档（写入初始化）

**从 ChronoPM skill-gap 抽取、必须有的能力：**

1. 用户明示「技能做不到 / 记成升级需求 / 这是 skill 的问题」→ **先写后告知**，不问要不要记。
2. 同一痛点（指纹=涉及文件路径 + 关键词）→ 原位更新，不另开 `rev-001`。
3. 当前 Skill 已包含该能力 → 旧稿标废弃（写并入版本），不新建。
4. 用户说「不要记」→ 该份标取消。
5. 告知必须含：路径 + 本次记了什么 + 历史是否在文中。
6. 正文对照模板缺节不得落盘。建议补丁节**禁止**写成完整 AP。
7. 改 Skill 仍走目标仓 A/B（或人同意执行），不因记了一份缺口就改 `SKILL.md`。

**不拷：** `ai/outputs`、`outputs/index.md` 的 ChronoPM 批次过程、项目 REQ/WP、`pm-decisions`、workspace schema 两行、P-ALWAYS 第 4 步自动检测（本包不做静默两次硬拒绝就落盘，避免小技能误记；只认明示触发）。

#### 3.12.1 种子落点（初始化 / 收编补缺）

| 源（本包） | 目标仓 | 进目标 zip |
|---|---|---|
| `assets/seed/gap-capture.md` | `references/gap-capture.md` | 是 |
| `assets/templates/skill-gap-demand.md` | `assets/templates/skill-gap-demand.md` | 是（pack 已含 `assets/`） |
| `SKILL.md.tmpl` 路由加一行 | `SKILL.md` 路由 | 是 |

`SKILL.md.tmpl` 路由增加：

| 用户信号 | 加载 |
|---|---|
| 技能做不到 / 记成升级需求 / 这是 skill 的问题 / 技能缺口 | `references/gap-capture.md` |

**01-init.md §4 目录树**须与 §5 复制表同时改，至少增出（初始化当时就落盘，不是懒建）：

```
├── references/
│   ├── README.md
│   └── gap-capture.md
├── assets/
│   ├── .gitkeep
│   └── templates/
│       └── skill-gap-demand.md      # 来自本包 assets/templates/
├── governance/
│   └── rules/
│       ├── skill-governance.md
│       └── upgrade-dual-agent.md
```

`outputs/` **不出现在 §4 树**（懒建）。`governance/templates/` 仍含 upgrade-plan 等；缺口模板在目标仓 **`assets/templates/`**（进 zip），不要放到 `governance/templates/`（不进 zip）——用的人装上包才能记缺口。

收编补缺见 3.13，禁止只按 1.1 补缺表执行。

#### 3.12.2 工作区产出

当前工作区（技能所服务的目录，不是必须是开发仓）：

```
outputs/skill-gaps/SG-YYYYMMDD-NNN-需求-{短标题}.md
```

- 建 `outputs/skill-gaps/` 为懒建。
- **三脚本同步**（B1 P1）：`assets/seed/pack.py`、`snapshot_baseline.py`、`audit_release.py` 的 `EXCLUDE_DIRS` / `EXCLUDE_FILES` / `EXCLUDE_EXTS` **保持同一套**，本版均增加 `outputs`。只改 pack、不改另外两个 = 基线会吸入缺口稿、审计会把 `outputs` 当应打包内容。注释「Keep EXCLUDE_* in sync」继续有效。
- **根白名单**（B1 P2）：`skill-governance.md` §13 **加入 `outputs/`**。定性：运行时生成物目录（懒建），与 `tests/` 类似——允许存在；其下 `skill-gaps/*.md` **不**算「新的根文件须先写进 AP-4」。禁止在根上散落 `需求-*.md`。收编时若已有 `outputs/`，列入出生 CR 即可，不算来源不明而停（停的仍是来源不明的 `governance/`）。
- 01-init §4 树：初始化**不预写** `outputs/`（懒建）。§4 必须列出缺口模板与 dual-agent（见 3.12.1），与 §5 复制表一致。不是「禁止运行时出现清单外目录」；清单外仍禁止的是乱造业务 `ai/` 等。

#### 3.12.3 模板必选节（精简，不是 ChronoPM 〇～八全套）

1. 一句话痛点  
2. 元信息：`sg_id`、技能英文名、`VERSION`（只抄根 `VERSION` 或已装 skill.json，禁止猜）、日期、状态 draft/deprecated/cancelled  
3. 用户原话  
4. 期望 vs 实际  
5. 现状为何（可含 mermaid）  
6. 建议补丁（条目级，**不是** AP-1～AP-7）  
7. 迭代记录  

缺节 = 不落盘。同指纹更新时重写 1～6、追加 7。

#### 3.12.4 与 A 的衔接

A 出升级方案前：若 `outputs/skill-gaps/` 有 `status=draft` 的稿，**必须读**并在 AP-1 引用 `sg_id`。缺口稿不是执行许可。没有缺口稿时，人口头需求仍可出 AP（不强制先记缺口）。

#### 3.12.5 否决

| 方案 | 否决原因 |
|---|---|
| 拷 ChronoPM `skill-gap-skill/` 整目录 | 绑 `ai/`、REQ、P-OUTPUT |
| 记缺口时直接改 `SKILL.md` | 绕过 A/B |
| 缺口稿当 AP 执行 | 缺七章与同意执行 |
| 问「要不要记」 | 与 ChronoPM 先写后告知相反；用户已明示 |
| 两次硬拒绝自动落盘 | 小技能误伤；本包只认明示口令 |

### 3.13 收编补缺表（相对 1.1 必须增列，禁止只看 1.1）

`references/02-adopt.md` 的「已有则保留 / 没有则补」表在 1.1 骨架之外，**必须显式写入**下列行（无则写入，有则不覆盖）：

| 目标已有？ | 收编动作 |
|---|---|
| `governance/rules/upgrade-dual-agent.md` | 无则从种子拷入 |
| `references/gap-capture.md` | 无则从种子拷入 |
| `assets/templates/skill-gap-demand.md` | 无则从本包 `assets/templates/` 拷入（先建目录） |
| `SKILL.md` 路由表「技能做不到 / 记成升级需求」行 | **不覆盖**已有路由。无该行则在表末**只追加一行**，指向 `references/gap-capture.md` |
| `AGENTS.md` | 1.1 已有：无则写入；有则只在未指向 §14 时文首追加指针 |
| `skill-governance.md` | 收编时 `governance/` 必须本不存在才整棵创建（1.1 硬闸）。因此新仓技能-governance 用本版种子（已含 §13 `outputs/`、§2.11、§14）。**禁止**在已有来源不明 `governance/` 上补丁 |

漏装上述任一项 = 收编失败，须补拷后再打基线。

## AP-4. 修改范围清单

### 收编（同 1.1，执行时不得漏）

`SKILL.md`（用法句扩到 17～20、21～**24**；**不加**本包缺口路由）、`skill.json`、`VERSION`、`CHANGELOG.md`、`README.md`、`references/00-core.md`、`01-init.md`（**§4 树与 §5 表同步**，见 3.12.1）、新 `02-adopt.md`（**补缺表含 3.13 四类**，不得只抄 1.1）、`references/README.md`、`CR-000-adopt.tmpl`、`upgrade-to-adopt.tmpl`、`skill-governance.md`（出生证明 + **§13 含 outputs/** + §1/§2 双路径 + §2.11 B 随 AP 删）、示例 03/04/17～20、`tests/README.md`、`tests/adopt.md`。

### 双路径与文档（本版增）

| 文件 | 修改类型 | 修改内容摘要 | 是否核心契约 |
|---|---|---|---|
| `assets/seed/upgrade-dual-agent.md` | 新增 | A/B 协议全文（§3.9）：角色、路径 H/B、B 节五小节、硬闸、人覆盖。目标仓 `governance/rules/upgrade-dual-agent.md` | 是（目标仓规则） |
| `assets/seed/skill-governance.md` | 改 | §1 七章齐全才能请人同意；§2 步骤 2 为路径 H 或 B；§2 步骤 11 写明 B 节随 AP 删除并已固化；**§13 白名单加入 `outputs/`**（运行时生成物）；**§14 为唯一开口权威**（点名 `upgrade-dual-agent.md`） | 是（目标仓规则） |
| `assets/seed/AGENTS.md` | 改 | 只引用 skill-governance **§14**，不另写一套 A/B 口令 | 否 |
| `assets/seed/rules-README.md` | 改 | 表增加 `upgrade-dual-agent.md` | 否 |
| `assets/templates/upgrade-plan.md` | 改 | 文末：B 只追加 `## B{N} 审核结果`，禁止改上方 A 正文 | 否 |
| `SKILL.md` | 改 | Agent A/B 行仍停止；用法见 examples 含 21～**24**；不加本包「技能做不到」路由 | 是 |
| `examples/08-初始化之后怎么升级.md` | 改 | 双路径总教程（七章 + 路径 H/B + B 节样例 + 人覆盖） | 否 |
| `examples/21-初始化之后A出方案人直接执行.md` | 新增 | 路径 H 对话 | 否 |
| `examples/22-初始化之后B审核再执行.md` | 新增 | 路径 B 对话，含 B1 节最小样例 | 否 |
| `examples/23-同一对话从A转B会停.md` | 新增 | 硬闸 | 否 |
| `examples/09` `10` `11` | 改 | 链到 21/22 | 否 |
| `examples/README.md` | 改 | 08 说明；增加 21～24；第二张 mermaid 改为双路径 | 否 |
| `README.md` | 改 | 能力表双路径 + 缺口；开口表 A/B/执行升级/记升级需求 | 否 |
| `tests/upgrade-roles.md` | 新增 | H 可跳过 B；B 不改 A；同对话转 B 失败；无 AP 时 B 停止 | 否 |
| `assets/seed/gap-capture.md` | 新增 | 缺口捕捉规则（明示触发、先写后告知、原位、废弃、禁当 AP） | 是（目标仓规则，进 zip） |
| `assets/templates/skill-gap-demand.md` | 新增 | 缺口文七节模板 | 否 |
| `assets/seed/SKILL.md.tmpl` | 改 | 路由表增加技能缺口行 | 是 |
| `assets/seed/pack.py` | 改 | `EXCLUDE_DIRS` 增加 `outputs`（与下列两脚本同一套） | 否（脚本） |
| `assets/seed/snapshot_baseline.py` | 改 | **同一套** `EXCLUDE_*`，增加 `outputs`（B1 P1） | 否（脚本） |
| `assets/seed/audit_release.py` | 改 | **同一套** `EXCLUDE_*`，增加 `outputs`（B1 P1） | 否（脚本） |
| `references/01-init.md` | 改 | **§4 目录树与 §5 复制表同步**：列出 `gap-capture.md`、`assets/templates/skill-gap-demand.md`、`upgrade-dual-agent.md`；不预写 `outputs/`；§7 结束语加双路径与记缺口 | 是（规则） |
| `references/02-adopt.md` | 新增 | 收编全文；补缺表**必须含 3.13**（dual-agent / gap-capture / 缺口模板 / SKILL 路由追加），禁止只实现 1.1 表 | 是（规则） |
| `examples/24-初始化之后记升级需求.md` | 新增 | 「技能做不到，记成升级需求」对话；路径、不问要不要记、不改正文 | 否 |
| `tests/gap-capture.md` | 新增 | 明示落盘；不问要不要记；同指纹原位；已有能力则废弃；不改 SKILL.md | 否 |

## AP-5. 回归测试计划

收编 P1/P2、N1～N7、R1～R3 同 1.1（R1 对照 **0.6.4**）。

| 编号 | 类型 | 输入 | 期望 |
|---|---|---|---|
| U1 | 正 H | 目标仓说「升级…」，确认工作区后写出七章 AP；人说「执行升级」 | 无 B 节也能建 CR 并改 AP-4 文件；CR 标明未经 B |
| U2 | 正 B | 新对话「你是 Agent B，审核 upgrade-plan-vX.md」 | 只在文末追加 B1；A 正文 hash 不变；不改 `SKILL.md`；人再「同意执行」才改 |
| U3 | 正 | B 结语「修订-需再审」后人口头「同意执行」 | 执行；CR 写人覆盖 B |
| N8 | 反 | 同一对话 A 出方案后立刻「你是 Agent B」 | 停止，不写 B 节 |
| N9 | 反 | 无 AP 文件说「你是 Agent B」 | 停止 |
| N10 | 反 | 对着 skill-devkit 本包说「你是 Agent A」 | 停止，不写本包 planning |
| R4 | 旧 | 空仓初始化 | 与 0.6.4 相同问答；结束语可多一句双路径，问项不增 |
| R5 | 旧 | 错别字直改 | 仍不走 AP（14） |
| G1 | 正 | 已初始化仓说「这是 skill 的问题，记成升级需求：……」 | 写出 `outputs/skill-gaps/SG-*-需求-*.md`；告知路径+记了什么；**不改** `SKILL.md`；不问要不要记 |
| G2 | 正 | 同一痛点再补一句 | 原位更新同一文件，迭代记录多一行，不新建号 |
| G3 | 正 | 当前版本已包含该能力后再记 | 旧稿 deprecated，不新建 |
| N11 | 反 | 记缺口后助手直接改 `SKILL.md` | 禁止；须另走 A |
| N12 | 反 | 无明示口令的普通不满 | 不落缺口文 |
| X1 | 正 | 三脚本 `EXCLUDE_DIRS` | 三者相等，且都含 `outputs`、`governance`、`tests` |
| X2 | 正 | 目标仓先放一份 `outputs/skill-gaps/SG-测试-需求-x.md`，再跑 `snapshot_baseline.py`、`audit_release.py`、`pack.py --dry-run` | **`audit_release.py` 退出码必须为 0**（有 `outputs/` 不得失败）；基线目录与 dry-run 打印路径均**不含** `outputs/`；zip 预览无缺口稿 |

## AP-6. 风险评估与回滚方案

1.1 收编风险表保留。新增：

| 风险 | 级别 | 缓解 | 回滚 |
|---|---|---|---|
| 做成「必须先 B」 | 高 | 路径 H 写进 skill-governance §2 与 08/21；U1 必测 | 回退 0.6.4 |
| A 审自己（同对话转 B） | 中 | N8 硬闸 | 删误写的 B 节 |
| B 改 A 正文 | 高 | 协议写死只追加；U2 查 hash | git 恢复 AP |
| 把 16 号全文灌进小技能 | 高 | 3.11 否决；种子自写短协议 | 不采用该文件 |
| 人覆盖坏方案 | 中 | CR 留痕；不拦人 | 基线回滚 |
| 本包误当 A 执行 | 中 | N10；本包路由仍停 | 不写盘 |
| 记缺口直接改技能 | 高 | G1/N11；规则写死缺口≠AP | 回退该次对 SKILL.md 的提交 |
| 缺口稿打进安装包或基线 | 高 | **三脚本**同步排除 `outputs/`；X1/X2 | 回退脚本 |
| `outputs/` 被 §13 判非法 | 中 | 白名单写入 `outputs/` 并定性为运行时生成物 | 改 §13 |
| 拷 ChronoPM gap 绑 ai/ | 高 | 3.12.5 否决 | 不用该目录 |

本包发布失败：保留 `v0.6.4`。目标仓收编/误升级：回退该次 commit，禁止半套 `governance/` 打补丁。

## AP-7. 版本影响

| 维度 | 变更前 | 变更后 |
|---|---|---|
| Skill Version | 0.6.4 | 0.7.0（Minor，三能力：收编 + 双路径 + 缺口文档） |
| 本包对照 | `2e9db76`，执行前补 `v0.6.4` | 本包无 `governance/baselines/` |
| 工作区迁移 | 否 | 否。已初始化仓**没有**自动长出 dual-agent 文件；要双路径须再收编或手拷种子（**不**在收编范围外改已规范仓）。新 init/新收编的仓自带 |
| 已规范旧仓 | 仅七章+人同意 | 行为仍可用路径 H（现有流程）。没有 `upgrade-dual-agent.md` 时：有 `skill-governance.md` 仍按七章+同意执行；B 口令若文件缺失则说明「本仓是旧种子，可复制该文件或继续直接同意执行」 |
| 本包分发包 | examples 16 篇 | examples 含 17～24；`references/02-adopt.md` 进本包 zip |
| 目标仓分发包 | 无缺口规则 | `references/gap-capture.md` 与缺口模板**进** zip；`governance/`（含 A/B）仍不进；`outputs/` 不进 |
| schema | 无 | 无 |

已用本包初始化、尚未放 dual-agent 文件的仓：不强制迁移。路径 H 与现在一致。要走 B：把新种子 `upgrade-dual-agent.md` 拷进 `governance/rules/`（可在该仓自己的下一轮升级里做，不在本包 0.7.0 对用户仓写盘）。

---

请审查以上方案（**1.5**，B2 三条已写入执行清单）。B 结语为通过-待修订，无需再审。确认后回复「同意执行」。  
执行第一步：`git tag v0.6.4`（0.6.3 不补 tag，除非你另说），再按 AP-4 落盘。

---

## B2 审核结果

### #0 工作空间核对

| 项 | 值 | 与 A 声明是否一致 |
|---|---|---|
| 根路径 | `c:\Users\qiusuo\Downloads\skill-devkit` | 一致 |
| `VERSION` | `0.6.4` | 一致 |
| git HEAD | `2e9db76` | 一致 |
| git tag | 仅 `v0.6.2`（0.6.3 / 0.6.4 未打 tag） | 与「执行前补 `v0.6.4`」一致 |
| 未跟踪文件 | 仅 `governance/planning/upgrade-plan-v0.7.0.md` | 一致（本 AP 未写盘） |

### #1 实读文件清单

本 B 节在 1.3 已实读全部相关文件（`SKILL.md`、`skill.json`、`VERSION`、`CHANGELOG.md`、`references/00-core.md`、`01-init.md`、`references/README.md`、种子 `skill-governance.md` / `AGENTS.md` / `SKILL.md.tmpl` / `skill.json.tmpl` / `pack.py` / `snapshot_baseline.py` / `audit_release.py`、`assets/templates/upgrade-plan.md`、示例 03 / 04 / README、`CR-000-init.tmpl`、`upgrade-to-0.1.0.tmpl`）。本轮对照 1.4 新增内容重读了 `pack.py`、`snapshot_baseline.py`、`audit_release.py`、`rules-README.md`、`01-init.md` §4/§5。

### #2 七章与 AP-4 核对

七章齐全。核对 1.4 对 B1 的吸收：

| B1 意见 | 1.4 落点 | 判定 |
|---|---|---|
| P1 三脚本同步加 `outputs` | AP-4 三行（pack / snapshot / audit）并列同一套；3.12.2 写明只改 pack 的后果 | ✅ 吸收 |
| P2 `outputs/` 白名单身份 | §13 加入 `outputs/`，定性运行时生成物懒建；3.12.2 与 AP-4 skill-governance 行 | ✅ 吸收 |
| P3 B 节随 AP 删除 | 新 3.9.8；§2 第 11 步写明不另存 B 副本 | ✅ 吸收 |
| §14 vs AGENTS | 3.9.9：权威只写 skill-governance §14；AGENTS 只引用；rules-README 只做索引 | ✅ 吸收 |
| examples/README mermaid | 3.10 行已列第二张 mermaid 改双路径 | ✅ 吸收 |
| 本包 SKILL.md 缺口路由 | 明确「不加」；用法句含 24 | ✅ 吸收 |
| 回归补 X1（三脚本一致）/ X2（含缺口稿时排除） | AP-5 已增 X1 / X2 | ✅ 吸收 |

### #3 阻塞问题

**无。** 本轮重读未发现新的高等级阻塞。

非阻塞建议（不要求再审，执行时顺手处理即可）：

1. **目标仓 `assets/templates/` 目录需进 01-init §4 树**：3.12.1 把缺口模板落到目标仓 `assets/templates/skill-gap-demand.md`，但 1.4 只写了「01-init 复制表增加缺口模板」，未同步更新 `01-init.md` §4 的目标仓目录树（现树里 `assets/` 只有 `.gitkeep`）。执行时请在 §4 树与 §5 复制表**同时**补 `assets/templates/skill-gap-demand.md`，并确认收编补缺也建该目录。

2. **收编补缺表需显式含新种子**：AP-4 收编段写「同 1.1」，但 1.1 的 `02-adopt.md` 补缺表不含 `upgrade-dual-agent.md`、`gap-capture.md`、缺口模板与 SKILL.md 路由追加行。3.9.1 / 3.12.1 已有文字声明「收编补缺：无则写入，有则不覆盖」，执行 `02-adopt.md` 时务必把这四类也列入补缺表，避免只看 1.1 而漏装。

3. **`audit_release.py` 的打包泄漏检查注释**：加了 `outputs` 后，`audit_release.py` 只查 governance/.git/AGENTS 泄漏；建议执行 X2 时顺带确认有 `outputs/` 时审计仍通过（方案已写，仅提示不要漏跑）。

### #4 结语

**通过-待修订**（仅 3 条非阻塞建议，无阻塞问题）。你回复「同意执行」即可进入执行；B1 的 P1～P3 已全部吸收，本次修订有效。若采纳上述建议，由执行轮直接落实，无需再审。

---

## B3 审核结果

### #0 工作空间核对

| 项 | 值 | 与 A 声明是否一致 |
|---|---|---|
| 根路径 | `c:\Users\qiusuo\Downloads\skill-devkit` | 一致 |
| `VERSION` | `0.6.4` | 一致 |
| git HEAD | `2e9db76` | 一致 |
| git tag | 仅 `v0.6.2`；0.6.3 / 0.6.4 均未打 tag | 与「只补 `v0.6.4`、0.6.3 不补」一致 |
| 未跟踪文件 | 仅 `governance/planning/upgrade-plan-v0.7.0.md` | 一致（本 AP 未写盘） |
| `B2 审核结果` 是否被改动 | 保留在文末，未删除 | 与「不改已有 B 节」一致 |

### #1 实读文件清单

本轮独立核验：`upgrade-plan-v0.7.0.md`（1.5 全文，含 B1 P1～P3 钉死表、3.9.8、3.9.9、3.12.1、3.12.2、3.13、AP-4、AP-5 X1/X2、AP-7）；对照实仓读取 `pack.py` / `snapshot_baseline.py` / `audit_release.py` 的 `EXCLUDE_*`（三份逐行一致，均在 `assets/seed/`）；via git 命令复核 `HEAD`、`VERSION`、tag、工作区状态。之前轮次已实读：`SKILL.md`、`skill.json`、`CHANGELOG.md`、`references/00-core.md`、`01-init.md`（§4/§5）、`references/README.md`、`assets/seed/skill-governance.md` / `AGENTS.md` / `SKILL.md.tmpl` / `skill.json.tmpl` / `rules-README.md` / `CR-000-init.tmpl` / `upgrade-to-0.1.0.tmpl`、`assets/templates/upgrade-plan.md`、`examples/README.md`、`examples/03`、`examples/04`。

### #2 七章与 AP-4 核对

七章齐全。核对 1.5 对 B2 三条的吸收：

| B2 建议 | 1.5 落点 | 判定 |
|---|---|---|
| 01-init §4 树与 §5 复制表同步补缺口模板 | 新增 3.12.1 目录树（`references/gap-capture.md`、`assets/templates/skill-gap-demand.md`、`governance/rules/upgrade-dual-agent.md`），明确 `outputs/` 不出现在树（懒建）；AP-4 增 `references/01-init.md` 行与「§4 树与 §5 表同步」 | ✅ 吸收 |
| 02-adopt 补缺表显式含新种子 | 新增 3.13 补缺表：dual-agent / gap-capture / 缺口模板 / SKILL 路由追加 / AGENTS / skill-governance 六行；AP-4 增 `references/02-adopt.md` 行；3.13 末「漏装任一项 = 收编失败」 | ✅ 吸收 |
| X2 有 `outputs/` 审计仍通过 | AP-5 X2 写死：`audit_release.py` 退出码 0、基线与 dry-run 路径不含 `outputs/`、zip 预览无缺口稿 | ✅ 吸收 |

并复核 B1 口径仍有效（P1 三脚本同步 + X1；P2 §13 含 `outputs/`；P3 §2.11 B 随 AP 删；§14 唯一权威；mermaid 改双路径；本包 SKILL.md 不加缺口路由）。三脚本当前 `EXCLUDE_DIRS` 实测一致（均无 `outputs`，待执行时同步加），与方案「追加 outputs」的现状描述吻合。

### #3 阻塞问题

**无。** 未发现新的阻塞问题。

非阻塞提示（执行轮注意事项，不要求再审）：

1. 3.13 要求 `02-adopt.md` 的 `references/gap-capture.md` 等补缺「从种子拷入」，执行时注意 gap-capture 与缺口模板的**源**不同：`references/gap-capture.md` 来自 `assets/seed/gap-capture.md`，`assets/templates/skill-gap-demand.md` 来自本包 `assets/templates/skill-gap-demand.md`（不是 seed）。复制表已分别点明，按表执行即可。
2. 落盘轮务必同步改三脚本 `EXCLUDE_*`（当前三份都尚未含 `outputs`），并跑 X1/X2 验证；X1 断言「三者相等且含 outputs」与现状「三者相等但不含 outputs」不冲突——X1 是执行后的验收，不是现状断言。
3. 1.5 文首「相对 1.4」表末括注「无需再审」与 B3 本轮仍在审不矛盾：那是 A 对 B2 三条的表述；B3 照常独立复核后给出结语，供人决策。

### #4 结语

**通过-可执行**。B2 三条已被 1.5 如实落盘，B1 P1～P3 口径未回退，无阻塞问题。可以按 3.0 先补 `git tag v0.6.4`，再按 AP-4 落盘（收编 + 双路径 + 缺口文档 + 示例/README 同一轮，三脚本 EXCLUDE 同步加 `outputs`，跑 X1/X2）。人回复「同意执行」即可进入执行。
