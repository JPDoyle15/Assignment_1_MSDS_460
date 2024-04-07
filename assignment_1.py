from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

model = LpProblem("Minimize_Z", LpMinimize)

# Decision Variables
a = LpVariable('a', lowBound=7, cat='Continuous')
b = LpVariable('b', lowBound=7, cat='Continuous')
c = LpVariable('c', lowBound=7, cat='Continuous')
d = LpVariable('d', lowBound=7, cat='Continuous')
e = LpVariable('e', lowBound=7, cat='Continuous')

# Objective Function
model += 0.74 * a + 2.83 * b + 0.09 * c + 0.79 * d + 1.00 * e

# Constraints
model += 75*a + 65*b + 10*c + 135*d + 65*e <= 35000
model += -110*a - 240*b - 160*c - 130*d - 25*e <= -14000
model += -24*a - 23*b - 3*c - 8*d - 2*e <= -350
model += -0.1*a - 19*b - 2.5*d <= -140
model += -10*a - 10*b - 320*d - 80*e <= -9100
model += -0.4*a - 0.4*b - 2*c - 2.3*e <= -126
model += -410*a - 410*b - 420*d - 470*e <= -32900

# Model
model.solve()

print(f"Chicken Breat = {round(a.varValue,2)} servings")
print(f"Salmon = {round(b.varValue,2)} servings")
print(f"White Rice = {round(c.varValue,2)} servings")
print(f"Milk = {round(d.varValue,2)} servings")
print(f"Spinach = {round(e.varValue,2)} servings")
print(f"Lowest Cost = ${round(value(model.objective),2)}")
