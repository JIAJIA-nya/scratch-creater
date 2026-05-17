# 侦测类积木块 (Sensing)

> 参考文件：`references/blocks-sensing.md` | 共 18 个积木块

侦测类积木块用于检测碰撞、距离、用户输入、时间等信息。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `sensing_touchingobject` | 碰到 ... ? | INPUT: `TOUCHINGOBJECTMENU` |
| `sensing_touchingcolor` | 碰到颜色 ... ? | INPUT: `COLOR` |
| `sensing_coloristouchingcolor` | 颜色 ... 碰到 ... ? | INPUTS: `COLOR`, `COLOR2` |
| `sensing_distanceto` | 到 ... 的距离 | INPUT: `DISTANCETOMENU` |
| `sensing_askandwait` | 询问 ... 并等待 | INPUT: `QUESTION` |
| `sensing_answer` | 回答 | reporter |
| `sensing_keypressed` | 按下 ... 键? | INPUT: `KEY_OPTION` |
| `sensing_mousedown` | 按下鼠标? | reporter |
| `sensing_mousex` | 鼠标的 x 坐标 | reporter |
| `sensing_mousey` | 鼠标的 y 坐标 | reporter |
| `sensing_setdragmode` | 设置拖拽模式 | FIELD: `DRAG_MODE` |
| `sensing_loudness` | 响度 | reporter |
| `sensing_timer` | 计时器 | reporter |
| `sensing_resettimer` | 计时器归零 | 无参数 |
| `sensing_of` | ... 的 ... | INPUT: `OBJECT`, FIELD: `PROPERTY` |
| `sensing_current` | 当前的 ... | FIELD: `CURRENTMENU` |
| `sensing_dayssince2000` | 2000 年至今的天数 | reporter |
| `sensing_username` | 用户名 | reporter |
| `sensing_userid` | 用户 ID | reporter |
| `sensing_loud` | 响度 > 10? | reporter，返回布尔值 |

## 字段值

### sensing_touchingobject 的 TOUCHINGOBJECTMENU
- `["_mouse_", null]` — 鼠标指针
- `["_edge_", null]` — 边缘
- 或引用角色名

### sensing_distanceto 的 DISTANCETOMENU
- `["_mouse_", null]` — 鼠标指针
- 或引用角色名

### sensing_keypressed 的 KEY_OPTION
- `["空格", null]`, `["上箭头", null]`, `["下箭头", null]`, `["左箭头", null]`, `["右箭头", null]`
- `["任意", null]`, `["a", null]` ~ `["z", null]`, `["0", null]` ~ `["9", null]`

### sensing_setdrag_mode 的 DRAG_MODE
- `["draggable", null]` — 可拖拽
- `["not draggable", null]` — 不可拖拽

### sensing_of 的 PROPERTY
- `["x position", null]`, `["y position", null]`, `["direction", null]`
- `["costume #", null]`, `["costume name", null]`, `["size", null]`
- `["volume", null]`
- 变量名（如 `["my variable", null]`）
- 列表名

### sensing_of 的 OBJECT
- 角色名，或 `["_stage_", null]`（舞台）

### sensing_current 的 CURRENTMENU
- `["YEAR", null]` — 年
- `["MONTH", null]` — 月
- `["DATE", null]` — 日
- `["DAYOFWEEK", null]` — 星期
- `["HOUR", null]` — 时
- `["MINUTE", null]` — 分
- `["SECOND", null]` — 秒

## JSON 示例

### 碰到鼠标指针？
```json
{
  "block": {
    "opcode": "sensing_touchingobject",
    "next": null,
    "parent": null,
    "inputs": {
      "TOUCHINGOBJECTMENU": [1, "_mouse_"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 碰到颜色？
```json
{
  "block": {
    "opcode": "sensing_touchingcolor",
    "next": null,
    "parent": null,
    "inputs": {
      "COLOR": [1, "#FF0000"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 颜色 A 碰到颜色 B？
```json
{
  "block": {
    "opcode": "sensing_coloristouchingcolor",
    "next": null,
    "parent": null,
    "inputs": {
      "COLOR": [1, "#FF0000"],
      "COLOR2": [1, "#00FF00"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 到鼠标指针的距离
```json
{
  "block": {
    "opcode": "sensing_distanceto",
    "next": null,
    "parent": null,
    "inputs": {
      "DISTANCETOMENU": [1, "_mouse_"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 询问并等待
```json
{
  "block": {
    "opcode": "sensing_askandwait",
    "next": null,
    "parent": "prev",
    "inputs": {
      "QUESTION": [1, [10, "你叫什么名字？"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 回答（reporter）
```json
{
  "block": {
    "opcode": "sensing_answer",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 按下空格键？
```json
{
  "block": {
    "opcode": "sensing_keypressed",
    "next": null,
    "parent": null,
    "inputs": {
      "KEY_OPTION": [1, "key_block_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 按下鼠标？
```json
{
  "block": {
    "opcode": "sensing_mousedown",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 鼠标 x / y 坐标
```json
{
  "block": {
    "opcode": "sensing_mousex",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 设置拖拽模式为可拖拽
```json
{
  "block": {
    "opcode": "sensing_setdragmode",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "DRAG_MODE": ["draggable", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 响度
```json
{
  "block": {
    "opcode": "sensing_loudness",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 计时器
```json
{
  "block": {
    "opcode": "sensing_timer",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 计时器归零
```json
{
  "block": {
    "opcode": "sensing_resettimer",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### ... 的 x 坐标（sensing_of）
```json
{
  "block": {
    "opcode": "sensing_of",
    "next": null,
    "parent": null,
    "inputs": {
      "OBJECT": [1, "Stage"]
    },
    "fields": {
      "PROPERTY": ["x position", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 当前年份
```json
{
  "block": {
    "opcode": "sensing_current",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "CURRENTMENU": ["YEAR", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 2000 年至今的天数
```json
{
  "block": {
    "opcode": "sensing_dayssince2000",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 用户名
```json
{
  "block": {
    "opcode": "sensing_username",
    "next": null,
  