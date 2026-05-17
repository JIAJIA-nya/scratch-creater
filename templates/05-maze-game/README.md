# 迷宫游戏模板

**难度**：进阶
**涉及概念**：键盘输入、碰撞检测（颜色）、变量、条件判断

## 描述

玩家用方向键控制角色在迷宫中移动，不能穿过墙壁，到达终点获胜。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `sensing_keypressed` — 按下某键
- `control_if` — 条件判断
- `sensing_touchingcolor` — 碰到颜色（墙壁检测）
- `motion_gotoxy` — 移动（或撤销移动）
- `looks_say` — 显示消息（到达终点）
- `control_stop` — 停止游戏
- `data_variable` — 变量（计分/计时）

## 角色要求

- 玩家角色：1 个小圆形造型
- 迷宫背景：墙壁和通道用不同颜色区分
- 终点区域：特定颜色标记
