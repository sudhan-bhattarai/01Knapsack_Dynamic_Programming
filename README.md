# Knapsack Problem

The **Knapsack Problem** is a classic optimization problem that seeks to maximize the total value of selected items without exceeding a given capacity (or budget).

We are given:
- A set of `n` items, each with a **value** and a **weight**.
- A maximum capacity (or budget) `W`.

**Goal:** Select a subset of items such that:
- The **sum of weights** does not exceed `W`.
- The **total value** is maximized.

This problem can be solved in multiple ways, including:
- **Recursive methods**
- **Mixed-Integer Programming (MIP)** formulations
- **Dynamic Programming (DP)** – a computationally efficient approach using a tabular method.

---

## **MIP Formulation**

Given:
- `n` items with values `value_1, ..., value_n`
- Weights `weight_1, ..., weight_n`
- Maximum budget (capacity) `W`

The problem is formulated as:

**Maximize:**
value_1 * x_1 + value_2 * x_2 + ... + value_n * x_n

**Subject to:**
- weight_1 * x_1 + weight_2 * x_2 + ... + weight_n * x_n <= W
- x_i in {0, 1} for all i = 1, ..., n
---

## **Dynamic Programming Approach**

**Input**
- `n` = number of items 
- `weights[1 ... n]`, `values[1 ... n]`
- `capacity` = maximum capacity

**Output**

Maximum total value

**Algorithm**
- Initialize: dp[0 ... capacity] = 0 
```bash
- For i = 1 to n:
    w = weights[i]
    v = values[i]
    For cap = capacity down to w:
      dp[cap] = max(dp[cap], dp[cap - w] + v)
```
- Return dp[capacity]
---

## **Usage**

### **Solver Class**
```python
from solver import KnapsackSolver

# Example data
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

# Create a solver instance
KS = KnapsackSolver(weights, values, capacity)

# Solve the problem
result = KS.solve()

print("Chosen Items:", result["chosen_items"])
print("Total Value:", result["total_value"])
print("Total Weight:", result["total_weight"])
```

### Example Notebook

- An example of using this solver for Amazon shopping optimization (maximize the total discount in a holiday-sale 
  season) is 
  provided in:
  - Jupyter notebook: `test_amazon_shopping.ipynb`
  - Data file: `amazon_shopping.csv`