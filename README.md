# CS LTX Director - Enhanced ComfyUI Node

一个功能完整的 ComfyUI 节点，为 Latent Trajectory eXtended (LTX) Video 模型提供专业的视频导演台功能。

## ✨ 核心功能

### 1. **Transition（过渡）控制** 🎬
- 每段画面的过渡平滑度控制（0=硬切，1=平滑混合）
- 支持多段视频的灵活过渡效果
- 自动计算过渡窗口和高斯分布参数

### 2. **Audio Processing（音频处理）** 🔊
- **音频裁剪**：支持对音频片段的精确裁剪（trimStart、length）
- **音频验证**：自动检测音频范围超出问题
- **合成混音**：支持多个音频段的叠加混合

### 3. **Image-Audio Alignment（图片-音频校准）** 📏
- 自动检测图片和音频段的对齐偏差
- 配置对齐容差阈值（默认 6 帧）
- 生成详细的对齐报告和不对齐警告

### 4. **Duration Control（时长控制）** ⏱️
- **自动时长计算**：根据所有 segments 自动计算所需总时长
- **自动扩展**：当 segments 超出现有 duration 时自动扩展
- **最小时长底限**：防止意外收缩的安全阈值

### 5. **Diagnostic（诊断）& Reporting** 📊
- 覆盖率分析（图片覆盖百分比）
- 段计数和时长分布统计
- 自动生成优化建议

## 🚀 快速开始

### 安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/25254722-lgtm/CS-WhatDreamsCost-LTX-Director.git
cd CS-WhatDreamsCost-LTX-Director
pip install -r requirements.txt
```

### 使用

1. 在 ComfyUI 中添加 "CS LTX Director" 节点
2. 连接模型、CLIP、可选的 Audio VAE
3. 配置参数并启用高级功能
4. 运行生成

## 📚 文档

- [安装指南](INSTALLATION.md) - 详细的安装步骤和故障排除
- [使用指南](USAGE.md) - 参数说明、实际例子、高级技巧
- [API 文档](#api-documentation)

## 🔧 主要功能

### Transition 过渡控制
- 修复了 relay_options 传递 BUG
- 正确解析 transition_smoothness 参数
- 每段独立的过渡平滑度设置

### Audio 处理增强
- 音频段验证（检测裁剪越界）
- 图片-音频对齐检查
- 自动或严格的音频处理模式

### Duration 自动管理
- 自动计算所需总时长
- 可选的自动扩展功能
- 最小时长底限保护

## 📋 参数概览

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `model` | Model | - | LTXV 视频生成模型 |
| `clip` | Clip | - | 文本编码器 |
| `global_prompt` | String | "" | 全局提示词 |
| `duration_frames` | Int | 120 | 时间线总帧数 |
| `auto_adjust_duration` | Boolean | False | 自动扩展时间线 |
| `transition_smoothness` | String | "" | 过渡平滑度（0-1） |
| `auto_align_audio` | Boolean | False | 自动对齐音频 |
| `alignment_tolerance_frames` | Int | 6 | 对齐容差（帧） |

更多参数见 [USAGE.md](USAGE.md)

## 🧪 测试

```bash
python test_enhancements.py
```

所有测试应该通过：
```
✓ 时长计算测试（5 项）
✓ 音频验证测试（2 项）
✓ 对齐检查测试（3 项）
✅ 所有测试通过
```

## 📈 版本历史

### v1.0.0 (2025-06-06)
- ✅ Transition 过渡控制
- ✅ 音频裁剪和验证
- ✅ 图片-音频对齐
- ✅ 自动时长计算
- ✅ 诊断和报告

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📝 许可证

MIT License - 详见 LICENSE 文件

## 📞 支持

- 📖 [安装指南](INSTALLATION.md)
- 📚 [使用指南](USAGE.md)
- 🐛 [报告 Bug](https://github.com/25254722-lgtm/CS-WhatDreamsCost-LTX-Director/issues)
- 💬 [讨论](https://github.com/25254722-lgtm/CS-WhatDreamsCost-LTX-Director/discussions)

---

**Made with ❤️ for ComfyUI creators**