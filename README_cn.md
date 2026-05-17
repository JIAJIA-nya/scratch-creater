# Scratch Creator Skill

> 让 AI Agent 帮你创建和修改 MIT Scratch 3.0 项目（.sb3 文件）。

**English version**: [README.md](README.md)

---

## 目录

- [这是什么？](#这是什么)
- [功能特性](#功能特性)
- [适用 Agent](#适用-agent)
- [环境要求](#环境要求)
- [安装](#安装)
- [目录结构](#目录结构)
- [快速开始](#快速开始)
  - [创建新项目](#创建新项目)
  - [修改已有项目](#修改已有项目)
  - [使用模板](#使用模板)
  - [直接运行脚本](#直接运行脚本)
- [项目工作流](#项目工作流)
  - [第一步：需求分析](#第一步需求分析)
  - [第二步：创建新项目](#第二步创建新项目)
  - [第三步：修改已有项目](#第三步修改已有项目)
  - [第四步：使用模板](#第四步使用模板)
- [理解 .sb3 文件](#理解-sb3-文件)
  - [文件格式](#文件格式)
  - [project.json 结构](#projectjson-结构)
  - [积木块 JSON 格式](#积木块-json-格式)
  - [输入值类型](#输入值类型)
  - [坐标系统](#坐标系统)
- [积木块参考](#积木块参考)
- [Python 脚本 API](#python-脚本-api)
  - [scratch_utils.py](#scratchutilspy)
  - [block_builder.py](#blockbuilderpy)
  - [project_builder.py](#projectbuilderpy)
- [项目模板](#项目模板)
- [最佳实践](#最佳实践)
- [限制和注意事项](#限制和注意事项)
- [资源](#资源)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 这是什么？

Scratch Creator 是一个 AI Agent Skill，让 Claude Code、Cursor、Copilot、Gemini、Codex、Windsurf、Augment、Continue、OpenCode、Amazon Q 等 AI 编程助手能够以编程方式创建、修改和打包 Scratch 3.0 项目。你只需用自然语言描述你想要什么，Agent 就能自动生成项目文件，无需在 Scratch 编辑器中手动拖拽积木块。

Scratch 3.0 由 MIT 开发，全球数百万儿童和教育工作者在使用。其 .sb3 文件格式是开放标准——一个包含 `project.json` 和媒体资源的 ZIP 压缩包。本 Skill 提供了 AI Agent 处理该格式所需的一切。

---

## 功能特性

- **从零创建** — 根据文字描述生成完整的 .sb3 项目
- **修改已有项目** — 解包、编辑、重新打包 .sb3 文件
- **全覆盖积木块** — 194+ 个积木块操作码的参考文档，涵盖所有类别和扩展
- **Python 工具** — 用于打包、解包、验证和程序化构建项目的脚本
- **项目模板** — 10 个常见项目类型的现成模板（动画、游戏、交互故事等）
- **跨 Agent 兼容** — 任何能读取文件和执行代码的 AI Agent 均可使用

---

## 适用 Agent

本 Skill 以 Markdown 文档 + Python 脚本的形式提供。理论上，**任何支持文件读取和代码执行的 AI Agent 都可以使用**。项目根目录下为每个平台提供了专属配置文件：

| # | Agent | 兼容性 | 配置文件 | 说明 |
|---|-------|--------|---------|------|
| 1 | **Claude Code** | 完美 | `CLAUDE.md` + `SKILL.md` | 原生支持 SKILL.md 格式；CLAUDE.md 提供项目级指令 |
| 2 | **Cursor** | 可用 | `.cursor/rules/scratch-creator.mdc` | 自动应用的规则文件；可读取上下文并在终端执行脚本 |
| 3 | **GitHub Copilot** | 可用 | `.github/copilot-instructions.md` | 提供积木块参考、工作流和代码生成指导 |
| 4 | **Gemini CLI** | 可用 | `.gemini/GEMINI.md` | 完整工作流，含 Python API 和积木块索引 |
| 5 | **OpenAI Codex** | 可用 | `.codex/CODEX.md` | 完整工作流，含 Python API 和积木块 JSON 格式参考 |
| 6 | **Windsurf** | 可用 | `.windsurfrules` | Scratch 积木块生成和脚本执行的项目规则 |
| 7 | **Augment** | 可用 | `.augment/rules/scratch-creator.md` | 含积木块索引的上下文感知规则 |
| 8 | **Continue** | 可用 | `.continuerules` | 扩展配置，含快速启动模式和参考表 |
| 9 | **OpenCode** | 可用 | `.opencode/AGENTS.md` | 遵循 OpenCode 规范的完整项目文档 |
| 10 | **Amazon Q** | 可用 | `.amazonq/rules/scratch-creator.md` | 开发规则，含积木块格式和工作流指导 |

**核心原理：** `SKILL.md` 和 `references/` 目录提供了完整的 Scratch 3.0 积木块参考文档，Agent 读取后即可获得所有 opcode 知识。`scripts/` 目录提供了 Python 工具函数，Agent 可以直接调用或翻译为其他语言执行。每个平台的配置文件教 Agent 如何有效使用这些资源。

---

## 环境要求

- **Python 3.7+** — 用于运行工具脚本
- **零外部依赖** — 脚本仅使用 Python 标准库模块（`zipfile`、`json`、`os`、`uuid`、`hashlib`、`shutil`）
- **AI Agent** — Claude Code、Claude Cowork、Codex、OpenCode、Cursor 等

---

## 安装

### 作为 Claude Code / Claude Cowork 的 Skill

1. 克隆或下载本仓库到你的项目目录或 skills 目录。
2. Agent 会自动检测 `SKILL.md` 并将其作为 skill 使用。

```bash
git clone https://github.com/your-repo/scratch-creator.git
```

### 作为独立 Python 库

1. 克隆仓库。
2. 将 `scripts/` 目录复制或软链接到你的项目中。
3. 直接导入使用：

```python
import sys
sys.path.insert(0, 'scripts')
from scratch_utils import create_demo_project, pack_sb3, unpack_sb3, validate_project
from block_builder import make_movesteps, make_say, ScriptBuilder
from project_builder import ScratchProject, quick_project
```

### 开发环境配置

```bash
# 克隆仓库
git clone https://github.com/your-repo/scratch-creator.git
cd scratch-creator

# 无需 pip install — 零外部依赖
# 验证是否正常工作：
python -c "from scripts.scratch_utils import create_demo_project, validate_project; p = create_demo_project(); print('Valid:', validate_project(p)[0])"
```

---

## 目录结构

```
scratch-creator/
├── SKILL.md                        # Agent skill 定义（工作流和使用方法）
├── CLAUDE.md                       # Claude Code 项目文档
├── AGENTS.md                       # OpenCode 项目指令
├── CODEX.md                        # OpenAI Codex CLI 指令
├── GEMINI.md                       # Gemini CLI 项目指令
├── README.md                       # 英文文档
├── README_cn.md                    # 中文文档（本文件）
├── .codex/CODEX.md                 # OpenAI Codex CLI 指令
├── .cursor/rules/                  # Cursor 规则文件
├── .gemini/GEMINI.md               # Gemini CLI 项目指令
├── .github/copilot-instructions.md # GitHub Copilot 指令
├── .opencode/AGENTS.md             # OpenCode 项目指令
├── .windsurfrules                  # Windsurf 项目规则
├── .continuerules                  # Continue 扩展规则
├── .augment/rules/                 # Augment 规则文件
├── .amazonq/rules/                 # Amazon Q 规则文件
├── references/                     # 积木块完整参考文档（194+ 个操作码）
│   ├── blocks-events.md            # 事件类积木块（10 个）
│   ├── blocks-motion.md            # 运动类积木块（18 个）
│   ├── blocks-looks.md             # 外观类积木块（24 个）
│   ├── blocks-sound.md             # 声音类积木块（12 个）
│   ├── blocks-control.md           # 控制类积木块（17 个）
│   ├── blocks-sensing.md           # 侦测类积木块（20 个）
│   ├── blocks-operators.md         # 运算类积木块（18 个）
│   ├── blocks-variables.md         # 变量和列表积木块（17 个）
│   ├── blocks-music.md             # 音乐扩展积木块（7 个）
│   ├── blocks-pen.md               # 画笔扩展积木块（11 个）
│   ├── blocks-video.md             # 视频侦测扩展积木块（3 个）
│   ├── blocks-translate.md         # 翻译扩展积木块（2 个）
│   ├── blocks-texttospeech.md      # 文字朗读扩展积木块（3 个）
│   ├── blocks-microbit.md          # micro:bit 扩展积木块（16 个）
│   ├── blocks-lego.md              # LEGO 扩展积木块（12+ 个）
│   ├── blocks-custom.md            # 自定义积木块（My Blocks）（4 个）
│   └── project-json-schema.md      # project.json 完整结构参考
├── scripts/                        # Python 工具脚本（零外部依赖）
│   ├── __init__.py                 # 包标记
│   ├── scratch_utils.py            # 打包/解包/验证 .sb3 文件
│   ├── block_builder.py            # 积木块流式构建器
│   └── project_builder.py          # 高层项目构建器
└── templates/                      # 项目模板（10 个）
    ├── 01-simple-animation/        # 简单动画（含示例 project.json）
    │   ├── project.json            # 完整可运行的项目文件
    │   └── README.md               # 模板说明
    ├── 02-bouncing-ball/           # 弹跳球（重力模拟）
    ├── 03-quiz-game/               # 问答游戏
    ├── 04-platformer/              # 平台跳跃游戏
    ├── 05-maze-game/               # 迷宫游戏
    ├── 06-pong/                    # 乒乓球游戏
    ├── 07-flappy-bird/             # 飞翔的小鸟
    ├── 08-interactive-story/       # 互动故事
    ├── 09-paint-app/               # 画板应用
    └── 10-multiplayer-chat/        # 多人聊天模拟
```

---

## 快速开始

### 创建新项目

告诉 Agent：

> "帮我创建一个 Scratch 小游戏，玩家用方向键控制角色收集星星"

Agent 会：
1. 读取 `SKILL.md` 了解工作流
2. 读取相关积木块参考文档（运动、事件、控制等）
3. 使用 `scripts/project_builder.py` 创建项目结构
4. 使用 `scripts/block_builder.py` 编写积木脚本
5. 使用 `scripts/scratch_utils.py` 打包为 .sb3 文件
6. 使用 `validate_project()` 验证输出

### 修改已有项目

> "帮我把这个 .sb3 文件中的角色移动速度改快一点"

Agent 会：
1. 使用 `unpack_sb3()` 解包 .sb3 文件
2. 读取并分析 `project.json`
3. 读取相关积木块参考确认正确的 opcode
4. 修改积木块参数（例如修改 `STEPS` 输入值）
5. 使用 `pack_sb3()` 重新打包

### 使用模板

> "用平台跳跃模板创建一个新游戏"

Agent 会：
1. 读取 `templates/04-platformer/README.md` 中的模板描述
2. 根据用户需求定制
3. 生成完整的 .sb3 文件

### 直接运行脚本

你也可以不通过 AI Agent，直接使用 Python 脚本：

```python
import sys
sys.path.insert(0, 'scripts')
from scratch_utils import create_demo_project, pack_sb3, validate_project, create_project_directory

# 创建演示项目
project = create_demo_project()

# 验证
is_valid, issues = validate_project(project)
print("Valid:", is_valid)

# 保存为 .sb3
create_project_directory(project, 'my_project')
pack_sb3('my_project', 'my_project.sb3')
print("已创建 my_project.sb3")
```

---

## 项目工作流

### 第一步：需求分析

创建项目前，需要了解：

- **项目类型**：动画、游戏、交互故事、还是教学演示？
- **目标受众**：儿童自学、课堂教学、还是个人项目？
- **复杂度**：简单演示还是完整游戏？
- **现有资源**：用户是否已有需要导入的素材？
- **是否需要扩展**：音乐、画笔、视频侦测、翻译、micro:bit、LEGO？

### 第二步：创建新项目

1. 读取 `references/project-json-schema.md` 了解完整结构
2. 根据项目类型读取对应积木块参考文档（见下方积木块索引）
3. 使用 `scripts/project_builder.py` 创建项目结构
4. 使用 `scripts/block_builder.py` 编写积木脚本
5. 使用 `scripts/scratch_utils.py` 打包为 .sb3

### 第三步：修改已有项目

1. **解包** .sb3：`unpack_sb3('file.sb3')` → 返回 `(project_dir, project_data)`
2. **读取** project.json：分析角色、脚本、媒体资源
3. **读取** 对应积木块参考确认需要修改的 opcode
4. **修改** project.json（更改 inputs、fields、添加/删除积木块）
5. **重新打包**：`pack_sb3(project_dir, 'output.sb3')`

### 第四步：使用模板

1. 读取 `templates/` 中对应模板文件夹的 `README.md`
2. 根据用户需求定制
3. 生成 .sb3 文件

---

## 理解 .sb3 文件

### 文件格式

.sb3 文件是一个 ZIP 压缩包，包含：
- `project.json` — 项目核心数据（角色、背景、脚本、变量）
- 媒体文件 — SVG/PNG 造型、WAV/MP3 声音（通过哈希值引用）

### project.json 结构

```json
{
  "targets": [ /* 舞台 + 角色列表 */ ],
  "monitors": [ /* 变量监视器 */ ],
  "extensions": [ /* 使用的扩展 */ ],
  "meta": {
    "semver": "3.0.0",
    "vm": "0.2.0",
    "agent": "Mozilla/5.0 ..."
  }
}
```

每个 **target** 要么是舞台（`isStage: true`），要么是角色（`isStage: false`）。每个 target 包含：
- `variables` — `{变量ID: [变量名, 初始值]}`
- `lists` — `{列表ID: [列表名, [项目1, 项目2]]}`
- `broadcasts` — `{消息ID: 消息名}`
- `blocks` — `{积木块ID: 积木块数据}`
- `costumes` — 造型描述符数组
- `sounds` — 声音描述符数组

### 积木块 JSON 格式

```json
{
  "blockId": {
    "opcode": "motion_movesteps",
    "next": "nextBlockId",
    "parent": "parentBlockId",
    "inputs": {
      "STEPS": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

- `opcode` — 积木块类型标识符（如 `motion_movesteps`）
- `next` — 下方连接的积木块 ID（纵向堆叠连接）
- `parent` — 上方连接的积木块 ID
- `inputs` — 输入槽（reporter、下拉菜单）
- `fields` — 固定字段值（如下拉选择）
- `shadow` — `true` 表示这是阴影块（不可被用户代码覆盖的默认值）
- `topLevel` — `true` 表示这是帽子块（脚本入口点）
- `x`, `y` — 在工作区中的坐标

### 输入值类型

| 格式 | 含义 |
|------|------|
| `[1, [4, "10"]]` | 数字字面量 |
| `[1, [10, "文本"]]` | 字符串字面量 |
| `[1, [12, "varId", "变量名"]]` | 变量引用 |
| `[2, "blockId"]` | 嵌套 reporter（来自另一个积木块的返回值） |
| `[3, "blockId", [10, "默认值"]]` | 嵌套 reporter + 默认值回退 |

**数字子类型：**
| 代码 | 类型 |
|------|------|
| `[4, N]` | 数字 |
| `[5, N]` | 正整数 |
| `[6, N]` | 正数 |
| `[7, N]` | 整数 |
| `[8, N]` | 角度 |

### 坐标系统

- 舞台大小：480 × 360 像素
- x 范围：[-240, 240]
- y 范围：[-180, 180]
- 中心点：(0, 0)
- 方向：0° = 上，90° = 右，180° = 下，-90° = 左

---

## 积木块参考

覆盖所有 Scratch 3.0 积木块的完整操作码文档：

| 类别 | 积木块数量 | 参考文件 |
|------|-----------|---------|
| 事件 | 10 | `references/blocks-events.md` |
| 运动 | 18 | `references/blocks-motion.md` |
| 外观 | 24 | `references/blocks-looks.md` |
| 声音 | 12 | `references/blocks-sound.md` |
| 控制 | 17 | `references/blocks-control.md` |
| 侦测 | 20 | `references/blocks-sensing.md` |
| 运算 | 18 | `references/blocks-operators.md` |
| 变量和列表 | 17 | `references/blocks-variables.md` |
| 音乐扩展 | 7 | `references/blocks-music.md` |
| 画笔扩展 | 11 | `references/blocks-pen.md` |
| 视频侦测扩展 | 3 | `references/blocks-video.md` |
| 翻译扩展 | 2 | `references/blocks-translate.md` |
| 文字朗读扩展 | 3 | `references/blocks-texttospeech.md` |
| micro:bit 扩展 | 16 | `references/blocks-microbit.md` |
| LEGO 扩展 | 12+ | `references/blocks-lego.md` |
| 自定义积木 | 4 | `references/blocks-custom.md` |
| **合计** | **194+** | |

每个参考文件包含：
- 所有操作码的表格，含名称和说明
- 可用的字段值和下拉菜单选项
- 每个积木块的完整 JSON 示例

---

## Python 脚本 API

### scratch_utils.py

.sb3 文件操作的核心工具函数。**零外部依赖。**

| 函数 | 说明 |
|------|------|
| `unpack_sb3(sb3_path, output_dir=None)` | 将 .sb3 文件解压到目录。返回 `(project_dir, project_data)`。 |
| `pack_sb3(project_dir, output_path)` | 将目录打包为 .sb3 文件。 |
| `create_empty_project()` | 创建一个最小的空项目字典（仅舞台）。 |
| `add_sprite(project_data, name, x=0, y=0, ...)` | 向项目中添加角色。返回角色字典。 |
| `add_backdrop(stage, name, svg_content=None)` | 向舞台添加背景。 |
| `create_block(opcode, inputs, fields, ...)` | 创建单个积木块字典。返回 `(block_id, block_dict)`。 |
| `add_block_to_target(target, block_id, block_dict)` | 将积木块添加到目标（角色/舞台）。 |
| `create_simple_script(target, blocks_list)` | 将一系列积木块连接成脚本链。返回第一个积木块 ID。 |
| `validate_project(project_data)` | 验证项目完整性。返回 `(is_valid, issues)`。 |
| `create_project_directory(project_data, output_dir, media_files=None)` | 将项目写入磁盘。 |
| `create_demo_project()` | 创建演示项目（绿旗 → 说"你好" → 移动）。 |
| `generate_block_id()` | 生成随机积木块 ID。 |
| `num(value)` | 创建数字输入：`[1, [4, str(value)]]` |
| `str_input(value)` | 创建字符串输入：`[1, [10, str(value)]]` |
| `var_ref(variable_name, var_id)` | 创建变量引用输入。 |
| `block_ref(block_id)` | 创建嵌套 reporter 引用：`[2, block_id]` |
| `block_ref_with_default(block_id, default)` | 带默认值的 reporter：`[3, block_id, [10, default]]` |
| `field_value(value)` | 创建字段值：`[value, None]`` |

**命令行用法：**
```bash
python scripts/scratch_utils.py
# 创建 demo_project/ 目录和 demo_project.sb3
```

### block_builder.py

用于创建单个积木块和脚本的流式构建器。每个函数返回 `BlockBuilder` 或 `ScriptBuilder` 对象。

**便捷积木块构建函数（部分）：**

| 函数 | 积木块 |
|------|--------|
| `make_event_whenflagclicked()` | 当绿旗被点击 |
| `make_event_whenkeypressed(key)` | 当按下某键 |
| `make_event_whenbroadcastreceived(name, id)` | 当接收到消息 |
| `make_broadcast(name, id)` | 广播消息 |
| `make_movesteps(steps)` | 移动 N 步 |
| `make_turnright(degrees)` / `make_turnleft(degrees)` | 右转/左转 N 度 |
| `make_gotoxy(x, y)` / `make_glidesecstoxy(secs, x, y)` | 移动到 x,y / 滑行到 x,y |
| `make_pointindirection(dir)` / `make_pointtowards(target)` | 面向方向 / 面向... |
| `make_say(msg)` / `make_sayforseconds(msg, secs)` | 说... / 说... N 秒 |
| `make_think(msg)` | 想... |
| `make_show()` / `make_hide()` | 显示 / 隐藏 |
| `make_nextcostume()` / `make_switchcostumeto(name)` | 下一个造型 / 切换造型 |
| `make_changesizeby(n)` / `make_setsizeto(n)` | 大小增加 / 大小设为 |
| `make_changeeffectby(effect, n)` / `make_seteffectto(effect, n)` | 特效增加 / 特效设为 |
| `make_wait(secs)` | 等待 N 秒 |
| `make_repeat(n)` / `make_forever()` | 重复 N 次 / 重复执行 |
| `make_if()` / `make_if_else()` | 如果...那么 / 如果...那么...否则 |
| `make_stop_all()` / `make_stop_this()` | 停止全部脚本 / 停止这个脚本 |
| `make_start_as_clone()` | 当作为克隆体启动时 |
| `make_create_clone_of(target)` | 克隆... |
| `make_play_sound(name)` / `make_playuntildone(name)` | 播放声音 / 播放声音直到结束 |
| `make_setinstrument(n)` / `make_playdrum(drum, beats)` | 设置乐器 / 击打...拍 |
| `make_playnote(note, beats)` / `make_rest(beats)` | 演奏音符 / 休止...拍 |
| `make_settempo(bpm)` | 将演奏速度设为... |
| `make_ask(question)` | 询问...并等待 |
| `make_pen_clear()` / `make_pen_down()` / `make_pen_up()` | 清空画笔 / 落笔 / 抬笔 |
| `make_setpencolor(hex)` / `make_setpensize(n)` | 设置画笔颜色 / 大小 |

**Reporter 积木块：** `reporter_add()`、`reporter_subtract()`、`reporter_multiply()`、`reporter_divide()`、`reporter_random()`、`reporter_gt()`、`reporter_lt()`、`reporter_equals()`、`reporter_and()`、`reporter_or()`、`reporter_not()`、`reporter_join()`、`reporter_letter_of()`、`reporter_length()`、`reporter_mod()`、`reporter_round()`、`reporter_mathop()`、`reporter_xposition()`、`reporter_yposition()`、`reporter_direction()`、`reporter_size()`、`reporter_volume()`、`reporter_answer()`、`reporter_mousex()`、`reporter_mousey()`、`reporter_loudness()`、`reporter_timer()`、`reporter_dayssince2000()`、`reporter_username()`、`reporter_current()`、`reporter_music_tempo()`

**输入辅助函数：** `num()`、`positive_int()`、`positive_num()`、`integer()`、`angle()`、`string()`、`variable_ref()`、`block_ref()`、`block_ref_default()`、`field_val()`、`color_val()`

**ScriptBuilder 示例：**
```python
from block_builder import ScriptBuilder, make_event_whenflagclicked

script = ScriptBuilder()
script.add("event_whenflagclicked", is_top_level=True)
script.add("motion_movesteps", inputs={"STEPS": num(10)})
script.add("looks_say", inputs={"MESSAGE": string("Hello!")})
blocks = script.build()
# 将 blocks 添加到 target["blocks"]
```

### project_builder.py

高层项目构建器，用于以编程方式创建完整的 Scratch 项目。

**ScratchProject 类：**

| 方法 | 说明 |
|------|------|
| `create_stage(name="Stage")` | 创建舞台 target |
| `create_sprite(name, x=0, y=0, size=100, direction=90)` | 创建角色 |
| `add_variable(target, var_name, initial_value=0)` | 添加变量。返回变量 ID。 |
| `add_list(target, list_name, initial_items=None)` | 添加列表。返回列表 ID。 |
| `add_broadcast(target, msg_name)` | 添加广播消息。返回消息 ID。 |
| `add_costume(target, name, data_format="svg", ...)` | 向 target 添加造型 |
| `add_sound(target, name, data_format="wav", ...)` | 向 target 添加声音 |
| `add_block(target, opcode, inputs, fields, ...)` | 添加单个积木块。返回积木块 ID。 |
| `add_blocks_from_chain(target, blocks_list)` | 添加连接的积木块链。 |
| `add_extension(ext_name)` | 注册扩展（如 `"pen"`、`"music"`） |
| `to_dict()` | 导出为 project.json 字典 |
| `save_json(filepath)` | 将 project.json 保存到文件 |
| `validate()` | 验证项目。返回 `(is_valid, issues)`。 |

**便捷函数：** `quick_project(sprite_name="Sprite1")` — 创建一个最小项目，包含舞台（空白背景）和一个角色（一个造型），可直接添加脚本。

**完整示例：**
```python
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()

# 舞台
stage = proj.create_stage()

# 玩家角色
player = proj.create_sprite("Player", x=0, y=0)

# 添加分数变量
score_id = proj.add_variable(stage, "score", 0)

# 脚本：当绿旗被点击 → 重复执行 → 移动 10 步 → 碰到边缘反弹
proj.add_blocks_from_chain(player, [
    ("event_whenflagclicked", {}, {}),
    ("control_forever", {"SUBSTACK": [2, "move_block"]}, {}),
])

# 保存
proj.save_json("my_game/project.json")
```

---

## 项目模板

10 个项目模板，覆盖常见 Scratch 项目类型。每个模板包含 README，说明设计思路、所需积木块和角色要求。

| # | 模板 | 难度 | 涉及概念 |
|---|------|------|---------|
| 01 | [简单动画](templates/01-simple-animation/) | 入门 | 事件触发、无限循环、造型切换、碰到边缘反弹 |
| 02 | [弹跳球](templates/02-bouncing-ball/) | 入门 | 重力模拟、变量、反弹 |
| 03 | [问答游戏](templates/03-quiz-game/) | 入门 | 变量、条件判断、询问与回答 |
| 04 | [平台跳跃](templates/04-platformer/) | 中级 | 键盘输入、重力、碰撞检测 |
| 05 | [迷宫游戏](templates/05-maze-game/) | 中级 | 键盘输入、碰撞检测、广播消息 |
| 06 | [乒乓球](templates/06-pong/) | 中级 | 运动、碰撞检测、计分、变量 |
| 07 | [飞翔的小鸟](templates/07-flappy-bird/) | 中级 | 重力、克隆体、碰撞检测、计分 |
| 08 | [互动故事](templates/08-interactive-story/) | 入门 | 广播消息、背景切换、对话 |
| 09 | [画板应用](templates/09-paint-app/) | 高级 | 画笔扩展、鼠标输入、克隆体 |
| 10 | [多人聊天](templates/10-multiplayer-chat/) | 高级 | 云变量、消息传递、列表 |

---

## 最佳实践

1. **从简单开始** — 先创建基本结构，再逐步添加复杂性
2. **模块化脚本** — 每个角色的行为独立，通过广播消息通信
3. **变量命名** — 使用有意义的名称（如 `score`、`lives`、`speed`）
4. **使用模板** — 从 templates/ 中的模板快速开始
5. **验证项目** — 创建后用 `scratch_utils.validate_project()` 验证
6. **测试迭代** — 在 Scratch 编辑器中测试，根据问题修改
7. **性能** — 避免在 forever 循环中做不必要的计算；合理使用克隆体
8. **清理克隆体** — 克隆体不再使用时，务必使用 `delete this clone`

---

## 限制和注意事项

- .sb3 文件是 ZIP 压缩包，project.json 必须在根目录（不能在子目录中）
- Scratch 在线平台有 50 MB 的项目文件大小限制
- 每个角色至少需要一个造型
- Stage 至少需要一个背景
- 扩展需在 project.json 的 `extensions` 数组中声明
- 媒体文件（造型、声音）需要正确的 `assetId` 和 `md5ext` 字段才能被 Scratch 编辑器识别
- 本 Skill 生成项目 JSON 结构，但不创建图像/音频资源——这些需要单独提供或使用 Scratch 内置素材

---

## 资源

- [MIT Scratch](https://scratch.mit.edu/) — Scratch 官方网站
- [Scratch Wiki - 文件格式](https://en.scratch-wiki.info/wiki/Scratch_File_Format) — 详细文件格式文档
- [Scratch Wiki - 积木块语法](https://en.scratch-wiki.info/wiki/Scratch_File_Format/Block_Selection) — 积木块选择参考
- [Scratch 3.0 文件格式 (GitHub)](https://github.com/scratchfoundation/scratch-vm) — scratch-vm 源码
- [Scratch Blocks](https://github.com/scratchfoundation/scratch-blocks) — 可视化积木块编辑器

---

## 贡献

欢迎贡献：
- 新的项目模板
- 积木块参考文档补充
- 脚本改进或 bug 修复
- 翻译

---

