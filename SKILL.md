---
name: skill-devkit
description: >
  Skill 开发工具包。给 Skill 作者用：在空文件夹初始化完整开发仓（含 git 与版本控制目录）。
  初始化完成后版本控制已在目标仓的 governance/ 里，不必再调用本包；本包不管已有 Skill 的升级，
  也不给终端用户做自动升级。
  触发：初始化skill、初始化技能、初始化一个skill、初始化这个skill、初始化技能仓库、
  初始化开发仓、初始化当前目录、把这个文件夹初始化成skill、把当前目录初始化为skill、
  在这个目录开发skill、空目录初始化skill、开发一个skill、开发一个技能、开发新skill、
  开发新技能、开始开发skill、从零开发skill、从零写skill、开始写skill、新建skill、
  新建技能、创建skill、创建技能、创建新skill、创建新技能、建一个skill、搭一个skill、
  搭技能仓库、生成skill骨架、生成技能骨架、脚手架skill、新skill、新技能、
  init skill、initialize skill、scaffold skill、bootstrap skill、create a skill、
  new skill、develop a skill、start a skill、/skill-devkit、/skill-devkit init、
  /init-skill、/new-skill。
  打开空的开发文件夹后使用。不要用于已有 Skill 的升级发版，不要用于项目日报、待办、周报。
metadata:
  short-description: "初始化 Skill 开发仓"
---

# Skill 开发工具包（skill-devkit）

给 **Skill 作者**用。只做一件事：把当前工作区初始化成 Skill 开发仓。

初始化一旦写完，目标仓根上的 git 和 `governance/` 就是完整版本控制（方案模板、打包、版本号同步都在里面）。**之后改那个 Skill、升版本、打包，都不必再调用本包。** 本包不考虑终端用户升级，也不给已有 Skill 当升级引擎。

不是业务项目管理。ChronoPM 只是「初始化向导怎么问人」的参考，不引用其路径。

用法对话见仓库 `examples/`。

## 工作区

打开**要用来开发那个新 Skill 的文件夹**当工作区。本 Skill 装在用户级（如 `~/.grok/skills/skill-devkit/`）。禁止把业务项目的 `ai/` 当成 Skill 根。

工作区可以是空文件夹，不要求已有 `SKILL.md`。

## 路由

用户一句话里已给出的字段，不要再问。

| 用户信号 | 工作区有 `SKILL.md`？ | 加载 |
|---|---|---|
| 初始化 / 开发一个 skill / 新建 / 创建 / 从零 / 脚手架 / 骨架 / init / scaffold / bootstrap / `/skill-devkit` / `/init-skill` / `/new-skill` | 无 | `references/01-init.md` |
| 同上 | 有 | `references/01-init.md` §2（拒绝再初始化） |
| 「开发 skill」且未说升级 | 无 | `references/01-init.md` |
| 升级 / 你是 Agent A / 你是 Agent B / 写 AP / 打基线 / 发版 | 任意 | 停止。本包不做这些。已有仓用它自己的 `governance/` |

硬闸与身份见 `references/00-core.md`。流程正文只在 `01-init.md`，不要把长文写进本文件。

## 硬闸

1. 用户确认问答清单之前禁止写盘。
2. 新仓版本固定 `0.1.0`。不问「升到几」。
3. 无 `SKILL.md`：初始化意图 → `01-init.md`；否则停止，提示改口「初始化 skill」。
4. 已有 `SKILL.md`：禁止再初始化，不要改写成升级流程。
5. 禁止把业务项目管理（日报、待办、`ai/`）写进目标仓。禁止把 `.git` 建在 `governance/` 里。
6. 禁止给本包或目标仓做「用户自动升级」。禁止把新 Skill 默装进 `~/.grok/skills/`。

## 版本

本包：见 `VERSION`。目标仓初始化为 `0.1.0`，之后的版本号由那个仓自己的 `VERSION` + `governance/` 管，与本包无关。
