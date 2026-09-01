# 核心门禁（skill-devkit）

## 身份

本包只做一件事：把用户选中的文件夹初始化成 Skill 开发仓（代码 + 根上 git + `governance/` 版本控制）。

初始化完成后，目标仓自己的 `governance/` 就是完整版本控制。不必再调用本包。禁止当已有 Skill 的升级引擎，禁止给终端用户做自动升级，禁止当 ChronoPM 用，禁止写业务 `ai/`。

## 确认工作区

工作区 = 用户选中的文件夹，**不要求**已有 `SKILL.md`。加载 `01-init.md`。

无 `SKILL.md` 且用户也不是在初始化 → 停止，提示改口「初始化 skill」。

已有 `SKILL.md` → 见 `01-init.md` §2，拒绝再初始化，不要改走升级。

## 未确认不写盘

用户确认问答清单前禁止写盘（见 `01-init.md`）。

## 与 create-skill

`create-skill`：把轻量 `SKILL.md` 脚手架到 `~/.grok/skills` 或项目 `.grok/skills`，**不**生成本包这套开发基线。初始化不要改走 create-skill。

打 zip、升版本：用目标仓自己的 `governance/pack/pack.py` 和 `governance/scripts/sync_version.py`，不经过本包。
