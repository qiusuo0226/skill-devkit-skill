# 核心门禁（skill-devkit）

## 身份

本包做两件一次流程，然后退场：

1. **初始化**：在空文件夹或空 git 仓写入版本控制、冻结基线、升级记录、变更门禁、触发词、打包与审计。
2. **收编**：已有 `SKILL.md`、尚无本包指纹时，只补缺失骨架，不改技能正文。

之后由目标仓的 `governance/rules/skill-governance.md` 执行。禁止当升级引擎，禁止给终端用户做自动升级，禁止当 ChronoPM 用，禁止写业务 `ai/`。禁止当常驻「记缺口」工具（缺口规则写在目标仓）。

## 确认工作区

| 工作区 | 加载 |
|---|---|
| 空（见 `01-init.md` §2） | `01-init.md` |
| 有 `SKILL.md`、无 `governance/rules/skill-governance.md` | 初始化口令 → `01-init.md` §2 指路收编；收编口令 → `02-adopt.md` |
| 已有指纹 / 非空非技能 / 升级 / Agent A 或 B | 停止，不要写盘。已规范仓读它自己的治理文件 |

## 未确认不写盘

用户确认问答清单前禁止写盘。

## 与 create-skill

`create-skill` 只脚手架轻量 `SKILL.md`，不生成本包这套开发基线。初始化不要改走 create-skill。无规范的已有 `SKILL.md` 走收编，不要当空仓覆盖。

打 zip、升版本、打基线、审计：用目标仓 `governance/` 里的脚本，不经过本包。
