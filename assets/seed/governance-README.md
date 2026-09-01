# 版本控制与发版（governance/）

skill-devkit 初始化时写入。之后**本仓自己**升版本、打基线、记升级、打包。不要把业务项目文件放进来。不必再调用 skill-devkit。

Agent 改本 Skill 时先读：`rules/skill-governance.md`。

| 子目录 | 用途 |
|---|---|
| `rules/` | 变更治理提示词（本仓后续流程的正文） |
| `planning/` | 升级方案 AP。每周期 1 个：`upgrade-plan-v{版本}.md` |
| `change-requests/` | 用户准许执行后才建 CR。`CR-000-init` 是初始化出生证明，不要删 |
| `impact-analysis/` | 影响分析 |
| `regression-reports/` | 回归报告 |
| `baselines/` | 已发布版本快照 `baselines/{版本}/`，只增不改 |
| `migrations/` | 升级记录 `upgrade-to-{版本}.md` |
| `review-checklists/` | 发布核对 |
| `templates/` | AP / CR / IA / RR / upgrade-to 空模板 |
| `pack/` | 打包 |
| `scripts/` | 版本同步、基线快照、发布审计 |

Git 仓库在**上一级根目录**（`.git`），不在本文件夹里。根目录 `VERSION` 才是版本号。

```
python governance/scripts/sync_version.py
python governance/scripts/snapshot_baseline.py
python governance/scripts/audit_release.py
python governance/pack/pack.py --skill-root .
powershell -File governance/dev.ps1 pack
powershell -File governance/dev.ps1 release
```

`governance/` 默认不打进分发包。新仓默认没有工作区 schema；真要给终端用户迁数据时再加。
