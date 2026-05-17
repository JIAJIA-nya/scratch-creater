# 多人聊天模拟模板

**难度**：进阶
**涉及概念**：列表、变量、用户输入、字符串操作、循环、条件判断

## 描述

模拟一个多人聊天室：不同角色轮流发言，用户也可以输入消息加入对话，消息显示在聊天记录列表中。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `data_variable` — 变量（发言者、消息计数）
- `data_listcontents` — 列表（聊天记录）
- `data_addtolist` — 加入聊天记录
- `data_deleteoflist` — 删除旧记录（保持列表不超长）
- `data_lengthoflist` — 列表长度
- `control_repeat` — 重复执行
- `control_wait` — 等待
- `looks_say` — 显示消息
- `sensing_askandwait` — 用户输入
- `sensing_answer` — 读取回答
- `operator_join` — 连接字符串（发言者 + 消息）
- `operator_random` — 随机选择发言者
- `control_forever` — 持续运行
- `control_if` — 判断用户输入

## 角色要求

- 角色 A：1 个造型
- 角色 B：1 个造型
- 角色 C：1 个造型
- 背景：聊天室风格
