# Skill 开发工具包（skill-devkit）

给 **Skill 作者**用的独立 Skill：改现有 Skill、写升级方案、A/B 审核、定版本、打基线、发版。

不是业务项目管理，不是把各种能力塞进一个包。ChronoPM 是参考流程的来源，不是本仓的一部分。

## 仓库

```
skill-devkit/
├── SKILL.md
├── skill.json
├── VERSION
├── CHANGELOG.md
├── references/          # 本包规则（给运行本 Skill 的 Agent 读）
├── governance/planning/ # 本包自己的升级方案草稿
└── README.md
```

目标仓（被升级的那个 Skill）不在本目录里。用法：打开目标仓当工作区，本包安装到 `~/.grok/skills/skill-devkit/`。

## 斜杠

`/skill-devkit`

## 状态

0.1.0 骨架。协议全文、默认治理、家族锁步、发布脚本尚未迁入。
