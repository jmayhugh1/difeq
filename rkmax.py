import numpy as np
import matplotlib.pyplot as plt

def rk4(f, x0, y0, h, x_end):
    """
    Implements the Fourth-Order Runge-Kutta (RK4) method for solving ODEs.
    
    Parameters:
    f      : Function representing the ODE y' = f(x, y)
    x0     : Initial x value
    y0     : Initial y value
    h      : Step size
    x_end  : The value of x at which to stop the integration
    
    Returns:
    xs     : Array of x values
    ys     : Array of y values corresponding to xs
    """
    # Calculate the number of steps
    N = int(np.ceil((x_end - x0) / h))
    
    # Initialize arrays to store x and y values
    xs = np.zeros(N + 1)
    ys = np.zeros(N + 1)
    
    # Set initial conditions
    xs[0] = x0
    ys[0] = y0
    
    # Iterate using RK4
    for i in range(N):
        xi = xs[i]
        yi = ys[i]
        
        # Compute RK4 coefficients
        k1 = h * f(xi, yi)
        k2 = h * f(xi + h/2, yi + k1/2)
        k3 = h * f(xi + h/2, yi + k2/2)
        k4 = h * f(xi + h, yi + k3)
        
        # Update y
        yi_next = yi + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        # Update x
        xi_next = xi + h
        
        # Store the next values
        xs[i + 1] = xi_next
        ys[i + 1] = yi_next
        
    return xs, ys

def f(x, y):
    """
    Defines the ODE y' = f(x, y) = 1.8 / x^4 - y^2
    """
    return (1.8 / x**4) - y**2

def find_max(xs, ys):
    """
    Finds the maximum y value and its corresponding x value.
    
    Parameters:
    xs : Array of x values
    ys : Array of y values
    
    Returns:
    max_y : The maximum y value
    max_x : The x value at which the maximum y occurs
    """
    max_index = np.argmax(ys)
    max_y = ys[max_index]
    max_x = xs[max_index]
    return max_y, max_x

def main():
    # Initial conditions
    x0 = 0.5
    y0 = -1
    h = 0.01  # Step size
    x_end = 1.5  # End of interval
    
    # Perform RK4
    xs, ys = rk4(f, x0, y0, h, x_end)
    
    # Find maximum y and its location
    max_y, max_x = find_max(xs, ys)
    
    # Display the results
    print("Approximate Solution using RK4:")
    for xi, yi in zip(xs, ys):
        print(f"x = {xi:.2f}, y = {yi:.6f}")
    
    print(f"\nMaximum value of y over [0.5, 1.5]: {max_y:.6f}")
    print(f"Occurs at x = {max_x:.2f}")
    
    # (Optional) Plot the solution
    plt.figure(figsize=(10, 6))
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
