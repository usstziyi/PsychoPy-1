# PsychoPy 循序渐进学习计划

本计划基于官方文档和源码仓库整理，遵循 **由易到难、逐课递进** 的原则，
将知识分解到 `lessons/` 目录下的若干 `.py` 文件中。每课可独立运行。

> 参考来源
>
> - 官网首页：<https://psychopy.org/>
>
> - 文档总览：<https://psychopy.org/documentation.html>
>
> - 教学资源：<https://psychopy.org/teaching/index.html>
>
> - GitHub 仓库：<https://github.com/psychopy/psychopy>

***

## 一、依赖环境（以下仅作为文档记录，本仓库不实际安装）

> ⚠️ 提示：本仓库 `pyproject.toml` 声明 `requires-python = ">=3.14"`。
> 当前 PsychoPy 对 Python 3.14 的支持仍在跟进，建议实际运行时使用
> Python 3.9 \~ 3.12（尤其推荐 PsychoPy Standalone 自带解释器，或在
> 官方支持的虚拟环境中安装）。

### 1. 核心依赖（pip）

```bash
pip install psychopy
```

安装 PsychoPy 会顺带引入其运行时依赖。可以显式补齐常用库：

```bash
pip install psychopy numpy scipy pandas openpyxl matplotlib
```

### 2. 各依赖用途

| 依赖           | 用途                     |
| ------------ | ---------------------- |
| `psychopy`   | 实验呈现核心（窗口、刺激、计时、输入、数据） |
| `numpy`      | 数组运算、生成刺激像素、条件随机化      |
| `scipy`      | 信号处理、滤波器（音频/视觉）        |
| `pandas`     | 数据分析、结果读取              |
| `openpyxl`   | 将数据保存为 `.xlsx`         |
| `matplotlib` | 事后可视化、绘图               |

### 3. 音频/显示后端（可选，按平台）

- **Windows**：使用自带的声卡驱动，AudioLib / pyo 后端即可。

- **macOS / Linux**：可能需要额外系统库，参见官方文档。

### 4. 建议的虚拟环境

如果坚持不使用 PsychoPy Standalone，推荐在本项目内用 uv 创建隔离环境：

```bash
uv venv .venv --python 3.12
uv pip install psychopy numpy scipy pandas openpyxl matplotlib
```

> 注意：当前仓库 `.venv` 为 uv 生成，若其 Python 版本为 3.14 且 psychoPy
> 不支持，请重新用 3.12 创建。

***

## 二、课程大纲（共 9 课 + 综合实战）

| 课次 | 文件                                    | 核心知识点                                | 难度   |
| -- | ------------------------------------- | ------------------------------------ | ---- |
| 01 | `lessons/01_hello_window.py`          | Window、TextStim、flip、core.wait       | ★    |
| 02 | `lessons/02_stimuli_shapes.py`        | 形状刺激（Rect/Circle/Line/Polygon）、颜色、位置 | ★    |
| 03 | `lessons/03_timing_and_clock.py`      | 刷新率、Clock、帧同步计时                      | ★★   |
| 04 | `lessons/04_keyboard_input.py`        | event.waitKeys / getKeys、按键反应        | ★★   |
| 05 | `lessons/05_mouse_and_rating.py`      | Mouse、RatingScale、点击反馈               | ★★   |
| 06 | `lessons/06_image_grating_texture.py` | ImageStim、GratingStim、动态纹理           | ★★★  |
| 07 | `lessons/07_loops_and_data.py`        | TrialHandler、条件随机、数据记录               | ★★★  |
| 08 | `lessons/08_sound.py`                 | sound 模块、音频刺激、节律                     | ★★★  |
| 09 | `lessons/09_full_experiment.py`       | 完整范式（fMRI局部处理 + RT 实验）               | ★★★★ |

每课底部都给出“思考题”，用于自测。

***

## 三、课程内容

### 课程 01 · 打开一个窗口（Hello World）

知识点：`visual.Window`、`visual.TextStim`、`stim.draw()`、
`win.flip()`（把画面“显示”到屏幕）、`core.wait`、`core.quit`。

运行：`python lessons/01_hello_window.py`

### 课程 02 · 基础形状刺激

知识点：`visual.Rect / Circle / Line / Polygon / Dot`，
坐标单位（`norm`/`height`/`deg`）、位置 `pos`、尺寸、填充色 `fillColor`。

运行：`python lessons/02_stimuli_shapes.py`

### 课程 03 · 计时与时钟

知识点：显示器刷新率（常规 60Hz）、`win.monitorFramePeriod`、
每帧 `win.flip()` 的垂直同步、`core.Clock` 测量呈现时长。

运行：`python lessons/03_timing_and_clock.py`

### 课程 04 · 键盘输入

知识点：`event.waitKeys`、`event.getKeys`、`keyList`、
在循环里按帧采样按键、退出键 `escape`。

运行：`python lessons/04_keyboard_input.py`

### 课程 05 · 鼠标与评定量表

知识点：`visual.Mouse`、按钮/位置、点击检测、
`visual.RatingScale`（李克特式量表，适合问卷调查）。

运行：`python lessons/05_mouse_and_rating.py`

### 课程 06 · 图片与纹理刺激

知识点：`visual.ImageStim`、直接用 numpy 数组生成纹理、
`visual.GratingStim`（正弦光栅）、`mask`、相位动画。

运行：`python lessons/06_image_grating_texture.py`

### 课程 07 · 试次循环与数据记录

知识点：`data.TrialHandler`、条件列表、随机化（`method='random'`）、
试次内记录反应、`saveAsWideText` / `saveAsExcel` 导出数据。

运行：`python lessons/07_loops_and_data.py`（会生成数据文件）

### 课程 08 · 声音刺激

知识点：`sound.Sound`、播放与循环、加载音频文件、
与视觉刺激在循环中同步播放（stroop 式双通道）。

运行：`python lessons/08_sound.py`

### 课程 09 · 综合实战：反应时实验（Stroop 风格）

知识点：整合前面所有内容——窗口、文字/音频双通道刺激、
计时、按键采样、试次循环、数据导出、退出处理。
适合作为最终项目模板。

运行：`python lessons/09_full_experiment.py`（会生成 `results_*.csv`）

***

## 四、常见问题 / 逻辑注意点

- **必须先** **`flip()`** **才显示**：`draw()` 只是入列绘制命令，`win.flip()`
  才真正把帧呈现在屏幕（并阻塞到下一帧刷新）。

- **计时用时钟，不要用** **`sleep`**：`core.wait` 用于设置延时，但精细计时
  应结合 `win.flip()` 的帧同步和 `core.Clock`。

- **`getKeys`** **会累积结果**：在帧循环中建议每帧调用一次并及时清空，
  否则键盘事件会堆积导致误判。

- **`TrialHandler`** **结束记得调用** **`trials.next()`**：或用 `for trial in trials`，
  循环结束后 `handler.saveAsWideText(...)` 保存。

- **结束后务必** **`win.close()`** **与** **`core.quit()`**，释放窗口与音频资源。

***

## 五、学习路线建议

1. 依次运行 01→09，先看现象，再读代码理解每行用途。
2. 练习：给每个形状改颜色/位置；把固定时长改成帧数；加一个“空格继续”逻辑。
3. 参考官方 [Coder Tutorials](https://psychopy.org/coder/index.html) 与
   [Building Experiments](https://psychopy.org/online/index.html) 做深化。
4. 兴趣方向：fMRI/EEG 需要更高时序精度——重点看课程 03、09。

