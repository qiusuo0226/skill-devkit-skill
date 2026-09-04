# upgrade-to-0.8.0

| 字段 | 值 |
|---|---|
| 目标版本 | 0.8.0 |
| 上一版本 | 0.7.0 |
| CR | CR-20260904-001 |
| 日期 | 2026-09-04 |
| git | tag `v0.8.0`（对照 `v0.7.0`） |

## 这版改了什么

- **探测**：占用检查、收编「是否在助手安装目录」、试用拷贝共用 `references/03-skill-roots.md` / `scripts/discover_skill_roots.py`。可设 `SKILL_DEVKIT_SKILLS_DIRS`。
- **恢复**：初始化/收编写到一半可续跑。已规范仓（含 VERSION 领先基线、删了 rules/ 但痕迹与非空基线仍在）仍停。
- **pack.ini**：三脚本同读排除名单。新 init / 新 adopt 自带；已用 0.7.x 初始化的仓不会自动长出。
- **版权默认**：`git config user.name`，空则改口问「写谁」。
- **触发词**：description 收缩；同义全表在 `references/04-triggers.md`。
- **冒烟**：`tests/run_smoke.py`。本包根不跑 seed `audit_release.py`。

B1+B2+B3 审核（通过-待修订）已吸收进 AP 1.3 并执行。B4 结语「通过」：两条注意——`audit_release.py` 补「pack.py 与 audit 加载结果相等」断言；本记录与 CR 写明 B4。

## 使用者要做什么

- [x] 无需迁移工作区
- [ ] 要用新探测/恢复：用新 zip / 新目录替换已安装的本包
- [ ] 已用 0.7.x 初始化过的仓**不会**自动长出 pack.ini / 冒烟；要这些能力请手拷本版种子，勿对本包说升级（已规范仓会停）
- [ ] 新初始化 / 新收编的仓自带上述能力

## 不兼容说明

对本包说「初始化」时，半套落盘不再当普通非空一刀切停止。已规范仓行为与 0.7.0 相同（停止）。description 缩短后，极端生僻同义口令可能少一次自动命中；斜杠口令与路由句仍在。

## 回滚

`git checkout v0.7.0`。本包对照物是 git tag，不是 `governance/baselines/`。不要在半套 0.8.0 上打补丁。
