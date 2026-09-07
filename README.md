# Skill 开发工具包（skill-devkit）

**空仓一次初始化，或收编已有无规范技能：版本控制、冻结基线、升级记录、变更门禁、触发词、一键打包、发布审计（含结构校验）。问完即落盘，本包退场。**

> Empty-folder initializer, or one-time adopt of an existing ungoverned skill. One conversation writes a self-releasing skill repo, then this kit exits.

给 Skill 作者。装进助手，工作区指到空文件夹，说「初始化 skill」。一次对话写入：

- **版本控制** — 根目录 `VERSION` + git，可同步到 `skill.json`
- **冻结基线** — `governance/baselines/{版本}/`，只增不改
- **升级记录** — CHANGELOG、出生 CR、`upgrade-to`、以后的 git tag
- **变更门禁** — 先方案后改文件，提示词留在仓里
- **触发词** — 写进 `SKILL.md` description，助手才唤得起
- **一键打包 / 发布审计** — zip 不含治理目录；版本不一致、说明缺项、引用断裂不准发

**写完本包就退场。** 之后升版本、打基线、打 zip，走这个文件夹自己的文件，不再经过本包。

## 和一篇 SKILL.md 脚手架差在哪

| | 普通「创建 Skill」 | 本包初始化 |
|---|---|---|
| 留下什么 | 一篇 `SKILL.md`，偶尔再加 scripts | 完整开发仓 |
| 版本 | 往往写死在文件里 | 根目录 `VERSION` 单一来源，可同步 |
| 基线 | 无 | 每版一份冻结快照，只增不改 |
| 升级 | 靠聊天记忆 | A 出 AP → 人执行或 B 审后再执行 → CR → 记录 → tag |
| 发包 | 手搓 zip | 一键打包，治理目录不进包 |
| 本包还管不管 | 常常一直赖在对话里 | **不管了** |

不是业务项目管理，不是万能工具箱。ChronoPM 的变更治理是种子里借鉴的流程，不是本仓的一部分。

## 仓库

- GitHub：[qiusuo0226/skill-devkit-skill](https://github.com/qiusuo0226/skill-devkit-skill)
- Gitee：[qiusuo0226/skill-devkit-skill](https://gitee.com/qiusuo0226/skill-devkit-skill)

## 安装

```bash
npx skills add qiusuo0226/skill-devkit-skill
```

或把本仓复制到助手的技能目录（探测见技能包内说明；Grok 常见为 `~/.grok/skills/skill-devkit/`。其他助手可设环境变量 `SKILL_DEVKIT_SKILLS_DIRS`）。装好后，工作区指到**空文件夹**，说「初始化 skill」。

[![skills.sh](https://skills.sh/b/qiusuo0226/skill-devkit-skill)](https://skills.sh/qiusuo0226/skill-devkit-skill)

## 它只做一件事

```mermaid
flowchart LR
    A["1 安装本包"] --> B["2 空文件夹或空仓"]
    B --> C["3 说：初始化 skill"]
    C --> D["4 问答 + 确认"]
    D --> E["5 写出开发仓"]
    E --> F["6 本包退场"]
```

普通非空目录：直接停止。已有 `SKILL.md` 但无规范：说「收编这个 skill」。已规范仓：本包停止，升级走那个仓自己的文件。

## 初始化后，开发仓自带这些能力

下列能力写进目标仓的**文件和提示词**（主要在 `governance/`）。之后由那个仓的 Agent 执行，不经过本包。

| 能力 | 落在哪 | 做什么 |
|---|---|---|
| **版本控制** | 根目录 `VERSION`（唯一可读源）、`skill.json`、git、`sync_version.py` | 先改 `VERSION`，再同步；git 在仓根 |
| **基线控制** | `governance/baselines/{版本}/`、`snapshot_baseline.py` | 每个发布版本一份分发包快照；只增不改 |
| **升级记录** | `CHANGELOG.md`、CR、`upgrade-to-{版本}.md`、git tag `v{版本}` | 每次发版可追溯；默认无工作区迁移 |
| **变更门禁** | `governance/rules/skill-governance.md`、`upgrade-dual-agent.md` | A 出七章 AP；人直接执行，或 B 只追加审核后再由人执行 |
| **技能缺口** | `references/gap-capture.md`、`outputs/skill-gaps/` | 明示「记成升级需求」先写后告知；不改正文；稿不进安装包 |
| **影响分析** | `governance/impact-analysis/` | 标契约层 / 规则层是否受影响 |
| **回归报告** | `tests/`、`governance/regression-reports/` | 正 / 反 / 旧能力各至少一条 |
| **打包发包** | `governance/pack/pack.py` | `{英文名}-Skill-v{版本}.zip`；不含治理目录 |
| **发布审计** | `audit_release.py`、发布核对清单 | 版本一致、有基线、包内无治理目录 |
| **结构校验** | `validate_skill.py`（audit 先跑） | frontmatter 必填、`references/` 引用存在、VERSION 与 skill.json 一致 |
| **升级方案** | `planning/upgrade-plan-v{版本}.md` | 每周期 1 个 AP；发布后删除 |
| **一键脚本** | `governance/dev.ps1` | `sync` / `snapshot` / `audit` / `validate` / `pack` / `release` |
| **仓骨架** | `SKILL.md`、`references/`、`LICENSE`、`README.md` | 可安装的 Skill 入口 |
| **触发词** | `SKILL.md` `description` | 向导收集开口说法，写入自动调用字段 |
| **出生证明** | `CR-000-init`、`upgrade-to-0.1.0.md` | 0.1.0 起记录连续，标明本版无业务能力 |

对已初始化的仓说：

```text
按 governance/rules/skill-governance.md 处理，不要直接改。先出 AP。
```

这些能力怎么开口（升级、写规则、改开口、打包、检查、错别字、回滚、试用），见 [examples/](examples/README.md)「初始化之后」。

## 看一段真实怎么问

对话示例（Skill 名和人名是假的，问法是真的）：

目录：[examples/](examples/README.md)（初始化、收编、初始化之后；升级见 08、21～23，缺口见 24）

建议先看 [01-初始化空文件夹.md](examples/01-初始化空文件夹.md)。写到一半看 [25](examples/25-初始化写到一半再开口.md)。老技能看 [17](examples/17-收编已有技能.md)。建好之后必看 [08](examples/08-初始化之后怎么升级.md)。人直接执行看 [21](examples/21-初始化之后A出方案人直接执行.md)，B 审核看 [22](examples/22-初始化之后B审核再执行.md)。

## 开口就能用

| 你说 | 它做 |
|---|---|
| 「初始化 skill」 | 问英文名、干什么、中文名、版权、别人怎么开口；你点头后写入文件夹 |
| 「开发一个 skill，英文名 meeting-notes，把纪要收成行动项」 | 已说的不问，只补缺的 |
| 「把这个文件夹初始化成 skill」（目录非空） | **停止**，请换空文件夹 |
| 「再初始化」（已经建过） | **停止**。在这个文件夹里直接说要改什么 |
| 「收编这个 skill」（已有 SKILL.md、无规范） | 读原文，只补骨架，不改正文 |
| （对本包）「升级这个 skill」/「你是 Agent A」 | **停止。** 工作区换成那个技能的文件夹 |
| （初始化之后）「升级这个 skill。给它加一个能力：……」 | 先把七章方案写到 `governance/planning/upgrade-plan-v版本.md` |
| （初始化之后）「执行升级」 | 人直接同意，不经 B |
| （初始化之后）「你是 Agent B，审核 upgrade-plan-vX.md」 | 只在方案文末追加审核；仍须人同意才改技能 |
| （初始化之后）「这是 skill 的问题，记成升级需求」 | 写入 `outputs/skill-gaps/`，不改技能正文 |
| （初始化之后）「把版本升到 0.2.0，打一份安装包」 | 同上 |
| （初始化之后）「别人还可以说『提炼待办』」 | 同上：改开口说法 |
| （初始化之后）「说明里有个错别字，改一下」 | 同上：小改可直接做 |
| （初始化之后）「这版不行，回到上一版」 | 同上：回滚 |
| （初始化之后）「装到助手里试用」 | 同上：你开口才拷 |

同义口令：`开发一个 skill`、`新建技能`、`从零写 skill`、`脚手架`、`init skill`、`/init-skill`、`/new-skill`。

## 快速开始

1. 安装：`npx skills add qiusuo0226/skill-devkit-skill`，或把本仓复制到助手的技能目录（Grok 常见为 `~/.grok/skills/skill-devkit/`；可设 `SKILL_DEVKIT_SKILLS_DIRS`）。
2. 新建一个**空文件夹**（或空 git 仓），把助手工作区指到那里（不要指到本仓上）。
3. 说：「初始化 skill」。
4. 问完确认清单，说「按这个写」。
5. 之后只在那个新文件夹里开发。本包不再出现。

## 初始化会写出什么

```
{你的新文件夹}/
├── .git/
├── AGENTS.md             # 开发提示，不进 zip
├── SKILL.md
├── skill.json
├── VERSION               # 0.1.0
├── CHANGELOG.md
├── LICENSE
├── README.md
├── references/
├── tests/
└── governance/           # 不进分发包
    ├── rules/skill-governance.md
    ├── change-requests/CR-000-init.md
    ├── migrations/upgrade-to-0.1.0.md
    ├── baselines/0.1.0/
    ├── dev.ps1
    ├── pack/pack.py
    └── scripts/
```

完整树和提问顺序见 `references/01-init.md`。

## 本仓结构

```
skill-devkit/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/
├── assets/seed/
├── assets/templates/
├── examples/
├── governance/planning/
└── README.md
```

## 许可证

[MIT](LICENSE) © 2026 仇索

## 斜杠

`/skill-devkit` · `/skill-devkit init` · `/init-skill` · `/new-skill`
