# Scratch Creator Skill

> 让 AI Agent 帮你创建和修改 MIT Scratch 3.0 项目（.sb3 文件）。

## 这是什么？

Scratch Creator 是一个 AI Agent Skill，使 Claude、Codex、OpenCode 等 AI 编程助手能够：

- **从零创建** Scratch 3.0 项目（.sb3 文件）
- **修改已有** 的 .sb3 项目文件
- **理解 Scratch 积木块** 的 JSON 格式并正确生成脚本
- **打包/解包** .sb3 文件
- **使用模板** 快速启动常见项目类型

## 适用 Agent

本 Skill 以 Markdown 文档 + Python 脚本的形式提供，**理论上任何支持文件读取和代码执行的 AI Agent 都可以使用**：

| Agent | 兼容性 | 说明 |
|-------|--------|------|
| **Claude (Cowork)** | ✅ 完美 | 原生支持 SKILL.md 格式，可直接读取 references/ 目录 |
| **Claude Code** | ✅ 完美 | 同上，SKILL.md 是 Claude Code 原生 skill 格式 |
| **OpenAI Codex** | ✅ 可用 | 读取 SKILL.md + references/ 作为上下文，执行 Python 脚本 |
| **OpenCode** | ✅ 可用 | 同上，支持 Markdown 上下文和脚本执行 |
| **Cursor** | ✅ 可用 | 将 SKILL.md 和 references/ 加入项目上下文 |
| **GitHub Copilot** | ⚠️ 部分 | 可将 SKILL.md 作为上下文参考，但无法直接执行脚本 |
| **Gemini CLI** | ✅ 可用 | 支持读取文件和执行命令的 Agent 均可使用 |

**核心原理**：SKILL.md 和 references/ 目录提供了完整的 Scratch 3.0 积木块参考文档，Agent 读取后即可获得所有 opcode 知识。scripts/ 目录提供了 Python 工具函数，Agent 可以直接调用或翻译为其他语言执行。

## 目录结构

```
scratch-creator/
├── SKILL.md                        # 主入口：核心工作流和使用方法
├── README.md                       # 本文件
├── references/                     # 积木块完整参考文档
│   ├── blocks-events.md            # 事件类积木
│   ├── blocks-motion.md            # 运动类积木
│   ├── blocks-looks.md             # 外观类积木
│   ├── blocks-sound.md             # 声音类积木
│   ├── blocks-control.md           # 控制类积木
│   ├── blocks-sensing.md           # 侦测类积木
│   ├── blocks-operators.md         # 运算类积木
│   ├── blocks-variables.md         # 变量和列表
│   ├── blocks-music.md             # 音乐扩展
│   ├── blocks-pen.md               # 画笔扩展
│   ├── blocks-video.md             # 视频侦测扩展
│   ├── blocks-translate.md         # 翻译扩展
│   ├── blocks-texttospeech.md      # 文字朗读扩展
│   ├── blocks-microbit.md          # micro:bit 扩展
│   ├── blocks-lego.md              # LEGO 扩展
│   ├── blocks-custom.md            # 自定义积木块
│   └── project-json-schema.md      # project.json 完整结构
├── scripts/                        # Python 工具脚本
│   ├── __init__.py
│   ├── scratch_utils.py            # 核心工具（打包/解包/验证）
│   ├── block_builder.py            # 积木块构建器
│   └── project_builder.py          # 项目构建器
└── templates/                      # 项目模板（10 个）
    ├── 01-simple-animation/        # 简单动画
    ├── 02-bouncing-ball/           # 弹跳球
    ├── 03-quiz-game/               # 问答游戏
    ├── 04-platformer/              # 平台跳跃
    ├── 05-maze-game/               # 迷宫游戏
    ├── 06-pong/                    # 乒乓球
    ├── 07-flappy-bird/             # 飞翔的小鸟
    ├── 08-interactive-story/       # 互动故事
    ├── 09-paint-app/               # 画板应用
    └── 10-multiplayer-chat/        # 多人聊天模拟
```

## 快速开始

### 1. 创建新项目

告诉 Agent：

> "帮我创建一个 Scratch 小游戏，玩家用方向键控制角色收集星星"

Agent 会：
1. 读取 SKILL.md 了解工作流
2. 读取相关积木块参考文档
3. 使用 scripts/ 中的工具创建项目
4. 生成 .sb3 文件

### 2. 修改现有项目

> "帮我把这个 .sb3 文件中的角色移动速度改快一点"

Agent 会：
1. 解包 .sb3 文件
2. 读取并分析 project.json
3. 修改对应积木块的参数
4. 重新打包为 .sb3

### 3. 从模板开始

> "用平台跳跃模板创建一个新游戏"

Agent 会：
1. 读取 templates/04-platformer/ 中的模板
2. 根据用户需求定制
3. 生成完整 .sb3 文件

## Scratch 3.0 积木块覆盖

本 Skill 覆盖 Scratch 3.0 全部积木块类型：

| 类别 | 积木块数量 | 参考文档 |
|------|-----------|---------|
| 事件 | 8 | `blocks-events.md` |
| 运动 | 18 | `blocks-motion.md` |
| 外观 | 22 | `blocks-looks.md` |
| 声音 | 8 | `blocks-sound.md` |
| 控制 | 11 | `blocks-control.md` |
| 侦测 | 18 | `blocks-sensing.md` |
| 运算 | 17 | `blocks-operators.md` |
| 变量 | 12 | `blocks-variables.md` |
| 音乐 | 6 | `blocks-music.md` |
| 画笔 | 11 | `blocks-pen.md` |
| 视频侦测 | 3 | `blocks-video.md` |
| 翻译 | 2 | `blocks-translate.md` |
| 文字朗读 | 2 | `blocks-texttospeech.md` |
| micro:bit | 16 | `blocks-microbit.md` |
| LEGO | 12+ | `blocks-lego.md` |
| 自定义积木 | 4 | `blocks-custom.md` |
| **合计** | **170+** | |

## 技术细节

### .sb3 文件格式

.sb3 文件是一个 ZIP 压缩包，包含：
- `project.json` — 项目核心数据（角色、背景、脚本）
- 媒体文件 — SVG/PNG 造型、WAV/MP3 声音

### project.json 结构

```json
{
  "targets": [ /* Stage + Sprites */ ],
  "monitors": [ /* 变量监视器 */ ],
  "extensions": [ /* 使用的扩展 */ ],
  "meta": { "semver": "3.0.0", "vm": "0.2.0" }
}
```

### 积木块 JSON 格式

```json
{
  "blockId": {
    "opcode": "motion_movesteps",
    "next": "nextBlockId",
    "parent": "parentBlockId",
    "inputs": { "STEPS": [1, [4, "10"]] },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0, "y": 0
  }
}
```

## 推荐许可证

本项目推荐使用 **MIT License**，与 Scratch 本身的开源精神一致。

MIT 许可证的优势：
- 宽松：允许自由使用、修改、分发
- 简洁：许可证文本简短易懂
- 兼容：与大多数开源项目兼容
- 商业友好：允许商业使用

## 贡献

欢迎贡献新的项目模板、积木块参考补充或脚本改进。

## 资源

- [MIT Scratch](https://scratch.mit.edu/)
- [Scratch Wiki - File Format](https://en.scratch-wiki.info/wiki/Scratch_File_Format)
- [Scratch Blocks Syntax](https://en.scratch-wiki.info/wiki/Scratch_File_Format/Block_Selection)
