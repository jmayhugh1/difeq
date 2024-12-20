import numpy as np
import matplotlib.pyplot as plt

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
    xs, ys: Lists of x and y values
    """
    xs = [x0]
    ys = [y0]
    
    for _ in range(steps):
        xi = xs[-1]
        yi = ys[-1]
        
        k1 = h * f(xi, yi)
        k2 = h * f(xi + h/2, yi + k1/2)
        k3 = h * f(xi + h/2, yi + k2/2)
        k4 = h * f(xi + h, yi + k3)
        
        y_next = yi + (k1 + 2*k2 + 2*k3 + k4)/6
        x_next = xi + h
        
        xs.append(x_next)
        ys.append(y_next)
        
    return xs, ys

def f(x, y):
    """
    Defines the ODE y' = cos(5y) - x
    """
    return np.cos(5*y) - x

def find_max(xs, ys):
    """
    Finds the maximum y value and its corresponding x value.
    
    Parameters:
    xs : List of x values
    ys : List of y values
    
    Returns:
    max_y : The maximum y value
    max_x : The x value at which the maximum y occurs
    """
    max_y = max(ys)
    max_index = ys.index(max_y)
    max_x = xs[max_index]
    return max_y, max_x

def main():
    # Initial conditions
    x0 = 0
    y0 = 7
    h = 0.4
    x_end = 12
    steps = int((x_end - x0)/h)
    
    # Perform RK4
    xs, ys = rk4(f, x0, y0, h, steps)
    
    # Find maximum y and its location
    max_y, max_x = find_max(xs, ys)
    
    # Display the results
    print("Approximate Solution using RK4:")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.1f}, y = {yi:.6f}")
    
    print(f"\nMaximum value of y over [0, 12]: {max_y:.6f}")
    print(f"Occurs at x = {max_x:.1f}")
    
    # Plot the solution
    plt.figure(figsize=(12, 6))
    plt.plot(xs, ys, 'bo-', label='RK4 Approximation')
    plt.plot(max_x, max_y, 'ro', label='Maximum y')
    plt.title("Solution of the IVP using Fourth-Order Runge-Kutta Method")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
