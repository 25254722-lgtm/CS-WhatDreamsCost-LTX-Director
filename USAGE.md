# 使用指南

## 快速开始

### 基本工作流

1. **添加节点**
   - ComfyUI → Add Node → CS-WhatDreamsCost → CS LTX Director

2. **连接输入**
   - Model：LTXV 视频模型
   - CLIP：文本编码器
   - Audio VAE（可选）：音频处理

3. **配置参数**
   - `global_prompt`：全局提示词
   - `duration_frames`：时间线总帧数
   - `frame_rate`：帧率（默认 24 FPS）

### 核心功能

#### 1. Transition 过渡控制
- `transition_smoothness`：0 (硬切) ~ 1 (平滑混合)
- 每段独立设置过渡效果

#### 2. Audio 处理
- 支持音频裁剪（trimStart、length）
- 自动检测超出范围的音频
- `audio_trim_mode`：automatic 或 strict

#### 3. Duration 自动管理
- `auto_adjust_duration`：自动扩展时间线
- `min_total_duration_frames`：最小时长底限

#### 4. 图片-音频对齐
- `auto_align_audio`：自动对齐
- `alignment_tolerance_frames`：容差阈值（默认 6 帧）

## 参数详解

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| global_prompt | String | "" | 全局提示词 |
| duration_frames | Int | 120 | 时间线帧数 |
| duration_seconds | Float | 5.0 | 时间线秒数 |
| frame_rate | Float | 24 | 帧率 FPS |
| auto_adjust_duration | Boolean | False | 自动扩展 |
| transition_smoothness | String | "" | 过渡平滑度 |
| auto_align_audio | Boolean | False | 自动对齐 |
| alignment_tolerance_frames | Int | 6 | 对齐容差 |
| audio_trim_mode | Combo | automatic | 音频裁剪模式 |

## 输出说明

- `model`：带路由的模型
- `positive`：正面条件
- `video_latent`：视频潜在表示
- `audio_latent`：音频潜在表示
- `guide_data`：导向数据
  - duration_info：时长信息
  - alignment_info：对齐报告
  - audio_validation：音频验证结果

## 最佳实践

✅ **推荐**
- 使用 120-240 帧（5-10 秒）
- 启用 `auto_adjust_duration`
- 设置 `transition_smoothness` 为 0.3-0.7
- 启用对齐检查

❌ **避免**
- 过长的时间线（> 480 帧）
- 混乱的提示词
- 不检查音视频同步

## 故障排除

### 输出质量差
- 改进提示词
- 调整 epsilon 或 transition_smoothness

### 音频不同步
```
auto_align_audio = True
alignment_tolerance_frames = 3
```

### 处理缓慢
```
duration_frames = 120      # 减少帧数
custom_width = 512         # 降低分辨率
img_compression = 23       # 增加压缩
```

## 更多信息

- [完整安装指南](INSTALLATION.md)
- [所有参数说明](README.md)
- [GitHub Issues](https://github.com/25254722-lgtm/CS-WhatDreamsCost-LTX-Director/issues)
