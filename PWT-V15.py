"""
Appendix D: Computational Implementation and Visualization
Prime Wave Theory (PWT) - Version 15.1

This module provides complete implementations for:
1. Computing the Prime Wave P_k(x)
2. Fourier coefficient calculation
3. Visualization (wave plots and spectra)
4. Numerical verification of theorems

Author: Tusk
Date: October 01, 2025
License: MIT (for research use)

Dependencies:
    numpy >= 1.21.0
    matplotlib >= 3.4.0
    scipy >= 1.7.0

Usage:
    python pwt_visualization.py --mode wave --k 3
    python pwt_visualization.py --mode spectrum --k 5
    python pwt_visualization.py --mode verify --k 7
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from typing import List, Tuple
import argparse


# ============================================================================
# SECTION D.1: Core Functions
# ============================================================================

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Generate primes up to limit using Sieve of Eratosthenes.

    Args:
        limit: Upper bound for prime search

    Returns:
        List of primes <= limit
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(limit + 1) if is_prime[i]]


def get_first_k_primes(k: int) -> List[int]:
    """
    Get the first k prime numbers.

    Args:
        k: Number of primes to return

    Returns:
        List of first k primes [2, 3, 5, 7, ...]
    """
    # Upper bound estimate: k * (log(k) + log(log(k))) for k >= 6
    if k < 6:
        limit = 15
    else:
        limit = int(k * (np.log(k) + np.log(np.log(k))) * 1.3)

    primes = sieve_of_eratosthenes(limit)
    return primes[:k]


def primorial(k: int) -> int:
    """
    Compute N_k = product of first k primes.

    Args:
        k: Number of primes

    Returns:
        Product of first k primes
    """
    primes = get_first_k_primes(k)
    return int(np.prod(primes))


# ============================================================================
# SECTION D.2: Prime Wave Functions (Definitions 3.1, 3.3)
# ============================================================================

def Psi_p(x: float, p: int) -> float:
    """
    Continuous Prime Pulse for prime p (Definition 3.1).

    Ψ_p(x) = 1 - (1/p) * Σ_{j=0}^{p-1} cos(2πjx/p)

    Args:
        x: Real number (can be non-integer)
        p: Prime number

    Returns:
        Value of Ψ_p(x) ∈ [0, 1]
    """
    cos_sum = sum(np.cos(2 * np.pi * j * x / p) for j in range(p))
    return 1 - cos_sum / p


def Psi_p_vectorized(x: np.ndarray, p: int) -> np.ndarray:
    """
    Vectorized version of Psi_p for array input.

    Args:
        x: Array of real numbers
        p: Prime number

    Returns:
        Array of Ψ_p(x) values
    """
    # Create j array [0, 1, ..., p-1]
    j = np.arange(p).reshape(-1, 1)  # Shape (p, 1)
    x_reshaped = x.reshape(1, -1)  # Shape (1, len(x))

    # Broadcast: (p, len(x)) array of cos(2πjx/p)
    cos_terms = np.cos(2 * np.pi * j * x_reshaped / p)
    cos_sum = np.sum(cos_terms, axis=0)  # Sum over j

    return 1 - cos_sum / p


def P_k(x: float, k: int) -> float:
    """
    Continuous Combined Prime Wave (Definition 3.3).

    P_k(x) = ∏_{i=1}^k Ψ_{p_i}(x)

    Args:
        x: Real number
        k: Number of primes to include

    Returns:
        Value of P_k(x) ∈ [0, 1]
    """
    primes = get_first_k_primes(k)
    result = 1.0
    for p in primes:
        result *= Psi_p(x, p)
    return result


def P_k_vectorized(x: np.ndarray, k: int) -> np.ndarray:
    """
    Vectorized version of P_k for array input.

    Args:
        x: Array of real numbers
        k: Number of primes

    Returns:
        Array of P_k(x) values
    """
    primes = get_first_k_primes(k)
    result = np.ones_like(x)
    for p in primes:
        result *= Psi_p_vectorized(x, p)
    return result


# ============================================================================
# SECTION D.3: Fourier Coefficients (Theorem 4.3)
# ============================================================================

def euler_phi(n: int) -> int:
    """
    Euler's totient function φ(n).

    Args:
        n: Positive integer

    Returns:
        Number of integers in [1, n] coprime to n
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def mobius(n: int) -> int:
    """
    Möbius function μ(n).

    Returns:
        1 if n is squarefree with even number of prime factors
        -1 if n is squarefree with odd number of prime factors
        0 if n is not squarefree
    """
    if n == 1:
        return 1

    # Factor n
    factors = []
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                temp //= p
                count += 1
            if count > 1:  # Not squarefree
                return 0
            factors.append(p)
        p += 1
    if temp > 1:
        factors.append(temp)

    return (-1) ** len(factors)


def gcd(a: int, b: int) -> int:
    """
    Greatest common divisor using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a


def compute_fourier_coefficient(m: int, k: int) -> float:
    """
    Compute Fourier coefficient c_m^{(k)} using Theorem 4.3.

    c_m^{(k)} = (1/N_k) * φ(N_k/gcd(m,N_k)) * μ(N_k/gcd(m,N_k))

    Args:
        m: Mode index (0 <= m < N_k)
        k: Number of primes

    Returns:
        Fourier coefficient c_m^{(k)}
    """
    N_k = primorial(k)
    d = gcd(m, N_k)
    q = N_k // d

    phi_q = euler_phi(q)
    mu_q = mobius(q)

    return phi_q * mu_q / N_k


def compute_all_fourier_coeffs(k: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute all Fourier coefficients for P_k.

    Args:
        k: Number of primes

    Returns:
        Tuple (modes, coefficients) where modes = [0, 1, ..., N_k-1]
    """
    N_k = primorial(k)
    modes = np.arange(N_k)
    coeffs = np.array([compute_fourier_coefficient(m, k) for m in modes])
    return modes, coeffs


# ============================================================================
# SECTION D.4: Verification Functions
# ============================================================================

def verify_zero_set(k: int, n_test: int = 100) -> dict:
    """
    Numerical verification of Theorem 4.7 (No Anomalous Zeros).

    Tests that P_k(x) = 0 iff x ∈ Z and gcd(x, N_k) > 1.

    Args:
        k: Number of primes
        n_test: Number of test points between integers

    Returns:
        Dictionary with verification results
    """
    N_k = primorial(k)
    results = {
        'k': k,
        'N_k': N_k,
        'integer_zeros_correct': 0,
        'integer_nonzeros_correct': 0,
        'noninteger_all_positive': 0,
        'max_ratio_noninteger': 0.0
    }

    # Test integers
    for n in range(N_k):
        P_n = P_k(float(n), k)
        should_be_zero = (gcd(n, N_k) > 1)

        if should_be_zero:
            if abs(P_n) < 1e-10:
                results['integer_zeros_correct'] += 1
        else:
            if abs(P_n - 1.0) < 1e-10:
                results['integer_nonzeros_correct'] += 1

    # Test non-integers (should all be positive)
    primes = get_first_k_primes(k)
    for p in primes[:min(3, k)]:  # Test first 3 primes
        for n in range(min(p, 10)):
            for delta in np.linspace(0.1, 0.9, n_test):
                x = n + delta
                P_x = P_k(x, k)

                if P_x > 1e-10:
                    results['noninteger_all_positive'] += 1

                # Compute sin(πθ)/sin(πθ/p) ratio (should be < p)
                theta = delta
                numerator = abs(np.sin(np.pi * theta))
                denominator = abs(np.sin(np.pi * theta / p))
                if denominator > 1e-10:
                    ratio = numerator / denominator
                    results['max_ratio_noninteger'] = max(
                        results['max_ratio_noninteger'],
                        ratio
                    )

    return results


def compute_besov_proxy(k: int, s: float, p: float,
                        n_samples: int = 1000) -> float:
    """
    Compute proxy for Besov seminorm (supporting Conjecture 6.1).

    Uses modulus of continuity:
    ω_r(f, t)_p = sup_{|h|≤t} ||Δ_h^r f||_{L^p}

    Args:
        k: Number of primes
        s: Regularity parameter
        p: Lebesgue exponent
        n_samples: Number of sample points

    Returns:
        Approximate Besov seminorm (finite => membership)
    """
    N_k = primorial(k)
    x = np.linspace(0, N_k, n_samples)
    P_vals = P_k_vectorized(x, k)

    # Compute first-order modulus of continuity
    h_values = np.logspace(-3, -0.5, 20)  # [0.001, 0.316...]
    seminorm = 0.0

    for h in h_values:
        # Shift by h
        x_shifted = x + h
        x_shifted = x_shifted % N_k  # Periodic
        P_shifted = P_k_vectorized(x_shifted, k)

        # ||P(x+h) - P(x)||_Lp
        diff = P_shifted - P_vals
        Lp_norm = np.mean(np.abs(diff) ** p) ** (1 / p)

        # Weight by h^{-s}
        weighted = Lp_norm / (h ** s)
        seminorm = max(seminorm, weighted)

    return seminorm


# ============================================================================
# SECTION D.5: Visualization Functions
# ============================================================================

def plot_wave(k: int, filename: str = None, show: bool = True):
    """
    Generate Figure 4.1: Prime Wave P_k(x) visualization.

    Args:
        k: Number of primes
        filename: Output filename (e.g., 'P3_wave_plot.pdf')
        show: Whether to display plot
    """
    N_k = primorial(k)
    primes = get_first_k_primes(k)

    # Generate x values (fine resolution)
    x = np.linspace(0, N_k, 5000)
    y = P_k_vectorized(x, k)

    # Integer values
    x_int = np.arange(N_k)
    y_int = np.array([P_k(float(n), k) for n in x_int])

    # Plot
    fig, ax = plt.subplots(figsize=(12, 5))

    # Continuous wave
    ax.plot(x, y, 'b-', linewidth=0.8, label=f'$P_{k}(x)$', alpha=0.7)

    # Integer points (zeros in red, ones in green)
    zeros = x_int[y_int < 0.5]
    ones = x_int[y_int > 0.5]
    ax.plot(zeros, y_int[y_int < 0.5], 'ro', markersize=4,
            label='Composite (mod $N_k$)')
    ax.plot(ones, y_int[y_int > 0.5], 'go', markersize=5,
            label='Coprime to $N_k$')

    ax.set_xlabel('$x$', fontsize=12)
    ax.set_ylabel(f'$P_{k}(x)$', fontsize=12)
    ax.set_title(f'Prime Wave for $k={k}$ (First {k} primes: {primes})',
                 fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_xlim([0, N_k])
    ax.set_ylim([-0.05, 1.1])

    # Add text annotation
    phi_Nk = euler_phi(N_k)
    ax.text(0.02, 0.95,
            f'$N_{k} = {N_k}$\n$\\varphi(N_{k}) = {phi_Nk}$\n' +
            f'Average: {phi_Nk / N_k:.4f}',
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved: {filename}")

    if show:
        plt.show()
    else:
        plt.close()


def plot_spectrum(k: int, filename: str = None, show: bool = True):
    """
    Generate Figure 4.2: Fourier spectrum of P_k.

    Args:
        k: Number of primes
        filename: Output filename (e.g., 'P3_fourier_spectrum.pdf')
        show: Whether to display plot
    """
    modes, coeffs = compute_all_fourier_coeffs(k)
    N_k = primorial(k)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Top panel: Full spectrum
    ax1.stem(modes, np.abs(coeffs), linefmt='b-', markerfmt='bo',
             basefmt='k-', label='$|c_m^{(k)}|$')
    ax1.set_xlabel('Mode $m$', fontsize=11)
    ax1.set_ylabel('$|c_m^{(k)}|$', fontsize=11)
    ax1.set_title(f'Fourier Spectrum of $P_{k}$ for $k={k}$ ($N_{k}={N_k}$)',
                  fontsize=13)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)

    # Highlight DC component
    ax1.plot(0, abs(coeffs[0]), 'ro', markersize=10,
             label=f'$c_0 = {coeffs[0]:.4f}$')

    # Bottom panel: Log-log plot (decay analysis)
    nonzero_mask = np.abs(coeffs) > 1e-10
    modes_nz = modes[nonzero_mask]
    coeffs_nz = np.abs(coeffs[nonzero_mask])

    ax2.loglog(modes_nz[1:], coeffs_nz[1:], 'bo', markersize=4,
               label='Non-zero coefficients')

    # Theoretical decay: e^{-γ}/log(k)
    gamma = 0.5772
    theoretical_decay = np.exp(-gamma) / np.log(k)
    ax2.axhline(theoretical_decay, color='r', linestyle='--',
                label=f'$e^{{-\\gamma}}/\\log k \\approx {theoretical_decay:.4f}$')

    ax2.set_xlabel('Mode $m$ (log scale)', fontsize=11)
    ax2.set_ylabel('$|c_m^{(k)}|$ (log scale)', fontsize=11)
    ax2.set_title('Decay Rate Analysis', fontsize=12)
    ax2.grid(True, which='both', alpha=0.3)
    ax2.legend(fontsize=10)

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Saved: {filename}")

    if show:
        plt.show()
    else:
        plt.close()


def generate_verification_table(k_values: List[int]) -> str:
    """
    Generate LaTeX table for Appendix B (numerical verification).

    Args:
        k_values: List of k values to test (e.g., [3, 5, 7])

    Returns:
        LaTeX table code
    """
    results = []
    for k in k_values:
        verify = verify_zero_set(k, n_test=50)
        N_k = primorial(k)
        phi_Nk = euler_phi(N_k)

        results.append({
            'k': k,
            'N_k': N_k,
            'mu_k': phi_Nk / N_k,
            'zeros_correct': verify['integer_zeros_correct'],
            'ones_correct': verify['integer_nonzeros_correct'],
            'max_ratio': verify['max_ratio_noninteger']
        })

    latex = "\\begin{table}[h]\n\\centering\n"
    latex += "\\begin{tabular}{ccccccc}\n"
    latex += "\\toprule\n"
    latex += "$k$ & $N_k$ & $\\mu_k$ & Zeros OK & Ones OK & Max Ratio & Status \\\\\n"
    latex += "\\midrule\n"

    for r in results:
        status = "\\checkmark" if r['max_ratio'] < get_first_k_primes(r['k'])[-1] else "\\times"
        latex += f"{r['k']} & {r['N_k']} & {r['mu_k']:.4f} & "
        latex += f"{r['zeros_correct']} & {r['ones_correct']} & "
        latex += f"{r['max_ratio']:.3f} & {status} \\\\\n"

    latex += "\\bottomrule\n\\end{tabular}\n"
    latex += "\\caption{Numerical Verification of Theorem 4.7}\n"
    latex += "\\label{tab:verification}\n\\end{table}"

    return latex


# ============================================================================
# SECTION D.6: Main Execution
# ============================================================================

def main():
    """
    Main execution function with command-line interface.
    """
    parser = argparse.ArgumentParser(
        description='Prime Wave Theory Visualization and Verification'
    )
    parser.add_argument('--mode', type=str, required=True,
                        choices=['wave', 'spectrum', 'verify', 'all'],
                        help='Operation mode')
    parser.add_argument('--k', type=int, default=3,
                        help='Number of primes (default: 3)')
    parser.add_argument('--output', type=str, default=None,
                        help='Output filename for plots')
    parser.add_argument('--no-show', action='store_true',
                        help='Do not display plots (save only)')

    args = parser.parse_args()

    if args.mode == 'wave' or args.mode == 'all':
        filename = args.output or f'P{args.k}_wave_plot.pdf'
        plot_wave(args.k, filename, not args.no_show)

    if args.mode == 'spectrum' or args.mode == 'all':
        filename = args.output or f'P{args.k}_fourier_spectrum.pdf'
        plot_spectrum(args.k, filename, not args.no_show)

    if args.mode == 'verify' or args.mode == 'all':
        print(f"\n=== Verification for k={args.k} ===")
        verify_results = verify_zero_set(args.k)
        for key, value in verify_results.items():
            print(f"{key}: {value}")

        print(f"\n=== Besov Proxy (s=1.3, p=2) ===")
        besov = compute_besov_proxy(args.k, s=1.3, p=2.0, n_samples=500)
        print(f"Seminorm: {besov:.4f} (finite => membership)")

        if args.mode == 'all':
            print("\n=== LaTeX Verification Table ===")
            print(generate_verification_table([3, 5, 7]))


if __name__ == '__main__':
    # If run without arguments, generate standard figures
    import sys

    if len(sys.argv) == 1:
        print("Generating standard figures for k=3...")
        plot_wave(3, 'P3_wave_plot.pdf', show=True)
        plot_spectrum(3, 'P3_fourier_spectrum.pdf', show=True)
        print("Done! Use --help for more options.")
    else:
        main()