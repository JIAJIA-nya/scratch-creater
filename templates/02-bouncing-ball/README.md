# 弹跳球模板

**难度**：入门
**涉及概念**：事件触发、无限循环、运动、反弹、重力模拟

## 描述

模拟一个弹跳的球：球从高处落下，碰到地面反弹，每次反弹高度逐渐降低，最终停止。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `motion_changeyby` — y 坐标变化（重力）
- `motion_movesteps` — 水平移动
- `control_if` — 条件判断（是否碰到地面）
- `motion_ifonedgebounce` — 碰到边缘反弹
- `operator_multiply` — 乘法（反弹系数）
- `data_variable` — 变量（速度）

## 角色要求

- 球角色：1 个圆形造型
- 地面角色：1 个长方形造型
