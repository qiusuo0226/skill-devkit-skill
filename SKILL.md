---
name: skill-devkit
description: >
  Empty-folder initializer for an Agent Skill repo: versioning, frozen
  baselines, changelog/CR, change gates, trigger phrases, pack and release
  audit. Use once on an empty folder, then this kit exits.
  空文件夹一次初始化 Skill 开发仓。覆盖：版本控制（VERSION+git）、冻结基线、
  升级记录（CHANGELOG/CR/upgrade-to/tag）、变更门禁（先方案后改文件）、
  影响分析与回归、触发词写入 description、英文名占用检查、一键打包与发布审计。
  问名字、用途、触发说法后落盘，本包用完即走；之后发版走这个文件夹自己的文件。
  触发：初始化skill、初始化技能、初始化一个skill、初始化这个skill、初始化技能仓库、
  初始化开发仓、初始化当前目录、把这个文件夹初始化成skill、把当前目录初始化为skill、
  在这个目录开发skill、空目录初始化skill、开发一个skill、开发一个技能、开发新skill、
  开发新技能、开始开发skill、从零开发skill、从零写skill、开始写skill、新建skill、
  新建技能、创建skill、创建技能、创建新skill、创建新技能、建一个skill、搭一个skill、
  搭技能仓库、生成skill骨架、生成技能骨架、脚手架skill、新skill、新技能、
  init skill、initialize skill、scaffold skill、bootstrap skill、create a skill、
  new skill、develop a skill、start a skill、/skill-devkit、/skill-devkit init、
  /init-skill、/new-skill。
  只用于空文件夹或空 git 仓。不要用于非空目录、已有 Skill 的升级发版、项目日报待办周报。
metadata:
  short-description: "空仓写入版本/基线/升级记录/打包，用完即走"
---

# Skill 开发工具包（skill-devkit）

**空仓一次初始化：版本控制、冻结基线、升级记录、变更门禁、触发词、一键打包、发布审计。问完即落盘，本包退场。**

一次对话写进空文件夹的不是一篇 `SKILL.md`，而是一套能自己发版的开发仓。写完 skill-devkit 从故事里消失；升版本、打基线、打 zip 都走这个文件夹自己的文件和提示词。

只在**空文件夹或空 git 仓**用。不是业务项目管理，不是常驻升级引擎，不是万能技能合集。

用法见 `examples/`（初始化 01～05、07；初始化之后升版本见 08：方案七章与生成路径；写规则 / 打包 / 试用见 10、06、16）。能力落点见 README 清单。

## 工作区

打开**空的**那个文件夹。本包装在用户级（如 `~/.grok/skills/skill-devkit/`）。禁止把业务项目的 `ai/` 当 Skill 根。禁止在非空目录初始化。

## 路由

用户一句话里已给出的字段，不要再问。

| 用户信号 | 工作区 | 加载 |
|---|---|---|
| 初始化 / 开发一个 skill / 新建 / 创建 / 从零 / 脚手架 / 骨架 / init / scaffold / bootstrap / `/skill-devkit` / `/init-skill` / `/new-skill` | 空（或仅 `.git` / `.DS_Store` / `Thumbs.db`） | `references/01-init.md` |
| 同上 | 已有 `SKILL.md` | `references/01-init.md` §2（停止，指本地治理提示词） |
| 同上 | 非空 | `references/01-init.md` §2（停止，换空文件夹） |
| 升级 / 你是 Agent A / 写 AP / 打基线 / 发版 | 任意 | 停止。已初始化的仓读它自己的 `governance/rules/skill-governance.md` |

硬闸见 `references/00-core.md`。流程正文只在 `01-init.md`。

## 硬闸

1. 只允许空文件夹或空 git 仓。非空不写盘、不问「能不能在这里初始化」。
2. 用户确认问答清单之前禁止写盘。
3. 新仓版本固定 `0.1.0`。
4. 已有 `SKILL.md`：禁止再初始化，不要改写成升级流程。
5. 禁止生成业务项目管理文件。禁止把 `.git` 建在 `governance/` 里。
6. 禁止给本包或目标仓做用户自动升级。禁止默装进 `~/.grok/skills/`。
7. 初始化结束后不要继续用本包识别该仓。

## 版本

本包：见 `VERSION`。目标仓初始化为 `0.1.0`，之后由那个仓的 `VERSION` + `governance/` 管。
