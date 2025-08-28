import matplotlib.pyplot as plt
import numpy as np

# Data from table
n_values = [2, 3, 4, 5, 6]
delta_e = [45.26, 17.88, 8.49, 4.63, 2.79]
rounded = [45, 18, 8, 5, 3]
primes = ['3²×5', '2×3²', '2³', '5', '3']

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(n_values, delta_e, marker='o', label='Actual ΔE (μeV)', color='blue')
ax.plot(n_values, rounded, marker='x', label='Rounded', color='red', linestyle='--')

# Annotations
for i, (n, val, rnd, pr) in enumerate(zip(n_values, delta_e, rounded, primes)):
    ax.text(n + 0.1, val, f'{val:.2f} → {rnd} ({pr})', fontsize=10)

ax.set_xlabel('Principal Quantum Number n')
ax.set_ylabel('Fine-Structure Splitting ΔE (μeV)')
ax.set_title('Harmonic Cascade in Hydrogen Fine-Structure Splitting')
ax.legend()
ax.grid(True)

# Save for embed
plt.savefig('harmonic_cascade_figure.png')
plt.show()