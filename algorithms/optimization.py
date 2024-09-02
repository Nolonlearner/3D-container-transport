# algorithms/optimization.py
import numpy as np

def cost_function(solution):
    """
    计算装载方案的成本，示例函数。

    参数：
    solution: 方案（NumPy数组）

    返回：
    总成本值
    """
    return np.sum(solution ** 2)  # 示例成本函数

def simulated_annealing(init_solution, temp=100, cooling_rate=0.99, iterations=1000):
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
    current_cost = cost_function(current_solution)  # 直接调用定义的 cost_function

    best_solution = current_solution.copy()
    best_cost = current_cost

    for i in range(iterations):
        # 生成邻域解
        new_solution = current_solution + np.random.randint(-1, 2, size=len(current_solution))

        # 添加一个边界条件，确保解的值在合理范围内，比如说从 1 到 10
        new_solution = np.clip(new_solution, 1, 10)

        new_cost = cost_function(new_solution)  # 直接调用定义的 cost_function

        # 如果新解更优或满足接受概率，则更新当前解
        if new_cost < current_cost or np.exp((current_cost - new_cost) / temp) > np.random.rand():
            current_solution = new_solution
            current_cost = new_cost

            # 更新最优解
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        # 降温
        temp *= cooling_rate

    return best_solution.tolist(), best_cost
