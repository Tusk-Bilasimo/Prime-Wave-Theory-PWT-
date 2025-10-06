{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab709
\pard\pardeftab709\partightenfactor0

\f0\fs24 \cf0 # Prime Wave Theory (PWT) Model Implementation\
# This script implements the refined damped model developed in our explorations.\
# It includes functions for symbolic and numerical fits, prime factorization checks,\
# and examples from atomic spectra, redshifts, particle masses, and the sterile neutrino prediction.\
# Dependencies: sympy, numpy, scipy.optimize (for curve_fit)\
# Author: Grok (built by xAI), based on collaborative discussions\
# License: MIT - Feel free to use, modify, and share.\
\
import sympy as sp\
import numpy as np\
from scipy.optimize import curve_fit\
from sympy import prime, primorial, log\
\
# Helper Functions\
\
def get_prime(n):\
    """Return the nth prime using sympy."""\
    return prime(n)\
\
def get_primorial(k):\
    """Return the primorial of k (product of first k primes)."""\
    return primorial(k)\
\
def factor_integer(number):\
    """Factor an integer using sympy and return prime factors."""\
    return sp.factorint(number)\
\
# Refined Damped Model\
def pwt_damped_model(n, a, b, c, m_shift=1, use_137=True):\
    """\
    Refined PWT model: r(n) \uc0\u8776  a / p(n) + b * log(primorial(m)) / denom + c * log(primorial(m)) / (p(n) * denom)\
    where m = n + m_shift, denom = 137 if use_137 else 1.\
    """\
    p_n = get_prime(n)\
    m = n + m_shift\
    prim_m = get_primorial(m)\
    log_prim = log(prim_m)\
    denom = 137 if use_137 else 1\
    return a / p_n + (b * log_prim) / denom + (c * log_prim) / (p_n * denom)\
\
# Numerical Fit Function\
def fit_pwt_model(data, use_137=True, m_shift=1):\
    """\
    Numerically fit the model to data using curve_fit.\
    data: list of r values for n=1 to len(data)\
    Returns fitted params a, b, c and predictions.\
    """\
    n_vals = np.arange(1, len(data) + 1)\
    def model_func(n, a, b, c):\
        return pwt_damped_model(n, a, b, c, m_shift, use_137)\
    \
    popt, _ = curve_fit(model_func, n_vals, data, p0=[1, 1, 1])\
    predictions = model_func(n_vals, *popt)\
    return popt, predictions\
\
# Symbolic Fit Example (for small datasets)\
def symbolic_fit_example(data):\
    """Symbolic solve for a, b, c on 3 points (exact fit)."""\
    n = sp.symbols('n')\
    a, b, c = sp.symbols('a b c')\
    eqs = []\
    for i in range(len(data)):\
        eq = pwt_damped_model(i+1, a, b, c) - data[i]\
        eqs.append(eq)\
    solution = sp.solve(eqs[:3], (a, b, c))  # Solve for first 3\
    return solution\
\
# Example Tests\
\
# 1. Hydrogen Fine-Structure Splits (MHz)\
hydrogen_data = [1276, 3242, 6425]  # From H-alpha components\
popt_h, pred_h = fit_pwt_model(hydrogen_data)\
print("Hydrogen Fit Params (a, b, c):", popt_h)\
print("Predictions:", pred_h)\
# Factor check\
print("Factors of 6425:", factor_integer(6425))  # \{5: 2, 257: 1\}\
\
# 2. Lithium Fine-Structure Splits (MHz)\
lithium_data = [10053, 456, 8]  # 2P, 4D, 10P approx\
popt_li, pred_li = fit_pwt_model(lithium_data)\
print("Lithium Fit Params (a, b, c):", popt_li)\
print("Predictions:", pred_li)\
print("Factors of 10053:", factor_integer(10053))  # \{3: 2, 1117: 1\}\
\
# 3. Mercury Fine-Structure Splits (MHz)\
mercury_data = [52990, 138850]  # 6s6p ^3P splits\
popt_hg, pred_hg = fit_pwt_model(mercury_data)\
print("Mercury Fit Params (a, b, c):", popt_hg)\
print("Predictions:", pred_hg)\
print("Factors of 52990:", factor_integer(52990))  # \{2: 1, 5: 1, 7: 1, 757: 1\}\
\
# 4. Gravitational Redshifts (z values, first 5 for fit)\
redshift_data = [2.12e-6, 7e-5, 1.015e-4, 2.68e-4, 6.67e-4, 0.16, 0.205, 0.22, 0.34, 0.35]\
popt_red, pred_red = fit_pwt_model(redshift_data[:5])\
print("Redshift Fit Params (a, b, c):", popt_red)\
print("Predictions for last 5:", popt_red_model(np.arange(6,11), *popt_red))  # Define pwt_red_model similar to above\
\
# 5. Sterile Neutrino Prediction Tie-In (Mass 7000 eV)\
sterile_mass = 7000\
print("Factors of 7000:", factor_integer(7000))  # \{2: 3, 5: 3, 7: 1\}\
# Proximity to primorial zone\
prim5 = get_primorial(5)  # 2310\
prim6 = get_primorial(6)  # 30030\
print(f"7000 in [2310, 30030]? \{2310 < 7000 < 30030\}")\
\
# Run symbolic example for hydrogen\
sym_sol_h = symbolic_fit_example(hydrogen_data)\
print("Symbolic Solution for Hydrogen:", sym_sol_h)\
\
# To extend, add your own data lists and call fit_pwt_model}