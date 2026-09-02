"""
课程 01 · 打开一个窗口（Hello World）
=====================================
核心概念：
  - visual.Window : 创建实验窗口
  - visual.TextStim: 文本刺激文本
  - stim.draw()   : 把刺激"画"到后台缓冲（不显示）
  - win.flip()    : 把后台缓冲一次性显示到屏幕（垂直同步）
  - core.wait()   : 让程序等待若干秒（显示期间占用）
  - core.quit()   : 干净地退出（关闭窗口、释放资源）

提示：直接运行  python lessons/01_hello_window.py
"""
from psychopy import visual, core

# 1. 创建窗口：尺寸 800x600，标题，非全屏，灰底
win = visual.Window(
    size=(800, 600),
    color="grey",
    units="height",          # 用"高度"作为坐标单位，方便缩放
    fullscr=False,
    monitor="testMonitor",   # 若没有配置显示器可用默认
)

# 2. 创建一个文本刺激对象
hello = visual.TextStim(
    win,
    text="Hello, PsychoPy!",
    pos=(0.0, 0.1),          # 画面中央略上方
    color="black",
    height=0.1,
)

# 3. 再来一个副标题
subtitle = visual.TextStim(
    win,
    text="按下任意键退出",
    pos=(0.0, -0.1),
    color="darkslategrey",
    height=0.05,
)

# 4. 画两个刺激，然后 flip 显示
hello.draw()
subtitle.draw()
win.flip()

# 5. 显示 2 秒
core.wait(20.0)

# 7. 收尾：关窗 + 退出
win.close()
core.quit()


"""
思考题
------
1. 如果把 win.flip() 去掉，屏幕上会出现文字吗？为什么？
2. units="height" 下 height=0.1 表示文字高度约为屏幕高度的 10%。
   试试改成 units="pix"，`height=60`，看看效果。
3. 把 `core.wait(2.0)` 的时长改小/改大，观察窗口持续时间的差异。
"""