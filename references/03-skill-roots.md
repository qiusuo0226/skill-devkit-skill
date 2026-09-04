# 技能目录探测

占用检查、收编「是否在助手安装目录」、试用拷贝目标，只读本文件。能跑则跑本包 `scripts/discover_skill_roots.py`，跑不了则按同文手扫。

## 环境变量

| 变量 | 作用 |
|---|---|
| `SKILL_DEVKIT_SKILLS_DIRS` | 分号分隔的绝对路径，每条作为一个扫描根。全平台用分号（避开 Windows 盘符冒号） |
| `GROK_HOME` / `LINGXI_HOME` / `CLAUDE_HOME` / `CODEX_HOME` | 助手 HOME。未设则跳过该项。对每个已设值，若 `{home}/skills` 或 `{home}/bundled/skills` 存在则加入 |

## 探测顺序

先命中的根都用，不是只留一个品牌。目录不存在则跳过，不把未安装的助手算失败。

1. `SKILL_DEVKIT_SKILLS_DIRS` 里的每一条（存在才加入）。
2. 上表助手 HOME 下的 `skills/` 与 `bundled/skills/`。
3. 用户主目录下候选（存在才加入）：`.grok/skills`、`.grok/bundled/skills`、`.claude/skills`、`.codex/skills`、`.cursor/skills`、`.lingma/skills`、`.lingxi/skills`、`.lingxi/bundled/skills`、`.qoder/skills`、`.agents/skills`。
4. 启发式（补充，不替代 1–3）：工作区路径匹配 `*/<点目录名>/skills/<叶>` 或 `*/bundled/skills/<叶>`。点目录名不枚举品牌，只认祖父目录名以 `.` 开头。命中则将该 `skills` 目录视为安装根。

去重按解析后的绝对路径。

## 占用检查

对每个存在的根：读 `*/SKILL.md` 的 front matter `name:`，以及与英文名同名的子目录。对用户只说「助手里已经有一个同名技能」，不把内部路径当正文。结束时可列扫到的根。

零个根 → 不阻断，结束写「未做占用检查（没有探测到技能目录；可设 SKILL_DEVKIT_SKILLS_DIRS）」。

脚本：`python scripts/discover_skill_roots.py --check-name <slug>`（先定位本包根）。

## 收编硬闸（安装目录）

工作区落在任一已探测根之下（含 `bundled/skills`）或启发式命中 → 停止。零个根时本条不阻断，但必须警告。

脚本：`python scripts/discover_skill_roots.py --contains <工作区绝对路径>`。`workspace_in_install_dir` 为 true 则停。

## 试用拷贝

禁止默装。用户开口试用时，从探测根里挑用户级 `skills/`（排除路径中含 `bundled` 的根）。0 个：问用户路径。2+ 个：列出，让用户选。仍须二次确认覆盖。

## 失败语义

扫失败（无权限 / 脚本跑不起来）→ 不阻断占用检查；收编安装闸零根时不阻断但警告。结束时必须说明扫了什么、跳过了什么。
