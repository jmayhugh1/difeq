import numpy as np
import sympy as sp
from sympy import symbols, Function, Eq, dsolve

# Define the differential equation using SymPy
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diffeq = Eq(y.diff(x, 4) + 3*y.diff(x, 3) - 2*y.diff(x, 2) - 4*y.diff(x) + 0.5*y, 0)

# Display the differential equation
print("Differential Equation:")
sp.pprint(diffeq)

# Solve the characteristic equation numerically
coefficients = [1, 3, -2, -4, 0.5]
roots = np.roots(coefficients)
def round_root(r, decimals=6):
    return complex(round(r.real, decimals), round(r.imag, decimals))

rounded_roots = [round_root(r) for r in roots]

# Categorize roots
real_roots = []
complex_roots = []

for r in rounded_roots:
    if abs(r.imag) < 1e-6:
        real_roots.append(r.real)
    else:
        # To avoid duplication, only add one from each complex conjugate pair
        if (r.real, r.imag) not in [(c.real, c.imag) for c in complex_roots]:
            complex_roots.append(r)

# Construct the general solution symbolically
C = symbols('C1 C2 C3 C4')
general_solution = 0

# Add terms for real roots
for i, r in enumerate(real_roots):
    general_solution += C[i] * sp.exp(r * x)

# Add terms for complex roots
for i, r in enumerate(complex_roots, len(real_roots)):
    alpha = r.real
    beta = abs(r.imag)
    general_solution += sp.exp(alpha * x) * (C[i] * sp.cos(beta * x) + C[i+1] * sp.sin(beta * x))

# Display the general solution
print("\nGeneral Solution:")
sp.pprint(sp.Eq(y, general_solution))
