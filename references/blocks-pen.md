# 画笔扩展积木块 (Pen Extension)

> 参考文件：`references/blocks-pen.md` | 共 11 个积木块

画笔扩展允许角色在舞台上绘制图形，类似于海龟绘图。

需要在 project.json 的 `extensions` 数组中包含 `"pen"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `pen_clear` | 清空 | 清除所有画笔痕迹 |
| `pen_stamp` | 图章 | 在当前位置盖一个角色的图章 |
| `pen_penDown` | 落笔 | 开始绘制 |
| `pen_penUp` | 抬笔 | 停止绘制 |
| `pen_setPenColorToColor` | 将画笔颜色设为 ... | INPUT: `COLOR` |
| `pen_changePenColorParamBy` | 将画笔 ... 增加 N | FIELD: `COLOR_PARAM`, INPUT: `VALUE` |
| `pen_setPenColorParamTo` | 将画笔 ... 设为 N | FIELD: `COLOR_PARAM`, INPUT: `VALUE` |
| `pen_changePenSizeBy` | 将画笔大小增加 N | INPUT: `SIZE` |
| `pen_setPenSizeTo` | 将画笔大小设为 N | INPUT: `SIZE` |
| `pen_setPenShadeToNumber` | 将画笔亮度设为 ... | INPUT: `SHADE` |
| `pen_changePenShadeBy` | 将画笔亮度增加 ... | INPUT: `SHADE` |

## 字段值

### pen_changePenColorParamBy / pen_setPenColorParamTo 的 COLOR_PARAM
- `["color", null]` — 颜色
- `["saturation", null]` — 饱和度
- `["brightness", null]` — 亮度
- `["transparency", null]` — 透明度

## JSON 示例

### 清空画布
```json
{
  "block": {
    "opcode": "pen_clear",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 图章
```json
{
  "block": {
    "opcode": "pen_stamp",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 落笔
```json
{
  "block": {
    "opcode": "pen_penDown",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 抬笔
```json
{
  "block": {
    "opcode": "pen_penUp",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 设置画笔颜色
```json
{
  "block": {
    "opcode": "pen_setPenColorToColor",
    "next": null,
    "parent": "prev",
    "inputs": {
      "COLOR": [1, "#FF0000"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 颜色输入格式（HSB）
颜色值可以是：
- 十六进制字符串：`[1, "#FF0000"]`
- 使用 `[1, [8, "色相值"]]` 作为 COLOR_PARAM 的输入

### 将颜色增加 10
```json
{
  "block": {
    "opcode": "pen_changePenColorParamBy",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [4, "10"]]
    },
    "fields": {
      "COLOR_PARAM": ["color", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 将饱和度设为 50
```json
{
  "block": {
    "opcode": "pen_setPenColorParamTo",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [4, "50"]]
    },
    "fields": {
      "COLOR_PARAM": ["saturation", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 将画笔大小增加 1
```json
{
  "block": {
    "opcode": "pen_changePenSizeBy",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SIZE": [1, [4, "1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将画笔大小设为 5
```json
{
  "block": {
    "opcode": "pen_setPenSizeTo",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SIZE": [1, [4, "5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将画笔亮度设为 50
```json
{
  "block": {
    "opcode": "pen_setPenShadeToNumber",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SHADE": [1, [4, "50"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将画笔亮度增加 10
```json
{
  "block": {
    "opcode": "pen_changePenShadeBy",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SHADE": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

## 完整示例：绘制正方形

```json
{
  "start": {
    "opcode": "event_whenflagclicked",
    "next": "clear",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "clear": {
    "opcode": "pen_clear",
    "next": "down",
    "parent": "start",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "down": {
    "opcode": "pen_penDown",
    "next": "loop_start",
    "parent": "clear",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "loop_start": {
    "opcode": "control_repeat",
    "next": "up",
    "parent": "down",
    "inputs": {
      "TIMES": [1, [6, "4"]],
      "SUBSTACK": [2, "move"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "move": {
    "opcode": "motion_movesteps",
    "next": "turn",
    "parent": null,
    "inputs": { "STEPS": [1, [4, "100"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "turn": {
    "opcode": "motion_turnright",
    "next": null,
    "parent": "move",
    "inputs": { "DEGREES": [1, [4, "90"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "up": {
    "opcode": "pen_penUp",
    "next": null,
    "parent": "loop_start",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
