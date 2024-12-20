import math
def imp_euler(f,x,y,c,N,h=None,v = 0):
    h = h if h else (c - x) / N
    if v ==1: print(f"intial values, x = {x}, y = {y}")
    for i in range(N):
        F = f(x,y)
        G = f(x + h, (y + h * F))
        
        x = x + h
        y = y + h * (F + G)/2
        if v == 1: print(f"step {i + 1}, x = {x}, y = {y}")
    return y

def imp_euler_with_tolerance(f, x0, y0, c=None, tol=1e-6, max_iterations=100):
    """
    Perform the implicit Euler method with adaptive step size to solve an ODE with a given tolerance.
    Parameters:
    f (function): The function defining the differential equation dy/dx = f(x, y).
    x0 (float): The initial value of x.
    y0 (float): The initial value of y.
    c (optional): Additional parameters to pass to the function f.
    tol (float, optional): The tolerance for the error estimate. Default is 1e-6.
    max_iterations (int, optional): The maximum number of iterations to perform. Default is 100.
    Returns:
    float: The estimated value of y at the final step that meets the tolerance criteria.
    Prints:
    Iteration details including the current number of steps (N), the new and previous y values, and the error estimate.
    """
    print(f"Initial values, x = {x0}, y = {y0}")
    
    # Start with N=1
    N = 1
    y_prev = imp_euler(f, x0, y0, c, N)
    
    for m in range(1, max_iterations + 1):
        N *= 2  # Double the number of steps
        y_new = imp_euler(f, x0, y0, c, N)
        
        # Estimate the error
        error = abs(y_new - y_prev)
        print(f"Iteration {m}: N = {N}, y_new = {y_new}, y_prev = {y_prev}, error = {error}")
        
        if error < tol:
            print(f"Tolerance reached, y = {y_new}")
            return y_new
        y_prev = y_new
    
    print(f"Max number of iterations reached, returning last value, y = {y_new}")
    return y_new
import numpy as np

def max_value_in_range(f, x0, y0, a, b, step=0.001, N_steps=1000):
    """
    Finds the maximum y value obtained by Euler's method over the range [a, b].

    Parameters:
    - f: The function f(x, y) defining the differential equation dy/dx = f(x, y).
    - x0: Initial x-value.
    - y0: Initial y-value.
    - a: Start of the range for x.
    - b: End of the range for x.
    - step: Step size for generating x-values (default is 0.001).
    - N_steps: Number of steps to use in Euler's method (default is 1000).

    Returns:
    - A tuple (max_x, max_y) where max_y is the maximum y value found in the range,
      and max_x is the corresponding x value.
    """
    # Initialize maximum values
    max_x = None
    max_y = -np.inf  # Use negative infinity to handle negative y values

    # Generate x-values using NumPy's arange for efficiency
    # Adding step to b to include the endpoint if possible
    range_list = np.arange(a, b + step, step)

    for x in range_list:
        # Estimate y at current x using Improved Euler's method
        est = imp_euler(f, x0, y0, x, N_steps)
        
        # Update maximum y and corresponding x if a new maximum is found
        if est > max_y:
            max_y = est
            max_x = x

    return max_x, max_y

## given f, intial and a range find the value of x that results i specifies value y
def find_y(f, x0,y0,y,a,b,N=1000):
    for x in np.arange(a,b,0.0001):
        if abs(imp_euler(f,x0,y0,x,N) - y) < .0001:
            return x
    return None

   
print(find_y(lambda x,y: (x + y + 1)**2, 0,-1,0,0,1.4))

