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

对用户说话用白话。不要甩内部文件名或术语（不要说 governance、CR、AP、基线路径、description、dry-run、front matter）。自由文本问，不要用选项卡片。说法对齐 `examples/`。

1. **英文名**：小写字母、数字、连字符；2–64；头尾是字母或数字。文件夹名若已合法，可作为默认，仍须确认。不合法 → 指出规则，再问，不要往下走。
2. **是否撞名**（有了合法英文名立刻做，见 §3.1）：对用户说「助手里已经有一个同名技能」，不要报内部路径当正文。有冲突则先问换名还是坚持，未决之前不问下一题。
3. **干什么**：一句话。
4. **给人看的中文名**。可默认「从干什么里缩」，仍须确认。
5. **版权写谁**。默认「仇索」须用户点头，禁止猜。
6. **别人以后怎么开口才会用到它**。请几句常用说法。用户说跳过 → 从「干什么」生成，仍须在清单里亮出。开口里已经给了则不要再问。
7. **有没有代码仓库地址**。没有就说没有。不自动建仓、不 push。

然后一次清单确认（可改；未确认不写盘）。清单用白话：

- 版本从 0.1.0 起
- 许可证 MIT（用户改用其他则不要套 MIT 模板）
- 中文说明
- 在这个文件夹里建立 git（已有则跳过）
- 第一次提交
- 写上版本、打包、以后改这个技能要用的说明
- 别人可以这样叫它：（干什么 + 开口说法）
- 代码仓库：已填的地址，或无

对应要写入的文件仍按 §4～§5 做，不要把文件清单念给用户听。

不问目标版本号（固定 0.1.0）。不问工作区 schema（默认无）。不问是否安装到 `~/.grok/skills/`。

### 3.1 英文名占用检查

Grok 根：环境变量 `GROK_HOME`，否则用户主目录下的 `.grok`。

扫描（能扫到什么扫什么，目录不存在则跳过该项并在结束时说明）：

- `{grok}/skills/*/SKILL.md` 的 front matter `name:`
- `{grok}/skills/` 下与英文名同名的目录
- `{grok}/bundled/skills/*/SKILL.md` 的 `name:`（若存在）

命中 → 列出路径，说明：开发仓仍可用这个名字，但装进助手时可能覆盖或并列冲突。问：换一个英文名，还是坚持。换名则对新名重新做本检查。

未命中 → 不必专门汇报「没占用」，进入下一问。

扫失败（无权限 / 无 `.grok`）→ 不阻断，结束时写「未做占用检查」。

## 4. 初始化写什么

全部写在**工作区根**。`governance/` 是版本控制文件夹，**不进分发包**。后续提示词在 `governance/rules/` 和根上 `AGENTS.md`。

```
{工作区}/
├── .git/
├── .gitignore
├── AGENTS.md
├── LICENSE
├── README.md
├── CHANGELOG.md                 # 0.1.0 脚手架诞生
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
    ├── change-requests/CR-000-init.md
    ├── impact-analysis/.gitkeep
    ├── regression-reports/.gitkeep
    ├── baselines/README.md
    ├── baselines/0.1.0/
    ├── migrations/README.md
    ├── migrations/upgrade-to-0.1.0.md
    ├── review-checklists/release-checklist.md
    ├── templates/
    ├── pack/pack.py
    ├── dev.ps1
    └── scripts/
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
| `assets/seed/gitkeep` | `assets/.gitkeep`、`scripts/.gitkeep`、`governance/impact-analysis/.gitkeep`、`governance/regression-reports/.gitkeep` |
| `assets/seed/governance-README.md` | `governance/README.md` |
| `assets/seed/rules-README.md` | `governance/rules/README.md` |
| `assets/seed/skill-governance.md` | `governance/rules/skill-governance.md` |
| `assets/seed/planning-README.md` | `governance/planning/README.md` |
| `assets/seed/baselines-README.md` | `governance/baselines/README.md` |
| `assets/seed/migrations-README.md` | `governance/migrations/README.md` |
| `assets/seed/CR-000-init.tmpl` | `governance/change-requests/CR-000-init.md` |
| `assets/seed/upgrade-to-0.1.0.tmpl` | `governance/migrations/upgrade-to-0.1.0.md` |
| `assets/seed/pack-README.md` | `governance/pack/README.md` |
| `assets/seed/dev.ps1` | `governance/dev.ps1` |
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

`SKILL.md.tmpl` 的 `__DESCRIPTION__` 必须是清单里确认过的那段（含触发）。`skill.json` 的 description 做成合法 JSON 字符串。`SKILL.md` front matter 换行用 YAML `>` 并保持缩进。文本 UTF-8。先建目录再写文件。

写完后在工作区根执行（按序；某步失败不回滚已写文件，列出失败项继续能做的）：

1. `python governance/scripts/snapshot_baseline.py` → `governance/baselines/0.1.0/`。不要覆盖已有基线。
2. `python governance/scripts/audit_release.py`。向用户汇报通过/失败项。
3. `python governance/pack/pack.py --skill-root . --dry-run`。汇报文件数；点名确认列表里**没有** `governance/`、`.git/`、`AGENTS.md`。列出不超过 20 条路径作预览。 **不要**把 zip 写进仓库。

## 6. Git

在工作区根执行（PowerShell 不要用 `&&`，不要用 bash heredoc）：

1. 若无 `.git`：`git init`
2. `git add .`
3. `git commit -m "0.1.0 初始化 Skill 仓库"`
4. 用户给了远程 URL：`git remote add origin <url>`。不要 push，除非用户明确说推

无 `git`：跳过本节，结束时说明。已有 `.git`：跳过 init，仍做 add + commit。

## 7. 写完对外说什么

白话，对齐 `examples/01-初始化空文件夹.md` 第 8 轮。不要念内部路径。

> 写好了。文件夹 / 英文名 / 中文名 / 版本 0.1.0。已经能打包；安装包里不会带上开发用的说明。本包用完了。以后改这个技能、升版本、打安装包，把工作区留在这个文件夹直接说就行。下一步把技能真正要做的规则写进去。要装到助手里试用，你开口我才拷。

检查失败时用白话说哪一步没过，再补一句内部命令给愿意看的人。撞名而用户坚持，补一句提醒。

## 8. 失败

名称不合法 → 指出规则，再问。占用冲突未决 → 不写盘。用户拒绝默认项 → 按改后的写。写盘失败 → 已写的列出，未写的说明。中途取消 → 已写的留下并列出，不要擅自删。非空目录 → 不写盘。
