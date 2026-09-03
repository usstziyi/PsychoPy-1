"""
课程 06 · 图片与纹理刺激
==========================
核心概念：
  - visual.ImageStim : 从文件或 numpy 数组加载图像显示
  - 直接生成 numpy 纹理（正弦光栅、高斯等）
  - visual.GratingStim : 光栅刺激，带 mask（形状遮罩）和相位
  - 相位动画（phase）产生漂移效果；用帧循环驱动

运行：python lessons/06_image_grating_texture.py
"""
import numpy as np
from psychopy import visual, core

win = visual.Window(size=(900, 500), color="grey", units="height",
                    fullscr=False)

# ---------- 第一部分：用 numpy 生成一张渐变图并显示为 ImageStim ----------
# 生成 256x256 的水平渐变数组，值域 [0,1]
gradient = np.tile(np.linspace(0, 1, 256), (256, 1))   # shape (256,256)
img_stim = visual.ImageStim(
    win,
    image=gradient,          # 直接接受 numpy 数组
    size=(0.6, 0.6),
    pos=(0.0, 0.0),
)
img_stim.draw()
win.flip()
core.wait(1.5)

# ---------- 第二部分：正弦光栅（GratingStim）漂移动画 ----------
grating = visual.GratingStim(
    win,
    tex="sin",              # 内置正弦纹理
    mask="gauss",           # 高斯遮罩（边缘平滑的圆斑）
    units="height",
    size=1.0,
    pos=(0.45, 0.0),
    sf=4.0,                 # 空间频率（周期/单位高度）
    phase=0.0,
    # 注意：不要设 color="grey"——grey 在 rgb 色彩空间亮度为 0，
    # 会让光栅调制幅度归零，与灰色背景融为一体而看不见
)

# 帧循环：相位递增产生漂移
n_frames = 900
for f in range(n_frames):
    grating.phase += 0.1       # 相位随帧更新
    grating.draw()
    win.flip()

core.wait(5)
win.close()

# ---------- 第三部分：随机纹理（噪声）另一窗口演示 ----------
win2 = visual.Window(size=(500, 500), color="black", units="norm",
                     fullscr=False)
rng = np.random.default_rng(0)
noise = rng.random((128, 128))
noise_stim = visual.ImageStim(win2, image=noise, size=(1.0, 1.0)) # 长宽各50%
noise_stim.draw()
win2.flip()
core.wait(5)

win2.close()
core.quit()


"""
思考题
------
1. GratingStim 的 phase 递增为什么能产生"漂移"视觉？
2. mask='gauss' 起什么作用？换成 'circle' 呢？
3. ImageStim 的 image 参数能否直接传一张磁盘上的图片路径？
"""