# main.py
from algorithms.optimization import simulated_annealing
from algorithms.visualization import visualize_loading
from utils.data_processing import load_data
from algorithms.calculatePosition import calculate_positions
import numpy as np

def main():
    # 加载货物数据
    cargo_data = load_data('data/cargo_details.csv')

    # 提取重量和体积
    weights = cargo_data['Weight'].values  # 货物重量
    volumes = cargo_data['Volume'].values  # 货物体积

    # 随机生成更大规模的初始解，确保范围在 0 到 len(weights) - 1 之间
    init_solution = np.random.randint(0, len(weights), size=len(weights))  # 修改这里

    # 使用模拟退火算法进行优化
    best_solution, best_cost = simulated_annealing(init_solution, cargo_data, temp=1000, cooling_rate=0.95, iterations=10000)

    print(f"Best solution: {best_solution}")
    print(f"Best cost: {best_cost}")

    container_dimensions = (5, 10, 10)  # 集装箱尺寸
    # 计算货物位置
    cargo_positions = calculate_positions(best_solution, cargo_data, container_dimensions)
    # 调用可视化函数
    visualize_loading(cargo_positions, container_dimensions)

if __name__ == "__main__":
    main()
