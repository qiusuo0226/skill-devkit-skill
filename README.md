# Skill 开发工具包（skill-devkit）

**把空文件夹变成一套能开发、能版本控制、能打包的 Skill 仓。初始化完，本包就退场。**

给 Skill 作者用。装进 AI 助手之后，你新建一个文件夹、把工作区指过去，说「初始化 skill」——它问名字和用途，点头后在这个文件夹里写下 `SKILL.md`、git，以及完整的 `governance/`（方案模板、版本号同步、打包脚本）。

初始化一旦结束，版本控制已经在**那个新仓**里。之后改规则、升版本、打 zip，都不必再打开本包。本包不管已有 Skill 的升级，也不给终端用户做自动升级。

不是业务项目管理，不是万能工具箱。ChronoPM 只是「向导怎么问人」的参考，不是本仓的一部分。

## 仓库

Gitee：[qiusuo0226/skill-devkit-skill](https://gitee.com/qiusuo0226/skill-devkit-skill)

## 它只做一件事

```mermaid
flowchart LR
    A["1 安装本包到助手"] --> B["2 新建空文件夹并选为工作区"]
    B --> C["3 说：初始化 skill"]
    C --> D["4 问答 + 确认清单"]
    D --> E["5 写出开发仓"]
    E --> F["6 本包退场\n用新仓的 governance/"]
```

不要指望它对已有 Skill 说「你是 Agent A」还能当升级引擎。那不是本包的工作。

## 看一段真实怎么问

对话示例（Skill 名和人名是假的，问法是真的）：

目录：[examples/](examples/)（6 篇）

建议先看 [01-初始化空文件夹.md](examples/01-初始化空文件夹.md)，再看 [06-初始化之后打包和升版本.md](examples/06-初始化之后打包和升版本.md)。

## 开口就能用

| 你说 | 它做 |
|---|---|
| 「初始化 skill」 | 一次一项问英文名、干什么、显示名、版权；清单确认后写盘 |
| 「开发一个 skill，英文名 meeting-notes，把纪要收成行动项」 | 已说的不问，只补缺的 |
| 「把这个文件夹初始化成 skill」（目录非空） | 先列出已有文件，你同意才继续 |
| 「再初始化」（已有 `SKILL.md`） | 拒绝。指你去用仓里的 `governance/` |
| （初始化之后）「把版本升到 0.2.0 再打包」 | **不要对本包说。** 工作区换成那个 Skill 文件夹，用它自己的脚本 |

同义口令：`开发一个 skill`、`新建技能`、`从零写 skill`、`脚手架`、`init skill`、`/init-skill`、`/new-skill`。

## 快速开始

1. 把本仓复制到助手的技能目录，例如 `~/.grok/skills/skill-devkit/`。
2. 新建一个**空文件夹**，把助手工作区指到那里（不要指到本仓上）。
3. 说：「初始化 skill」。
4. 问完确认清单，说「按这个写」。
5. 之后开发、升版本、打包都在那个新文件夹里进行，不再调用本包。

打包（在**目标仓**里，不是在本仓里）：

```
python governance/pack/pack.py --skill-root .
```

升版本：改目标仓根目录 `VERSION`，再：

```
python governance/scripts/sync_version.py
```

## 初始化会写出什么

工作区根上是 Skill 正文和 git（`.git` 在根上）。版本控制全部在 `governance/`：

```
{你的新文件夹}/
├── .git/                 # 根上，不在 governance/ 里
├── SKILL.md
├── skill.json
├── VERSION               # 0.1.0
├── CHANGELOG.md
├── LICENSE
├── README.md
├── references/
└── governance/           # 版本控制与打包，不进分发包
    ├── pack/pack.py
    ├── scripts/sync_version.py
    └── templates/
```

完整树和提问顺序见 `references/01-init.md`。种子在 `assets/seed/`。

## 本仓结构

```
skill-devkit/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/           # 本包规则（给运行本 Skill 的 Agent 读）
├── assets/seed/          # 初始化时拷到目标仓
├── assets/templates/
├── examples/             # 对话示例
├── governance/planning/  # 仅本包作者自己用，不面向使用者升级
└── README.md
```

## 许可证

[MIT](LICENSE) © 2026 仇索

## 斜杠

`/skill-devkit` · `/skill-devkit init` · `/init-skill` · `/new-skill`
