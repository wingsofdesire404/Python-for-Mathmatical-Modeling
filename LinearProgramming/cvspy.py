import cvxpy as cp

# Define the variables
x1 = cp.Variable()
x2 = cp.Variable()

# Define the objective function
obj = cp.Minimize(2*x1 + 3*x2)

# Define the constraints
constraints = [
    x1 + x2 <= 10,
    2*x1 + 5*x2 >= 15,
    x1 >= 0,
    x2 >= 0
]

# Solve the problem
prob = cp.Problem(obj, constraints)
prob.solve()

# Print the optimal values
print("Optimal value of x1:", x1.value)
print("Optimal value of x2:", x2.value)
print("Optimal value of the objective function:", prob.value)
