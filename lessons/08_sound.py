"""
课程 08 · 声音刺激
====================
核心概念：
  - sound.Sound(value, secs, stereo) : 播放正弦音 / 加载音频文件
  - .play() / .stop() / .isDone
  - 与视觉刺激在帧循环中同步；用 clock 对齐
  - 用 numpy 生成自定义波形（如双音）

运行：python lessons/08_sound.py
（需要一个音频文件 test.wav；否则本课自动用内置正弦音）
"""
import os
import numpy as np
from psychopy import sound, visual, core

win = visual.Window(size=(800, 500), color="black", units="height",
                    fullscr=False)

# ---------- 1. 播放内置正弦音（440Hz，A音）----------
beep = sound.Sound(
    value=440,      # 频率 Hz
    secs=0.5,       # 时长
    stereo=True,
)
beep.play()
print("播放 440Hz 正弦 0.5s...")
core.wait(0.6)


# ---------- 2. 尝试加载本地 wav（若存在）----------
wav_path = "test.wav"   # 可自己放一个 test.wav 到当前目录
if os.path.exists(wav_path):
    snd = sound.Sound(wav_path)
    snd.play()
    core.wait(min(snd.getDuration(), 1.5))
else:
    print(f"[信息] 未找到 {wav_path}，跳过文件播放。")


# ---------- 3. 视觉 + 音频同步演示 ----------
msg = visual.TextStim(win, text="", pos=(0, 0.2), color="white", height=0.1)
tone = sound.Sound(value=880, secs=0.3)     # 更高音，用于提示

n_reps = 4
clock = core.Clock()
for i in range(n_reps):
    # 显示文字并同步放一个提示音
    msg.text = f"第 {i+1}/{n_reps} 次"
    msg.draw()
    win.flip()

    tone.play()
    # 显示一小段时间（配合声音）
    core.wait(0.7)

# ---------- 4. 用 numpy 自定义波形并播放 ----------
sr = 44100
t = np.linspace(0, 0.5, int(sr * 0.5), endpoint=False)
custom = np.concatenate([np.sin(2*np.pi*523*t), np.sin(2*np.pi*784*t)])  # C→G
custom_norm = custom / np.max(np.abs(custom))

note = sound.Sound(custom_norm, sampleRate=sr)
note.play()
print("播放自定义和弦...")
core.wait(1.0)

win.close()
core.quit()


"""
思考题
------
1. sound.Sound 的 value 可以是频率(Hz)或音频文件路径，怎么区分？
2. 如何精确地把声音和视觉刺激对齐到同一毫秒？（提示：用 clock + flip 返回时间）
3. 循环播放音频（音乐节律）应该怎么做？
"""