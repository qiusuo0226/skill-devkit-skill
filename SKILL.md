---
name: skill-devkit
description: >
  Skill 开发工具包。给 Skill 作者用：在空文件夹初始化完整开发仓（含 git 与版本控制目录），
  或给已有 Skill 写升级方案、A/B 审核、定版本、打基线、打包发版。
  初始化触发：初始化skill、初始化技能、初始化一个skill、初始化这个skill、初始化技能仓库、
  初始化开发仓、初始化当前目录、把这个文件夹初始化成skill、把当前目录初始化为skill、
  在这个目录开发skill、空目录初始化skill、开发一个skill、开发一个技能、开发新skill、
  开发新技能、开始开发skill、从零开发skill、从零写skill、开始写skill、新建skill、
  新建技能、创建skill、创建技能、创建新skill、创建新技能、建一个skill、搭一个skill、
  搭技能仓库、生成skill骨架、生成技能骨架、脚手架skill、新skill、新技能、
  init skill、initialize skill、scaffold skill、bootstrap skill、create a skill、
  new skill、develop a skill、start a skill、/skill-devkit init、/init-skill、/new-skill。
  升级触发：升级 Skill、你是 Agent A、你是 Agent B、写 AP、审核升级方案、Skill 发版、
  打基线、/skill-devkit。
  打开某个 Skill 代码仓或空的开发文件夹后使用。
  不要用于项目日报、待办、周报或业务项目管理。
metadata:
  short-description: "初始化并维护 Skill 开发仓"
---

# Skill 开发工具包（skill-devkit）

给 **Skill 作者**用。对象是当前工作区里的 **Skill 开发仓**（已有或即将创建），不是业务项目文件夹。

本包与 ChronoPM 独立。升级流程**借鉴**其门禁（先方案后改文件、A/B 分角色、版本与基线），不引用 ChronoPM 路径，不接管日报/待办。

## 工作区

打开**被开发的那个文件夹**当工作区。本 Skill 装在用户级（如 `~/.grok/skills/skill-devkit/`）。禁止把业务项目的 `ai/` 当成 Skill 根。

- **初始化**：工作区可以是空文件夹，不要求已有 `SKILL.md`。
- **升级 / 改规则**：Skill 根 = 含 `SKILL.md` 的目录。仓内多个 `SKILL.md` 时按「技能家族」处理：先问锁步还是各升各的。

## 路由

先判初始化，再判升级。用户一句话里已给出的字段，初始化时不要再问。

| 用户信号 | 工作区有 `SKILL.md`？ | 角色 | 加载 |
|---|---|---|---|
| 初始化 / 开发一个 skill / 新建 / 创建 / 从零 / 脚手架 / 骨架 / init / scaffold / bootstrap / `/skill-devkit init` / `/init-skill` / `/new-skill` | 无 | 初始化 | `references/01-init.md` |
| 同上（初始化意图） | 有 | 拒绝再初始化 | `references/01-init.md` §2 |
| 「开发 skill」且未说升级、也未说初始化 | 无 | 初始化 | `references/01-init.md` |
| 「开发 skill」且未说初始化 | 有 | A（改已有仓） | `references/00-core.md` |
| 你是 Agent A / 写升级方案 / 写 AP / `/skill-devkit a` | 有 | A | `references/00-core.md` |
| 你是 Agent B / B1 / B2 / 审核升级方案 | 有 | B | `references/00-core.md` |
| 同意执行 / 开始改文件 | 有 | 执行 | `references/00-core.md`（须已有确认方案） |
| 升级 / 写 AP / Agent A 或 B | 无 | 停止 | 提示先初始化，或打开已有 Skill 仓 |

细则未迁入前：00 为核心门禁。A/B 全文协议后续单独迁入 `references/`，禁止把长协议写进本文件。

## 硬闸

1. 未确认方案前禁止改**已有**目标 Skill 正文。初始化在用户确认问答清单之前禁止写盘。
2. 用户开口不必报目标版本；新仓固定 `0.1.0`。已有仓由 A 读 `VERSION` / `skill.json` 后按变更类型拟定，写入方案。
3. 禁止向用户索要 ChronoPM 或 Downloads 里的外置升级提示词。
4. 无 `SKILL.md`：初始化意图 → 走 `01-init.md`；否则停止，提示打开 Skill 代码仓或改口「初始化 skill」。
5. 同一对话已以 A 出过方案 → 拒绝直接转 B。
6. 禁止把业务项目管理（日报、待办、`ai/`）写进目标仓。禁止把 `.git` 建在 `governance/` 里。

## 版本

本包：见 `VERSION`。目标仓版本由初始化（`0.1.0`）或升级方案拟定，不与本包版本混用。
