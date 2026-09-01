---
name: skill-devkit
description: >
  Skill 开发工具包。给 Skill 作者改规则、写升级方案、审方案、定版本、打基线、发版。
  打开某个 Skill 代码仓后使用。触发：开发 Skill、升级 Skill、你是 Agent A、你是 Agent B、
  写 AP、审核升级方案、Skill 发版、打基线、/skill-devkit。
  不要用于项目日报、待办、周报或业务项目管理。
---

# Skill 开发工具包（skill-devkit）

给 **Skill 作者**用。对象是当前工作区里的 **Skill 代码仓**，不是业务项目文件夹。

本包与 ChronoPM 独立。升级流程**借鉴**其门禁（先方案后改文件、A/B 分角色、版本与基线），不引用 ChronoPM 路径，不接管日报/待办。

## 工作区

打开**被开发的那个 Skill 仓库**当工作区，本 Skill 装在用户级或本仓。禁止把业务项目的 `ai/` 当成 Skill 根。

Skill 根 = 含 `SKILL.md` 的目录。仓内多个 `SKILL.md` 时按「技能家族」处理：先问锁步还是各升各的。

## 路由

| 用户信号 | 角色 | 加载 |
|---|---|---|
| 你是 Agent A / 写升级方案 / 写 AP / /skill-devkit a | A | `references/00-core.md` |
| 你是 Agent B / B1 / B2 / 审核升级方案 | B | `references/00-core.md` |
| 同意执行 / 开始改文件 | 执行 | `references/00-core.md`（须已有确认方案） |

细则未迁入前：00 为核心门禁。A/B 全文协议后续单独迁入 `references/`，禁止把长协议写进本文件。

## 硬闸

1. 未确认方案前禁止改目标 Skill 正文。
2. 用户开口不必报目标版本；A 读目标仓 `VERSION` / `skill.json` 后按变更类型拟定，写入方案。
3. 禁止向用户索要 ChronoPM 或 Downloads 里的外置升级提示词。
4. 业务仓（无 `SKILL.md`）命中本 Skill → 停止，提示打开 Skill 代码仓。
5. 同一对话已以 A 出过方案 → 拒绝直接转 B。

## 版本

本包：见 `VERSION`。目标仓版本由方案拟定，不与本包版本混用。
