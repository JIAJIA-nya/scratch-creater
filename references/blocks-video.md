# 视频侦测扩展积木块 (Video Sensing Extension)

> 参考文件：`references/blocks-video.md` | 共 3 个积木块

视频侦测扩展使用摄像头检测运动，适合体感交互项目。

需要在 project.json 的 `extensions` 数组中包含 `"videoSensing"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `videoSensing_videoOn` | ... 方向上的视频 ... | FIELD: `VIDEO_STATE`, reporter |
| `videoSensing_whenMotionGreaterThan` | 当视频运动大于 N | INPUT: `REFERENCE` |
| `videoSensing_setVideoTransparency` | 将视频透明度设为 N | INPUT: `TRANSPARENCY` |

## 字段值

### videoSensing_videoOn 的 VIDEO_STATE
- `["motion", null]` — 运动量
- `["direction", null]` — 运动方向

### videoSensing_videoOn 输入
- `SUBJECT`: `[1, "_stage_"]`（检测舞台区域）或角色名

## JSON 示例

### 读取视频运动量
```json
{
  "block": {
    "opcode": "videoSensing_videoOn",
    "next": null,
    "parent": null,
    "inputs": {
      "SUBJECT": [1, "_stage_"]
    },
    "fields": {
      "VIDEO_STATE": ["motion", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取视频运动方向
```json
{
  "block": {
    "opcode": "videoSensing_videoOn",
    "next": null,
    "parent": null,
    "inputs": {
      "SUBJECT": [1, "_stage_"]
    },
    "fields": {
      "VIDEO_STATE": ["direction", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 当视频运动大于 10
```json
{
  "block": {
    "opcode": "videoSensing_whenMotionGreaterThan",
    "next": null,
    "parent": null,
    "inputs": {
      "REFERENCE": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 将视频透明度设为 50
```json
{
  "block": {
    "opcode": "videoSensing_setVideoTransparency",
    "next": null,
    "parent": "prev",
    "inputs": {
      "TRANSPARENCY": [1, [4, "50"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

## 完整示例：体感游戏控制

当摄像头检测到运动时，角色向上移动：

```json
{
  "start": {
    "opcode": "videoSensing_whenMotionGreaterThan",
    "next": "move_up",
    "parent": null,
    "inputs": { "REFERENCE": [1, [4, "10"]] },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "move_up": {
    "opcode": "motion_changeyby",
    "next": null,
    "parent": "start",
    "inputs": { "DY": [1, [4, "10"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
