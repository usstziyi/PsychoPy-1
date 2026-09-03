"""
课程 09 · 综合实战：Stroop 反应时实验
======================================
整合前八课：
  - visual 窗口 / 文本刺激、计时 flip、键盘采样、条件循环、
    数据记录与导出、退出处理

范式：屏幕中央显示一个颜色词，被试按键判断“字体颜色”与“词义”是否一致。
  - 一致词（word==color）→ 按 F
  - 不一致词（word!=color）→ 按 J
记录：反应按键、正确与否、反应时(RT)。
结果输出到 results_stroop.csv

运行：python lessons/09_full_experiment.py
"""
import os
import random
from psychopy import core, visual, event, data

# ================= 0. 设置 =================
SUBJECT = "demo"
SESSION = 1
n_reps = 2

# 颜色词与其印刷颜色（中文/英文可并存，这里用中文颜色词）
STIMULI = [
    {"word": "红", "color": "red"},
    {"word": "蓝", "color": "blue"},
    {"word": "绿", "color": "green"},
]

# ================= 1. 窗口 =================
win = visual.Window(size=(800, 600), color="black", units="height",
                    fullscr=False, monitor="testMonitor")

# ================= 2. 刺激 =================
fix = visual.TextStim(win, text="+", pos=(0, 0), color="grey", height=0.05)
word_stim = visual.TextStim(win, text="", pos=(0, 0), color="white",
                            height=0.25)

# ================= 3. 条件：生成全部一致性组合并随机 =================
all_conditions = []
for item in STIMULI:
    for target in STIMULI:
        congruent = (target["color"] == item["color"])   # 词义==颜色
        all_conditions.append({
            "word": item["word"],
            "print_color": target["color"],   # 字体颜色打印值
            "congruent": congruent,
        })
random.shuffle(all_conditions)   # 打乱顺序（重跑时顺序不同）

# ================= 4. TrialHandler =================
trials = data.TrialHandler(all_conditions, nReps=n_reps, method="random",
                           extraInfo={"subject": SUBJECT, "session": SESSION})

# ================= 5. 呈现固定 + 指导语 =================
instr = visual.TextStim(
    win,
    text=("判断词义是否等于字体颜色\n一致按 F，不一致按 J\n\n按 空格 开始"),
    pos=(0, 0), color="white", height=0.05,
)
instr.draw()
win.flip()
start_key = event.waitKeys(keyList=["space", "escape"])
# waitKeys 会"消费"按键，因此要用它的返回值判断，而不是再查 getKeys
if "escape" in (start_key or []):
    win.close()
    core.quit()

# ================= 6. 试次主循环 =================
clock = core.Clock()
for trial in trials:
    # 6.1 固定十字（400ms）
    fix.draw()
    flip_ts = win.flip()
    core.wait(0.4)

    # 6.2 显示刺激，记录起始时间
    word_stim.text = trial["word"]
    word_stim.color = trial["print_color"]
    word_stim.draw()
    start_ts = win.flip()          # flip 返回该帧显示的精确时间
    clock.reset()                  # 重置计时器 → 测量 RT

    # 6.3 采样按键直到正确/超时（最多 5s）
    resp = None
    rt = None
    while clock.getTime() < 5:
        # 每帧都要重新绘制刺激，否则下次 flip 画面会变空白
        word_stim.draw()
        keys = event.getKeys(keyList=["f", "j", "escape"])
        if keys:
            if "escape" in keys:
                win.close()
                core.quit()
            resp = keys[0]
            rt = clock.getTime()
            break
        # flip 一帧，让刺激持续可见
        win.flip()

    # 6.4 判断正确性
    if resp is not None:
        # 正确 = 一致→F，不一致→J
        correct = ((resp == "f") == trial["congruent"])
    else:
        correct = None

    # 6.5 记录数据
    trials.addData("resp", resp)
    trials.addData("correct", correct)
    trials.addData("rt", rt)
    # word / print_color / congruent 已在条件列表中，会自动导出，
    # 不要再用 addData 重复记录（重名列会让 pandas 导出报错）

# ================= 7. 结束与保存 =================
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "results_stroop.csv")
trials.saveAsWideText(out_path, delim=",")
print("数据已保存到:", out_path)

fin = visual.TextStim(win, text="实验结束，谢谢！", color="white", height=0.1)
fin.draw()
win.flip()
core.wait(1.0)

win.close()
core.quit()


"""
思考题
------
1. 6.3 中为什么要持续 win.flip()？不 flip 会怎样？
2. start_ts 与 clock.reset() 都在 flip 后，RT 的“零时刻”到底指哪一帧？
3. correct 判定用了 `(resp=='f') == congruent`，试推一下四种情况是否都正确。
4. 如何把 RT 换成更精确的帧时间戳对齐（用 flip 返回值相减）？
"""