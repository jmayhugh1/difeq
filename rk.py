def rk4(f, x0, y0, h, steps):
    """
    Fourth-order Runge-Kutta method.

    Parameters:
    f     : Function representing the ODE y' = f(x, y)
    x0    : Initial x value
    y0    : Initial y value
    h     : Step size
    steps : Number of steps to take

    Returns:
    (x, y): Tuple containing lists of x and y values
    """
    x = x0
    y = y0
    xs = [x]
    ys = [y]
    
    for _ in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        
        xs.append(x)
        ys.append(y)
        
    return xs, ys

# Define the ODE
def f(x, y):
    return x + 3 - y

# Initial conditions
x0 = 0
y0 = 12
h = 0.4
x_target = 0
steps = int((x_target - x0) / h)

# Perform RK4
xs, ys = rk4(f, x0, y0, h, steps)

# Extract the value at x = 1
phi_K_1 = ys[-1]

print(f"Approximation using RK4 at x = {x_target}: phi_K(1) = {phi_K_1:.6f}")
