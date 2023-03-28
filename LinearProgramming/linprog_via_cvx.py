import cvxpy as cp
import numpy as np
c = np.array([[3.75832409 , 3.75832409 , 5.85768726 , 4.06970515 , 5.85234996, 7.11512474],
              [5.79870675 , 9.19918475 , 2.70416346 , 4.25       , 1.11803399, 5.30330086]])
x = cp.Variable((2, 6))
obj = cp.Minimize(cp.sum(cp.multiply(c, x)))
con = [x >= 0,
       cp.sum(x[:, 0]) >= 3,
       cp.sum(x[:, 1]) >= 5,
       cp.sum(x[:, 2]) >= 4,
       cp.sum(x[:, 3]) >= 7,
       cp.sum(x[:, 4]) >= 6,
       cp.sum(x[:, 5]) >= 11,
       cp.sum(x[0, :]) <= 20,
       cp.sum(x[1, :]) <= 20,
       ]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:", prob.value)
print("最优解为:", x.value)