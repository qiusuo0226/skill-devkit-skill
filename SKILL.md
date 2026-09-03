---
name: skill-devkit
description: >
  Empty-folder initializer for an Agent Skill repo, or one-time adopt of an
  existing ungoverned skill. Versioning, frozen baselines, changelog/CR,
  change gates, trigger phrases, pack and release audit. Use once, then this
  kit exits.
  空文件夹一次初始化 Skill 开发仓，或收编已有但无规范的技能。覆盖：版本控制、
  冻结基线、升级记录、变更门禁、触发词、一键打包、发布审计。问完即落盘，本包退场。
  触发：初始化skill、初始化技能、初始化一个skill、初始化这个skill、初始化技能仓库、
  初始化开发仓、初始化当前目录、把这个文件夹初始化成skill、把当前目录初始化为skill、
  在这个目录开发skill、空目录初始化skill、开发一个skill、开发一个技能、开发新skill、
  开发新技能、开始开发skill、从零开发skill、从零写skill、开始写skill、新建skill、
  新建技能、创建skill、创建技能、创建新skill、创建新技能、建一个skill、搭一个skill、
  搭技能仓库、生成skill骨架、生成技能骨架、脚手架skill、新skill、新技能、
  init skill、initialize skill、scaffold skill、bootstrap skill、create a skill、
  new skill、develop a skill、start a skill、/skill-devkit、/skill-devkit init、
  /init-skill、/new-skill、
  收编skill、收编这个skill、收编已有skill、把这个skill收编进规范、把现有skill纳入基线、
  改造现有skill、规范化现有skill、给现有skill加基线、adopt skill、retrofit skill、
  /skill-devkit adopt。
  空仓走初始化；已有 SKILL.md 但无规范走收编。不要用于普通非空目录、已规范仓的升级发版、
  项目日报待办周报。
metadata:
  short-description: "空仓初始化或收编无规范技能，用完即走"
---

# Skill 开发工具包（skill-devkit）

**空仓一次初始化，或收编已有无规范技能：版本控制、冻结基线、升级记录、变更门禁、触发词、一键打包、发布审计。问完即落盘，本包退场。**

一次对话写进文件夹的不是一篇 `SKILL.md`，而是一套能自己发版的开发仓。写完 skill-devkit 从故事里消失；升版本、打基线、打 zip、A/B 审核都走那个文件夹自己的文件。

不是业务项目管理，不是常驻升级引擎，不是万能技能合集。

用法见 `examples/`（初始化 01～05、07；收编 17～20；初始化之后升版本见 08、21～23；记升级需求见 24；写规则 / 打包 / 试用见 10、06、16）。能力落点见 README 清单。

## 工作区

初始化：打开**空的**那个文件夹。收编：打开**已有技能、尚无本包规范**的那个文件夹。本包装在用户级（如 `~/.grok/skills/skill-devkit/`）。禁止把业务项目的 `ai/` 当 Skill 根。禁止在普通非空目录当空仓初始化。

## 路由

用户一句话里已给出的字段，不要再问。

| 用户信号 | 工作区 | 加载 |
|---|---|---|
| 初始化 / 开发一个 skill / 新建 / 创建 / 从零 / 脚手架 / 骨架 / init / scaffold / bootstrap / `/skill-devkit` / `/init-skill` / `/new-skill` | 空（或仅 `.git` / `.DS_Store` / `Thumbs.db`） | `references/01-init.md` |
| 同上 | 已有 `governance/rules/skill-governance.md` | `references/01-init.md` §2（停止） |
| 同上 | 已有 `SKILL.md`、无上条指纹 | `references/01-init.md` §2（停止，指路收编） |
| 同上 | 非空且无 `SKILL.md` | `references/01-init.md` §2（停止，换空文件夹） |
| 收编 / 纳入基线 / 改造现有 skill / adopt / retrofit / `/skill-devkit adopt` | 有 `SKILL.md`、无指纹 | `references/02-adopt.md` |
| 同上 | 空 | 停止，指路初始化 |
| 同上 | 已有指纹 | 停止，已规范 |
| 同上 | 非空无 `SKILL.md` | 停止 |
| 升级 / 你是 Agent A / 你是 Agent B / 写 AP / 打基线 / 发版 / 执行升级 | 任意 | 停止。已初始化或收编的仓读它自己的 `governance/rules/skill-governance.md` 与 `upgrade-dual-agent.md` |

硬闸见 `references/00-core.md`。初始化正文 `01-init.md`。收编正文 `02-adopt.md`。

## 硬闸

1. **初始化**只允许空文件夹或空 git 仓。非空不写盘、不问「能不能在这里初始化」。
2. **收编**只允许：根上有 `SKILL.md`，没有 `governance/rules/skill-governance.md`，没有来源不明的 `governance/`，不是本包自己，不在助手安装目录。版本多源冲突未决不写盘。
3. 用户确认问答清单之前禁止写盘。
4. 新空仓版本固定 `0.1.0`。收编保留已有版本（无则 0.1.0），不因收编升版。
5. 已规范仓禁止再初始化、禁止再收编。收编禁止改写技能正文与已有规则文件。
6. 禁止生成业务项目管理文件。禁止把 `.git` 建在 `governance/` 里。
7. 禁止给本包或目标仓做用户自动升级。禁止默装进 `~/.grok/skills/`。
8. 初始化或收编结束后不要继续用本包识别该仓。

## 版本

本包：见 `VERSION`。目标仓初始化为 `0.1.0`，收编沿用已有版本，之后由那个仓的 `VERSION` + `governance/` 管。
