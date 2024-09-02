# tests/test_optimization.py

import unittest
from algorithms.optimization import simulated_annealing, cost_function


class TestSimulatedAnnealing(unittest.TestCase):

    def test_optimization(self):
        init_solution = [1, 2, 3, 4, 5]
        best_solution, best_cost = simulated_annealing(init_solution, cost_function)

        # 检查输出结果类型
        self.assertIsInstance(best_solution, list)
        self.assertIsInstance(best_cost, (int, float))

        # 检查最优成本是否合理
        self.assertGreaterEqual(best_cost, 0)


if __name__ == '__main__':
    unittest.main()
