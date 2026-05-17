# 乒乓球游戏模板

**难度**：进阶
**涉及概念**：克隆、碰撞检测、变量、运动、反弹

## 描述

经典乒乓球游戏：两个玩家分别控制左右挡板，球在中间弹来弹去，没接到球失分。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `motion_movesteps` — 球的移动
- `motion_ifonedgebounce` — 碰到边缘反弹
- `control_if` — 条件判断
- `sensing_touchingobject` — 碰到挡板
- `motion_turnright` / `motion_turnleft` — 反弹角度
- `control_create_clone_of` — 克隆球
- `control_start_as_clone` — 克隆体脚本
- `data_variable` — 变量（分数）
- `data_changevariableby` — 分数增加
- `sensing_keypressed` — 键盘控制挡板

## 角色要求

- 球：1 个小圆形造型
- 左挡板：1 个长方形造型
- 右挡板：1 个长方形造型
