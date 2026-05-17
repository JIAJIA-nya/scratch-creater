# 画板应用模板

**难度**：进阶
**涉及概念**：画笔扩展、鼠标输入、克隆、变量、颜色控制

## 描述

一个简单的画板应用：用户按住鼠标拖动来绘图，可以切换颜色和画笔大小，支持清空画布。

## 积木块

- `event_whenflagclicked` — 当绿旗被点击
- `pen_clear` — 清空画布
- `control_forever` — 重复执行
- `sensing_mousedown` — 按下鼠标？
- `pen_penDown` — 落笔
- `pen_penUp` — 抬笔
- `motion_goto` — 移动到鼠标位置
- `pen_setPenColorToColor` — 设置画笔颜色
- `pen_setPenSizeTo` — 设置画笔大小
- `sensing_mousex` / `sensing_mousey` — 鼠标坐标
- `control_if` — 判断是否按下鼠标
- `data_variable` — 变量（颜色索引、画笔大小）
- `event_whenkeypressed` — 键盘切换颜色
- `pen_changePenColorParamBy` — 改变颜色
- `pen_changePenSizeBy` — 改变大小

## 角色要求

- 画笔角色：1 个小圆形造型（作为画笔尖）
- 颜色选择器角色：多个不同颜色的小方块
- 背景：白色
