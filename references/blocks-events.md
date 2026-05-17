# 事件类积木块 (Events)

> 参考文件：`references/blocks-events.md` | 共 10 个积木块

事件类积木块是脚本的触发器，位于每个脚本的最顶端（topLevel: true）。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `event_whenflagclicked` | 当绿旗被点击 | 最常见的触发器 |
| `event_whenkeypressed` | 当按下某键 | FIELD: `KEY_OPTION` |
| `event_whenthisspriteclicked` | 当角色被点击 | 点击当前角色时触发 |
| `event_whenstageclicked` | 当舞台被点击 | 点击舞台时触发（仅 Stage） |
| `event_whenbackdropswitchesto` | 当背景切换到 | FIELD: `BACKDROP` |
| `event_whengreaterthan` | 当响度/计时器 > N | FIELD: `WHENGREATERTHANMENU` (响度/计时器), INPUT: `VALUE` |
| `event_whenbroadcastreceived` | 当接收到消息 | FIELD: `BROADCAST_OPTION` |
| `event_broadcast` | 广播消息 | INPUT: `BROADCAST_INPUT` |
| `event_broadcastandwait` | 广播消息并等待 | INPUT: `BROADCAST_INPUT` |
| `event_whentouchingobject` | 当碰到 ... | INPUT: `TOUCHINGOBJECTMENU` |

## JSON 示例

### 当绿旗被点击
```json
{
  "abc001": {
    "opcode": "event_whenflagclicked",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 当按下某键
```json
{
  "abc001": {
    "opcode": "event_whenkeypressed",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "KEY_OPTION": ["空格", null]
    },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

可选按键值：`空格`, `上箭头`, `下箭头`, `左箭头`, `右箭头`, `任意`, `a`-`z`, `0`-`9`

### 当接收到消息
```json
{
  "abc001": {
    "opcode": "event_whenbroadcastreceived",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "BROADCAST_OPTION": ["消息1", "message1"]
    },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 广播消息
```json
{
  "abc001": {
    "opcode": "event_broadcast",
    "next": null,
    "parent": "prev001",
    "inputs": {
      "BROADCAST_INPUT": [1, [11, "消息1", "message1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 广播消息并等待
```json
{
  "abc001": {
    "opcode": "event_broadcastandwait",
    "next": null,
    "parent": "prev001",
    "inputs": {
      "BROADCAST_INPUT": [1, [11, "消息1", "message1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 当响度/计时器大于
```json
{
  "abc001": {
    "opcode": "event_whengreaterthan",
    "next": null,
    "parent": null,
    "inputs": {
      "VALUE": [1, [4, "10"]]
    },
    "fields": {
      "WHENGREATERTHANMENU": ["响度", null]
    },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

`WHENGREATERTHANMENU` 可选值：`响度`, `计时器`

### 当背景切换到
```json
{
  "abc001": {
    "opcode": "event_whenbackdropswitchesto",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "BACKDROP": ["背景1", null]
    },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 当角色被点击
```json
{
  "abc001": {
    "opcode": "event_whenthisspriteclicked",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},