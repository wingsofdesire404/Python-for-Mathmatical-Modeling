import numpy as np
from scipy.optimize import linprog
c = np.array([-2, -1, 0, 0, 0])
# A_ub = np.array([[0, 5, 1, 0, 0],
#                 [6, 2, 0, 1, 0],
#                 [1, 1, 0, 0, 1]
#                 ])
# b_ub = np.array([10, 16, 8, 1800, 8700, 5300])
# A_eq = np.array([[-2.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
# b_eq = np.array([1.0, 0.0])
A_eq = np.array([[0, 5, 1, 0, 0],
                 [6, 2, 0, 1, 0],
                 [1, 1, 0, 0, 1]
                 ])
b_eq = np.array([15, 24, 5])
x1_bound = (0.0, np.inf)
x2_bound = (0.0, np.inf)
x3_bound = (0.0, np.inf)
x4_bound = x5_bound = (0.0, np.inf)
bounds = [x1_bound, x2_bound, x3_bound, x4_bound, x5_bound]
result = linprog(c, A_ub=None, b_ub=None, A_eq= A_eq, b_eq= b_eq, bounds=bounds)
print(result)
print(result.fun)