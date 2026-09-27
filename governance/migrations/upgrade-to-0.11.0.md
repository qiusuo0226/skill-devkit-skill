# upgrade-to-0.11.0

| 字段 | 值 |
|---|---|
| 目标版本 | 0.11.0 |
| 上一版本 | 0.10.1 |
| CR | CR-20260927-001～006 |
| 日期 | 2026-09-27 |
| git | tag `v0.11.0`（对照 `v0.10.1`） |

## 这版改了什么

- **打包排除修好了**：目标仓 `governance/pack/pack.py` 之前找不到 `governance/scripts/pack_exclude.py`，改了 `governance/pack.ini` 也不生效，打包时出 `WARN: pack_exclude.py missing`。新种子已修；发版检查多一条，退回内置名单就不过。
- **两条新检查**（`validate_skill.py`，发版检查会先跑它）：`SKILL.md`、README、`skill.json` 三处触发说法必须一样；升版后安装包里不许再出现上一版号或旧安装包名（`CHANGELOG.md`、`skill.json` 的版本历史和 `schemaVersion` 不算）。
- **检查器自测**：新测试 `tests/test_checker_mutations.py`。每条检查规则都故意弄坏一处，必须由那一条规则报出来；以后加了规则不配用例，冒烟就不过。
- **回归固定四问**：每版回归报告都答「装得上 / 唤得起 / 答得对 / 说得清」，题和输入不换，旁边写上一版结果。
- **可信度标签**：写方案、B 审核时每条结论标「已验证 / 推断 / 参考」。推断只能放进回归计划当待验证项。
- **中文 Windows**：发版检查读子进程输出按 UTF-8，不再按 GBK。

## 使用者要做什么

- [x] 无需迁移工作区
- [ ] 要用新种子：用新 zip / 新目录替换已安装的本包。新初始化 / 新收编自带上面全部能力
- [ ] 已建好的技能仓**不会**自动改。在那个仓按它自己的 `skill-governance.md` 单独升级（改 `governance/` 脚本不在 §1 例外里，建议出一份 Patch 方案）

### 已建好的仓怎么补

**只修打包排除（0.8.0～0.10.1 初始化的仓都建议做）**：

1. 打开 `governance/pack/pack.py`，把
   `here.parents[2] / "governance" / "scripts" / "pack_exclude.py",`
   改成
   `here.parent / "scripts" / "pack_exclude.py",`
   或整份换成本版 `assets/seed/pack.py`。
2. 跑 `python governance/pack/pack.py --skill-root . --dry-run`：不再出 `WARN: pack_exclude.py missing`。
3. 如果之前改过 `pack.ini`，对一下以前打出的 zip 是否多带了本该排除的文件。

已知仓（2026-09-27 实查）：

| 仓 | 情况 | 要做 |
|---|---|---|
| personal-graph | `governance/pack/pack.py` 第 25 行带旧路径，dry-run 出 WARN；`pack.ini` 仍是默认值 | 按上面 1～2 修。之前的包内容不受影响（默认 ini 与内置名单相同） |
| session-handoff | pack.py 是 0.8.0 以前的版本，没有 `pack.ini` / `pack_exclude.py` | 不受这个缺陷影响；要用 `pack.ini` 与新检查就整套补种子（见下）。预演：换上新 validate 后「no previous version…」报 `examples/07-装到助手里试用.md` 第 5 行的「0.1.0」（当前 0.2.0），要改这句 |

**要新检查与自测**：

1. 拷本版 `assets/seed/validate_skill.py`、`audit_release.py`、`pack_exclude.py` 到 `governance/scripts/`；`assets/seed/pack.py` 到 `governance/pack/`；没有 `governance/pack.ini` 就拷 `assets/seed/pack.ini`。
2. 拷 `assets/seed/test_checker_mutations.py`、`test_validate_skill.py`、`test_pack_exclude.py` 到 `tests/`（`run_smoke.py` 没有也拷）。
3. 拷模板 `assets/templates/RR-template.md`、`upgrade-plan.md` 到 `governance/templates/`，`release-checklist.md` 到 `governance/review-checklists/`。
4. `skill-governance.md` §2 第 6 步、§3，`upgrade-dual-agent.md` §2 第 5 步、§4 #3 的新句手工并入；`tests/README.md` 补「固定四问」表并填实固定输入。
5. 跑 `python governance/scripts/audit_release.py`。「trigger phrases consistent」不过：让 README 有一行「触发：」或「同义口令：」，与 `SKILL.md` description 的触发段同集（只按「、」分隔）；`skill.json` description 同样。「no previous version…」不过：把分发文件里残留的上一版号改掉。2026-09-27 预演：personal-graph 换新种子后 audit 全 PASS；session-handoff 触发三处同集，只差上面那一句示例。

## 不兼容说明

- 新 `validate_skill.py` 对「三处触发不一致」「分发集留有上一版号」报 FAIL。以前能过的仓换上新脚本后可能不过，按上面第 5 步补。
- audit 转印的 validate 输出改为缩进两格。只影响读输出的人或脚本。

## 回滚

`git checkout v0.10.1`。本包对照物是 git tag，不是 `governance/baselines/`。不要在半套 0.11.0 上打补丁。
