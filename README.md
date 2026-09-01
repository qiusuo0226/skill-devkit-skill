# Skill 开发工具包（skill-devkit）

给 **Skill 作者**用的独立 Skill：在空文件夹初始化完整开发仓，或给已有 Skill 写升级方案、A/B 审核、定版本、打基线、打包发版。

不是业务项目管理，不是把各种能力塞进一个包。ChronoPM 是参考流程的来源，不是本仓的一部分。

## 用法

1. 把本包装进 Agent（例如 `~/.grok/skills/skill-devkit/`）。
2. 新建一个空文件夹，把 Agent 工作区指到那里。
3. 说「初始化 skill」「开发一个 skill」「新建技能」等（见 `SKILL.md` description）。
4. 按提问确认英文名、干什么、显示名、版权；再确认默认清单。
5. 确认后在该文件夹生成开发基线：`SKILL.md`、git（根上）、`governance/`（版本控制与打包）。

已有 Skill 仓：打开该仓当工作区，说「你是 Agent A」+ 需求。

目标仓不在本目录里。不要把业务项目的 `ai/` 当 Skill 根。

## 仓库

```
skill-devkit/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/          # 本包规则（给运行本 Skill 的 Agent 读）
├── assets/seed/         # 初始化时拷到目标仓的种子
├── assets/templates/    # 初始化时拷到目标仓 governance/templates
├── governance/planning/ # 本包自己的升级方案草稿
└── README.md
```

## 许可证

[MIT](LICENSE) © 2026 仇索

## 斜杠

`/skill-devkit` · `/skill-devkit init` · `/init-skill` · `/new-skill`
