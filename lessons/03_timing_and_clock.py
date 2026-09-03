"""
课程 03 · 计时与时钟
======================
核心概念：
  - 显示器刷新率（常见 60Hz → 每帧约 16.7ms）
  - win.flip() 采用垂直同步，返回值为帧时间戳
  - core.Clock 可测量一段程序/一帧持续多久
  - 用帧数控制刺激时长（帧同步计时），而不要依赖 CPU sleep

运行：python lessons/03_timing_and_clock.py
"""
from psychopy import visual, core

win = visual.Window(
    size=(800, 600),
    color="black",
    units="height",
    fullscr=False,
    monitor="MiMonitor",
)

# 用一个色块刺激
square = visual.Rect(
    win,
    width=0.5,
    height=0.5,
    fillColor="cyan",
)

# 文字提示当前刷新周期
info = visual.TextStim(
    win,
    text="",
    pos=(0.0, 0.35),
    color="white",
    height=0.04,
)

# 打印显示器帧周期的估算值（显示器未配置时可能为 None）
frame_period = win.monitorFramePeriod
if frame_period:
    print(f"估算的帧周期: {frame_period*1000:.2f} ms  ->  刷新率约 "
          f"{1.0/frame_period:.1f} Hz")
else:
    print("未配置显示器参数，帧周期未知（仅作学习演示，不影响运行）")
    frame_period = None

# 用内置计时器
clock = core.Clock()

n_frames = 90   # 想显示 90 帧

# 帧循环：绘制 + flip + 更新文字
for f in range(n_frames):
    # 让方块每 15 帧翻转一次颜色，肉眼可感知闪烁节奏
    if (f // 15) % 2 == 0:
        square.fillColor = "cyan"
    else:
        square.fillColor = "magenta"

    square.draw()
    info.text = f"帧序号: {f:03d}"
    info.draw()

    frame_ts = win.flip()       # 关键：flip 返回本帧显示时间戳（秒）

# 测量这一段消耗的真实时间
elapsed = clock.getTime()       # 从 clock.reset()（创建时即为0）到现在的秒数

print(f"完成 {n_frames} 帧，实际耗时 {elapsed:.3f} s")
print(f"实测帧率: {n_frames / elapsed:.1f} Hz")

win.close()
core.quit()


"""
思考题
------
1. 为什么用"帧数 x 帧周期"来定时，比 core.wait(秒) 更精确？
2. 如果想显示正好 1 秒，在 60Hz 显示器上应该用多少帧？在 144Hz 呢？
3. frame_ts 有什么用？可以拿它来对齐音频/EEG 打标。
"""