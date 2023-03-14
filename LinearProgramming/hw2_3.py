import cvxpy as cp
import numpy as np
c = np.array([[4, 2, 3, 4],
              [6, 4, 5, 5],
              [7, 6, 7, 6],
              [7, 8, 8, 6],
              [7, 9, 8, 6],
              [7, 10, 8, 6]])
x = cp.Variable((6, 4), integer = True)
obj = cp.Maximize(cp.sum(cp.multiply(c, x)))
con = [x >= 0,
       x <= 1,
       cp.sum(x[:, 0]) >= 1,
       cp.sum(x[:, 1]) >= 1,
       cp.sum(x[:, 2]) >= 1,
       cp.sum(x[:, 3]) >= 1,
       cp.sum(x[0, :]) <= 1,
       cp.sum(x[1, :]) <= 1,
       cp.sum(x[2, :]) <= 1,
       cp.sum(x[3, :]) <= 1,
       cp.sum(x[4, :]) <= 1,
       cp.sum(x[5, :]) <= 1,
       ]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:", prob.value)
print("最优解为:", x.value)