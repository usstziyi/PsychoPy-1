"""
课程 02 · 基础形状刺激
=========================
核心概念：
  - 多种基础刺激类：Rect / Circle / Line / Polygon / Dot
  - 坐标单位 units（norm / height / deg / pix）
  - 位置 pos、尺寸 size、颜色 fillColor / lineColor
  - borderWidth 描边宽度；多个形状叠加成一幅画面

运行：python lessons/02_stimuli_shapes.py
"""
from psychopy import visual, core

win = visual.Window(
    size=(900, 600),
    color="white",
    units="height",
    fullscr=False,
)

# --- 画一个方形（以黄/黑填充）---
rect = visual.Rect(
    win,
    width=0.4,
    height=0.4,
    pos=(-0.4, 0.2),
    fillColor="coral",
    lineColor="black",
    lineWidth=3,
)

# --- 画一个圆形 ---
circle = visual.Circle(
    win,
    radius=0.2,
    pos=(0.4, 0.2),
    fillColor="skyblue",
    lineColor="navy",
    lineWidth=2,
)

# --- 画一条线段 ---
line = visual.Line(
    win,
    start=(-0.35, -0.35),
    end=(0.35, -0.35),        # 一条水平线
    lineColor="seagreen",
    lineWidth=4,
)

# --- 画一个正三角形（任意顶点用 ShapeStim；Polygon 只能画正多边形）---
tri = visual.ShapeStim(
    win,
    vertices=[(-0.1, -0.2), (0.1, -0.2), (0.0, -0.2 + 0.28)],  # 底边+顶点
    closeShape=True,          # 首尾相连成封闭图形
    lineColor="black",
    fillColor="gold",
    lineWidth=2,
)

# --- 画一个小圆点（表示一个点）---
dot = visual.Circle(
    win,
    radius=0.025,
    pos=(0.0, 0.25),
    fillColor="purple",
    lineColor=None,       # 描边设为透明，就是纯填充的点（新版不能 lineWidth=0）
)

# 把上面所有刺激画到后台缓冲
rect.draw()
circle.draw()
line.draw()
tri.draw()
dot.draw()

# 显示（flip 一帧）
win.flip()
core.wait(3.0)


# --- 进阶：观察坐标网格（可选：第二段演示）---
grid_win = visual.Window(
    size=(400, 400), 
    color="white", 
    units="norm",
    fullscr=False
)

cross = visual.TextStim(
    grid_win, 
    text="+", 
    color="black", 
    height=0.2, # 文字高度
    pos=(0, 0)
)

cross.draw()
grid_win.flip()
core.wait(2.0)
grid_win.close()

# --- 收尾 ---
win.close()
core.quit()


"""
思考题
------
1. units="norm" 时，右上角坐标是多少？units="height" 时分辨率变化会怎样？
2. 怎么让两个形状重叠？重叠时 z 顺序怎么控制？
3. 把 tri 的顶点坐标改一下，画一个倒三角形。
"""