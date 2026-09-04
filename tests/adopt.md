# 收编回归

| 编号 | 类型 | 输入 | 期望 |
|---|---|---|---|
| P1 | 正 | 仅有手写 `SKILL.md` + `references/foo.md`，说「收编这个 skill」 | 确认后出现 `VERSION`、`governance/`、基线、`CR-000-adopt`；`SKILL.md` 与 `foo.md` 正文不变；dry-run 无 `governance/` |
| P2 | 正 | `skill.json` version `1.2.0`、无 `VERSION` | 写入 `VERSION=1.2.0`，基线目录名 `1.2.0` |
| N1 | 反 | 已有 `governance/rules/skill-governance.md` | 停止、不写盘 |
| N2 | 反 | 无 `SKILL.md` 的非空目录 | 停止 |
| N3 | 反 | 空目录说收编 | 停止，指路初始化 |
| N4 | 反 | 有 `governance/` 无指纹 | 停止 |
| N5 | 反 | 工作区在已探测的助手技能安装目录下 | 停止 |
| P3 | 正 | 半套收编：用户 SKILL.md + 种子痕迹 + 无非空版本基线 | 不判已规范、不判来源不明；不改正文；补缺并续跑 |
| N6 | 反 | 对无规范技能说「初始化」 | 不写盘，指路收编 |
| N7 | 反 | `VERSION` 与 `skill.json` version 不一致 | 停止、不写盘 |
| R1 | 旧 | 空文件夹「初始化 skill」 | 与 0.6.4 相同问答与落盘（结束语可多一句） |
| R2 | 旧 | 非空非技能「初始化」 | 仍停止 |
| R3 | 旧 | 已规范仓说「升级」 | 本包仍停止 |
