import cvxpy as cp
import numpy as np
c = np.array([20, 90, 80, 70, 30])
x = cp.Variable(5, integer = True)
obj = cp.Minimize(c @ x)
a = np.array([[-1, -1, 0, 0, -1],
             [0, 0, -1, -1, 0],
             [3, 0, 2, 0, 0],
             [0, 3, 0, 2, 1]])
b = np.array([-30, -30, 120, 48])
con = [
       x >= 0,
       a @ x <= b
       ]
prob = cp.Problem(obj, con)
prob.solve()
print("最优值为:", prob.value)
print("最优解为:", x.value)