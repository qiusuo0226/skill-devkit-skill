# 升级双路径（A 出方案 / B 审核 / 人执行）

本文件由开发仓在「写升级方案 / 你是 Agent A / 你是 Agent B / 审核 AP」时**整份加载**。分发包不含本文件。总流程仍以 `skill-governance.md` 为准。

口令权威在 `skill-governance.md` §14。不要另编一套。

## 1. 角色

| 角色 | 做 | 不做 |
|---|---|---|
| **A** | 确认工作区；扫描；写七章 AP 到 `governance/planning/upgrade-plan-v{版本}.md` | 不改技能正文；不建 CR |
| **B** | 独立实读文件；只在该 AP **文末追加** `## B{N} 审核结果` | 不改 A 正文；不执行 |
| **人** | 「同意执行」或「执行升级」才改技能 | — |

用户不必报目标版本。A 读根 `VERSION` 拟定。

## 2. Agent A

触发：升级这个 skill / 写一份升级方案 / 你是 Agent A / 先出方案再改。

1. **工作区确认**：展示根路径、`VERSION`、git HEAD（无 git 则写无）。等人确认后再扫描写盘。
2. 扫描 `SKILL.md`、`references/`、`VERSION`、`skill.json`、`governance/planning/`。若有 `outputs/skill-gaps/` 且 `status=draft` 的稿，必须读并在 AP-1 引用 `sg_id`。缺口稿不是执行许可。
3. 方案只能叫 `governance/planning/upgrade-plan-v{拟定版本}.md`。每周期一份。空模板 `governance/templates/upgrade-plan.md` 不许改来凑合。
4. 七章缺一 = 失败，不得请人同意。文首可加工作区快照与需求照抄，不得替代七章。
5. 写完停止，同时给出两条路：

> 方案在 `governance/planning/upgrade-plan-vX.md`。
> - 直接做：回复「同意执行」或「执行升级」。
> - 先审核：新开对话说「你是 Agent B，审核 governance/planning/upgrade-plan-vX.md」。

## 3. 路径 H · 人直接执行

人说「同意执行」「执行升级」「按这个执行」。不要求已有 B 节。进入 `skill-governance.md` §2 从建 CR 起。CR 写：`执行授权: 人直接同意（未经 B）`。

## 4. 路径 B · 审核后再等人

触发：你是 Agent B / B1 / B2 / 审核这份升级方案 / 审核 upgrade-plan-vX.md。

1. 核对工作区与 A 快照同一仓、同一 `VERSION`/git；不一致则停止，不写审核节。
2. 独立实读 AP-4 列出的文件，禁止只读 AP。
3. 只在该 AP 文末追加 `## B{N} 审核结果`（未编号默认 B1）。禁止改 A 正文、其他 B 节。
4. 不得执行、不得建 CR、不得改 `SKILL.md`。
5. 审核节缺下列任一小节 = 失败：

| 小节 | 内容 |
|---|---|
| #0 | 工作空间核对 |
| #1 | 实读文件清单 |
| #2 | 七章是否齐全；AP-4 与实仓是否对得上 |
| #3 | 阻塞问题（无则写「无」） |
| #4 | 四档之一：通过-可执行 / 通过-待修订 / 修订-需再审 / 重做-需再审 |

写完后告诉人：前两档可回复「同意执行」；后两档应让 A 修订——除非人明确覆盖。

## 5. 人覆盖 B

B 结语为「修订-需再审」或「重做-需再审」，人仍说「同意执行」：执行。CR 写 `执行授权: 人覆盖 B（B 结语=…）`。A/B 不得拦人。

## 6. 硬闸

1. 同一对话已经以 A 出过该 AP → 禁止转 B。请新开对话把路径交给 B。
2. 没有 AP 文件 → B 停止。
3. A 在人同意前改技能正文 = 失败。
4. B 改了 A 正文 = 失败，从 git 恢复 AP 后重审。
5. 发版后删除该 AP（含文末 B 节）。B 节已固化到 CR / CHANGELOG / 基线 / upgrade-to，不另存副本。
