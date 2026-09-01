# 核心门禁（skill-devkit）

## 身份

本包是 Skill **开发与发版**工具。当前工作区应是某个 Skill 开发仓（已有，或初始化即将创建）。禁止当 ChronoPM 用，禁止写业务 `ai/` 事实源。

## 确认工作区

先看本轮是否初始化意图（见 `SKILL.md` 路由）。是 → 加载 `01-init.md`，工作区 = 用户选中的文件夹，**不要求**已有 `SKILL.md`。

否则：找出含 `SKILL.md` 的根（仓根或子目录）。向用户展示路径与目标 `VERSION` / `skill.json` 的 version，等确认后再改文件。

多个 `SKILL.md`：列为家族成员，询问锁步还是独立。未答之前只读，不写版本号。

无 `SKILL.md` 且不是初始化 → 停止，提示打开 Skill 代码仓，或改口「初始化 skill」。

## 方案未确认不改目标

禁止在用户确认方案前修改**已有**目标仓 Skill 正文。本包自己的 `governance/planning/` 可写方案草稿。

初始化：用户确认问答清单前禁止写盘（见 `01-init.md`）。

## 版本拟定

用户不必报升到几。新仓固定 `0.1.0`。已有仓：读目标仓版本 → 按类型建议：规则修复 Patch、新能力或新目录 Minor、核心契约 Major 或 Minor。写入方案。禁止把「请先告诉我升到几」当成开干前提。

## 与 create-skill / pack-skill

本包负责：空文件夹初始化**完整开发仓**（git + `governance/` 版本控制与打包），以及已有仓的升级生命周期。

`create-skill`：把轻量 `SKILL.md` 脚手架到 `~/.grok/skills` 或项目 `.grok/skills`，**不**生成本包这套开发基线。初始化不要改走 create-skill。

打 zip：用目标仓 `governance/pack/pack.py`。若用户已装 pack-skill 也可以，二者不互斥。
