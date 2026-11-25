# pairwise-flame-blackbody-volume

## 领域

游戏、图形与多媒体

## 主题

火焰体积与黑体色温

## 说明

定步长积分、温度速度耦合、黑体色温映射。

初始状态下 `graphics/flame_volume.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
