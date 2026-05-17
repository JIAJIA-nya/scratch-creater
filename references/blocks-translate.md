# 翻译扩展积木块 (Translate Extension)

> 参考文件：`references/blocks-translate.md` | 共 2 个积木块

翻译扩展使用 Google Translate API 将文本翻译为不同语言。

需要在 project.json 的 `extensions` 数组中包含 `"translate"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `translate_getTranslate` | 将 ... 译为 ... | reporter，INPUTS: `WORDS`, `LANGUAGE` |
| `translate_getViewerLanguage` | 访客语言 | reporter |

## 语言代码

常用语言代码：
- `"zh-cn"` — 中文（简体）
- `"zh-tw"` — 中文（繁体）
- `"en"` — 英语
- `"ja"` — 日语
- `"ko"` — 韩语
- `"fr"` — 法语
- `"de"` — 德语
- `"es"` — 西班牙语
- `"it"` — 意大利语
- `"pt"` — 葡萄牙语
- `"ru"` — 俄语
- `"ar"` — 阿拉伯语
- `"hi"` — 印地语
- `"th"` — 泰语
- `"vi"` — 越南语

## JSON 示例

### 将 "Hello" 译为中文
```json
{
  "block": {
    "opcode": "translate_getTranslate",
    "next": null,
    "parent": null,
    "inputs": {
      "WORDS": [1, [10, "Hello"]],
      "LANGUAGE": [1, [10, "zh-cn"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取访客语言
```json
{
  "block": {
    "opcode": "translate_getViewerLanguage",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

## 完整示例：多语言问候

```json
{
  "start": {
    "opcode": "event_whenflagclicked",
    "next": "say_greeting",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "say_greeting": {
    "opcode": "looks_say",
    "next": null,
    "parent": "start",
    "inputs": {
      "MESSAGE": [2, "translate_block"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "translate_block": {
    "opcode": "translate_getTranslate",
    "next": null,
    "parent": null,
    "inputs": {
      "WORDS": [1, [10, "Hello, welcome!"]],
      "LANGUAGE": [2, "lang_block"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "lang_block": {
    "opcode": "translate_getViewerLanguage",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
