# 3D集装箱装载优化

## 项目概述

本项目全称为“集装箱装载优化及方案设计”，旨在开发一种基于人工智能的解决方案，用于优化船舱内集装箱的装载。项目通过利用模拟退火算法和遗传算法等优化算法，在多重约束条件下提高集装箱体积利用率和运输利润。

该项目重点研究船舱不规则形状的装载问题，并结合理论与实际应用进行探索。

## 主要功能

- **算法优化**：利用人工智能算法解决复杂的集装箱装载问题，考虑了重量限制、体积限制和承重能力等因素。
- **不规则集装箱处理**：与大多数研究不同，本项目专注于不规则形状的集装箱装载优化，这在实际应用中更为常见。
- **仿真与可视化**：模拟装载场景并可视化展示结果，确保优化方案在实际应用中具有可操作性和效果。

## 项目结构
```
3D-container-transport/
│
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── data/
│   ├── container_dimensions.csv
│   ├── data_introduce.csv
│   ├── cargo_details.csv
│   └── ship_cabin_layout.csv
├── algorithms/
│   ├── __init__.py
│   ├── optimization.py
│   └── visualization.py
├── tests/
│   ├── __init__.py
│   └── test_optimization.py
├── utils/
│   └── data_processing.py 
└── .idea/
    └── workspace.xml
    
```
### 各文件和文件夹说明
- `README.md`: 项目的总体介绍、使用方法和各文件说明。
- `main.py`: 主程序入口，负责调用算法和数据进行优化计算与展示。
- `requirements.txt`: 列出项目所需的Python依赖库，便于其他用户通过pip install -r requirements.txt安装依赖。
- `.gitignore`: 配置哪些文件或文件夹不应提交到Git版本控制中，例如虚拟环境文件、IDE配置等。
- `data/` : 存放项目的实验数据文件。
- `data/cargo_details.csv`: 存放货物的详细信息。
- `data/container_dimensions.csv`: 存放集装箱的尺寸数据。
- `data/ship_cabin_layout.csv`: 存放船舱的布局信息。
- `algorithms/__init__.py`: 算法包的初始化文件，用于导入相关模块。
- `algorithms/`: 存放算法相关的代码文件。
- `optimization.py`: 包含优化算法的实现代码，如模拟退火、遗传算法等。
- `visualization.py`: 包含用于结果可视化的代码。
- `utils/data_processing.py`: 数据处理逻辑
- `tests/`: 单元测试代码文件，确保算法的正确性和鲁棒性。
- `test/__init__.py`: 初始化测试包文件，可以暂时留空。
- `test_optimization.py`: 测试优化算法功能的代码。

## 项目流程

- 一旦你处理好了项目中的所有文件并修正了代码，整个项目的运转流程如下：

1. 数据准备：
data/cargo_details.csv: 这个文件包含所有待装载的货物的详细信息，比如货物的 ID、长、宽、高等。
data/container_dimensions.csv: 这个文件定义了集装箱的尺寸（长、宽、高）。
data/ship_cabin_layout.csv: 如果需要处理不规则船舱的装载，这个文件将定义船舱布局及其可用空间。
2. 算法运行：
在项目的 main.py 中，主函数调用算法来优化装载方案。你可以使用遗传算法（Genetic Algorithm）或模拟退火算法（Simulated Annealing Algorithm）来求解货物的最佳装载方式。
这些算法会读取 data 目录下的 CSV 文件，获取集装箱和货物的详细信息，基于这些数据生成一个初始解，并通过不断优化得到一个较优的装载方案。
3. 可视化结果：
优化算法计算出装载方案后，调用 algorithms/visualization.py 中的 visualize_loading 函数，将装载结果可视化。这个函数会生成一个三维图形，展示货物在集装箱中的布局。
4. 结果展示：
运行 main.py 后，程序会输出最优的装载方案和对应的成本（比如剩余空间或不平衡程度）。
同时，程序会弹出一个三维可视化窗口，展示货物如何放置在集装箱中。

## 安装说明

按照以下步骤在本地设置项目：

1. **克隆仓库：**
   ```bash
   git clone https://github.com/yourusername/3D-container-transport.git

2. **进入项目目录：**
   ```bash
   cd 3D-container-transport

3. **创建虚拟环境并激活：**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows上使用 `venv\Scripts\activate`

4. **安装所需依赖：**
   ```bash
   pip install -r requirements.txt
   
## 运行项目

1. **运行主脚本：**
   ```bash
   python main.py
  - 这将执行装载优化算法，并输出最佳装载方案和成本。

## 许可证

- 本项目使用 MIT 许可证 进行许可。
