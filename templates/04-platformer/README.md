# 平台跳跃游戏模板

**难度**：进阶
**涉及概念**：重力模拟、键盘输入、碰撞检测、变量、布尔运算

## 描述

玩家用方向键控制角色移动和跳跃，角色受重力影响下落，站在平台上不掉落。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `data_variable` — 变量（速度、是否在地面）
- `data_changevariableby` — 速度变化（重力）
- `motion_changeyby` — y 坐标变化
- `sensing_keypressed` — 按下某键
- `motion_changexby` — x 坐标变化
- `control_if` — 条件判断
- `operator_and` — 逻辑与
- `sensing_touchingcolor` — 碰到颜色（平台检测）
- `motion_gotoxy` — 初始位置

## 角色要求

- 玩家角色：1 个造型
- 平台角色：1 个长方形造型（带颜色）
