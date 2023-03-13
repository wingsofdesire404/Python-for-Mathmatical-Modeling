import cvxpy as cp
import numpy as np
import pandas as pd
d1 = pd.read_excel("Pdata5_6.xlsx", header = None)
d2 = d1.values; c = d2[:-1, :-1]
d = d2[-1, :-1].reshape(1, -1); e = d2[:-1, -1].reshape(-1, 1)
x = cp.Variable((6,8))
obj = cp.Minimize(cp.sum(cp.multiply(c,x))) # cp.mutiply为逐个元素乘法
con = [cp.sum(x, axis = 1, keepdims = True) <= e, cp.sum(x, axis = 0, keepdims = True) == d, x >= 0]
prob = cp.Problem(obj, con) 
# axis = 0 <=> sum of row <=> Xij = 1 for j from 1 to 5
# axis = 1 <=> sum of col <=> Xij = 1 for i from 1 to 5
prob.solve(solver = 'GLPK_MI', verbose = True)
