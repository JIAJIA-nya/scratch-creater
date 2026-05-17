---
name: scratch-creator
description: "协助用户创建和修改 MIT Scratch 3.0 项目（.sb3 文件）。涵盖从零创建项目、添加角色和背景、用积木块编写脚本、修改现有项目、以及打包发布。当用户提到 Scratch 编程、创建动画/游戏/交互故事、或处理 .sb3 文件时触发。"
---

# Scratch Creator Skill

协助用户创建和修改 MIT Scratch 3.0 项目。.sb3 文件本质上是一个 ZIP 压缩包，包含 project.json 和媒体资源。

## 核心工作流

### 1. 需求分析

开始创建前，了解：

- **项目类型**：动画、游戏、交互故事、教学演示？
- **目标受众**：儿童自学、课堂教学、个人项目？
- **复杂度**：简单演示 vs 完整游戏（是否需要变量、克隆、列表等高级特性）？
- **现有资源**：用户是否已有素材（图片、声音）需要导入？

### 2. 从零创建新项目

#### 2.1 项目结构

一个 .sb3 文件解包后的结构：

```
project/
├── project.json          # 核心：包含所有角色、背景、积木脚本
├── (可选媒体文件)
    ├── (md5).svg         # 矢量角色造型
    ├── (md5).png         # 位图角色造型
    ├── (md5).wav         # 音效
    └── (md5).mp3         # 背景音乐
```

#### 2.2 project.json 顶层结构

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
      "costumes": [],
      "sounds": [],
      "volume": 100,
      "layerOrder": 0
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

#### 2.3 创建步骤

1. **创建项目目录和初始 project.json**：
   - Stage 至少有一个 costume（背景）
   - 添加用户需要的 Sprite（角色）

2. **添加造型（Costumes）**：
   - 每个角色至少需要一个造型
   - SVG 矢量格式优先（Scratch 编辑器默认使用）
   - 造型需要放入项目目录，md5 命名

3. **编写积木脚本（Blocks）**：
   - 使用 Scratch 积木块语法
   - 参考下方「积木块编写指南」

4. **打包为 .sb3**：
   - 将项目目录打包为 ZIP，重命名为 .sb3
   - 确保 project.json 在根目录

### 3. 修改现有项目

1. **解包 .sb3**：将 .sb3 重命名为 .zip 并解压
2. **读取 project.json**：分析角色、脚本、媒体资源
3. **修改**：
   - 添加/删除角色：修改 targets 数组
   - 修改脚本：编辑对应 target 的 blocks 对象
   - 添加媒体：放入文件并更新 costumes/sounds 数组
4. **重新打包**：ZIP 打包后改回 .sb3

### 4. 积木块编写指南

#### 4.1 积木块 JSON 格式

每个积木块是一个 key-value 对：

```json
{
  "blockId": {
    "opcode": "event_whenflagclicked",
    "next": "nextBlockId",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

#### 4.2 常用积木块参考

**事件类：**
| opcode | 说明 |
|--------|------|
| `event_whenflagclicked` | 点击绿旗时 |
| `event_whenkeypressed` | 按下某键时 |
| `event_whenthisspriteclicked` | 点击角色时 |
| `event_whenbroadcastreceived` | 接收到消息时 |
| `event_whenbackdropswitchesto` | 背景切换到 |

**运动类：**
| opcode | 说明 |
|--------|------|
| `motion_movesteps` | 移动 N 步 |
| `motion_turnright` | 右转 N 度 |
| `motion_turnleft` | 左转 N 度 |
| `motion_gotoxy` | 移动到 x,y |
| `motion_glideto` | 滑行到 |
| `motion_pointindirection` | 面向方向 |
| `motion_changebyx` | x 变化 |
| `motion_changebyy` | y 变化 |
| `motion_setx` | 设置 x |
| `motion_sety` | 设置 y |
| `motion_ifonedgebounce` | 碰到边缘反弹 |

**外观类：**
| opcode | 说明 |
|--------|------|
| `looks_say` | 说 "你好" |
| `looks_sayforseconds` | 说 N 秒 |
| `looks_switchcostumeto` | 切换造型 |
| `looks_nextcostume` | 下一个造型 |
| `looks_switchbackdropto` | 切换背景 |
| `looks_changesizeby` | 大小变化 |
| `looks_setsizeto` | 设置大小 |
| `looks_show` | 显示 |
| `looks_hide` | 隐藏 |
| `looks_gotofrontback` | 移到最前面/最后面 |

**声音类：**
| opcode | 说明 |
|--------|------|
| `sound_play` | 播放声音 |
| `sound_playuntildone` | 播放并等待 |
| `sound_stopallsounds` | 停止所有声音 |
| `sound_changevolumeby` | 音量变化 |
| `sound_setvolumeto` | 设置音量 |

**控制类：**
| opcode | 说明 |
|--------|------|
| `control_wait` | 等待 N 秒 |
| `control_repeat` | 重复 N 次 |
| `control_forever` | 永远重复 |
| `control_if` | 如果...那么 |
| `control_if_else` | 如果...那么...否则 |
| `control_wait_until` | 等待直到 |
| `control_repeat_until` | 重复直到 |
| `control_stop` | 停止 |
| `control_start_as_clone` | 当作为克隆体启动时 |
| `control_create_clone_of` | 克隆 |
| `control_delete_this_clone` | 删除此克隆体 |

**侦测类：**
| opcode | 说明 |
|--------|------|
| `sensing_touchingobject` | 碰到... |
| `sensing_touchingcolor` | 碰到颜色 |
| `sensing_coloristouchingcolor` | 颜色碰到颜色 |
| `sensing_distanceto` | 到...的距离 |
| `sensing_askandwait` | 询问并等待 |
| `sensing_answer` | 回答 |
| `sensing_keypressed` | 按下某键 |
| `sensing_mousedown` | 按下鼠标 |
| `sensing_mousex` | 鼠标 x |
| `sensing_mousey` | 鼠标 y |

**运算类：**
| opcode | 说明 |
|--------|------|
| `operator_add` | 加 |
| `operator_subtract` | 减 |
| `operator_multiply` | 乘 |
| `operator_divide` | 除 |
| `operator_random` | 随机数 |
| `operator_gt` | 大于 |
| `operator_lt` | 小于 |
| `operator_equals` | 等于 |
| `operator_and` | 且 |
| `operator_or` | 或 |
| `operator_not` | 不成立 |
| `operator_join` | 连接字符串 |
| `operator_letter_of` | 第 N 个字符 |
| `operator_length` | 字符串长度 |
| `operator_mod` | 取余 |
| `operator_round` | 四舍五入 |
| `operator_mathop` | 数学函数 |

**变量类：**
| opcode | 说明 |
|--------|------|
| `data_setvariableto` | 设置变量 |
| `data_changevariableby` | 变量增加 |
| `data_showvariable` | 显示变量 |
| `data_hidevariable` | 隐藏变量 |
| `data_addtolist` | 添加到列表 |
| `data_deleteoflist` | 删除列表项 |
| `data_insertatlist` | 插入列表项 |
| `data_replaceitemoflist` | 替换列表项 |
| `data_itemoflist` | 列表项 |
| `data_lengthoflist` | 列表长度 |

#### 4.3 积木块连接示例

**简单序列（点击绿旗 → 移动10步 → 说"你好"）：**

```json
{
  "abc123": {
    "opcode": "event_whenflagclicked",
    "next": "def456",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "def456": {
    "opcode": "motion_movesteps",
    "next": "ghi789",
    "parent": "abc123",
    "inputs": {
      "STEPS": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "ghi789": {
    "opcode": "looks_say",
    "next": null,
    "parent": "def456",
    "inputs": {
      "MESSAGE": [1, [10, "你好"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

**带循环和条件的示例：**

```json
{
  "start": {
    "opcode": "event_whenflagclicked",
    "next": "loop",
    "parent": null,
    "inputs": {},
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "loop": {
    "opcode": "control_forever",
    "next": null,
    "parent": "start",
    "inputs": {
      "SUBSTACK": [2, "if_cond"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "if_cond": {
    "opcode": "control_if_else",
    "next": null,
    "parent": "loop",
    "inputs": {
      "CONDITION": [2, "touching"],
      "SUBSTACK": [2, "say_hit"],
      "SUBSTACK2": [2, "say_miss"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "touching": {
    "opcode": "sensing_touchingobject",
    "next": null,
    "parent": "if_cond",
    "inputs": {
      "TOUCHINGOBJECTMENU": [1, "edge_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "edge_id": {
    "opcode": "sensing_touchingobjectmenu",
    "next": null,
    "parent": "touching",
    "inputs": {},
    "fields": {
      "TOUCHINGOBJECTMENU": ["_edge_", null]
    },
    "shadow": true,
    "topLevel": false
  },
  "say_hit": {
    "opcode": "looks_say",
    "next": null,
    "parent": "if_cond",
    "inputs": {
      "MESSAGE": [1, [10, "碰到边缘了！"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "say_miss": {
    "opcode": "looks_say",
    "next": null,
    "parent": "say_hit",
    "inputs": {
      "MESSAGE": [1, [10, "继续前进"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

#### 4.4 输入值格式

积木块输入使用特定数组格式：

| 格式 | 含义 | 示例 |
|------|------|------|
| `[1, [4, "10"]]` | 数字字面量 10 | 移动10步 |
| `[1, [10, "你好"]]` | 字符串字面量 "你好" | 说 "你好" |
| `[1, [12, "myVar", "变量名"]]` | 读取变量 | 使用变量值 |
| `[2, "blockId"]` | 引用另一个积木块的输出 | 嵌套表达式 |
| `[3, "blockId", [10, "默认值"]]` | 引用 + 默认值 | 条件中的嵌套 |

数字类型编码：
- `[4, "N"]` — 数字
- `[5, "N"]` — 正整数
- `[6, "N"]` — 正数
- `[7, "N"]` — 整数
- `[8, "N"]` — 角度

### 5. 角色（Sprite）完整示例

```json
{
  "isStage": false,
  "name": "Cat",
  "variables": {},
  "lists": {},
  "broadcasts": {},
  "blocks": {},
  "comments": {},
  "currentCostume": 0,
  "costumes": [
    {
      "assetId": "83a9787d4cb6f3b7632b4ddfebf74367",
      "name": "cat-a",
      "bitmapResolution": 1,
      "md5ext": "83a9787d4cb6f3b7632b4ddfebf74367.svg",
      "dataFormat": "svg",
      "rotationCenterX": 48,
      "rotationCenterY": 50
    }
  ],
  "sounds": [
    {
      "assetId": "83c36d806dc92327b9e7049a565c6bff",
      "name": "Meow",
      "dataFormat": "wav",
      "rate": 48000,
      "sampleCount": 40194,
      "md5ext": "83c36d806dc92327b9e7049a565c6bff.wav"
    }
  ],
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

### 6. 坐标系统

- Scratch 舞台：x 范围 -240 到 240，y 范围 -180 到 180
- 中心点：(0, 0)
- 方向：0 = 上，90 = 右，180 = 下，-90 = 左

### 7. 打包/解包操作

#### 解包 .sb3

```python
import zipfile, json, os

def unpack_sb3(sb3_path, output_dir):
    """将 .sb3 文件解压到目录"""
    with zipfile.ZipFile(sb3_path, 'r') as z:
        z.extractall(output_dir)
    # 读取 project.json
    json_path = os.path.join(output_dir, 'project.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)
```

#### 打包为 .sb3

```python
import zipfile, json, os

def pack_sb3(project_dir, output_path):
    """将目录打包为 .sb3 文件"""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, project_dir)
                z.write(filepath, arcname)
```

### 8. 最佳实践

1. **从简单开始**：先创建基本结构，再逐步添加复杂性
2. **模块化脚本**：每个角色的行为独立，通过广播消息通信
3. **变量命名**：使用有意义的名称（如 `score`、`lives`、`speed`）
4. **注释**：在 project.json 的 comments 字段中添加注释说明复杂逻辑
5. **测试迭代**：创建后在 Scratch 编辑器中测试，根据问题修改
6. **性能**：避免在 forever 循环中做不必要的计算；合理使用克隆体

### 9. 常见项目模板

#### 简单动画
- 角色在舞台上移动
- 循环切换造型产生动画效果
- 碰到边缘反弹

#### 平台跳跃游戏
- 重力模拟（y 坐标持续减小）
- 键盘控制（左右移动 + 跳跃）
- 碰撞检测（碰到平台停止下落）
- 计分变量

#### 问答游戏
- 使用 `sensing_askandwait` 提问
- `sensing_answer` 获取回答
- 条件判断对错并计分

#### 互动故事
- 多背景切换
- 角色对话
- 用户选择分支

### 10. 限制和注意事项

- Scratch 3.0 支持的扩展：音乐、画笔、视频侦测、文字朗读、翻译、micro:bit、LEGO 等
- 自定义积木块使用 `procedures_definition` 和 `procedures_call` opcode
- 项目文件大小限制（Scratch 在线平台为 50MB）
- 角色和背景数量合理控制以保证性能
