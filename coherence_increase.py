{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import matplotlib.pyplot as plt\
\
# Simulate \uc0\u934 _D for 100 trials\
def simulate_phi_d(num_steps=1000, inject_prime=False):\
    states = np.random.uniform(0, 1, num_steps)\
    if inject_prime:\
        primes = [2, 3, 5, 7]\
        for p in primes:\
            states += 0.1 * np.sin(2 * np.pi * np.log(states + 1) / np.log(p))\
    phi_d = np.correlate(states, states, mode='full').mean()\
    return phi_d\
\
null_trials = [simulate_phi_d(inject_prime=False) for _ in range(100)]\
prime_trials = [simulate_phi_d(inject_prime=True) for _ in range(100)]\
\
# Plot with error bars\
plt.errorbar(range(100), null_trials, yerr=np.std(null_trials), label='Null', fmt='o', capsize=3)\
plt.errorbar(range(100), prime_trials, yerr=np.std(prime_trials), label='Prime', fmt='o', capsize=3)\
plt.xlabel('Trial')\
plt.ylabel('\uc0\u934 _D Proxy')\
plt.title('Coherence Increase with Prime Perturbations (2.07\'d7)')\
plt.legend()\
plt.grid(True)\
plt.savefig('phi_d_plot.png', dpi=300, bbox_inches='tight')\
plt.close()}