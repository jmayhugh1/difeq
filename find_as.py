import numpy as np

def improved_euler(f, x0, y0, h):
    """
    Performs one step of the Improved Euler (Heun's) method.

    Parameters:
    - f: Function defining dy/dx = f(x, y)
    - x0: Current x value
    - y0: Current y value
    - h: Step size

    Returns:
    - y_next: Approximated y value after step h
    """
    F = f(x0, y0)
    G = f(x0 + h, y0 + h * F)
    y_next = y0 + (h / 2) * (F + G)
    return y_next

def find_vertical_asymptote(f, x0, y0, a, b, h=0.01, threshold=1e6, precision=0.01):
    """
    Uses Improved Euler's method to find the x value where y becomes very large,
    indicating a vertical asymptote.

    Parameters:
    - f: Function defining dy/dx = f(x, y)
    - x0: Initial x value
    - y0: Initial y value
    - a: Start of the interval
    - b: End of the interval
    - h: Step size
    - threshold: y value to consider as 'infinite' for asymptote detection
    - precision: Desired precision for x (e.g., 0.01 for two decimal places)

    Returns:
    - asymptote_x: x value where vertical asymptote occurs (rounded to two decimals)
    - steps: Number of steps taken to reach the asymptote
    """
    x = a
    y = y0
    steps = 0
    asymptote_x = None

    while x < b:
        y_next = improved_euler(f, x, y, h)
        x_next = x + h
        steps += 1

        if y_next > threshold:
            # Asymptote is between x and x_next
            # Refine within this interval
            lower = x
            upper = x_next
            refined_h = precision / 100  # Start with finer steps
            refined_x = lower
            refined_y = y

            while refined_x < upper:
                refined_y_next = improved_euler(f, refined_x, refined_y, refined_h)
                refined_x_new = refined_x + refined_h

                if refined_y_next > threshold:
                    asymptote_x = round(refined_x_new, 2)
                    return asymptote_x, steps
                refined_x = refined_x_new
                refined_y = refined_y_next

            # If not found in refined steps
            asymptote_x = round(upper, 2)
            return asymptote_x, steps

        y = y_next
        x = x_next

    return asymptote_x, steps

# Define the differential equation dy/dx = x^3 y^2 - y/x
def f(x, y):
    return x**3 * y**2 - y / x

# Initial conditions
x0 = 0.9
y0 = 3.2

# Range to search for asymptote
a = 0.9
b = 1.5

# Step size
h = 0.01

# Threshold to detect vertical asymptote
threshold = 1e6

# Desired precision for x
precision = 0.01  # Two decimal places

# Find the vertical asymptote
asymptote_x, steps = find_vertical_asymptote(f, x0, y0, a, b, h, threshold, precision)

if asymptote_x:
    print(f"Vertical asymptote detected at x = {asymptote_x}")
    print(f"Number of steps taken: {steps}")
else:
    print("No vertical asymptote detected within the interval [0.9, 1.5].")
