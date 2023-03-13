import cvxpy as cp
import numpy as np
c = np.array([[1, 0, 0, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 1],
             [0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 1]])
x = cp.Variable((6, 8), integer = True)
obj = cp.Minimize(cp.sum((x)))
con = [x >= 0,
       x <= 1,
       cp.sum(x[:, 0]) >= 1,
       cp.sum(x[:, 1]) >= 1,
       cp.sum(x[:, 2]) >= 1,
       cp.sum(x[:, 3]) >= 1,
       cp.sum(x[:, 4]) >= 1,
       cp.sum(x[:, 5]) >= 1,
       cp.sum(x[:, 6]) >= 1,
       cp.sum(x[:, 7]) >= 1,
       
       ]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:", prob.value)
print("最优解为:", x.value)