import sympy as sp

# Define the variable and function
x = sp.symbols('x')
y = sp.Function('y')

# Define the nonhomogeneous term
g = sp.exp(-6 * x)

# Define the homogeneous differential equation y''' + 9 y'' - 108 y = 0
# We'll find the complementary (homogeneous) solution first

# Define the characteristic equation
r = sp.symbols('r')
char_eq = sp.Eq(r**3 + 9*r**2 - 108, 0)

# Solve the characteristic equation for roots
roots = sp.solve(char_eq, r)
print("Roots of the characteristic equation:", roots)

# Based on the roots, define the homogeneous solutions
# Assume roots are distinct or repeated as necessary
# For example purposes, let's compute them symbolically

# Find numerical roots for clarity (if necessary)
# If roots are not easily factorizable, SymPy will keep them symbolic
# For this example, one real root and a double real root
# Let's factor the equation if possible

# Factor the characteristic equation
factored_eq = sp.factor(r**3 + 9*r**2 - 108)
print("Factored characteristic equation:", factored_eq)

# From factoring, we find that r = 3 is a root
# Perform polynomial division or use SymPy to factor further
# r = 3 is a root, so divide the polynomial by (r - 3)
divided_poly = sp.div(r**3 + 9*r**2 - 108, (r - 3))
print("Division result:", divided_poly)

# The characteristic equation factors as (r - 3)(r^2 + 12r + 36) = 0
# Solve r^2 + 12r + 36 = 0 for the remaining roots
remaining_roots = sp.solve(r**2 + 12*r + 36, r)
print("Remaining roots:", remaining_roots)

# Thus, the roots are r = 3, r = -6 (double root)
# Define homogeneous solutions accordingly
y1 = sp.exp(3 * x)
y2 = sp.exp(-6 * x)
y3 = x * sp.exp(-6 * x)  # Multiply by x for the repeated root

# Display homogeneous solutions
print("Homogeneous Solutions:")
print("y1 =", y1)
print("y2 =", y2)
print("y3 =", y3)

# Form the Wronskian matrix
Wronskian_matrix = sp.Matrix([
    [y1, y2, y3],
    [y1.diff(x), y2.diff(x), y3.diff(x)],
    [y1.diff(x, 2), y2.diff(x, 2), y3.diff(x, 2)]
])

# Compute the Wronskian determinant
W = Wronskian_matrix.det()
print("\nWronskian (W):")
sp.pprint(W)

# Now, set up the system for u1', u2', u3' using Variation of Parameters
# The system is:
# y1*u1' + y2*u2' + y3*u3' = 0
# y1'*u1' + y2'*u2' + y3'*u3' = 0
# y1''*u1' + y2''*u2' + y3''*u3' = g(x)

# Create the matrix of coefficients
coeff_matrix = Wronskian_matrix

# Create the right-hand side vector
# The first two equations are zero, and the third is g(x)
rhs = sp.Matrix([0, 0, g])

# Compute the determinants for u1', u2', u3' using Cramer's Rule
# Replace each column with the RHS vector in turn

# For u1'
Wronskian_u1 = Wronskian_matrix.copy()
Wronskian_u1[:, 0] = rhs
W1 = Wronskian_u1.det()

# For u2'
Wronskian_u2 = Wronskian_matrix.copy()
Wronskian_u2[:, 1] = rhs
W2 = Wronskian_u2.det()

# For u3'
Wronskian_u3 = Wronskian_matrix.copy()
Wronskian_u3[:, 2] = rhs
W3 = Wronskian_u3.det()

# Compute u1', u2', u3'
u1_prime = W1 / W
u2_prime = W2 / W
u3_prime = W3 / W

print("\nu1' =", u1_prime)
print("u2' =", u2_prime)
print("u3' =", u3_prime)

# Integrate to find u1, u2, u3
u1 = sp.integrate(u1_prime, x)
u2 = sp.integrate(u2_prime, x)
u3 = sp.integrate(u3_prime, x)

print("\nu1 =", u1)
print("u2 =", u2)
print("u3 =", u3)

# The particular solution y_p is given by:
# y_p = u1*y1 + u2*y2 + u3*y3
y_p = u1 * y1 + u2 * y2 + u3 * y3

# Simplify the particular solution
y_p = sp.simplify(y_p)

print("\nThe particular solution y_p(x) is:")
sp.pprint(y_p)
