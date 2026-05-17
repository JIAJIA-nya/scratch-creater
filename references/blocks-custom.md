# 自定义积木块 (Custom Blocks / My Blocks)

> 参考文件：`references/blocks-custom.md` | 共 4 个积木块

自定义积木块允许用户定义自己的可复用积木，类似函数/过程。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `procedures_definition` | 定义 ... | 定义自定义积木的入口 |
| `procedures_call` | 调用 ... | 调用自定义积木 |
| `argument_reporter_string_number` | （字符串/数字参数） | reporter，读取参数值 |
| `argument_reporter_boolean` | （布尔参数） | reporter，读取布尔参数 |

## 自定义积木定义结构

自定义积木在 target 的 `blocks` 中使用 `procedures_definition` 定义：

```json
{
  "definition_id": {
    "opcode": "procedures_definition",
    "next": null,
    "parent": null,
    "inputs": {
      "custom_block": [1, "prototype_id"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "prototype_id": {
    "opcode": "procedures_prototype",
    "next": null,
    "parent": null,
    "inputs": {
      "param1_id": [1, "param1_shadow_id"],
      "param2_id": [1, "param2_shadow_id"]
    },
    "fields": {},
    "shadow": true,
    "topLevel": false
  }
}
```

## 参数类型

参数通过 shadow 块指定类型：
- `argument_reporter_string_number` — 字符串/数字参数
- `argument_reporter_boolean` — 布尔参数

## JSON 示例

### 定义 "移动 N 步并说 M" 自定义积木

```json
{
  "def_block": {
    "opcode": "procedures_definition",
    "next": "move_block",
    "parent": null,
    "inputs": {
      "custom_block": [1, "proto_block"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  },
  "proto_block": {
    "opcode": "procedures_prototype",
    "next": null,
    "parent": null,
    "inputs": {
      "param_steps": [1, "param_steps_shadow"],
      "param_msg": [1, "param_msg_shadow"]
    },
    "fields": {},
    "shadow": true,
    "topLevel": false
  },
  "param_steps_shadow": {
    "opcode": "argument_reporter_string_number",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VALUE": ["步数", null]
    },
    "shadow": true,
    "topLevel": false
  },
  "param_msg_shadow": {
    "opcode": "argument_reporter_string_number",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VALUE": ["消息", null]
    },
    "shadow": true,
    "topLevel": false
  },
  "move_block": {
    "opcode": "motion_movesteps",
    "next": "say_block",
    "parent": "def_block",
    "inputs": {
      "STEPS": [3, "ref_steps", [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "ref_steps": {
    "opcode": "argument_reporter_string_number",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VALUE": ["步数", null]
    },
    "shadow": false,
    "topLevel": false
  },
  "say_block": {
    "opcode": "looks_say",
    "next": null,
    "parent": "move_block",
    "inputs": {
      "MESSAGE": [3, "ref_msg", [10, "你好"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "ref_msg": {
    "opcode": "argument_reporter_string_number",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VALUE": ["消息", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 调用自定义积木

```json
{
  "block": {
    "opcode": "procedures_call",
    "next": null,
    "parent": "prev",
    "inputs": {
      "param_steps": [1, [4, "20"]],
      "param_msg": [1, [10, "Hello!"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 布尔参数示例

```json
{
  "bool_shadow": {
    "opcode": "argument_reporter_boolean",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VALUE": ["是否可见", null]
    },
    "shadow": true,
    "topLevel": false
  }
}
```

## 注意事项

1. `procedures_prototype` 必须是 shadow 块
2. 参数通过 `argument_reporter_string_number` 或 `argument_reporter_boolean` 引用
3. 调用时使用 `[3, "ref_block", default_value]` 格式引用参数
4. 自定义积木的积木块 ID 需要全局唯一
