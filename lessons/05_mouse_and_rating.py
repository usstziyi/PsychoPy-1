"""
课程 05 · 鼠标与评定量表
=========================
核心概念：
  - visual.Mouse : 状态（位置、按钮、可见性）
  - 点击检测：getPressed（返回 [left, mid, right] 的布尔）
  - win.mouseVisible : 控制光标显隐
  - visual.RatingScale : 李克特/滑块式评定量表，常用于问卷调查

运行：python lessons/05_mouse_and_rating.py
"""
from psychopy import visual, core, event

win = visual.Window(size=(900, 600), color="grey", units="height",
                    fullscr=False)

# ---------- 第一部分：鼠标点击画点 ----------
inst = visual.TextStim(win, text="在画面任意位置点鼠标左键，点右键或按 ESC 结束",
                       pos=(0.0, 0.35), color="white", height=0.04)

mouse = visual.Mouse(win=win)      # 绑定到窗口
data_hint = visual.TextStim(win, text="", pos=(0.0, -0.35),
                            color="white", height=0.03)

inst.draw()
win.flip()

clicks = []
# 记录左键"按下"边沿：上一次左键是否处于按下状态
prev_left = False
while True:
    # 状态：位置 + 按钮
    x, y = mouse.getPos()
    left, mid, right = mouse.getPressed()

    # 检测左键"刚按下"（从 False -> True 的上升沿），避免一帧内重复记录
    if left and not prev_left:
        clicks.append((x, y))
        data_hint.text = f"已记录 {len(clicks)} 个点，最近在 ({x:.2f}, {y:.2f})"
    prev_left = left

    # 右键结束
    if right:
        break

    # ESC 也是结束方式
    if event.getKeys(keyList=["escape"]):
        break

    inst.draw()
    data_hint.draw()
    # 把记录的点画成小圆
    for cx, cy in clicks:
        visual.Circle(win, radius=0.02, pos=(cx, cy), fillColor="gold",
                      lineWidth=0).draw()
    win.flip()

print("记录的点击:", clicks)
win.close()

# ---------- 第二部分：RatingScale（单独一个窗口）----------
win2 = visual.Window(size=(900, 500), color="white", units="height",
                     fullscr=False)
question = visual.TextStim(win2, text="请评价你的幸福感", pos=(0, 0.25),
                           color="black", height=0.06)

scale = visual.RatingScale(
    win2,
    low=1, high=100,
    labels=["完全不幸福", "非常幸福"],
    marker="slider",          # 拖动滑块
    size=1.6,
    pos=(0, -0.05),
)

while scale.noResponse:       # 内部会自动更新，等待被试确认
    question.draw()
    scale.draw()
    if event.getKeys(keyList=["escape"]):
        break
    win2.flip()

if scale.noResponse:
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
1. getPressed() 返回的是三维数组，代表哪三个键？
2. 为什么在帧循环里调用 getKeys 检查 ESC，而不是 event.waitKeys？
3. RatingScale 的 noResponse、getRating、getRT 分别表示什么？
4. 把 marker 换成 'triangle' 或 'circle'，观察外观差异。
"""