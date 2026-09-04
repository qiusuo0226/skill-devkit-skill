# 核心门禁（skill-devkit）

## 身份

本包做两件一次流程，然后退场：

1. **初始化**：在空文件夹或空 git 仓写入版本控制、冻结基线、升级记录、变更门禁、触发词、打包与审计。半套落盘走恢复，见 `01-init.md`。
2. **收编**：已有 `SKILL.md`、尚无本包完成态时，只补缺失骨架，不改技能正文。半套收编走恢复，见 `02-adopt.md`。

之后由目标仓的 `governance/rules/skill-governance.md` 执行。禁止当升级引擎，禁止给终端用户做自动升级，禁止当 ChronoPM 用，禁止写业务 `ai/`。禁止当常驻「记缺口」工具（缺口规则写在目标仓）。

## 完成 / 半套（E 先于 C/D）

种子痕迹（三选一）：`governance/change-requests/CR-000-init.md` 或 `CR-000-adopt.md`；`governance/rules/skill-governance.md`；`governance/pack/pack.py`。

非空版本基线目录：`governance/baselines/` 下名称像版本号的子目录，且目录内至少有一个文件。`baselines/README.md` 不算。空版本目录不算完成。

| 状态 | 磁盘 | 动作 |
|---|---|---|
| E 已规范 | 任一种子痕迹 + 任一非空版本基线目录 | 停止。含 VERSION 领先基线、删了 `rules/` 但痕迹与基线仍在 |
| C 半套初始化 | 种子痕迹 + 无非空版本基线目录 | `01-init.md` 恢复节 |
| D 半套收编 | 用户 `SKILL.md` + 种子痕迹 + 无非空版本基线目录 | `02-adopt.md` 恢复节 |

## 确认工作区

| 工作区 | 加载 |
|---|---|
| 空（见 `01-init.md` §2） | `01-init.md` |
| 半套初始化（C） | `01-init.md` 恢复节 |
| 有 `SKILL.md`、无种子痕迹 | 初始化口令 → `01-init.md` §2 指路收编；收编口令 → `02-adopt.md` |
| 半套收编（D） | `02-adopt.md` 恢复节 |
| 已规范（E） / 非空非技能 / 升级 / Agent A 或 B | 停止，不要写盘。已规范仓读它自己的治理文件 |

探测见 `references/03-skill-roots.md`。

## 未确认不写盘

用户确认问答清单前禁止写盘。

## 与 create-skill

`create-skill` 只脚手架轻量 `SKILL.md`，不生成本包这套开发基线。初始化不要改走 create-skill。无规范的已有 `SKILL.md` 走收编，不要当空仓覆盖。

打 zip、升版本、打基线、审计：用目标仓 `governance/` 里的脚本，不经过本包。
