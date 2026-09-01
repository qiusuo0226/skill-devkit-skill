# pack/

把 Skill 打成分发包 zip。默认排除 `.git`、`governance/`、`tests/`、`AGENTS.md`、缓存和压缩包。

```
python governance/pack/pack.py --skill-root .
python governance/pack/pack.py --skill-root . --dry-run
python governance/pack/pack.py --skill-root . --output-dir <目录>
```

zip 名：`{name}-Skill-v{VERSION}.zip`。`name` 取 `skill.json` 的英文名（小写字母、数字、连字符），不用中文显示名。版本优先读根目录 `VERSION`。
