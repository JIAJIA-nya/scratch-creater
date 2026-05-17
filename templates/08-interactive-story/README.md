# 互动故事模板

**难度**：入门
**涉及概念**：背景切换、对话、广播消息、条件判断、用户选择

## 描述

一个互动故事：背景切换展示不同场景，角色之间有对话，用户通过按键选择故事分支。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `looks_switchbackdropto` — 切换背景
- `looks_sayforseconds` — 说 ... N 秒
- `control_wait` — 等待
- `sensing_askandwait` — 询问用户选择
- `sensing_answer` — 读取回答
- `operator_equals` — 判断选择
- `control_if_else` — 分支
- `event_broadcast` — 广播切换场景
- `event_whenbroadcastreceived` — 接收场景切换
- `looks_show` / `looks_hide` — 显示/隐藏角色

## 角色要求

- 主角角色：1+ 个造型
- 配角角色：1+ 个造型
- 背景：3+ 个（不同场景）
