# 核心门禁（skill-devkit）

## 身份

本包是 Skill **开发与发版**工具。当前工作区应是某个 Skill 代码仓。禁止当 ChronoPM 用，禁止写业务 `ai/` 事实源。

## 确认工作区

首次动作：找出含 `SKILL.md` 的根（仓根或子目录）。向用户展示路径与目标 `VERSION` / `skill.json` 的 version，等确认后再扫描。

多个 `SKILL.md`：列为家族成员，询问锁步还是独立。未答之前只读，不写版本号。

## 方案未确认不改目标

禁止在用户确认方案前修改目标仓 Skill 正文。本包自己的 `governance/planning/` 可写方案草稿。

## 版本拟定

用户不必报升到几。读目标仓版本 → 按类型建议：规则修复 Patch、新能力或新目录 Minor、核心契约 Major 或 Minor。写入方案。禁止把「请先告诉我升到几」当成开干前提。

## 与 create-skill / pack-skill

空白脚手架用 create-skill。打 zip 用 pack-skill（若已装）。本包管变更生命周期，不替代那两个。
