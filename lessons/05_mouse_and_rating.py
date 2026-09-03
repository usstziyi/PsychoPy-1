"""
课程 05 · 鼠标与评定量表
=========================
核心概念：
  - Mouse（psychopy.hardware.mouse，新版已不在 visual 里）: 状态（位置、按钮、可见性）
  - 点击检测：mouse.buttons（[left, mid, right] 的布尔）
  - win.mouseVisible : 控制光标显隐
  - visual.Slider : 滑块式评定量表（RatingScale 的新版替代，无需 legacy 插件）

运行：python lessons/05_mouse_and_rating.py
"""
import numpy as np
from psychopy import visual, core, event
from psychopy.hardware.mouse import Mouse

# win = visual.Window(size=(900, 600), color="grey", units="height", fullscr=False, monitor="testMonitor")

# # ---------- 第一部分：鼠标点击画点 ----------
# inst = visual.TextStim(win, text="在画面任意位置点鼠标左键，点右键或按 ESC 结束",
#                        pos=(0.0, 0.35), color="white", height=0.04)

# mouse = Mouse(win=win)      # 绑定到窗口（新版 Mouse 位于 psychopy.hardware.mouse）
# data_hint = visual.TextStim(win, text="", pos=(0.0, -0.35),
#                             color="white", height=0.03)

# inst.draw()
# win.flip()

# # ---- 圆点改用 ElementArrayStim 批量绘制 ----
# # 预申请一批圆点，点击时只改对应坐标/透明度；每帧 draw 一次即画完全部，
# # 不再像"每帧新建 Circle 对象"那样产生大量临时对象
# MAX_DOTS = 1000
# dot_pos = np.zeros((MAX_DOTS, 2))   # 每个点的坐标（height 单位）
# dot_opc = np.zeros(MAX_DOTS)        # 每个点透明度：0=看不见（未使用）
# dots = visual.ElementArrayStim(
#     win, units="height",
#     nElements=MAX_DOTS,
#     elementTex=None,          # 纯色填充
#     elementMask="circle",     # 圆形遮罩 → 视觉上就是实心圆
#     sizes=0.04,               # 直径 0.04，等同原 radius=0.02 的 Circle
#     colors="gold",
#     autoLog=False,
# )
# dots.xys = dot_pos
# dots.opacities = dot_opc

# clicks = []                    # 记录点击坐标（用于最后打印/保存）
# # 记录左键"按下"边沿：上一次左键是否处于按下状态
# prev_left = False
# while True:
#     # 状态：位置 + 按钮
#     x, y = mouse.getPos()
#     left, mid, right = mouse.buttons   # 新 API：buttons 是 [left, mid, right] 的布尔数组

#     # 检测左键"刚按下"（从 False -> True 的上升沿），避免一帧内重复记录
#     if left and not prev_left:
#         if len(clicks) < MAX_DOTS:
#             dot_pos[len(clicks)] = (x, y)   # 新点写入预留槽位
#             dot_opc[len(clicks)] = 1.0
#             clicks.append((x, y))
#             dots.xys = dot_pos              # 让 ElementArrayStim 拾取新坐标
#             dots.opacities = dot_opc
#             data_hint.text = f"已记录 {len(clicks)} 个点，最近在 ({x:.2f}, {y:.2f})"
#     prev_left = left

#     # 右键结束
#     if right:
#         break

#     # ESC 也是结束方式
#     if event.getKeys(keyList=["escape"]):
#         break

#     inst.draw()
#     data_hint.draw()
#     dots.draw()               # 一次调用批量画完所有圆点
#     win.flip()

# print("记录的点击:", clicks)
# win.close()

# core.quit()
# exit()

# ---------- 第二部分：Slider 量表（单独一个窗口）----------
win2 = visual.Window(size=(900, 500), color="white", units="height",
                     fullscr=False)
question = visual.TextStim(win2, text="请评价你的幸福感", pos=(0, 0.25),
                           color="black", height=0.06)

scale = visual.Slider(
    win2,
    ticks=[1, 100],                   # 两端点即取值范围 1~100
    labels=["完全不幸福", "非常幸福"],  # 两个刻度各一个标签
    granularity=1,                    # 最小步长 1（整数评分；0=连续 VAS）
    style="slider",                   # 滑块样式；可试 "rating"/"radio"
    size=(1.5, 0.1),                  # (宽, 高)，单位随 units
    pos=(0, -0.05),
    units="height",
    labelColor="black",               # 白底窗口需用深色才看得见
    lineColor="black",
    markerColor="red",
    font="Microsoft YaHei",  # 中文需用含中文字形的字体（Arial 会乱码）
)

while scale.getRating() is None:      # Slider 没有 noResponse，用 rating 判断
    question.draw()
    scale.draw()                      # draw() 内部自动处理鼠标点击/拖拽
    if event.getKeys(keyList=["escape"]):
        break
    win2.flip()

if scale.getRating() is None:
    print("被试按 ESC 跳过了评分")
else:
    rating = scale.getRating()
    rt = scale.getRT()
    print(f"评分: {rating}    反应时: {rt:.3f}s")

win2.close()
core.quit()


"""
思考题
------
1. mouse.buttons 返回的是三维数组，代表哪三个键？
2. 为什么在帧循环里调用 getKeys 检查 ESC，而不是 event.waitKeys？
3. Slider 的 getRating、getRT 分别表示什么？怎么判断被试还没作答？
4. 把 style 换成 'rating' 或 'radio'，观察外观差异。
"""