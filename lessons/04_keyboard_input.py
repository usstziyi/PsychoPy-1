"""
课程 04 · 键盘输入
====================
核心概念：
  - event.waitKeys : 阻塞等待按键（适合单个刺激等待反应）
  - event.getKeys  : 非阻塞读取已按下的键（适合连续帧循环）
  - keyList  : 只接受指定按键
  - maxWait  : 最长等待时间
  - 退出键处理：escape

运行：python lessons/04_keyboard_input.py
"""
from psychopy import visual, core, event

win = visual.Window(size=(800, 600), color="black", units="height", fullscr=False, monitor="MiMonitor")

prompt = visual.TextStim(win, text="按 F 或 J 键（对应左右），按 ESC 退出", pos=(0.0, 0.2), color="white", height=0.05)

# ---------- 第一部分：waitKeys（阻塞式，适合每次只等一次按键）----------
prompt.text = "看：请判断中央色块是红色还是蓝色，按 F(红) 或 J(蓝)"
prompt.draw()

# 中央色块
probe = visual.Rect(win, width=0.3, height=0.3, fillColor="red")
probe.pos = (0, -0.05)
probe.draw()
win.flip()

# 等待 F 或 J，最多 5 秒；超时返回 None
keys = event.waitKeys(maxWait=5.0, keyList=["f", "j", "escape"])
print("waitKeys 返回:", keys)

if keys is None:
    print("本次没有按键（超时）")
elif "escape" in keys:
    # 用户想退出
    win.close()
    core.quit()
else:
    print("按键为:", keys[0])

# ---------- 第二部分：getKeys（非阻塞，适合帧循环）----------
# 重新开启,在一个 2 秒的帧循环里不断采样按键
prompt.text = "getKeys 演示：2 秒内连续按任意数字键"
prompt.draw()
win.flip()

clock = core.Clock()
pressed = []
while clock.getTime() < 5.0:
    # 每帧读取累积的按键；getKeys 会消费（清空）已读到的键
    new = event.getKeys(keyList=["0", "1", "2", "3", "4", "5",
                                 "6", "7", "8", "9", "escape"])
    pressed.extend(new)
    if "escape" in new:
        print("检测到退出键，提前结束循环")
        break

print("5 秒内按下的数字键:", pressed)

win.close()
core.quit()


"""
思考题
------
1. waitKeys vs getKeys 各自适用于什么场景？
2. 为什么在帧循环里每帧都要调用一次 getKeys，而不是循环结束后调一次？
3. keyList 里没包含 escape，会怎样？（点击左上角叉号也能关窗）
"""