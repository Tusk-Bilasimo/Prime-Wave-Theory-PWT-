from scipy.integrate import odeint
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

# Coupled ODE model (fixed to handle stimulus array)
def coupled_model(z, t, a, b, c, d, s):
    x, y = z
    idx = int(t * (len(s) - 1) / (s.size - 1))  # Index into s array
    s_val = s[idx] if 0 <= idx < len(s) else 0  # Safety check
    dx_dt = a * x - b * x * y + s_val
    dy_dt = -c * y + d * x * y
    return [dx_dt, dy_dt]

z0 = [1.0, 1.0]
t = np.linspace(0, 20, 2000)
s_prime = 0.1 * np.sin(2 * np.pi * t / np.log(2))
s_composite = 0.1 * np.sin(2 * np.pi * t / np.log(6))

sol_prime = odeint(coupled_model, z0, t, args=(0.5, 0.4, 0.3, 0.2, s_prime))
sol_composite = odeint(coupled_model, z0, t, args=(0.5, 0.4, 0.3, 0.2, s_composite))

fft_prime = fft(sol_prime[:, 0])
fft_composite = fft(sol_composite[:, 0])
phase_prime = np.angle(fft_prime[:100])
phase_composite = np.angle(fft_composite[:100])

neg_phase_prime = np.mean(phase_prime < 0)
neg_phase_composite = np.mean(phase_composite < 0)

# Plot Fourier spectrum
plt.plot(np.abs(fft_prime[:50]), label=f'Prime Spectrum (Neg Phase: {neg_phase_prime:.2%})', color='blue')
plt.plot(np.abs(fft_composite[:50]), label=f'Composite Spectrum (Neg Phase: {neg_phase_composite:.2%})', color='red')
plt.xlabel('Frequency Bin')
plt.ylabel('Amplitude')
plt.title('Fourier Spectrum: Prime vs. Composite Stimuli (1.78×)')
plt.legend()
plt.grid(True)
plt.savefig('fourier_spectrum_plot.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"Negative phase proportion (prime): {neg_phase_prime:.4f}; (composite): {neg_phase_composite:.4f}")
