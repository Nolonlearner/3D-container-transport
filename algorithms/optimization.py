import numpy as np

def simulated_annealing(init_solution, cost_function, temp, cooling_rate, iterations):
    current_solution = np.array(init_solution)  # 确保输入是 NumPy 数组
    current_cost = cost_function(current_solution)
    best_solution = current_solution
    best_cost = current_cost

    for i in range(iterations):
        new_solution = np.copy(current_solution)
        np.random.shuffle(new_solution)  # 随机扰动

        new_cost = cost_function(new_solution)
        delta_cost = new_cost - current_cost

        if delta_cost < 0 or np.random.rand() < np.exp(-delta_cost / temp):
            current_solution = new_solution
            current_cost = new_cost

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        temp *= cooling_rate

    return best_solution, best_cost

# 示例成本函数
def cost_function(solution):
    return np.sum(solution**2)  # 示例成本函数
