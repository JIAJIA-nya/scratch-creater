# 变量和列表积木块 (Variables)

> 参考文件：`references/blocks-variables.md` | 共 12 个积木块

变量和列表积木块用于存储和操作数据。变量存储单个值，列表存储多个值。

## 积木块列表

### 变量

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `data_variable` | （变量） | reporter，读取变量值 |
| `data_setvariableto` | 将 ... 设为 N | FIELD: `VARIABLE`, INPUT: `VALUE` |
| `data_changevariableby` | 将 ... 增加 N | FIELD: `VARIABLE`, INPUT: `VALUE` |
| `data_showvariable` | 显示变量 | FIELD: `VARIABLE` |
| `data_hidevariable` | 隐藏变量 | FIELD: `VARIABLE` |

### 列表

| opcode | 中文名 | 说明 |
|--------|--------|------|
| `data_listcontents` | （列表） | reporter，读取列表内容 |
| `data_addtolist` | 将 ... 加入 ... | FIELD: `LIST`, INPUT: `ITEM` |
| `data_deleteoflist` | 删除 ... 的第 N 项 | FIELD: `LIST`, INPUT: `INDEX` |
| `data_deletealloflist` | 删除 ... 的全部项目 | FIELD: `LIST` |
| `data_insertatlist` | 在 ... 的第 N 项插入 ... | FIELD: `LIST`, INPUTS: `INDEX`, `ITEM` |
| `data_replaceitemoflist` | 将 ... 的第 N 项替换为 ... | FIELD: `LIST`, INPUTS: `INDEX`, `ITEM` |
| `data_itemoflist` | ... 的第 N 项 | FIELD: `LIST`, INPUT: `INDEX` |
| `data_itemnumoflist` | ... 中第一个 ... 的编号 | FIELD: `LIST`, INPUT: `ITEM` |
| `data_lengthoflist` | ... 的项目数 | FIELD: `LIST` |
| `data_listcontainsitem` | ... 包含 ... ? | FIELD: `LIST`, INPUT: `ITEM` |
| `data_showlist` | 显示列表 | FIELD: `LIST` |
| `data_hidelist` | 隐藏列表 | FIELD: `LIST` |

## 字段格式

变量/列表字段值格式：`["变量名", "变量ID"]`

变量 ID 是 project.json 中 variables/lists 对象的 key。

## JSON 示例

### 读取变量（reporter）
```json
{
  "block": {
    "opcode": "data_variable",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "VARIABLE": ["得分", "score_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 设置变量
```json
{
  "block": {
    "opcode": "data_setvariableto",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [10, "0"]]
    },
    "fields": {
      "VARIABLE": ["得分", "score_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 变量增加
```json
{
  "block": {
    "opcode": "data_changevariableby",
    "next": null,
    "parent": "prev",
    "inputs": {
      "VALUE": [1, [4, "10"]]
    },
    "fields": {
      "VARIABLE": ["得分", "score_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 显示变量
```json
{
  "block": {
    "opcode": "data_showvariable",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "VARIABLE": ["得分", "score_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 隐藏变量
```json
{
  "block": {
    "opcode": "data_hidevariable",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "VARIABLE": ["得分", "score_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 读取列表（reporter）
```json
{
  "block": {
    "opcode": "data_listcontents",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 加入列表
```json
{
  "block": {
    "opcode": "data_addtolist",
    "next": null,
    "parent": "prev",
    "inputs": {
      "ITEM": [1, [10, "新项目"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 删除第 N 项
```json
{
  "block": {
    "opcode": "data_deleteoflist",
    "next": null,
    "parent": "prev",
    "inputs": {
      "INDEX": [1, [7, "1"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 删除全部
```json
{
  "block": {
    "opcode": "data_deletealloflist",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 插入项目
```json
{
  "block": {
    "opcode": "data_insertatlist",
    "next": null,
    "parent": "prev",
    "inputs": {
      "INDEX": [1, [7, "1"]],
      "ITEM": [1, [10, "新项目"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 替换项目
```json
{
  "block": {
    "opcode": "data_replaceitemoflist",
    "next": null,
    "parent": "prev",
    "inputs": {
      "INDEX": [1, [7, "1"]],
      "ITEM": [1, [10, "替换内容"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 获取第 N 项
```json
{
  "block": {
    "opcode": "data_itemoflist",
    "next": null,
    "parent": null,
    "inputs": {
      "INDEX": [1, [7, "1"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 获取项目编号
```json
{
  "block": {
    "opcode": "data_itemnumoflist",
    "next": null,
    "parent": null,
    "inputs": {
      "ITEM": [1, [10, "搜索内容"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 列表长度
```json
{
  "block": {
    "opcode": "data_lengthoflist",
    "next": null,
    "parent": null,
    "inputs": {},
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 列表是否包含
```json
{
  "block": {
    "opcode": "data_listcontainsitem",
    "next": null,
    "parent": null,
    "inputs": {
      "ITEM": [1, [10, "搜索内容"]]
    },
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

### 显示/隐藏列表
```json
{
  "block": {
    "opcode": "data_showlist",
    "next": null,
    "parent": "prev",
    "inputs": {},
    "fields": {
      "LIST": ["高分榜", "highscores_id_xxx"]
    },
    "shadow": false,
    "topLevel": false
  }
}
```

## 在 Target 中定义变量和列表

变量和列表需要在 target 的 `variables` 和 `lists` 字段中声明：

```json
{
  "isStage": true,
  "name": "Stage",
  "variables": {
    "score_id_xxx": ["得分", 0],
    "lives_id_xxx": ["生命", 3]
  },
  "lists": {
    "highscores_id_xxx": ["高分榜", [100, 80, 60]]
  }
}
```

变量格式：`["变量名", 初始值]`
列表格式：`["列表名", [项目1, 项目2, ...]]`
