#!/usr/bin/env python3
"""
Generate publication-quality figures for the Gap Compression paper.

Figure 1: Convergence of S(Q) as a function of the prime bound.
Figure 2: Gap compression effect at n = 10^10000.

Reads data/convergence.csv and produces figures/*.pdf.

Author: Ruqing Chen
Repository: https://github.com/Ruqing1963/Q47-GapCompression
"""

import csv
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def load_convergence(path="data/convergence.csv"):
    """Load convergence data from CSV."""
    primes, partials = [], []
    with open(path) as f:
        for row in csv.reader(f):
            if row[0].startswith('#') or row[0] == 'prime_p':
                continue
            primes.append(int(row[0]))
            partials.append(float(row[3]))
    return np.array(primes), np.array(partials)


def figure1_convergence(primes, partials):
    """Figure 1: Convergence of S(Q)."""
    fig, ax = plt.subplots(figsize=(10, 5.5))

    ax.plot(primes, partials, color='teal', lw=1.2,
            label=r'$\mathfrak{S}_Q(X) = \prod_{p \leq X}'
                  r' \frac{1-\omega(p)/p}{1-1/p}$')
    ax.axhline(y=partials[-1], color='red', ls='--', lw=1, alpha=0.7,
               label=f'Asymptotic $\\approx {partials[-1]:.2f}$')

    # Annotate first drop
    idx283 = np.searchsorted(primes, 283)
    ax.annotate('First Drop\n$p=283$\n($\\omega=46$)',
                xy=(283, partials[idx283]),
                xytext=(6000, 10.3), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='black', lw=0.8))
    ax.annotate('Rapid Rise (Shielding Primes $\\omega=0$)',
                xy=(50, 2.5), fontsize=9, color='teal',
                bbox=dict(boxstyle='round,pad=0.3', fc='white',
                          ec='teal', alpha=0.8))

    ax.set_xlabel('Prime $p$', fontsize=12)
    ax.set_ylabel('Partial Product', fontsize=12)
    ax.set_title(r'Figure 1: Convergence of the Singular Series'
                 r' $\mathfrak{S}_Q$', fontsize=13)
    ax.legend(fontsize=10, loc='right')
    ax.set_xlim(0, 100000)
    ax.set_ylim(1.5, 11)
    ax.grid(True, alpha=0.2)
    plt.tight_layout()

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/figure1_convergence.pdf", dpi=300,
                bbox_inches='tight')
    print("Figure 1 saved to figures/figure1_convergence.pdf")
    plt.close()


def figure2_stress():
    """Figure 2: Gap compression at n = 10^10000."""
    ln_x = 10000 * np.log(10)  # ≈ 23026

    fig, ax = plt.subplots(figsize=(10, 5.5))
    H = np.linspace(0, 1.3e6, 1000)

    E_titan = (8.70 / 46) * H / ln_x
    E_generic = (1.0 / 46) * H / ln_x
    E_int = (1.0 / 1) * H / ln_x

    ax.plot(H, E_titan, color='blue', lw=2,
            label=r'Titan Poly ($d=46, \mathfrak{S}=8.70$)')
    ax.plot(H, E_generic, color='gray', lw=2, ls='--',
            label=r'Generic Poly ($d=46, \mathfrak{S}=1$)')
    ax.plot(H, E_int, color='green', lw=1.5, ls=':', alpha=0.7,
            label=r'Integers ($d=1$)')
    ax.axhline(y=1, color='red', ls='-', lw=1, alpha=0.5,
               label='Threshold $E=1$')

    H_titan = 46 * ln_x / 8.70
    H_generic = 46 * ln_x / 1.0
    ax.plot(H_titan, 1, 'bo', ms=8, zorder=5)
    ax.plot(H_generic, 1, 'o', color='gray', ms=8, zorder=5)
    ax.annotate(f'$H={H_titan/1e3:.0f}\\!\\times\\!10^3$',
                xy=(H_titan, 1), xytext=(H_titan - 1e5, 3),
                fontsize=9, color='blue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=0.8))
    ax.annotate(f'$H={H_generic/1e6:.2f}\\!\\times\\!10^6$',
                xy=(H_generic, 1), xytext=(H_generic - 2.5e5, 3),
                fontsize=9, color='gray',
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.8))

    ax.set_xlabel('Search Window Size $H$', fontsize=12)
    ax.set_ylabel('Expected Number of Primes', fontsize=12)
    ax.set_title(r'Figure 2: Prime Gap "Compression" at $n = 10^{10000}$',
                 fontsize=13)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlim(0, 1.3e6)
    ax.set_ylim(0, 55)
    ax.grid(True, alpha=0.2)
    plt.tight_layout()

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/figure2_stress.pdf", dpi=300,
                bbox_inches='tight')
    print("Figure 2 saved to figures/figure2_stress.pdf")
    plt.close()


def main():
    primes, partials = load_convergence()
    figure1_convergence(primes, partials)
    figure2_stress()


if __name__ == "__main__":
    main()
