# 运动类积木块 (Motion)

> 参考文件：`references/blocks-motion.md` | 共 18 个积木块

运动类积木块控制角色在舞台上的位置、方向和旋转。

## 坐标系统

- 舞台范围：x ∈ [-240, 240]，y ∈ [-180, 180]
- 中心点：(0, 0)
- 方向：0° = 上，90° = 右，180° = 下，-90° = 左

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `motion_movesteps` | 移动 N 步 | INPUT: `STEPS` |
| `motion_turnright` | 右转 N 度 | INPUT: `DEGREES` |
| `motion_turnleft` | 左转 N 度 | INPUT: `DEGREES` |
| `motion_pointindirection` | 面向方向 | FIELD: `DIRECTION` |
| `motion_pointtowards` | 面向... | INPUT: `TOWARDS`（可引用鼠标指针或其他角色） |
| `motion_gotoxy` | 移动到 x: y: | INPUTS: `X`, `Y` |
| `motion_goto` | 移动到... | INPUT: `TO`（鼠标指针/随机位置/角色名） |
| `motion_glidesecstoxy` | 滑行 N 秒到 x: y: | INPUTS: ` SECS`, `X`, `Y` |
| `motion_glideto` | 滑行 N 秒到... | INPUTS: `SECS`, `TO` |
| `motion_changexby` | x 增加 N | INPUT: `DX` |
| `motion_setx` | 设置 x 为 N | INPUT: `X` |
| `motion_changeyby` | y 增加 N | INPUT: `DY` |
| `motion_sety` | 设置 y 为 N | INPUT: `Y` |
| `motion_ifonedgebounce` | 碰到边缘反弹 | 无参数 |
| `motion_setrotationstyle` | 设置旋转方式 | FIELD: `STYLE` |
| `motion_xposition` | x 坐标 | reporter，返回当前 x |
| `motion_yposition` | y 坐标 | reporter，返回当前 y |
| `motion_direction` | 方向 | reporter，返回当前方向 |

## 字段值

### motion_pointindirection
- `DIRECTION`: `["90", null]` (右), `["0", null]` (上), `["-90", null]` (左), `["180", null]` (下)

### motion_setrotationstyle
- `STYLE`: `["左右翻转", null]`, `["不旋转", null]`, `["任意旋转", null]`

### motion_goto / motion_glideto 的 TO 输入
- `[1, "_mouse_"]` — 鼠标指针
- `[1, "_random_"]` — 随机位置
- `[1, "角色名"]` — 指定角色

## JSON 示例

### 移动 N 步
```json
{
  "block": {
    "opcode": "motion_movesteps",
    "next": null,
    "parent": "prev",
    "inputs": {
      "STEPS": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 面向鼠标指针
```json
{
  "block": {
    "opcode": "motion_pointtowards",
    "next": null,
    "parent": "prev",
    "inputs": {
      "TOWARDS": [1, "_mouse_"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 滑行到随机位置
```json
{
  "block": {
    "opcode": "motion_glidesecstoxy",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SECS": [1, [4, "1"]],
      "X": [1, [4, "0"]],
      "Y": [1, [4, "0"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 碰到边缘反弹
```json
{
  "block": {
    "opcode": "motion_ifonedgebounce",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 设置旋转方式为左右翻转
```json
{
  "block": {
    "opcode": "motion_setrotationstyle",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "STYLE": ["左右翻转", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 使用 Reporter（x 坐标）
```json
{
  "block": {
    "opcode": "motion_xposition",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
Reporter 积木块作为输入时使用 `[1, "blockId"]` 嵌套引用。
