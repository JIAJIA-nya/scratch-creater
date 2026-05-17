# project.json 完整结构

> 参考文件：`references/project-json-schema.md`

.sb3 文件解压后的核心文件，包含所有项目数据。

## 顶层结构

```json
{
  "targets": [ ... ],
  "monitors": [ ... ],
  "extensions": [ ... ],
  "meta": { ... }
}
```

## targets 数组

每个 target 代表一个 Stage 或 Sprite。

### Stage 结构

```json
{
  "isStage": true,
  "name": "Stage",
  "variables": {
    "varId1": ["变量名", 初始值]
  },
  "lists": {
    "listId1": ["列表名", ["item1", "item2"]]
  },
  "broadcasts": {
    "msgId1": "消息名"
  },
  "blocks": { ... },
  "comments": { ... },
  "currentCostume": 0,
  "costumes": [
    {
      "assetId": "md5hash",
      "name": "背景1",
      "bitmapResolution": 1,
      "md5ext": "md5hash.svg",
      "dataFormat": "svg",
      "rotationCenterX": 240,
      "rotationCenterY": 180
    }
  ],
  "sounds": [
    {
      "assetId": "md5hash",
      "name": "喵",
      "dataFormat": "wav",
      "format": "",
      "rate": 48000,
      "sampleCount": 40194,
      "md5ext": "md5hash.wav"
    }
  ],
  "volume": 100,
  "layerOrder": 0,
  "tempo": 60,
  "videoTransparency": 50,
  "videoState": "on",
  "textToSpeechLanguage": null
}
```

### Sprite 结构

```json
{
  "isStage": false,
  "name": "角色1",
  "variables": { ... },
  "lists": { ... },
  "broadcasts": { ... },
  "blocks": { ... },
  "comments": { ... },
  "currentCostume": 0,
  "costumes": [
    {
      "assetId": "md5hash",
      "name": "造型1",
      "bitmapResolution": 1,
      "md5ext": "md5hash.svg",
      "dataFormat": "svg",
      "rotationCenterX": 48,
      "rotationCenterY": 50
    }
  ],
  "sounds": [ ... ],
  "volume": 100,
  "layerOrder": 1,
  "visible": true,
  "x": 0,
  "y": 0,
  "size": 100,
  "direction": 90,
  "draggable": false,
  "rotationStyle": "all around"
}
```

## blocks 结构

```json
{
  "blockId": {
    "opcode": "motion_movesteps",
    "next": "nextBlockId",
    "parent": "parentBlockId",
    "inputs": {
      "INPUT_NAME": [type, value]
    },
    "fields": {
      "FIELD_NAME": ["value", null]
    },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 积木块连接关系

- `topLevel: true` + `parent: null` — 脚本入口（事件触发器）
- `next` — 指向下一个积木块（纵向连接）
- `parent` — 指向父积木块
- `shadow: true` — 阴影块（不可被用户代码覆盖的默认值）

## comments 结构

```json
{
  "commentId": {
    "blockId": "attachedBlockId",
    "x": 100,
    "y": 100,
    "width": 200,
    "height": 200,
    "minimized": false,
    "text": "这是注释内容"
  }
}
```

## monitors 结构（变量/列表监视器）

```json
{
  "id": "monitorId",
  "opcode": "data_variable",
  "mode": "default",
  "params": {
    "VARIABLE": "变量名"
  },
  "spriteName": "Stage",
  "value": 0,
  "width": 0,
  "height": 0,
  "x": 5,
  "y": 5,
  "visible": true,
  "sliderMin": 0,
  "sliderMax": 100,
  "isDiscrete": true
}
```

## extensions 数组

声明项目使用的扩展：

```json
["pen", "music", "videoSensing", "text2speech", "translate", "microbit", "ev3", "wedo2", "makeymakey"]
```

可用扩展：
| 扩展名 | 说明 |
|--------|------|
| `pen` | 画笔 |
| `music` | 音乐 |
| `videoSensing` | 视频侦测 |
| `text2speech` | 文字朗读 |
| `translate` | 翻译 |
| `microbit` | BBC micro:bit |
| `ev3` | LEGO MINDSTORMS EV3 |
| `wedo2` | LEGO Education WeDo 2.0 |
| `makeymakey` | Makey Makey |

## meta 结构

```json
{
  "semver": "3.0.0",
  "vm": "0.2.0",
  "agent": "Mozilla/5.0 (..."
}
```

## 完整最小示例

```json
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "variables": {},
      "lists": {},
      "broadcasts": {},
      "blocks": {},
      "comments": {},
      "currentCostume": 0,
      "costumes": [
        {
          "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
          "name": "backdrop1",
          "bitmapResolution": 1,
          "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
          "dataFormat": "svg",
          "rotationCenterX": 240,
          "rotationCenterY": 180
        }
      ],
      "sounds": [],
      "volume": 100,
      "layerOrder": 0
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "variables": {},
      "lists": {},
      "broadcasts": {},
      "blocks": {
        "event_block": {
          "opcode": "event_whenflagclicked",
          "next": "say_block",
          "parent": null,
          "inputs": {},
          "fields": {},
          "shadow": false,
          "topLevel": true,
          "x": 0,
          "y": 0
        },
        "say_block": {
          "opcode": "looks_say",
          "next": null,
          "parent": "event_block",
          "inputs": {
            "MESSAGE": [1, [10, "你好！"]]
          },
          "fields": {},
          "shadow": false,
          "topLevel": false
        }
      },
      "comments": {},
      "currentCostume": 0,
      "costumes": [
        {
          "assetId": "bcf454acf82e4504149f7ffe07081dbc",
          "name": "costume1",
          "bitmapResolution": 1,
          "md5ext": "bcf454acf82e4504149f7ffe07081dbc.svg",
          "dataFormat": "svg",
          "rotationCenterX": 48,
          "rotationCenterY": 50
        }
      ],
      "sounds": [],
      "volume": 100,
      "layerOrder": 1,
      "visible": true,
      "x": 0,
      "y": 0,
      "size": 100,
      "direction": 90,
      "draggable": false,
      "rotationStyle": "all around"
    }
  ],
  "monitors": [],
  "extensions": [],
  "meta": {
    "semver": "3.0.0",
    "vm": "0.2.0",
    "agent": ""
  }
}
```
