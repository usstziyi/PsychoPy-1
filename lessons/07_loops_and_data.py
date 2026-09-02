"""
课程 07 · 试次循环与数据记录
==============================
核心概念：
  - data.importConditions : 从 CSV 导入条件
  - data.TrialHandler : 管理试次的顺序、重复与随机化
  - for trial in handler : 遍历每个试次
  - trial 是带 .get(key) 的字典；handler.addData 记录试次级数据
  - 保存数据：saveAsWideText / saveAsExcel
  - data.ExperimentHandler : 记录被试/会话级信息

运行：python lessons/07_loops_and_data.py
（会在当前目录生成 results.csv）
"""
import os
from psychopy import data, core, visual, event

win = visual.Window(size=(800, 600), color="black", units="height",
                    fullscr=False)

# ---------- 1. 定义条件（也可以 importConditions 从 CSV 读取）----------
conditions = [
    {"word": "RED",   "color": "green"},
    {"word": "GREEN", "color": "red"},
    {"word": "BLUE",  "color": "yellow"},
    {"word": "YELLOW","color": "blue"},
]

# ---------- 2. 创建 TrialHandler（随机、重复 2 次）----------
trials = data.TrialHandler(
    conditions,
    nReps=2,
    method="random",
    extraInfo={"participant": "demo", "session": 1},
)

# 一个被试信息处理器（用于统一命名/汇总）
exp = data.ExperimentHandler(
    extraInfo={"participant": "demo", "session": 1},
    savePsydat=True,   # 可选，保存 .psydat
)

# 文本刺激
msg = visual.TextStim(win, text="", pos=(0, 0), height=0.2)

# ---------- 3. 主试次循环 ----------
for trial in trials:
    # 每次从 trial 中读取该试次的 word 与 color
    word = trial["word"]
    color = trial["color"]

    # 显示一个词，颜色和语义可以一致（活动词Stroop）或不一致
    msg.text = word
    msg.color = color          # TextStim 的 color 用名字或 RGB/颜色名
    msg.draw()
    win.flip()

    # 等待按键（正确按键 f / 错误键 j）
    resp = event.waitKeys(keyList=["f", "j"], maxWait=2.0)

    # ---------- 4. 记录该试次反应数据 ----------
    if resp is None:
        trials.addData("resp", "NA")
        trials.addData("correct", "NA")
        trials.addData("rt", "NA")
    else:
        key = resp[0]
        # 简单规则：没有任何"对错"标准，这里演示把按键存下来即可
        trials.addData("resp", key)
        # 用 RT = waitKeys 可通过 after 参数拿更精确时间，这里不展开
        trials.addData("correct", "NA")
        trials.addData("rt", "NA")

    # 注意：用 `for trial in trials` 遍历时，循环对象会自动推进到下一试次，
    # 因此不要在循环体里再手动调用 trials.next()，否则会跳过/错位试次。

# ---------- 5. 保存 ----------
data_dir = os.path.dirname(os.path.abspath(__file__))
trials.saveAsWideText(os.path.join(data_dir, "results.csv"), delim=",")
print(f"数据已保存到: {os.path.join(data_dir, 'results.csv')}")

win.close()
core.quit()


"""
思考题
------
1. TrialHandler 的 method="random" 是全随机还是有放回的采样？
2. 若要记录反应时，waitKeys 怎么拿到更精确的 RT？
3. ExperimentHandler 和 TrialHandler 的数据在文件里怎么组织？
4. 运行两次，生成的 results.csv 每行试次顺序会一样吗？
"""