---
name: scratch-creator
description: "协助用户创建和修改 MIT Scratch 3.0 项目（.sb3 文件）。涵盖从零创建项目、添加角色和背景、用积木块编写脚本（全部 170+ 个积木块）、修改现有项目、打包发布。当用户提到 Scratch 编程、创建动画/游戏/交互故事、或处理 .sb3 文件时触发。"
---

# Scratch Creator Skill

协助用户创建和修改 MIT Scratch 3.0 项目。.sb3 文件本质上是 ZIP 压缩包，包含 project.json 和媒体资源。

## 目录结构

```
scratch-creator/
├── SKILL.md                        # 本文件：核心工作流
├── README.md                       # 项目说明和 Agent 兼容性
├── references/                     # 积木块完整参考（按类别分文件）
│   ├── blocks-events.md            # 事件类（8 个）
│   ├── blocks-motion.md            # 运动类（18 个）
│   ├── blocks-looks.md             # 外观类（22 个）
│   ├── blocks-sound.md             # 声音类（8 个）
│   ├── blocks-control.md           # 控制类（11 个）
│   ├── blocks-sensing.md           # 侦测类（18 个）
│   ├── blocks-operators.md         # 运算类（17 个）
│   ├── blocks-variables.md         # 变量和列表（12 个）
│   ├── blocks-music.md             # 音乐扩展（6 个）
│   ├── blocks-pen.md               # 画笔扩展（11 个）
│   ├── blocks-video.md             # 视频侦测扩展（3 个）
│   ├── blocks-translate.md         # 翻译扩展（2 个）
│   ├── blocks-texttospeech.md      # 文字朗读扩展（3 个）
│   ├── blocks-microbit.md          # micro:bit 扩展（16 个）
│   ├── blocks-lego.md              # LEGO 扩展（12+ 个）
│   ├── blocks-custom.md            # 自定义积木（4 个）
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

## 核心工作流

### 1. 需求分析

开始创建前，了解：

- **项目类型**：动画、游戏、交互故事、教学演示？
- **目标受众**：儿童自学、课堂教学、个人项目？
- **复杂度**：简单演示 vs 完整游戏？
- **现有资源**：用户是否已有素材需要导入？
- **是否需要扩展**：音乐、画笔、视频侦测、翻译、micro:bit、LEGO？

### 2. 创建新项目

#### 步骤

1. **读取 `references/project-json-schema.md`** 了解完整结构
2. **根据项目类型读取对应积木块参考**（见下方积木块索引）
3. **使用 `scripts/project_builder.py`** 创建项目结构
4. **使用 `scripts/block_builder.py`** 编写积木脚本
5. **使用 `scripts/scratch_utils.py`** 打包为 .sb3

#### 积木块索引

| 积木块类别 | 积木数量 | 参考文件 |
|-----------|---------|---------|
| 事件 | 8 | `references/blocks-events.md` |
| 运动 | 18 | `references/blocks-motion.md` |
| 外观 | 22 | `references/blocks-looks.md` |
| 声音 | 8 | `references/blocks-sound.md` |
| 控制 | 11 | `references/blocks-control.md` |
| 侦测 | 18 | `references/blocks-sensing.md` |
| 运算 | 17 | `references/blocks-operators.md` |
| 变量和列表 | 12 | `references/blocks-variables.md` |
| 音乐扩展 | 6 | `references/blocks-music.md` |
| 画笔扩展 | 11 | `references/blocks-pen.md` |
| 视频侦测扩展 | 3 | `references/blocks-video.md` |
| 翻译扩展 | 2 | `references/blocks-translate.md` |
| 文字朗读扩展 | 3 | `references/blocks-texttospeech.md` |
| micro:bit 扩展 | 16 | `references/blocks-microbit.md` |
| LEGO 扩展 | 12+ | `references/blocks-lego.md` |
| 自定义积木 | 4 | `references/blocks-custom.md` |
| **合计** | **170+** | |

### 3. 修改现有项目

1. **解包 .sb3**：使用 `scratch_utils.unpack_sb3()`
2. **读取 project.json**：分析角色、脚本、媒体资源
3. **读取对应积木块参考**确认需要修改的 opcode
4. **修改 project.json**
5. **重新打包**：使用 `scratch_utils.pack_sb3()`

### 4. 使用模板

1. 读取 `templates/` 中对应模板文件夹
2. 根据用户需求定制
3. 生成 .sb3 文件

## 积木块 JSON 通用格式

```json
{
  "blockId": {
    "opcode": "opcode_name",
    "next": "nextBlockId",
    "parent": "parentBlockId",
    "inputs": { "INPUT_NAME": [type, value] },
    "fields": { "FIELD_NAME": ["value", null] },
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

### 输入值类型

| 格式 | 含义 |
|------|------|
| `[1, [4, "10"]]` | 数字字面量 |
| `[1, [10, "文本"]]` | 字符串字面量 |
| `[1, [12, "varId", "变量名"]]` | 变量引用 |
| `[2, "blockId"]` | 嵌套 reporter |
| `[3, "blockId", [10, "默认值"]]` | 嵌套 + 默认值 |

数字子类型：`[4, N]` 数字，`[5, N]` 正整数，`[6, N]` 正数，`[7, N]` 整数，`[8, N]` 角度

## 坐标系统

- 舞台：x ∈ [-240, 240]，y ∈ [-180, 180]
- 中心：(0, 0)
- 方向：0° = 上，90° = 右，180° = 下，-90° = 左

## 最佳实践

1. **从简单开始**：先创建基本结构，再逐步添加复杂性
2. **模块化脚本**：每个角色的行为独立，通过广播消息通信
3. **变量命名**：使用有意义的名称（如 `score`、`lives`、`speed`）
4. **使用模板**：从 templates/ 中的模板快速开始
5. **验证项目**：创建后用 `scratch_utils.validate_project()` 验证
6. **测试迭代**：在 Scratch 编辑器中测试，根据问题修改
7. **性能**：避免在 forever 循环中做不必要的计算；合理使用克隆体

## 限制和注意事项

- .sb3 文件是 ZIP 压缩包，project.json 必须在根目录
- 项目文件大小限制（Scratch 在线平台为 50MB）
- 每个角色至少需要一个造型
- Stage 至少需要一个背景
- 扩展需在 project.json 的 `extensions` 数组中声明
