# 版本控制与发版（governance/）

本目录由 **Skill 开发工具包（skill-devkit）** 初始化，给**这个 Skill 自己**升版本、写方案、打包用。不要把业务项目文件放进来。

| 子目录 | 用途 |
|---|---|
| `planning/` | 升级方案 AP。每周期 1 个：`upgrade-plan-v{版本}.md` |
| `change-requests/` | 用户准许执行后才建 CR |
| `impact-analysis/` | 影响分析 |
| `regression-reports/` | 回归报告 |
| `baselines/` | 已发布版本的快照 `baselines/{版本}/`。初始化时为空，首发后再拷 |
| `review-checklists/` | 发布核对 |
| `templates/` | AP / CR / RR 空模板 |
| `pack/` | 打包 |
| `scripts/` | 版本号同步 |

Git 仓库在**上一级根目录**（`.git`），不在本文件夹里。

根目录 `VERSION` 才是版本号；改版本先改那里，再跑：

```
python governance/scripts/sync_version.py
python governance/pack/pack.py --skill-root .
```

`governance/` 默认不打进分发包。新仓默认没有工作区 schema，不需要 `migrations/`；真要给终端用户迁数据时再加。
