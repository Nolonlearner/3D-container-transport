from algorithms.optimization import simulated_annealing, cost_function

init_solution = [1, 2, 3, 4, 5]
best_solution, best_cost = simulated_annealing(init_solution, cost_function, temp=100, cooling_rate=0.99, iterations=1000)

print(f"Best solution: {best_solution}")
print(f"Best cost: {best_cost}")
