{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from scipy.integrate import odeint\
import numpy as np\
import matplotlib.pyplot as plt\
\
# ODE model for memory persistence (fixed to interpolate stimulus)\
def model(x, t, k, t_array, s):\
    t_idx = np.interp(t, t_array, np.arange(len(t_array)))  # Interpolate time index\
    s_val = s[int(np.clip(t_idx, 0, len(s) - 1))]  # Safe index into s\
    return -k * x + s_val  # Return scalar derivative\
\
# Time array and stimuli\
t = np.linspace(0, 10, 1000)\
k = 0.1\
s_prime = 0.1 * np.sin(2 * np.pi * np.log(t + 1) / np.log(2))\
s_composite = 0.1 * np.sin(2 * np.pi * np.log(t + 1) / np.log(6))\
\
# Solve ODEs\
x_prime = odeint(model, [0], t, args=(k, t, s_prime))\
x_composite = odeint(model, [0], t, args=(k, t, s_composite))\
\
# Calculate forget rates (fixed indexing to match lengths)\
forget_rate_prime = np.mean(np.diff(x_prime[-101:, 0]) / x_prime[-102:-2, 0])  # 100 differences / 100 denominators\
forget_rate_composite = np.mean(np.diff(x_composite[-101:, 0]) / x_composite[-102:-2, 0])\
\
# Plot\
plt.plot(t, x_prime[:, 0], label=f'Prime Stimulus (Forget Rate: \{forget_rate_prime:.4f\})', color='blue')\
plt.plot(t, x_composite[:, 0], label=f'Composite Stimulus (Forget Rate: \{forget_rate_composite:.4f\})', color='red')\
plt.xlabel('Time')\
plt.ylabel('State Value')\
plt.title('Memory Persistence: Prime vs. Composite Stimuli (3.97\'d7)')\
plt.legend()\
plt.grid(True)\
plt.savefig('memory_persistence_plot.png', dpi=300, bbox_inches='tight')\
plt.close()\
\
print(f"Forget rate (prime): \{forget_rate_prime:.4f\}; (composite): \{forget_rate_composite:.4f\}")}