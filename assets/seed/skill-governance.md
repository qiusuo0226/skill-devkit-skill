# 本 Skill 开发仓的变更治理

本文件在 **skill-devkit 初始化时写入**，之后由本仓自己执行。不要再加载 skill-devkit。

当你要改本仓的 `SKILL.md` / `references/` / 升版本 / 打包 / 打基线 / 发版时：读本文件并按流程做。分发包不含 `governance/`，终端用户看不到本规则。

## 1. 先方案后改文件

禁止直接改 Skill 正文。即使用户说「直接改吧」，也必须先写出升级方案（AP）的 **AP-1～AP-7（缺一不可）**，等人确认后再动文件。写方案 / 你是 A 或 B 时整份加载 `upgrade-dual-agent.md`。

例外（可直接改，但必须记 CHANGELOG）：错别字、仅新增测试、仅新增模板且不改已有文件。

## 2. 强制流程

```
1. 写 AP：governance/planning/upgrade-plan-v{目标版本}.md（每周期 1 个；A 出方案，七章齐全）
2. 路径 H：用户说「同意执行」或「执行升级」（可无 B 节）
   或路径 B：新对话「你是 Agent B，审核该 AP」→ 文末追加 B 节 → 仍须用户「同意执行」
3. 建 CR：governance/change-requests/CR-YYYYMMDD-NNN.md（写明执行授权：人直接同意 / B 通过后人同意 / 人覆盖 B）
4. 建 IA：governance/impact-analysis/IA-YYYYMMDD-NNN.md
5. 按最小范围改文件
6. 回归（正 / 反 / 旧能力各至少 1 条）→ RR
7. 改根目录 VERSION → python governance/scripts/sync_version.py
8. 更新 CHANGELOG.md
9. 写升级记录：governance/migrations/upgrade-to-{版本}.md
10. python governance/scripts/audit_release.py 必须通过
11. 删除该版本 AP（含文末 B 审核节；内容已固化到 CR / CHANGELOG / 基线 / upgrade-to，不另存 B 副本）
12. python governance/scripts/snapshot_baseline.py（基线只增不改）
13. python governance/pack/pack.py --skill-root .
14. git tag v{版本}（有 git 才做；不擅自 push）
```

未确认方案前禁止改 `SKILL.md`、`references/`、`skill.json`。

## 3. AP 七章（缺一不可）

模板：`governance/templates/upgrade-plan.md`。必须含：变更概述、影响点表、策略与被否决的替代方案、修改范围清单、回归计划、风险与回滚、版本影响。

命名只能是 `upgrade-plan-v{版本}.md`。禁止拆成多个 AP。

## 4. 单一目标

一次变更只服务一个可验证目标。新功能、修复、重构混在一起必须拆 CR。

## 5. 核心契约

未经用户明确批准不得改：`SKILL.md`、`skill.json`。改这两项视为契约变更，须全量回归。

## 6. 版本号

根目录 `VERSION` 是唯一可读源。先改它，再跑 `sync_version.py`。

| 变更类型 | 提升 |
|---|---|
| 核心契约或行为不兼容 | Major 或 Minor |
| 新能力或新目录 | Minor |
| 规则修复 | Patch |
| 仅测试或模板 | Patch |

用户开口不必报「升到几」；读当前 `VERSION` 按上表拟定，写入 AP。新仓从初始化的 `0.1.0` 起。

## 7. CHANGELOG

每个发布版本必须有一段，写清：目标、改了哪些文件、测了什么、怎么回滚。

## 8. 基线控制

`governance/baselines/{版本}/` 是该版本**分发包内容**的快照（不含 `governance/`、`.git/`）。只增不改：已有目录禁止覆盖或回填。回滚对照上一版基线。

初始化时已有 `0.1.0` 基线。之后每发一版打一版。

## 9. 升级记录

每次发布必须同时留下：

| 记录 | 位置 |
|---|---|
| CHANGELOG 段 | 根目录 `CHANGELOG.md` |
| CR | `governance/change-requests/` |
| IA | `governance/impact-analysis/` |
| RR | `governance/regression-reports/` |
| upgrade-to | `governance/migrations/upgrade-to-{版本}.md` |
| git tag | `v{版本}` |

`upgrade-to` 写给「已经在用上一版的人」：这版改了什么、要不要重装、工作区要不要动手。本仓默认无工作区 schema；没有迁移就写「无需迁移」。

出生证明是 `CR-000-init` **或** `CR-000-adopt`，以及对应的 `upgrade-to`，禁止删除。

## 10. 打包发包

```
python governance/pack/pack.py --skill-root .
python governance/pack/pack.py --skill-root . --dry-run
```

zip 名 `{name}-Skill-v{VERSION}.zip`（英文名，不用中文显示名）。排除名单以 `governance/pack.ini` 为准。默认不包含 `.git/`、`governance/`、`tests/`、`AGENTS.md`。

## 11. 发布审计

```
python governance/scripts/audit_release.py
```

失败禁止发版。再勾 `governance/review-checklists/release-checklist.md`。

## 12. 回滚

回归失败：停，建议回到上一版基线，不要叠临时补丁。

## 13. 根目录白名单

根上只允许：`SKILL.md`、`skill.json`、`VERSION`、`CHANGELOG.md`、`README.md`、`LICENSE`、`AGENTS.md`、`.gitignore`、`.git/`、`assets/`、`governance/`、`references/`、`scripts/`、`tests/`、`outputs/`。

`outputs/` 是运行时生成物目录（懒建）。其下 `skill-gaps/` 稿件不须每次写入 AP-4。禁止把缺口稿散落在根上。新的其它根文件须先写进 AP-4。收编前已存在的额外根文件可保留，必须写进出生 CR。

## 14. 对助手怎么说

```
按 governance/rules/skill-governance.md 处理，不要直接改。先出 AP。
写升级方案 / 你是 Agent A / 你是 Agent B 时同时读 governance/rules/upgrade-dual-agent.md。
同意执行或执行升级才改技能。
```
