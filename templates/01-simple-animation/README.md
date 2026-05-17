# 简单动画模板

**难度**：入门
**涉及概念**：事件触发、无限循环、造型切换、碰到边缘反弹

## 描述

点击绿旗后，角色在舞台上持续移动，碰到边缘反弹，同时循环切换造型产生动画效果。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `control_forever` — 重复执行
- `motion_movesteps` — 移动 10 步
- `motion_ifonedgebounce` — 碰到边缘反弹
- `looks_nextcostume` — 下一个造型
- `control_wait` — 等待 0.2 秒

## 角色要求

- 角色 1：至少 2 个造型（用于动画切换）
- 背景 1：任意纯色背景
