# 控制类积木块 (Control)

> 参考文件：`references/blocks-control.md` | 共 16 个积木块

控制类积木块管理程序的执行流程，包括循环、条件、等待和克隆。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `control_wait` | 等待 N 秒 | INPUT: `DURATION` |
| `control_repeat` | 重复执行 N 次 | INPUT: `TIMES`, SUBSTACK |
| `control_forever` | 重复执行 | SUBSTACK |
| `control_if` | 如果 ... 那么 | INPUT: `CONDITION`, SUBSTACK |
| `control_if_else` | 如果 ... 那么 ... 否则 | INPUT: `CONDITION`, SUBSTACK, SUBSTACK2 |
| `control_wait_until` | 等待 ... | INPUT: `CONDITION` |
| `control_repeat_until` | 重复执行直到 ... | INPUT: `CONDITION`, SUBSTACK |
| `control_while` | 当 ... 重复执行 | INPUT: `CONDITION`, SUBSTACK |
| `control_for_each` | 重复执行 ... 次（带变量） | FIELD: `VARIABLE`, INPUT: `VALUE`, SUBSTACK |
| `control_stop` | 停止 ... | FIELD: `STOP_OPTION` |
| `control_start_as_clone` | 当作为克隆体启动时 | 事件触发器 |
| `control_create_clone_of` | 克隆 ... | INPUT: `CLONE_OPTION` |
| `control_delete_this_clone` | 删除此克隆体 | 仅克隆体可用 |
| `control_get_counter` | 计数器 | reporter，返回计数器值 |
| `control_incr_counter` | 计数器增加 1 | 无参数 |
| `control_clear_counter` | 计数器归零 | 无参数 |
| `control_all_at_once` | 全部执行 | SUBSTACK（加速执行） |

## 字段值

### control_stop 的 STOP_OPTION
- `["all", null]` — 全部脚本
- `["this script", null]` — 这个脚本
- `["other scripts in sprite", null]` — 该角色的其他脚本

### control_create_clone_of 的 CLONE_OPTION
- `["_myself_", null]` — 自己（克隆自己）
- 或引用其他角色名

### control_for_each 的 VARIABLE
- `["counter", null]` — 计数器变量名

## JSON 示例

### 等待 1 秒
```json
{
  "block": {
    "opcode": "control_wait",
    "next": null,
    "parent": "prev",
    "inputs": { "DURATION": [1, [5, "1"]] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 重复 10 次
```json
{
  "block": {
    "opcode": "control_repeat",
    "next": null,
    "parent": "prev",
    "inputs": {
      "TIMES": [1, [6, "10"]],
      "SUBSTACK": [2, "first_block_in_loop"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 重复执行（forever）
```json
{
  "block": {
    "opcode": "control_forever",
    "next": null,
    "parent": "prev",
    "inputs": { "SUBSTACK": [2, "first_block_in_loop"] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 如果 ... 那么
```json
{
  "block": {
    "opcode": "control_if",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CONDITION": [2, "condition_block"],
      "SUBSTACK": [2, "first_block_in_then"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 如果 ... 那么 ... 否则
```json
{
  "block": {
    "opcode": "control_if_else",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CONDITION": [2, "condition_block"],
      "SUBSTACK": [2, "first_block_in_then"],
      "SUBSTACK2": [2, "first_block_in_else"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 等待直到
```json
{
  "block": {
    "opcode": "control_wait_until",
    "next": null,
    "parent": "prev",
    "inputs": { "CONDITION": [2, "condition_block"] },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 重复执行直到
```json
{
  "block": {
    "opcode": "control_repeat_until",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CONDITION": [2, "condition_block"],
      "SUBSTACK": [2, "first_block_in_loop"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 当 ... 重复执行（while）
```json
{
  "block": {
    "opcode": "control_while",
    "next": null,
    "parent": "prev",
    "inputs": {
      "CONDITION": [2, "condition_block"],
      "SUBSTACK": [2, "first_block_in_loop"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 停止全部脚本
```json
{
  "block": {
    "opcode": "control_stop",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": { "STOP_OPTION"