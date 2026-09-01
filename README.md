# Skill 开发工具包（skill-devkit）

**在空文件夹或空 git 仓里，用一次，留下一套能自己管版本的 Skill 开发仓。**

给 Skill 作者用。装进 AI 助手 → 新建空文件夹并选为工作区 → 说「初始化 skill」。问完名字和用途、你点头之后，它写下 `SKILL.md`、git，以及完整的 `governance/`：版本控制、基线快照、升级记录、打包发包，还有之后任何助手都要读的治理提示词。

**写完本包就退场。** 那个仓以后的升版本、打基线、记升级、打 zip，都走它自己的文件和提示词，不再经过本包，本包也不再识别或控制它。这就是本包的用法：只用一次。

不是业务项目管理，不是万能工具箱。ChronoPM 的变更治理是种子里借鉴的流程，不是本仓的一部分。

## 仓库

Gitee：[qiusuo0226/skill-devkit-skill](https://gitee.com/qiusuo0226/skill-devkit-skill)

## 它只做一件事

```mermaid
flowchart LR
    A["1 安装本包"] --> B["2 空文件夹或空仓"]
    B --> C["3 说：初始化 skill"]
    C --> D["4 问答 + 确认"]
    D --> E["5 写出开发仓"]
    E --> F["6 本包退场"]
```

非空目录、已经有 `SKILL.md` 的仓：直接停止，不写盘。

## 初始化后，开发仓自带这些能力

下列能力写进目标仓的**文件和提示词**（主要在 `governance/`）。之后由那个仓的 Agent 执行，不经过本包。

| 能力 | 落在哪 | 做什么 |
|---|---|---|
| **版本控制** | 根目录 `VERSION`（唯一可读源）、`skill.json`、git、`governance/scripts/sync_version.py` | 先改 `VERSION`，再同步；git 在仓根，不在 `governance/` 里 |
| **基线控制** | `governance/baselines/{版本}/`、`snapshot_baseline.py` | 每个发布版本一份分发包快照；只增不改；回滚对照上一版 |
| **升级记录** | `CHANGELOG.md`、`change-requests/`、`migrations/upgrade-to-{版本}.md`、git tag `v{版本}` | 每次发版留下可追溯记录；默认无工作区迁移 |
| **变更门禁** | `governance/rules/skill-governance.md`、`AGENTS.md` | 先写 AP，人确认再改文件；即使用户说「直接改」也先出方案 |
| **影响分析** | `governance/impact-analysis/` | 准许执行后写 IA，标契约层 / 规则层是否受影响 |
| **回归报告** | `tests/`、`governance/regression-reports/` | 正 / 反 / 旧能力各至少一条，写入 RR |
| **打包发包** | `governance/pack/pack.py` | `{品牌}-Skill-v{版本}.zip`；不含 `governance/`、`.git/`、`AGENTS.md` |
| **发布审计** | `audit_release.py`、`review-checklists/release-checklist.md` | 版本三处一致、有基线、包内无治理目录；失败不准发 |
| **升级方案** | `governance/planning/upgrade-plan-v{版本}.md` | 每周期 1 个 AP；发布后删除（思路进 CR / CHANGELOG / 基线） |
| **仓骨架** | `SKILL.md`、`references/`、`LICENSE`、`README.md` | 可安装的 Skill 入口；MIT（可在确认清单里改） |

对已初始化的仓说：

```text
按 governance/rules/skill-governance.md 处理，不要直接改。先出 AP。
```

不要再对本包说「升级」「你是 Agent A」。

## 看一段真实怎么问

对话示例（Skill 名和人名是假的，问法是真的）：

目录：[examples/](examples/)（6 篇）

建议先看 [01-初始化空文件夹.md](examples/01-初始化空文件夹.md)，再看 [06-初始化之后打包和升版本.md](examples/06-初始化之后打包和升版本.md)。

## 开口就能用

| 你说 | 它做 |
|---|---|
| 「初始化 skill」 | 确认是空目录后，问英文名、干什么、显示名、版权；清单确认后写盘 |
| 「开发一个 skill，英文名 meeting-notes，把纪要收成行动项」 | 已说的不问，只补缺的 |
| 「把这个文件夹初始化成 skill」（目录非空） | **停止**，请换空文件夹 |
| 「再初始化」（已有 `SKILL.md`） | **停止**。指你去读仓里的 `governance/rules/skill-governance.md` |
| （初始化之后）「把版本升到 0.2.0 再打包」 | **不要对本包说。** 工作区换成那个 Skill 文件夹 |

同义口令：`开发一个 skill`、`新建技能`、`从零写 skill`、`脚手架`、`init skill`、`/init-skill`、`/new-skill`。

## 快速开始

1. 把本仓复制到助手的技能目录，例如 `~/.grok/skills/skill-devkit/`。
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
    ├── baselines/0.1.0/
    ├── migrations/
    ├── pack/pack.py
    └── scripts/          # sync_version / snapshot_baseline / audit_release
```

完整树和提问顺序见 `references/01-init.md`。

## 本仓结构

```
skill-devkit/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/           # 本包规则（只服务「用一次」的初始化）
├── assets/seed/          # 拷到目标仓的种子
├── assets/templates/
├── examples/
├── governance/planning/  # 仅本包作者自己用
└── README.md
```

## 许可证

[MIT](LICENSE) © 2026 仇索

## 斜杠

`/skill-devkit` · `/skill-devkit init` · `/init-skill` · `/new-skill`
