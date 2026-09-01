# 发布核对

目标版本：

## 变更控制

- [ ] 有 AP，用户已同意执行
- [ ] 有 CR，目标可验证，没有混入无关改动
- [ ] 有 IA
- [ ] 有 RR（正 / 反 / 旧能力）

## 版本与记录

- [ ] 根目录 `VERSION`、`skill.json` 的 `version`、`CHANGELOG.md` 该版本段一致
- [ ] 已跑 `python governance/scripts/sync_version.py`
- [ ] 已写 `governance/migrations/upgrade-to-{版本}.md`
- [ ] 该版本 AP 已删除（思路在 CR / CHANGELOG / upgrade-to / 基线）

## 基线与打包

- [ ] `python governance/scripts/snapshot_baseline.py` 已生成且未改历史基线
- [ ] `python governance/pack/pack.py --skill-root . --dry-run` 不含 `governance/`、`.git/`、`AGENTS.md`
- [ ] `python governance/scripts/audit_release.py` 退出码 0

## Git

- [ ] 已提交
- [ ] tag 为 `v{版本}`（不擅自 push）
