# baselines/

已发布版本的快照。每个版本一个目录：`{版本}/`。内容 = 当时分发包会带上的文件（不含 `governance/`、`.git/`）。

**只增不改。** 目录一旦写成，禁止覆盖、回填、删改。回滚时对照上一版目录。

初始化已写入 `0.1.0/`。之后发版跑：

```
python governance/scripts/snapshot_baseline.py
```

当前 `VERSION` 对应目录已存在则脚本拒绝覆盖。
