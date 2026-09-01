# pack/

把 Skill 打成分发包 zip。默认排除 `.git`、`governance/`、`tests/`、缓存和压缩包。

```
python governance/pack/pack.py --skill-root .
python governance/pack/pack.py --skill-root . --dry-run
python governance/pack/pack.py --skill-root . --output-dir <目录>
```

zip 名：`{displayName 品牌}-Skill-v{VERSION}.zip`。品牌取 `skill.json` 的 `displayName`（遇 `—` 或 `(` 截断）。版本优先读根目录 `VERSION`。
