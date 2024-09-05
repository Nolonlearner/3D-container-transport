# algorithms/optimization.py
import numpy as np


def cost_function(solution):
    """
    计算装载方案的成本。
    假设：每个值代表货物重量。我们引入一个目标值来优化货物的重量分布，或者避免过度装载。

    参数：
    solution: 方案（NumPy数组）

    返回：
    总成本值
    """
    max_capacity = 500  # 集装箱的最大承载能力
    ideal_weight = 250  # 假设最优重量分布为250
    weight = np.sum(solution)  # 计算方案的总重量

    # 计算与理想重量的差距
    cost = np.abs(weight - ideal_weight)

    # 如果超过最大容量，增加惩罚
    if weight > max_capacity:
        penalty = (weight - max_capacity) ** 2
        cost += penalty

    return cost


def simulated_annealing(init_solution, temp=1000, cooling_rate=0.9, iterations=10000):
    """
    模拟退火算法的实现。

    参数：
    init_solution: 初始解（列表形式）
    temp: 初始温度
    cooling_rate: 降温速率
    iterations: 迭代次数

    返回：
    best_solution: 最优解
    best_cost: 最小成本
    """
    current_solution = np.array(init_solution)
    current_cost = cost_function(current_solution)  # 计算初始解的成本

    best_solution = current_solution.copy()
    best_cost = current_cost

    for i in range(iterations):
        # 生成新的候选解，通过在原解的基础上添加随机扰动
        new_solution = current_solution + np.random.randint(-5, 6, size=len(current_solution))

        # 限制解的范围，例如让每个值在1到100之间
        new_solution = np.clip(new_solution, 1, 100)

        new_cost = cost_function(new_solution)  # 计算新解的成本

        # 判断是否接受新解
        if new_cost < current_cost or np.exp((current_cost - new_cost) / temp) > np.random.rand():
            current_solution = new_solution
            current_cost = new_cost

            # 如果找到更好的解，更新最优解
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        # 降温，逐渐减小搜索范围
        temp *= cooling_rate

    return best_solution.tolist(), best_cost
