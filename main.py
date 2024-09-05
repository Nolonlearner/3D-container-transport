# main.py
from algorithms.optimization import simulated_annealing, cost_function
from algorithms.visualization import visualize_loading
import numpy as np

def main():
    init_solution = np.random.randint(1, 100, size=20)  # 随机生成更大规模的初始解

    # 使用模拟退火算法进行优化
    best_solution, best_cost = simulated_annealing(init_solution, temp=1000, cooling_rate=0.95, iterations=10000)

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
