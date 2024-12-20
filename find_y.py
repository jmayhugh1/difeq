from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Define the ODE
def dy_dx(x, y):
    return (x + y + 1)**2

# Initial conditions
x0 = 0
y0 = -1

# Define the target range
a = 0
b = 1.4
target_y = 0    
# Solve the ODE
sol = solve_ivp(dy_dx, [a, b], [y0], method='RK45', dense_output=True)

# Extract the solution
x_vals = np.linspace(a, b, 1000)
y_vals = sol.sol(x_vals)[0]

# Plot the solution
plt.plot(x_vals, y_vals, label='Numerical Solution (RK45)')
plt.axhline(y=0, color='r', linestyle='--', label='y = 0')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution of dy/dx = (x + y + 1)^2 with y(0) = -1')
plt.legend()
plt.grid(True)
plt.show()

# Find the x where y crosses 0
# Using interpolation
from scipy.interpolate import interp1d

f_interp = interp1d(y_vals, x_vals, kind='linear', fill_value="extrapolate")
x_target = f_interp(target_y)
print(f"The value of x where y(x) ≈ {target_y} is approximately x = {x_target:.4f}")
