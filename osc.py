import numpy as np
import matplotlib.pyplot as plt

def compute_coefficients(m, b, k, Omega):
    """
    Compute the coefficients A and B for the synchronous solution.
    
    Parameters:
    m     : Mass (constant)
    b     : Damping coefficient
    k     : Spring constant
    Omega : Driving frequency (array)
    
    Returns:
    A     : Coefficient for cosine term (array)
    B     : Coefficient for sine term (array)
    """
    denominator = b**2 * Omega**2 + (k - m * Omega**2)**2
    A = (k - m * Omega**2) / denominator
    B = (b * Omega) / denominator
    return A, B

def main():
    # Parameters
    m = 1       # Mass
    b1 = 0.1    # Damping coefficient for Case 1
    b2 = 0      # Damping coefficient for Case 2 (Undamped)
    k = 25      # Spring constant
    Omega = np.linspace(4, 6, 400)  # Driving frequency from 4 to 6 with fine resolution

    # Compute coefficients for both cases
    A1, B1 = compute_coefficients(m, b1, k, Omega)
    A2, B2 = compute_coefficients(m, b2, k, Omega)

    # Plot 1: Damped Case (b=0.1)
    plt.figure(figsize=(12, 6))
    plt.plot(Omega, A1, label='A(Ω)', color='blue')
    plt.plot(Omega, B1, label='B(Ω)', color='green')
    plt.axvline(x=5, color='red', linestyle='--', label='Resonance at Ω=5')
    plt.title('Coefficients A and B vs. Driving Frequency Ω (Damped)')
    plt.xlabel('Driving Frequency Ω')
    plt.ylabel('Coefficient Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-1.5, 2.5)  # Based on the provided graph options
    plt.xlim(4, 6)
    plt.show()

    # Plot 2: Undamped Case (b=0)
    plt.figure(figsize=(12, 6))
    plt.plot(Omega, A2, label='A(Ω)', color='blue')
    plt.plot(Omega, B2, label='B(Ω)', color='green')
    plt.axvline(x=5, color='red', linestyle='--', label='Resonance at Ω=5')
    plt.title('Coefficients A and B vs. Driving Frequency Ω (Undamped)')
    plt.xlabel('Driving Frequency Ω')
    plt.ylabel('Coefficient Value')
    plt.legend()
    plt.grid(True)
    plt.ylim(-3, 3)  # Adjusted to visualize blow-up at resonance
    plt.xlim(4, 6)
    plt.show()

if __name__ == "__main__":
    main()
