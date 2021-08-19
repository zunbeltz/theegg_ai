"""Maximize cow milk production subject to cow total weight contrain."""

from pulp import (LpProblem, LpVariable, LpInteger, LpMaximize,
                  LpStatus, value)
from data import cows, weight_limit


items = list(sorted(cows.keys()))

# We want to maximize the milk
m = LpProblem("Cow problem", LpMaximize)

# We create x0, x1 variable for each cow.
# If x_i = 1 the cow is in the truck, otherwise it is out
x = LpVariable.dicts('x', items, lowBound=0, upBound=1, cat=LpInteger)

# The sum of milk is the function we want to maximize
m += sum(cows[i][1]*x[i] for i in items)

# The constrain is the sum of the weight
m += sum(cows[i][0]*x[i] for i in items) <= weight_limit

print(m)

# Execute the sovler
m.solve()

# Print if optimal value was achived
print("Status = %s" % LpStatus[m.status])

# Gather the solution
solution = [i for i in items if x[i].varValue == 1]

# Solution milk
solution_milk = value(m.objective)
solution_weight = sum([cows[i][0] for i in solution])

print()
print("The solution by linear programming")
print("-"*20)
print(f"Limit weight: {weight_limit}")
print(f"Soluiton weight: {solution_weight}")
print(f"Soluiton milk: {solution_milk}")
print(f"Solution cow list: {solution}")
