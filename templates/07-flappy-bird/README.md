# 飞翔的小鸟模板

**难度**：进阶
**涉及概念**：克隆、重力模拟、碰撞检测、变量、广播消息

## 描述

类似 Flappy Bird 游戏：点击屏幕让小鸟向上飞，不点击时小鸟下落，穿过管道得分，碰到管道或地面游戏结束。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `control_if` — 条件判断
- `sensing_mousedown` / `sensing_keypressed` — 点击/按键检测
- `motion_changeyby` — 重力下落 / 向上飞
- `control_create_clone_of` — 克隆管道
- `control_start_as_clone` — 管道克隆体移动
- `control_delete_this_clone` — 删除超出屏幕的管道
- `sensing_touchingobject` — 碰到管道
- `data_variable` — 分数
- `data_changevariableby` — 增加分数
- `event_broadcast` — 广播游戏结束消息
- `control_stop` — 停止

## 角色要求

- 小鸟角色：1 个造型（最好有 2-3 个动画造型）
- 上管道：1 个长方形造型
- 下管道：1 个长方形造型
