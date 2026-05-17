# LEGO 扩展积木块 (LEGO MINDSTORMS / SPIKE Extension)

> 参考文件：`references/blocks-lego.md` | 共 12+ 个积木块

LEGO 扩展支持 LEGO MINDSTORMS EV3 和 LEGO Education SPIKE Prime。

需要在 project.json 的 `extensions` 数组中包含 `"ev3"` 或 `"wedo2"`。

## LEGO MINDSTORMS EV3

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `ev3_motorTurnClockwise` | 马达 ... 顺时针转动 N 秒 | FIELD: `MOTOR_PORT`, INPUT: `TIME` |
| `ev3_motorTurnCounterClockwise` | 马达 ... 逆时针转动 N 秒 | FIELD: `MOTOR_PORT`, INPUT: `TIME` |
| `ev3_motorSetPower` | 将马达 ... 功率设为 N | FIELD: `MOTOR_PORT`, INPUT: `POWER` |
| `ev3_motorGetSpeed` | 马达 ... 速度 | FIELD: `MOTOR_PORT` (reporter) |
| `ev3_motorStop` | 停止马达 ... | FIELD: `MOTOR_PORT` |
| `ev3_whenButtonPressed` | 当 EV3 按钮被按下 | 事件 |
| `ev3_whenDistanceLessThan` | 当距离小于 N | INPUT: `DISTANCE` |
| `ev3_whenBrightnessLessThan` | 当亮度小于 N | INPUT: `BRIGHTNESS` |
| `ev3_buttonPressed` | EV3 按钮被按下? | reporter |
| `ev3_getDistance` | 距离 | reporter |
| `ev3_getBrightness` | 亮度 | reporter |
| `ev3_beep` | 鸣响 N 秒 | INPUT: `DURATION` |

## LEGO Education SPIKE Prime / Essential

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `wedo2_motorOn` | 开启马达 ... | FIELD: `MOTOR_PORT` |
| `wedo2_motorOff` | 关闭马达 ... | FIELD: `MOTOR_PORT` |
| `wedo2_motorOnFor` | 开启马达 ... N 秒 | FIELD: `MOTOR_PORT`, INPUT: `DURATION` |
| `wedo2_motorPower` | 将马达 ... 功率设为 N | FIELD: `MOTOR_PORT`, INPUT: `POWER` |
| `wedo2_motorDirection` | 将马达 ... 方向设为 ... | FIELD: `MOTOR_PORT`, `DIRECTION` |
| `wedo2_whenDistance` | 当距离 ... N | FIELD: `OP`, INPUT: `REFERENCE` |
| `wedo2_whenTilted` | 当向 ... 倾斜 | FIELD: `DIRECTION` |
| `wedo2_getDistance` | 距离 | reporter |
| `wedo2_isTilted` | 向 ... 倾斜? | FIELD: `DIRECTION` |
| `wedo2_getTiltAngle` | 向 ... 倾斜角度 | FIELD: `DIRECTION` (reporter) |
| `wedo2_playNoteFor` | 演奏音符 ... 拍 | INPUTS: `NOTE`, `DURATION` |

## 字段值

### EV3 马达端口 (MOTOR_PORT)
- `["A", null]` — 端口 A
- `["B", null]` — 端口 B
- `["C", null]` — 端口 C
- `["D", null]` — 端口 D

### WeDo 马达端口
- `["motor", null]` — 马达

### WeDo 马达方向 (DIRECTION)
- `["clockwise", null]` — 顺时针
- `["counter-clockwise", null]` — 逆时针
- `["this way", null]` — 这个方向
- `["that way", null]` — 那个方向
- `["reverse", null]` — 反转

### WeDo 倾斜方向
- `["up", null]` — 上
- `["down", null]` — 下
- `["left", null]` — 左
- `["right", null]` — 右
- `["any", null]` — 任意

### WeDo 距离比较 (OP)
- `["<", null]` — 小于
- `[">", null]` — 大于

## JSON 示例 (EV3)

### 马达 A 顺时针转 1 秒
```json
{
  "block": {
    "opcode": "ev3_motorTurnClockwise",
    "next": null,
    "parent": "prev",
    "inputs": { "TIME": [1, [4, "1"]] },
    "fields": { "MOTOR_PORT": ["A", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 马达 B 功率设为 50
```json
{
  "block": {
    "opcode": "ev3_motorSetPower",
    "next": null,
    "parent": "prev",
    "inputs": { "POWER": [1, [4, "50"]] },
    "fields": { "MOTOR_PORT": ["B", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取距离传感器
```json
{
  "block": {
    "opcode": "ev3_getDistance",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 当距离小于 10
```json
{
  "block": {
    "opcode": "ev3_whenDistanceLessThan",
    "next": null,
    "parent": null,
    "inputs": { "DISTANCE": [1, [4, "10"]] },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

## JSON 示例 (WeDo 2.0)

### 开启马达
```json
{
  "block": {
    "opcode": "wedo2_motorOn",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": { "MOTOR_PORT": ["motor", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 关闭马达
```json
{
  "block": {
    "opcode": "wedo2_motorOff",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": { "MOTOR_PORT": ["motor", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取距离
```json
{
  "block": {
    "opcode": "wedo2_getDistance",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 当距离小于 50
```json
{
  "block": {
    "opcode": "wedo2_whenDistance",
    "next": null,
    "parent": null,
    "inputs": { "REFERENCE": [1, [4, "50"]] },
    "fields": { "OP": ["<", null] },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 当向上倾斜
```json
{
  "block": {
    "opcode": "wedo2_whenTilted",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "DIRECTION": ["up", null] },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 读取倾斜角度
```json
{
  "block": {
    "opcode": "wedo2_getTiltAngle",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "DIRECTION": ["up", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 演奏音符 60 一拍
```json
{
  "block": {
    "opcode": "wedo2_playNoteFor",
    "next": null,
    "parent": "prev",
    "inputs": {
      "NOTE": [1, [7, "60"]],
      "DURATION": [1, [4, "1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
