# 文字朗读扩展积木块 (Text to Speech Extension)

> 参考文件：`references/blocks-texttospeech.md` | 共 2 个积木块

文字朗读扩展将文本转换为语音播放，支持多种语言和声音。

需要在 project.json 的 `extensions` 数组中包含 `"text2speech"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `text2speech_speakAndWait` | 朗读 ... | INPUT: `WORDS` |
| `text2speech_setVoice` | 将声音设为 ... | FIELD: `VOICE` |
| `text2speech_setLanguage` | 将语言设为 ... | FIELD: `LANGUAGE` |

## 字段值

### text2speech_setVoice 的 VOICE
- `["alto", null]` — 低音
- `["tenor", null]` — 高音
- `["squeak", null]` — 尖声
- `["giant", null]` — 巨人
- `["kitten", null]` — 小猫

### text2speech_setLanguage 的 LANGUAGE
- `["zh-cn"]` — 中文
- `["en"]` — 英语
- `["ja"]` — 日语
- `["ko"]` — 韩语
- `["fr"]` — 法语
- `["de"]` — 德语
- `["es"]` — 西班牙语
- `["it"]` — 意大利语
- `["pt"]` — 葡萄牙语
- `["ru"]` — 俄语
- `["ar"]` — 阿拉伯语
- `["hi"]` — 印地语

## JSON 示例

### 朗读 "你好世界"
```json
{
  "block": {
    "opcode": "text2speech_speakAndWait",
    "next": null,
    "parent": "prev",
    "inputs": {
      "WORDS": [1, [10, "你好世界"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将声音设为高音
```json
{
  "block": {
    "opcode": "text2speech_setVoice",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "VOICE": ["tenor", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 将语言设为中文
```json
{
  "block": {
    "opcode": "text2speech_setLanguage",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "LANGUAGE": ["zh-cn", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```
