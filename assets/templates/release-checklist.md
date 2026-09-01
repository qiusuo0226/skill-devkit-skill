# 发布核对

目标版本：

- [ ] 根目录 `VERSION`、`skill.json` 的 `version`、`CHANGELOG.md` 最新段三者一致
- [ ] `SKILL.md` 有 `name` 和 `description`（description 含触发说法）
- [ ] `LICENSE` 存在
- [ ] `python governance/pack/pack.py --skill-root . --dry-run` 文件列表不含 `governance/`、`.git/`
- [ ] 若有 git：工作区已提交，tag 与版本号对应（`v{版本}`）
