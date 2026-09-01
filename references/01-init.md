# 初始化 Skill 开发仓

工作区 = 用户选中的文件夹。本流程在该文件夹里**新建一个 Skill 开发仓**（代码 + git + 版本控制目录），不是改 ChronoPM，也不是只丢一个 `SKILL.md`。

种子与模板从 **本包（skill-devkit）** 根目录复制：`assets/seed/`、`assets/templates/`。先定位本包根（含本包 `SKILL.md` 且 `name: skill-devkit` 的目录）。种子缺失 → 停止，说明 skill-devkit 安装不完整。

## 1. 何时走本文件

见 `SKILL.md` 路由。典型口令：初始化 skill / 开发一个 skill / 新建 / 创建 / 从零 / 脚手架 / 骨架 / init / scaffold / bootstrap / `/skill-devkit init`。

用户一句话里已经给出的字段（名字、干什么、显示名）**不要再问**，只补缺的。

## 2. 先看文件夹

| 状况 | 动作 |
|---|---|
| 已有 `SKILL.md` | **禁止再初始化**。说明这里已经是 Skill 开发仓，版本控制在本文件夹的 `governance/`（若还没有，那是残缺仓，问用户要不要只补 `governance/`，不要整仓重做）。本包不做升级。 |
| 非空（有其它文件）且无 `SKILL.md` | 列出已有文件，问能否在此初始化，须明确同意才继续提问 |
| 空，或仅有无关的 `.DS_Store` / `Thumbs.db` | 进入提问 |

`.git` 已存在：不 `git init`，沿用；仍可补 Skill 文件与 `governance/`。

## 3. 必问（一次问一项，等答再问下一项）

自由文本用普通对话问，不要用选项卡片。

1. **英文名** `name`：小写字母、数字、连字符；2–64；头尾是字母或数字。文件夹名若已合法，可作为默认，仍须确认。
2. **干什么**：一句话，写成 `description` 的原料（做什么 + 何时用）。
3. **显示名**：给人看的中文名。可默认「从干什么里缩」，仍须确认。
4. **版权人**：LICENSE 用。默认「仇索」须用户点头，禁止猜。

名称不合法 → 指出规则，再问，不要往下走。

然后一次清单确认（可改；未确认不写盘）：

- 版本 `0.1.0`
- 许可证 MIT（本包只内置 MIT 模板；用户改用其他许可证则不要套该模板，按用户指定写）
- 中文 README
- `git init`（在**工作区根**，不是 `governance/` 里；若已有 `.git` 则跳过 init）
- 首提交（有 git 才做）
- 建 `governance/`（版本控制与发版目录）
- 远程 URL：默认无。用户给出再 `git remote add`，不主动 push
- 根据「干什么」草拟的 `SKILL.md` `description`（含触发说法）。用户可改

不问：目标版本号（新仓固定 0.1.0）。不问是否要工作区 schema（新仓默认无）。不问是否安装到 `~/.grok/skills/`（写完再提示，须用户明确要求才安装）。

## 4. 初始化写什么

全部写在**工作区根**。`governance/` 即「版本控制文件夹」：升级方案、变更单、基线快照、打包脚本都在这里。

```
{工作区}/
├── .git/                         # git init 在根上；不要放到 governance/ 里
├── .gitignore
├── LICENSE
├── README.md
├── CHANGELOG.md
├── SKILL.md
├── skill.json
├── VERSION                       # 0.1.0；发版读这里
├── references/README.md          # 该 Skill 自己的规则（先放说明）
├── assets/.gitkeep               # 该 Skill 运行时素材（可空）
├── scripts/.gitkeep              # 该 Skill 运行时脚本（可空）
└── governance/                   # 版本控制与发版（不进分发包）
    ├── README.md                 # 怎么升版本、怎么打包
    ├── planning/README.md        # AP：upgrade-plan-v{ver}.md
    ├── change-requests/.gitkeep
    ├── impact-analysis/.gitkeep
    ├── regression-reports/.gitkeep
    ├── baselines/README.md       # 已发布版本快照；初始化时不写 0.1.0 快照
    ├── review-checklists/release-checklist.md
    ├── templates/                # AP / CR / RR 空模板
    │   ├── upgrade-plan.md
    │   ├── CR-template.md
    │   └── RR-template.md
    ├── pack/
    │   ├── README.md
    │   └── pack.py
    └── scripts/
        └── sync_version.py
```

禁止：把 `.git` 建在 `governance/` 下；禁止把 `VERSION` 只放在 governance（根上必须有）；禁止生成 ChronoPM 的 `ai/`、todos、日报；禁止把新 Skill 默装进 `~/.grok/skills/`；禁止把本包（skill-devkit）自己的 `SKILL.md` 原文拷进目标仓。

初始化**不**写入 `governance/baselines/0.1.0/`。首发后再打快照。本流程写出的树本身就是开发基线。

## 5. 从种子复制

本包根 = 当前加载的 skill-devkit 目录。占位符整词替换，不要漏：

| 占位符 | 值 |
|---|---|
| `__NAME__` | 英文名 |
| `__DISPLAY_NAME__` | 显示名 |
| `__DESCRIPTION__` | 已确认的 description（可多行） |
| `__COPYRIGHT__` | 版权人 |
| `__YEAR__` | 当年（按对话日期） |
| `__DATE__` | 当天 `YYYY-MM-DD` |

| 源（本包） | 目标（工作区） |
|---|---|
| `assets/seed/gitignore` | `.gitignore` |
| `assets/seed/LICENSE.tmpl` | `LICENSE` |
| `assets/seed/README.md.tmpl` | `README.md` |
| `assets/seed/CHANGELOG.md.tmpl` | `CHANGELOG.md` |
| `assets/seed/SKILL.md.tmpl` | `SKILL.md` |
| `assets/seed/skill.json.tmpl` | `skill.json` |
| `assets/seed/VERSION` | `VERSION` |
| `assets/seed/references-README.md` | `references/README.md` |
| `assets/seed/gitkeep` | `assets/.gitkeep`、`scripts/.gitkeep`、`governance/change-requests/.gitkeep`、`governance/impact-analysis/.gitkeep`、`governance/regression-reports/.gitkeep` |
| `assets/seed/governance-README.md` | `governance/README.md` |
| `assets/seed/planning-README.md` | `governance/planning/README.md` |
| `assets/seed/baselines-README.md` | `governance/baselines/README.md` |
| `assets/seed/pack-README.md` | `governance/pack/README.md` |
| `assets/seed/pack.py` | `governance/pack/pack.py` |
| `assets/seed/sync_version.py` | `governance/scripts/sync_version.py` |
| `assets/templates/upgrade-plan.md` | `governance/templates/upgrade-plan.md` |
| `assets/templates/CR-template.md` | `governance/templates/CR-template.md` |
| `assets/templates/RR-template.md` | `governance/templates/RR-template.md` |
| `assets/templates/release-checklist.md` | `governance/review-checklists/release-checklist.md` |

`SKILL.md.tmpl` 的 `__DESCRIPTION__` 必须是清单里确认过的那段（含触发），不要另写一套。

写入注意：

- `skill.json` 的 `description` 必须是合法 JSON 字符串（转义 `"` 和 `\`，不要把未转义换行塞进 JSON）。
- `SKILL.md` front matter 若 description 含换行，用 YAML `>` 块并保持缩进，不要把未缩进换行插进 `---` 之间。

先建目录再写文件。文本文件 UTF-8。

## 6. Git

在工作区根执行（PowerShell 不要用 `&&`，不要用 bash heredoc）：

1. 若无 `.git`：`git init`
2. 空目录或用户同意纳入全部：`git add .`。若目录原先非空：只 add 本流程写出的路径，不要把用户原有无关文件卷进首提交，除非用户要求
3. `git commit -m "0.1.0 初始化 Skill 仓库"`
4. 用户给了远程 URL：`git remote add origin <url>`。不要 push，除非用户明确说推

无 `git` 命令：跳过本节，在结束说明里写「未做 git」。`.git` 已存在：跳过 init，仍做 add + commit（若无变更可跳过 commit）。

## 7. 写完对外说什么

- 根路径、英文名、显示名、版本 `0.1.0`
- `governance/` 已是完整版本控制与发版目录，默认不进 zip
- **本包对这个文件夹的工作结束。** 以后改规则、升版本、打包都不必再调用 skill-devkit
- 打包：`python governance/pack/pack.py --skill-root .`
- 升版本：改根目录 `VERSION`，再 `python governance/scripts/sync_version.py`
- 试用：须用户明确要求，才复制/安装到 `~/.grok/skills/<name>/`
- 建议下一步：把 `SKILL.md` 路由和 `references/` 细则写成这个 Skill 真正要做的事

## 8. 失败

名称不合法 → 指出规则，再问。用户拒绝默认项 → 按改后的写。写盘失败 → 已写的列出，未写的说明。中途取消 → 已写的留下并列出，不要擅自删。
