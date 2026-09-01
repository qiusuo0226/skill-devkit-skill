# 核心门禁（skill-devkit）

## 身份

本包只做一件事：在**空文件夹或空 git 仓**初始化 Skill 开发仓（代码 + 根上 git + `governance/` 里的版本控制、基线、升级记录、打包，以及后续提示词）。

写完即退场。之后由目标仓的 `governance/rules/skill-governance.md` 执行，本包不再识别或接管。禁止当升级引擎，禁止给终端用户做自动升级，禁止当 ChronoPM 用，禁止写业务 `ai/`。

## 确认工作区

工作区必须是空的（见 `01-init.md` §2）。加载 `01-init.md`。

非空、已有 `SKILL.md`、或用户在说升级 → 停止，不要写盘。

## 未确认不写盘

用户确认问答清单前禁止写盘。

## 与 create-skill

`create-skill` 只脚手架轻量 `SKILL.md`，不生成本包这套开发基线。初始化不要改走 create-skill。

打 zip、升版本、打基线、审计：用目标仓 `governance/` 里的脚本，不经过本包。
