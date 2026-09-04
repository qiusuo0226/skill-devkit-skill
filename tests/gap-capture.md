# 缺口捕捉回归

| 编号 | 类型 | 输入 | 期望 |
|---|---|---|---|
| G1 | 正 | 「这是 skill 的问题，记成升级需求：……」 | 写出 `outputs/skill-gaps/SG-*-需求-*.md`；告知路径+记了什么；不改 `SKILL.md`；不问要不要记 |
| G2 | 正 | 同一痛点再补一句 | 原位更新，不新建号 |
| G3 | 正 | 当前版本已包含后再记 | 旧稿 deprecated |
| N11 | 反 | 记缺口后直接改 `SKILL.md` | 禁止 |
| N12 | 反 | 无明示口令的不满 | 不落缺口文 |
| X1 | 正 | 三脚本经 `pack_exclude.py` 加载 | dirs/files/exts 相等，且 ini 含 `outputs`；audit 断言 pack.py `load_sets` 与 `load_excludes` 一致 |
| X2 | 正 | 已有 `outputs/skill-gaps/*.md` 时 snapshot + audit + pack dry-run | `audit_release.py` 退出码 0；基线与 dry-run 不含 `outputs/` |
