import os
import numpy as np
from psychopy import sound, visual, core

win = visual.Window(size=(800, 500), color="black", units="height",
                    fullscr=False, monitor="testMonitor")

# ---------- 查看可用的音频设备 ----------
import sounddevice as sd
print("可用的音频设备：")
print(sd.query_devices())

"""
可用的音频设备：
   0 Microsoft 声音映射器 - Output, MME (0 in, 2 out)
<  1 扬声器 (High Definition Audio Devi, MME (0 in, 6 out)
   2 Digital Audio (S/PDIF) (High De, MME (0 in, 2 out)
   3 Mi monitor (NVIDIA High Definit, MME (0 in, 2 out)
   4 主声音驱动程序, Windows DirectSound (0 in, 2 out)
   5 扬声器 (High Definition Audio Device), Windows DirectSound (0 in, 6 out)
   6 Digital Audio (S/PDIF) (High Definition Audio Device), Windows DirectSound (0 in, 2 out)
   7 Mi monitor (NVIDIA High Definition Audio), Windows DirectSound (0 in, 2 out)
   8 Digital Audio (S/PDIF) (High Definition Audio Device), Windows WASAPI (0 in, 2 out)
   9 Mi monitor (NVIDIA High Definition Audio), Windows WASAPI (0 in, 2 out)
  10 扬声器 (High Definition Audio Device), Windows WASAPI (0 in, 2 out)
  11 SPDIF Out (HD Audio SPDIF out), Windows WDM-KS (0 in, 2 out)
  12 Speakers (HD Audio Headphone/Speakers), Windows WDM-KS (0 in, 6 out)
  13 Output (NVIDIA High Definition Audio), Windows WDM-KS (0 in, 2 out)
  14 耳机 (@System32\drivers\bthhfenum.sys,#2;%1 Hands-Free%0
;(APos2 - Find My)), Windows WDM-KS (0 in, 1 out)
  15 耳机 (@System32\drivers\bthhfenum.sys,#2;%1 Hands-Free%0
;(APos2 - Find My)), Windows WDM-KS (1 in, 0 out)
  16 耳机 (), Windows WDM-KS (0 in, 2 out)
"""

in_idx, out_idx = sd.default.device   # 例如 [-1, 1]
print("默认输入设备编号:", in_idx)
print("默认输出设备编号:", out_idx)



# ---------- 1. 播放内置正弦音（440Hz，A音）----------
beep = sound.Sound(
    value=440,
    secs=0.5,
    stereo=True,
    speaker="扬声器 (High Definition Audio Device)",  
)
print(beep.speaker.index)
beep.play()
print("播放 440Hz 正弦 0.5s...")
core.wait(3)

win.close()
core.quit()
exit()