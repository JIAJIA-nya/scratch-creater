# 音乐扩展积木块 (Music Extension)

> 参考文件：`references/blocks-music.md` | 共 7 个积木块

音乐扩展允许项目演奏音符、设置乐器、控制节拍和速度。

需要在 project.json 的 `extensions` 数组中包含 `"music"`。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `music_playDrumForBeats` | 击打 ... 拍 | INPUT: `DRUM`, `BEATS` |
| `music_restForBeats` | 休止 ... 拍 | INPUT: `BEATS` |
| `music_playNoteForBeats` | 演奏音符 ... 拍 | INPUT: `NOTE`, `BEATS` |
| `music_setInstrument` | 将乐器设为 ... | INPUT: `INSTRUMENT` |
| `music_setTempo` | 将演奏速度设为 ... | INPUT: `TEMPO` |
| `music_changeTempo` | 将演奏速度增加 ... | INPUT: `TEMPO` |
| `music_getTempo` | 演奏速度 | reporter |

## 字段值

### music_setInstrument 的 INSTRUMENT
- `["1", null]` — 钢琴 (Piano)
- `["2", null]` — 电钢琴 (Electric Piano)
- `["3", null]` — 风琴 (Organ)
- `["4", null]` — 吉他 (Guitar)
- `["5", null]` — 电吉他 (Electric Guitar)
- `["6", null]` — 贝斯 (Bass)
- `["7", null]` — 拨弦 (Pizzicato)
- `["8", null]` — 大提琴 (Cello)
- `["9", null]` — 长号 (Trombone)
- `["10", null]` — 单簧管 (Clarinet)
- `["11", null]` — 萨克斯风 (Saxophone)
- `["12", null]` — 长笛 (Flute)
- `["13", null]` — 木笛 (Wooden Flute)
- `["14", null]` — 巴松管 (Bassoon)
- `["15", null]` — 合唱团 (Choir)
- `["16", null]` — 颤音琴 (Vibraphone)
- `["17", null]` — 音乐盒 (Music Box)
- `["18", null]` — 钢鼓 (Steel Drum)
- `["19", null]` — 木琴 (Marimba)
- `["20", null]` — 合成器 (Synthesizer)
- `["21", null]` — 低音合成器 (Synth Bass)

### music_playDrumForBeats 的 DRUM
- `["1", null]` — 小鼓 (Snare Drum)
- `["2", null]` — 低音鼓 (Bass Drum)
- `["3", null]` — 军鼓边击 (Side Stick)
- `["4", null]` — 铜钹 (Crash Cymbal)
- `["5", null]` — 开镲 (Open Hi-Hat)
- `["6", null]` — 闭镲 (Closed Hi-Hat)
- `["7", null]` — 铃鼓 (Tambourine)
- `["8", null]` — 拍手 (Hand Clap)
- `["9", null]` — 木鱼 (Claves)
- `["10", null]` — 木块 (Wood Block)
- `["11", null]` — 牛铃 (Cowbell)
- `["12", null]` — 三角铁 (Triangle)
- `["13", null]` — 邦加鼓 (Bongo)
- `["14", null]` — 康加鼓 (Conga)
- `["15", null]` — 卡巴萨 (Cabasa)
- `["16", null]` — 刮瓜 (Guiro)
- `["17", null]` — 响棒 (Vibraslap)
- `["18", null]` — 铃铛 (Sleigh Bells)

## JSON 示例

### 击打小鼓 0.25 拍
```json
{
  "block": {
    "opcode": "music_playDrumForBeats",
    "next": null,
    "parent": "prev",
    "inputs": {
      "DRUM": [1, [4, "1"]],
      "BEATS": [1, [4, "0.25"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 演奏音符 C4 1 拍
```json
{
  "block": {
    "opcode": "music_playNoteForBeats",
    "next": null,
    "parent": "prev",
    "inputs": {
      "NOTE": [1, [7, "60"]],
      "BEATS": [1, [4, "1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

音符编号：C4 = 60, D4 = 62, E4 = 64, F4 = 65, G4 = 67, A4 = 69, B4 = 71, C5 = 72

### 将乐器设为钢琴
```json
{
  "block": {
    "opcode": "music_setInstrument",
    "next": null,
    "parent": "prev",
    "inputs": {
      "INSTRUMENT": [1, [4, "1"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将演奏速度设为 120
```json
{
  "block": {
    "opcode": "music_setTempo",
    "next": null,
    "parent": "prev",
    "inputs": {
      "TEMPO": [1, [4, "120"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 将演奏速度增加 10
```json
{
  "block": {
    "opcode": "music_changeTempo",
    "next": null,
    "parent": "prev",
    "inputs": {
      "TEMPO": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 休止 0.5 拍
```json
{
  "block": {
    "opcode": "music_restForBeats",
    "next": null,
    "parent": "prev",
    "inputs": {
      "BEATS": [1, [4, "0.5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取演奏速度（reporter）
```json
{
  "block": {
    "opcode": "music_getTempo",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

## 完整示例：简单旋律

```json
{
  "start": {
    "opcode": "event_whenflagclicked",
    "next": "set_inst",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "set_inst": {
    "opcode": "music_setInstrument",
    "next": "set_tempo",
    "parent": "start",
    "inputs": { "INSTRUMENT": [1, [4, "1"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "set_tempo": {
    "opcode": "music_setTempo",
    "next": "note1",
    "parent": "set_inst",
    "inputs": { "TEMPO": [1, [4, "120"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "note1": {
    "opcode": "music_playNoteForBeats",
    "next": "note2",
    "parent": "set_tempo",
    "inputs": { "NOTE": [1, [7, "60"]], "BEATS": [1, [4, "1"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "note2": {
    "opcode": "music_playNoteForBeats",
    "next": "note3",
    "parent": "note1",
    "inputs": { "NOTE": [1, [7, "64"]], "BEATS": [1, [4, "1"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "note3": {
    "opcode": "music_playNoteForBeats",
    "next": null,
    "parent": "note2",
    "inputs": { "NOTE": [1, [7, "67"]], "BEATS": [1, [4, "2"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```
