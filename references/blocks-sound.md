# 声音类积木块 (Sound)

> 参考文件：`references/blocks-sound.md` | 共 12 个积木块

声音类积木块控制音效和背景音乐的播放。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `sound_play` | 播放声音 ... | INPUT: `SOUND_MENU` |
| `sound_playuntildone` | 播放声音 ... 直到结束 | INPUT: `SOUND_MENU` |
| `sound_stopallsounds` | 停止所有声音 | 无参数 |
| `sound_changeeffectby` | 将音效增加 N | FIELD: `EFFECT`, INPUT: `VALUE` |
| `sound_seteffectto` | 将音效设定为 N | FIELD: `EFFECT`, INPUT: `VALUE` |
| `sound_cleareffects` | 清除音效 | 无参数 |
| `sound_changevolumeby` | 音量增加 N | INPUT: `VOLUME` |
| `sound_setvolumeto` | 音量设为 N% | INPUT: `VOLUME` |
| `sound_volume` | 音量 | reporter，返回当前音量 |
| `sound_sounds_menu` | （声音菜单） | reporter/field，返回声音名 |
| `sound_beats_menu` | （节拍菜单） | reporter/field，返回节拍数 |
| `sound_effects_menu` | （音效菜单） | reporter/field，返回音效类型 |

## 字段值

### sound_changeeffectby / sound_seteffectto 的 EFFECT
- `["PAN", null]` — 左右平衡（pan left/right）
- `["PITCH", null`] — 音调（pitch）

## JSON 示例

### 播放声音
```json
{
  "block": {
    "opcode": "sound_play",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SOUND_MENU": [1, "sound_block_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 播放声音直到结束
```json
{
  "block": {
    "opcode": "sound_playuntildone",
    "next": null,
    "parent": "prev",
    "inputs": {
      "SOUND_MENU": [1, "sound_block_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 停止所有声音
```json
{
  "block": {
    "opcode": "sound_stopallsounds",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将左右平衡音效增加 -100（全左）
```json
{
  "block": {
    "opcode": "sound_seteffectto",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [4, "-100"]]
    },
    "fields": {
      "EFFECT": ["PAN", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 音量设为 50%
```json
{
  "block": {
    "opcode": "sound_setvolumeto",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VOLUME": [1, [4, "50"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 音量增加 -10
```json
{
  "block": {
    "opcode": "sound_changevolumeby",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VOLUME": [1, [4, "-10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取音量（reporter）
```json
{
  "block": {
    "opcode": "sound_volume",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```