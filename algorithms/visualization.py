# algorithms/visualization.py
import matplotlib.pyplot as plt

def visualize_loading(cargo_positions, container_dimensions):
    """
    可视化货物装载到集装箱中的情况。

    参数：
        cargo_positions (list of tuples): 每个元组包含 (cargo_id, x, y, z, length, width, height)。
        container_dimensions (tuple): 集装箱的尺寸 (length, width, height)。
    """
    fig = plt.figure()  # 创建一个新的三维图形
    ax = fig.add_subplot(111, projection='3d')  # 添加一个 3D 的子图

    # 绘制集装箱
    container_length, container_width, container_height = container_dimensions  # 解压集装箱的尺寸
    ax.bar3d(0, 0, 0, container_length, container_width, container_height, color='cyan', alpha=0.1)  # 绘制集装箱的三维立方体

    # 绘制每一个货物
    for cargo in cargo_positions:
        cargo_id, x, y, z, length, width, height = cargo  # 解压货物信息
        ax.bar3d(x, y, z, length, width, height, alpha=0.6)  # 绘制货物的三维立方体

    ax.set_xlabel('长度')  # 设置 X 轴标签为 "长度"
    ax.set_ylabel('宽度')  # 设置 Y 轴标签为 "宽度"
    ax.set_zlabel('高度')  # 设置 Z 轴标签为 "高度"
    ax.set_title('货物装载可视化')  # 设置图形标题为 "货物装载可视化"

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
    plt.show()  # 显示图形
