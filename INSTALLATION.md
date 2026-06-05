# 安装指南

## 系统要求

- **ComfyUI**：最新版本
- **Python**：3.10+
- **依赖库**：
  - PyTorch（通常由 ComfyUI 提供）
  - PyAV（音频处理）
  - Pillow（图片处理）
  - NumPy

## 安装步骤

### 方法 1：自动安装（推荐）

1. **下载仓库到自定义节点目录**：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/25254722-lgtm/CS-WhatDreamsCost-LTX-Director.git
```

2. **安装依赖**：
```bash
cd CS-WhatDreamsCost-LTX-Director
pip install -r requirements.txt
```

3. **重启 ComfyUI**

### 快速验证

```bash
python test_enhancements.py
```

预期：所有测试通过 ✅

## 常见问题

### ModuleNotFoundError: No module named 'av'

```bash
pip install av
# 或
conda install av -c conda-forge
```

### 节点不在列表中

检查文件结构：
```
ComfyUI/custom_nodes/CS-WhatDreamsCost-LTX-Director/
├── __init__.py
├── ltx_director.py
├── prompt_relay.py
├── patches.py
├── README.md
└── ...
```

更多详情见 INSTALLATION.md
