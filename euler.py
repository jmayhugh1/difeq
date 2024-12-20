def dTdt(T, M=292, K=0.04):
    # Differential equation: dT/dt = K(M - T)
    return K * (M - T)

# Parameters
h = 0.1    # step size in minutes
T0 = 364   # initial temperature at t=0
end_time_1 = 30.0
end_time_2 = 60.0

# Function to approximate T(end_time) using Euler's method
def euler_method(T_initial, h, end_time):
    # Number of steps to reach end_time
    steps = int(end_time / h)
    T = T_initial
    t = 0.0
    for _ in range(steps):
        slope = dTdt(T)
        T = T + h * slope
        t += h
    return T

# Compute T(30)
T_30 = euler_method(T0, h, end_time_1)
# Compute T(60)
T_60 = euler_method(T0, h, end_time_2)

print(f"Approximate temperature after 30 minutes: {T_30:.2f} K")
print(f"Approximate temperature after 60 minutes: {T_60:.2f} K")
