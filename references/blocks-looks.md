# 外观类积木块 (Looks)

> 参考文件：`references/blocks-looks.md` | 共 22 个积木块

外观类积木块控制角色的显示效果，包括对话气泡、造型切换、大小、颜色特效等。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `looks_say` | 说 ... | INPUT: `MESSAGE` |
| `looks_sayforseconds` | 说 ... N 秒 | INPUTS: `MESSAGE`, `SECS` |
| `looks_think` | 想 ... | INPUT: `MESSAGE` |
| `looks_thinkforseconds` | 想 ... N 秒 | INPUTS: `MESSAGE`, `SECS` |
| `looks_show` | 显示 | 无参数 |
| `looks_hide` | 隐藏 | 无参数 |
| `looks_switchcostumeto` | 切换造型为 ... | INPUT: `COSTUME` |
| `looks_nextcostume` | 下一个造型 | 无参数 |
| `looks_switchbackdropto` | 切换背景为 ... | INPUT: `BACKDROP` |
| `looks_nextbackdrop` | 下一个背景 | 无参数 |
| `looks_changeeffectby` | 将特效增加 N | FIELD: `EFFECT`, INPUT: `CHANGE` |
| `looks_seteffectto` | 将特效设定为 N | FIELD: `EFFECT`, INPUT: `VALUE` |
| `looks_cleargraphiceffects` | 清除图形特效 | 无参数 |
| `looks_changesizeby` | 大小增加 N | INPUT: `CHANGE` |
| `looks_setsizeto` | 大小设为 N% | INPUT: `SIZE` |
| `looks_gotofrontback` | 移到最前/最后层 | FIELD: `FRONT_BACK` |
| `looks_goforwardbackwardlayers` | 前/后移 N 层 | FIELD: `FORWARD_BACKWARD`, INPUT: `NUM` |
| `looks_costumenumbername` | 造型编号/名称 | FIELD: `NUMBER_NAME` |
| `looks_backdropnumbername` | 背景编号/名称 | FIELD: `NUMBER_NAME` |
| `looks_size` | 大小 | reporter，返回当前大小 |
| `looks_switchbackdroptoandwait` | 切换背景并等待 | INPUT: `BACKDROP` |
| `looks_hideallsprites` | 隐藏所有角色 | 无参数 |
| `looks_changestretchby` | 伸缩增加 N | INPUT: `CHANGE` |
| `looks_setstretchto` | 伸缩设为 N% | INPUT: `STRETCH` |

## 字段值

### looks_changeeffectby / looks_seteffectto 的 EFFECT
可选值：`颜色`, `鱼眼`, `旋涡`, `像素化`, `马赛克`, `亮度`, `虚像`
对应英文 key：`COLOR`, `FISHEYE`, `WHIRL`, `PIXELATE`, `MOSAIC`, `BRIGHTNESS`, `GHOST`

### looks_gotofrontback 的 FRONT_BACK
- `["front", null]` — 最前面
- `["back", null]` — 最后面

### looks_goforwardbackwardlayers 的 FORWARD_BACKWARD
- `["forward", null]` — 前移
- `["backward", null]` — 后移

### looks_costumenumbername 的 NUMBER_NAME
- `["number", null]` — 编号
- `["name", null]` — 名称

## JSON 示例

### 说 "你好！"
```json
{
  "block": {
    "opcode": "looks_say",
    "next": null,
    "parent": "prev",
    "inputs": {
      "MESSAGE": [1, [10, "你好！"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 说 "你好！" 2 秒
```json
{
  "block": {
    "opcode": "looks_sayforseconds",
    "next": null,
    "parent": "prev",
    "inputs": {
      "MESSAGE": [1, [10, "你好！"]],
      "SECS": [1, [4, "2"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 切换造型
```json
{
  "block": {
    "opcode": "looks_switchcostumeto",
    "next": null,
    "parent": "prev",
    "inputs": {
      "COSTUME": [1, "costume_block_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将颜色特效增加 25
```json
{
  "block": {
    "opcode": "looks_changeeffectby",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CHANGE": [1, [4, "25"]]
    },
    "fields": {
      "EFFECT": ["颜色", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 将虚像特效设为 50
```json
{
  "block": {
    "opcode": "looks_seteffectto",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [4, "50"]]
    },
    "fields": {
      "EFFECT": ["虚像", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 移到最前面
```json
{
  "block": {
    "opcode": "looks_gotofrontback",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "FRONT_BACK": ["front", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 大小增加 10
```json
{
  "block": {
    "opcode": "looks_changesizeby",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CHANGE": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 切换背景并等待
```json
{
  "block": {
    "opcode": "looks_switchbackdroptoan