# 初始化 Skill 开发仓

工作区 = 用户选中的文件夹。只允许 **空文件夹或空 git 仓**。本流程在这里新建一套完整开发仓（代码 + git + 版本控制 + 基线 + 打包 + 后续提示词）。不是改 ChronoPM，不是只丢一个 `SKILL.md`。

种子与模板从 **本包（skill-devkit）** 根目录复制：`assets/seed/`、`assets/templates/`。先定位本包根（含本包 `SKILL.md` 且 `name: skill-devkit`）。种子缺失 → 停止，说明安装不完整。

初始化写完后，目标仓用自己的 `governance/rules/skill-governance.md` 做版本、基线、升级记录、打包。**本包使命结束，不再识别或接管那个仓。**

## 1. 何时走本文件

见 `SKILL.md` 路由。用户一句话里已经给出的字段不要再问。

## 2. 先看文件夹（空才继续）

列出工作区内容。下列视为「空」，可以初始化：

- 完全没有文件
- 仅有 `.DS_Store` / `Thumbs.db`
- 仅有 `.git/`（空仓：还没有 `SKILL.md` 和其他项目文件）

| 状况 | 动作 |
|---|---|
| 空（含上空仓） | 进入提问 |
| 已有 `SKILL.md` | **停止**。已经是 Skill 开发仓。本包只用一次。改规则、升版本、打包读那个仓的 `governance/rules/skill-governance.md` |
| 有任何其他文件或目录 | **停止**。列出文件。请换一个空文件夹或空 git 仓。禁止问「能不能在这里初始化」，禁止在非空目录写盘 |

`.git` 已存在：不 `git init`，沿用。

## 3. 必问（一次问一项，等答再问下一项）

自由文本用普通对话问，不要用选项卡片。

1. **英文名** `name`：小写字母、数字、连字符；2–64；头尾是字母或数字。文件夹名若已合法，可作为默认，仍须确认。
2. **干什么**：一句话，写成 `description` 的原料（做什么 + 何时用）。
3. **显示名**：给人看的中文名。可默认「从干什么里缩」，仍须确认。
4. **版权人**：LICENSE 用。默认「仇索」须用户点头，禁止猜。

名称不合法 → 指出规则，再问，不要往下走。

然后一次清单确认（可改；未确认不写盘）：

- 版本 `0.1.0`
- 许可证 MIT（本包只内置 MIT 模板；用户改用其他则不要套该模板）
- 中文 README
- `git init`（工作区根；已有 `.git` 则跳过）
- 首提交
- 建 `governance/`（版本控制、基线、升级记录、打包、治理提示词）
- 打 `0.1.0` 基线快照
- 远程 URL：默认无。用户给出再 `git remote add`，不主动 push
- 草拟的 `SKILL.md` `description`（含触发）。用户可改

不问目标版本号（固定 0.1.0）。不问工作区 schema（默认无）。不问是否安装到 `~/.grok/skills/`。

## 4. 初始化写什么

全部写在**工作区根**。`governance/` 是版本控制文件夹，**不进分发包**。后续提示词在 `governance/rules/` 和根上 `AGENTS.md`。

```
{工作区}/
├── .git/
├── .gitignore
├── AGENTS.md                    # 开发提示：读 governance/rules；不进 zip
├── LICENSE
├── README.md
├── CHANGELOG.md
├── SKILL.md
├── skill.json
├── VERSION                      # 0.1.0
├── references/README.md
├── assets/.gitkeep
├── scripts/.gitkeep
├── tests/README.md
└── governance/
    ├── README.md
    ├── rules/skill-governance.md
    ├── planning/README.md
    ├── change-requests/.gitkeep
    ├── impact-analysis/.gitkeep
    ├── regression-reports/.gitkeep
    ├── baselines/README.md
    ├── baselines/0.1.0/         # 初始化末尾快照
    ├── migrations/README.md
    ├── review-checklists/release-checklist.md
    ├── templates/               # AP / CR / IA / RR / upgrade-to
    ├── pack/pack.py
    └── scripts/                 # sync_version / snapshot_baseline / audit_release
```

禁止：`.git` 建在 `governance/`；`VERSION` 只放在 governance；生成 ChronoPM 的 `ai/`；默装进 `~/.grok/skills/`；把本包 `SKILL.md` 原文拷进目标仓。

## 5. 从种子复制

占位符整词替换：`__NAME__` `__DISPLAY_NAME__` `__DESCRIPTION__` `__COPYRIGHT__` `__YEAR__` `__DATE__`。

| 源（本包） | 目标（工作区） |
|---|---|
| `assets/seed/gitignore` | `.gitignore` |
| `assets/seed/AGENTS.md` | `AGENTS.md` |
| `assets/seed/LICENSE.tmpl` | `LICENSE` |
| `assets/seed/README.md.tmpl` | `README.md` |
| `assets/seed/CHANGELOG.md.tmpl` | `CHANGELOG.md` |
| `assets/seed/SKILL.md.tmpl` | `SKILL.md` |
| `assets/seed/skill.json.tmpl` | `skill.json` |
| `assets/seed/VERSION` | `VERSION` |
| `assets/seed/references-README.md` | `references/README.md` |
| `assets/seed/tests-README.md` | `tests/README.md` |
| `assets/seed/gitkeep` | `assets/.gitkeep`、`scripts/.gitkeep`、`governance/change-requests/.gitkeep`、`governance/impact-analysis/.gitkeep`、`governance/regression-reports/.gitkeep` |
| `assets/seed/governance-README.md` | `governance/README.md` |
| `assets/seed/rules-README.md` | `governance/rules/README.md` |
| `assets/seed/skill-governance.md` | `governance/rules/skill-governance.md` |
| `assets/seed/planning-README.md` | `governance/planning/README.md` |
| `assets/seed/baselines-README.md` | `governance/baselines/README.md` |
| `assets/seed/migrations-README.md` | `governance/migrations/README.md` |
| `assets/seed/pack-README.md` | `governance/pack/README.md` |
| `assets/seed/pack.py` | `governance/pack/pack.py` |
| `assets/seed/sync_version.py` | `governance/scripts/sync_version.py` |
| `assets/seed/snapshot_baseline.py` | `governance/scripts/snapshot_baseline.py` |
| `assets/seed/audit_release.py` | `governance/scripts/audit_release.py` |
| `assets/templates/upgrade-plan.md` | `governance/templates/upgrade-plan.md` |
| `assets/templates/CR-template.md` | `governance/templates/CR-template.md` |
| `assets/templates/IA-template.md` | `governance/templates/IA-template.md` |
| `assets/templates/RR-template.md` | `governance/templates/RR-template.md` |
| `assets/templates/upgrade-to.md` | `governance/templates/upgrade-to.md` |
| `assets/templates/release-checklist.md` | `governance/review-checklists/release-checklist.md` |

`SKILL.md.tmpl` 的 `__DESCRIPTION__` 必须是清单里确认过的那段。`skill.json` 的 description 做成合法 JSON 字符串。`SKILL.md` front matter 换行用 YAML `>` 并保持缩进。文本 UTF-8。先建目录再写文件。

写完后在工作区根执行：`python governance/scripts/snapshot_baseline.py`（生成 `governance/baselines/0.1.0/`）。失败则按 `pack.py` 的排除规则手工拷贝分发包会包含的文件到该目录，并说明。不要覆盖已有基线目录。

## 6. Git

在工作区根执行（PowerShell 不要用 `&&`，不要用 bash heredoc）：

1. 若无 `.git`：`git init`
2. `git add .`
3. `git commit -m "0.1.0 初始化 Skill 仓库"`
4. 用户给了远程 URL：`git remote add origin <url>`。不要 push，除非用户明确说推

无 `git`：跳过本节，结束时说明。已有 `.git`：跳过 init，仍做 add + commit。

## 7. 写完对外说什么

- 根路径、英文名、显示名、版本 `0.1.0`，已有 `0.1.0` 基线
- **本包对这个文件夹的工作结束，只用了一次。**
- 以后改这个 Skill：工作区仍是本文件夹，对助手说「按 `governance/rules/skill-governance.md` 处理，不要直接改」
- 不必再调用 skill-devkit，也不要对本包说升级 / Agent A
- 打包 / 升版本 / 打基线 / 审计命令见 `governance/README.md`
- 试用须用户明确要求，才拷到 `~/.grok/skills/<name>/`
- 下一步：把 `SKILL.md` 路由和 `references/` 写成这个 Skill 真正要做的事

## 8. 失败

名称不合法 → 指出规则，再问。用户拒绝默认项 → 按改后的写。写盘失败 → 已写的列出，未写的说明。中途取消 → 已写的留下并列出，不要擅自删。非空目录 → 不写盘。
