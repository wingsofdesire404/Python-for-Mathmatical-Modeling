import cvxpy as cp
import numpy as np
c = np.array([[3, -7, -1, -6],
              [9, -1, 5, 0]])
x = cp.Variable((2, 4))
obj = cp.Maximize(cp.sum(cp.multiply(c, x)))
con = [x >= 0,
       cp.sum(x[0, :]) == 100,
       cp.sum(x[1, :]) == 200,
       0.03 * x[0, 0] + 0.01 * x[0, 1] + 0.02 * x[0, 2] + 0.01 * x[0, 3] <= 0.025,
       0.03 * x[1, 0] + 0.01 * x[1, 1] + 0.02 * x[1, 2] + 0.01 * x[1, 3] <= 0.015,
       x[0, 3] + x[1, 3] <= 50
       ]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:", prob.value)
print("最优解为:", x.value)