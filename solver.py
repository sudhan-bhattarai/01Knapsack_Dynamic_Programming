import numpy as np
from typing import List, Union, Dict


class KnapsackSolver:
    def __init__(
            self,
            weights: Union[List[int], np.ndarray],
            values: Union[List[int], np.ndarray],
            capacity: int
        ):
        """
        Initialize the Knapsack solver.

        Args:
            values (list or np.ndarray): Item values (profits or discounts).
            weights (list or np.ndarray): Item weights (costs or prices).
            capacity (int): Maximum weight (or budget).
        """
        # Convert to NumPy arrays for consistency
        self.values = np.array(values, dtype=int)
        self.weights = np.array(weights, dtype=int)
        self.capacity = capacity

        # Validations
        assert self.values.ndim == 1 and self.weights.ndim == 1, \
            "values and weights must be 1D arrays"
        assert len(self.values) == len(self.weights), \
            "values and weights must have the same length"
        assert np.all(self.values >= 0), \
            "All values must be non-negative"
        assert np.all(self.weights >= 0), \
            "All weights must be non-negative"
        assert isinstance(capacity, int) and capacity >= 0, \
            "capacity must be a non-negative integer"

        self.n = len(self.values)
        self.dp = np.zeros(capacity + 1, dtype=int)
        self.choice_matrix = np.full(
            (self.n + 1, capacity + 1),
            False,
            dtype=bool
        )

    def solve(self) -> Dict[str, Union[int, List[int]]]:
        """
        Solves the knapsack problem and returns chosen items, total value,
        and total weight.
        """
        for i in range(1, self.n + 1):
            w = self.weights[i - 1]
            v = self.values[i - 1]
            # reverse loop for 1D DP
            for cap in range(self.capacity, w - 1, -1):
                if self.dp[cap] < self.dp[cap - w] + v:
                    self.dp[cap] = self.dp[cap - w] + v
                    self.choice_matrix[i][cap] = True

        # Backtrack to find chosen items
        chosen_items = []
        cap = self.capacity
        for i in range(self.n, 0, -1):
            if self.choice_matrix[i][cap]:
                chosen_items.append(i - 1)  # store original index
                cap -= self.weights[i - 1]

        chosen_items.reverse()  # original order
        total_value = int(self.dp[self.capacity])
        total_weight = 0
        if chosen_items:
            total_weight = int(np.sum(self.weights[chosen_items]))

        return {
            "chosen_items": chosen_items,
            "total_value": total_value,
            "total_weight": total_weight
        }
