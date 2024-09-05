# main.py
from algorithms.optimization import simulated_annealing
from algorithms.visualization import visualize_loading
from utils.data_processing import load_data
import numpy as np

def main():
    cargo_data = load_data('data/cargo_details.csv')
    init_solution = np.random.randint(1, len(cargo_data), size=20)  # 初始化解

    # 使用模拟退火算法进行优化
    best_solution, best_cost = simulated_annealing(init_solution,cargo_data, temp=1000, cooling_rate=0.95, iterations=10000)

    print(f"Best solution: {best_solution}")
    print(f"Best cost: {best_cost}")

    # 假设货物位置的计算结果
    cargo_positions = [
        (1, 0, 0, 0, 2, 2, 2),
        (2, 2, 0, 0, 1, 1, 3),
        (3, 0, 2, 0, 1, 3, 1),
        (4, 1, 1, 1, 2, 1, 2),
        (5, 2, 2, 2, 2, 2, 2)
    ]

    container_dimensions = (5, 5, 5)  # 集装箱尺寸

    # 调用可视化函数
    visualize_loading(cargo_positions, container_dimensions)

if __name__ == "__main__":
    main()
