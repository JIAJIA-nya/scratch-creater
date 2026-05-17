# micro:bit 扩展积木块 (micro:bit Extension)

> 参考文件：`references/blocks-microbit.md` | 共 16 个积木块

micro:bit 扩展允许 Scratch 与 BBC micro:bit 微控制器交互。

需要在 project.json 的 `extensions` 数组中包含 `"microbit"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `microbit_whenButtonPressed` | 当 ... 键被按下 | FIELD: `BTN` |
| `microbit_buttonIsPressed` | ... 键被按下? | FIELD: `BTN` |
| `microbit_whenGesture` | 当 ... | FIELD: `GESTURE` |
| `microbit_displaySymbol` | 显示 ... | FIELD: `SYMBOL` |
| `microbit_displayText` | 显示文本 ... | INPUT: `TEXT` |
| `microbit_displayClear` | 清空屏幕 | 无参数 |
| `microbit_whenTilted` | 当向 ... 倾斜 | FIELD: `DIRECTION` |
| `microbit_isTilted` | 向 ... 倾斜? | FIELD: `DIRECTION` |
| `microbit_getTiltAngle` | 向 ... 倾斜角度 | FIELD: `DIRECTION` |
| `microbit_whenPinConnected` | 当引脚 ... 被连接 | FIELD: `PIN` |
| `microbit_digitalWritePin` | 将数字引脚 ... 设为 ... | FIELD: `PIN`, INPUT: `VALUE` |
| `microbit_analogWritePin` | 将模拟引脚 ... 设为 ... | FIELD: `PIN`, INPUT: `VALUE` |
| `microbit_digitalReadPin` | 读取数字引脚 ... | FIELD: `PIN` (reporter) |
| `microbit_analogReadPin` | 读取模拟引脚 ... | FIELD: `PIN` (reporter) |
| `microbit_getLightLevel` | 光线强度 | reporter |
| `microbit_getTemperature` | 温度 | reporter |

## 字段值

### microbit_whenButtonPressed / microbit_buttonIsPressed 的 BTN
- `["a", null]` — A 键
- `["b", null]` — B 键
- `["any", null]` — 任意键

### microbit_whenGesture 的 GESTURE
- `["shake", null]` — 摇晃
- `["freefall", null]` — 自由落体
- `["tilt up", null]` — 向上倾斜
- `["tilt down", null]` — 向下倾斜
- `["tilt left", null]` — 向左倾斜
- `["tilt right", null]` — 向右倾斜
- `["face up", null]` — 正面朝上
- `["face down", null]` — 正面朝下

### microbit_whenTilted / microbit_isTilted / microbit_getTiltAngle 的 DIRECTION
- `["front", null]` — 前
- `["back", null]` — 后
- `["left", null]` — 左
- `["right", null]` — 右
- `["up", null]` — 上
- `["down", null]` — 下

### microbit_displaySymbol 的 SYMBOL
- `["heart", null]` — ❤
- `["small heart", null]` — 小❤
- `["yes", null]` — ✓
- `["no", null]` — ✗
- `["happy", null]` — 😊
- `["sad", null]` — 😢
- `["confused", null]` — 😕
- `["angry", null]` — 😠
- `["asleep", null]` — 😴
- `["surprised", null]` — 😮
- `["silly", null]` — 😜
- `["fabulous", null]` — 😎
- `["meh", null]` — 😐
- `["t-shirt", null]` — T恤
- `["roller skate", null]` — 轮滑
- `["duck", null]` — 鸭子
- `["house", null]` — 房子
- `["tortoise", null]` — 乌龟
- `["butterfly", null]` — 蝴蝶
- `["stick figure", null]` — 火柴人
- `["ghost", null]` — 幽灵
- `["sword", null]` — 剑
- `["giraffe", null]` — 长颈鹿
- `["skull", null]` — 骷髅
- `["umbrella", null]` — 雨伞
- `["snake", null]` — 蛇

### microbit_whenPinConnected 的 PIN
- `["0", null]` — 引脚 0
- `["1", null]` — 引脚 1
- `["2", null]` — 引脚 2

## JSON 示例

### 当 A 键被按下
```json
{
  "block": {
    "opcode": "microbit_whenButtonPressed",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "BTN": ["a", null] },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### A 键被按下？
```json
{
  "block": {
    "opcode": "microbit_buttonIsPressed",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "BTN": ["a", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 当被摇晃
```json
{
  "block": {
    "opcode": "microbit_whenGesture",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "GESTURE": ["shake", null] },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 显示心形
```json
{
  "block": {
    "opcode": "microbit_displaySymbol",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": { "SYMBOL": ["heart", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 显示文本
```json
{
  "block": {
    "opcode": "microbit_displayText",
    "next": null,
    "parent": "prev",
    "inputs": { "TEXT": [1, [10, "Hello!"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 清空屏幕
```json
{
  "block": {
    "opcode": "microbit_displayClear",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 当向前倾斜
```json
{
  "block": {
    "opcode": "microbit_whenTilted",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "DIRECTION": ["front", null] },
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
    "opcode": "microbit_getTiltAngle",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "DIRECTION": ["front", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 设置数字引脚
```json
{
  "block": {
    "opcode": "microbit_digitalWritePin",
    "next": null,
    "parent": "prev",
    "inputs": { "VALUE": [1, [4, "1"]] },
    "fields": { "PIN": ["0", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取模拟引脚
```json
{
  "block": {
    "opcode": "microbit_analogReadPin",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": { "PIN": ["0", null] },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取光线强度
```json
{
  "block": {
    "opcode": "microbit_getLightLevel",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取温度
```json
{
  "block": {
    "opcode": "microbit_getTemperature",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
