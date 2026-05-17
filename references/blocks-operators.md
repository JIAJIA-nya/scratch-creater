# 运算类积木块 (Operators)

> 参考文件：`references/blocks-operators.md` | 共 18 个积木块

运算类积木块提供数学运算、逻辑运算和字符串操作功能。所有运算积木块都是 reporter（返回值），需要嵌入到其他积木块的 inputs 中使用。

## 积木块列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `operator_add` | + | INPUTS: `NUM1`, `NUM2` |
| `operator_subtract` | - | INPUTS: `NUM1`, `NUM2` |
| `operator_multiply` | * | INPUTS: `NUM1`, `NUM2` |
| `operator_divide` | / | INPUTS: `NUM1`, `NUM2` |
| `operator_random` | 在 ... 到 ... 间随机选数 | INPUTS: `FROM`, `TO` |
| `operator_gt` | > | INPUTS: `OPERAND1`, `OPERAND2` |
| `operator_lt` | < | INPUTS: `OPERAND1`, `OPERAND2` |
| `operator_equals` | = | INPUTS: `OPERAND1`, `OPERAND2` |
| `operator_and` | 且 | INPUTS: `OPERAND1`, `OPERAND2` |
| `operator_or` | 或 | INPUTS: `OPERAND1`, `OPERAND2` |
| `operator_not` | 不成立 | INPUT: `OPERAND` |
| `operator_join` | 连接 ... ... | INPUTS: `STRING1`, `STRING2` |
| `operator_letter_of` | 第 ... 个字符 | INPUTS: `LETTER`, `STRING` |
| `operator_length` | 字符串长度 | INPUT: `STRING` |
| `operator_mod` | ... 除以 ... 的余数 | INPUTS: `NUM1`, `NUM2` |
| `operator_round` | 将 ... 四舍五入 | INPUT: `NUM` |
| `operator_mathop` | ... 运算 | FIELD: `OPERATOR`, INPUT: `NUM` |
| `operator_contains` | ... 包含 ... ? | INPUTS: `STRING1`, `STRING2` |

## 字段值

### operator_mathop 的 OPERATOR
- `["abs", null]` — 绝对值
- `["floor", null]` — 向下取整
- `["ceiling", null]` — 向上取整
- `["sqrt", null]` — 平方根
- `["sin", null]` — sin
- `["cos", null]` — cos
- `["tan", null]` — tan
- `["asin", null]` — asin
- `["acos", null]` — acos
- `["atan", null]` — atan
- `["ln", null]` — ln
- `["log", null]` — log
- `["e ^", null]` — e 的乘方
- `["10 ^", null]` — 10 的乘方

## JSON 示例

### 加法（3 + 5）
```json
{
  "block": {
    "opcode": "operator_add",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "3"]],
      "NUM2": [1, [4, "5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 减法
```json
{
  "block": {
    "opcode": "operator_subtract",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "10"]],
      "NUM2": [1, [4, "3"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 乘法
```json
{
  "block": {
    "opcode": "operator_multiply",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "6"]],
      "NUM2": [1, [4, "7"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 除法
```json
{
  "block": {
    "opcode": "operator_divide",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "100"]],
      "NUM2": [1, [4, "4"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 随机数（1 到 10）
```json
{
  "block": {
    "opcode": "operator_random",
    "next": null,
    "parent": null,
    "inputs": {
      "FROM": [1, [4, "1"]],
      "TO": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 大于
```json
{
  "block": {
    "opcode": "operator_gt",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND1": [1, [4, "10"]],
      "OPERAND2": [1, [4, "5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 小于
```json
{
  "block": {
    "opcode": "operator_lt",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND1": [1, [4, "3"]],
      "OPERAND2": [1, [4, "5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 等于
```json
{
  "block": {
    "opcode": "operator_equals",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND1": [1, [10, "hello"]],
      "OPERAND2": [1, [10, "hello"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 逻辑与
```json
{
  "block": {
    "opcode": "operator_and",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND1": [2, "condition1"],
      "OPERAND2": [2, "condition2"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 逻辑或
```json
{
  "block": {
    "opcode": "operator_or",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND1": [2, "condition1"],
      "OPERAND2": [2, "condition2"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 逻辑非
```json
{
  "block": {
    "opcode": "operator_not",
    "next": null,
    "parent": null,
    "inputs": {
      "OPERAND": [2, "condition"]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 连接字符串
```json
{
  "block": {
    "opcode": "operator_join",
    "next": null,
    "parent": null,
    "inputs": {
      "STRING1": [1, [10, "hello"]],
      "STRING2": [1, [10, "world"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 第 N 个字符
```json
{
  "block": {
    "opcode": "operator_letter_of",
    "next": null,
    "parent": null,
    "inputs": {
      "LETTER": [1, [4, "1"]],
      "STRING": [1, [10, "hello"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 字符串长度
```json
{
  "block": {
    "opcode": "operator_length",
    "next": null,
    "parent": null,
    "inputs": {
      "STRING": [1, [10, "hello"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 取余
```json
{
  "block": {
    "opcode": "operator_mod",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "10"]],
      "NUM2": [1, [4, "3"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 四舍五入
```json
{
  "block": {
    "opcode": "operator_round",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM": [1, [4, "3.7"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 字符串包含
```json
{
  "block": {
    "opcode": "operator_contains",
    "next": null,
    "parent": null,
    "inputs": {
      "STRING1": [1, [10, "hello world"]],
      "STRING2": [1, [10, "world"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```

### 数学函数（绝对值）
```json
{
  "block": {
    "opcode": "operator_mathop",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM": [1, [4, "-5"]]
    },
    "fields": {
      "OPERATOR": ["abs", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 数学函数（sin）
```json
{
  "block": {
    "opcode": "operator_mathop",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM": [1, [4, "30"]]
    },
    "fields": {
      "OPERATOR": ["sin", null]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

## 嵌套示例

运算积木块可以嵌套使用，例如 `(3 + 5) * 2`：

```json
{
  "add_block": {
    "opcode": "operator_add",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [1, [4, "3"]],
      "NUM2": [1, [4, "5"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  },
  "mul_block": {
    "opcode": "operator_multiply",
    "next": null,
    "parent": null,
    "inputs": {
      "NUM1": [2, "add_block"],
      "NUM2": [1, [4, "2"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": false
  }
}
```